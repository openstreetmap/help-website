+++
type = "question"
title = "Carports layer=1 or footpaths: covered=yes"
description = '''There are two methods of doing a pathway/sidewalk. Mark the building on top of it layer=1. Or, break the sidewalk/pathway and for the sidewalk/pathway under it mark covered=yes. Which one is preferable?'''
date = "2022-09-11T17:20:00Z"
lastmod = "2022-09-11T21:03:00Z"
weight = 85602
keywords = [ "sidewalk", "pathways" ]
aliases = [ "/questions/85602" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Carports layer=1 or footpaths: covered=yes](/questions/85602/carports-layer1-or-footpaths-coveredyes)

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
<span id="post-85602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85602-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are two methods of doing a pathway/sidewalk. Mark the building on top of it <code>layer=1</code>. Or, break the sidewalk/pathway and for the sidewalk/pathway under it mark <a href="https://wiki.openstreetmap.org/wiki/Tag:covered%3Dyes"><code>covered=yes</code></a>. Which one is preferable?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sidewalk" rel="tag" title="see questions tagged &#39;sidewalk&#39;">sidewalk</span> <span class="post-tag tag-link-pathways" rel="tag" title="see questions tagged &#39;pathways&#39;">pathways</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '22, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/605442f85418d858e2ce1e1aea2092bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Evan%20Carroll&#39;s gravatar image" />
<p><span>Evan Carroll</span><br />
<span class="score" title="43 reputation points">43</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Evan Carroll has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '22, 17:24</strong> </span></p>
</div>
</div>
<div id="comments-container-85602" class="comments-container">
&#10;</div>
<div id="comment-tools-85602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85602-form-container" class="comment-form-container">
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

<span id="85604"></span>

<div id="answer-container-85604" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85604-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the way to think about this is how people might consume the data.</p>
<p>A hiking or pedestrian routing app is unlikely to pull down details of all the buildings and then try &amp; work out which paths are covered or obstructed by buildings (it's not unusual for buildings to obstruct paths on OSM even through in reality they don't). Splitting the path and adding covered=yes (or tunnel=building_passage if something more substantial than a roof canopy) is much more likely to be picked up by data consumers.</p>
<p>You still need to map the building appropriately (because other consumers will be more interested in that aspect of OSM): take a looks at whether people typically add layer tags to building=roof or building=car_port.</p>
<p>Making implicit information explicit through adding more tags is rarely a bad thing (sometimes it can be an impediment if the tagging needs to change), and is probably a longstanding trend on OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '22, 21:03</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-85604" class="comments-container">
&#10;</div>
<div id="comment-tools-85604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85604-form-container" class="comment-form-container">
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

