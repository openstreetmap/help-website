+++
type = "question"
title = "Re-apply daily diff with osm2pgsql"
description = '''Hi all I have imported the Europe dataset in PostgreSQL with osm2pgsql, and I apply daily updates with a routine every night. Looking at the logs I keep, I believe one of the daily updates was not correctly applied. I was thinking about simply re-playing those updates (edit : all the daily updates s...'''
date = "2019-03-05T07:55:00Z"
lastmod = "2019-05-15T10:18:00Z"
weight = 68268
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/68268" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Re-apply daily diff with osm2pgsql](/questions/68268/re-apply-daily-diff-with-osm2pgsql)

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
<span id="post-68268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68268-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I have imported the Europe dataset in PostgreSQL with osm2pgsql, and I apply daily updates with a routine every night. Looking at the logs I keep, I believe one of the daily updates was not correctly applied. I was thinking about simply re-playing those updates (edit : all the daily updates since the failure, of course). Would this work ? From what I understand of the way osm2pgsql works it basically does inserts and deletes, so I'd say this could work, but I'd rather be sure.</p>
<p>Thanks for your help on this !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '19, 07:55</strong></p>
<img src="https://secure.gravatar.com/avatar/6b4f06fde4e48d946ba27ad93d11187e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="codata_al&#39;s gravatar image" />
<p><span>codata_al</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="codata_al has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '19, 08:38</strong> </span></p>
</div>
</div>
<div id="comments-container-68268" class="comments-container">
&#10;</div>
<div id="comment-tools-68268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68268-form-container" class="comment-form-container">
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

<span id="68270"></span>

<div id="answer-container-68270" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68270-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="codata_al has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm2pgsql's update process is safe to replay. That means you can repeat updates provided you reapply all updates from the date that the update process failed and you apply them in the correct order. The database is only back to a consistent state when all updates have been processed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '19, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '19, 12:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-68270" class="comments-container">
<span id="68271"></span>
<div id="comment-68271" class="comment">
<div id="post-68271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's excellent news Lonvia !</p>
<p>Thanks for your help !</p>
</div>
<div id="comment-68271-info" class="comment-info">
<span class="comment-age">(05 Mar '19, 12:07)</span> <span class="comment-user userinfo">codata_al</span>
</div>
</div>
</div>
<div id="comment-tools-68270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68270-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69194"></span>

<div id="answer-container-69194" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69194-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi again !</p>
<p>Just to make sure I got this right : I've had ONE update failing (say, sequenceNumber = 2245 for instance), BUT the ones after that ran fine (2246 was applied, as well as 2247 and 2248).</p>
<p>It is fine to reapply all updates starting from 2245 (2245 to 2248), even though the updates from 2246 to 2248 had already been applied ?</p>
<p>Sorry for being so verbose, but I am not sure that my first message made it very clear that I had subsequent update successfully applied.</p>
<p>Thanks !</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '19, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/6b4f06fde4e48d946ba27ad93d11187e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="codata_al&#39;s gravatar image" />
<p><span>codata_al</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="codata_al has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69194" class="comments-container">
<span id="69195"></span>
<div id="comment-69195" class="comment">
<div id="post-69195-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, that's what I meant with the answer above. If you want to reapply 2245, you <em>must</em> reapply 2246 to 2248 afterwards again. When all changes until 2248 are applied, your database is in a consistent state.</p>
</div>
<div id="comment-69195-info" class="comment-info">
<span class="comment-age">(15 May '19, 10:13)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="69196"></span>
<div id="comment-69196" class="comment">
<div id="post-69196-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, just wanted to be 100% sure. Sorry for the noise, and thanks again !</p>
</div>
<div id="comment-69196-info" class="comment-info">
<span class="comment-age">(15 May '19, 10:18)</span> <span class="comment-user userinfo">codata_al</span>
</div>
</div>
</div>
<div id="comment-tools-69194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69194-form-container" class="comment-form-container">
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

