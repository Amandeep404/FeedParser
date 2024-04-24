import feedparser

# ex url - https://www.planetpython.org/rss20.xml

def parse(url):
    return feedparser.parse(url)
    
def get_source(parsed):
    feed = parsed['feed']
    return {
        'link': feed['link'],
        'title': feed['title'],
        'subtitle': feed['subtitle'],
    }

def get_articles(parsed):
    articles = []
    entries = parsed['entries']
    for entry in entries:
        # Initialize an image URL variable to None (or a default image)
        image_url = "/assets/images/placeholders/default-image.jpg"
        
        # Try to extract an image from known fields (like media:thumbnail)
        if 'media_thumbnail' in entry:
            image_url = entry['media_thumbnail'][0]['url']
        elif 'media_content' in entry:
            image_url = entry['media_content'][0]['url']
        elif 'links' in entry:  # Sometimes, the image is part of the links
            for link in entry['links']:
                if 'image' in link['type']:
                    image_url = link['href']
                    break
                
        articles.append({
            'id': entry['id'],
            'link': entry['link'],
            'title': entry['title'],
            'summary': entry['summary'],
            'published': entry['published_parsed'],
            'image': image_url
        })
    return articles