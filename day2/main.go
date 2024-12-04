package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
	"math"
	"fmt"
)

func readInput() [][]int {
	var reports [][]int

	file, _ := os.Open("./inputs/input2.txt")
	
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		strNumbers := strings.Fields(line)
		var intNumbers []int
		for _, str := range strNumbers {
			num, _ := strconv.Atoi(str)
			intNumbers = append(intNumbers, num)
		}
		reports = append(reports, intNumbers)
	}

	return reports
}

func checkSorted(report []int) bool {
	isAsc := sort.IntsAreSorted(report)

	isDesc := true

	for i := 1; i < len(report); i++ {
		if report[i] > report[i-1]{
			isDesc = false
		}
	}

	return isAsc || isDesc
} 

func checkDifference(report []int) bool {
	valid := true

	for i := 0; i < len(report) - 1; i++ {
		if  1 > math.Abs(float64(report[i]-report[i+1])) || math.Abs(float64(report[i]-report[i+1])) > 3 {
			valid = false
			break
		} 
	}
	return valid
}

func isStrictlySafe(report []int) bool {
	return checkSorted(report) && checkDifference(report)
}

func countSafeReports(reports [][]int) int {
	sum := 0
	for i := 0; i < len(reports); i++ {
		if isStrictlySafe(reports[i]){
			sum += 1
		}
	}
	return sum
}

func removeAtIndex(arr []int, index int) []int {
	newArr := make([]int, len(arr)-1)
	copy(newArr, arr[:index])
	copy(newArr[index:], arr[index+1:])
	return newArr
}


func countCanBeSafeReports(reports [][]int) int {
	sum := 0

	for i := 0; i < len(reports); i++ {
		if !isStrictlySafe(reports[i]){
			for j:=0; j < len(reports[i]); j++ {
				report_no_level := removeAtIndex(reports[i], j)
				if isStrictlySafe(report_no_level){
					sum += 1
					break
				}
			}
		}
	}
	return sum
}


func main() {
	reports := readInput()
	fmt.Println(countSafeReports(reports))
	fmt.Println(countSafeReports(reports)+ countCanBeSafeReports(reports))
}