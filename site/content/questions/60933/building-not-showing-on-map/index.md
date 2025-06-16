+++
type = "question"
title = "Building not showing on map?"
description = '''I recently placed a school building on the map, but it does not seem to show. The tag seems to show up on the map but there is no building after a couple of hours. https://www.openstreetmap.org/#map=18/40.26114/-74.53082'''
date = "2017-12-02T01:26:00Z"
lastmod = "2017-12-02T11:47:00Z"
weight = 60933
keywords = [ "building", "not_shown" ]
aliases = [ "/questions/60933" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Building not showing on map?](/questions/60933/building-not-showing-on-map)

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
<span id="post-60933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60933-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently placed a school building on the map, but it does not seem to show. The tag seems to show up on the map but there is no building after a couple of hours. <a href="https://www.openstreetmap.org/#map=18/40.26114/-74.53082">https://www.openstreetmap.org/#map=18/40.26114/-74.53082</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '17, 01:26</strong></p>
<img src="https://secure.gravatar.com/avatar/6583883367dc9661db0a4ce21e7f7466?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Riley%20S&#39;s gravatar image" />
<p><span>Riley S</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Riley S has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Dec '17, 01:26</strong> </span></p>
</div>
</div>
<div id="comments-container-60933" class="comments-container">
<span id="60934"></span>
<div id="comment-60934" class="comment">
<div id="post-60934-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Fixed the issue</p>
</div>
<div id="comment-60934-info" class="comment-info">
<span class="comment-age">(02 Dec '17, 02:40)</span> <span class="comment-user userinfo">Riley S</span>
</div>
</div>
<span id="60941"></span>
<div id="comment-60941" class="comment">
<div id="post-60941-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You don't need the "type" tag on a way. I see you deleted some nodes in one of the earlier revisions, but haven't investigated to see if with those in the area had crossing sections and so perhaps an invalid shape.</p>
</div>
<div id="comment-60941-info" class="comment-info">
<span class="comment-age">(02 Dec '17, 11:07)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60933" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60933-form-container" class="comment-form-container">
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

<span id="60942"></span>

<div id="answer-container-60942" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60942-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-60942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This overlapping section would have been the problem I suspect, which you have since fixed.</p>
<p><img src="/upfiles/schoolclip.PNG" alt="Closeup." /></p>
<p>As mentioned above you can remove type=multipolygon from the way - this is a tag used for relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '17, 11:12</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</img>
</div>
</div>
<div id="comments-container-60942" class="comments-container">
&#10;</div>
<div id="comment-tools-60942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60942-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60943"></span>

<div id="answer-container-60943" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60943-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found the crossed section of the drawing, which was making the building not appear fully. I have since fixed the issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '17, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/6583883367dc9661db0a4ce21e7f7466?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Riley%20S&#39;s gravatar image" />
<p><span>Riley S</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Riley S has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60943" class="comments-container">
&#10;</div>
<div id="comment-tools-60943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60943-form-container" class="comment-form-container">
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

