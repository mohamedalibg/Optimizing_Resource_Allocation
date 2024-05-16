import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { SERVER_API_URL } from '../app.constants';

@Injectable({
  providedIn: 'root',
})
export class AuthService {


  constructor(protected http: HttpClient) { }

  login(username: string, password: string): Observable<HttpResponse<any>> {
    return this.http
      .post<any>(`${SERVER_API_URL}/accounts/login/`, { "username": username, "password": password }, { observe: 'response' });
  }
}
