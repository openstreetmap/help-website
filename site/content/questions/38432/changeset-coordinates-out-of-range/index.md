+++
type = "question"
title = "Changeset coordinates Out of range?"
description = '''Looking at some changesets I find odd information regarding coordinates and objects version. For instance, in changeset 420453 one can find ...  Coordinates outside the range [-180 -90, 180 90] such as lon=&quot;214.7483647&quot; for node id=&quot;60876769&quot;; Consequently, the bounding box is also out the expected ...'''
date = "2014-11-10T19:28:00Z"
lastmod = "2014-11-15T03:50:00Z"
weight = 38432
keywords = [ "coordinate", "changeset", "version" ]
aliases = [ "/questions/38432" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Changeset coordinates Out of range?](/questions/38432/changeset-coordinates-out-of-range)

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
<span id="post-38432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38432-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Looking at some changesets I find odd information regarding coordinates and objects version. For instance, in <span>changeset 420453</span> one can find ...</p>
<ul>
<li>Coordinates outside the range [-180 -90, 180 90] such as lon="214.7483647" for node id="60876769";</li>
<li>Consequently, the bounding box is also out the expected range;</li>
<li>Versions 2 &amp; 3 of the same node (again node id="<span>60876769</span>") exist in the same changeset (420453);</li>
</ul>
<p>Does anybody can provide me with some historical context/explanation how such data appeared in the database? Is it still possible it happens again?</p>
<p>Cheers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coordinate" rel="tag" title="see questions tagged &#39;coordinate&#39;">coordinate</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '14, 19:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Nov '14, 16:17</strong> </span></p>
</div>
</div>
<div id="comments-container-38432" class="comments-container">
<span id="38434"></span>
<div id="comment-38434" class="comment">
<div id="post-38434-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For the curious: It isn't possible to upload a node with this longitude any longer. The server responds with error 400 and "The node is outside this world".</p>
</div>
<div id="comment-38434-info" class="comment-info">
<span class="comment-age">(10 Nov '14, 20:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="38435"></span>
<div id="comment-38435" class="comment">
<div id="post-38435-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Regarding your observation in list member two: "One element can be updated multiple times during one changeset and its version number is increased each time so there can be multiple history versions of a single element for one changeset." (<span>API 0.6</span>). So this is nothing unexpected.</p>
</div>
<div id="comment-38435-info" class="comment-info">
<span class="comment-age">(10 Nov '14, 20:25)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="38436"></span>
<div id="comment-38436" class="comment">
<div id="post-38436-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The linked changeset was created at the time when <span>API 0.5</span> was active. Maybe the coordinates were not enforced to be in the range [-180 -90, 180 90] at this time.</p>
</div>
<div id="comment-38436-info" class="comment-info">
<span class="comment-age">(10 Nov '14, 20:27)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="38443"></span>
<div id="comment-38443" class="comment">
<div id="post-38443-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Possibly, although the <a href="https://wiki.openstreetmap.org/wiki/API_changes_between_v0.5_and_v0.6">API changes between v0.5 and v0.6</a> don't mention the introduction of such checks.</p>
</div>
<div id="comment-38443-info" class="comment-info">
<span class="comment-age">(11 Nov '14, 07:52)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-38432" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38432-form-container" class="comment-form-container">
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

<span id="38568"></span>

<div id="answer-container-38568" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38568-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All the comments make sense... I missed the point about multiple versions of an object in a changeset - It's certainly possible! Concerning the erroneous coordinate, I'm happy it is not possible anymore!</p>
<p>Thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '14, 03:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38568" class="comments-container">
&#10;</div>
<div id="comment-tools-38568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38568-form-container" class="comment-form-container">
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

