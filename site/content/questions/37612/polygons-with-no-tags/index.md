+++
type = "question"
title = "Polygons with no tags"
description = '''I found on the map near Mazin, Croatia a polygon with no tags but &quot;source = landsat&quot;. Is it rubbish or what does it stand for?'''
date = "2014-10-14T18:16:00Z"
lastmod = "2014-10-14T18:50:00Z"
weight = 37612
keywords = [ "notags", "polygon" ]
aliases = [ "/questions/37612" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Polygons with no tags](/questions/37612/polygons-with-no-tags)

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
<span id="post-37612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37612-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I found on the map near Mazin, Croatia a polygon with no tags but "source = landsat". Is it rubbish or what does it stand for?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-notags" rel="tag" title="see questions tagged &#39;notags&#39;">notags</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '14, 18:16</strong></p>
<img src="https://secure.gravatar.com/avatar/3f98397b356009a6d5cdd11e4afbec94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reinhard%20Tisma&#39;s gravatar image" />
<p><span>Reinhard Tisma</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reinhard Tisma has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37612" class="comments-container">
&#10;</div>
<div id="comment-tools-37612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37612-form-container" class="comment-form-container">
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

<span id="37614"></span>

<div id="answer-container-37614" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37614-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-37614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I presume that you mean this one:</p>
<p><a href="https://www.openstreetmap.org/way/77629035">https://www.openstreetmap.org/way/77629035</a></p>
<p>It's actually part of a "<a href="https://wiki.openstreetmap.org/wiki/Multipolygon">multipolygon</a>" - a piece of forest shaped like a doughnut:</p>
<p><a href="https://www.openstreetmap.org/relation/1369031">https://www.openstreetmap.org/relation/1369031</a></p>
<p>That has the relevant tags on it, including "<a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dforest">landuse=forest</a>".</p>
<p>It's perfectly OK to have the multipolygon tags on the relation, as it enables a mapper to have different tags on the constituent ways (for example, when mapping a forest I might have been able to do some parts from survey and the rest only from aerial imagery, and might want to use different "source" tags), while keeping the tags that apply to the relation as a whole on the relation.</p>
<p>A word of warning - the outer way of this forest has a very large number of nodes, so if you try and use Potlatch 2's** internal history viewer your browser may struggle. Also, you'll notice in Potlatch 2 that it doesn't render the forest as a forest (because the main tag's on the relation) - unfortunately this is normal.</p>
<p>** I'm guessing that you're using that editor based on a similarly named mapper's previous edits; apologies if I've got the wrong person.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '14, 18:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Oct '14, 19:02</strong> </span></p>
</div>
</div>
<div id="comments-container-37614" class="comments-container">
&#10;</div>
<div id="comment-tools-37614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37614-form-container" class="comment-form-container">
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

