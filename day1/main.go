package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sort"
	"math"
)

func read_input() ([]int, []int){
	var list1, list2 []int

	file, err := os.Open("./inputs/input1.txt")
	if err != nil {
		fmt.Println("Failed to open file:", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		numbers := strings.Fields(line)

		num1, err1 := strconv.Atoi(numbers[0])
		num2, err2 := strconv.Atoi(numbers[1])

		if err1 != nil || err2 != nil {
			fmt.Println("Error parsing line", line)
			continue
		}

		list1 = append(list1, num1)
		list2 = append(list2, num2)
	}

	return list1, list2
}

func calculate_distance(list1 []int, list2 []int) int {
	sort.Ints(list1)
	sort.Ints(list2)

	sum := 0
	for i, val := range list1 {
		sum += int(math.Abs(float64(val-list2[i])))
	}
	return sum
}

func calculate_similarity(list1 []int, list2 []int) int {
	similarity := 0
	counts := make(map[int]int)

	for _, n := range list2 {
		counts[n]++
	}

	for _, n := range list1 {
		similarity += n * counts[n]
	}
	return similarity
}
func main() {
	list1, list2 := read_input()
	//list3 := []int{3, 4, 2, 1, 3, 3}
	//list4 := []int{4, 3, 5, 3, 9, 3}
	fmt.Println(calculate_distance(list1,list2))
	fmt.Println(calculate_similarity(list1,list2))
}
