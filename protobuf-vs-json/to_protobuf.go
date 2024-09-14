package main

import (
	"math/rand"
	"os"

	"github.com/golang/protobuf/proto"

	"benchmark/genproto"
)

func main() {
	vectorSize := 768
	vector := make([]float64, vectorSize)
	for i := 0; i < vectorSize; i++ {
		vector[i] = rand.Float64()
	}
	data, _ := proto.Marshal(&genproto.ProductVector{Id: 1, Vector: vector})
	os.WriteFile("/tmp/data.bin", data, 0644)
}
