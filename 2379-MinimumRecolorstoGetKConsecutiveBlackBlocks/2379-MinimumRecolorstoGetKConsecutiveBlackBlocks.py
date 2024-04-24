        for i in range(k):
            if blocks[i] == "W":
                window_count += 1

        ans = window_count

        while right < l:
            if blocks[right] == 'W':
                window_count += 1
            if blocks[left] == 'W':
                window_count -= 1
            left += 1
            ans = min(ans, window_count)
            right += 1

            right += 1
        return ans
        
        ans = k
        l = len(blocks)
"
