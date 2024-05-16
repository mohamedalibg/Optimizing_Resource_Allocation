import { Component } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { AsideComponent } from '../aside/aside.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [NavbarComponent,AsideComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {

}
