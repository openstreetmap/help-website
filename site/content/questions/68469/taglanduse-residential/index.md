+++
type = "question"
title = "tag:landuse-residential"
description = '''Background I have read the discussion on tag:launduse=residential and see three usage. I focus on the first two only. These are: 1) split residential areas into blocks that do not contain any streets 2) restrict such splitting to major thoroughfares My main mapping focus is on paths, footpaths and r...'''
date = "2019-03-24T17:28:00Z"
lastmod = "2019-03-25T19:11:00Z"
weight = 68469
keywords = [ "residential" ]
aliases = [ "/questions/68469" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tag:landuse-residential](/questions/68469/taglanduse-residential)

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
<span id="post-68469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68469-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Background</strong></p>
<p>I have read the discussion on <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dresidential">tag:launduse=residential</a> and see three usage. I focus on the first two only. These are:</p>
<p>1) split residential areas into blocks that do not contain any streets 2) restrict such splitting to major thoroughfares</p>
<p>My main mapping focus is on paths, footpaths and roads for walking. In doing that I often find polygon edges for areas (scrub, wood, forest landuse etc) and highways (roads, paths etc) are very close together and often are joined at some or all of their nodes.</p>
<p>For my part of the world, usage 1) streets not included is the exclusive usage.</p>
<p>When attempting to add, remove or adjust the line for a path I regularly find I have to adjust the edges of one or more area polygons. In doing this for landuse=residential I have found different standards by which the edge was originally placed. As often as not close to the line for the road and well outside, relatively speaking, the residential properties themselves.</p>
<p>In those circumstances I have felt tempted to simplify the presentation to usage 2) above.</p>
<p><strong>Request</strong></p>
<p>To help me decide what to do in future would readers please offer discussion on this matter.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '19, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/74f0fedc2fe8cb83660a329f79f88791?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlwynWellington&#39;s gravatar image" />
<p><span>AlwynWellington</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlwynWellington has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68469" class="comments-container">
<span id="68487"></span>
<div id="comment-68487" class="comment">
<div id="post-68487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As mentioned by InsertUser, there's debate regarding whether landuse should extend to the centerline or to the edge of the road. However, I think both sides would probably agree that mapping it to somewhere in between the two, as described above, would be "wrong".</p>
</div>
<div id="comment-68487-info" class="comment-info">
<span class="comment-age">(25 Mar '19, 15:53)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-68469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68469-form-container" class="comment-form-container">
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

<span id="68475"></span>

<div id="answer-container-68475" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68475-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There appear to be varied opinions on this.</p>
<h3 id="on-node-merging">On node merging:</h3>
<p>Some think landuse that goes up to a road should share geometry with the road (or path).</p>
<p>Others think that the landuse should end where the use actually physically stops (some distance form the road centreline). Some who support this have <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/landuse%3Dhighway">proposed landuse=highway</a> to eliminate the "gaps" visible at high zooms. This would be similar to <a href="https://wiki.openstreetmap.org/wiki/Rivers">river tagging</a> which has a logical 'way' and a series of areas for extents.</p>
<p>Personally, I find it far easier to edit the map when the nodes aren't merged.</p>
<h3 id="on-splitting">On Splitting:</h3>
<p>For your numbered items I tend to prefer 2 as I tend to think that e.g. residential roads go through residential areas rather than dividing them. If the areas on each side of a road have different names (or other properties) I would expect them to be split, but otherwise be continuous. I would also say that a major road can go through a residential area, but again opinions differ on all of this.</p>
<p>A final thing to note is that if local mappers in your area seem to have settled on one way of doing things, it is probably best to engage with them before introducing any sweeping changes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '19, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-68475" class="comments-container">
<span id="68476"></span>
<div id="comment-68476" class="comment">
<div id="post-68476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>These might also be useful:</p>
<ul>
<li><a href="/questions/6508/mapping-landuse-residential-and-overlapping-it-by-other-landuse-on-smaller-areas-in-towns">Mapping landuse residential and overlapping it by other landuse (on smaller areas in towns)</a></li>
<li><a href="/questions/18495/is-it-okay-if-landuse-borders-share-nodes-with-streets-rivers">Is it okay if landuse borders share nodes with streets / rivers?</a></li>
<li><a href="/questions/5352/should-the-edges-of-landuse-or-boundary-areas-share-points-with-streets-that-form-their-borders">Should the edges of landuse= <em>or boundary=</em> areas share points with streets that form their borders?</a></li>
</ul>
</div>
<div id="comment-68476-info" class="comment-info">
<span class="comment-age">(25 Mar '19, 09:30)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="68495"></span>
<div id="comment-68495" class="comment">
<div id="post-68495-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>I think the majority would be in favour of NOT having landuses extend up to the highway (or waterway) centre line. I wouldn't obsess about "not having filled in all the landuse".</p>
</div>
<div id="comment-68495-info" class="comment-info">
<span class="comment-age">(25 Mar '19, 19:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68475-form-container" class="comment-form-container">
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

