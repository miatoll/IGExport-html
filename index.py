import csv

def csv_to_html(input_csv, output_html):
    try:
        with open(input_csv, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            
            
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Users List</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    .user { border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; display: flex; align-items: center; }
                    .avatar { width: 50px; height: 50px; border-radius: 50%; margin-right: 15px; object-fit: cover; }
                    .details { flex: 1; }
                </style>
            </head>
            <body>
                <h1>Users List</h1>
            """
            
            for row in reader:
               
                avatar = row.get("Avatar", "").strip()
                username = row.get("Username", "Unknown")
                full_name = row.get("Full Name", "Unknown")
                user_id = row.get("User ID", "Unknown")
                followed_by_you = row.get("Followed By You", "No")
                
               
                if not avatar:
                    print(f"Missing avatar for user: {username}")
                    avatar = "https://via.placeholder.com/50"
                else:
                    print(f"Avatar URL: {avatar}")
                
               
                html_content += f"""
                <div class="user">
                    <img class="avatar" src="{avatar}" alt="{username}'s avatar">
                    <div class="details">
                        <p><strong>Username:</strong> {username}</p>
                        <p><strong>Full Name:</strong> {full_name}</p>
                        <p><strong>User ID:</strong> {user_id}</p>
                        <p><strong>Followed By You:</strong> {followed_by_you}</p>
                    </div>
                </div>
                """
           
            html_content += """
            </body>
            </html>
            """

      
        with open(output_html, mode='w', encoding='utf-8') as html_file:
            html_file.write(html_content)
            print(f"HTML file successfully created: {output_html}")
    except Exception as e:
        print(f"An error occurred: {e}")


csv_to_html('input.csv', 'output.html')
