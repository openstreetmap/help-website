+++
type = "question"
title = "Maperitive: generate tiles matching real boundaries"
description = '''Hello, I&#x27;m relatively new to this world. I think my objective is pretty simple but I&#x27;m having a little trouble trying to achieve it.  What I need: take a part of my city and generate the corresponding tiles for use them offline with GPS data. Basically draw a point at the position I&#x27;m in. What I&#x27;m d...'''
date = "2022-02-28T10:06:00Z"
lastmod = "2022-03-01T02:21:00Z"
weight = 83603
keywords = [ "boundaries", "osm", "maperitive" ]
aliases = [ "/questions/83603" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maperitive: generate tiles matching real boundaries](/questions/83603/maperitive-generate-tiles-matching-real-boundaries)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83603-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm relatively new to this world. I think my objective is pretty simple but I'm having a little trouble trying to achieve it.</p>
<p>What I need: take a part of my city and generate the corresponding tiles for use them offline with GPS data. Basically draw a point at the position I'm in.</p>
<p>What I'm doing: first, I'm locating my area with OSM data using Maperitive. I manually draw a bounding area and I generate the tiles. So far everything works fine.</p>
<p>The problem: the boundaries I draw don't match with the real tiles boundaries. <strong>The resulting JSON contains the boundaries I draw, but not the real tiles boundaries, plus the tiles also don't have matching boundaries between different zoom levels</strong>. This makes sense because of the standard division of the world. Just in case, I illustrate with some images that I found and that describe the situation:</p>
<p><img src="https://lh3.googleusercontent.com/-OQZmnRDK5Zs/Vx4yWKUTX1I/AAAAAAAAAIE/CAl_zqtLFIQvfJWkbEgMurB0JFiEnKLLQCLcB/s320/Area.png" alt="alt text" /></p>
<p><img src="https://lh3.googleusercontent.com/-jHfe7rfvzbg/Vx4yY_f5n3I/AAAAAAAAAII/QUojPcBA-HEFMxWG_hlhF5RWomtIx-WPgCLcB/s320/Zoom%2B10%2BArea.png" alt="alt text" /></p>
<p><img src="https://lh3.googleusercontent.com/-tTJwVQMXwjk/Vx4ybDimAhI/AAAAAAAAAIM/4dvqhuwn5zAKXbZC-xoLswpolsNaOdTzwCLcB/s320/Zoom%2B11%2BArea.png" alt="alt text" /></p>
<p><strong>The question</strong>: is there any way to crop an area and get all the necessary tiles to make them match with the original boundaries?</p>
<p>Greetings.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '22, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/afd9a800e915f09ad316211adbbf52bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sergio&#39;s gravatar image" />
<p><span>Sergio</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sergio has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-83603" class="comments-container">
&#10;</div>
<div id="comment-tools-83603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83603-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="83615"></span>

<div id="answer-container-83615" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83615-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After reading and reading I ended up by resolving my particular problem. The first point is that I wasn't giving it the right focus.</p>
<p>It wasn't about the "real tile boundaries" I was talking about, it was about that <strong>the tiles are the boundaries</strong>. Each tile represent an XYZ point on the global map, and the way Maperitive downloads and stores them is that. It creates the first folder (Z), the sub folders (X) and the files (Y). The nomenclature of every data is the value for the axis.</p>
<p>Solution: for knowing in what tile my coordinates were, I just had to transform my Lat, Lon values as the documentation says. Finally, knowing that the image files are 256x256 and starting from the upper left corner, the only thing needed is to know where the point is inside the image multiplying the floating part by 256.</p>
<p>I coded a Python solution to get this knowing Lat, Lon:</p>
<pre><code>import math
lat_deg = 43.253192
lon_deg = -2.914479
zoom = 19
lat_rad = math.radians(lat_deg)
n = 2.0 ** zoom
xtile = float((lon_deg + 180.0) / 360.0 * n)
ytile = float((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
print(&quot;Tesela para &quot;, lat_deg, lon_deg)
print(&quot;--------------------------------------&quot;)
print(&quot;Carpeta raiz:&quot;, zoom)
print(&quot;Sub carpeta:&quot;, (int)(xtile))
print(&quot;Fichero de imagen&quot;, (int)(ytile))
print(&quot;Pixel X en tesela: &quot;, (xtile % 1)*256)
print(&quot;Pixel Y en tesela: &quot;,  (ytile % 1)*256)</code></pre>
<p>And that's all. I hope this helps someone with no experiencie like me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '22, 02:21</strong></p>
<img src="https://secure.gravatar.com/avatar/afd9a800e915f09ad316211adbbf52bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sergio&#39;s gravatar image" />
<p><span>Sergio</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sergio has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-83615" class="comments-container">
&#10;</div>
<div id="comment-tools-83615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83615-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

