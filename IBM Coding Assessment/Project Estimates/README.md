A number of bids are received for a project.  Determine the number of distinct pairs of project costs where their absolute difference is some target value.  Two pairs are distinct if they differ in at least one value.

Example
n=3
projectCosts = [1, 3, 5]
There are 2 pairs [1,3], [3,5] with the target difference target = 2. Therefore 2  is returned.


Function Description 
countPairs has the following parameter(s):
     int projectCosts[n]:  array of integers
     int target: the target difference

Return
int: the number of distinct pairs in projectCosts with an absolute  difference of target

Constraints
5 ≤ n ≤ 10^5
0 < projectCosts[i] ≤ 2 × 10^9
Each projectCosts[i] is distinct, i.e. unique within projectCosts
1 ≤target ≤ 10^9
