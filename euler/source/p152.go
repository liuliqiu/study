package main

import "fmt"

func find_sum(target uint64, numbers []uint64, sum_numbers uint64) (int) {
    if target > sum_numbers {
        return 0
    } else if target < 0 {
        return 0
    } else if target == sum_numbers {
        return 1
    } else {
        first := numbers[0]
        last := numbers[1:]
        x := find_sum(target, last, sum_numbers - first)
        y := find_sum(target - first, last, sum_numbers - first)
        return x + y
    }
}

// 55  8    17.214s
// 60  34   59.211s
// 65  53   325.010s

func main() {
    const limit = 55
    var x uint64 = 302702400 * 302702400
    var target uint64 = x / 4
    count := 0
    var numbers [limit]uint64
    for n := 3; n <= limit; n++ {
        if x % uint64(n) == 0 {
            numbers[count] = x / uint64(n * n)
            count += 1
        }
    }
    var sum_numbers uint64 = 0
    for _, n := range numbers {
        sum_numbers += n
    }
    fmt.Println(find_sum(target, numbers[:count], sum_numbers))
}
