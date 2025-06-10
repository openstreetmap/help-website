+++
type = "question"
title = "[closed] How can I check if a marker is inside a KML Layer boundary ?"
description = '''Hello everbody, I&#x27;m new here. I would like to know, If is there a way to determine if a marker has entered an area covered by a KmlLayer. My .kml is mostly made up of some &amp;lt;polygons&amp;gt; with a bunch of coordinates that define the boundary.'''
date = "2014-02-12T06:59:00Z"
lastmod = "2014-02-12T10:20:00Z"
weight = 30668
keywords = [ "kml" ]
aliases = [ "/questions/30668" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How can I check if a marker is inside a KML Layer boundary ?](/questions/30668/how-can-i-check-if-a-marker-is-inside-a-kml-layer-boundary)

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
<span id="post-30668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30668-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everbody, I'm new here. I would like to know, If is there a way to determine if a marker has entered an area covered by a KmlLayer. My .kml is mostly made up of some &lt;polygons&gt; with a bunch of coordinates that define the boundary.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '14, 06:59</strong></p>
<img src="https://secure.gravatar.com/avatar/6a312ace25e0e46a57bb171332ff63a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Renan&#39;s gravatar image" />
<p><span>Renan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Renan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>12 Feb '14, 10:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-30668" class="comments-container">
<span id="30670"></span>
<div id="comment-30670" class="comment">
<div id="post-30670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does this relate to OpenStreetMap in some way? If not, you might be better asking somewhere more general like <a href="http://gis.stackexchange.com/">http://gis.stackexchange.com/</a> .</p>
</div>
<div id="comment-30670-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 09:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30668-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Frederik Ramm 12 Feb '14, 10:21

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30672"></span>

<div id="answer-container-30672" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30672-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not an OpenStreetMap related question. If you're using OpenLayers, check out <a href="http://dev.openlayers.org/docs/files/OpenLayers/Geometry/Polygon-js.html#OpenLayers.Geometry.Polygon.containsPoint">http://dev.openlayers.org/docs/files/OpenLayers/Geometry/Polygon-js.html#OpenLayers.Geometry.Polygon.containsPoint</a> - But this is not an OpenStreetMap related question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '14, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30672" class="comments-container">
&#10;</div>
<div id="comment-tools-30672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30672-form-container" class="comment-form-container">
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

