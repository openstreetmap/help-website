+++
type = "question"
title = "Holes in scrub (relations, inner &amp; outer)"
description = '''At http://www.openstreetmap.org/?lat=46.84408&amp;amp;lon=11.69212&amp;amp;zoom=16&amp;amp;layers=M I have a scrub, where within there are some open areas with landuse=meadow (clearly visible in the data inspector). The scrub (way 85074083) is outer on relation 1270018, with 7 ways being inner in this relation,...'''
date = "2010-11-13T00:58:00Z"
lastmod = "2010-11-13T10:25:00Z"
weight = 1535
keywords = [ "landuse", "inner", "relations" ]
aliases = [ "/questions/1535" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Holes in scrub (relations, inner & outer)](/questions/1535/holes-in-scrub-relations-inner-outer)

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
<span id="post-1535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1535-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>At <a href="http://www.openstreetmap.org/?lat=46.84408&amp;lon=11.69212&amp;zoom=16&amp;layers=M">http://www.openstreetmap.org/?lat=46.84408&amp;lon=11.69212&amp;zoom=16&amp;layers=M</a> I have a scrub, where within there are some open areas with landuse=meadow (clearly visible in the data inspector).</p>
<p>The scrub (way 85074083) is outer on relation 1270018, with 7 ways being inner in this relation, but they don't show up on mapnik. I don't have problems putting holes in forests though.</p>
<p>On the other hand, <a href="http://www.openstreetmap.org/?lat=46.82837&amp;lon=11.775642&amp;zoom=18&amp;layers=M">http://www.openstreetmap.org/?lat=46.82837&amp;lon=11.775642&amp;zoom=18&amp;layers=M</a> shows a church inside a graveyard, but the graveyard is also over the church, even though I also made it a hole in the graveyard's releation. I don't see any difference (in tagging) to <a href="http://www.openstreetmap.org/?lat=46.843974&amp;lon=11.725565&amp;zoom=18&amp;layers=M">http://www.openstreetmap.org/?lat=46.843974&amp;lon=11.725565&amp;zoom=18&amp;layers=M</a> where it is rendered correctly. What am I doing wrong/what am I not seeing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-inner" rel="tag" title="see questions tagged &#39;inner&#39;">inner</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '10, 00:58</strong></p>
<img src="https://secure.gravatar.com/avatar/720ecc66aa0d49f61a12c4d9e526e66f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexander%20Roalter&#39;s gravatar image" />
<p><span>Alexander Ro...</span><br />
<span class="score" title="276 reputation points">276</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexander Roalter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1535" class="comments-container">
&#10;</div>
<div id="comment-tools-1535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1535-form-container" class="comment-form-container">
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

<span id="1536"></span>

<div id="answer-container-1536" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1536-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alexander Roalter has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You haven't tagged the relations correctly. For the scrub relation and the graveyard/church relation, they don't have any tags at all, though the ways that are part of them are tagged correctly. You have to tag the relations as <code>type=multipolygon</code></p>
<p>Then the renderer will know it is a multipolygon relation, with separate outer and inner parts, and show it correctly. See the wiki page for details: <a href="http://wiki.openstreetmap.org/wiki/Relation:multipolygon">Relation:multipolygon</a> The second example graveyard/church relation is tagged as <code>type=multipolygon</code>, and as you say, it is rendered correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '10, 01:50</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-1536" class="comments-container">
<span id="1537"></span>
<div id="comment-1537" class="comment">
<div id="post-1537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the explanation. Apparently, in woods the renderer renders holes just fine, so I didn't see the need for the multipolygon there. Don't remember how I did that for the one graveyard where it was already ok...</p>
<p>It renders OK now, but here <a href="http://www.openstreetmap.org/?lat=46.84927&amp;lon=11.69452&amp;zoom=16&amp;layers=M">http://www.openstreetmap.org/?lat=46.84927&amp;lon=11.69452&amp;zoom=16&amp;layers=M</a> (in the center) the big area is tagged as wood=confierous,landuse=forest, but is not rendered as such... One other difference in the graveyards was the other one that worked was tagged cemetary. Once changed to grave_yard, making a hole doesn't work as expected anymore.</p>
</div>
<div id="comment-1537-info" class="comment-info">
<span class="comment-age">(13 Nov '10, 10:25)</span> <span class="comment-user userinfo">Alexander Ro...</span>
</div>
</div>
</div>
<div id="comment-tools-1536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1536-form-container" class="comment-form-container">
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

