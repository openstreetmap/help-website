+++
type = "question"
title = "Reverting a very large changeset"
description = '''Hi. Earlier today, in this changeset, 小智智 removed the (valid) psv=* tag from roughly 1,700 ways in Hong Kong using overpass turbo, and the changeset seems to be too large to download with the JOSM reverter plugin. Could someone help me revert this?'''
date = "2016-09-19T15:54:00Z"
lastmod = "2016-09-20T21:27:00Z"
weight = 52108
keywords = [ "changeset", "revert", "josm" ]
aliases = [ "/questions/52108" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Reverting a very large changeset](/questions/52108/reverting-a-very-large-changeset)

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
<span id="post-52108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52108-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. Earlier today, in <a href="https://www.openstreetmap.org/changeset/42263645">this changeset</a>, <a href="https://www.openstreetmap.org/user/%E5%B0%8F%E6%99%BA%E6%99%BA">小智智</a> removed the (valid) psv=* tag from roughly 1,700 ways in Hong Kong using overpass turbo, and the changeset seems to be too large to download with the JOSM reverter plugin. Could someone help me revert this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Sep '16, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/10aad7ad0d2c684dec652fe1883e4be6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jc86035&#39;s gravatar image" />
<p><span>jc86035</span><br />
<span class="score" title="191 reputation points">191</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jc86035 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52108" class="comments-container">
<span id="52110"></span>
<div id="comment-52110" class="comment">
<div id="post-52110-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well the first thing that I'd do would be to comment on the changeset explaining the problem, and asking why he thought that it was a "nonsense" tag...</p>
<p>It is possible to revert "large" changesets, but you need to create the .osc file by other means. If you don't get any volunteers here drop a mail to the Data Working Group via data@osmfoundation.org and someone will pick it up.</p>
</div>
<div id="comment-52110-info" class="comment-info">
<span class="comment-age">(19 Sep '16, 16:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52111"></span>
<div id="comment-52111" class="comment">
<div id="post-52111-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've already messaged him privately (including a link to this page); he has yet to respond.</p>
</div>
<div id="comment-52111-info" class="comment-info">
<span class="comment-age">(19 Sep '16, 16:17)</span> <span class="comment-user userinfo">jc86035</span>
</div>
</div>
<span id="52128"></span>
<div id="comment-52128" class="comment">
<div id="post-52128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>小智智 says that he removed the tags because <code>psv=bus</code> isn't a valid combination, and that he didn't know what to re-tag them with. I've emailed <code>data@osmfoundation.org</code>.</p>
</div>
<div id="comment-52128-info" class="comment-info">
<span class="comment-age">(20 Sep '16, 12:46)</span> <span class="comment-user userinfo">jc86035</span>
</div>
</div>
</div>
<div id="comment-tools-52108" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52108-form-container" class="comment-form-container">
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

<span id="52138"></span>

<div id="answer-container-52138" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52138-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jc86035 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've reverted this. See comments on <a href="https://www.openstreetmap.org/changeset/42263645">https://www.openstreetmap.org/changeset/42263645</a> and the linked revert changeset for details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '16, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-52138" class="comments-container">
&#10;</div>
<div id="comment-tools-52138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52138-form-container" class="comment-form-container">
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

