reports = []

with open('./inputs/input2.txt', 'r') as file: 
    for line in file:
        reports.append(list(map(int, line.split())))

def check_sorted(report):
    return sorted(report) == report or sorted(report, reverse=True) == report

def check_difference(report):
    return all(0 < abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))

def is_strictly_safe(report):
    return check_difference(report) and check_sorted(report)

def count_safe_reports(reports):
    safe_or_not = [is_strictly_safe(report) for report in reports]
    return sum(safe_or_not)
       
print(count_safe_reports(reports))

################## Part 2 ###################


def check_almost_sorted(report):
    def safe_if_almost_sorted(report, sorted_report):
        for i in range(len(report)):
            if report[i] != sorted_report[i]:
                report_no_x = report.copy()
                report_no_x.pop(i)
                report_no_y = report.copy()
                report_no_y.pop(i)
                if is_strictly_safe(report_no_x) or is_strictly_safe(report_no_y):
                    return True
        return False

    strictly_sorted = check_sorted(report)
    if strictly_sorted == False:
        return safe_if_almost_sorted(report, sorted(report)) or safe_if_almost_sorted(report, sorted(report, reverse=True))
    return False

def check_almost_safe_differences(report):
    def offending_indices(report):
        offences = []
        for i in range(len(report)-1):
            if not(0 < abs(report[i] - report[i+1]) <= 3):
                offences.append((i, i+1))
        return offences
    
    offences = offending_indices(report)
    if len(offences) == 1:
        x, y = offences[0]
        report_no_x = report.copy()
        report_no_x.pop(x)
        report_no_y = report.copy()
        report_no_y.pop(y)
        return is_strictly_safe(report_no_x) or is_strictly_safe(report_no_y)
    return False

def count_kinda_safe_reports(reports):
    safe_or_not = []
    for report in reports:
        kinda_safe = check_almost_sorted(report) or check_almost_safe_differences(report)
        safe_or_not.append(kinda_safe)
    return sum(safe_or_not)


########### Naive solution ##################

def brute_force(reports):
    kinda_safe = 0
    for report in reports:
        if not is_strictly_safe(report):
            for i, _ in enumerate(report):
                report_no_level = report.copy()
                report_no_level.pop(i)
                if is_strictly_safe(report_no_level):
                    kinda_safe += 1
                    break
    return kinda_safe


print(count_safe_reports(reports) + count_kinda_safe_reports(reports))
print(count_safe_reports(reports) + brute_force(reports))