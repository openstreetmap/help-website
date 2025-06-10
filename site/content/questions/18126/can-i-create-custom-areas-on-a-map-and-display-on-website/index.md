+++
type = "question"
title = "Can I create custom areas on a map and display on website"
description = '''Hi I would like to draw several areas on the map (which are not overlapping), preferrably in different colour each. Each area should have one central point (headquarter). It can be marked with marker. Website visitors can then see which area they are within and which central point they need to repor...'''
date = "2012-11-30T17:11:00Z"
lastmod = "2012-11-30T23:14:00Z"
weight = 18126
keywords = [ "areas", "custom" ]
aliases = [ "/questions/18126" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can I create custom areas on a map and display on website](/questions/18126/can-i-create-custom-areas-on-a-map-and-display-on-website)

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
<span id="post-18126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18126-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I would like to draw several areas on the map (which are not overlapping), preferrably in different colour each. Each area should have one central point (headquarter). It can be marked with marker. Website visitors can then see which area they are within and which central point they need to report. However, those areas are useful to the visitors of my web site only i.e. they are not county borders or anything similar worth marking permanently and sharing with general public (but no problem if needed to be). The map should be embedded on my web site. It should look something similar to this: <a href="http://goo.gl/maps/8B8A">link text</a> Is it possible to do it using OpenStreetMap, and what would be the best way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '12, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/44c54eb5201b6155b35964abf2456539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nik&#39;s gravatar image" />
<p><span>Nik</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18126" class="comments-container">
&#10;</div>
<div id="comment-tools-18126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18126-form-container" class="comment-form-container">
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

<span id="18128"></span>

<div id="answer-container-18128" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18128-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You would not technically be doing this "with OpenStreetMap". You would just display OpenStreetMap as your background layer (or, indeed, any other map), and use a suitable JavaScript library (OpenLayers or Leaflet) to display your polygons on top of that. That will require a little JavaScript coding but not much. You will also need a way to feed your polygons into the JavaScript - this can either happen through a static KML document that you amend with an editor each time a polygon is added or changed, or it could be with a database on some kind of server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '12, 18:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-18128" class="comments-container">
<span id="18130"></span>
<div id="comment-18130" class="comment">
<div id="post-18130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik, I hoped that there is some ready made solution, as I'm not a Java programmer, but I'll figure it out with the help of some friends.</p>
</div>
<div id="comment-18130-info" class="comment-info">
<span class="comment-age">(30 Nov '12, 23:14)</span> <span class="comment-user userinfo">Nik</span>
</div>
</div>
</div>
<div id="comment-tools-18128" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18128-form-container" class="comment-form-container">
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

