+++
type = "question"
title = "Fix the openstreetmap.org website"
description = '''Whenever I open openstreetmap.org in my laptop, the following error shows:  The website works ok in my smartphone, so I have posted this through my phone.'''
date = "2022-01-08T09:02:00Z"
lastmod = "2022-01-10T10:04:00Z"
weight = 82995
keywords = [ "openstreetmap.org" ]
aliases = [ "/questions/82995" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Fix the openstreetmap.org website](/questions/82995/fix-the-openstreetmaporg-website)

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
<span id="post-82995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82995-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Whenever I open openstreetmap.org in my laptop, the following error shows: <img src="https://help.openstreetmap.org/upfiles/Capture2_BxkHlIo.PNG" alt="Error page while opening openstreetmap.org" /></p>
<p>The website works ok in my smartphone, so I have posted this through my phone.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap.org" rel="tag" title="see questions tagged &#39;openstreetmap.org&#39;">openstreetmap.org</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '22, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/26c2ef8e2fb0187719b5ad2dbcca4700?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Soumyabrata&#39;s gravatar image" />
<p><span>Soumyabrata</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Soumyabrata has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-82995" class="comments-container">
&#10;</div>
<div id="comment-tools-82995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82995-form-container" class="comment-form-container">
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

<span id="83032"></span>

<div id="answer-container-83032" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83032-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-83032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If this has been happening for longer than a few days, then the most likely explanation is that you need to update your operating system. This is because I suspect your computer is missing the "ISRG Root X1" certificate, which is found in all up-to-date operating systems. Without that, you will get error messages when trying to connect to OpenStreetMap.</p>
<p>The "invalid date" is because the alternative root certificate used by Let's Encrypt, known as "DST Root CA X3", has now expired.</p>
<p>Updates to the root certificates are included in regular operating system updates, so applying all those updates are the quickest and easiest way to solve the problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '22, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-83032" class="comments-container">
&#10;</div>
<div id="comment-tools-83032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83032-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82997"></span>

<div id="answer-container-82997" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82997-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This should be fixed again as the underlying ssl certificate by let's encrypt got renewed.</p>
<p>If it's not fixed for you, you may have to check your computers date or if you are using any proxy in between.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '22, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jan '22, 09:33</strong> </span></p>
</div>
</div>
<div id="comments-container-82997" class="comments-container">
&#10;</div>
<div id="comment-tools-82997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82997-form-container" class="comment-form-container">
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

