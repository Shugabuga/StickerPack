print("SSP Homepage Compiler")

from os import listdir
from os.path import isfile, join
import json
from urllib import parse

stickers = [f for f in listdir(".") if ".png" in f]

stickEl = ""
stickList = {}
stickCount = 0
for img in stickers:
    parseCache = parse.quote(img)
    if "_tp" not in img:
        stickEl += f"<a title=\"{img}\" href=\"/{parseCache}\"><span>{img}</span><img src=\"{parseCache}\"></a>"
    else:
        stickEl += f"<a class=\"tp\" title=\"{img}\" href=\"/{parseCache}\"><span>{img}</span><img src=\"{parseCache}\"></a>"
    stickCount += 1
    stickList[img.replace(".png", "")] = parseCache

page = """<html><head><title>Shuga Sticker Pack</title><meta charset="utf-8"/>
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
    span {
        font-size: 0;
        opacity: 0;
        color: transparent;
    }
    .tp {
        display: none;
    }
    button {
        text-align: center;
        background: #222;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 10px;
        color: white;
        margin: 10px auto;
        display: block;
        cursor: pointer;
    }
</style><script>
let thirdParty = false;
function toggletp() {
    for (let i = 0; i < document.querySelectorAll(".tp").length;i++) {
        if (thirdParty) document.querySelectorAll(".tp")[i].style.display = "none";
        else document.querySelectorAll(".tp")[i].style.display = "inline";
        thirdParty = thirdParty ? false : true;
    }
}</script></head><body>
<h1><a class="title" href="//buy.dyn.dev/stickerpack">Shuga Sticker Pack</a> API</h1>
<p>Contact <code>stickerpack [at] shuga [dot] co</code> for non-personal usage inquiries or higher-quality assets (or vectors).</p>
<button onclick="toggletp()">Toggle Third Party Stickers</button>
<div class="stickers">""" + stickEl + "</div><div class=\"c\">© Shuga and Respective Owners</div></body></html>"

with open('index.html', 'w') as file:
    file.write(page)
    print("Generated gallery at ./index.html")

with open('bd_api.json', 'w') as file:
    file.write(json.dumps(stickList))
    print("Generated BetterDiscord-compatible API at ./bd_api.json")