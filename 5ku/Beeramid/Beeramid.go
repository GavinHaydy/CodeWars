package kata

func Beeramid(bonus int, price float64) int {
	// your code here
	r := 0
	for i := 0; i < bonus*100/(int(price*100)); i++ {
		r += i * i
		if bonus*100/(int(price*100)) < r {
			return i - 1
		} else if bonus*100/(int(price*100)) == r {
			return i
		}
	}
	if bonus == int(price) {
		return 1
	}
	return 0
}

/*	best
package kata


func Beeramid(bonus int, price float64) (row int) {
	cans := int(float64(bonus) / price)
	for cans > 0 {
		cans = cans - row*row
		if cans >= (row+1)*(row+1) {
			row++
		}
	}
	return row
}
*/
