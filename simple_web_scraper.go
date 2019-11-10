// Make an HTTP Request
package main

import (
	"fmt"
	"golang.org/x/net/html"
	"net/http"
	"os"
	"strings"
)

//Helper function to pull the href attribute form a Token

func getHref(t html.Token) (ok bool,href string) {
	// Iterate over all of the Token's attributes until we find on "href"
	for _, a := range t.Attr {
		if a.Key == "href" {
			
			href  = a.Val

			ok = true
		}

	}

	//"bare" will return the variables (ok,href) as defined in
	//the function definition
	return
	
}

//Extract all http** links from a given webpage

func scrape(url string, ch chan string, chFinished chan bool) {
	resp,err := http.Get(url)

	defer func() {
		// NOtify that we are done after this function

		chFinished <- true
	}()

	if err != nil {
		fmt.Println("ERROR: Failed to scrape \"" + url + "\"")
		return
	}

	b := resp.Body

	defer b.Close() //close Body when the function returns

	z := html.NewTokenizer(b)

	for {
		tt := z.Next()

		switch{
			case tt == html.ErrorToken:
				// End of the document, we are done
				return
			case tt == html.StartTagToken:
				t := z.Token()

			//CHeck if the token is an <a> tag

			isAnchor := t.Data == "a"

			if !isAnchor {
				continue
			}

			//Extrac the href value, if there is one

			ok,url := getHref(t)
			
			if !ok {
				continue
			}
			
			//Make sure the url begins in http**

			hasProto := strings.Index(url,"http") == 0

			if hasProto {
					ch <- url
			}

		}
	}
}

func main() {
	fmt.Println("%d\n",len(os.Args))

	foundUrls := make(map[string]bool)

	seedUrls := os.Args[1:]
	
	

	//Channels

	chUrls := make(chan string)

	chFinished := make(chan bool)

	//Kick off the scrape process (concurrently)

	for _, url := range seedUrls {
		go scrape(url,chUrls,chFinished)
	}

	//Subscribe to both channels

	for c := 0; c < len(seedUrls); {
		select {
			case url := <- chUrls:
				foundUrls[url] = true

			case <- chFinished:
				c++
		}
	}

	// We're done! Print the results...

	fmt.Println("\nFound", len(foundUrls), "unique urls:\n")

	for url, _ := range foundUrls {
		fmt.Println(" - " + url)
	}

	
	close(chUrls)
}


