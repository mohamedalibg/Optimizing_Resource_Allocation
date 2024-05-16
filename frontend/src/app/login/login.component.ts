import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';
import { HttpClientModule, HttpResponse } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { TokenStorageService } from '../services/token-storage.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, ReactiveFormsModule, HttpClientModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

      
  constructor(private formBuilder: FormBuilder, protected authService: AuthService, private _router: Router, protected tokenService: TokenStorageService) {
  }

  loginForm = this.formBuilder.group({
    username: [],
    password: [],
  });


  handleSubmit() {

    const body: any = {
      username: this.loginForm.get(['username'])!.value,
      password: this.loginForm.get(['password'])!.value,
    };
    console.log(body);
    if (!body.username) {
      alert('Field Required')
      return;
    }

    if (!body.password) {
      alert('Field Required')
      return;
    }

    this.authService.login(body.username, body.password).subscribe((res: HttpResponse<any>) => {
      console.log(res.body!);
      this.tokenService.saveToken(res.body.jwt)
      if (res.body.user_type == 'manager') 
        this._router.navigate([''])
      
      if (res.body.user_type == 'admin') 
        this._router.navigate(['admin'])



    }, (error:any) => {
      console.log(error);
      alert(error.error.detail)
    });
  }

}
