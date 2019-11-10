package main
import(
	"fmt"
	"log"
	"net/http"
	"github.com/PuerkitoBio/goquery"
)

func scrapeAttributes(){
	resp, err := http.Get("https://github.com/trending")
	if err != nil{
		log.Fatal(err)
	}

	defer resp.Body.Close()

	if resp.StatusCode !=  200{
		log.Fatalf("Status code error: %d %s",resp.StatusCode,resp.Status)
	}

	doc,err := goquery.NewDocumentFromReader(resp.Body)
	
	if err != nil{
		log.Fatal(err)
	}

	fmt.Println(doc.Find("title").Text())

	doc.Find("ol li").Each(func(i int, s *goquery.Selection){
		href,has_attr := s.Find("a").First().Attr("href")

		if has_attr{
			fmt.Println("https://github.com"+href)
		}
	})

}

func main(){
	scrapeAttributes()
}
