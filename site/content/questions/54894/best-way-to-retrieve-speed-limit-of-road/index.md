+++
type = "question"
title = "best way to retrieve speed limit of road"
description = '''Hi,  I&#x27;m currently working on an application which returns the speed limit of the road a user is travelling on based on their longitude and latitude. I am currently doing this through two calls.  The first is to nominatim using the reverse geocoding feature to get the osm id. The second call is then...'''
date = "2017-03-03T18:17:00Z"
lastmod = "2017-03-04T23:22:00Z"
weight = 54894
keywords = [ "maxspeed" ]
aliases = [ "/questions/54894" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [best way to retrieve speed limit of road](/questions/54894/best-way-to-retrieve-speed-limit-of-road)

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
<span id="post-54894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54894-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm currently working on an application which returns the speed limit of the road a user is travelling on based on their longitude and latitude. I am currently doing this through two calls.</p>
<p>The first is to nominatim using the reverse geocoding feature to get the osm id.</p>
<p>The second call is then to overpassapi to get the max speed of the road.</p>
<p>Is there a way I can limit it this to one call using either of these services or maybe another service I am unaware of?</p>
<p>Any help on the matter would be appreciated.</p>
<p>Sample calls:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=53.95090&amp;lon=-6.37792">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=53.95090&amp;lon=-6.37792</a></p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;way(144887813);out;">http://overpass-api.de/api/interpreter?data=[out:json];way(144887813);out;</a></p>
<p>J</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '17, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/5dbcaa427d466b90c22c6385137ef171?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tj15&#39;s gravatar image" />
<p><span>tj15</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tj15 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54894" class="comments-container">
&#10;</div>
<div id="comment-tools-54894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54894-form-container" class="comment-form-container">
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

<span id="54896"></span>

<div id="answer-container-54896" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54896-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tj15 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps you could retrieve all roads around your current location with Overpass' <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29">around function</a>, so you do not need the Nominatim call ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '17, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-54896" class="comments-container">
<span id="54905"></span>
<div id="comment-54905" class="comment">
<div id="post-54905-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes I have been looking into this function and it does seem to be more suitable, rather than making the two calls. Thanks for your help!</p>
</div>
<div id="comment-54905-info" class="comment-info">
<span class="comment-age">(04 Mar '17, 23:22)</span> <span class="comment-user userinfo">tj15</span>
</div>
</div>
</div>
<div id="comment-tools-54896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54896-form-container" class="comment-form-container">
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

