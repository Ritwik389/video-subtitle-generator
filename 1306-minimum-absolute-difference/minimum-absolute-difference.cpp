class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        int mindiff = INT_MAX;
        sort(arr.begin(), arr.end());
        vector<vector<int>> ans;
        for(int i =0; i<arr.size()-1; i++){
            mindiff = min(mindiff, arr[i+1]-arr[i]);
        }
        for(int i =0; i<arr.size()-1; i++){
            int diff = arr[i+1] - arr[i];
            if(diff == mindiff) ans.push_back({arr[i], arr[i+1]});
        }
        return ans;






        }

        
};