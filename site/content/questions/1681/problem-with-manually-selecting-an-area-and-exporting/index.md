+++
type = "question"
title = "problem with manually selecting an area and exporting?"
description = '''When I manually select an area to export, the minimum longitude value (for example) in the osm file is not actually the minimum longitude value across all nodes. So, when I parse the osm file to generate a map in my software program, the bounds cannot be generated correctly (unless I iterate through...'''
date = "2010-11-30T16:48:00Z"
lastmod = "2010-11-30T18:00:00Z"
weight = 1681
keywords = [ "export" ]
aliases = [ "/questions/1681" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [problem with manually selecting an area and exporting?](/questions/1681/problem-with-manually-selecting-an-area-and-exporting)

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
<span id="post-1681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1681-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I manually select an area to export, the minimum longitude value (for example) in the osm file is not actually the minimum longitude value across all nodes. So, when I parse the osm file to generate a map in my software program, the bounds cannot be generated correctly (unless I iterate through all nodes and find the minimum longitude value myself).</p>
<p>Am I missing something?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '10, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/dc3a22502276d7e548c0bd9872cb4cbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joelosm&#39;s gravatar image" />
<p><span>joelosm</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joelosm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1681" class="comments-container">
&#10;</div>
<div id="comment-tools-1681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1681-form-container" class="comment-form-container">
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

<span id="1684"></span>

<div id="answer-container-1684" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1684-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joelosm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you export an osm file you get all the nodes in the bbox, and all ways that contains a node in the bbox, and all the nodes that is contained in those ways, and all the relations that contains a node or a way that is exported.</p>
<p>This means that you can get nodes outside the bbox if it is contained in a way that touches the bbox. Note that you are not guaranteed to get all nodes of any area outside of the bbox. Depending on your application you might have to filter or ignore those nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '10, 18:00</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1684" class="comments-container">
&#10;</div>
<div id="comment-tools-1684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1684-form-container" class="comment-form-container">
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

