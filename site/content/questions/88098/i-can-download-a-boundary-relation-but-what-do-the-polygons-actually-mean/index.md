+++
type = "question"
title = "I can download a boundary relation but what do the polygons actually mean?"
description = '''Hi, I have an overpass API that retrieves me all the ways and nodes of the admin level 2 boundary for a given country. My example is Spain. area[&quot;ISO3166-1&quot;=ES];(rel(pivot);nw(r);node(w););out; I postprocess the data I get from this and end up with 21 closed polygons. One of the polygons is made up ...'''
date = "2023-12-29T15:25:00Z"
lastmod = "2024-01-25T09:39:00Z"
weight = 88098
keywords = [ "polygons" ]
aliases = [ "/questions/88098" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I can download a boundary relation but what do the polygons actually mean?](/questions/88098/i-can-download-a-boundary-relation-but-what-do-the-polygons-actually-mean)

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
<span id="post-88098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88098-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have an overpass API that retrieves me all the ways and nodes of the admin level 2 boundary for a given country. My example is Spain.</p>
<p>area["ISO3166-1"=ES];(rel(pivot);nw(r);node(w););out;</p>
<p>I postprocess the data I get from this and end up with 21 closed polygons. One of the polygons is made up of just one way:</p>
<p>Way ID = "46430215"</p>
<p>Which I believe is the maritime border for the island of Ibiza. There were no tags on the &lt;way&gt; though that told me this. I had to work it out manually using a totally unprogrmatic approach.</p>
<p>My ultimate aim is for a user to pick a location by long lat and then find out where this is. For this though I need to get polygons and check if the point is in a polygon. If it is, I need to tell the user something useful about the polygon like what it is called.</p>
<p>So how can I get information like this is an island and it is called Ibiza from OSM? the user could equally well of course chosen a point in the middle of mainland Spain or the Meditterranean Sea and I would want to give them relevant answers for these as well.</p>
<p>Any guidance on the approach I can use is most welcome, Chessel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '23, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a7c7c42b3ace9de1b7d8fd5592ece3ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chessel&#39;s gravatar image" />
<p><span>Chessel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88098" class="comments-container">
&#10;</div>
<div id="comment-tools-88098" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88098-form-container" class="comment-form-container">
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

<span id="88197"></span>

<div id="answer-container-88197" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88197-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There probably wouldn't be tags on the way if it exists just to be part of a <a href="https://wiki.openstreetmap.org/wiki/Relation:boundary">boundary relation</a>. A more general overview of how boundaries are recorded is <a href="https://wiki.openstreetmap.org/wiki/Boundaries">here</a> on the wiki. Whether the way is part of a hole in the area or an outline would depend on the role it had within the relation, which is also stored in the relation.</p>
<p>Overpass has an <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_(is_in)"><code>is_in</code> query</a> that should return all areas that encompass the supplied point(s). This data can be further processed to give relevant <code>name</code> tags etc.</p>
<p>It sounds to me like you might want reverse geocoding for a point you query. There are some <a href="https://wiki.openstreetmap.org/wiki/Geocoding#Comparison_of_HTTP_APIs">existing geocoders</a> that might get you something close to what you want with less effort.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '24, 23:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-88197" class="comments-container">
<span id="88199"></span>
<div id="comment-88199" class="comment">
<div id="post-88199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. I've been on a bit of a journey of discovery with OSM and my understanding of how to use it is improving. Thanks for your links. I now know what areas are and what reverse geotagging is having done that reading. Many thanks.</p>
</div>
<div id="comment-88199-info" class="comment-info">
<span class="comment-age">(25 Jan '24, 09:39)</span> <span class="comment-user userinfo">Chessel</span>
</div>
</div>
</div>
<div id="comment-tools-88197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88197-form-container" class="comment-form-container">
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

