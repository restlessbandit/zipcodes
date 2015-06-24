package main
 
import (
    "fmt"
    "math"
)
 
type location struct {
    lat float64 // latitude, radians
    long float64 // longitude, radians
}
 
func deg2rad(lat, long float64) location {
    return location{lat * math.Pi / 180, long * math.Pi / 180}
}
 
const R = 3963.1676 // Radius of earth in miles
 
func distance(p1, p2 location) float64 {
    var dlat float64 = p1.lat - p2.lat
    var dlong float64 = p1.long - p2.long

    var a float64 = math.Pow(math.Sin(dlat/2), 2) + math.Cos(p1.lat)*math.Cos(p2.lat)*math.Pow(math.Sin(dlong/2), 2)
    return 2 * R * math.Atan2(math.Sqrt(a), math.Sqrt(1 - a))
}

func main() {
    fmt.Println(distance(deg2rad(37.78, -122.43), deg2rad(37.78, -122.39)))
}