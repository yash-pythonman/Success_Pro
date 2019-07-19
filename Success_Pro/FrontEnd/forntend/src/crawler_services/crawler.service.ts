import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CrawlerService {

  constructor(private http:HttpClient) { }

  public sendUrlDepth(object:object):Observable<any>{

    return this.http.post("http://localhost:8000/apicrawler", object)

  }

  public getHomePageUrls(): Observable<any>{

    return this.http.get("http://localhost:8000/basepageurls")
  }

  public getSubPageUrls(): Observable<any>{
    
    return this.http.get("http://localhost:8000/subpageurls")
  }

  public getHomePageImages(): Observable<any>{

    return this.http.get("http://localhost:8000/homepageimages")
  }
  
  public getSubPageImage(): Observable <any>{

    return this.http.get("http://localhost:8000/subpageimages")
  }
}