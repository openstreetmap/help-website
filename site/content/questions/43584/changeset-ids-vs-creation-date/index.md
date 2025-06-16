+++
type = "question"
title = "Changeset ids vs creation date"
description = '''Hi,  I was looking at my changesets history and I found that for a while, some changeset ids got smaller even if they were created later in time, until they got back to more reasonable values about two weeks later (!). I thought that both were increasing over time! Example is here ... http://www.ope...'''
date = "2015-06-16T01:01:00Z"
lastmod = "2015-06-16T06:45:00Z"
weight = 43584
keywords = [ "changeset", "id", "timestamps" ]
aliases = [ "/questions/43584" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Changeset ids vs creation date](/questions/43584/changeset-ids-vs-creation-date)

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
<span id="post-43584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43584-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I was looking at my changesets history and I found that for a while, some changeset ids got smaller even if they were created later in time, until they got back to more reasonable values about two weeks later (!). I thought that both were increasing over time! Example is here ...</p>
<p><a href="https://www.openstreetmap.org/api/0.6/changesets?user=101184&amp;time=2009-03-30T00:00:00Z,2009-04-05T00:00:00Z">https://www.openstreetmap.org/api/0.6/changesets?user=101184&amp;time=2009-03-30T00:00:00Z,2009-04-05T00:00:00Z</a> <a href="https://www.openstreetmap.org/api/0.6/changesets?user=101184&amp;time=2009-04-16T00:00:00Z,2009-04-23T00:00:00Z">https://www.openstreetmap.org/api/0.6/changesets?user=101184&amp;time=2009-04-16T00:00:00Z,2009-04-23T00:00:00Z</a></p>
<p>The first request shows when my changesets ids dropped and the second when the ids seem to have jumped back to a reasonable value. Is it a problem that is spread all over ids for nodes, ways and relations or only on changesets? Any information about what caused this problem and if it is possible to know the range of ids that were affected?</p>
<p>Best regards, Daniel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '15, 01:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jun '15, 01:23</strong> </span></p>
</div>
</div>
<div id="comments-container-43584" class="comments-container">
&#10;</div>
<div id="comment-tools-43584" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43584-form-container" class="comment-form-container">
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

<span id="43585"></span>

<div id="answer-container-43585" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43585-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-43585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Changesets were new in API v0.6 which the wiki says was released 20th April 2009. Not sure what the algorithm was to assign changeset IDs to all earlier data was but I can imagine it might not process all edits in strict original date time order (I suspect individual nodes ways and relations would have been done in version order, but changesets that don't have any objects in common might cause what you see).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '15, 06:45</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-43585" class="comments-container">
&#10;</div>
<div id="comment-tools-43585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43585-form-container" class="comment-form-container">
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

