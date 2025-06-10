+++
type = "question"
title = "Blocked access"
description = '''It appears that my application has been blocked by OpenStreetMap. My Windows application used to be able to access the OpenStreetMap tiles but it no longer can. Who can I contact in order to work this issue?'''
date = "2019-06-06T19:45:00Z"
lastmod = "2019-06-06T21:08:00Z"
weight = 69506
keywords = [ "blocked" ]
aliases = [ "/questions/69506" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Blocked access](/questions/69506/blocked-access)

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
<span id="post-69506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69506-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It appears that my application has been blocked by OpenStreetMap. My Windows application used to be able to access the OpenStreetMap tiles but it no longer can. Who can I contact in order to work this issue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-blocked" rel="tag" title="see questions tagged &#39;blocked&#39;">blocked</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '19, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/8265ed23c983edeccc203d2efbe9d211?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seminole86&#39;s gravatar image" />
<p><span>seminole86</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seminole86 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69506" class="comments-container">
<span id="69508"></span>
<div id="comment-69508" class="comment">
<div id="post-69508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not using Greatmaps. I'm using DevExpress, which is a third party software library that provides a class that loads OpenStreetMaps. Its URL is set to tile.openstreetmap.org. I am not able to change the URL.</p>
</div>
<div id="comment-69508-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 20:09)</span> <span class="comment-user userinfo">seminole86</span>
</div>
</div>
<span id="69510"></span>
<div id="comment-69510" class="comment">
<div id="post-69510-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I suspect that your best course of action is to lobby DevExpress to let you change the URL to one you control or find a different library. For completeness, OSM's tile usage policy is <a href="https://operations.osmfoundation.org/policies/tiles/">here</a>. Until you can get control over which tiles you're actually using you'll continue to be at the mercy of library mistakes like this.</p>
</div>
<div id="comment-69510-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 21:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69511"></span>
<div id="comment-69511" class="comment">
<div id="post-69511-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was able to email in operations and there response was:</p>
<p>This is not something that is targeted at you specifically and you have not triggered any sort of IP based block.</p>
<p>Rather the application you are using is probably not complying with our terms of use:</p>
<p><a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a></p>
<p>Specifically it is probably sending a generic, or faked, user agent and/or referer with it's requests.</p>
<p>We have recently been applying blocks to such traffic to force proper identification of traffic sources.</p>
<p>I have sent this to DevExpress to get their take on it.</p>
</div>
<div id="comment-69511-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 21:08)</span> <span class="comment-user userinfo">seminole86</span>
</div>
</div>
</div>
<div id="comment-tools-69506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69506-form-container" class="comment-form-container">
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

<span id="69507"></span>

<div id="answer-container-69507" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69507-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you using the "Greatmaps" library/framework? If yes, <a href="https://help.openstreetmap.org/questions/69383/error-code-403">https://help.openstreetmap.org/questions/69383/error-code-403</a> might provide some insight.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '19, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69507" class="comments-container">
&#10;</div>
<div id="comment-tools-69507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69507-form-container" class="comment-form-container">
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

