
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private baseUrl = 'http://127.0.0.1:8000/accounts';

  constructor(private http: HttpClient) { }

  getAllUsers() {
    // Retrieve token from cookies
    const token = this.getCookie('jwt');

    // Check if token is available
    if (!token) {
      console.error('Authentication token not found in cookies.');
      return;
    }

    // Include token in the request headers
    const headers = { Authorization: `Bearer ${token}` };

    return this.http.get(this.baseUrl, { headers });
  }

  private getCookie(name: string): string | null {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop()?.split(';').shift() || null;
    return null;
  }
}