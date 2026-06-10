# News-Portal CMS

A modern, high-fidelity News Portal Content Management System (CMS) built with Django, styled with Vanilla CSS and Bootstrap, and featuring dynamic content sliders, user authentication, a private writing dashboard, and Access Control List (ACL) security patterns.

---

## Key Features

1. **Brand Theme Customization**: Elegant, consistent theme colors across the entire site using an Orange/Coral accent color (`#FF6F61`) and refined Dark/Charcoal secondary tones.
2. **Dynamic Categories**: Dynamic carousels for *Sports*, *Technology*, *Business*, and *Entertainment* news.
3. **Advanced Slider Mechanics**: Custom Slick Carousel integrations that dynamically render single or multiple articles without breaking layouts, and feature fallback placeholder news cards for empty states.
4. **Markdown Supported Editor**: Uses the rich **EasyMDE Markdown Editor** for creating/editing post descriptions, with customized focus indicators matching the brand's style.
5. **Image Live Previews**: Live file-preview functionality on post creation and modification screens using JavaScript's FileReader API.
6. **Programmatic Image Resizing**: Automatic backend image optimization and resizing to a maximum width of 800px using PIL (Pillow) upon post submission to save storage space and boost page load speeds (Core Web Vitals).
7. **User Authentication & Dashboard**: Built-in secure user registration, login, logout, and a private writer's Dashboard to manage self-published articles.
8. **Access Control List (ACL) Constraints**: 
   - Public view shows articles from all publishers mixed together.
   - Public homepage and post detail pages conditionally render edit/delete actions only to the post's authenticated author.
   - Strict server-side validation checks return `403 Forbidden` if unauthorized users attempt to modify other writers' posts.

---

## Tech Stack

- **Backend**: Django 4.2.x (Python 3.13)
- **Database**: SQLite (default local development database)
- **Frontend**: HTML5, Vanilla CSS, Bootstrap 4.4.1, jQuery
- **Libraries & Plugins**:
  - [Slick Slider](https://kenwheeler.github.io/slick/) (Responsive Carousel Slider)
  - [EasyMDE](https://github.com/Ionaru/easymde) (Markdown Text Editor)
  - [Pillow](https://python-pillow.org/) (Python Image Processing Library)
  - [Markdown](https://python-markdown.github.io/) (Markdown parser for rendering descriptions)

---

## Getting Started

### Prerequisites
- Python 3.8 or higher installed.

### Installation & Run Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Hasrat270/News-Portal.git
   cd News-Portal
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django pillow markdown
   ```

4. **Apply Database Migrations**:
   ```bash
   python3 manage.py migrate
   ```

5. **Start Development Server**:
   ```bash
   python3 manage.py runserver
   ```
   Open `http://127.0.0.1:8000/posts` in your web browser.

---

## Manual Testing Credentials

To make testing the authentication and author-specific dashboard limits easy right away, use the following pre-created test superuser credentials:

- **Username**: `hasrat`
- **Password**: `hasrat123`

*Note: Existing posts in the local database have been associated with this account. Logging in will immediately reveal Edit and Delete controls for these posts on the homepage and dashboard.*
