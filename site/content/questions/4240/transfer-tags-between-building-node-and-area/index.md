+++
type = "question"
title = "Transfer tags between building node and area"
description = '''I drew a number of buildings from aerial imagery, using the terracer plugin in JOSM, and now I have higher quality building outlines, though they don&#x27;t have addressing information on them. What I&#x27;d like to do is convert the buildings to centroids, transferring the tags in the process, then transfer ...'''
date = "2011-04-01T02:34:00Z"
lastmod = "2011-04-01T07:58:00Z"
weight = 4240
keywords = [ "building", "josm", "plugin" ]
aliases = [ "/questions/4240" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Transfer tags between building node and area](/questions/4240/transfer-tags-between-building-node-and-area)

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
<span id="post-4240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4240-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I drew a number of buildings from aerial imagery, using the terracer plugin in JOSM, and now I have higher quality building outlines, though they don't have addressing information on them. What I'd like to do is convert the buildings to centroids, transferring the tags in the process, then transfer the tags from the nodes back to the new building outlines. I'm pretty sure this is something a JOSM plugin or script could do, but I wanted to see if this functionality exists before I reinvent the wheel.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '11, 02:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ba99ad3778972fee07700e1eb36cc822?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoshD&#39;s gravatar image" />
<p><span>JoshD</span><br />
<span class="score" title="300 reputation points">300</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoshD has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-4240" class="comments-container">
&#10;</div>
<div id="comment-tools-4240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4240-form-container" class="comment-form-container">
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

<span id="4241"></span>

<div id="answer-container-4241" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4241-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-4241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no JOSM plugin that would automatically select a node inside a building for transferring tags. However a manual tag transfer is possible with this procedure:</p>
<ul>
<li>select node</li>
<li>hit Ctrl-C to copy node to clipboard</li>
<li>hit Del to delete node</li>
<li>select building outline way</li>
<li>hit Shift-Strl-V to copy tags from object in clipboard to selected object</li>
</ul>
<p>Some people prefer to actually merge the node into the building outline and remove the tags from it. This is more manual work but it preserves the edit history of the building.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '11, 07:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-4241" class="comments-container">
&#10;</div>
<div id="comment-tools-4241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4241-form-container" class="comment-form-container">
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

