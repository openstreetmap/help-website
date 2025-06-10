+++
type = "question"
title = "Bus Stops partially missing in zoom level 17"
description = '''i imported OSM data to PostgreSQL and drawing the map using TileMill. i notice bus_stop show less in zoom level 17 but showing all bus stops in level 18+, do anyone know how to fix this? /* labels.mss MapCSS*/ #planetosmpoint[amenity=&#x27;bus_station&#x27;][zoom&amp;gt;=10] { point-file: url(res/bus-15.png); } #...'''
date = "2012-10-20T10:03:00Z"
lastmod = "2012-10-20T10:16:00Z"
weight = 17043
keywords = [ "mapcss", "tilemill" ]
aliases = [ "/questions/17043" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bus Stops partially missing in zoom level 17](/questions/17043/bus-stops-partially-missing-in-zoom-level-17)

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
<span id="post-17043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17043-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i imported OSM data to PostgreSQL and drawing the map using TileMill. i notice bus_stop show less in zoom level 17 but showing all bus stops in level 18+, do anyone know how to fix this?</p>
<pre><code>/* labels.mss MapCSS*/
#planetosmpoint[amenity=&#39;bus_station&#39;][zoom&gt;=10] { point-file: url(res/bus-15.png); }
#planetosmpoint[highway=&#39;bus_stop&#39;][zoom&gt;=16] { point-file: url(res/bus-15.png); }</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapcss" rel="tag" title="see questions tagged &#39;mapcss&#39;">mapcss</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '12, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/1b3c34db49592fde43cc167e7f6dc186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Simon&#39;s gravatar image" />
<p><span>Simon</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Simon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '12, 10:04</strong> </span></p>
</div>
</div>
<div id="comments-container-17043" class="comments-container">
&#10;</div>
<div id="comment-tools-17043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17043-form-container" class="comment-form-container">
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

<span id="17044"></span>

<div id="answer-container-17044" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17044-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>solved ...</p>
<pre><code>#planetosmpoint[amenity=&#39;bus_station&#39;][zoom&gt;=10],#planetosmpoint[highway=&#39;bus_stop&#39;][zoom&gt;=16] { point-allow-overlap:true; }</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '12, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/1b3c34db49592fde43cc167e7f6dc186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Simon&#39;s gravatar image" />
<p><span>Simon</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Simon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '12, 11:57</strong> </span></p>
</div>
</div>
<div id="comments-container-17044" class="comments-container">
&#10;</div>
<div id="comment-tools-17044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17044-form-container" class="comment-form-container">
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

