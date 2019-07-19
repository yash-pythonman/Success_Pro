import { Injectable } from '@angular/core';
import { HttpClient } from  '@angular/common/http'
import { Observable } from 'rxjs';
import { TouchSequence } from 'selenium-webdriver';
import { ThrowStmt } from '@angular/compiler';

@Injectable({
  providedIn: 'root'
})

export class EmployeeService {
  constructor(private http:HttpClient) { }

  public getEmployee():Observable<any> 
  {
    return this.http.get("http://localhost:8001/emp")
  }

  public saveEmployee(object:Object):Observable<any>
  {
    return  this.http.post("http://localhost:8001/emp",object)
  }
   
  public updateEmployee(object:Object ,id:string):Observable<any>
  {
    return this.http.put("http://localhost:8001/emp/"+id ,object)
  }

  public deleteEmployee(id:string):Observable<any>
  {
    return  this.http.delete("http://localhost:8001/emp/"+id)
  }

}
