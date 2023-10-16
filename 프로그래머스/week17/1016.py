def solution(record_list):
    answer = []
    user_dict = {}
    records = []
    
    for record in record_list:       
        split_record = record.split()
        
        if split_record[0] != "Leave":
            user_dict[split_record[1]] = split_record[2]
            
        if split_record[0] in {"Enter", "Leave"}:
            records.append((split_record[1], split_record[0]))
            
    for record in records:
        user = user_dict[record[0]]
        if record[1] == "Enter":
            answer.append(f"{user}님이 들어왔습니다.")
        elif record[1] == "Leave":
            answer.append(f"{user}님이 나갔습니다.")
    
    return answer
