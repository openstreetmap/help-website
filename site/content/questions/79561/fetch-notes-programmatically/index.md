+++
type = "question"
title = "Fetch Notes Programmatically"
description = '''I have seen some suspicious activities on closing notes (not node!) without any reason. Therefore I am thinking about monitory Note related activities in a region. I have made some research and found out there is not way to fetch Notes using Overpass. Is there any other way to do so?'''
date = "2021-04-08T11:00:00Z"
lastmod = "2021-04-09T10:56:00Z"
weight = 79561
keywords = [ "notes-api", "notes" ]
aliases = [ "/questions/79561" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Fetch Notes Programmatically](/questions/79561/fetch-notes-programmatically)

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
<span id="post-79561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79561-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have seen some suspicious activities on closing notes (not node!) without any reason. Therefore I am thinking about monitory Note related activities in a region.</p>
<p>I have made some research and found out there is not way to fetch Notes using Overpass. Is there any other way to do so?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-notes-api" rel="tag" title="see questions tagged &#39;notes-api&#39;">notes-api</span> <span class="post-tag tag-link-notes" rel="tag" title="see questions tagged &#39;notes&#39;">notes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '21, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/310c06992b82ea5760d2c6de2ec193a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahangarha&#39;s gravatar image" />
<p><span>ahangarha</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahangarha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79561" class="comments-container">
&#10;</div>
<div id="comment-tools-79561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79561-form-container" class="comment-form-container">
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

<span id="79580"></span>

<div id="answer-container-79580" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79580-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ahangarha has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can fetch map notes via the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Map_Notes_API">OSM API</a>.</p>
<p>Example: <a href="https://api.openstreetmap.org/api/0.6/notes?bbox=-0.65094,51.312159,0.374908,51.669148">https://api.openstreetmap.org/api/0.6/notes?bbox=-0.65094,51.312159,0.374908,51.669148</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '21, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-79580" class="comments-container">
&#10;</div>
<div id="comment-tools-79580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79580-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79581"></span>

<div id="answer-container-79581" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79581-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>SomeoneElse wrote a small program (<a href="https://github.com/SomeoneElseOSM/Notes01">https://github.com/SomeoneElseOSM/Notes01</a>) which downloads notes in a bbox and converts it to a suitable format for Garmin GPSr devices. I'm sure much of the code could be reused for your own purposes, or perhaps that format is good enough.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '21, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Apr '21, 10:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-79581" class="comments-container">
<span id="79582"></span>
<div id="comment-79582" class="comment">
<div id="post-79582-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Much of the logic in there is designed to work around Garmin foibles (not understanding a bare "&amp;" in a string, for example). If you just want "all the notes" then talking to the API directly in the language of your choice (as scai suggests) will work.</p>
<p>Watch out for the default returned limit of 100 notes, though.</p>
</div>
<div id="comment-79582-info" class="comment-info">
<span class="comment-age">(09 Apr '21, 10:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79581-form-container" class="comment-form-container">
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

