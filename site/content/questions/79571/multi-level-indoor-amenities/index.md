+++
type = "question"
title = "Multi-level Indoor Amenities"
description = '''Hi, how do you connect two areas in a department store that belong to one and the same shop, i.e. a shop that covers several floors and the floors differ in size/position (example: Wollworth in the Forum Mülheim, https://www.openstreetmap.org/#map=18/51.42911/6.88598) or on the same floor a shop and...'''
date = "2021-04-08T19:12:00Z"
lastmod = "2021-04-11T10:58:00Z"
weight = 79571
keywords = [ "indoor" ]
aliases = [ "/questions/79571" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Multi-level Indoor Amenities](/questions/79571/multi-level-indoor-amenities)

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
<span id="post-79571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79571-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, how do you connect two areas in a department store that belong to one and the same shop, i.e. a shop that covers several floors and the floors differ in size/position (example: Wollworth in the Forum Mülheim, <a href="https://www.openstreetmap.org/#map=18/51.42911/6.88598)">https://www.openstreetmap.org/#map=18/51.42911/6.88598)</a> or on the same floor a shop and a sales stand in the corridor (Cafe Venezia)?</p>
<p>Do I have to store them individually, or is it also possible with a relation?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '21, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/87d68dc4815c8c28241ccc1d4dd64e52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MSmolarz&#39;s gravatar image" />
<p><span>MSmolarz</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MSmolarz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '21, 19:15</strong> </span></p>
</div>
</div>
<div id="comments-container-79571" class="comments-container">
&#10;</div>
<div id="comment-tools-79571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79571-form-container" class="comment-form-container">
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

<span id="79586"></span>

<div id="answer-container-79586" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79586-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MSmolarz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's currently no standard way to model a shop with different dimensions on each floor in Simple Indoor Tagging. As you noticed, it only has a solution if the 2D extent of a feature is the same on all levels.</p>
<p>This is one of several topics where SIT is in need of some improvement. At the moment, there's not really a good solution I'm afraid. I guess you could try making up a relation linking together multiple areas, or stick to using a node.</p>
<p>The Cafe Venezia example, on the other hand, doesn't seem to be directly related to indoor mapping – it would be the same problem if it was outdoors. I can't judge the situation well enough from what's visible online, but maybe this could just be two features with the same operator.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '21, 13:43</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-79586" class="comments-container">
<span id="79602"></span>
<div id="comment-79602" class="comment">
<div id="post-79602-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, thank you</p>
</div>
<div id="comment-79602-info" class="comment-info">
<span class="comment-age">(11 Apr '21, 10:58)</span> <span class="comment-user userinfo">MSmolarz</span>
</div>
</div>
</div>
<div id="comment-tools-79586" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79586-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79583"></span>

<div id="answer-container-79583" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79583-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging#Multi-level_features_and_repeated_features">https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging#Multi-level_features_and_repeated_features</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '21, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-79583" class="comments-container">
<span id="79585"></span>
<div id="comment-79585" class="comment">
<div id="post-79585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've seen that too, but that's only for features that span multiple levels with the same location and size, but in my case, it's one store across two levels, with different sizes, and one with two physically separate spaces on one floor.</p>
</div>
<div id="comment-79585-info" class="comment-info">
<span class="comment-age">(09 Apr '21, 13:06)</span> <span class="comment-user userinfo">MSmolarz</span>
</div>
</div>
</div>
<div id="comment-tools-79583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79583-form-container" class="comment-form-container">
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

