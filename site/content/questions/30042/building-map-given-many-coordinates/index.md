+++
type = "question"
title = "Building Map, Given Many Coordinates"
description = '''Ok, I am trying to get an idea of where to start with this. I have:  1. A fixed height and width for a display window  2. A list of many coordinates My end-goal is to query OSM for a map (of the given height and width) which contains all of the coordinates. It will be a static map, so not interactiv...'''
date = "2014-01-21T21:10:00Z"
lastmod = "2014-01-22T04:24:00Z"
weight = 30042
keywords = [ "dimensions" ]
aliases = [ "/questions/30042" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Building Map, Given Many Coordinates](/questions/30042/building-map-given-many-coordinates)

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
<span id="post-30042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30042-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ok, I am trying to get an idea of where to start with this.</p>
<p>I have: 1. A fixed height and width for a display window 2. A list of many coordinates</p>
<p>My end-goal is to query OSM for a map (of the given height and width) which contains all of the coordinates. It will be a static map, so not interactive. I understand how to get a single map tile of 256x256, but I don't understand how to get a map of many tiles. I think the way OSM used to work (it's been several years) is that I provided it a center coordinate, a height and width, and a zoom level, and it would give me a map of all the tiles which would fill in the given area. The URL has changed since then, and it no longer seems that I can send it a height and width in the url, so I'm a bit lost. Can anyone point me in the correct direction?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dimensions" rel="tag" title="see questions tagged &#39;dimensions&#39;">dimensions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '14, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a36c891e7c5533a9297fc6c5afd52ca9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aussiemcgr&#39;s gravatar image" />
<p><span>aussiemcgr</span><br />
<span class="score" title="30 reputation points">30</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aussiemcgr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30042" class="comments-container">
<span id="30043"></span>
<div id="comment-30043" class="comment">
<div id="post-30043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm sorry, but what are you talking about and what is your question exactly?</p>
</div>
<div id="comment-30043-info" class="comment-info">
<span class="comment-age">(21 Jan '14, 21:18)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="30051"></span>
<div id="comment-30051" class="comment">
<div id="post-30051-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a program, and I am querying OSM for a static map with the URL. For example, this link describes how to get a single tile: <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames</a> The problem is that a single 256x256 tile will not fit my needs. There used to be a way to query a whole map (consisting of several tiles), but I can't seem to figure out how to do that anymore. The old URL has been deprecated.</p>
</div>
<div id="comment-30051-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 00:24)</span> <span class="comment-user userinfo">aussiemcgr</span>
</div>
</div>
</div>
<div id="comment-tools-30042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30042-form-container" class="comment-form-container">
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

<span id="30052"></span>

<div id="answer-container-30052" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30052-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap isn't actually a mapping service, so you don't need to "query OSM for a map". At its heart it's just <a href="http://planet.openstreetmap.org/">a big lump of data</a> that you can download, or <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Downloading">download extracts from</a>, and use yourself to either create tiles from (if you want map tiles) or extract points of interest, or whatever else you want to do.</p>
<p>If you want to create "a map of many tiles" <a href="http://switch2osm.org/serving-tiles/">these instructions</a> provide one way to do it based on data that you've downloaded previously (although that's just one way of displaying data on a map, and each of the components involved even in doing that has alternatives).</p>
<p>Just as you're free to use OSM data to provide a map other people are too, and there may well be someone that operates an API that works in the way that you describe (at a stretch, it's close to how tile rendering libraries such as <a href="http://leafletjs.com/">Leaflet</a> work - and again, other display libraries are available). If you want to extract data rather than render tiles, services such as <a href="http://wiki.osm.org/wiki/Overpass_API">Overpass</a> might be useful.</p>
<p>However, as <span>@iii</span> says, it's not immediately clear what you're describing - maybe if you can provide the URL that you used to use, people would know more about what you're trying to do?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 00:35</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-30052" class="comments-container">
<span id="30054"></span>
<div id="comment-30054" class="comment">
<div id="post-30054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a java applet, and the user has a list of coordinates. My goal is to just render a map which contains all the user's coordinates. The map I render doesn't need to do anything special because I intend to paint interactive items over top of the map image in java (points, lines, the ability for the user to draw lines, ect.). So all I need is the static map image, but it will differ for each user, which is why I can't just save some single map image for all the users to use.</p>
</div>
<div id="comment-30054-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 04:24)</span> <span class="comment-user userinfo">aussiemcgr</span>
</div>
</div>
<span id="30055"></span>
<div id="comment-30055" class="comment">
<div id="post-30055-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The old url I used to use looked like this: <a href="http://pafciu17.dev.openstreetmap.org/?module=map&amp;lon=">http://pafciu17.dev.openstreetmap.org/?module=map&amp;lon="+currLong+"&amp;lat="+currLat+"&amp;zoom="+currZoom+"&amp;width="+currWidth+"&amp;height="+currHeight+"&amp;type=mapnik&amp;imgType=gif</a></p>
<p>The variables concatenated into the url was determined at runtime. This worked several years ago (like 3 years ago, I think), but I believe pafciu17 has been shut down since then.</p>
</div>
<div id="comment-30055-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 04:24)</span> <span class="comment-user userinfo">aussiemcgr</span>
</div>
</div>
</div>
<div id="comment-tools-30052" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30052-form-container" class="comment-form-container">
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

