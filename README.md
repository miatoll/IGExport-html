This Python script reads data from a IGExport CSV file and generates an HTML document that displays a list of users with their details, including avatars, usernames, full names, user IDs, and whether they are followed by the user.

 -  **CSV Reading**:
    
    -   The script reads the CSV file using Python's `csv.DictReader`.
    -   It expects columns: `Avatar`, `Username`, `Full Name`, `User ID`, and `Followed By You`.
 -  **HTML Generation**:
    
    -   Creates a styled HTML document with a list of user details.
    -   Each user is represented by a card containing:
        -   A circular avatar image.
        -   Username, full name, user ID, and "Followed By You" status.
 -  **Error Handling for Missing Avatars**:
    
    -   If the `Avatar` field is empty, a placeholder image is used.
    -   The script uses `onerror` in the `<img>` tag to replace broken avatar links with a default placeholder.
 -  **Diagnostics**:
    
    -   Includes debug prints (`print(row)`) to display each row of data being read from the CSV file.
    -   Logs a message when the `Avatar` field is empty for a specific user.
 -  **Output**:
    
    -   The final HTML is saved to the specified file, ready to be opened in a web browser.
 - **Starting**
   - Place the IGexport CSV file in the root directory, rename it to `input.csv`, and then run `index.py` to generate a beautifully formatted `output.html` file containing your data

