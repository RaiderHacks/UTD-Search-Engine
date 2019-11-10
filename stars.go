package main
import (
    "fmt"
    "log"
    "strings"
    "net/http"
    "github.com/PuerkitoBio/goquery"
)
func scrapeViaClassName(){
    resp, err := http.Get("https://github.com/trending")
    if err != nil{
        log.Fatal(err)
    }
    defer resp.Body.Close()

    if resp.StatusCode != 200{
        log.Fatalf("Status code error: %d %s", resp.StatusCode, resp.Status)
    }
    doc, err := goquery.NewDocumentFromReader(resp.Body)
    if err != nil{
        log.Fatal(err)
    }
    fmt.Println(doc.Find("title").Text())

    doc.Find("ol li").Each(func(i int, s *goquery.Selection){
        fmt.Println(strings.TrimSpace(s.Find(".float-sm-right").Text()))
    })
}


func main(){
    scrapeViaClassName()
}
