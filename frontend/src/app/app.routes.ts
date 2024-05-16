import { Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';
import { AuthGuardService } from './services/auth-guard.service';
import { AdminComponent } from './admin/admin.component';

export const routes: Routes = [
    { path: '' ,component: DashboardComponent,canActivate:[AuthGuardService]},
    { path: 'login' ,component: LoginComponent},
    { path: 'admin' ,component: AdminComponent,canActivate:[AuthGuardService]},

];
