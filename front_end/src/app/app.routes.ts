import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import {UsersComponent } from './users/users.component';

export const routes: Routes = [
    {path:'login',component: LoginComponent},
    {path:'user',component:UsersComponent}



];
