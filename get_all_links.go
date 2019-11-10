//file name: get_all_links.go

package main

import(
	//import standard libraries
	"fmt"
	"log"
	// import third party libraries
	"github.com/PuerkitoBio/goquery"
)

func linkScrape() {
	doc, err := goquery.NewDocument("https://en.wikipedia.org")
	if err != nil {
		log.Fatal(err)
	}

	//use CSS selector found with the browser inspector
	//for each, use index and item
	doc.Find("body a").Each(func(index int,item * goquery.Selection) {
		linkTag := item
		link, _ := linkTag.Attr("href")
		linkText := linkTag.Text()
		fmt.Printf("Link #%d: '%s' - '%s'\n",index,linkText,link)
	})

	}

func main(){
	linkScrape()
}
