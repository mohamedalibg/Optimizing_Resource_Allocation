import { Component } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { FormControl, Validators, FormsModule, ReactiveFormsModule } from '@angular/forms';  // Import reactive forms modules
import { LoginService } from '../services/login.service';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    FormsModule,
    ReactiveFormsModule,
    MatIconModule,
    HttpClientModule,
  ],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  router: any;
  constructor(private loginService: LoginService) {}

  username = new FormControl('', [Validators.required]);
  password = new FormControl('', [Validators.required]); 

  getErrorMessage() {
    if (this.username.hasError('required')) {
      return 'You must enter a value';
    } else {
      return '';
    }
  }

  hide = true;

  onSubmit(): void {
    const usernameValue = this.username.value;
    const passwordValue = this.password.value;

    if (usernameValue !== null && passwordValue !== null) {
      this.loginService.login(usernameValue, passwordValue).subscribe({
        next: (response) => {
          console.log(response);  // Handle successful login response

          // Assuming your server returns a token or other data indicating a successful login
          // Redirect the user to the HomeComponent after a successful login
          this.router.navigate(['/user']);
        },
        error: (error) => {
          console.error(error);  // Handle login error
        }
      });
    } else {
      console.error('Username or password is null.');
    } 
  }
} 