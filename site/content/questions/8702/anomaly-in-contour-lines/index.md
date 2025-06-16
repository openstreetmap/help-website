+++
type = "question"
title = "Anomaly in contour lines"
description = '''Hello, When I make contour lines of mountainous areas, I get some anomalies in the contour lines. At places where the lines are very close, I get polygons. In attachment [1] you will find such a .osm-file. What is the reason of this anomaly, and how can I solve it? I make contour lines with srtm2osm...'''
date = "2011-10-30T12:17:00Z"
lastmod = "2011-11-01T11:31:00Z"
weight = 8702
keywords = [ "anomaly", "contours" ]
aliases = [ "/questions/8702" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Anomaly in contour lines](/questions/8702/anomaly-in-contour-lines)

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
<span id="post-8702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8702-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="/upfiles/Contour_lines.png" alt="alt text" />Hello,</p>
<p>When I make contour lines of mountainous areas, I get some anomalies in the contour lines. At places where the lines are very close, I get polygons. In attachment [1] you will find such a .osm-file.</p>
<p>What is the reason of this anomaly, and how can I solve it?</p>
<p>I make contour lines with srtm2osm (OS: Ubuntu 11.04). In order to make a .osm-file, I use following command (with variables): mono Srtm2Osm.exe -bounds1 $ZL $WL $NL $OL -step $ele_mi -cat $ele_ma $ele_me</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-anomaly" rel="tag" title="see questions tagged &#39;anomaly&#39;">anomaly</span> <span class="post-tag tag-link-contours" rel="tag" title="see questions tagged &#39;contours&#39;">contours</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '11, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/9266d153beaa529de5fd8f40394c1d53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter&#39;s gravatar image" />
<p><span>Peter</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '11, 12:19</strong> </span></p>
</div>
</div>
<div id="comments-container-8702" class="comments-container">
&#10;</div>
<div id="comment-tools-8702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8702-form-container" class="comment-form-container">
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

<span id="8715"></span>

<div id="answer-container-8715" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8715-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These are "voids" in the SRTM data - areas where there are no heights recorded in the SRTM data source.</p>
<p>There are a few void-filling utilities available, or you can find pre-processed SRTM data that has the voids filled in. Please note that many popular sources of void-filled SRTM data, including CGIAR and Viewfinder Panorama, are distributed under licenses that are incompatible with the OSM license.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '11, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-8715" class="comments-container">
<span id="8735"></span>
<div id="comment-8735" class="comment">
<div id="post-8735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there any worldwide better-than-srtm source available that has a compatible license ? If so, it could really do with some promotion, because these "srtm bugs" come back way too often (especially since they happen at high altitudes, which is often the areas you're interested in when you're interested in terrain).</p>
</div>
<div id="comment-8735-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 11:31)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8715-form-container" class="comment-form-container">
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

