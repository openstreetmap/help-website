+++
type = "question"
title = "Rendering or tagging error?"
description = '''The node 31290236 is part of a bridge - the road forks there. On Mapnik rendering it looks like only one part is a bridge and the other goes somehow underneath it. This is however not true, they are connected. Looking at the data, it seems ok and MapQuest layer got the rendering right. Still I&#x27;d lik...'''
date = "2012-02-26T21:44:00Z"
lastmod = "2012-02-27T00:03:00Z"
weight = 10820
keywords = [ "rendering", "mapnik", "bridge" ]
aliases = [ "/questions/10820" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Rendering or tagging error?](/questions/10820/rendering-or-tagging-error)

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
<span id="post-10820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10820-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The node <a href="https://www.openstreetmap.org/browse/node/31290236">31290236</a> is part of a bridge - the road forks there.<br />
On Mapnik rendering it looks like only one part is a bridge and the other goes somehow underneath it. This is however not true, they are connected. Looking at the data, it seems ok and MapQuest layer got the rendering right.<br />
Still I'd like to ask if the data is really correct before filing a bug for Mapnik.<br />
</p>
<p>It is <a href="https://www.openstreetmap.org/?mlat=49.193251&amp;mlon=16.569754&amp;zoom=18&amp;layers=M">here</a>, how it actually looks can by seen <a href="http://www.mapy.cz/s/3ako">here</a></p>
<p><img src="/upfiles/Crossing.png" title="the place concerned" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '12, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></br></p>
</img>
</div>
</div>
<div id="comments-container-10820" class="comments-container">
&#10;</div>
<div id="comment-tools-10820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10820-form-container" class="comment-form-container">
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

<span id="10822"></span>

<div id="answer-container-10822" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10822-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LM_1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is usually a good idea to avoid junctions of ways on different layers. One of the roads at that node is tagged as <code>layer=1</code>, while they other road doesn't have any layer tag. Both roads are tagged as <code>bridge=yes</code>, which sometimes implies <code>layer=1</code>, but it is usually best to tag this explicitly. So I think both roads should be tagged as <code>layer=1</code>.</p>
<p>Tools like <a href="http://keepright.ipax.at/">Keep Right!</a> can warn of these "mixed layers intersections".</p>
<p>Though I'm not sure if this actually affects the Mapnik rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '12, 22:49</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span> </br></p>
</div>
</div>
<div id="comments-container-10822" class="comments-container">
<span id="10823"></span>
<div id="comment-10823" class="comment">
<div id="post-10823-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adding the layer tag helped and since it is the part that goes from one level to another is is not incorrect.</p>
</div>
<div id="comment-10823-info" class="comment-info">
<span class="comment-age">(27 Feb '12, 00:03)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-10822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10822-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10821"></span>

<div id="answer-container-10821" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10821-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a rendering error. You can submit bug descriptions and patches at <a href="http://trac.openstreetmap.org/">trac</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '12, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-10821" class="comments-container">
&#10;</div>
<div id="comment-tools-10821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10821-form-container" class="comment-form-container">
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

