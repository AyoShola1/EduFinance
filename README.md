

---

# EduFinance

EduFinance is a Django-based web application designed to manage student invoices and payments efficiently. It allows the creation, updating, and deletion of invoices and receipts, with features to print and download invoices as PDFs. The app is designed for educational institutions to streamline their financial processes.

## Features

- Create, update, and delete student invoices
- Generate and manage receipts for payments
- Print and download invoices as PDFs
- Auto-generate student registration numbers
- Notification system for new payments
- Search functionality for invoices by term and session
- User authentication and authorization

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/edufinance.git
   cd edufinance
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000`.

## Configuration

Ensure you have the following configurations in your `settings.py` file:

- **Database:**
  Configure your database settings to use your preferred database (e.g., PostgreSQL, MySQL, SQLite).

- **Static Files:**
  Ensure the static files are correctly configured to serve CSS, JavaScript, and images.

- **Email Backend:**
  Configure the email backend for sending invoices via email.

## Usage

- **Admin Interface:**
  Access the admin interface at `http://127.0.0.1:8000/admin` to manage students, invoices, and receipts.

- **Invoice Management:**
  Create, update, and delete invoices for students. Add receipts for payments and manage them through the admin interface.

- **Notifications:**
  View recent payment notifications on the dashboard.

- **PDF Downloads:**
  Use the form on the invoice list page to select the term and session and download invoices as PDFs.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any feature additions, bug fixes, or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [admin@xchelon.com.ng](mailto:ayoshola17@gmail.com).

---
