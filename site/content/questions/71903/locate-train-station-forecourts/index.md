+++
type = "question"
title = "Locate train station forecourts"
description = '''Hello. Is there a possibility to locate forecourts of train stations?'''
date = "2019-11-30T10:31:00Z"
lastmod = "2019-11-30T13:55:00Z"
weight = 71903
keywords = [ "station", "train", "openrailwaymap", "square" ]
aliases = [ "/questions/71903" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Locate train station forecourts](/questions/71903/locate-train-station-forecourts)

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
<span id="post-71903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71903-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. Is there a possibility to locate forecourts of train stations?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-station" rel="tag" title="see questions tagged &#39;station&#39;">station</span> <span class="post-tag tag-link-train" rel="tag" title="see questions tagged &#39;train&#39;">train</span> <span class="post-tag tag-link-openrailwaymap" rel="tag" title="see questions tagged &#39;openrailwaymap&#39;">openrailwaymap</span> <span class="post-tag tag-link-square" rel="tag" title="see questions tagged &#39;square&#39;">square</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '19, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/b26fe30ff3b0b67875f807c7ba7a5288?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blabsl&#39;s gravatar image" />
<p><span>Blabsl</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blabsl has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71903" class="comments-container">
&#10;</div>
<div id="comment-tools-71903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71903-form-container" class="comment-form-container">
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

<span id="71905"></span>

<div id="answer-container-71905" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71905-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Blabsl has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There does not seem to be any <a href="https://taginfo.openstreetmap.org/keys/railway#values">explicit tag</a> to delineate a station forecourt.</p>
<p>Station forecourts can be readily recognised by a person looking directly at OpenStreetMap, so, in principle, it should be possible to detect them. I've called this type of implicit feature in OSM 'emergent data' - other examples include urban areas, drainage basins, tree-lined streets etc.</p>
<p>Typical forecourts will be adjacent to the main entrance of the station and are likely to represent the area between that entrance and the nearest adjacent public road (i.e., excluding footways, cycleways, pedestrian areas and service roads). They are also likely to contain bus and/or tram stops, taxi ranks, bicycle parking, disabled parking or access, passenger drop-off points, information boards/maps etc.</p>
<p>Unfortunately not all the features needed to readily identify forecourts are mapped consistently. Ideally the main entrance would be mapped as a node of the station building or station area (although small stations without a building are unlikely to have a forecourt). In lieu one can find footways entering the station building, and define the points where they intersect the building as entrances but then one needs to identify the main entrance.</p>
<p>So <strong>in summary</strong>: at present finding them will require a fair amount of clever processing of OSM data.</p>
<p>You can also encourage the OSM community to map (or likely tag) more station entrances and perhaps suggest an explicit way of marking forecourts (try the tagging mailing list).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '19, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-71905" class="comments-container">
&#10;</div>
<div id="comment-tools-71905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71905-form-container" class="comment-form-container">
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

