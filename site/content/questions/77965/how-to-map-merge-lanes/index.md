+++
type = "question"
title = "How to map merge lanes?"
description = '''I tried searching for this and wasn&#x27;t having much luck finding answers here or examples elsewhere. How do we handle &quot;merge lanes&quot; where a lane is ending so you much merge over? Here is an example on little road going north bound at fivay: https://www.openstreetmap.org/edit#map=19/28.33999/-82.66584'''
date = "2020-12-17T08:52:00Z"
lastmod = "2020-12-21T06:30:00Z"
weight = 77965
keywords = [ "lanes" ]
aliases = [ "/questions/77965" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to map merge lanes?](/questions/77965/how-to-map-merge-lanes)

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
<span id="post-77965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77965-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I tried searching for this and wasn't having much luck finding answers here or examples elsewhere.</p>
<p>How do we handle "merge lanes" where a lane is ending so you much merge over?</p>
<p>Here is an example on little road going north bound at fivay: <a href="https://www.openstreetmap.org/edit#map=19/28.33999/-82.66584">https://www.openstreetmap.org/edit#map=19/28.33999/-82.66584</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '20, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/043d95939633cb3216e446401aee254a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ray331&#39;s gravatar image" />
<p><span>ray331</span><br />
<span class="score" title="120 reputation points">120</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ray331 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77965" class="comments-container">
&#10;</div>
<div id="comment-tools-77965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77965-form-container" class="comment-form-container">
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

<span id="77966"></span>

<div id="answer-container-77966" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77966-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It turns out I want to use <code>turn:lanes</code> = <code>merge_to_right</code> for my use case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '20, 08:59</strong></p>
<img src="https://secure.gravatar.com/avatar/043d95939633cb3216e446401aee254a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ray331&#39;s gravatar image" />
<p><span>ray331</span><br />
<span class="score" title="120 reputation points">120</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ray331 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77966" class="comments-container">
<span id="77986"></span>
<div id="comment-77986" class="comment">
<div id="post-77986-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to tag all the lanes individually. For your three lane one-way road it would be <code>turn:lanes=merge_to_right|none|none</code> or shorter <code>turn:lanes=merge_to_right||</code>. But I see you have done it already in that way.</p>
</div>
<div id="comment-77986-info" class="comment-info">
<span class="comment-age">(18 Dec '20, 10:10)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-77966" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77966-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77981"></span>

<div id="answer-container-77981" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77981-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To be clear, you should use <code>turn:lanes=merge_to_right|none|none</code>.</p>
<p>If the lane configuration is complicated, further consider <a href="https://wiki.openstreetmap.org/wiki/Relation:connectivity.">https://wiki.openstreetmap.org/wiki/Relation:connectivity.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '20, 04:56</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Dec '20, 06:31</strong> </span></p>
</div>
</div>
<div id="comments-container-77981" class="comments-container">
<span id="77985"></span>
<div id="comment-77985" class="comment">
<div id="post-77985-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not at all. We count the lanes from left to right. So it needs to be <code>turn:lanes=merge_to_right|none|none</code>.</p>
</div>
<div id="comment-77985-info" class="comment-info">
<span class="comment-age">(18 Dec '20, 10:09)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="78032"></span>
<div id="comment-78032" class="comment">
<div id="post-78032-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn"></a><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> Typo at the wrong side. Obviously <code>=merge_to_right</code> on the rightmost doesn't make sense.</p>
</div>
<div id="comment-78032-info" class="comment-info">
<span class="comment-age">(21 Dec '20, 06:30)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-77981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77981-form-container" class="comment-form-container">
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

