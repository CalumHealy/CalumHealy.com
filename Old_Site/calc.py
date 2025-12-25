# First Semester
Cit = 65
ComputerArchitecture = 71
WebDev = 55
ProgrammingFundamentals = 59
ComputerSecurityPrinciples = 57
MathsForComputerScience = 64

# Second Semester
DiscreteMaths = 57
ModularProgramming = 69
NetworkingFundamentals = 43
IntroductionToDatabases = 54
OperatingSystemsInPractise = 46
PhysicalComputing = 72

# Third Semester
RequirementsEngineering = 61
ObjectOrientedPrinciples = 41
OperatingSystems = 47
MathematicalExplorations = 79
LinearDataStructuresAndAlgorithms = 43
DatabaseDesign = 71

# Fourth Semester
ObjectOrientedProgramming = 48
ObjectOrientedAnalysisAndDesign = 35
NoSQLDataArchitectures = 42
CProgramming = 51
NonLinearDataStructuresAndAlgorithms = 55
ProbabilityAndStatistic = 43

# Fifth Semester
GroupProject = 61
DistributedSystemsProgramming = 53
AdvancedWebPublishingApps = 54
ProgrammingMobileDevices = 58
AgileProcesses = 59
ProgrammingForDataAnalytics = 28

FirstSemesterAverage = (Cit + ComputerArchitecture + WebDev + ProgrammingFundamentals + ComputerSecurityPrinciples + MathsForComputerScience) / 6
print(f"First Semester: {FirstSemesterAverage:.2f}%")

SecondSemesterAverage = (DiscreteMaths + ModularProgramming + NetworkingFundamentals + IntroductionToDatabases + OperatingSystemsInPractise + PhysicalComputing) / 6
print(f"Second Semester: {SecondSemesterAverage:.2f}%")

ThirdSemesterAverage = (RequirementsEngineering + ObjectOrientedPrinciples + OperatingSystems + MathematicalExplorations + LinearDataStructuresAndAlgorithms + DatabaseDesign) / 6
print(f"Third Semester: {ThirdSemesterAverage:.2f}%")

FourthSemesterAverage = (ObjectOrientedProgramming + ObjectOrientedAnalysisAndDesign + NoSQLDataArchitectures + CProgramming + NonLinearDataStructuresAndAlgorithms + ProbabilityAndStatistic) / 6
print(f"Fourth Semester: {FourthSemesterAverage:.2f}%")

FifthSemesterAverage = (GroupProject + DistributedSystemsProgramming + AdvancedWebPublishingApps + ProgrammingMobileDevices + AgileProcesses + ProgrammingForDataAnalytics) / 6
print(f"Fifth Semester: {FifthSemesterAverage:.2f}%")

TotalAverage = (FirstSemesterAverage + SecondSemesterAverage + ThirdSemesterAverage + FourthSemesterAverage + FifthSemesterAverage) / 5
print(f"Total Average: {TotalAverage:.2f}%")
