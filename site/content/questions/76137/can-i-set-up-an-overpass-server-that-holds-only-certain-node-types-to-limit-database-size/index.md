+++
type = "question"
title = "can I set-up an overpass server that holds only certain node types to limit database size?"
description = '''Hi, currently I am operating my own overpass-api server based upon the full osm data replication. This is quite resource intensive as about 450 Gbyte of local storage are required for this as it holds ALL OSM data and can be used to query all of it. But the use-case I have only requires certain amou...'''
date = "2020-08-16T09:00:00Z"
lastmod = "2020-08-16T10:34:00Z"
weight = 76137
keywords = [ "overpassapi", "overpass" ]
aliases = [ "/questions/76137" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can I set-up an overpass server that holds only certain node types to limit database size?](/questions/76137/can-i-set-up-an-overpass-server-that-holds-only-certain-node-types-to-limit-database-size)

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
<span id="post-76137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76137-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>currently I am operating my own overpass-api server based upon the full osm data replication.</p>
<p>This is quite resource intensive as about 450 Gbyte of local storage are required for this as it holds ALL OSM data and can be used to query all of it.</p>
<p>But the use-case I have only requires certain amounts of data to be available.</p>
<p>Is someone here that could help me finding out how I can set-up the overpass server so that only the required objects get stored and updated/filtered in the overpass database to have a smaller footprint?</p>
<p>Specifically this is the query that needs to be answered:</p>
<p>[out:json] [timeout:25]; ( node<a href="%7B%7Bbbox%7D%7D">amenity=toilets</a>; way<a href="%7B%7Bbbox%7D%7D">amenity=toilets</a>; relation<a href="%7B%7Bbbox%7D%7D">amenity=toilets</a>; ); out body;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '20, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/2dcdd6ad7f317c95755cb2d7cf4e4ff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bietiekay&#39;s gravatar image" />
<p><span>bietiekay</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bietiekay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76137" class="comments-container">
&#10;</div>
<div id="comment-tools-76137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76137-form-container" class="comment-form-container">
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

<span id="76138"></span>

<div id="answer-container-76138" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76138-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most systems that use Overpass in a "production" environment turn out to be not very well designed (or, to put it more favourably, turn out to be a proof of concept that has been promoted to production mode). Overpass is an all-purpose databsae system, striking a balance between being able to query very specific objects and also return data for large areas. Your use case would be much better served by an osm2pgsql import into a PostgreSQL database, using a style file that just imports toilets.</p>
<p>However - no matter which database system you use - you need to remember one thing regarding updates: If a way gets created then the nodes it uses will not be in the update. This means if someone constructs a way from pre-existing nodes and tags it <code>amenity=toilets</code> then you need to already have these nodes, or you don't know where the toilet is. Same for relations; if someone should construct a relation from two already-existing ways and tag it <code>amenity=toilets</code>, and you haven't kept the ways because they looked un-interesting, then you're screwed.</p>
<p>If you can live with an update frequency of once a day or less, then the least resource-intensive process might be this:</p>
<ul>
<li>keep a full planet file lying around</li>
<li>update it at the end of the day, or week, with either osmosis or pyosmium-up-to-date (the latter is faster)</li>
<li>filter the planet file to keep just amenity=toilets nodes/ways/relations, using osmosis or osmium (the latter is a lot faster)</li>
<li>import the resulting toilet dataset into Overpass or PostgreSQL</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '20, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-76138" class="comments-container">
<span id="76139"></span>
<div id="comment-76139" class="comment">
<div id="post-76139-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>AH! I see. My knowledge of the underlying data structures isn't good enough to have seen this connection of way and nodes.</p>
<p>Thanks a lot for pointing it out. I will give both your proposals a try - the postgresql and the overpass solution.</p>
<p>Right now the big-full-sync works but as the machine does only have mechanical hard disks right now at the required size I fear for their lives with the minute updates running constantly.</p>
<p>thanks a lot!</p>
</div>
<div id="comment-76139-info" class="comment-info">
<span class="comment-age">(16 Aug '20, 10:34)</span> <span class="comment-user userinfo">bietiekay</span>
</div>
</div>
</div>
<div id="comment-tools-76138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76138-form-container" class="comment-form-container">
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

