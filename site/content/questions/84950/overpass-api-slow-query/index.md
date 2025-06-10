+++
type = "question"
title = "Overpass API : Slow Query"
description = '''Hi, I&#x27;m using this docker for local db, https://github.com/wiktorn/Overpass-API. When I try to query for a specific lat-lon with around, it is taking like 0.5 - 0.6 secs on Linux x86_64 machine Ubuntu 18.04 here is my example query command: curl &quot;http://localhost/api/interpreter?data=%5Bout:json%5D%...'''
date = "2022-07-02T14:23:00Z"
lastmod = "2022-07-03T09:23:00Z"
weight = 84950
keywords = [ "overpass", "speed", "around", "query" ]
aliases = [ "/questions/84950" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API : Slow Query](/questions/84950/overpass-api-slow-query)

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
<span id="post-84950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84950-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm using this docker for local db, <a href="https://github.com/wiktorn/Overpass-API.">https://github.com/wiktorn/Overpass-API.</a> When I try to query for a specific lat-lon with around, it is taking like 0.5 - 0.6 secs on Linux x86_64 machine Ubuntu 18.04 here is my example query command: curl "http://localhost/api/interpreter?data=%5Bout:json%5D%5Btimeout:25%5D;(way(around:5,52.29201,-1.51869)%5B"highway"%5D;._;&gt;;);out;"</p>
<p>Is there a way to improve this query speed? I also removed the around keyword and added bbox coordinates, it was worse. Is this result normal and that is the maximum I can reach or is there a way to improve this?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-speed" rel="tag" title="see questions tagged &#39;speed&#39;">speed</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '22, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/761de0d6d13397df82446f39cf1098b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alisvndk88&#39;s gravatar image" />
<p><span>alisvndk88</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alisvndk88 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84950" class="comments-container">
<span id="84951"></span>
<div id="comment-84951" class="comment">
<div id="post-84951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unsure if I'd describe half a second as slow. Do you mean 5 seconds? What speed are you getting on the main api server?</p>
<p>Could you provide a correctly formatted routine please.</p>
</div>
<div id="comment-84951-info" class="comment-info">
<span class="comment-age">(02 Jul '22, 16:01)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="84952"></span>
<div id="comment-84952" class="comment">
<div id="post-84952-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, it is 0.5-0.6 seconds which is equal to 500-600 msec. I'm using localhost and a docker image for queries. This is not a online query. But, I'd like to know that whether it is the maximum speed I can get or or not. If not, what can I do to improve this?</p>
</div>
<div id="comment-84952-info" class="comment-info">
<span class="comment-age">(03 Jul '22, 09:23)</span> <span class="comment-user userinfo">alisvndk88</span>
</div>
</div>
</div>
<div id="comment-tools-84950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84950-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

