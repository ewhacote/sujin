//Synchronization variable
boolean_lock = false;

//process P1
do{
    while(Test_and_Set(lock));
    //critical section
    lock = false;
    //remainder section
}