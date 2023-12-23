                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            else:
                x -= 1
            if [x,y] in ref_list:
                return True
            else:
                ref_list.append ([x,y])
        return False
        
"
