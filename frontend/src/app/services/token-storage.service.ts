import { Injectable } from '@angular/core';

const TOKEN_KEY = 'jwt';

@Injectable({
  providedIn: 'root'
})
export class TokenStorageService {

  constructor() { }

  // Set a cookie
  private setCookie(name: string, value: string, days: number): void {
    let expires = '';
    if (days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      expires = '; expires=' + date.toUTCString();
    }
    document.cookie = name + '=' + (value || '') + expires + '; path=/';
  }

  // Get a cookie
  private getCookie(name: string): string | null {
    const nameEQ = name + '=';
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }

  // Remove a cookie
  private eraseCookie(name: string): void {
    document.cookie = name + '=; Max-Age=-99999999;';
  }

  // Sign out by removing the token cookie
  signOut(): void {
    this.eraseCookie(TOKEN_KEY);
  }

  // Save token by setting a cookie
  public saveToken(token: string): void {
    this.setCookie(TOKEN_KEY, token, 7); // Set the cookie to expire in 7 days
  }

  // Get token by reading the cookie
  public getToken(): string | null {
    return this.getCookie(TOKEN_KEY);
  }
}
