import { Component, OnInit } from '@angular/core';
import { CrawlerService } from 'src/crawler_services/crawler.service';

@Component({
  selector: 'app-subpageimage',
  templateUrl: './subpageimage.component.html',
  styleUrls: ['./subpageimage.component.css']
})
export class SubpageimageComponent implements OnInit {

  constructor(private subpage:CrawlerService) { }
  subpageimage:object
  ngOnInit() {
    this.subpage.getSubPageImage().subscribe((res)=>{this.subpageimage=res;
    console.log(this.subpageimage)
    })
  }

}
