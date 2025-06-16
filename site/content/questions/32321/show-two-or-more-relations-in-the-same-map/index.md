+++
type = "question"
title = "Show two or more relations in the same map"
description = '''I&#x27;m trying to print maps to paste in the bus stops near my home, showing the routes of the buses stopping in those bus stops. Thus for each bus stop, I need to produce a map that shows several relations at the same time. I&#x27;d like to, for example, combine these two relations: http://www.openstreetmap...'''
date = "2014-04-12T15:46:00Z"
lastmod = "2014-04-12T21:47:00Z"
weight = 32321
keywords = [ "bus", "busroute", "relations", "busstops" ]
aliases = [ "/questions/32321" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Show two or more relations in the same map](/questions/32321/show-two-or-more-relations-in-the-same-map)

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
<span id="post-32321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32321-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to print maps to paste in the bus stops near my home, showing the routes of the buses stopping in those bus stops. Thus for each bus stop, I need to produce a map that shows several relations at the same time. I'd like to, for example, combine these two relations: <a href="https://www.openstreetmap.org/relation/370218#map=12/-34.6158/-58.4141">https://www.openstreetmap.org/relation/370218#map=12/-34.6158/-58.4141</a> <a href="https://www.openstreetmap.org/relation/370221#map=12/-34.6158/-58.4141">https://www.openstreetmap.org/relation/370221#map=12/-34.6158/-58.4141</a> and possibly others, into a single map.</p>
<p>I tried searching for "osm combine relations", "osm combine maps", "osm merge relations", etc, but couldn't find a way yet. The closest thing I found to an answer is <a href="/questions/2014/,">https://help.openstreetmap.org/questions/2014/,</a> but I'm not sure how to adapt it to my particular case. Can anyone help me out? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-busroute" rel="tag" title="see questions tagged &#39;busroute&#39;">busroute</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '14, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f601e56447b7874e8016c9cb4de1ce56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LFS&#39;s gravatar image" />
<p><span>LFS</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LFS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32321" class="comments-container">
&#10;</div>
<div id="comment-tools-32321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32321-form-container" class="comment-form-container">
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

<span id="32334"></span>

<div id="answer-container-32334" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32334-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-32334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LFS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are ready-made public transport maps like <a href="http://öpnvkarte.de/?zoom=14&amp;lat=-34.61294&amp;lon=-58.41101&amp;layers=TBTTT">öpnvkarte.de</a> an option? If not, you can create an <a href="http://overpass-turbo.eu/s/33j">Overpass query</a> that loads and displays these relations, or if you're unhappy with how they're displayed, export then through Overpass and load them into an OpenLayers or Leaflet map yourself (then you can control the styling).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '14, 21:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32334" class="comments-container">
&#10;</div>
<div id="comment-tools-32334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32334-form-container" class="comment-form-container">
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

