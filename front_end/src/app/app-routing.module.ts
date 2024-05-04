// src/app/app-routing.module.ts
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' } // Redirects to /login
];

@NgModule({
  imports: [RouterModule.forRoot(routes),app-login],
  exports: [RouterModule]
})
export class AppRoutingModule { }
