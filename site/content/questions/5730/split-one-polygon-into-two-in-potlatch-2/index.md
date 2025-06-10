+++
type = "question"
title = "Split One Polygon into Two in Potlatch 2?"
description = '''Is there a way I can split one large polygon in Potlatch 2 into two smaller ones (to save redrawing / adding nodes)? This is for landuse - to save editing and redrawing large parts. Ideally, the two split halves would inherit the same tags from the parent. Thanks'''
date = "2011-06-13T12:57:00Z"
lastmod = "2011-06-13T13:35:00Z"
weight = 5730
keywords = [ "potlatch2", "polgon", "editing", "split" ]
aliases = [ "/questions/5730" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Split One Polygon into Two in Potlatch 2?](/questions/5730/split-one-polygon-into-two-in-potlatch-2)

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
<span id="post-5730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5730-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way I can split one large polygon in Potlatch 2 into two smaller ones (to save redrawing / adding nodes)?</p>
<p>This is for landuse - to save editing and redrawing large parts. Ideally, the two split halves would inherit the same tags from the parent.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-polgon" rel="tag" title="see questions tagged &#39;polgon&#39;">polgon</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '11, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/fafdd7d0595258b50e78e78156d4c2d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tommg&#39;s gravatar image" />
<p><span>tommg</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tommg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5730" class="comments-container">
&#10;</div>
<div id="comment-tools-5730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5730-form-container" class="comment-form-container">
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

<span id="5731"></span>

<div id="answer-container-5731" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5731-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-5731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tommg has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>You can select a node where you would like to split the polygon, and click the "cut" icon. This will split the single way into two parts (obviously there will be another split created somewhere around the loop.</p>
<p>Both halves will inherit the tags from the whole, however, you will now have two linear ways, rather than one area. If it is landuse, you will need to join the areas back into two separate circular ways for it to render again.</p>
<p>i.e. assume you have a square field with six nodes, A-F</p>
<p>A--------B---------C</p>
<p>|......................|</p>
<p>|......................|</p>
<p>|......................|</p>
<p>D--------E----------F</p>
<p>You could split this at E. Assuming the way also splits at B, you then have two separate ways, BADE and BCFE.</p>
<p>You would then need to join E to B (perhaps via some new nodes) twice, once for way BADE and once for way BCFE, if that makes sense...?</p>
<p>Regards Chris</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '11, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7a81832ca1b48080d1a57be29dff3a8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="c2r&#39;s gravatar image" />
<p><span>c2r</span><br />
<span class="score" title="413 reputation points">413</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="c2r has 2 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-5731" class="comments-container">
<span id="5732"></span>
<div id="comment-5732" class="comment">
<div id="post-5732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(Note that if there multipolygon relations, then this becomes slightly more tricky)</p>
</div>
<div id="comment-5732-info" class="comment-info">
<span class="comment-age">(13 Jun '11, 13:35)</span> <span class="comment-user userinfo">c2r</span>
</div>
</div>
</div>
<div id="comment-tools-5731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5731-form-container" class="comment-form-container">
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

