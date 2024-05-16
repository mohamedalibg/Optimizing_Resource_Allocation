import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { AuthService } from './services/auth.service';
import { TokenStorageService } from './services/token-storage.service';
import { AdminComponent } from './admin/admin.component';
import { CommonModule } from '@angular/common';
import { UserService } from './services/users.service';

@Component({
  selector: 'app-root',
  standalone: true,
  providers:[AuthService,TokenStorageService,UserService],
  imports: [RouterOutlet,DashboardComponent,LoginComponent,HttpClientModule,AdminComponent,CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
