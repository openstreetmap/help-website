+++
type = "question"
title = "Snapping feature"
description = '''Is it possible to snap (ArcGis tool) line feature to a polygon without joining vertexes? '''
date = "2013-05-17T11:19:00Z"
lastmod = "2013-05-17T14:16:00Z"
weight = 22503
keywords = [ "snap", "arcgis", "snapping" ]
aliases = [ "/questions/22503" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Snapping feature](/questions/22503/snapping-feature)

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
<span id="post-22503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22503-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to snap (ArcGis tool) line feature to a polygon without joining vertexes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-snap" rel="tag" title="see questions tagged &#39;snap&#39;">snap</span> <span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span> <span class="post-tag tag-link-snapping" rel="tag" title="see questions tagged &#39;snapping&#39;">snapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '13, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/7bcdd445994c4d88c988c3e91c38413e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mjolnirr&#39;s gravatar image" />
<p><span>mjolnirr</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mjolnirr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '13, 11:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-22503" class="comments-container">
&#10;</div>
<div id="comment-tools-22503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22503-form-container" class="comment-form-container">
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

<span id="22515"></span>

<div id="answer-container-22515" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22515-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think it is and I cannot see a reason why one would do it.</p>
<p>Either both objects have a topological relationship - e.g. the fence is exactly at the boundary of the meadow. Then you <em>want</em> joined vertexes (else somebody fixes the geometry of the meadow and the fence is not fixed with it).</p>
<p>Or both objects are defined independently of each other, e.g. both the fence and the meadow are visible from the aerial imagery and you want both to have their own geometry. Then you want neither shared vertexes nor snapped geometry!</p>
<p>(JOSM will not join vertexes if you hold the Ctrl key while clicking at the new node position, however that means no snapping either.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '13, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22515" class="comments-container">
&#10;</div>
<div id="comment-tools-22515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22515-form-container" class="comment-form-container">
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

