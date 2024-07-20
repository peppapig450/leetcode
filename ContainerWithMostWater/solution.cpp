class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(NULL);
        std::cout.tie(NULL);

        int left = 0;
        int right = height.size() - 1;
        int max_area = 0;

        while (left < right)
        {
            int width = right - left;
            int current_height = std::min(height[left], height[right]);
            int current_area = width * current_height;

            max_area = std::max(max_area, current_area);

            if (height[left] < height[right])
            {
                ++left;
            }
            else
            {
                --right;
            }
        }

        return max_area;
    }
};