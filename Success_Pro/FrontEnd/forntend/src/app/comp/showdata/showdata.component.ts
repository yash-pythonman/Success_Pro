import { Component, OnInit } from '@angular/core';
import { EmployeeService } from 'src/services/employee.service';

@Component({
  selector: 'app-showdata',
  templateUrl: './showdata.component.html',
  styleUrls: ['./showdata.component.css']
})
export class ShowdataComponent implements OnInit {

  constructor(private  empserivice:EmployeeService) { }
  empdata:Object
  ngOnInit() {
    this.empserivice.getEmployee().subscribe((res) =>{
      this.empdata=res;
    })
  }
  public empDelete(id:string){
     this.empserivice.deleteEmployee(id).subscribe((res) =>{
       console.log(res)
     })
   
  }

}
