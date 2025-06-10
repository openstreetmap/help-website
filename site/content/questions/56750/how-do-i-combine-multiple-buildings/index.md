+++
type = "question"
title = "How do I combine multiple buildings?"
description = '''So I&#x27;m adding a fitness center that has multiple buildings. I would like the buildings to share the same info and be recognized as one place. Would I do this via multipolygon? Thanks in advance'''
date = "2017-06-26T02:50:00Z"
lastmod = "2017-06-26T12:31:00Z"
weight = 56750
keywords = [ "multiple", "multipolygon" ]
aliases = [ "/questions/56750" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I combine multiple buildings?](/questions/56750/how-do-i-combine-multiple-buildings)

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
<span id="post-56750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56750-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I'm adding a fitness center that has multiple buildings. I would like the buildings to share the same info and be recognized as one place. Would I do this via multipolygon? Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '17, 02:50</strong></p>
<img src="https://secure.gravatar.com/avatar/f520c340d96a71526542aa2a01572467?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lucask1861&#39;s gravatar image" />
<p><span>Lucask1861</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lucask1861 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56750" class="comments-container">
&#10;</div>
<div id="comment-tools-56750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56750-form-container" class="comment-form-container">
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

<span id="56751"></span>

<div id="answer-container-56751" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56751-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-56751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Lucask1861 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you can draw a polygon around them, put all the info on the polygon. If the buildings are spread out and there are other buildings between them or highways or other features, you can put all the buildings in a <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Site">site</a>-relation. However, there are almost no data consumers that support the site relation at this moment.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '17, 04:04</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-56751" class="comments-container">
<span id="56752"></span>
<div id="comment-56752" class="comment">
<div id="post-56752-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Site relation is the right answer here. Drawing a polygon around everything and tagging that doesn't make any sense. You'd have a polygon that might have a name or opening times or so but isn't tagged as anything.</p>
</div>
<div id="comment-56752-info" class="comment-info">
<span class="comment-age">(26 Jun '17, 06:41)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="56754"></span>
<div id="comment-56754" class="comment">
<div id="post-56754-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>depends on whether the area between the buildings also belong to the fitness center or not. I can imagine that in some cases there is a garden with some paths between the different buildings where the garden also belongs to the fitness center.</p>
</div>
<div id="comment-56754-info" class="comment-info">
<span class="comment-age">(26 Jun '17, 12:07)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="56755"></span>
<div id="comment-56755" class="comment">
<div id="post-56755-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The documentation for the site wiki page you linked to suggest multipolygon should perhaps be used: "However, this relation is not to be used in cases where the elements are inside one or more areas where the perimeter can be tagged with an appropriate Area area tag." - followed by examples involving multiple dispersed buildings. If the buildings are close though then the amenity could apply to the whole area and the buildings just be buildings within the area (as per school tagging) and no relation would be needed.</p>
</div>
<div id="comment-56755-info" class="comment-info">
<span class="comment-age">(26 Jun '17, 12:31)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56751-form-container" class="comment-form-container">
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

