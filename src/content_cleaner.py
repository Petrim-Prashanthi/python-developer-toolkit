
def clean_txt(content):
    return content.strip()

def clean_csv(content):
    cleaned_content = []
    for row in content:
        cleaned_row = []
        for c in row:
            cleaned_row.append(c.strip())
        cleaned_content.append(cleaned_row)
    return cleaned_content

def clean_json(content):
    if isinstance(content, dict):
        clean_dict = {}
        for i,j in content.items():
            clean_dict[i] = clean_json(j)
        return clean_dict
    elif isinstance(content,list):
        clean_list = []
        for i in content:
            clean_list.append(clean_json(i))
        return clean_list
    elif isinstance(content,str):
        return content.strip()
    else:
        return content

def clean_pdf(content):
    if isinstance(content,str):
        return content.strip()
    else:
        return content
             