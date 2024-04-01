package kata

import "strings"

func Points(games []string) int {
	result := 0
	for _, v := range games {
		if strings.Split(v, ":")[0] > strings.Split(v, ":")[1] {
			result += 3
		} else if strings.Split(v, ":")[0] == strings.Split(v, ":")[1] {
			result += 1
		}
	}
	return result
}
