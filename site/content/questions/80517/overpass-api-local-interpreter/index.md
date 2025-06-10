+++
type = "question"
title = "Overpass API: Local interpreter?"
description = '''I’ve installed openstreetmaps API onto a sever and have static requests working as well as http://my_address/api/status giving the correct information. But from here it makes it sound as if I should be able to go to http://my_address/api/ and have an interpreter I can type into, is that supposed to ...'''
date = "2021-06-10T14:21:00Z"
lastmod = "2021-06-10T14:34:00Z"
weight = 80517
keywords = [ "apache", "overpass", "api", "overpass-turbo" ]
aliases = [ "/questions/80517" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API: Local interpreter?](/questions/80517/overpass-api-local-interpreter)

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
<span id="post-80517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I’ve installed openstreetmaps API onto a sever and have static requests working as well as <a href="http://my_address/api/status">http://my_address/api/status</a> giving the correct information. But from <a href="https://wiki.openstreetmap.org/wiki/User:ZeLonewolf/Overpass_Installation_Guide#Query_Tests">here</a> it makes it sound as if I should be able to go to <a href="http://my_address/api/">http://my_address/api/</a> and have an interpreter I can type into, is that supposed to be the case? When I navigate to <a href="http://my_address/api/">http://my_address/api/</a> apache gives an error of “attempt to invoke directory as script /opt/overpass/cgi-bin/" and the web page says "403... You don't have permission to access this resource."</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '21, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/90c1a2a6f8b3789f0622ae27f3d92bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nbreden&#39;s gravatar image" />
<p><span>nbreden</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nbreden has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80517" class="comments-container">
&#10;</div>
<div id="comment-tools-80517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80517-form-container" class="comment-form-container">
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

<span id="80518"></span>

<div id="answer-container-80518" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80518-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nbreden has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't get a local "Overpass Turbo" instance or any sort of web frontend. But as the document you linked to explains, you can instruct the public Overpass Turbo instance to use your local interpreter: "Go to settings and enter the server as follows: http://{SERVER_ADDRESS}/api/" - SERVER_ADDRESS is your own Overpass server's address.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '21, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-80518" class="comments-container">
<span id="80519"></span>
<div id="comment-80519" class="comment">
<div id="post-80519-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank makes so much more sense, thank you!</p>
</div>
<div id="comment-80519-info" class="comment-info">
<span class="comment-age">(10 Jun '21, 14:34)</span> <span class="comment-user userinfo">nbreden</span>
</div>
</div>
</div>
<div id="comment-tools-80518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80518-form-container" class="comment-form-container">
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

