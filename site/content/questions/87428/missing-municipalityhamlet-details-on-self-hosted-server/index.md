+++
type = "question"
title = "Missing municipality/hamlet details on self-hosted server"
description = '''Hi all, Since a few weeks we&#x27;ve running a self-hosted Nominatim server now. The server is running like a gem, but we noticed a little difference in some of our queries sometimes.  When we request a reverse query with lat/lon data on our self-hosted server, we are receiving (almost) the same informat...'''
date = "2023-07-04T13:03:00Z"
lastmod = "2023-07-04T13:34:00Z"
weight = 87428
keywords = [ "hamlet", "municipality", "missing" ]
aliases = [ "/questions/87428" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Missing municipality/hamlet details on self-hosted server](/questions/87428/missing-municipalityhamlet-details-on-self-hosted-server)

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
<span id="post-87428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87428-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>Since a few weeks we've running a self-hosted Nominatim server now. The server is running like a gem, but we noticed a little difference in some of our queries sometimes.</p>
<p><img src="https://i.ibb.co/Yhf1xwm/Screenshot-2023-07-04-at-12-04-01.png" alt="Screenshot" /></p>
<p>When we request a reverse query with lat/lon data on our self-hosted server, we are receiving (almost) the same information as the nominatim.openstreetmap.org API, but unfortunately the municipality and also the hamlet is sometimes missing on our self-hosted server.</p>
<p>Does anyone have an idea how to add these missing municipality/hamlet details to our output?</p>
<p>Many thanks in advance!</p>
<p>Kind regards, Randy Dautzenberg</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hamlet" rel="tag" title="see questions tagged &#39;hamlet&#39;">hamlet</span> <span class="post-tag tag-link-municipality" rel="tag" title="see questions tagged &#39;municipality&#39;">municipality</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '23, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/372040659e831a437de9e1d52104c66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Randy&#39;s gravatar image" />
<p><span>Randy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Randy has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '23, 13:12</strong> </span></p>
</div>
</div>
<div id="comments-container-87428" class="comments-container">
&#10;</div>
<div id="comment-tools-87428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87428-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="87430"></span>

<div id="answer-container-87430" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87430-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try format=geocodejson instead of format=jsonv2 - are you still seeing differences?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '23, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87430" class="comments-container">
&#10;</div>
<div id="comment-tools-87430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87430-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87434"></span>

<div id="answer-container-87434" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87434-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Frederik,</p>
<p>Many thanks for your very quick response! I've tried to add the format=geocodejson instead of format=jsonv2.</p>
<p>There is a little difference in the city and locality this time. Does that mean there's something wrong with our self-hosted server?</p>
<p><img src="https://i.ibb.co/cktDrtc/Screenshot-2023-07-04-at-14-28-06.png" alt="Screenshot" /></p>
<p>Again many thanks for the quick reply!</p>
<p>Kind regards, Randy</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '23, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/372040659e831a437de9e1d52104c66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Randy&#39;s gravatar image" />
<p><span>Randy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Randy has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '23, 13:41</strong> </span></p>
</div>
</div>
<div id="comments-container-87434" class="comments-container">
&#10;</div>
<div id="comment-tools-87434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87434-form-container" class="comment-form-container">
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

