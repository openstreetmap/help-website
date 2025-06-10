+++
type = "question"
title = "Finding country Bbox from Nominatim Database"
description = '''I have a Nominatim database with UK data being stored. I grabbed the data from Geofabrik and installed Nominatim alongside the data import as per the Nominatim documentation. Is there any way, from the dataset I currently have, to find the bounding box? I&#x27;ve read threads such as https://help.openstr...'''
date = "2016-10-13T08:13:00Z"
lastmod = "2016-10-13T08:38:00Z"
weight = 52518
keywords = [ "nominatim", "bbox" ]
aliases = [ "/questions/52518" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Finding country Bbox from Nominatim Database](/questions/52518/finding-country-bbox-from-nominatim-database)

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
<span id="post-52518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52518-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a Nominatim database with UK data being stored. I grabbed the data from Geofabrik and installed Nominatim alongside the data import as per the Nominatim documentation.</p>
<p>Is there any way, from the dataset I currently have, to find the bounding box? I've read threads such as <a href="https://help.openstreetmap.org/questions/36323/how-to-export-country-bounding-boxes">https://help.openstreetmap.org/questions/36323/how-to-export-country-bounding-boxes</a> but I'm concerned that the bounding boxes generated from external websites may not reflect my database accurately, which would cause logic error further along down the line with my code</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '16, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-52518" class="comments-container">
&#10;</div>
<div id="comment-tools-52518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52518-form-container" class="comment-form-container">
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

<span id="52520"></span>

<div id="answer-container-52520" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52520-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Solved this, I downloaded the .poly files (didn't see them before, probably should have checked!) which provides an Osmosis bounding box for the dataset. I then loaded them into <a href="http://GeoJSON.io">GeoJSON.io</a> which provided the BBox coordinates.</p>
<p>This approach will only work if you're using Geofabrik's Osm.Pbf format (which most will be).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '16, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-52520" class="comments-container">
&#10;</div>
<div id="comment-tools-52520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52520-form-container" class="comment-form-container">
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

