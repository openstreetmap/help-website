+++
type = "question"
title = "How to uncouple street segments"
description = '''I am trying to add street names but when I click on a street segment- multiple segments of connected streets highlight- how can I uncouple them?'''
date = "2019-05-25T19:48:00Z"
lastmod = "2019-05-26T08:53:00Z"
weight = 69300
keywords = [ "streetnames" ]
aliases = [ "/questions/69300" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to uncouple street segments](/questions/69300/how-to-uncouple-street-segments)

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
<span id="post-69300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69300-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to add street names but when I click on a street segment- multiple segments of connected streets highlight- how can I uncouple them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '19, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/9f83906ac5171d69dc4f4ce798625f4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="legend1&#39;s gravatar image" />
<p><span>legend1</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="legend1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69300" class="comments-container">
<span id="69307"></span>
<div id="comment-69307" class="comment">
<div id="post-69307-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you point to the place where this happens? Also I'm guessing that you're using OSM's default editor (iD) here?</p>
</div>
<div id="comment-69307-info" class="comment-info">
<span class="comment-age">(25 May '19, 23:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69300-form-container" class="comment-form-container">
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

<span id="69311"></span>

<div id="answer-container-69311" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69311-score" class="post-score" title="current number of votes">
-7
</div>
<span id="post-69311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have been using the default editor and just answered my own question. Just highlight the segmented roads and right click to put them in the trash can and use the line function to draw the new roads</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '19, 03:43</strong></p>
<img src="https://secure.gravatar.com/avatar/9f83906ac5171d69dc4f4ce798625f4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="legend1&#39;s gravatar image" />
<p><span>legend1</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="legend1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69311" class="comments-container">
<span id="69315"></span>
<div id="comment-69315" class="comment">
<div id="post-69315-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>It is not a good idea to remove street segments and draw new ones instead. You might easily drop tags that were there before or break relations using those streets. Use the scissors tool to split the segments where you need.</p>
</div>
<div id="comment-69315-info" class="comment-info">
<span class="comment-age">(26 May '19, 06:27)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="69317"></span>
<div id="comment-69317" class="comment">
<div id="post-69317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also please be aware that you have unjoined several highways.</p>
</div>
<div id="comment-69317-info" class="comment-info">
<span class="comment-age">(26 May '19, 08:53)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-69311" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69311-form-container" class="comment-form-container">
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

