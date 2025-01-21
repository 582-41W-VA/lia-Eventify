# Proposal for Eventify - Event Planning Portal

**Date:** 01-21-2025  
**Teamenbers:** Fangfang Chen, Aaron James Asuncion, Byeonggil Kim, Changheon Oh

## Project Overview:

Eventify is a Django-based web application that simplifies event planning and management for users. The portal offers an intuitive way to create, manage, and search for events while allowing users to save their favorite events for future reference.  
This proposal outlines the development plan for Eventify, leveraging Django's simplicity and efficiency and using the default SQLite database for seamless integration and management.

---

## Team Members and Roles

- **Aaron**: Design (Figma, HTML/CSS)  
  Responsible for creating the visual identity, wireframes, and mockups using Figma.

- **Oh**: Front-End Developer (Django Templates, HTML/CSS)  
  Focuses on implementing the user interface and ensuring responsiveness.

- **Fangfang**: Back-End Developer  
  Manages the Django backend, including models and views. (Django, Python, SQL)

- **Kim**: Repository Manager  
  Manages the GitHub repository, tracks issues, ensures adherence to version control, and ensures code reviews and continuous integration guidelines.

---

## Primary Users

- **Event Organizers**: Individuals or businesses looking to create and share events.
- **Event Attendees**: Users looking to browse, search for, and save local events of interest.
- **Admin Users**: Individuals managing users, events, and content within the system.

---

## Features

### As a user, I can:

- **Create, Edit, and Delete Events**: Manage events by adding, editing, and deleting event details.
- **Search, Sort, and Filter Events**: Browse events based on different criteria (e.g., event type, date, location).
- **Comment on Events**: Leave feedback on events via comments to foster community engagement.
- **Like Events**: Click the heart button to like events.
- **Save Events**: Save events of interest for future reference.
- **User Registration and Profile**: Create and manage accounts to track event history and preferences.

### As an admin, I can:

- **Manage User Accounts**: Edit or delete user accounts.
- **Manage Events and Comments**: Moderate, edit, and delete events and comments.
- **Review Flagged Events**: Review inappropriate or erroneous events flagged by users.

---

## Technologies Used

Eventify will be developed using the following technologies:

- **Django (Python)**: Django will serve as the primary framework for both the front-end and back-end, providing server-side functionality and HTML templating. All interactivity, including search, filter, and user management, will be handled through Django forms, views, and server-side logic.
- **SQLite**: The application will use SQLite, which is Django’s default database option, for simplicity and ease of development.
- **HTML/CSS**: Custom styles will be used for the responsive and attractive design, avoiding front-end frameworks like Bootstrap or Bulma.

---

## Project Milestones

### Week 1:

- Set up GitHub repository and branch protection rules.
- Create and submit the Request for Proposal (RFP).
- Create and submit the Proposal document including the application features and architecture, define the milestones and project timeline.

### Week 2:

- Draft Visual Guidelines.
- Wireframes and Mockups: Design key pages (home, event listing, event details, login) in Figma (Figma design file or FigJam file).
- Data Model: JPEG or PNG image.
- Define project structure.
- Create installation steps with a Markdown file.
- Create models for events, users, and saved events.
- Implement user authentication and account management.

### Week 3:

- Implement basic CRUD (Create, Read, Update, Delete) functionality for events.
- Submit database model (Entity-Relationship diagram).
- Add search, sorting, and filtering capabilities for browsing events.

### Week 4:

- Design and implement the "Save Event" feature.
- Test features for usability and correctness.
- Complete styling for all pages based on visual guidelines
