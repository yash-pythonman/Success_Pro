import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RegistationComponent } from './comp/registation/registation.component';
import { ShowdataComponent } from './comp/showdata/showdata.component';
import { UrldepthComponent } from './comp/urldepth/urldepth.component';
import { HomepageimageComponent } from './comp/homepageimage/homepageimage.component';
import { SubpageimageComponent } from './comp/subpageimage/subpageimage.component';
import { HomepageurlComponent } from './comp/homepageurl/homepageurl.component';
import { SubpageurlComponent } from './comp/subpageurl/subpageurl.component';


const routes: Routes = [ 
  {path:"reg" , component:RegistationComponent},
  {path:"show",component:ShowdataComponent},
  {path:"crawler", component:UrldepthComponent},
  {path:"homeimage", component:HomepageimageComponent},
  {path:"subpageimage", component:SubpageimageComponent},
  {path:"homeurl", component:HomepageurlComponent},
  {path:"subpageurl", component:SubpageurlComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 
 
}
