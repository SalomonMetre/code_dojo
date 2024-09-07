#include <iostream>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()
#include <unistd.h> // For the sleep() function. You won't need this in the actual implementation

#define MIN 1
#define MAX 5
#define AVG_REFR 5

int main(){
    // Seed initialization for random numbers
    std::srand(std::time(0));
    double sum = 0.0, avg = 0.0;
    int count = 0;
    double measurement;
    
    while(true){
        sleep(2); // used only for simulation purposes. You won't need it.

        // Generating the measurement using random numbers
        // TODO: here you will have to get the actual measurement from your instrument
        double random_number = static_cast<double>(std::rand()) / RAND_MAX;
        measurement = MIN + random_number * (MAX - MIN);

        // core logic
        count++;
        sum += measurement;

        if(count % AVG_REFR == 0){
            avg = sum / count;
            std::cout << "Average is : " << avg << std::endl;
        }
    }

    return 0;
}
