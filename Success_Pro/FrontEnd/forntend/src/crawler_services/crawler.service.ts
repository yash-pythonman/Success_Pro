import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CrawlerService {

  constructor(private http:HttpClient) { }

  public sendUrlDepth(object:object):Observable<any>{

    return this.http.post("http://localhost:8000/apicrawler/", object)

  }

  public getHomePageUrls(): Observable<any>{

return this.http.post("http://localhost:8000/basepageurls/", "Testing")
  }

  public getSubPageUrls(): Observable<any>{
    
    return this.http.post("http://localhost:8000/subpageurls/", "Tesing")
  }

  public getHomePageImages(): Observable<any>{

    return this.http.post("http://localhost:8000/homepageimages/", "Testing")
  }
  
  public getSubPageImage(): Observable <any>{

    return this.http.post("http://localhost:8000/subpageimages/", "Testing")
  }
}