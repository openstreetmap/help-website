+++
type = "question"
title = "Problem with rendering water from Overpass data"
description = '''EDIT:  The question is also posted here: http://forum.openstreetmap.org/viewtopic.php?id=55126 In the past, I thought thay it might be a problem with Maperitive, but apparently it is not: https://groups.google.com/forum/m/#!msg/maperitive/-aXn7-2_f-4/nrVaQJ18HgAJ Hello! I am trying to render a simpl...'''
date = "2016-07-13T14:12:00Z"
lastmod = "2016-07-18T12:42:00Z"
weight = 50891
keywords = [ "water", "overpass", "overpassapi", "maperitive", "query" ]
aliases = [ "/questions/50891" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with rendering water from Overpass data](/questions/50891/problem-with-rendering-water-from-overpass-data)

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
<span id="post-50891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50891-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>EDIT: The question is also posted here: <a href="http://forum.openstreetmap.org/viewtopic.php?id=55126">http://forum.openstreetmap.org/viewtopic.php?id=55126</a></p>
<p>In the past, I thought thay it might be a problem with Maperitive, but apparently it is not: <a href="https://groups.google.com/forum/m/#!msg/maperitive/-aXn7-2_f-4/nrVaQJ18HgAJ">https://groups.google.com/forum/m/#!msg/maperitive/-aXn7-2_f-4/nrVaQJ18HgAJ</a></p>
<p>Hello! I am trying to render a simple but complete map of a 18x18km city area.</p>
<p>I extract data from my own instance of OverpassAPI, using query given below, and then open extracted *.osm file in Maperitive and render a bitmap.</p>
<p>My example query for NYC:</p>
<pre><code>[timeout:3600];(node(40.64975,-74.09327,40.811447,-73.87989);rel(bn)-&gt;.x;way(bn);rel(bw););(._;way(r););(._;node(r)-&gt;.x;node(w););(._;rel(br);rel(br);rel(br);rel(br););out;</code></pre>
<p>Example map - as you can clearly see, a huge part of water is not rendered at all:</p>
<p><img src="/upfiles/NYC.jpg" alt="alt text" /></p>
<p>P.S. Someone has already advised me to download data from geofabrik, and extract a piece of it with osmconvert, using the 'keep ways and areas complete, even if they cross the border' option. It works just fine, but is 10x slower than downloading data from Overpass. I am pretty sure that it is possible to write a Overpass query which will fit my needs, but the query language is difficult. Help me please!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '16, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/83574717ad22ec1c6ed654911a88ff9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kervyn&#39;s gravatar image" />
<p><span>Kervyn</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kervyn has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '16, 10:09</strong> </span></p>
</div>
</div>
<div id="comments-container-50891" class="comments-container">
<span id="50894"></span>
<div id="comment-50894" class="comment">
<div id="post-50894-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Did you check your .osm file in JOSM already to see if it includes all relevant data?</p>
</div>
<div id="comment-50894-info" class="comment-info">
<span class="comment-age">(13 Jul '16, 14:48)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="50900"></span>
<div id="comment-50900" class="comment">
<div id="post-50900-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Cross posted: <a href="http://forum.openstreetmap.org/viewtopic.php?pid=600156#p600156">http://forum.openstreetmap.org/viewtopic.php?pid=600156#p600156</a></p>
</div>
<div id="comment-50900-info" class="comment-info">
<span class="comment-age">(13 Jul '16, 18:47)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-50891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50891-form-container" class="comment-form-container">
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

<span id="50901"></span>

<div id="answer-container-50901" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50901-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know enough about coastline rendering to be positive, but if you have a look at <a href="https://www.openstreetmap.org/way/179057060">one of the ways where your water stops</a> you'll see that it's only part of one multipolygon. Hence your map is rendering the data correctly: there is actually nothing in the data that would imply this is water. That has something to do with this being the sea: in OpenStreetMap, coastlines are treated a bit special. A dataset defining the main bodies of water is kept a little separate from the general database, to define main landmasses and oceans. This is to avoid the constant flooding of continents you would see everytime someone makes a tiny mistake when editing coastlines.</p>
<p>I guess you might solve it for your usecase by closing your landmasses along the border of your area, and defining everything not enclosed as sea.</p>
<p>I'm sure others can give a more exact answer as to the rendering of coastlines.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '16, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-50901" class="comments-container">
<span id="50905"></span>
<div id="comment-50905" class="comment">
<div id="post-50905-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks joost! It would be quite difficult to write a tool automatically closing the landmasses as you suggest, though. I hope that somebody will help me rewrite the query, or suggest other solution to download the data (including water) properly ;-)</p>
</div>
<div id="comment-50905-info" class="comment-info">
<span class="comment-age">(14 Jul '16, 11:23)</span> <span class="comment-user userinfo">Kervyn</span>
</div>
</div>
<span id="50965"></span>
<div id="comment-50965" class="comment">
<div id="post-50965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I'm not sure if there's a way to let overpass return you data that doesn't exist :) (i.e. continents aren't regular polygons in OSM) But you could refrase your question into "how to get closed landmasses with overpass" or something like that. Other than that, I would think the simplest way would be to manually create a polygon for the area you need.</p>
</div>
<div id="comment-50965-info" class="comment-info">
<span class="comment-age">(18 Jul '16, 10:58)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="50967"></span>
<div id="comment-50967" class="comment">
<div id="post-50967-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This might help too: <a href="http://maperitive.net/docs/Rendering_Coastlines_And_Sea.html">http://maperitive.net/docs/Rendering_Coastlines_And_Sea.html</a></p>
</div>
<div id="comment-50967-info" class="comment-info">
<span class="comment-age">(18 Jul '16, 12:42)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-50901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50901-form-container" class="comment-form-container">
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

