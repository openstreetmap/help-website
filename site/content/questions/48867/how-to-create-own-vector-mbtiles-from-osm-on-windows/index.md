+++
type = "question"
title = "How to create own vector mbtiles from OSM on Windows ?"
description = '''Hi, I&#x27;m trying to create vector mbtiles and style them from OSM data. I used the steps outlined: https://sourceforge.net/p/topomapcreator/wiki/TileMill/ I downloaded .osm data and convert them to PostGIS then used OSM bright style and was able to see the map come nicely and styled using TileMill (de...'''
date = "2016-03-27T16:47:00Z"
lastmod = "2017-06-16T13:49:00Z"
weight = 48867
keywords = [ "windows", "osm", "mapnik", "postgis", "mbtiles" ]
aliases = [ "/questions/48867" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create own vector mbtiles from OSM on Windows ?](/questions/48867/how-to-create-own-vector-mbtiles-from-osm-on-windows)

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
<span id="post-48867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48867-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to create vector mbtiles and style them from OSM data. I used the steps outlined: <a href="https://sourceforge.net/p/topomapcreator/wiki/TileMill/">https://sourceforge.net/p/topomapcreator/wiki/TileMill/</a></p>
<p>I downloaded .osm data and convert them to PostGIS then used OSM bright style and was able to see the map come nicely and styled using TileMill (desktop app). Now I wanted to export the tiles to mbtiles format so I can self host them with their styles. When I tried this, TileMill wanted to create a large mbtiles file. From searching on the web, TileMill seems to generate raster files and hence the large size. My goal is to generate a vector based mbtiles (smaller size and more flexible for styling).</p>
<p>Are there alternatives on Windows to generate vector mbtiles either from .osm or .osm converted to PostGIS ?</p>
<p>Thanks for any hints or pointers.</p>
<p>Jeff</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '16, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/3f3eee6fe4d19e7b5080999ffcb1b44e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeff_Lacoste&#39;s gravatar image" />
<p><span>Jeff_Lacoste</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeff_Lacoste has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '16, 12:50</strong> </span></p>
</div>
</div>
<div id="comments-container-48867" class="comments-container">
<span id="48877"></span>
<div id="comment-48877" class="comment">
<div id="post-48877-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For MapBox specific product questions (anything that has to do with an account on their system and so on) you need to ask MapBox sales and support not here.</p>
</div>
<div id="comment-48877-info" class="comment-info">
<span class="comment-age">(28 Mar '16, 11:39)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="48880"></span>
<div id="comment-48880" class="comment">
<div id="post-48880-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for clarification. I edited my question to be OSM only.</p>
</div>
<div id="comment-48880-info" class="comment-info">
<span class="comment-age">(28 Mar '16, 12:51)</span> <span class="comment-user userinfo">Jeff_Lacoste</span>
</div>
</div>
</div>
<div id="comment-tools-48867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48867-form-container" class="comment-form-container">
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

<span id="48868"></span>

<div id="answer-container-48868" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48868-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure there is really a mature stack yet, but there are alternatives. One is Tilemaker:</p>
<p><a href="http://blog.systemed.net/post/13">http://blog.systemed.net/post/13</a></p>
<p>And recently <a href="http://osm2vectortiles.org/">http://osm2vectortiles.org/</a> .</p>
<p>(There's probably more worth mentioning, but those are projects with recent activity)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '16, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-48868" class="comments-container">
<span id="48882"></span>
<div id="comment-48882" class="comment">
<div id="post-48882-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you 'maxerickson' for your response. I checkout 'TileMaker' but unfortunately its not built on Windows as I'm using Windows. Also I checkout <a href="http://osm2vectortiles.org/">http://osm2vectortiles.org/</a> but in the doc how to create own tiles, it recommend using docker-compose that is not available on Windows. Also the how to use Docker is explained to a level that I can't just read and run with it.</p>
</div>
<div id="comment-48882-info" class="comment-info">
<span class="comment-age">(28 Mar '16, 15:41)</span> <span class="comment-user userinfo">Jeff_Lacoste</span>
</div>
</div>
<span id="56644"></span>
<div id="comment-56644" class="comment">
<div id="post-56644-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Meanwhile there is a successor to osm2vectortiles: <a href="https://openmaptiles.org/">https://openmaptiles.org/</a></p>
</div>
<div id="comment-56644-info" class="comment-info">
<span class="comment-age">(16 Jun '17, 13:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48868" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48868-form-container" class="comment-form-container">
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

