package main

import (
	"fmt"
	"log"
	"math/rand"
	"time"
)

// seed to ensure pseudo randomness
var seededRand *rand.Rand = rand.New(
	rand.NewSource(time.Now().UnixNano()))

// define a dice roll
func roll(sides int) int {
	min, max := 1, sides
	roll := min + seededRand.Intn(max-min+1)
	return roll
}

// update a set of unique rolls
func updateUniqueRolls(roll int, unique_rolls map[int]bool) map[int]bool {
	_, true := unique_rolls[roll]
	if !true {
		unique_rolls[roll] = true // add new unique roll
	}
	return unique_rolls
}

// keep rolling until every unique number is rolled
func main() {
	var sides int = 10000
	log.Printf("rolling a %v sided dice\n", sides)
	unique_rolls := map[int]bool{}
	i := 1
	for len(unique_rolls) < sides {
		var roll int = roll(sides)
		fmt.Println("rolled a", roll)
		unique_rolls = updateUniqueRolls(roll, unique_rolls)
		i += 1
	}
	log.Printf("got %v unique rolls in %v attempts \n", len(unique_rolls), i)
}
