/*
8 ms
Beats 80.21% of users with C++
13.16 MB 
Beats 35.24% of users with C++
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // create a new vector of num-index pairs
        size_t len = nums.size();
        vector<pair<int, int>> v;
        v.reserve(len); // avoiding copying elements by specifying size at outset
        for (int i = 0; i < len; i++)
        {
            v.push_back(make_pair(nums[i], i)); // pushing back becomes O(1) operation with specified vector size
        }

        // sort new vector
        sort(v.begin(), v.end(), [](pair<int, int> a, pair<int, int> b) {return a.first < b.first;});

        // iterate through pairs in ascending order
        for (int i = 0; i < len; i++)
        {
            // binary search entire vector for target - current num
            int curr_num = v[i].first;
            vector<pair<int, int>>::iterator idx = lower_bound(v.begin(), v.end(), target - curr_num, [](pair<int, int> a, int e) {return a.first < e;});
                // return current num and iterator if:
                // - iterator points to an actually existing element
                // - iterator points to exact complement of current num
                // - iterator doesn't point to current num
                // note: If idx == v.end(), idx->first results in an error. 
                //       That's why idx != v.end() is checked first.
                if (idx != v.end() && idx->first == target - curr_num && idx - v.begin() != i)
                    return vector<int> {v[i].second, idx->second};
            
        }

        // "error" return value
        return vector<int> {100, 100};    
    }
};
