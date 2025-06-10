+++
type = "question"
title = "Blocked from service. Destination Host Unreachable from production server. Works from home ip ?"
description = '''cURL error 7: Failed to connect to nominatim.openstreetmap.org port 80: Connection refused (see https://curl.haxx.se/libcurl/c/libcurl-errors.html) Request goes through from my main machine but fails from production. I also can&#x27;t ping the service. PING amsterdam.nominatim.openstreetmap.org (130.117....'''
date = "2020-11-28T23:50:00Z"
lastmod = "2020-11-29T13:54:00Z"
weight = 77770
keywords = [ "blocked" ]
aliases = [ "/questions/77770" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Blocked from service. Destination Host Unreachable from production server. Works from home ip ?](/questions/77770/blocked-from-service-destination-host-unreachable-from-production-server-works-from-home-ip)

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
<span id="post-77770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77770-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>cURL error 7: Failed to connect to nominatim.openstreetmap.org port 80: Connection refused (see <a href="https://curl.haxx.se/libcurl/c/libcurl-errors.html)">https://curl.haxx.se/libcurl/c/libcurl-errors.html)</a></p>
<p>Request goes through from my main machine but fails from production. I also can't ping the service.</p>
<pre><code>PING amsterdam.nominatim.openstreetmap.org (130.117.76.9) 56(84) bytes of data.
From 130.117.76.9 (130.117.76.9) icmp_seq=1 Destination Host Unreachable
From 130.117.76.9 (130.117.76.9) icmp_seq=2 Destination Host Unreachable
From 130.117.76.9 (130.117.76.9) icmp_seq=3 Destination Host Unreachable
^C
--- amsterdam.nominatim.openstreetmap.org ping statistics ---
3 packets transmitted, 0 received, +3 errors, 100% packet loss, time 2003ms</code></pre>
<p>The service wasn't used abusively and I also did nothing against TOS. What happens?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-blocked" rel="tag" title="see questions tagged &#39;blocked&#39;">blocked</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '20, 23:50</strong></p>
<img src="https://secure.gravatar.com/avatar/c76aeee5a97e51db9035d3cd2f703f84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Victor&#39;s gravatar image" />
<p><span>Victor</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Victor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77770" class="comments-container">
<span id="77771"></span>
<div id="comment-77771" class="comment">
<div id="post-77771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to check - you have read and followed <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> ?</p>
</div>
<div id="comment-77771-info" class="comment-info">
<span class="comment-age">(28 Nov '20, 23:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="77772"></span>
<div id="comment-77772" class="comment">
<div id="post-77772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. I also use a custom User Agent.</p>
</div>
<div id="comment-77772-info" class="comment-info">
<span class="comment-age">(29 Nov '20, 00:30)</span> <span class="comment-user userinfo">Victor</span>
</div>
</div>
<span id="77774"></span>
<div id="comment-77774" class="comment">
<div id="post-77774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you sent more than 1 request per sec? Sth. triggered the blocking, so reade the usage policy closely again.</p>
</div>
<div id="comment-77774-info" class="comment-info">
<span class="comment-age">(29 Nov '20, 09:20)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="77776"></span>
<div id="comment-77776" class="comment">
<div id="post-77776-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>At the risk of stating the bleeding obvious, are you sure that what you're seeing is an actual block applied by OSM's nominatim server? I hesitate to call it a "service", because it's really not designed to be one.</p>
<p>If you try and make outbound connections on port 80 to other servers using "telnet ipaddress 80" from your "live" server, what happens?</p>
</div>
<div id="comment-77776-info" class="comment-info">
<span class="comment-age">(29 Nov '20, 10:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77770-form-container" class="comment-form-container">
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

<span id="77782"></span>

<div id="answer-container-77782" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77782-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The ban has been lifted. Not sure what happened. Thanks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '20, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c76aeee5a97e51db9035d3cd2f703f84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Victor&#39;s gravatar image" />
<p><span>Victor</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Victor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77782" class="comments-container">
&#10;</div>
<div id="comment-tools-77782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77782-form-container" class="comment-form-container">
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

