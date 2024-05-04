import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  loginForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.loginForm.valid) {
      this.http.post<any>('http://localhost:8000/login/', this.loginForm.value).subscribe({
        next: (res) => {
          console.log('Login successful');
          this.router.navigate(['/home']); // Navigate to the home route after login
        },
        error: (err) => {
          console.error('Login failed:', err);
        }
      });
    }
  }
}
