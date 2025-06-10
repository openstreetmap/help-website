+++
type = "question"
title = "[closed] Distance Between Nodes"
description = '''I want to implement the shortest path algorithm using the OSM data but i dont know how to get the distance between nodes(http://api.openstreetmap.org/api/0.6/map?bbox=11.54,48.14,11.543,48.145 in this file for example. where is the distance between nodes?) how can i get the distance between nodes us...'''
date = "2014-01-27T12:18:00Z"
lastmod = "2014-01-27T12:42:00Z"
weight = 30252
keywords = [ "node", "api", "osm", "routing" ]
aliases = [ "/questions/30252" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Distance Between Nodes](/questions/30252/distance-between-nodes)

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
<span id="post-30252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30252-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to implement the shortest path algorithm using the OSM data but i dont know how to get the distance between nodes(<a href="http://api.openstreetmap.org/api/0.6/map?bbox=11.54,48.14,11.543,48.145">http://api.openstreetmap.org/api/0.6/map?bbox=11.54,48.14,11.543,48.145</a> in this file for example. where is the distance between nodes?)</p>
<p>how can i get the distance between nodes using the OSM data? i am newbie using the opensteetmap.</p>
<p>thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '14, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/c090a639a333b8072c9ebe6ece32008e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kenji%20Gabriel&#39;s gravatar image" />
<p><span>Kenji Gabriel</span><br />
<span class="score" title="-1 reputation points">-1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kenji Gabriel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>27 Jan '14, 12:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-30252" class="comments-container">
&#10;</div>
<div id="comment-tools-30252" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30252-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Frederik Ramm 27 Jan '14, 12:34

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30253"></span>

<div id="answer-container-30253" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30253-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are several very good routing engines for OpenStreetMap data already. The distance between two locations given in lat,lon coordinates on the Earth's surface is called the "Great Circle Distance" and can be computed using, among others, the so-called Haversine formula. This is not really an OpenStreetMap related question so I'm closing it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '14, 12:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30253" class="comments-container">
<span id="30254"></span>
<div id="comment-30254" class="comment">
<div id="post-30254-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to add to that - this page of the beginners' guide explains a bit about the data in OSM (and in the file that you downloaded):</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Beginners_Guide_1.3">http://wiki.openstreetmap.org/wiki/Beginners_Guide_1.3</a></p>
<p>The distance been points isn't in the file, but their place on the surface of the earth is. In addition, bear in mind that you don't need to use an API call to obtain OSM data - just download one of the extracts linked from this page:</p>
<p><a href="http://planet.openstreetmap.org/">http://planet.openstreetmap.org/</a></p>
</div>
<div id="comment-30254-info" class="comment-info">
<span class="comment-age">(27 Jan '14, 12:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30253-form-container" class="comment-form-container">
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

