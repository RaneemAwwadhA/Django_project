from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def list_beauty(request):
  beauty=[
        {'id':1,'name':'Body Spray - Scandal', 'price':115,'description':'A refreshing body mist inspired by the iconic Scandal fragrance. For everyday use, it leaves your body feeling refreshed all day long.','image':'https://cdn.salla.sa/yoZjz/yIlTpTl2MjSirSToIrDAvttTq93rR4yfjrOvcwU4.jpg'},
        {'id':2,'name':'Maybelline Lash Sensational Sky High Mascara', 'price':39,'description':'Enjoy a perfect look and captivating eyes with this intense black mascara.','image':'https://assets.goldenscent.com/catalog/product/cache/2/small_image/750x750/9df78eab33525d08d6e5fb8d27136e95/3/0/30166967_-_maybelline_-_maybelline_lash_sensational_sky_high_mascara_-_fd.png'},
        {'id':3,'name':'Lil Gloss Bomb Trio Mini Lip Gloss Set', 'price':200,'description':'This universal lip luminizer delivers explosive shine in 3 shades that flatter all skin tones.','image':'https://img-product.sephora.me/dw/image/v2/BKWK_PRD/on/demandware.static/-/Sites-masterCatalog_Sephora/default/dw5b1d0a16/images/hi-res/SKU/SKU_5530/734259_swatch.jpg?sw=1248&sh=1248&sm=fit&q=85'},
        {'id':4,'name':'Make Over 22 Marplus Brush Set, (MX-02) 12 brushes', 'price':103.05,'description':'Embark on a world of beauty and radiance with the distinctive Marbles brush set from Makeover 22, which includes 12 diverse pieces that meet all your needs for eye-catching professional makeup.','image':'https://cdn.salla.sa/onqKZz/b162a43b-c9b2-4cc2-b560-3d415e923073-750x1000-X3GklMYv2bL3jAMPxbGYlED8r2nK7L2vw9LMzTSK.jpg'},

    ]
  
  contex={
    'beauty':beauty
  }
  #print(request)
  template=loader.get_template('list_beauty.html')
  return HttpResponse(template.render(contex))