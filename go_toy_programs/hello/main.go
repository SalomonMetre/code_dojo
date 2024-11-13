package main
import "fmt"

func isEven(number int) (bool,error){
	if number <= 0 {
		return false, fmt.Errorf("error : n must be > 0")
	}
	return number % 2 == 0, nil
}


func main(){
	var x int
	x = 43
	result, err := isEven(x)
	if err != nil {
		fmt.Println(err)
	} else{
		fmt.Println("Is",x,"even?\n-->",result)
	}
}
