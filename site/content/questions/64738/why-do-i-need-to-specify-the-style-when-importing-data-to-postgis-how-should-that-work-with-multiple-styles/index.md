+++
type = "question"
title = "Why do I need to specify the style when importing data to postgis? How should that work with multiple styles?"
description = '''Why do I need to specify the style when importing data to postgis? How should that work with multiple styles? The slightly longer version: I&#x27;d like to setup mapnik, so that it supports multiple styles. So far I have managed to get a tile server set up by following the instructions for Ubuntu 18.04 o...'''
date = "2018-07-15T15:19:00Z"
lastmod = "2018-07-15T16:30:00Z"
weight = 64738
keywords = [ "openstreetmap", "renderd", "osm2pgsql", "mapnik", "tileserver" ]
aliases = [ "/questions/64738" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why do I need to specify the style when importing data to postgis? How should that work with multiple styles?](/questions/64738/why-do-i-need-to-specify-the-style-when-importing-data-to-postgis-how-should-that-work-with-multiple-styles)

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
<span id="post-64738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64738-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why do I need to specify the style when importing data to postgis? How should that work with multiple styles?</p>
<p>The slightly longer version:</p>
<p>I'd like to setup mapnik, so that it supports multiple styles.</p>
<p>So far I have managed to get a tile server set up by following the instructions for Ubuntu 18.04 on <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">switch2osm.org</a> (and working around a couple of problems while doing that).</p>
<p>Having done that I want to add another style(osm-bright), but when I look at the installation instructions of the "original" openstreetmap.org style <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md">https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md</a> then I see that I would have needed to specify that style already when importing the data to postgis:</p>
<pre><code>osm2pgsql -d gis ~/path/to/data.osm.pbf --style openstreetmap-carto.style --tag-transform-script openstreetmap-carto.lua</code></pre>
<p><strong>Why does the style influence the database? How can I get multiple style to work?</strong> (Like at the german site <a href="http://www.openstreetmap.de/karte.html">http://www.openstreetmap.de/karte.html</a> where I can switch between styles on the right.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '18, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/943a788b771da12a63057582fbf250b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anuranpal&#39;s gravatar image" />
<p><span>anuranpal</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anuranpal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '18, 15:30</strong> </span></p>
</div>
</div>
<div id="comments-container-64738" class="comments-container">
&#10;</div>
<div id="comment-tools-64738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64738-form-container" class="comment-form-container">
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

<span id="64739"></span>

<div id="answer-container-64739" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64739-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="anuranpal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Different visual styles are written against different database schemas.</p>
<p>The osm2pgsql style file transforms OSM data into a particular database schema. Reading through openstreetmap-carto.style is a good enough way to see what it is doing.</p>
<p><a href="https://www.openstreetmap.de/karte.html">https://www.openstreetmap.de/karte.html</a> is loading tiles from multiple servers, it is not rendering all the styles available.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '18, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-64739" class="comments-container">
&#10;</div>
<div id="comment-tools-64739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64739-form-container" class="comment-form-container">
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

