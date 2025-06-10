+++
type = "question"
title = "OSM Vector Tiles creation and rendering methods and tools"
description = '''Hello, I&#x27;m starting to work on Vector Tiles creation from OSM data stored in my PostgreSQL database. And I&#x27;m curious to know:  Which tool and method OSM uses to create its vector tiles. Which tool/software/toolkit OSM then uses for rendering. I read somewhere that it uses Mapnik but I would need con...'''
date = "2020-09-25T10:38:00Z"
lastmod = "2020-09-25T18:06:00Z"
weight = 76809
keywords = [ "creation", "rendering", "tiles", "vector", "osm" ]
aliases = [ "/questions/76809" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Vector Tiles creation and rendering methods and tools](/questions/76809/osm-vector-tiles-creation-and-rendering-methods-and-tools)

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
<span id="post-76809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76809-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm starting to work on Vector Tiles creation from OSM data stored in my PostgreSQL database. And I'm curious to know:</p>
<ol>
<li>Which tool and method OSM uses to create its vector tiles.</li>
<li>Which tool/software/toolkit OSM then uses for rendering. I read somewhere that it uses Mapnik but I would need confirmation.</li>
</ol>
<p>I know there are many ways (and tools) of creating vector tiles (<a href="https://github.com/mapbox/awesome-vector-tiles/">mapbox/awesome-vector-tiles</a>) but I would really like to conform to the way OSM does it for its own website.</p>
<p>Thanks a lot for your answers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-creation" rel="tag" title="see questions tagged &#39;creation&#39;">creation</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '20, 10:38</strong></p>
<img src="https://secure.gravatar.com/avatar/823cd1782cf26169746327eb33ec93a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Flo%20Sophia&#39;s gravatar image" />
<p><span>Flo Sophia</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Flo Sophia has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76809" class="comments-container">
&#10;</div>
<div id="comment-tools-76809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76809-form-container" class="comment-form-container">
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

<span id="76811"></span>

<div id="answer-container-76811" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76811-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>OSM is an ecosystem and there can be different places with vector tiles based on OSM data.</li>
<li>OSM.org presents few different maps (layers), and the default is based on OSM Carto style, which is not a vector style at all, it's purely a raster one.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '20, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-76811" class="comments-container">
<span id="76818"></span>
<div id="comment-76818" class="comment">
<div id="post-76818-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. But maybe my questions were not properly phrased.</p>
<p>What I'm actually after is to know which tools are used by OSM to create and then render the vector tiles: t-rex? Tegola? etc. and then Mapnik? OpenLayers?</p>
</div>
<div id="comment-76818-info" class="comment-info">
<span class="comment-age">(25 Sep '20, 16:30)</span> <span class="comment-user userinfo">Flo Sophia</span>
</div>
</div>
<span id="76819"></span>
<div id="comment-76819" class="comment">
<div id="post-76819-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>To reiterate - it's raster tiles, not vector tiles. The software stack is similar to what you get via <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> (except much more complicated, as there are different servers serving different parts of the world).</p>
<p>The final "display" bit is using Leaflet, not OpenLayers.</p>
</div>
<div id="comment-76819-info" class="comment-info">
<span class="comment-age">(25 Sep '20, 16:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="76820"></span>
<div id="comment-76820" class="comment">
<div id="post-76820-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The base question is what do you mean by "OSM". Please be more specific.</p>
<p>In general sense (1) it's a broad community, which uses multiple tools for different needs, including raster or vector tiles. If you mean (2) OSM.org website, than the answer is "they don't use vector tiles there".</p>
<p>When it comes to OSM.org standard map layer, it uses OSM Carto style, which is rendered by Mapnik. But that is not the end of the road - the tiles are simply just a bunch of raster square images, nothing more. Than something like Leaflet library is used to serve the tiles in a consistent way as a map you can drag and zoom in a browser. You can read more about it here:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Slippy_Map#OpenStreetMap_.22Standard.22_tile_server">https://wiki.openstreetmap.org/wiki/Slippy_Map#OpenStreetMap_.22Standard.22_tile_server</a></p>
<p>I'm not sure what do you ask exactly, so please give more details.</p>
</div>
<div id="comment-76820-info" class="comment-info">
<span class="comment-age">(25 Sep '20, 17:16)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="76821"></span>
<div id="comment-76821" class="comment">
<div id="post-76821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for those details.</p>
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: The link you provided will help me, thanks!</p>
<p><a href="https://help.openstreetmap.org/users/11332/kocio">@kocio</a>: Sorry, I was indeed not clear at all. When I said "OSM" I was actually talking about the website and the technology behind, which serves the maps. And I also thought that the server used "vector" tiles and not "raster" tiles.</p>
<p>Thanks again to both of you. The information you provided really makes things clearer for me.</p>
</div>
<div id="comment-76821-info" class="comment-info">
<span class="comment-age">(25 Sep '20, 18:06)</span> <span class="comment-user userinfo">Flo Sophia</span>
</div>
</div>
</div>
<div id="comment-tools-76811" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76811-form-container" class="comment-form-container">
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

