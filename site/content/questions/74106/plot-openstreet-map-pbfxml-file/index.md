+++
type = "question"
title = "Plot OpenStreet Map pbf/xml file"
description = '''I have downloaded the pbf file of OpenStreet Map historical data from this site https://planet.openstreetmap.org/planet/full-history . How can I plot the graph using python?'''
date = "2020-04-12T08:49:00Z"
lastmod = "2020-04-13T06:35:00Z"
weight = 74106
keywords = [ "openstreetmap", "python", "graph" ]
aliases = [ "/questions/74106" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Plot OpenStreet Map pbf/xml file](/questions/74106/plot-openstreet-map-pbfxml-file)

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
<span id="post-74106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74106-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded the pbf file of OpenStreet Map historical data from this site <a href="https://planet.openstreetmap.org/planet/full-history">https://planet.openstreetmap.org/planet/full-history</a> . How can I plot the graph using python?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '20, 08:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a8715c0057b4a180446b8bf89be9cb37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Satabdi&#39;s gravatar image" />
<p><span>Satabdi</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Satabdi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '20, 08:52</strong> </span></p>
</div>
</div>
<div id="comments-container-74106" class="comments-container">
&#10;</div>
<div id="comment-tools-74106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74106-form-container" class="comment-form-container">
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

<span id="74108"></span>

<div id="answer-container-74108" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74108-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For maps, we don't use the term "plot a graph" - we speak of "rendering a map". While plotting a graph usually involves nothing more than saying "here's a bunch of numbers, please draw this" (and perhaps adding "... with a blue line"), rendering a map is vastly more complicated, as you will need drawing styles for every single feature, and potentially on different zoom levels.</p>
<p>To make matters even more complicated, the history file not only contains different map features, but timestamps as well. You cannot (easily) render a map that shows different times; you will first have to decide which date you want to draw a map for, so you'll want to use the <code>osmium</code> command line tool to extract the data for a specific date. Then you can proceed with rendering it; if you want to render the map for the whole planet you might need to load the data into a PostgreSQL data base with osm2pgsql then render with a tile server (Mapnik, renderd), or if you only want a small area then you can again use osmium to excerpt that area from the history file and render it with something like Maperitive or even QGIS.</p>
<p>You will need to tell us more about what you want to do in order for us to help you better!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '20, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-74108" class="comments-container">
<span id="74109"></span>
<div id="comment-74109" class="comment">
<div id="post-74109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to work with a particular country/small place Like Bangladesh. How can I do that? Do you have any tutorial link? so that I can get some help from there</p>
</div>
<div id="comment-74109-info" class="comment-info">
<span class="comment-age">(12 Apr '20, 11:17)</span> <span class="comment-user userinfo">Satabdi</span>
</div>
</div>
<span id="74112"></span>
<div id="comment-74112" class="comment">
<div id="post-74112-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you looking to make a web map, a printed map, or what? And do you want current data or old (historic) data?</p>
</div>
<div id="comment-74112-info" class="comment-info">
<span class="comment-age">(12 Apr '20, 17:06)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="74122"></span>
<div id="comment-74122" class="comment">
<div id="post-74122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to work with the data from 2014-2020. I want to work with the changes in the road network of a place in Python environment.</p>
</div>
<div id="comment-74122-info" class="comment-info">
<span class="comment-age">(13 Apr '20, 06:35)</span> <span class="comment-user userinfo">Satabdi</span>
</div>
</div>
</div>
<div id="comment-tools-74108" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74108-form-container" class="comment-form-container">
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

