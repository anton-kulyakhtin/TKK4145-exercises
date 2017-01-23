// gcc 4.7.2 +
// gcc -std=gnu99 -Wall -g -o helloworld_c helloworld_c.c -lpthread

#include <pthread.h>
#include <stdio.h>

static int i;

pthread_mutex_t lock;

void* increase_i(void* total_steps){
	
	int* total = (int* )total_steps;
	
	for(int k=0;k<(*total);k++){
		pthread_mutex_lock(&lock);
    	i++; 
		pthread_mutex_unlock(&lock);
    	//printf("%d \n",i);
    }
    return NULL;
}

void* decrease_i(void* total_steps){
	int* total = (int* )total_steps;
    for(int k=0;k<((*total)+2);k++){
    	pthread_mutex_lock(&lock); // quesiton regarding locking only in one thread
    	i--; 
		pthread_mutex_unlock(&lock);
    	//printf("%d \n",i);
 	}
    return NULL;
}

int main(){
	
	i=0;
	int total_steps=1000000;
	
    pthread_t Thread_inc;
    pthread_t Thread_dec;
    
	if (pthread_mutex_init(&lock, NULL) != 0)
    {
        printf("\n mutex init failed\n");
        return 1;
    }
	
    pthread_create(&Thread_inc, NULL, increase_i, &total_steps);
    // Arguments to a thread would be passed here ---------^
    
    pthread_create(&Thread_dec, NULL, decrease_i, &total_steps);
    // Arguments to a thread would be passed here ---------^
    
    pthread_join(Thread_inc, NULL);
    pthread_join(Thread_dec, NULL);
    
    printf("%d \n",i);
	pthread_mutex_destroy(&lock);
    //printf("Hello from main!\n");
    return 0;
    
}


/**


// Note the return type: void*
void* someThreadFunction(){
    printf("Hello from a thread!\n");
    return NULL;
}



int main(){
    pthread_t someThread;
    pthread_create(&someThread, NULL, someThreadFunction, NULL);
    // Arguments to a thread would be passed here ---------^
    
    pthread_join(someThread, NULL);
    printf("Hello from main!\n");
    return 0;
    
}
**/