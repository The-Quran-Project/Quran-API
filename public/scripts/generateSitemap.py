import os
from datetime import datetime, timezone

if os.path.exists("public"):
    os.chdir("public")


# Dictionary of paths
paths = {
    "/": "index.mdx",
    "/about": "about.mdx",
    "/resources": "resources.mdx",
    "/docs": "docs.mdx",
    "/introduction": "introduction.mdx",
    "/getting-started": "getting-started.mdx",
    "/getting-started/list-of-chapters": "getting-started/list-of-chapters.mdx",
    "/getting-started/audio-recitation": "getting-started/audio-recitation.mdx",
    "/getting-started/get-a-verse": "getting-started/get-a-verse.mdx",
    "/getting-started/get-a-chapter": "getting-started/get-a-chapter.mdx",
    "/getting-started/available-reciters": "getting-started/available-reciters.mdx",
}

# Base URL of the website
BASE_URL = "https://quranapi.pages.dev"


def get_last_modified_time(file_path):
    """Return the last modified time of a file in ISO 8601 format."""
    originalPath = f"../pages/{file_path}"
    if os.path.exists(originalPath):
        timestamp = os.path.getmtime(originalPath)
        return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()
    else:
        return datetime.now(
            timezone.utc
        ).isoformat()  # Default to current time if file doesn't exist


def generate_sitemap(paths, base_url):
    """Generate a sitemap.xml content."""
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for path, location in paths.items():
        last_modified = get_last_modified_time(location)
        sitemap.append("  <url>")
        sitemap.append(f"    <loc>{base_url}{path}</loc>")
        sitemap.append(f"    <lastmod>{last_modified}</lastmod>")
        sitemap.append("  </url>")

    sitemap.append("</urlset>")
    return "\n".join(sitemap)


# Generate the sitemap content
sitemap_content = generate_sitemap(paths, BASE_URL)

# Write to sitemap.xml
output_file = "sitemap.xml"
with open(output_file, "w") as f:
    f.write(sitemap_content)

print(
    f"\033[93msitemap.xml\033[0m has been generated successfully at \033[92m{output_file}\033[0m"
)
