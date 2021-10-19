class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int sz=nums.size();
        if(sz>0){
        int fl=nums[0];
        for(int i=1;i<nums.size();i++){
            if((nums[i]==fl)){nums[i]=100000;sz--;}
            if(nums[i]!=100000)fl=nums[i];
        }
        sort(nums.begin(),nums.end());}
        return sz;
    }
};
