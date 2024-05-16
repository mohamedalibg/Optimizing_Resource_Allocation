import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { TokenStorageService } from './token-storage.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate {

  constructor(
    private router: Router,private token: TokenStorageService) { }

  canActivate() {
    if (this.token.getToken() == null) {
      this.router.navigate(['/login']);
      return false;
    }
    return true;
  }
}
