import { Component } from '@angular/core';
import { TokenStorageService } from '../services/token-storage.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {
  constructor(private router: Router, protected tokenService: TokenStorageService) { }
  handleSignout() {
    console.log("signing out")
    this.tokenService.signOut()
    this.router.navigate(['/login']);
  }
}
