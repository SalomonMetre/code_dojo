#include <iostream>

int main(){
    double num1, num2;
    std::cout<<"Enter the first number : "<<std::endl;
    std::cin >> num1;
    std::cout<<"Enter the second number : "<<std::endl;
    std::cin >> num2;
    std::cout<<"Sum : "<<num1 + num2<<", difference : "<<num1 - num2<<", product : "<<num1 * num2;
    if (num2 != 0) {
        std::cout<<", quotient : "<<num1 / num2<<std::endl;
    }

}