print("SSP Homepage Compiler")

from os import listdir
from os.path import isfile, join
stickers = [f for f in listdir(".") if ".png" in f]

stickEl = ""
for img in stickers:
    stickEl += f"<a href=\"/{img}\"><img src=\"{img}\"></a>"

page = """<html><head><title>Shuga Sticker Pack</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        padding: 25px;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
    a {
        color: #1da1f1;
        text-decoration: none;
    }
    a:hover {
        opacity: 0.5!important;
    }
    .stickers {
        text-align: center;
        display: grid;
        grid-template-columns: 23% 23% 23% 23%;
        grid-gap: 10px
    }
    .stickers > a > img {
        width: 100%;
        height: auto;
    }
    .c {
        opacity: 0.5;
        text-align: center;
        margin: 10px;
    }
</style></head><body>
<h1><a href="//buy.dyn.dev/stickerpack">Shuga Sticker Pack</a> API</h1>
<p>Contact <code>stickerpack [at] shuga [dot] co</code> for non-personal usage inquiries or higher-quality assets (or vectors).</p>
<div class="stickers">""" + stickEl + "</div><div class=\"c\">© Shuga and Respective Owners</div></body></html>"

with open('index.html', 'w') as file:
    file.write(page)
    print("Generated gallery at ./index.html")