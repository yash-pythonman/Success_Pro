import { Component, OnInit } from '@angular/core';
import { CrawlerService } from 'src/crawler_services/crawler.service';
import { ThrowStmt } from '@angular/compiler';

@Component({
  selector: 'app-homepageimage',
  templateUrl: './homepageimage.component.html',
  styleUrls: ['./homepageimage.component.css']
})
export class HomepageimageComponent implements OnInit {

  constructor(private imageservice:CrawlerService) { }
  homeimage:object
  ngOnInit() {
      this.imageservice.getHomePageImages().subscribe((res=>{this.homeimage=res}))
  }

}
