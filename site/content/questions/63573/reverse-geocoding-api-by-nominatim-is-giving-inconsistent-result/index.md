+++
type = "question"
title = "Reverse geocoding API by nominatim is giving inconsistent result"
description = '''Hello all, I&#x27;m trying to get value of the key &quot;city&quot; using latitude and longitude. But unfortunately, I&#x27;m not getting expected result most of the time. For example, the following API is giving correct value of city (&quot;Dhaka&quot;): https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;amp;lat=23.71238...'''
date = "2018-05-20T11:18:00Z"
lastmod = "2018-05-21T09:29:00Z"
weight = 63573
keywords = [ "reversegeocoding", "nominatim" ]
aliases = [ "/questions/63573" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Reverse geocoding API by nominatim is giving inconsistent result](/questions/63573/reverse-geocoding-api-by-nominatim-is-giving-inconsistent-result)

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
<span id="post-63573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63573-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>I'm trying to get value of the key "city" using latitude and longitude. But unfortunately, I'm not getting expected result most of the time.</p>
<p>For example, the following API is giving correct value of city ("Dhaka"): <a href="https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;lat=23.7123823525915215&amp;lon=90.4103022068739&amp;zoom=18">https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;lat=23.7123823525915215&amp;lon=90.4103022068739&amp;zoom=18</a></p>
<p>On the other hand, this API is not giving any value of city, whereas both of the locations are from same city: <a href="https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;lat=23.76615&amp;lon=90.35673&amp;zoom=18">https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;lat=23.76615&amp;lon=90.35673&amp;zoom=18</a></p>
<p>Any suggestion on how to get more consistent result?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '18, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/96e37ecee4689b2bc6a7a771c71eb5d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shamimabrishti&#39;s gravatar image" />
<p><span>shamimabrishti</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shamimabrishti has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63573" class="comments-container">
&#10;</div>
<div id="comment-tools-63573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63573-form-container" class="comment-form-container">
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

<span id="63585"></span>

<div id="answer-container-63585" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63585-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="shamimabrishti has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a data coverage issue in this case. The city of Dhaka is in OSM data <a href="https://www.openstreetmap.org/node/3442474911,">https://www.openstreetmap.org/node/3442474911,</a> but it doesn't have (administrative) boundaries, so Nominatim simply doesn't know how big it is. The center point of the city (that node) is too far away to make a guess. Somebody (that could be you, <a href="https://www.openstreetmap.org/fixthemap)">https://www.openstreetmap.org/fixthemap)</a> needs to change the OSM data to add boundaries.</p>
<p>An alternative is to add 'is_in' tags <a href="https://wiki.openstreetmap.org/wiki/Key:is_in">https://wiki.openstreetmap.org/wiki/Key:is_in</a> to the suburbs. So is_in:city=Dhaka to (1) Pisciculture Housing (2) Mohammadpur (3) Mohammadpur Future Town. I got the names of the nearby suburbs from <a href="https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=370027291">https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=370027291</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '18, 21:28</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-63585" class="comments-container">
<span id="63592"></span>
<div id="comment-63592" class="comment">
<div id="post-63592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot <a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a> for your effort, it was really helpful. I'll work on your suggestion :)</p>
</div>
<div id="comment-63592-info" class="comment-info">
<span class="comment-age">(21 May '18, 09:29)</span> <span class="comment-user userinfo">shamimabrishti</span>
</div>
</div>
</div>
<div id="comment-tools-63585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63585-form-container" class="comment-form-container">
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

