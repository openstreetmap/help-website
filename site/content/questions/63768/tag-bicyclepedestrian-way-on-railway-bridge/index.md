+++
type = "question"
title = "Tag bicycle/pedestrian way on railway bridge"
description = '''There is a bridge crossing a river whose characteristics are;  Allow trains to cross the river Has a narrow path on on the bridge next to the tracks that can be used by pedestrians and cyclists. In fact a bicycle route that is part of a relation goes along this path.  How do I tag this path whist it...'''
date = "2018-05-27T23:11:00Z"
lastmod = "2018-05-28T04:16:00Z"
weight = 63768
keywords = [ "cycleway", "railwaybridge" ]
aliases = [ "/questions/63768" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tag bicycle/pedestrian way on railway bridge](/questions/63768/tag-bicyclepedestrian-way-on-railway-bridge)

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
<span id="post-63768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63768-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a bridge crossing a river whose characteristics are;</p>
<ol>
<li>Allow trains to cross the river</li>
<li>Has a narrow path on on the bridge next to the tracks that can be used by pedestrians and cyclists. In fact a bicycle route that is part of a relation goes along this path.</li>
</ol>
<p>How do I tag this path whist it is on the bridge? Do I draw a highway=path right next to railway=rail tag? Do I draw a bridge?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cycleway" rel="tag" title="see questions tagged &#39;cycleway&#39;">cycleway</span> <span class="post-tag tag-link-railwaybridge" rel="tag" title="see questions tagged &#39;railwaybridge&#39;">railwaybridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '18, 23:11</strong></p>
<img src="https://secure.gravatar.com/avatar/c386bfc33fe5fc783e26c89ed54a85b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GavinX&#39;s gravatar image" />
<p><span>GavinX</span><br />
<span class="score" title="56 reputation points">56</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GavinX has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63768" class="comments-container">
&#10;</div>
<div id="comment-tools-63768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63768-form-container" class="comment-form-container">
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

<span id="63775"></span>

<div id="answer-container-63775" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63775-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-63775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can map this as follows</p>
<ul>
<li>2 ways close to one another, one for the railway, one for path. Split both ways at the beginning/end of the bridge and tag that section as bridge=yes, layer=1. Now, at least you know there is a bridge along the path. But it appears as if there are two bridges. You might stop here, and that is what many people have done.</li>
<li>In addition, map the bridge as an area. Tag that area as man_made=bridge, layer=1. The wiki page on <a href="https://wiki.openstreetmap.org/wiki/Tag:man_made=bridge">man_made=bridge</a> has some pictures and details on the proper mapping.</li>
</ul>
<p>Note that the value of the layer lag of bridge=yes and man_made=bridge has to be the same and higher than the layer of the underlying stream, road, etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '18, 04:16</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-63775" class="comments-container">
&#10;</div>
<div id="comment-tools-63775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63775-form-container" class="comment-form-container">
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

