+++
type = "question"
title = "overpass-turbo.eu =&gt; runtime error check /api/status for quota"
description = '''Hello, I am new to OSM, and I get the below error recurringly when running queries on https://overpass-turbo.eu/. I am merely running manual tests, certainly not putting any strain on the server. What am I doing wrong? I would appreciate any input!  An error occured during the execution of the overp...'''
date = "2021-05-25T17:05:00Z"
lastmod = "2021-05-25T17:47:00Z"
weight = 80290
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/80290" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [overpass-turbo.eu =\> runtime error check /api/status for quota](/questions/80290/overpass-turboeu-runtime-error-check-apistatus-for-quota)

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
<span id="post-80290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80290-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am new to OSM, and I get the below error recurringly when running queries on <a href="https://overpass-turbo.eu/.">https://overpass-turbo.eu/.</a> I am merely running manual tests, certainly not putting any strain on the server. What am I doing wrong? I would appreciate any input!</p>
<hr />
<p>An error occured during the execution of the overpass query! This is what overpass API returned:</p>
<h2 id="error-runtime-error-please-check-apistatus-for-the-quota-of-your-ip-address.">Error: runtime error: […] Please check /api/status for the quota of your IP address.</h2>
<p>Here is an example of a query: [out:json]; area["boundary"="administrative"]["name"="Paris"] -&gt; .a; ( nwr(area.a)["amenity"="restaurant"]; ); out center 100;</p>
<p>As a URL string: <a href="https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3Barea%5B%22boundary%22%3D%22administrative%22%5D%5B%22name%22%3D%22Paris%22%5D%2D%3E%2Ea%3B%28nwr%5B%22amenity%22%3D%22restaurant%22%5D%28area%2Ea%29%3B%29%3Bout%20100%20center%3B%0A">https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3Barea%5B%22boundary%22%3D%22administrative%22%5D%5B%22name%22%3D%22Paris%22%5D%2D%3E%2Ea%3B%28nwr%5B%22amenity%22%3D%22restaurant%22%5D%28area%2Ea%29%3B%29%3Bout%20100%20center%3B%0A</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '21, 17:05</strong></p>
<img src="https://secure.gravatar.com/avatar/76504fbe80677b48648e42bdf3cb7bb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zazablue&#39;s gravatar image" />
<p><span>zazablue</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zazablue has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80290" class="comments-container">
&#10;</div>
<div id="comment-tools-80290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80290-form-container" class="comment-form-container">
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

<span id="80292"></span>

<div id="answer-container-80292" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80292-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It does work for me. Did you check the api/status page as suggested ? Maybe too much tests, it should work again after some time. Or your IP is shared with heavy users...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '21, 17:47</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80292" class="comments-container">
&#10;</div>
<div id="comment-tools-80292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80292-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

