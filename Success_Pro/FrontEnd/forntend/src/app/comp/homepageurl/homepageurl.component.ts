import { Component, OnInit } from '@angular/core';
import { CrawlerService } from 'src/crawler_services/crawler.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-homepageurl',
  templateUrl: './homepageurl.component.html',
  styleUrls: ['./homepageurl.component.css']
})
export class HomepageurlComponent implements OnInit {

  constructor(private homeurl:CrawlerService) { }
  homepageurls:object

  ngOnInit() {
      this.homeurl.getHomePageUrls().subscribe((res )=> {this.homepageurls=res
       console.log(this.homepageurls)  })
     
  }

}
