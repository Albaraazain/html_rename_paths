from bs4 import BeautifulSoup
import os

def update_file_paths(html_file_path, output_file_path):
    # Read the HTML content
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Update href in all link tags for CSS files
    for link in soup.find_all('link', {'rel': 'stylesheet'}):
        if link.get('href'):
            link['href'] = os.path.join('css', os.path.basename(link['href']))

    # Update src in all script tags for JavaScript files
    for script in soup.find_all('script'):
        if script.get('src'):
            script['src'] = os.path.join('js', os.path.basename(script['src']))

    # Update src in all img tags for image files
    for img in soup.find_all('img'):
        if img.get('src'):
            img['src'] = os.path.join('imgs', os.path.basename(img['src']))

    # Write the modified HTML back to a new file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# Example usage
update_file_paths('index.html', 'index2.html')
