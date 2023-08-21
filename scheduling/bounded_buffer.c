//producer
do{
    //produce an item in x

    P(empty);
    P(mutex);

    //add x to buffer

    V(mutex);
    V(full);
}while(1);

//consumer
do{
    P(full);
    P(mutex);
    
    //remove an item form buffer to y

    V(mutex);
    V(empty);

    //consume the item in y
}while(1);