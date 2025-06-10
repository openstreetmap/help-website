+++
type = "question"
title = "Miss aligned roads of Qinngorput Area with the aereal imagery"
description = '''Hi just wanted to ask, how to aligned roads in Greenland (City Nuuk) in Qinngorput Area. I notice the problem when using bing aerial imagery and DigitalGlobe Premium imagery, and the DigitalGlobe Standart Imagery, and last Mapbox Satellite imagery, all of the roads are miss-aligned with the aerial i...'''
date = "2019-02-12T18:29:00Z"
lastmod = "2019-02-12T20:33:00Z"
weight = 67985
keywords = [ "qinngorput", "nuuk" ]
aliases = [ "/questions/67985" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Miss aligned roads of Qinngorput Area with the aereal imagery](/questions/67985/miss-aligned-roads-of-qinngorput-area-with-the-aereal-imagery)

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
<span id="post-67985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67985-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>just wanted to ask, how to aligned roads in Greenland (City Nuuk) in Qinngorput Area.</p>
<p>I notice the problem when using bing aerial imagery and DigitalGlobe Premium imagery, and the DigitalGlobe Standart Imagery, and last Mapbox Satellite imagery, all of the roads are miss-aligned with the aerial imagery, how can we fix those?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qinngorput" rel="tag" title="see questions tagged &#39;qinngorput&#39;">qinngorput</span> <span class="post-tag tag-link-nuuk" rel="tag" title="see questions tagged &#39;nuuk&#39;">nuuk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '19, 18:29</strong></p>
<img src="https://secure.gravatar.com/avatar/59f6a3194e0341585c18fea47f9b153f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kristian%20Kuluk%20Frederiksen&#39;s gravatar image" />
<p><span>Kristian Kul...</span><br />
<span class="score" title="-9 reputation points">-9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kristian Kuluk Frederiksen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67985" class="comments-container">
&#10;</div>
<div id="comment-tools-67985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67985-form-container" class="comment-form-container">
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

<span id="67986"></span>

<div id="answer-container-67986" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67986-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Normally, GPS traces take precedence over imagery for alignment, especially in hilly/steep areas where the methods used to align imagery often don't work as well. While an individual GPS trace can be out significantly, multiple traces over multiple days usually average out to something pretty accurate.</p>
<p>The area you describe, actually shows <a href="https://www.openstreetmap.org/#map=16/64.1749/-51.6726&amp;layers=G">fairly decent alignment</a> to the publicly uploaded GPS traces, so I would suspect that most of the error here lies with the satellite overlays and not the OSM data. The <a href="https://www.strava.com/heatmap#14.70/-51.67375/64.17347/hot/all">Strava heatmap</a> seems to agree with OSM too.</p>
<p>Most editors have an option to shift background imagery including <a href="https://blog.mapbox.com/better-openstreetmap-data-with-ids-new-imagery-offset-tool-ff1906ef6c53">iD</a>, <a href="https://learnosm.org/en/josm/correcting-imagery-offset/">JOSM</a> and <a href="http://vespucci.io/help/en/Aligning%20background%20imagery/">Vespucci</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '19, 20:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-67986" class="comments-container">
&#10;</div>
<div id="comment-tools-67986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67986-form-container" class="comment-form-container">
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

