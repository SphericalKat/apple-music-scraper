import os
import scrapy
import dateparser
import pytimeparse

class AlbumSpider(scrapy.Spider):
    name = "album"
    allowed_domains = ["music.apple.com"]
    start_urls = ["https://music.apple.com/us/album"]

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.album = kwargs.get('album')

    def start_requests(self):
        for url in self.start_urls:
            if not self.album:
                os.exit(1)
            yield scrapy.Request(url=f'{url}/{self.album}', callback=self.parse)

    def parse(self, response):
        album_name = response.css('h1.headings__title::text').get()
        artist_name = response.css('div.headings__subtitles a::text').get()
        metadata = response.css('div.headings__metadata-bottom::text').get().split('·')
        genre = metadata[0].strip()

        details = response.css('p.description::text').get()
        details_arr = details.split('\n')
        release_date = dateparser.parse(details_arr[0].strip())
        no_tracks, time = [x.strip() for x in details_arr[1].split(',', 1)]
        no_tracks = no_tracks.replace(' Songs', '')
        time_parsed = pytimeparse.parse(time)
        label = details_arr[2].strip()

        print(f'Album: {album_name}')
        print(f'Artist: {artist_name}') 
        print(f'Genre: {genre}')
        print(f'Release Date: {release_date}')
        print(f'No of tracks: {no_tracks}')
        print(f'Length: {time_parsed}')
        print(f'Label: {label}')
        pass
