# Example WordPress Integration Script

# This is a placeholder for scripts that automate WordPress updates, plugin management, or content publishing.
# You can use WP-CLI, REST API, or FTP/SFTP for integration.

# Example: publish_content.py
# def publish_to_wordpress(content):
#     # Use WordPress REST API to create/update posts
#     pass

import os
import requests
from dotenv import load_dotenv

load_dotenv()
WP_URL = os.getenv("WORDPRESS_URL")
WP_USER = os.getenv("WORDPRESS_USER")
WP_PASS = os.getenv("WORDPRESS_APP_PASSWORD")

def publish_homepage(html_content, title="Home"): 
    # Get the ID of the homepage (assumes a page titled 'Home' exists)
    pages_url = f"{WP_URL}/wp-json/wp/v2/pages?search={title}"
    resp = requests.get(pages_url, auth=(WP_USER, WP_PASS))
    if resp.status_code == 200 and resp.json():
        page_id = resp.json()[0]['id']
        update_url = f"{WP_URL}/wp-json/wp/v2/pages/{page_id}"
        data = {"content": html_content}
        update_resp = requests.post(update_url, json=data, auth=(WP_USER, WP_PASS))
        if update_resp.status_code == 200:
            print("Homepage updated successfully!")
        else:
            print("Failed to update homepage:", update_resp.text)
    else:
        # If no Home page exists, create one
        create_url = f"{WP_URL}/wp-json/wp/v2/pages"
        data = {"title": title, "content": html_content, "status": "publish"}
        create_resp = requests.post(create_url, json=data, auth=(WP_USER, WP_PASS))
        if create_resp.status_code == 201:
            print("Homepage created and published!")
        else:
            print("Failed to create homepage:", create_resp.text)

# Example usage:
# with open('../vr_ar/index.html', 'r', encoding='utf-8') as f:
#     html = f.read()
# publish_homepage(html)
