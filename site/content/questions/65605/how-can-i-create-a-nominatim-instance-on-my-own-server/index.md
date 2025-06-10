+++
type = "question"
title = "How can I create a Nominatim instance on my own server?"
description = '''I need somehow to download the database to my own server, then search through the database to find places names by latitude and longitude and return the results in JSON format. In other words: I need to create a copy of this service: link. I&#x27;m wondering because I read about the limits of this API (1...'''
date = "2018-08-28T08:55:00Z"
lastmod = "2018-08-28T10:29:00Z"
weight = 65605
keywords = [ "nominatim", "database" ]
aliases = [ "/questions/65605" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I create a Nominatim instance on my own server?](/questions/65605/how-can-i-create-a-nominatim-instance-on-my-own-server)

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
<span id="post-65605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65605-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need somehow to download the database to my own server, then search through the database to find places names by latitude and longitude and return the results in JSON format. In other words: I need to create a copy of this service: <a href="https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=40.758896&amp;lon=-73.985130&amp;zoom=218&amp;addressdetails=1&amp;accept-language=null">link</a>.</p>
<p>I'm wondering because I read about the limits of this API (1 request per second) and it's not fits my requirements, so I decided to create my own instance. Any help? I've searched a lot, but couldn't find any suggestions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '18, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/04f1539a79e0f4b65a42046c1037949f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fergv1&#39;s gravatar image" />
<p><span>Fergv1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fergv1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65605" class="comments-container">
&#10;</div>
<div id="comment-tools-65605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65605-form-container" class="comment-form-container">
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

<span id="65606"></span>

<div id="answer-container-65606" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65606-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Download and install instructions on <a href="https://www.nominatim.org/">https://www.nominatim.org/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '18, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-65606" class="comments-container">
<span id="65608"></span>
<div id="comment-65608" class="comment">
<div id="post-65608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Fergv1, it would be great if you could explain to us exactly how you tried to find this ("I've searched a lot but couldn't find any suggestions") because the link that mtmail posted is really the first that anyone should come up with. If you tell us what you have searched for that <em>did't</em> yield this result, we can perhaps improve the page with suitable search terms.</p>
</div>
<div id="comment-65608-info" class="comment-info">
<span class="comment-age">(28 Aug '18, 10:29)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65606-form-container" class="comment-form-container">
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

