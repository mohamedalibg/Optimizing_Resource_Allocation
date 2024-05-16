import { Component, OnInit } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { AsideAdminComponent } from '../aside-admin/aside-admin.component';
import { UserService } from '../services/users.service';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import * as bootstrap from 'bootstrap';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [AsideAdminComponent, NavbarComponent, CommonModule, HttpClientModule,FormsModule, ReactiveFormsModule],
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.css'
})
export class AdminComponent implements OnInit {
  users: any[] = [];
  newUser: any = {};  

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    this.userService.getUsers().subscribe((data: any[]) => {
      this.users = data;
    });
  }
  deleteUser(id: number): void {
    if (confirm('Are you sure you want to delete this user?')) {
      this.userService.deleteUser(id).subscribe(
        () => {
          this.ngOnInit(); // Reload the users after deletion
        },
        (error) => {
          console.error('Error deleting user:', error);
        }
      );
    }
  }
  addNewRecord(): void {
    this.userService.addUser(this.newUser).subscribe(
      () => {
        this.ngOnInit(); // Reload the users after adding a new user
        this.newUser = {}; // Reset the new user form
        const formElement = document.getElementById('form-add-new-record') as HTMLFormElement;
        if (formElement) {
          formElement.reset();
        }
        const offcanvasElement = document.getElementById('add-new-record');
        if (offcanvasElement) {
          const offcanvas = new bootstrap.Offcanvas(offcanvasElement);
          offcanvas.hide();
        }
      },
      (error) => {
        console.error('Error adding user:', error);
      }
    );
  }

  handleFileInput(event: any): void {
    if (event.target.files.length > 0) {
      this.newUser.profile_pic = event.target.files[0];
    }
  }
}
