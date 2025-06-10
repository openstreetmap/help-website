+++
type = "question"
title = "i have use &quot;node-geocoder&quot; and getting &quot;ECONNREFUSED&quot; error"
description = '''i had no any problem but last two days i hve getting this type of error  err HttpError: request to http://nominatim.openstreetmap.org/reverse?lat=-11.9795359&amp;amp;lon=-77.0425113&amp;amp;format=json&amp;amp;addressdetails=1 failed, reason: connect ECONNREFUSED 140.100.167.100:80 name: &#x27;HttpError&#x27;, message: &#x27;...'''
date = "2022-01-17T08:07:00Z"
lastmod = "2022-01-17T09:08:00Z"
weight = 83093
keywords = [ "openstreetmap", "node-geocoder" ]
aliases = [ "/questions/83093" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [i have use "node-geocoder" and getting "ECONNREFUSED" error](/questions/83093/i-have-use-node-geocoder-and-getting-econnrefused-error)

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
<span id="post-83093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83093-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i had no any problem but last two days i hve getting this type of error</p>
<p>err HttpError: request to <a href="http://nominatim.openstreetmap.org/reverse?lat=-11.9795359&amp;lon=-77.0425113&amp;format=json&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?lat=-11.9795359&amp;lon=-77.0425113&amp;format=json&amp;addressdetails=1</a> failed, reason: connect ECONNREFUSED 140.100.167.100:80</p>
<p>name: 'HttpError', message: 'request to ' + 'http://nominatim.openstreetmap.org/reverselat=-11.9795359&amp;lon=-77.0425113&amp;format=json&amp;addressdetails=1 ' + 'failed, reason: connect ECONNREFUSED 140.100.167.100:80', code: 'ECONNREFUSED'</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-node-geocoder" rel="tag" title="see questions tagged &#39;node-geocoder&#39;">node-geocoder</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '22, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d9d1b8ad1f3b23940529123e937837c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabu%20hetal&#39;s gravatar image" />
<p><span>gabu hetal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabu hetal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83093" class="comments-container">
&#10;</div>
<div id="comment-tools-83093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83093-form-container" class="comment-form-container">
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

<span id="83094"></span>

<div id="answer-container-83094" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83094-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Is your server capable of following 301 redirects and to handle secure connections (as <a href="http://nomi">http://nomi</a>... redirects to https:nomi... and uses ssl)?</p>
<p>Did you read the documentation at <a href="https://nominatim.org/release-docs/latest/">https://nominatim.org/release-docs/latest/</a> ? E.g. it recommends to include an email parameter with your contact address.</p>
<p>Did you read and follow the Nominatim Usage Policy found here: <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> ? E.g. did you include an unique user agent, did you follow the rate limiting? If not, you will get blocked.</p>
<p>In general it's not recommended to use the public Nominatim instances that are funded by donations if you need higher usage volumes or want to include them in an app or commercial use case. The Nominatim wiki page lists some third-party providers (see <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives.2FThird-party_providers">https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives.2FThird-party_providers</a> ) for that, alternatively you could run your own Nominatim instance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '22, 09:08</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '22, 09:34</strong> </span></p>
</div>
</div>
<div id="comments-container-83094" class="comments-container">
&#10;</div>
<div id="comment-tools-83094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83094-form-container" class="comment-form-container">
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

