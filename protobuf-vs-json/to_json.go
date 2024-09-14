package main

import (
	"encoding/json"
	"math/rand"
	"os"
)

type ProductVector struct {
	Id     int64
	Vector []float64
}

func main() {
	vectorSize := 768
	vector := make([]float64, vectorSize)
	for i := 0; i < vectorSize; i++ {
		vector[i] = rand.Float64()
	}
	json_data, _ := json.Marshal(&ProductVector{Id: 1, Vector: vector})
	os.WriteFile("/tmp/data.json", json_data, 0644)
}
