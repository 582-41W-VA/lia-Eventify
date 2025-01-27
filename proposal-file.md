# Proposal for Eventify - Event Planning Portal

**Date:** 01-21-2025  
**Teamenbers:** Fangfang Chen, Aaron James Asuncion, Byeonggil Kim, Changheon Oh

## Project Overview:

Eventify is a web-based event planning portal designed to simplify the organization, management, and discovery of events. It caters to individual users, event planners, and administrators by providing a seamless interface for creating, managing, and discovering events. The project emphasizes simplicity, leveraging Django and Python for all core functionalities, and uses the default SQLite database for straightforward implementation.

---

## Benefits of Eventify

- Simplifies event creation and management.
- Empowers users with personalized features like history tracking and private collections.
- Provides admins with robust tools for moderation and analytics.
- Built with a lightweight, efficient technology stack for ease of maintenance.

---

## Team Members and Roles

- **Aaron James Asuncion**: Design Lead (Figma, HTML/CSS)  
  Responsible for creating the visual identity, wireframes, and mockups using Figma.
- **Changheon Oh**: Front-End Developer (Django Templates, HTML/CSS)  
  Focuses on implementing the user interface and ensuring responsiveness.
- **Fangfang Chen**: Back-End Developer (Django, Python, SQL)  
  Manages the Django backend, including models and views.
- **Byeonggil Kim**: Repository Manager  
  Manages the GitHub repository, tracks issues, ensures adherence to version control, and oversees code reviews and CI/CD guidelines.

---

## Primary Users

- **Event Organizers**: Individuals or businesses looking to create and share events.
- **Event Attendees**: Users looking to browse, search for, and save local events of interest.
- **Admin Users**: Individuals managing users, events, and content within the system.

---

## Features

### As a user, I can:

- **Create, Edit, and Delete Articles (Events)**  
  Description: Users can create, update, and remove events. When creating events, users can input essential details such as the name, description, date, time, amout of people and location of the event. They also have the option to upload images, add tags, and categorize events.

- **Browse, Sort, Filter, and Search Events**  
  Description: The platform offers robust browsing functionality, allowing users to sort events by categories like location, date, or popularity. Filters can be applied to narrow down searches to specific interests or types of events (e.g., concerts, conferences, parties).

- **Like and Unlike Events**  
  Description: Users can mark events they like, which are then stored in their profile. If they change their mind, they can, unlike the event, and it will be removed from their linked list.

- **Flag Inappropriate or Erroneous Events**  
  Description: If a user finds an event that is inappropriate or contains incorrect information, they can flag it for review by an administrator. Flagged events are logged and visible in the admin panel for further action.

- **Add Comments on Events**  
  Description: Users can interact with events by leaving comments, asking questions, or providing feedback. These comments are shown publicly and attributed to the user.

- **Save Events to Favorate**  
  Description: Users can save events that interest them to a Favorate list, giving them easy access later.

- **Browse, Sort, Filter, and Search Favorates events**  
  Description: Saved events in a user's Favorate list can be organized with similar sorting and filtering options as the broader event listings. Users can look up events by name, type, or date in their Favorate list.

- **View User Profile/dashboard**  
  Description: A user’s Profile/dashboard can create event and will display events they’ve liked or flagged (based on event types and categories).

- **Create and Manage Accounts**  
  Description: Users can create an account to track their activities, log in to access saved Favorate list, liked events, and other personalized features. Password management and account settings, including notifications and preferences, are also included.

### As an admin, I can:

- **Edit and Delete User Accounts**  
  Description: Admin users have full control over user accounts. They can view, modify, or delete accounts if necessary, ensuring the platform remains free from spam or inappropriate activity.

- **Edit and Delete Events**  
  Description: Admins can edit or remove any event listed on the platform. This includes correcting event details, removing erroneous content, and ensuring that all listed events comply with platform guidelines.

- **Edit and Delete Comments**  
  Description: Admins have the ability to moderate comments, removing offensive or irrelevant feedback and ensuring a positive user experience.

- **Review Flagged Events**  
  Description: Admins can review flagged events for possible violations of platform rules. They can take appropriate action, such as removing the event or contacting the event creator for clarification.

- **Integrate Maps API**
  Description: Admins can integrate Maps into the platform to enhance event location features. This will allow users to view event locations on an interactive map, improving accessibility and clarity for attendees.

- **Generate Statistics**  
  Description: Admins can access real-time statistics on platform activity, including the number of active users, events, flagged content, and more. These analytics are crucial for monitoring platform health and user engagement.

