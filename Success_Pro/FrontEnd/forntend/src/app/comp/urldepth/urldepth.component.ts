import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { FormGroup, FormControl } from '@angular/forms';
import { CrawlerService } from 'src/crawler_services/crawler.service';

@Component({
  selector: 'app-urldepth',
  templateUrl: './urldepth.component.html',
  styleUrls: ['./urldepth.component.css']
})
export class UrldepthComponent implements OnInit {

  constructor(private service:CrawlerService) { }
  urldepth:FormGroup
  
  ngOnInit() {

    this.urldepth = new FormGroup({
      url: new FormControl(''),
      depth: new FormControl(''),

    })
  }

public formData(){
  this.service.sendUrlDepth(this.urldepth.value).subscribe((res) =>{
    console.log(res
      )
  })
  console.log(this.urldepth.value)
}
}
