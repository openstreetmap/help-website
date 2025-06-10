+++
type = "question"
title = "nominatim reverse geocode city nearby"
description = '''i am trying to lookup localized city name from gps position via nominatim reverse call, which works pretty well when user is in town. But when in the middle of nowhere (e.g. user is anchored with his yacht near the coast), nominatim return only the administrative region. example: https://nominatim.o...'''
date = "2020-10-30T14:54:00Z"
lastmod = "2020-11-16T08:46:00Z"
weight = 77325
keywords = [ "reversegeocoding", "nominatim", "nearby", "city" ]
aliases = [ "/questions/77325" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim reverse geocode city nearby](/questions/77325/nominatim-reverse-geocode-city-nearby)

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
<span id="post-77325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77325-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i am trying to lookup localized city name from gps position via nominatim reverse call, which works pretty well when user is in town. But when in the middle of nowhere (e.g. user is anchored with his yacht near the coast), nominatim return only the administrative region. example: <a href="https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;lat=36.540548&amp;lon=35.742612&amp;zoom=18">https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;lat=36.540548&amp;lon=35.742612&amp;zoom=18</a> the same is returned without reverse: <a href="https://nominatim.openstreetmap.org/search?format=jsonv2&amp;q=36.540548,35.742612&amp;zoom=18">https://nominatim.openstreetmap.org/search?format=jsonv2&amp;q=36.540548,35.742612&amp;zoom=18</a> What we need is the name of the nearest town. Any suggestions, experiences or hacks (e.g. town of next atm or something) to get that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-nearby" rel="tag" title="see questions tagged &#39;nearby&#39;">nearby</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '20, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/6a6ea04c3737ab2722b2e667aa532757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qeepcologne&#39;s gravatar image" />
<p><span>qeepcologne</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qeepcologne has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77325" class="comments-container">
&#10;</div>
<div id="comment-tools-77325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77325-form-container" class="comment-form-container">
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

<span id="77332"></span>

<div id="answer-container-77332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim, being a reverse geocoder aiming to give you the address for your location, is the wrong tool for this job.</p>
<p>Overpass is a slightly better tool; it cannot (to my knowledge) give you the "closest" of something but it can give you "nearby things" in a given radius - here, all cities and towns within 50km of the given position:</p>
<pre><code>node(around:50000,53.6509,6.8310)[place~&quot;^(city|town)$&quot;];
out geom;</code></pre>
<p>The task of identifying the closest of several results would still be yours to solve, and this solution would, unlike Nominatim, not tell you the administrative hierarchy (i.e. what county/state/country the city is in).</p>
<p>The best solution would probably be a server that you run yourself, with OSM data imported into a PostGIS database and a small script that would run a nearest-neighbour search in the database and return only the closest place. This would have the added advantage of not relying on servers run by other people.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '20, 19:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-77332" class="comments-container">
<span id="77566"></span>
<div id="comment-77566" class="comment">
<div id="post-77566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks a lot, i tried with your query on overpass-turbo and results are looking ok. We run nominatim (via docker image) on our own server. I used the openstreemap.org url to demonstrate the query to work for everybody, because our server is not public. So i have to find out how to run/install nominatim and overpass on the same database via docker.</p>
</div>
<div id="comment-77566-info" class="comment-info">
<span class="comment-age">(16 Nov '20, 08:46)</span> <span class="comment-user userinfo">qeepcologne</span>
</div>
</div>
</div>
<div id="comment-tools-77332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77332-form-container" class="comment-form-container">
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

