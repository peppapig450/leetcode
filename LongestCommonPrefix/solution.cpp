class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.empty())
            return "";

        // Min_element with custom comparator to find the shortest string
        string minStr = *min_element(strs.begin(), strs.end(),
                                     [](const string &a, const string &b)
                                     {
                                         return a.size() < b.size();
                                     });

        for (int i = 0; i < minStr.size(); ++i)
        {
            char c = minStr[i];
            for (int j = 0; j < strs.size(); ++j)
            {
                if (strs[j][i] != c)
                {
                    return minStr.substr(0, i);
                }
            }
        }

        return minStr;
    }
};