# Yass - Yet Another Static Site Generator

Yass is a simple static site generator built with Python, Jinja2, and Markdown.
The tool is designed to be straightforward and easy to use,.

## Features

- [x] **Python-based**: Utilizes Python for scripting and automation.
- [x] **Jinja2 Templates**: Allows for dynamic content generation using Jinja2 templates.
- [x] **Markdown Support**: Write your content in Markdown for easy readability and formatting.
- [x] **Front Matter**: Interpret front matter as YAML for metadata management.
- [x] **Static Files**: Easily include static files like CSS, JavaScript, and images.
- [x] **Environment Variables**: Customize your build process with environment variables.

## Directory Structure

```
.
├── content 		# Markdown content
├── LICENSE
├── public		# Public HTML (yass output)
├── README.md
├── requirements.txt
├── static		# Static HTML (will be copied into public/static)
├── template 		# HTML Templates dir
└── yass

```

## Getting Started

### Prerequisites

Everything is defined in `requirements.txt`

- Python 3.x
- Jinja2
- Markdown
- PyYAML

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/nflatrea/yass.git
   cd yass
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. **Configure Environment Variables**:

   You may set the following environment variables to overrite the directories and configuration file:

   - `STATIC_DIR`	: Directory for static files.
   - `CONTENT_DIR`	: Directory for Markdown content.
   - `TEMPLATE_DIR`	: Directory for Jinja2 templates.
   - `BASE_TEMPLATE`	: Base template file.
   - `CONFIG_FILE`	: Configuration file for site settings.

2. **Create Configuration File**:

   Create a `config.yaml` file in the root directory with your site settings. Here is a sample `config.yaml`:

   ```yaml
   style: "/static/style.css"
   email: "contact@acme.corp"

   social:
     - name: Discord
       url: "https://discord.com/invite/ADCEFGabcdefg"
     - name: Twitter
       url: "https://twitter.com/@acmecorp"
     - name: Linkedin
       url: "https://linkedin.com/company/acmecorp"
       
   menu:
     - name: "Home"
       href: "/index.html"
     - name: "Blog"
       href: "/blog.html"
     - name: "Contact"
       href: "/contact.html"
   ```

3. **Create Content Files**:

   Create Markdown files in the `content` directory. Here is a sample `index.md`:
   ```markdown
   ---
   title: Home
   ---
   ## Hello World!
   ```

   The base will use by default the template defined in `BASE_TEMPLATE`, you can overrite this by adding :
 
   ```markdown
   ---
   title: Home
   template: post.html
   ---
   ## This is a blog post !

   Hello World !
   ```

4. **Build the Site**:

   Run the Yass tool to build your site:
   ```sh
   python yass
   ```

5. **Serve the Site**:

   You can use Python's built-in HTTP server to serve the site:
   ```sh
   python -m http.server -d public
   ```

## Contributing

This project is nowhere near production ready and just a quick draft for my own website
Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
