+++
type = "question"
title = "Serving Tiles (with style) in 4326"
description = '''Is it possible to serve files in SRS 4326? I am following the directions for deploying my own server, and in the section for OSM Bright I see a snippet regarding WGS84 (what I think is 4326), but that&#x27;s all I see. I am able to get my tiles to display, but there&#x27;s ZERO style overlayed on them. All I ...'''
date = "2016-10-28T14:27:00Z"
lastmod = "2016-11-02T23:37:00Z"
weight = 52724
keywords = [ "wgs84" ]
aliases = [ "/questions/52724" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Serving Tiles (with style) in 4326](/questions/52724/serving-tiles-with-style-in-4326)

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
<span id="post-52724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52724-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to serve files in SRS 4326? I am following the directions for deploying my own server, and in the section for OSM Bright I see a snippet regarding WGS84 (what I think is 4326), but that's all I see.</p>
<p>I am able to get my tiles to display, but there's ZERO style overlayed on them. All I see is the planet without any cities, roads, etc.</p>
<p>Am I on the wrong track?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wgs84" rel="tag" title="see questions tagged &#39;wgs84&#39;">wgs84</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '16, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/fbe7fec63244565a6dc744a1b1f48e99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ismail44&#39;s gravatar image" />
<p><span>ismail44</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ismail44 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52724" class="comments-container">
<span id="52725"></span>
<div id="comment-52725" class="comment">
<div id="post-52725-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think so, but it depends what track you're following. Can you tell us what you have done so far? Lot of guidance you'll find is dedicated to give you a map in Mercator, so it can be a good idea to have a small extract of OSM rendered in this projection then adapt the database and style for 4326.</p>
</div>
<div id="comment-52725-info" class="comment-info">
<span class="comment-age">(29 Oct '16, 08:06)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
<span id="52729"></span>
<div id="comment-52729" class="comment">
<div id="post-52729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have followed the instructions for installing openstreet on ubuntu 14.04 from scratch to the letter. The only difference is that I am importing the planet with the "-l" switch in the osm2pgsql command.</p>
</div>
<div id="comment-52729-info" class="comment-info">
<span class="comment-age">(29 Oct '16, 14:25)</span> <span class="comment-user userinfo">ismail44</span>
</div>
</div>
<span id="52733"></span>
<div id="comment-52733" class="comment">
<div id="post-52733-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you sure your style file works in 4326?</p>
</div>
<div id="comment-52733-info" class="comment-info">
<span class="comment-age">(29 Oct '16, 21:11)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
<span id="52734"></span>
<div id="comment-52734" class="comment">
<div id="post-52734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's what I think is wrong... my styles aren't showing up?</p>
</div>
<div id="comment-52734-info" class="comment-info">
<span class="comment-age">(30 Oct '16, 01:36)</span> <span class="comment-user userinfo">ismail44</span>
</div>
</div>
<span id="52735"></span>
<div id="comment-52735" class="comment">
<div id="post-52735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Before correcting your style, maybe try to render a map in Mercator if not already done.</p>
</div>
<div id="comment-52735-info" class="comment-info">
<span class="comment-age">(30 Oct '16, 06:26)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
<span id="52762"></span>
<div id="comment-52762" class="comment not_top_scorer">
<div id="post-52762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So... serving the tiles in spherical mercator worked just fine... I guess the trick now is going to be to find out how to serve them in lat/lon mercator... which, I would expect that I just need to find the correct .shp files for OSMBright in the correct mercator???</p>
</div>
<div id="comment-52762-info" class="comment-info">
<span class="comment-age">(31 Oct '16, 14:35)</span> <span class="comment-user userinfo">ismail44</span>
</div>
</div>
</div>
<div id="comment-tools-52724" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-52724-form-container" class="comment-form-container">
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

<span id="52769"></span>

<div id="answer-container-52769" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52769-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The style has a list of layers - usually in an .mml or .yml file - and each layer has projection information to go with it. Since OSMBright is made for a database imported in Mercator units, and yours is in latitude and longitude, nothing will work - in effect, your data for the whole world will crouch somewhere near "null island" in the sea off Africa.</p>
<p>But all is not lost, you just need to inform your style that the data source is in EPSG:4326 instead of Mercator, then things will work again as expected. Look for layers configured to access the database with something like</p>
<pre><code>&quot;srs&quot;: &quot;+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over&quot;</code></pre>
<p>and change that to</p>
<pre><code>&quot;srs&quot; : &quot;+init=epsg:4326&quot;</code></pre>
<p>BUT:</p>
<p>This whole exercise is only half of what you want. It is good that the style now knows your data source is in EPSG:4326 but you will also want to request tiles in that projection. It is no problem to use a command line tool like nik2img.py to create images in EPSG:4326 but all the standard tile generating programs like renderd etc. are geared towards the EPSG:3857 tiling scheme (where the world is quadratic). You'll have a hard time setting these standard utilities up to support non-mercator tiles because the assumption that standard mercator tiles are used is hardcoded in many places.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '16, 22:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52769" class="comments-container">
<span id="52770"></span>
<div id="comment-52770" class="comment">
<div id="post-52770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@frederik</a>, thanks for a very insightful comment. I am getting my tiles from osm in .pbf format and using osm2pgsql to import them. If I pass in the "-l" option, would that take care of my tile generation problem (Assuming, of course, that I fix the style's mercation)?</p>
</div>
<div id="comment-52770-info" class="comment-info">
<span class="comment-age">(31 Oct '16, 23:41)</span> <span class="comment-user userinfo">ismail44</span>
</div>
</div>
<span id="52806"></span>
<div id="comment-52806" class="comment">
<div id="post-52806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The maps that you can produce are (unless we're talking north and south of 85°) the <em>same</em>, wether you import without <code>-l</code> and use the unmodified style, or import with <code>-l</code> and correct for that in the style. The thing you want to do differently is the actual production of the tiles. The problem with that is that the "Google Mercator" tiling scheme is standardised and well documented - if you give me the coordinates of a tile I can tell you exactly what's going to be on that tile. But to my knowledge an EPSG:4326 tile scheme is not standardised. It begins with the world tile at zoom 0 - in Google Mercator this is obvious, it's one single quadratic tile. But in EPSG:4326 the world is a rectangle twice as wide as it is high. Does that mean we have two tiles on z0? Or one tile where the bottom half is empty? Or the top half? Or 64 pixels unused above the world image and 64 pixels below? When a certain tile is requested, the rendering engine needs to know which bounding box to render the tile for, and this will be hard-wired to EPSG:3857 in most setups.</p>
</div>
<div id="comment-52806-info" class="comment-info">
<span class="comment-age">(02 Nov '16, 23:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52769-form-container" class="comment-form-container">
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

