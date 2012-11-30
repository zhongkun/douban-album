from douban_client import DoubanClient

DOUBAN_API_KEY = '0beb137ce048a99623c13a76a0d9fcc2'
DOUBAN_API_SECRET = '0c4e47816f6a0a93'
DOUBAN_SCOPE = 'book_basic_r,book_basic_w,community_basic_note,community_basic_online,community_basic_photo,community_advanced_photo,community_basic_user,douban_basic_common,event_basic_r,event_basic_w,movie_basic_r,movie_basic_w,music_artist_r,music_basic_r,music_basic_w,shuo_basic_r,shuo_basic_w'
DOUBAN_REDIRECT_URI = 'http://book.douban.com:8080/login'

client = DoubanClient(DOUBAN_API_KEY, DOUBAN_API_SECRET, DOUBAN_REDIRECT_URI, DOUBAN_SCOPE)
