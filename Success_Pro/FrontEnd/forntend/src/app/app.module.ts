import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormGroup, FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';


import { HttpClient, HttpClientModule } from  '@angular/common/http';
import { UrldepthComponent } from './comp/urldepth/urldepth.component';
import { HomepageurlComponent } from './comp/homepageurl/homepageurl.component';
import { SubpageurlComponent } from './comp/subpageurl/subpageurl.component';
import { HomepageimageComponent } from './comp/homepageimage/homepageimage.component';
import { SubpageimageComponent } from './comp/subpageimage/subpageimage.component'
@NgModule({
  declarations: [
    AppComponent,
    UrldepthComponent,
    HomepageurlComponent,
    SubpageurlComponent,
    HomepageimageComponent,
    SubpageimageComponent,
    
    
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule

   
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
