package main

import (
	"benchmark/genproto"
	"encoding/json"
	"fmt"
	"math/rand"
	"time"

	"github.com/golang/protobuf/proto"
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

	productVector := ProductVector{Id: 1, Vector: vector}
	N := 1000

	start_time := time.Now()
	for i := 0; i < N; i++ {
		json.Marshal(&productVector)
	}
	end_time := time.Now()
	fmt.Println("json marshal time:", end_time.Sub(start_time))

	marshalData, _ := json.Marshal(&productVector)
	var jsonProductVector ProductVector
	start_time = time.Now()
	for i := 0; i < N; i++ {
		json.Unmarshal(marshalData, &jsonProductVector)
	}
	end_time = time.Now()
	fmt.Println("json unmarshal time:", end_time.Sub(start_time))

	start_time = time.Now()
	productVector2 := genproto.ProductVector{Id: 1, Vector: vector}
	for i := 0; i < N; i++ {
		proto.Marshal(&productVector2)
	}
	end_time = time.Now()
	fmt.Println("protobuf marshal time:", end_time.Sub(start_time))

	marshalData, _ = proto.Marshal(&genproto.ProductVector{Id: 1, Vector: vector})
	var protoProductVector genproto.ProductVector
	start_time = time.Now()
	for i := 0; i < N; i++ {
		proto.Unmarshal(marshalData, &protoProductVector)
	}
	end_time = time.Now()
	fmt.Println("protobuf unmarshal time:", end_time.Sub(start_time))
}
