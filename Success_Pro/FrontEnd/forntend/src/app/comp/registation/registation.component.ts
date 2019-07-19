import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-registation',
  templateUrl: './registation.component.html',
  styleUrls: ['./registation.component.css']
})
export class RegistationComponent implements OnInit {

  constructor() { }
  regform:FormGroup
  ngOnInit()
  {
  
  this.regform = new FormGroup({
       name : new  FormControl(''),
       lastname:new FormControl(''),
       
  }) ;
  }

  public onSubmit()
  {
    console.log(this.regform.value)
  }

}
