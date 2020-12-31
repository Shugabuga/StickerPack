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
        background: transparent;
        transition: padding 0.25s ease-in-out, background 0.25s ease-in-out;
        border-radius: 10px;
    }
    .title:hover {
        opacity: 0.5!important;
    }
    a:not(.title):hover {
        background: #222;
        padding: 10px;
    }
    .stickers {
        text-align: center;
        display: grid;
        grid-template-columns: 22% 22% 22% 22%;
        grid-gap: 10px
    }
    .stickers > a > img {
        width: 100%;
        height: auto;
        padding: 0;
    }
    .c {
        opacity: 0.5;
        text-align: center;
        margin: 10px;
    }
</style></head><body>
<h1><a class="title" href="//buy.dyn.dev/stickerpack">Shuga Sticker Pack</a> API</h1>
<p>Contact <code>stickerpack [at] shuga [dot] co</code> for non-personal usage inquiries or higher-quality assets (or vectors).</p>
<div class="stickers">""" + stickEl + "</div><div class=\"c\">© Shuga and Respective Owners</div></body></html>"

with open('index.html', 'w') as file:
    file.write(page)
    print("Generated gallery at ./index.html")