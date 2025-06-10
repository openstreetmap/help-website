+++
type = "question"
title = "How to edit an overlapped way?"
description = '''Not far from where I live there is an abandoned railway. But a path also follows this railway exactly. For the eastern half, I can just about highlight the underlying (cycle) path because the ways diverge slightly at one end. But for the western half I can&#x27;t see how to highlight the underlying path ...'''
date = "2021-02-02T17:17:00Z"
lastmod = "2021-02-03T13:36:00Z"
weight = 78630
keywords = [ "editing", "way" ]
aliases = [ "/questions/78630" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to edit an overlapped way?](/questions/78630/how-to-edit-an-overlapped-way)

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
<span id="post-78630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78630-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Not far from where I live there is an <a href="https://www.openstreetmap.org/way/25818737#map=15/50.2533/-5.0565">abandoned railway</a>. But a path also follows this railway exactly. For the eastern half, I can just about highlight the underlying (cycle) path because the ways diverge slightly at one end. But for the western half I can't see how to highlight the underlying path to edit it (I want to add 'bicyles=yes')- or even if such a path exists on OSM! A search through other answers suggests using '/' in Potlatch, but the potlatch editor option seems to have disappeared. I'm using the standard editor, tried on Firefox and Chrome.</p>
<p>[later] there is a (footpath) underlying the railway, I can see it on OpenCycleMap. But I can't see it on OSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '21, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/75a3968b636bd5edde4fe95bd276176e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quilkin&#39;s gravatar image" />
<p><span>quilkin</span><br />
<span class="score" title="116 reputation points">116</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quilkin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Feb '21, 20:00</strong> </span></p>
</div>
</div>
<div id="comments-container-78630" class="comments-container">
<span id="78631"></span>
<div id="comment-78631" class="comment">
<div id="post-78631-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>(slightly unrelated to the main bit of the question) but Potlatch is now downloadable at <a href="https://www.systemed.net/potlatch/download/">https://www.systemed.net/potlatch/download/</a> .</p>
</div>
<div id="comment-78631-info" class="comment-info">
<span class="comment-age">(02 Feb '21, 17:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="78633"></span>
<div id="comment-78633" class="comment">
<div id="post-78633-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have now tried Potlatch but no help, sorry. the '/' command is listed but appears to do nothing. And I can't even highight the part of the cycle track that I can with the web editor.</p>
</div>
<div id="comment-78633-info" class="comment-info">
<span class="comment-age">(02 Feb '21, 19:59)</span> <span class="comment-user userinfo">quilkin</span>
</div>
</div>
<span id="78634"></span>
<div id="comment-78634" class="comment">
<div id="post-78634-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The "/" works if the ways share nodes (it toggles through ways which use a given node) not ways at a given location so you need to select a node. One way with iD is to hide the railway layer (scroll down the menu in the "Map Data" option at RHS of screen until you see "Map Features", rail features is about 10 items down). PS. Dont forget to toggle it back or you may get puzzled later on. (Also this discussion on options in a range of editors which suggests "\" should do something similar in iD - although it doesnt for me)</p>
</div>
<div id="comment-78634-info" class="comment-info">
<span class="comment-age">(02 Feb '21, 20:21)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="78636"></span>
<div id="comment-78636" class="comment">
<div id="post-78636-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It should be noted that using two overlapping ways like this isn't how a situation like this is generally mapped. Since this is really one linear feature - a path following the route of an abandoned railway bed - there should be one way with the tags for both features. This way can be split for the piece at the east end, which would just have the railway tags.</p>
</div>
<div id="comment-78636-info" class="comment-info">
<span class="comment-age">(02 Feb '21, 22:49)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="78640"></span>
<div id="comment-78640" class="comment">
<div id="post-78640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> I think your statement is a little too dogmatic. It is not uncommon for them to be mapped as two separate ways &amp; there are probably cases where this is for good reasons.</p>
</div>
<div id="comment-78640-info" class="comment-info">
<span class="comment-age">(03 Feb '21, 13:36)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78630-form-container" class="comment-form-container">
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

<span id="78635"></span>

<div id="answer-container-78635" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78635-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks to <a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a>, I have now managed to edit this. For future reference:</p>
<ul>
<li>In Potlatch, click on a node and then use '/' to scroll between overlaid ways.</li>
<li>In iD, use 'Map Features' and toggle off 'Past/Future features' (or whatever needs hiding); apparently an abandoned railway isn't a railway but a 'past feature'. Makes sense I guess.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '21, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/75a3968b636bd5edde4fe95bd276176e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quilkin&#39;s gravatar image" />
<p><span>quilkin</span><br />
<span class="score" title="116 reputation points">116</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quilkin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78635" class="comments-container">
&#10;</div>
<div id="comment-tools-78635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78635-form-container" class="comment-form-container">
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

