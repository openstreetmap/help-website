+++
type = "question"
title = "Osmose &quot;Highway underground and no tunnel&quot;"
description = '''Should be ways be drawn under the area representing pedestrian square? http://osmose.openstreetmap.fr/cs/error/33636894748 https://www.openstreetmap.org/way/691454935 I am the author and found my edit in Osmose.'''
date = "2019-10-09T10:23:00Z"
lastmod = "2019-10-11T17:51:00Z"
weight = 71084
keywords = [ "mapping", "osmose", "routing", "area" ]
aliases = [ "/questions/71084" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Osmose "Highway underground and no tunnel"](/questions/71084/osmose-highway-underground-and-no-tunnel)

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
<span id="post-71084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71084-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Should be ways be drawn under the area representing pedestrian square?</p>
<p><a href="http://osmose.openstreetmap.fr/cs/error/33636894748">http://osmose.openstreetmap.fr/cs/error/33636894748</a> <a href="https://www.openstreetmap.org/way/691454935">https://www.openstreetmap.org/way/691454935</a></p>
<p>I am the author and found my edit in Osmose.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-osmose" rel="tag" title="see questions tagged &#39;osmose&#39;">osmose</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '19, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/418a2db325df1a1bb60780c0274eb6ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="batat&#39;s gravatar image" />
<p><span>batat</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="batat has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71084" class="comments-container">
<span id="71114"></span>
<div id="comment-71114" class="comment">
<div id="post-71114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It should be noted that the Osmose error is fundamentally flawed in treating layer=-1 as being an object that's underground. That isn't what the tag means. It did find something that was a real issue in this case, but for the wrong reason. The real issue was two unconnected and crossing highways with different layer tags and neither with bridge or tunnel tags.</p>
</div>
<div id="comment-71114-info" class="comment-info">
<span class="comment-age">(11 Oct '19, 17:51)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-71084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71084-form-container" class="comment-form-container">
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

<span id="71085"></span>

<div id="answer-container-71085" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71085-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.openstreetmap.org/way/691454935">Way 691454935</a> is tagged with <code>layer=-1</code>. It is on the same level as the <a href="https://www.openstreetmap.org/way/140304144">pedestrian area</a>, hence it should get the same layer tag. <code>layer=-1</code> needs to be removed from this way and from other similar ways in this area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '19, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71085" class="comments-container">
&#10;</div>
<div id="comment-tools-71085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71085-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71102"></span>

<div id="answer-container-71102" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71102-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to the <a href="https://wiki.openstreetmap.org/wiki/Layer">Wiki on Layers</a>:</p>
<blockquote>
<p>When editing, the <code>layer=*</code> tag is used to describe vertical relationships between crossing or overlapping elements, e.g. a bridge over a street.</p>
</blockquote>
<p>So the pedestrian area and the ways should be on the same level as <a href="https://help.openstreetmap.org/questions/71084/osmose-highway-underground-and-no-tunnel/71085">scai said</a>. In other words, the layer keys should be removed.</p>
<p>Mapping is about modelling real life objects and their relations to each other. <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">You shouldn't map to the renderer</a> thus You shouldn't care about how the rendering engine will show the given way inside that area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '19, 00:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a9715d60e31c91a442c2dacefdc1dae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UntaggedWay&#39;s gravatar image" />
<p><span>UntaggedWay</span><br />
<span class="score" title="576 reputation points">576</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UntaggedWay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '19, 00:03</strong> </span></p>
</div>
</div>
<div id="comments-container-71102" class="comments-container">
&#10;</div>
<div id="comment-tools-71102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71102-form-container" class="comment-form-container">
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