- **Manage Admin Panel**
  Description: The admin panel provides a comprehensive interface for managing users, events, comments, flagged content, and generating statistics. It features customizations to Django’s default admin interface, offering a more user-friendly layout. Admins can view detailed logs and analytics, review flagged content, and perform moderation actions with a few clicks.

---

## Technologies Used

Eventify will be developed using the following technologies:

- **Django (Python)**: The backbone of the backend functionality, Django allows for efficient handling of requests, views, models, and templates. Its built-in features, such as the authentication system, make it ideal for this project.
- **SQLite**: Chosen for its lightweight nature, SQLite provides a simple yet powerful database solution that requires minimal setup and is easy to manage, making it a suitable choice for Eventify.
- **Django Authentication System**: Handles all user authentication processes, ensuring that users can securely log in, register, and manage their profiles.
- **Django Admin Panel**: Customized to suit the needs of Eventify, the admin panel provides a user-friendly interface for managing users, events, and comments, along with essential moderation and reporting tools.
- **Django Templates**: Used to render HTML for user-facing pages, templates ensure that the site's look and feel are consistent and can be easily updated when necessary.
- **Third-Party API Integration**: Used to fetch and import event data from trusted sources, ensuring Eventify is always up to date with a diverse array of events.

---

## Page Summaries

- **Homepage**  
  The homepage will serve as the entry point for users to explore various events. It will include a search bar, event categories, and quick links to popular events. Featured events will be displayed, allowing users to easily browse upcoming events.

- **Event Listing Page**  
  This page will display a list of events. Users can sort, filter, and search for events by date, location, and type. Each event listing will include a brief summary with a link to the event details page.

- **Event Details Page**  
  The event details page will provide comprehensive information about a specific event, including date, time, location, and a detailed description. Users can like, comment on, and save the event to their collection from this page.

- **Sign Up Page**  
  The Sign up page is showing a form for the user to sign up an account, including user name, email, password (Ffchen234456, at least 8 characters).

- **Login Page**  
  The login page will allow users to securely access their accounts. Users can log in with their email and password, or reset their password if necessary.

- **User Dashboard**  
  The user dashboard will create new event and display all of a user’s Favorate events, liked events, and a history of events they’ve attended or interacted with. It provides an overview of the user’s preferences and event history.

- **Admin Panel**  
  The admin panel will allow administrators to manage users, events, comments, and flagged content. It will also provide statistical insights into event activity and user engagement.

---

## Project Milestones

### Week 1:

- Set up GitHub repository and branch protection rules.
- Create and submit the Request for Proposal (RFP).
- Create and submit the Proposal document including the application features and architecture, define the milestones and project timeline.

### Week 2:

- Draft Visual guidelines.
- Wireframes and Mockups for key pages (home, event listing, Event Details, event details, login) in Figma (Figma design file or FigJam file).
- Data model: Entity-Relationship diagram. JPEG or PNG image.
- Initialize the Django project and configure SQLite as the database.
- Installation Steps with Markdown file.
- Create models for events, users, and saved events.
- Set up user authentication, registration, and account management.

### Week 3:

- Develop CRUD operations for events.
- Implement event browsing, sorting, and filtering.
- Add liking/unliking functionality.
- Enable saving events to a private collection.
- Create user dashboards to display history and preferences.

### Week 4:

- Customize the Django admin panel to manage users, events, comments, and flags.
- Build tools for generating statistics and importing third-party content.
- Complete styling for all pages based on visual guidelines.
- Integrate search functionality using Django QuerySets.
- Enhance user dashboards with recommendations.

### Week 5:

- Conduct internal testing to ensure functionality and responsiveness.
- Create a user manual and API documentation.
- Final review of the project, making sure all features are integrated and functional.
- Submit the final project for evaluation.

---

## Expected Deliverables

- Request for Proposal (RFP): Due: end of week 1 (Format: Markdown file)
- Proposal Document: Due: end of week 1 (Format: Markdown file)
- Visual Guidelines: Due: end of week 2 (Format: Figma design file)
- Figma Wireframes: Due: end of every week (Format: Figma design file or FigJam file)
- Mockups: Due: end of every week (Format: Figma design document)
- Installation steps:Due: end of week 2(Format: Markdown file)
- Data model: Entity-Relationship Diagram.Due: end of week 2 (Format: JPEG or PNG image)
- Source code:Due: end of every week
- Final presentation:Due: last class(Format: slide deck)
