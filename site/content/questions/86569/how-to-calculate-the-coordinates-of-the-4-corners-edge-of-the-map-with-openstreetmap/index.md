+++
type = "question"
title = "How to calculate the coordinates of the 4 corners (edge) of the map with OpenStreetMap?"
description = '''How to calculate the coordinates of the 4 corners (edge) of the map with OpenStreetMap? '''
date = "2023-01-27T08:58:00Z"
lastmod = "2023-01-27T10:10:00Z"
weight = 86569
keywords = [ "corner" ]
aliases = [ "/questions/86569" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to calculate the coordinates of the 4 corners (edge) of the map with OpenStreetMap?](/questions/86569/how-to-calculate-the-coordinates-of-the-4-corners-edge-of-the-map-with-openstreetmap)

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
<span id="post-86569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86569-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to calculate the coordinates of the 4 corners (edge) of the map with OpenStreetMap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-corner" rel="tag" title="see questions tagged &#39;corner&#39;">corner</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '23, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/77607f05001735bba22f6e2026906d56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sultanb&#39;s gravatar image" />
<p><span>Sultanb</span><br />
<span class="score" title="10 reputation points">10</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sultanb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86569" class="comments-container">
<span id="86570"></span>
<div id="comment-86570" class="comment">
<div id="post-86570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i need the 4 corner coordinates of the map to use as raster</p>
</div>
<div id="comment-86570-info" class="comment-info">
<span class="comment-age">(27 Jan '23, 09:00)</span> <span class="comment-user userinfo">Sultanb</span>
</div>
</div>
</div>
<div id="comment-tools-86569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86569-form-container" class="comment-form-container">
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

<span id="86571"></span>

<div id="answer-container-86571" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86571-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Set up your own Leaflet map (it's just a few lines of Javascript, see <a href="https://leafletjs.com/examples/quick-start/)">https://leafletjs.com/examples/quick-start/)</a> then use getBounds to retrieve the currently visible map extent: <a href="https://stackoverflow.com/questions/22948096/get-the-bounding-box-of-the-visible-leaflet-map">https://stackoverflow.com/questions/22948096/get-the-bounding-box-of-the-visible-leaflet-map</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '23, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-86571" class="comments-container">
<span id="86572"></span>
<div id="comment-86572" class="comment">
<div id="post-86572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can it be done for desktop application and with c#?</p>
</div>
<div id="comment-86572-info" class="comment-info">
<span class="comment-age">(27 Jan '23, 10:10)</span> <span class="comment-user userinfo">Sultanb</span>
</div>
</div>
</div>
<div id="comment-tools-86571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86571-form-container" class="comment-form-container">
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

