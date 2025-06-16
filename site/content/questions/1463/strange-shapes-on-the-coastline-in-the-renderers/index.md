+++
type = "question"
title = "Strange shapes on the coastline in the renderers"
description = '''How can I fix or get rid of the odd triangle shape here? https://www.openstreetmap.org/?lat=-20.501&amp;amp;lon=116.848&amp;amp;zoom=9&amp;amp;layers=M'''
date = "2010-11-05T14:31:00Z"
lastmod = "2010-11-05T15:14:00Z"
weight = 1463
keywords = [ "shapes" ]
aliases = [ "/questions/1463" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Strange shapes on the coastline in the renderers](/questions/1463/strange-shapes-on-the-coastline-in-the-renderers)

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
<span id="post-1463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1463-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I fix or get rid of the odd triangle shape here? <a href="https://www.openstreetmap.org/?lat=-20.501&amp;lon=116.848&amp;zoom=9&amp;layers=M"></a><a href="https://www.openstreetmap.org/?lat=-20.501&amp;lon=116.848&amp;zoom=9&amp;layers=M"></a><a href="https://www.openstreetmap.org/?lat=-20.501&amp;lon=116.848&amp;zoom=9&amp;layers=M">https://www.openstreetmap.org/?lat=-20.501&amp;lon=116.848&amp;zoom=9&amp;layers=M</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapes" rel="tag" title="see questions tagged &#39;shapes&#39;">shapes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '10, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/bb3567df51199dcfc295966cb56cb357?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Moondyne&#39;s gravatar image" />
<p><span>Moondyne</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Moondyne has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '10, 16:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-1463" class="comments-container">
&#10;</div>
<div id="comment-tools-1463" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1463-form-container" class="comment-form-container">
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

<span id="1466"></span>

<div id="answer-container-1466" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1466-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems that it might have been a problem with the coastline data since both mapnik and osmrenderer shows errors in the coastline. However this seems to have been fixed since the newer (higher zoom levels) tiles do not show these artifacts. You just have to wait for the renderers to get around and render the tile again. This might take a few days since the bigger areas takes longer to render and therefore gets scheduled with lower priority.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '10, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1466" class="comments-container">
&#10;</div>
<div id="comment-tools-1466" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1466-form-container" class="comment-form-container">
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

