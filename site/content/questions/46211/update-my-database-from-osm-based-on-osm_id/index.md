+++
type = "question"
title = "Update my database from osm based on osm_id"
description = '''Hi, I want to store some data extracted from OSM (via overpass-api) into my database. Periodically (every month or year not decided yet), I want to search again for those nodes, ways or relations using osm_id and look for changes in the tags and update my database. can I count on the osm_id to retri...'''
date = "2015-10-29T10:18:00Z"
lastmod = "2015-10-29T18:01:00Z"
weight = 46211
keywords = [ "extract", "update", "osm_id" ]
aliases = [ "/questions/46211" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Update my database from osm based on osm_id](/questions/46211/update-my-database-from-osm-based-on-osm_id)

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
<span id="post-46211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46211-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to store some data extracted from OSM (via overpass-api) into my database. Periodically (every month or year not decided yet), I want to search again for those nodes, ways or relations using osm_id and look for changes in the tags and update my database. can I count on the osm_id to retrieve the same node, way or relation as I read that osm_ids my change.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-osm_id" rel="tag" title="see questions tagged &#39;osm_id&#39;">osm_id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Oct '15, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/395503aa766a76a0367248a7188c667c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Faissal%20Aeh&#39;s gravatar image" />
<p><span>Faissal Aeh</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Faissal Aeh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46211" class="comments-container">
&#10;</div>
<div id="comment-tools-46211" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46211-form-container" class="comment-form-container">
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

<span id="46217"></span>

<div id="answer-container-46217" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46217-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot count on OSM IDs being the same; it is probably better if you load all OSM data for the area in question and then check for another object that has the same (or somewhat the same) tags. One thing that might happen to POIs for example is that they are made into a building and therefore the same tags might now be attached to a different object.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '15, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46217" class="comments-container">
<span id="46225"></span>
<div id="comment-46225" class="comment">
<div id="post-46225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>but if we cannot count on osm_id there is, actually, no way to re-query a node representing a hotel for example just using the "tourism"="hotel" and the name tags cause they may change also.</p>
</div>
<div id="comment-46225-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 15:32)</span> <span class="comment-user userinfo">Faissal Aeh</span>
</div>
</div>
<span id="46226"></span>
<div id="comment-46226" class="comment">
<div id="post-46226-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, this is true. What exactly is your use case - what is your local database for, and why do you need to update it (instead of just repeating your overpass query)?</p>
</div>
<div id="comment-46226-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 15:45)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="46227"></span>
<div id="comment-46227" class="comment">
<div id="post-46227-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>First, thank you for responding. I want to have a list of hotels in my database (extracted from OSM). And periodically (for ex. every month or 3 months) I want to re-query those elements and if some information was changed (in OSM), I want to update my database with the last one (ex. phone number, stars, addresse...)</p>
</div>
<div id="comment-46227-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 16:00)</span> <span class="comment-user userinfo">Faissal Aeh</span>
</div>
</div>
<span id="46228"></span>
<div id="comment-46228" class="comment">
<div id="post-46228-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you already check <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Augmented_Delta_between_two_dates_.28.22adiff.22.29"><code>[adiff: ]</code></a> in the Overpass API documentation? This may be exactly what you're looking for.</p>
</div>
<div id="comment-46228-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 18:01)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-46217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46217-form-container" class="comment-form-container">
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

