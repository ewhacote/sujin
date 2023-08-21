//shared data
int readcount = 0;
DB 자체;

//synchronization variables
semaphore mutex = 1;
db = 1;

//writer
P(db);
//writing DB is performed
V(db);

//reader
P(mutex);
readcount++;

if(readcount==1){
    P(db);
}
V(mutex);

//reading DB is performed

P(mutex);
readcount--;

if(readcount==0){
    V(db);
}
V(mutex)