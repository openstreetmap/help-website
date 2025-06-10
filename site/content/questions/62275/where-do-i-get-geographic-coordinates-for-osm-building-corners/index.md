+++
type = "question"
title = "Where do I get geographic coordinates for OSM building Corners"
description = '''I am very new to OSM. I am working on a computer vision project to segment buildings using Aerial images. I am looking for data that has the geographic coordinates of building corners. I cam e across JOSM to label building, but not sure how to extract the data. I&#x27;d be glad if someone could point me ...'''
date = "2018-02-22T19:08:00Z"
lastmod = "2018-02-22T19:41:00Z"
weight = 62275
keywords = [ "building", "corner", "bounding-polygon", "geojson", "josm" ]
aliases = [ "/questions/62275" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where do I get geographic coordinates for OSM building Corners](/questions/62275/where-do-i-get-geographic-coordinates-for-osm-building-corners)

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
<span id="post-62275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62275-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am very new to OSM. I am working on a computer vision project to segment buildings using Aerial images. I am looking for data that has the geographic coordinates of building corners. I cam e across JOSM to label building, but not sure how to extract the data. I'd be glad if someone could point me to the right direction to get the data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-corner" rel="tag" title="see questions tagged &#39;corner&#39;">corner</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '18, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/9912c69eb28c9483cbfcbece4cda1d81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sam1107&#39;s gravatar image" />
<p><span>sam1107</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sam1107 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62275" class="comments-container">
&#10;</div>
<div id="comment-tools-62275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62275-form-container" class="comment-form-container">
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

<span id="62276"></span>

<div id="answer-container-62276" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62276-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Read <a href="https://wiki.openstreetmap.org/wiki/Elements">https://wiki.openstreetmap.org/wiki/Elements</a> and <a href="https://wiki.openstreetmap.org/wiki/Key:building">https://wiki.openstreetmap.org/wiki/Key:building</a></p>
<p>If a (closed) way is tagged as building, then the way's nodes are the building corners. Each node has coordinates.</p>
<p>If a relation is tagged as building it is more complicated - see <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">https://wiki.openstreetmap.org/wiki/Relation:multipolygon</a> , but 99% of all buildings are simply closed ways, so I think for the start you can ignore relations.</p>
<p>And for really getting filtered data <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">https://wiki.openstreetmap.org/wiki/Overpass_turbo</a> is your friend (use its wizard for the start).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '18, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '18, 19:43</strong> </span></p>
</div>
</div>
<div id="comments-container-62276" class="comments-container">
&#10;</div>
<div id="comment-tools-62276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62276-form-container" class="comment-form-container">
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

