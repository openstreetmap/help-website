+++
type = "question"
title = "OverPassAPI performance"
description = '''HI, I am new to OverPassAPI, and setup in my local server(using apache). But the performance is very bad. When I call 100 threads parallel through interpreter, 6 or 7 threads only executed at a time. How do i configure for execute more threads in parallel and improve performance. cc:@mmd'''
date = "2016-06-01T08:06:00Z"
lastmod = "2016-06-21T08:34:00Z"
weight = 49941
keywords = [ "overpassapi", "overpass", "threads", "overpass-api", "performance" ]
aliases = [ "/questions/49941" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OverPassAPI performance](/questions/49941/overpassapi-performance)

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
<span id="post-49941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49941-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>HI,</p>
<p>I am new to OverPassAPI, and setup in my local server(using apache). But the performance is very bad.</p>
<p>When I call 100 threads parallel through interpreter, 6 or 7 threads only executed at a time. How do i configure for execute more threads in parallel and improve performance.</p>
<p>cc:<a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-threads" rel="tag" title="see questions tagged &#39;threads&#39;">threads</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '16, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jun '16, 08:51</strong> </span></p>
</div>
</div>
<div id="comments-container-49941" class="comments-container">
<span id="49965"></span>
<div id="comment-49965" class="comment">
<div id="post-49965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I seen few dispatcher configurations in <a href="https://github.com/drolbr/Overpass-API/blob/master/src/overpass_api/dispatch/dispatcher_server.cc">https://github.com/drolbr/Overpass-API/blob/master/src/overpass_api/dispatch/dispatcher_server.cc</a> But still performance not improved, also where can i get more details about this dispatcher config?</p>
</div>
<div id="comment-49965-info" class="comment-info">
<span class="comment-age">(02 Jun '16, 06:16)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-49941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49941-form-container" class="comment-form-container">
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

<span id="50347"></span>

<div id="answer-container-50347" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50347-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One step here might be to configure Apache. Check out stackoverflow.com/questions/13883646/apache-prefork-vs-worker-mpm for more reference.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '16, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/cf5c4da8efcef260c079f54179669581?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="poornibadrinath&#39;s gravatar image" />
<p><span>poornibadrinath</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="poornibadrinath has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-50347" class="comments-container">
&#10;</div>
<div id="comment-tools-50347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50347-form-container" class="comment-form-container">
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

