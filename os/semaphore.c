
while (s<=0); //자원이 없으면 기다린다
s--; //자원을 획득한다

s++; //자원을 반납한다

//bock & wakeup
typedef struct{
    int value; //semaphore
    struct process *L; //process wait queue
}semaphore;

//new p operation
S.value--; //prepare to enter
if (S.value<0){
    add this process to S.L;
    block();
}

//new v operation
S.value++; //prepare to enter
if (S.value<=0){
    remove a process P from S.L;
    wakeup(P);
}