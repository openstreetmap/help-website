+++
type = "question"
title = "Cors error after searching"
description = '''Hi all! We implemented OpenStreetMap.org and it works great, but we get a CORS error, see below, after searching. We added the below code to the htacces, but it does&#x27;nt seem to work. We just can&#x27;t find the solution and hope someone can help us :-) ERROR Access to XMLHttpRequest at &#x27;https://nominatim...'''
date = "2021-10-21T09:14:00Z"
lastmod = "2021-10-22T10:29:00Z"
weight = 82293
keywords = [ "cors" ]
aliases = [ "/questions/82293" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cors error after searching](/questions/82293/cors-error-after-searching)

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
<span id="post-82293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82293-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all!</p>
<p>We implemented OpenStreetMap.org and it works great, but we get a CORS error, see below, after searching. We added the below code to the htacces, but it does'nt seem to work. We just can't find the solution and hope someone can help us :-)</p>
<p>ERROR Access to XMLHttpRequest at 'https://nominatim.openstreetmap.org/search?format=json&amp;q=President%20Allendelaan%202,%201064GW%20Amsterdam' from origin 'https://www.frituurvetrecyclehet.nl' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.</p>
<p>HTACCESS &lt;ifmodule mod_headers.c=""&gt; Header set Access-Control-Allow-Origin <a href="https://nominatim.openstreetmap.org">https://nominatim.openstreetmap.org</a> Header set Access-Control-Allow-Credentials true &lt;/ifmodule&gt;</p>
<p>Any help is appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cors" rel="tag" title="see questions tagged &#39;cors&#39;">cors</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Oct '21, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/38ff743726ef7be96a9c59cc5f469ce3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Internetbureau%20Jun-E-Jay&#39;s gravatar image" />
<p><span>Internetbure...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Internetbureau Jun-E-Jay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82293" class="comments-container">
&#10;</div>
<div id="comment-tools-82293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82293-form-container" class="comment-form-container">
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

<span id="82294"></span>

<div id="answer-container-82294" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82294-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you see a CORS issue like that with nominatim.openstreetmap.org then the underlying issue is likely that you have been blocked for some reason. The site sends proper CORS headers with normal responses but it does not send them when returning a HTTP 403 or 429. Check your logs for HTTP errors.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '21, 09:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-82294" class="comments-container">
<span id="82302"></span>
<div id="comment-82302" class="comment">
<div id="post-82302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, thanks, but is there a way to check? We notice that we get 10 results without the error, and the 11th result gives the error. Any suggestion on how to fix this?</p>
</div>
<div id="comment-82302-info" class="comment-info">
<span class="comment-age">(22 Oct '21, 09:14)</span> <span class="comment-user userinfo">Internetbure...</span>
</div>
</div>
<span id="82303"></span>
<div id="comment-82303" class="comment">
<div id="post-82303-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The simplest way to fix this is to respect the <a href="https://operations.osmfoundation.org/policies/nominatim/">Usage policy</a> of the service and make sure to not send more than 1req/s. If that is not enough for you you will need to run your own instance of Nominatim.</p>
</div>
<div id="comment-82303-info" class="comment-info">
<span class="comment-age">(22 Oct '21, 10:29)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-82294" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82294-form-container" class="comment-form-container">
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

