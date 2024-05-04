import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  username: string = '';  // Initialize as empty string to satisfy TypeScript
  password: string = '';  // Initialize as empty string to satisfy TypeScript

  constructor(private http: HttpClient) {}

  login() {
    this.http.post<any>('http://localhost:8000/accounts/login', { username: this.username, password: this.password })
      .subscribe({
        next: (response) => {
          console.log('Login successful', response);
          localStorage.setItem('jwt', response.jwt);
        },
        error: (error) => {
          console.error('Login failed', error);
        }
      });
  }
}

