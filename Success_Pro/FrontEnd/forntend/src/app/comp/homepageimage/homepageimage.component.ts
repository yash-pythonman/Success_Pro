import { Component, OnInit } from '@angular/core';
import { CrawlerService } from 'src/crawler_services/crawler.service';
import { ThrowStmt } from '@angular/compiler';
import { HomepageurlComponent } from '../homepageurl/homepageurl.component';

@Component({
  selector: 'app-homepageimage',
  templateUrl: './homepageimage.component.html',
  styleUrls: ['./homepageimage.component.css']

})
export class HomepageimageComponent implements OnInit {

  constructor(private imageservice:CrawlerService) { }
  homeimage:object
  url:object
  ngOnInit() {
      this.imageservice.getHomePageImages().subscribe((res)=>{this.homeimage=res;
      console.log(this.homeimage)
      })

      this.imageservice.getHomePageUrls().subscribe((res)=>{this.url=res;
        
       console.log(this.url)})

  }

}
