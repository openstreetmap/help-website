+++
type = "question"
title = "Track surface vs tracktype and Mapnik rendering"
description = '''I noticed that Mapnik rendered some tracks in maroon dashes or continued line (like roads). If a track&#x27;s surface is made of concrete and tagged as surface=concrete, will it be rendered as a continuous line in Mapnik?'''
date = "2012-07-11T20:02:00Z"
lastmod = "2012-07-12T07:34:00Z"
weight = 14194
keywords = [ "track", "tracktype", "surface", "mapnik" ]
aliases = [ "/questions/14194" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Track surface vs tracktype and Mapnik rendering](/questions/14194/track-surface-vs-tracktype-and-mapnik-rendering)

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
<span id="post-14194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14194-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I noticed that Mapnik rendered some tracks in maroon dashes or continued line (like roads).</p>
<p>If a track's surface is made of concrete and tagged as surface=concrete, will it be rendered as a continuous line in Mapnik?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-tracktype" rel="tag" title="see questions tagged &#39;tracktype&#39;">tracktype</span> <span class="post-tag tag-link-surface" rel="tag" title="see questions tagged &#39;surface&#39;">surface</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '12, 20:02</strong></p>
<img src="https://secure.gravatar.com/avatar/1fb9da36bbe8817c461df33d395ee413?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerdami&#39;s gravatar image" />
<p><span>gerdami</span><br />
<span class="score" title="696 reputation points">696</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="46 badges"><span class="bronze">●</span><span class="badgecount">46</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerdami has 2 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-14194" class="comments-container">
&#10;</div>
<div id="comment-tools-14194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14194-form-container" class="comment-form-container">
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

<span id="14196"></span>

<div id="answer-container-14196" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14196-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-14196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gerdami has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. The Mapnik <a href="http://wiki.openstreetmap.org/wiki/Mapnik#Stylesheet">style sheet</a> we currently use doesn't recognize any surface tags but it can be implemented of course. There as been a <a href="http://help.openstreetmap.org/questions/5503/are-there-any-plans-to-implement-keysurface-rendering-ever">similar answer on help</a>, a rather old <a href="https://trac.openstreetmap.org/ticket/1447">ticket</a> and probably several <a href="http://lists.openstreetmap.org/pipermail/dev/2011-June/022789.html">mailing list discussion</a>s about this issue. There is also an <a href="http://www.itoworld.com/map/25">ITO Map</a> showing different surface tags in different colors.</p>
<p>But it doesn't seem like there are any current plans in supporting the surface tag in <a href="https://trac.openstreetmap.org/browser/applications/rendering/mapnik/osm.xml">our Mapnik style sheet</a>. Yet you can try to add it or improve existing patches in hope somebody will merge your changes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '12, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '12, 20:48</strong> </span></p>
</div>
</div>
<div id="comments-container-14196" class="comments-container">
<span id="14204"></span>
<div id="comment-14204" class="comment">
<div id="post-14204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply and all useful links. I understand now that it is only the tracktype=grade 1-5 that produces different Mapnik renderings. However, the relation analyser actually uses the surface key to compute surface composition averages for relations. Hence I should use both keys, e.g. surface=concrete and tracktype=grade1.</p>
</div>
<div id="comment-14204-info" class="comment-info">
<span class="comment-age">(12 Jul '12, 00:02)</span> <span class="comment-user userinfo">gerdami</span>
</div>
</div>
<span id="14209"></span>
<div id="comment-14209" class="comment">
<div id="post-14209-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oups, my mistake. The relation analyser computes percentages of roads, tracks, paths for let's say a walking route.</p>
</div>
<div id="comment-14209-info" class="comment-info">
<span class="comment-age">(12 Jul '12, 07:34)</span> <span class="comment-user userinfo">gerdami</span>
</div>
</div>
</div>
<div id="comment-tools-14196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14196-form-container" class="comment-form-container">
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

