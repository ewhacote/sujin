
from collections import Counter
def solution(s):
    s= s.replace('{','') # 괄호 제거
    s= s.replace('}','')
    s = list(map(int, s.split(','))) # ,으로 숫자 구분
    number_dict = Counter(s) # ~갯수 셈
    
    # 가장 많이 언급된 순서대로 key 저장
    return [k for k, v in number_dict.most_common(len(number_dict))]