+++
type = "question"
title = "How to split a building into two?"
description = '''How do I split a building into two? A former hotel occupying two villas was converted to a single residential building (shown on the map), but then split into two separate residential dwellings, each with own house number. I should like to update the map to show this last change. How do I make that ...'''
date = "2021-04-14T19:46:00Z"
lastmod = "2021-04-15T09:35:00Z"
weight = 79676
keywords = [ "building", "splitting", "wikidata", "feature", "delete" ]
aliases = [ "/questions/79676" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to split a building into two?](/questions/79676/how-to-split-a-building-into-two)

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
<span id="post-79676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79676-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I split a building into two?</p>
<p>A former hotel occupying two villas was converted to a single residential building (shown on the map), but then split into two separate residential dwellings, each with own house number. I should like to update the map to show this last change.</p>
<p>How do I make that amendment? (I have previously managed a couple of other edits, but I am still very much a newbie.)</p>
<p>It seems simplest to delete the feature and start again, but this is apparently blocked by the fact that there is wikidata associated with it.</p>
<p>In case anyone wants to look, the address is 25 and 26 (shown as 25-26) Pembridge Square, London W2.</p>
<p>TIA!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-splitting" rel="tag" title="see questions tagged &#39;splitting&#39;">splitting</span> <span class="post-tag tag-link-wikidata" rel="tag" title="see questions tagged &#39;wikidata&#39;">wikidata</span> <span class="post-tag tag-link-feature" rel="tag" title="see questions tagged &#39;feature&#39;">feature</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '21, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a0825f2629b0629841a7f65b887969ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daslondon&#39;s gravatar image" />
<p><span>daslondon</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daslondon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>14 Apr '21, 19:49</strong> </span></p>
</div>
</div>
<div id="comments-container-79676" class="comments-container">
<span id="79679"></span>
<div id="comment-79679" class="comment">
<div id="post-79679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems you already have tried (<a href="https://www.openstreetmap.org/changeset/102947630">Changeset</a>) and stumbled upon one of ID's annoying "features" where it creates relations when you try to split features. Now it requires a bit of repairing before any other solution works. Keep that in mind when going on.</p>
<p>But don't worry. No major harm done.</p>
</div>
<div id="comment-79679-info" class="comment-info">
<span class="comment-age">(15 Apr '21, 09:00)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-79676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79676-form-container" class="comment-form-container">
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

<span id="79677"></span>

<div id="answer-container-79677" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79677-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using the JOSM editor you can select two points on the polygon then under "additional tools" (which might be a plug-in) select "split object". If there are no nodes/points where you want to do the split, then you can add them first.</p>
<p>I suspect that the web based iD will have some similar functionality but I don't use that editor so I can't say for sure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '21, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-79677" class="comments-container">
&#10;</div>
<div id="comment-tools-79677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79677-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79680"></span>

<div id="answer-container-79680" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79680-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In iD there is no easy way of doing it. Avoid using the function to split the way as it will create a relation which is even harder to handle in iD.</p>
<p>Probably the easiest way of doing it is just refining the existing outline to only cover one of the building parts and change the house number. Then draw a new outline for the other half and apply the appropriate tags.</p>
<p>Or after refining the outline to the first building you can copy and paste outline and turn the copy into the second building. In this way you retain all the tags and just have to change the house number. But make sure the nodes of the two building parts are joined (grey not white nodes) where the building parts meet.</p>
<p>The whole exercise is much easier to be accomplished with JOSM which stf already has explained.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '21, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-79680" class="comments-container">
&#10;</div>
<div id="comment-tools-79680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79680-form-container" class="comment-form-container">
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

