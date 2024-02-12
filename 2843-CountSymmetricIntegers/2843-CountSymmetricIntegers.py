            
            left_sum = 0
            right_sum = 0
            
            for i in range(num_len // 2):
                left_sum += int(num_str[i])
                right_sum += int(num_str[num_len - 1 - i])
            
            # If both halves have the same sum, the number is symmetric
            if left_sum == right_sum:
                count += 1
        
        return count

1
