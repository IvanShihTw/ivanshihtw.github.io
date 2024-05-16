import os

def generate_sitemap(directory):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.relpath(os.path.join(root, file), directory)
                url = 'https://IvanShihTw.github.io/ivanshihtw.github.io/' + file_path
                sitemap += f'  <url>\n    <loc>{url}</loc>\n  </url>\n'

    sitemap += '</urlset>\n'

    with open('sitemap.xml', 'w') as f:
        f.write(sitemap)

if __name__ == '__main__':
    generate_sitemap('IvanShihTw/ivanshihtw.github.io')
