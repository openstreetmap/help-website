+++
type = "question"
title = "Reverse Geocoding Error"
description = '''First of all I am new to OpenStreetMap. I am using the following to reverse geocode a point http://nominatim.openstreetmap.org/reverse?format=xml&amp;amp;lat=40.35456&amp;amp;lon=-76.74331&amp;amp;zoom=18&amp;amp;addressdetails=1. The road (Linglestown Road), County (Dauphin), state (PA), and zip code (17112) retur...'''
date = "2014-02-24T18:08:00Z"
lastmod = "2014-02-24T19:20:00Z"
weight = 30976
keywords = [ "reversegeocoding" ]
aliases = [ "/questions/30976" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Reverse Geocoding Error](/questions/30976/reverse-geocoding-error)

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
<span id="post-30976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30976-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>First of all I am new to OpenStreetMap. I am using the following to reverse geocode a point <a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=40.35456&amp;lon=-76.74331&amp;zoom=18&amp;addressdetails=1.">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=40.35456&amp;lon=-76.74331&amp;zoom=18&amp;addressdetails=1.</a> The road (Linglestown Road), County (Dauphin), state (PA), and zip code (17112) returned are correct for the position, but the city returned is Holiday Park, PA which is in Allegheny County with a zip code of 15239 near Plum, PA (Pittsburg area)instead of Harrisburg, PA. Holiday Park (Longitude: -79.7092) is over 200 miles west of Harrisburg (Longitude: 76.74331 for the address). Is this a database error or what would cause the city to be incorrect? Thanks for any help with this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '14, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a34fdc7f9bd132ec582251630b6de6fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iTRAKDeveloper&#39;s gravatar image" />
<p><span>iTRAKDeveloper</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iTRAKDeveloper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30976" class="comments-container">
&#10;</div>
<div id="comment-tools-30976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30976-form-container" class="comment-form-container">
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

<span id="30977"></span>

<div id="answer-container-30977" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30977-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-30977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="iTRAKDeveloper has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This appears to be a data issue, although I should add that this does not necessarily mean that the data are incorrect. It does mean that Nominatim is behaving as expected with its given inputs.</p>
<p>According to OpenStreetMap there are two places coded as place=hamlet (probably incorrectly, many small areas of cities were so coded when GNIS data were imported) in PA. One is the one you refer to, Holiday Park, Allegheny Co, but the other is very close to your latlon reference in Dauphin Co.</p>
<p>There are the two relevant nodes, and their associated Nominatim info:</p>
<ul>
<li>Holiday Park, Allegheny Co: <a href="http://www.openstreetmap.org/node/158282935">OSM</a>, <a href="http://nominatim.openstreetmap.org/details.php?place_id=503343">Nominatim</a></li>
<li>Holiday Park, Dauphin Co: <a href="http://www.openstreetmap.org/node/158580514">OSM</a>, <a href="http://nominatim.openstreetmap.org/details.php?place_id=446712">Nominatim</a></li>
</ul>
<p>Many places in the US could do with better information regarding their relative status: in particular many places named hamlet would be better classified as suburbs, or neighbourhoods. In the main more information as to the bounds of the area a node refers to makes Nominatim's task easier.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '14, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-30977" class="comments-container">
&#10;</div>
<div id="comment-tools-30977" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30977-form-container" class="comment-form-container">
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

