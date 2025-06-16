+++
type = "question"
title = "Tile coordinates from lat+lon+zoom formula problem?"
description = '''Hi All, I&#x27;m trying to get tile coordinates of lat/lon points on various zoom level maps using the code shown in the OSM wiki. I started testing with the following python code from the OSM wiki: -- code ------------------ import math  def deg2num(latdeg, londeg, zoom):   latrad = math.radians(latdeg)...'''
date = "2014-10-19T07:39:00Z"
lastmod = "2014-10-19T10:12:00Z"
weight = 37743
keywords = [ "python", "tiles", "coordinates" ]
aliases = [ "/questions/37743" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile coordinates from lat+lon+zoom formula problem?](/questions/37743/tile-coordinates-from-latlonzoom-formula-problem)

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
<span id="post-37743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37743-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I'm trying to get tile coordinates of lat/lon points on various zoom level maps using the code shown <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#lon.2Flat_to_tile_numbers" title="here">in the OSM wiki</a>. I started testing with the following python code from the OSM wiki:</p>
<p>-- code ------------------</p>
<pre><code>import math
&#10;def deg2num(latdeg, londeg, zoom):  
    latrad = math.radians(latdeg)  
    n = 2.0 ** zoom  
    xtile = int((londeg + 180.0) / 360.0 * n)  
    ytile = int((1.0 - math.log(math.tan(latrad) + (1 / math.cos(latrad))) / math.pi) / 2.0 * n)  
    return (xtile, ytile)
&#10;zoom = 4  
lon = 0.0  
print &#39;zoom=%d, lon=%.1f&#39; % (zoom, lon)  
for lat in range(80,91):  
    print &#39;lat=%.2f, result=%s&#39; % (lat, str(deg2num(lat, lon, zoom)))</code></pre>
<p>-- end code --------------</p>
<p>This code, when run, shows this:</p>
<pre><code>zoom=4, lon=0.0  
lat=80.00, result=(8, 1)  
lat=81.00, result=(8, 1)  
lat=82.00, result=(8, 1)  
lat=83.00, result=(8, 0)  
lat=84.00, result=(8, 0)  
lat=85.00, result=(8, 0)  
lat=86.00, result=(8, 0)  
lat=87.00, result=(8, -1)  
lat=88.00, result=(8, -2)  
lat=89.00, result=(8, -4)  
lat=90.00, result=(8, -88)</code></pre>
<p>Note that the values for latitudes greater than 86.0 degrees return NEGATIVE tile coordinates. I don't see any indication that the OSM formula is valid only if abs(lat) &lt;= 85 degrees, so what am I doing wrong? Or is this a known limitation of the geomapping?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '14, 07:39</strong></p>
<img src="https://secure.gravatar.com/avatar/f6758169071d716fa9942318699aac60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rzzzwilson&#39;s gravatar image" />
<p><span>rzzzwilson</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rzzzwilson has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '14, 12:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-37743" class="comments-container">
&#10;</div>
<div id="comment-tools-37743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37743-form-container" class="comment-form-container">
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

<span id="37745"></span>

<div id="answer-container-37745" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37745-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-37745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="https://en.wikipedia.org/wiki/Mercator_projection">https://en.wikipedia.org/wiki/Mercator_projection</a> you will need to use a different projection if you want to display the pole regions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '14, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-37745" class="comments-container">
&#10;</div>
<div id="comment-tools-37745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37745-form-container" class="comment-form-container">
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

