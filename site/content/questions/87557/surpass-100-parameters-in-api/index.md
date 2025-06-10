+++
type = "question"
title = "Surpass 100 parameters in api"
description = '''I am using the openstreet api to get the duration matrix of the trip from one point to another, setting the origin as the first parameter and the destinations to the rest of parameters. However, the limit is 100 total(including origin and destinations).  Is there a way to increase this limit, and if...'''
date = "2023-07-26T14:22:00Z"
lastmod = "2023-07-26T15:11:00Z"
weight = 87557
keywords = [ "duration", "distance", "api", "request" ]
aliases = [ "/questions/87557" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Surpass 100 parameters in api](/questions/87557/surpass-100-parameters-in-api)

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
<span id="post-87557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87557-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using the openstreet api to get the duration matrix of the trip from one point to another, setting the origin as the first parameter and the destinations to the rest of parameters. However, the <strong>limit</strong> is 100 total(including origin and destinations).</p>
<p>Is there a way to increase this limit, and if so, how can I do so? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-duration" rel="tag" title="see questions tagged &#39;duration&#39;">duration</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '23, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/fd97d1605933ed2f98e73bac9abd8ed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HowsyWorldd&#39;s gravatar image" />
<p><span>HowsyWorldd</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HowsyWorldd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87557" class="comments-container">
<span id="87558"></span>
<div id="comment-87558" class="comment">
<div id="post-87558-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>the openstreet api</p>
</blockquote>
<p>Which API are you actually calling? I'm guessing your calling some sort of router? What is normally referred to as "the OSM API" is just for editing.</p>
</div>
<div id="comment-87558-info" class="comment-info">
<span class="comment-age">(26 Jul '23, 14:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87560"></span>
<div id="comment-87560" class="comment">
<div id="post-87560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Presumably you have some code and that code calls "something"? What is the "something"?</p>
</div>
<div id="comment-87560-info" class="comment-info">
<span class="comment-age">(26 Jul '23, 14:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87557-form-container" class="comment-form-container">
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

<span id="87561"></span>

<div id="answer-container-87561" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87561-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-87561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="HowsyWorldd has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From the URL it appears like the software you are interacting with is OSRM (<a href="https://github.com/Project-OSRM/osrm-backend).">https://github.com/Project-OSRM/osrm-backend).</a> When the OSRM server is started, you can specify the maximum matrix size on the command line. 100 is the default.</p>
<p>Apparently you are using a service operated by solucionait.es - you would have to ask them if they can increase the limit for you. If they cannot, then you can run the OSRM software yourself with an increased limit - both the data and the software are open - or you can ask another provider to do that for you.</p>
<p>Note that you are using ~ 20 characters per coordinate pair in your request and there are limits to the length of a GET URL. What exactly the limit is depends on which pieces of software your provider has put between you and OSRM; it is relatively safe that 200 coordinate pairs (4k characters) will work, but at 350 or 400 coordinate pairs (8k characters) you'll very likely hit a brick wall and you will then have to consider POST requests or using Google polyline encoding.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '23, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87561" class="comments-container">
&#10;</div>
<div id="comment-tools-87561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87561-form-container" class="comment-form-container">
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

