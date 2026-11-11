def generate_statistics(content, file_type):
    
        if file_type == 'TXT' or file_type == 'PDF':
            statistics = {'character_count' : len(content),
                          'word_count' : len(content.split()),
                          'line_count' : len(content.splitlines())}
        
        elif file_type == 'CSV':
            statistics = {'row_count' : len(content)-1,
                          'column_count' : len(content[0])}
        
        elif file_type == 'JSON':
            if isinstance(content,dict):
                statistics = {'key_count' : len(content)}

            elif isinstance(content,list):
                statistics = {'element_count' : len(content)}

            else:
                 raise ValueError("Unsupported JSON content!")

        else :
            raise ValueError("Invalid file type!")
        return statistics
   
    