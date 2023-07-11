from heapq import heappush, heappop

def toMin(string):
    h,m = map(int,string.split(":"))
    return h*60+m

def solution(book_time):
    book_time.sort(key = lambda x : x[0])
    heap=[]
    for s,e in book_time:
        check_in, check_out = toMin(s), toMin(e)+10
        if len(heap)!=0 and heap[0]<=check_in:
            heappop(heap)
        heappush(heap,check_out)      
    return len(heap)
