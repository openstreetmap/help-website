+++
type = "question"
title = "Very restrictive usage limit on the overpass api since a while?"
description = '''My Android app BikeNode was successfully using the overpass api for years. I was using this format:   http://www.overpass-api.de/api/xapi?node[rcn_ref=*][bbox=5.170799818181818,51.363934891891894,5.534436181818181,51.580151108108105]  But since a while I face issues. Now often I get this error: runt...'''
date = "2016-10-06T20:57:00Z"
lastmod = "2016-10-12T18:54:00Z"
weight = 52384
keywords = [ "usage", "overpass", "xapi", "limit", "overpass-api" ]
aliases = [ "/questions/52384" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Very restrictive usage limit on the overpass api since a while?](/questions/52384/very-restrictive-usage-limit-on-the-overpass-api-since-a-while)

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
<span id="post-52384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52384-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My Android app <a href="https://play.google.com/store/apps/details?id=nl.rulex.bikenode">BikeNode</a> was successfully using the overpass api for years. I was using this format:</p>
<ul>
<li><a href="http://www.overpass-api.de/api/xapi?node%5Brcn_ref=*%5D%5Bbbox=5.170799818181818,51.363934891891894,5.534436181818181,51.580151108108105%5D">http://www.overpass-api.de/api/xapi?node[rcn_ref=*][bbox=5.170799818181818,51.363934891891894,5.534436181818181,51.580151108108105]</a></li>
</ul>
<p>But since a while I face issues. Now often I get this error:</p>
<pre><code>runtime error: open64: 0 Success /osm3s_v0.7.53_osm_base Dispatcher_Client::request_read_and_idx::rate_limited. Please check /api/status for the quota of your IP address.</code></pre>
<p>Before August-2016 I never received this error. Usage of my BikeNode app did not increase. If I check this <a href="http://www.overpass-api.de/api/status">/api/status</a> page I see a message like this:</p>
<pre><code>Connected as: 2441151942
Rate limit: 2
Slot available after: 2016-10-06T10:34:46Z
Slot available after: 2016-10-06T10:36:35Z
Currently running queries (pid, space limit, time limit, start time):</code></pre>
<p>I tried to switch to the Rambler Overpass API Instance, using this format:</p>
<ul>
<li><a href="http://overpass.osm.rambler.ru/cgi/xapi?node%5Brcn_ref=*%5D%5Bbbox=5.170799818181818,51.363934891891894,5.534436181818181,51.580151108108105%5D">http://overpass.osm.rambler.ru/cgi/xapi?node[rcn_ref=*][bbox=5.170799818181818,51.363934891891894,5.534436181818181,51.580151108108105]</a></li>
</ul>
<p>But this regularly shows this error:</p>
<pre><code>runtime error: open64: 0 No error: 0 /osm3s_v0.7.52_osm_base Dispatcher_Client::request_read_and_idx::timeout. Probably the server is overcrowded.</code></pre>
<p>If I check its <a href="http://overpass.osm.rambler.ru/cgi/status">/api/status</a> page, I see a message like this:</p>
<pre><code>Connected as: 2130706433
Rate limit: 0
Currently running queries (pid, space limit, time limit, start time):
75742   536870912   180 2016-10-06T10:42:52Z
75784   536870912   180 2016-10-06T10:43:00Z
75770   536870912   180 2016-10-06T10:42:57Z
75796   536870912   180 2016-10-06T10:43:02Z
75797   536870912   180 2016-10-06T10:43:02Z
75808   536870912   180 2016-10-06T10:43:02Z
75809   536870912   180 2016-10-06T10:43:02Z</code></pre>
<p>The general <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/status">Overpass API/status</a> page explains about an issue since 23-aug-2016.</p>
<p><strong>Does anybody know what's happening here? What is the current status of the servers? Is there a limit configured since some weeks? Are the servers overloaded since some weeks? Does anybody have tips/hints?</strong></p>
<p>PS1. Both servers (Main and Rambler) have the following Usage Policy:</p>
<ul>
<li>Both servers have a total capacity of about 1.000.000 requests per day. You can safely assume that you don't disturb other users when you do less than 10.000 queries per day or download less than 5 GB data per day.</li>
</ul>
<p>PS2. Related question: <a href="https://help.openstreetmap.org/questions/52333">https://help.openstreetmap.org/questions/52333</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-limit" rel="tag" title="see questions tagged &#39;limit&#39;">limit</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '16, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/595fb362d66af578137fd9607c891639?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexvanderlinden&#39;s gravatar image" />
<p><span>alexvanderli...</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexvanderlinden has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '16, 20:27</strong> </span></p>
</div>
</div>
<div id="comments-container-52384" class="comments-container">
&#10;</div>
<div id="comment-tools-52384" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52384-form-container" class="comment-form-container">
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

<span id="52385"></span>

<div id="answer-container-52385" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52385-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-52385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "xapi" endpoint has been severely limited to counteract a malicious or extremely thoughtless user/app developer making between 300,000 and 500,000 requests every hour since the 20th of August. If you were to switch to "Overpass QL" or XML queries instead of using the "xapi" endpoint you'd still get responses.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '16, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52385" class="comments-container">
<span id="52401"></span>
<div id="comment-52401" class="comment">
<div id="post-52401-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm switching to "Overpass QL" and that works. Thanks for the input! I'm using this format now:</p>
<p><a href="http://www.overpass-api.de/api/interpreter?data=node%5B">http://www.overpass-api.de/api/interpreter?data=node["rcn_ref"](51.42283,5.44612,51.45386,5.50655);out;</a></p>
</div>
<div id="comment-52401-info" class="comment-info">
<span class="comment-age">(07 Oct '16, 21:18)</span> <span class="comment-user userinfo">alexvanderli...</span>
</div>
</div>
<span id="52428"></span>
<div id="comment-52428" class="comment">
<div id="post-52428-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I skipped to conclusions to fast. The "Overpass QL" format shows the same availability issues. After testing some time, this seems to be the behavior for both end-points (.de/api/xapi and .de/api/interpreter):</p>
<ul>
<li>From one IP address you can use it twice in a row. After this you'll have to wait some minutes before you can use it again.</li>
<li>The performance from phone (from my android app) is very slow (around 15s response time).</li>
</ul>
</div>
<div id="comment-52428-info" class="comment-info">
<span class="comment-age">(09 Oct '16, 20:36)</span> <span class="comment-user userinfo">alexvanderli...</span>
</div>
</div>
<span id="52456"></span>
<div id="comment-52456" class="comment">
<div id="post-52456-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This related issue at the server has been registered at 7-oct-2016: <a href="https://github.com/drolbr/Overpass-API/issues/323">https://github.com/drolbr/Overpass-API/issues/323</a></p>
</div>
<div id="comment-52456-info" class="comment-info">
<span class="comment-age">(10 Oct '16, 21:15)</span> <span class="comment-user userinfo">alexvanderli...</span>
</div>
</div>
<span id="52501"></span>
<div id="comment-52501" class="comment">
<div id="post-52501-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This issue is fixed: <a href="https://github.com/drolbr/Overpass-API/issues/323">https://github.com/drolbr/Overpass-API/issues/323</a> . As a result the server response is like it used to be. Thanks a lot for fixing this issue!</p>
</div>
<div id="comment-52501-info" class="comment-info">
<span class="comment-age">(12 Oct '16, 18:54)</span> <span class="comment-user userinfo">alexvanderli...</span>
</div>
</div>
</div>
<div id="comment-tools-52385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52385-form-container" class="comment-form-container">
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

