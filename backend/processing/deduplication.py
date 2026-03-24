def deduplicate(data):
    seen=set() 
    unique_data=[]

    for item in data:
        key=item.get('title',' ') + item.get('source',' ')

        if key not in seen:
            seen.add(key)
            unique_data.append[item]
         
    return unique_data