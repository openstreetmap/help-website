+++
type = "question"
title = "Licence change timeline"
description = '''As I understand, on April 1st this year any data that does not meet the new licence is going to be deleted. Yet even today, it seems, it is not clear what data is going to be deleted. I know that there are some estimates and warning plug-ins, but they all claim to be only informative and that the fi...'''
date = "2012-01-05T19:19:00Z"
lastmod = "2012-01-06T12:52:00Z"
weight = 9822
keywords = [ "licence-change" ]
aliases = [ "/questions/9822" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Licence change timeline](/questions/9822/licence-change-timeline)

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
<span id="post-9822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9822-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As I understand, on April 1st this year any data that does not meet the new licence is going to be deleted. Yet even today, it seems, it is not clear what data is going to be deleted.<br />
I know that there are some estimates and warning plug-ins, but they all claim to be only informative and that the final decision can be different.<br />
Is there going to be some phase (IMHO it should be quite long) where it will be clear what data is safe and what is to be deleted (so that it can be remapped without disappearing from the final map)?<br />
</p>
<p>More practically: Is there a way to have a single way/area reverted to the state after licence change so that edits can be made based on this (instead of deleting the whole thing when only some incompatible edits were made)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-licence-change" rel="tag" title="see questions tagged &#39;licence-change&#39;">licence-change</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '12, 19:19</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '12, 19:47</strong> </span></p>
</div>
</div>
<div id="comments-container-9822" class="comments-container">
&#10;</div>
<div id="comment-tools-9822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9822-form-container" class="comment-form-container">
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

<span id="9827"></span>

<div id="answer-container-9827" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9827-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tools are getting better, but the problem is that there is still ongoing discussion about how to handle some corner cases, and that writing "exact" visualisation tools is a hard problem. Precisely because we want to keep as much as possible (for example reverting a way to the latest CT-clean version, but it's even more fine-grained than that).</p>
<p>But we already have pretty good tools (<a href="http://tools.geofabrik.de/osmi/">osmi</a> and <a href="http://cleanmap.poole.ch/">cleanmap</a> at least). While they do (rarely) show false-positives, they shouldn't show any false-negative; so if in doubt assume it needs to be relicensed. Even if we end up doing a handfull of "unneeded" remaping it's not useless work: you'll have refreshed the data and hopefully improved it. Knowing <strong>exactly</strong> what will survive the fine-grained deletion is IMHO not very important : just concentrate on reducing the number of unclean objects where you can.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '12, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span> </br></p>
</div>
</div>
<div id="comments-container-9827" class="comments-container">
&#10;</div>
<div id="comment-tools-9827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9827-form-container" class="comment-form-container">
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

