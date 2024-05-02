# HTML Path Updater

## Overview
The HTML Path Updater is a Python script designed to modify HTML files to ensure that all CSS, JavaScript, and image file paths point to local directories (`css`, `js`, `imgs`). This is particularly useful for adapting HTML content extracted from development tools for local deployment.

## Features
- Automatically updates `href` attributes in `<link>` tags for CSS files.
- Automatically updates `src` attributes in `<script>` tags for JavaScript files.
- Automatically updates `src` attributes in `<img>` tags for image files.

## Prerequisites
Before running this script, ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/).

Additionally, the script uses BeautifulSoup4 for HTML parsing and manipulation. You will need to install this package using pip if it's not already installed:

```bash
pip install beautifulsoup4
```

## Installation
1. Clone this repository or download the script directly.
2. Ensure all dependencies listed under "Prerequisites" are installed.

## Usage
To use the HTML Path Updater, navigate to the directory containing the script and run it using the following command format:

```bash
python html_path_updater.py <input_html_file> <output_html_file>
```

Replace `<input_html_file>` and `<output_html_file>` with the paths to your input and desired output HTML files respectively.

### Example
```bash
python html_path_updater.py example.html updated_example.html
```

This command will process `example.html`, update the file paths as specified, and save the results to `updated_example.html`.

## Contributing
Contributions to the HTML Path Updater are welcome. Please feel free to fork the repository, make improvements, and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
If you encounter any problems or have suggestions, please open an issue on the GitHub repository.


### **Instructions for Use**
1. Copy the text provided above into a new text file.
2. Save this file as `README.md` in the same directory where your script is located.
3. Upload this along with your script to your GitHub repository.
