+++
type = "question"
title = "Island rendered improperly after improved outline is done."
description = '''Hello, Need urgent help needed here. Pulau Banding 5.5438, 101.3434 I was improving the outline of the island by using FastDraw plugin on JOSM. I removed a portion of existing outline of island. Then I drew a more correct outline and join it up to make it whole again. I have tested the method first ...'''
date = "2021-01-28T16:48:00Z"
lastmod = "2021-01-29T00:09:00Z"
weight = 78574
keywords = [ "mapping", "error" ]
aliases = [ "/questions/78574" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Island rendered improperly after improved outline is done.](/questions/78574/island-rendered-improperly-after-improved-outline-is-done)

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
<span id="post-78574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78574-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, Need urgent help needed here.</p>
<p>Pulau Banding 5.5438, 101.3434</p>
<p>I was improving the outline of the island by using FastDraw plugin on JOSM. I removed a portion of existing outline of island. Then I drew a more correct outline and join it up to make it whole again. I have tested the method first on nearby island a couple of times and there was no issue. So I thought the method is alright. When I did the same method to Pulau Banding, these was a sort of wash out when the map renders. I hope someone can pinpoint the error or revert the map back.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '21, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/f0fa1124bfe0753c1883b68eb8de8ec5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="banban_msm&#39;s gravatar image" />
<p><span>banban_msm</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="banban_msm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78574" class="comments-container">
&#10;</div>
<div id="comment-tools-78574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78574-form-container" class="comment-form-container">
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

<span id="78577"></span>

<div id="answer-container-78577" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78577-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There was a small gap between two nodes at the north end of the island, so the way that describes the island wasn't closed. Since this island is an inner of the larger lake multipolygon relation, this break caused the entire lake to stop rendering properly. I connected the two nodes to close the island way (<a href="https://www.openstreetmap.org/changeset/98311277">changeset</a>), so things should show up properly soon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '21, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-78577" class="comments-container">
<span id="78585"></span>
<div id="comment-78585" class="comment">
<div id="post-78585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much, alester. Made my morning. I would have been left worried for a few coming days. I have to be more careful in the future and have to be wary of the temptation of correcting badly drawn land outlines. In hindsight I thought I should break the relation before redrawing and put back the relation after that. Would this have made a difference? Any suggestion of a better way of doing this?</p>
</div>
<div id="comment-78585-info" class="comment-info">
<span class="comment-age">(28 Jan '21, 23:22)</span> <span class="comment-user userinfo">banban_msm</span>
</div>
</div>
<span id="78586"></span>
<div id="comment-78586" class="comment">
<div id="post-78586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Removing and re-adding the relation may have helped show that there was an issue, but it would also wipe out the history of the relation, so I don't think that would be the way to go.</p>
<p>I see that you use JOSM for your edits. A good thing to do is run the built-in Validator before you upload changes, which will check for common issues. This is what I used to find the issue in this case. The validator reported the broken multipolygon relation and identified the nodes where the issue was occurring.</p>
</div>
<div id="comment-78586-info" class="comment-info">
<span class="comment-age">(29 Jan '21, 00:09)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-78577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78577-form-container" class="comment-form-container">
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

