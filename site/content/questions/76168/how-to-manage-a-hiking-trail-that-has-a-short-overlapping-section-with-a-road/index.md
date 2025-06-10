+++
type = "question"
title = "How to manage a hiking trail that has a short overlapping section with a road?"
description = '''There is a hiking trail (highway=path) in Ontario (way=801771876) that is mostly through woods but has a short section that is on a road. You walk in the woods, come on to the road, walk a little ways, then step off back into the path in the woods.  What is the proper way to handle this? When I firs...'''
date = "2020-08-17T18:33:00Z"
lastmod = "2020-08-17T18:50:00Z"
weight = 76168
keywords = [ "path", "overlap" ]
aliases = [ "/questions/76168" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to manage a hiking trail that has a short overlapping section with a road?](/questions/76168/how-to-manage-a-hiking-trail-that-has-a-short-overlapping-section-with-a-road)

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
<span id="post-76168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76168-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a hiking trail (highway=path) in Ontario (<a href="https://www.openstreetmap.org/way/801771876">way=801771876</a>) that is mostly through woods but has a short section that is on a road. You walk in the woods, come on to the road, walk a little ways, then step off back into the path in the woods.</p>
<p>What is the proper way to handle this? When I first mapped it I just sort of put the path on top of the road. Should I have two new junctions, where the path meets the road, and mark that overlapping section to be both a road and path?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-overlap" rel="tag" title="see questions tagged &#39;overlap&#39;">overlap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '20, 18:33</strong></p>
<img src="https://secure.gravatar.com/avatar/8ee2f6d1715220cb57a0e662bd82cb4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wdenton&#39;s gravatar image" />
<p><span>wdenton</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wdenton has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76168" class="comments-container">
&#10;</div>
<div id="comment-tools-76168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76168-form-container" class="comment-form-container">
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

<span id="76169"></span>

<div id="answer-container-76169" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76169-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sign posted routes are mapped as route relations. Sounds complicated but a relation is just an ordered list of other OSM elements.</p>
<p>So the proper way to do this is to map infrastructure only once, then add the bits to the route relation and add the necessary tags to that (in this case probably just a name).</p>
<p>More information see <a href="https://wiki.openstreetmap.org/wiki/Relation:route#Walking_routes_.28also_hiking_and_pilgrimage.29">https://wiki.openstreetmap.org/wiki/Relation:route#Walking_routes_.28also_hiking_and_pilgrimage.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '20, 18:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '20, 18:51</strong> </span></p>
</div>
</div>
<div id="comments-container-76169" class="comments-container">
&#10;</div>
<div id="comment-tools-76169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76169-form-container" class="comment-form-container">
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

