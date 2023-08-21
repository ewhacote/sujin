chopstick[5]; //semaphore

do{
    P(chopstick[i]);
    P(chopstick[(i+1)%5]);

    eat();

    V(chopstick[i]);
    V(chopstick[(i+1)%5]);

    think();
}while(1);