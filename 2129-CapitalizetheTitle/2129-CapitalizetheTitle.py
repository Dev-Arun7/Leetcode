        for i, word in enumerate(title_list):
            if len(word) < 3:
                # Keep short words in lowercase
                result += word.lower()
            else:
                # Capitalize longer words
                result += word.capitalize()

            # Add space if it's not the last word
            if i < len(title_list) - 1:
                result += " "

        return result


        title_list = title.split()
"
