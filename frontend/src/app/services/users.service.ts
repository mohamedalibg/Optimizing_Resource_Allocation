import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SERVER_API_URL } from '../app.constants';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = SERVER_API_URL+'/accounts'

  constructor(private http: HttpClient) {}

  getUsers(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/users`, { withCredentials: true });
  }
  deleteUser(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}/delete`, { withCredentials: true });
  }
  addUser(user: any): Observable<any> {
    const formData: FormData = new FormData();
    formData.append('first_name', user.first_name);
    formData.append('last_name', user.last_name);
    formData.append('username', user.username);
    formData.append('password', user.password);
    formData.append('email', user.email);
    if (user.profile_picture) {
      formData.append('profile_picture', user.profile_picture);
    }

    return this.http.post<any>(`${this.apiUrl}/register/`, formData, { withCredentials: true });
  }
}
