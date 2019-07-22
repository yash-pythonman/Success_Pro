import { Component, OnInit } from '@angular/core';
import { CrawlerService } from 'src/crawler_services/crawler.service';

@Component({
  selector: 'app-subpageurl',
  templateUrl: './subpageurl.component.html',
  styleUrls: ['./subpageurl.component.css']
})
export class SubpageurlComponent implements OnInit {

  constructor(private subpag:CrawlerService) { }
  subpageurls:object[]
  ngOnInit() {
    this.subpag.getSubPageUrls().subscribe((res)=>{this.subpageurls=res;
    console.log(this.subpageurls)
    })
  }
}
