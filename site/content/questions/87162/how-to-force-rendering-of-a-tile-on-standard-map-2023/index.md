+++
type = "question"
title = "How to force rendering of a tile on standard map 2023?"
description = '''Hi all. Can anyone explain how I force rendering of a specific tile on the standard map nowadays, as of 2023, or perhaps point me to where the updated documentation is? Apparently the old way to force rendering of a specific map tile, by adding &quot;/dirty&quot; after the url, is not working anymore. From wh...'''
date = "2023-04-24T20:10:00Z"
lastmod = "2023-04-25T10:20:00Z"
weight = 87162
keywords = [ "dirty", "rendering", "force", "update", "tileserver" ]
aliases = [ "/questions/87162" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to force rendering of a tile on standard map 2023?](/questions/87162/how-to-force-rendering-of-a-tile-on-standard-map-2023)

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
<span id="post-87162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87162-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-87162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all.</p>
<p>Can anyone explain how I force rendering of a specific tile on the standard map nowadays, as of 2023, or perhaps point me to where the updated documentation is?</p>
<p>Apparently the old way to force rendering of a specific map tile, by adding "/dirty" after the url, is not working anymore.</p>
<p>From what I can understand, what has happened is that "cdn-servers" has been added in front of the real servers, caching the data externally. What I don't understand is why these "cdn-servers" can not selectively redirect certain requests, like when "/dirty" is in the url, to a real server which then could write to the dirty-queue. Then this architectural change would have been completely transparent to end users, and users like me wouldn't need to search forums and ask questions like this.</p>
<p>But, here we are now. The functionality has been changed from the user perspective, and I can't find any documentation on how this work now.</p>
<p>I think this is an essential feature, that cannot just be dropped, since the renderer and the queue-handler misses things sometimes. One such case is when one have removed a point (POI) near the edge of a tile, then the system can fail to understand that there are two or more tiles which also are affected, and then half of the letters in the name will get stuck "forever". Also, when working with relations, such edits will also often not be updated.</p>
<p>I don't think doing dummy edits, as I have seen suggested elsewhere, is a valid solution. That would make history messier than it has to be. Also, it will force all other maps to render, even though those renderers are not affected by the same render bug and they don't have the same queue implementation as the standard map. It will also likely make map updates for mobile users larger than necessary.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dirty" rel="tag" title="see questions tagged &#39;dirty&#39;">dirty</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-force" rel="tag" title="see questions tagged &#39;force&#39;">force</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '23, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/004664ea648043a0be46ae6830aabbbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="henriko&#39;s gravatar image" />
<p><span>henriko</span><br />
<span class="score" title="130 reputation points">130</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="henriko has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87162" class="comments-container">
<span id="87169"></span>
<div id="comment-87169" class="comment">
<div id="post-87169-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I hadn't even noticed the /dirty was not working anymore. I would be interested in an answer, too.</p>
</div>
<div id="comment-87169-info" class="comment-info">
<span class="comment-age">(25 Apr '23, 10:10)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-87162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87162-form-container" class="comment-form-container">
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

<span id="87166"></span>

<div id="answer-container-87166" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87166-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-87166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The referenced functionality hasn't worked for years for the reasons you state. The rest of your posting isn't a question and needs to be taken elsewhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '23, 07:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-87166" class="comments-container">
<span id="87170"></span>
<div id="comment-87170" class="comment">
<div id="post-87170-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The main question is still valid: How to force rendering of a tile on standard map?</p>
</div>
<div id="comment-87170-info" class="comment-info">
<span class="comment-age">(25 Apr '23, 10:11)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="87171"></span>
<div id="comment-87171" class="comment">
<div id="post-87171-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As the OP already knows and noted (see my answer), that isn't possible, end of story.</p>
</div>
<div id="comment-87171-info" class="comment-info">
<span class="comment-age">(25 Apr '23, 10:16)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87166-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87172"></span>

<div id="answer-container-87172" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87172-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My understanding is the same as the questioner's - I don't think that there is a way to "dirty" a tile so that the <em>next</em> request that a particular client makes for a tile will get an updated version. It's a difficult problem to solve because I've no idea how you'd know where that request would go.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '23, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87172" class="comments-container">
&#10;</div>
<div id="comment-tools-87172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87172-form-container" class="comment-form-container">
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

