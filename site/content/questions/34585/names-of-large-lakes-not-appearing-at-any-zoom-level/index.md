+++
type = "question"
title = "Names of large lakes not appearing at any zoom level"
description = '''Zooming in and out over various large lakes in Italy, I either never see a lake name (eg Lake Garda), or it makes a brief appearance only if one zooms into the centre of the lake (eg Lake Bolsena) so that no shorelines can be seen. It would be nice for the lake name to appear when looking at shoreli...'''
date = "2014-07-03T10:32:00Z"
lastmod = "2014-07-04T13:10:00Z"
weight = 34585
keywords = [ "zoom", "lake", "name" ]
aliases = [ "/questions/34585" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Names of large lakes not appearing at any zoom level](/questions/34585/names-of-large-lakes-not-appearing-at-any-zoom-level)

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
<span id="post-34585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34585-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-34585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Zooming in and out over various large lakes in Italy, I either never see a lake name (eg Lake Garda), or it makes a brief appearance only if one zooms into the centre of the lake (eg Lake Bolsena) so that no shorelines can be seen. It would be nice for the lake name to appear when looking at shoreline (towns etc) if the view includes enough water.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '14, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c6b4c0ba6a099eb97b5e75576b911864?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Duffy&#39;s gravatar image" />
<p><span>David Duffy</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Duffy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34585" class="comments-container">
&#10;</div>
<div id="comment-tools-34585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34585-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="34597"></span>

<div id="answer-container-34597" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34597-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM is just a database and many different maps and services are made of it. Maps are generated based on OSM data and map style which is set of rules describing how data will be displayed. And creating a map style that reflects lots of conflicting requirements is hard.</p>
<p>Unfortunately, because there are an infinite number of possible tags, every feature can't be displayed and still have the map look legible, so not every "please can the standard map render X" request can be accommodated. So as result only small but the most important part of the data is used in generating map.</p>
<p>Obviously, sometimes authors of the map style missed some important tags, there is a beter way to do things that was missed or nobody had time to improve/update map style.</p>
<p>The stylesheet used by the "standard" style on OpenStreetMap.org is here: <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> In case of reasonable ideas (like this one) it is possible to make change to map style (it is quite easy but not trivial) and propose including it. It is also possible to (after checking whatever it was not already suggested) request it at <a href="https://github.com/gravitystorm/openstreetmap-carto/issues">https://github.com/gravitystorm/openstreetmap-carto/issues</a> and wait till somebody else will do the necessary work.</p>
<p>(based on answer to <a href="/questions/30019/plant_nursery-not-rendered-on-the-map">https://help.openstreetmap.org/questions/30019/plant_nursery-not-rendered-on-the-map</a> )</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '14, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/220a7c896723cbc2b5d57a1bfd5d66f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mateusz%20Konieczny&#39;s gravatar image" />
<p><span>Mateusz Koni...</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mateusz Konieczny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '14, 17:02</strong> </span></p>
</div>
</div>
<div id="comments-container-34597" class="comments-container">
<span id="34599"></span>
<div id="comment-34599" class="comment">
<div id="post-34599-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Interestingly <a href="https://www.openstreetmap.org/#map=15/51.2640/14.5733">some lakes</a> are rendered. But the humanitarian layer seems to be the only one which <a href="https://www.openstreetmap.org/#map=12/45.6478/10.6801&amp;layers=H">renders Lake Garda</a> and other lakes. I can't find any pattern. Maybe its just because the humanitarian layer is less cluttered or has different priorities? However it seems worth to create a ticket for this because lakes are important map features.</p>
</div>
<div id="comment-34599-info" class="comment-info">
<span class="comment-age">(03 Jul '14, 17:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="34602"></span>
<div id="comment-34602" class="comment">
<div id="post-34602-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It seems that according to <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/7c56d82c62855960899ef9d342988d7e161b1f23/amenity-points.mss#L578">https://github.com/gravitystorm/openstreetmap-carto/blob/7c56d82c62855960899ef9d342988d7e161b1f23/amenity-points.mss#L578</a> labels on natural=water will be rendered from zoom level 15 on default layer. Humanitarian layer is smarter and labels may be rendered from z10, depending on area - see <a href="https://github.com/hotosm/HDM-CartoCSS/blob/c101c2c20777e9653001fc4a5c60adaaed57773a/labels.mss#L416">https://github.com/hotosm/HDM-CartoCSS/blob/c101c2c20777e9653001fc4a5c60adaaed57773a/labels.mss#L416</a></p>
</div>
<div id="comment-34602-info" class="comment-info">
<span class="comment-age">(03 Jul '14, 17:36)</span> <span class="comment-user userinfo">Mateusz Koni...</span>
</div>
</div>
<span id="34625"></span>
<div id="comment-34625" class="comment">
<div id="post-34625-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>see <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/700">https://github.com/gravitystorm/openstreetmap-carto/issues/700</a> on this topic (created by David-Duffy)</p>
</div>
<div id="comment-34625-info" class="comment-info">
<span class="comment-age">(04 Jul '14, 04:58)</span> <span class="comment-user userinfo">Mateusz Koni...</span>
</div>
</div>
</div>
<div id="comment-tools-34597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34597-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34587"></span>

<div id="answer-container-34587" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I looked at the tags with Potlatch2. Garda as a polygon and the Italian name for it. Bolsena as a polygon and it's names in lots of languages BUT neither as a lake tag or an English name. They do turn up in a map search. I am not quite sure whats going on so I won't edit it. I noticed one polygon was last worked on three month ago.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '14, 12:41</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
</div>
<div id="comments-container-34587" class="comments-container">
<span id="34591"></span>
<div id="comment-34591" class="comment">
<div id="post-34591-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, it's a general behaviour - I just picked those two out as motivating examples. I get the same problems with the US Great Lakes, or Oneida Lake (near Syracuse NY) which is only labelled as "New York Barge Canal" on the standard view when the scale reads "1 km", but not when zoomed further out. This polygon is tagged "Lake" with the correct name "Oneida Lake", which is how Bing's view labels it when zoomed further out viewed in iD.</p>
<p>For smaller bodies of water it is not a problem (the label appears at an appropriate level of zoom), but with these larger ones it is slightly frustrating in terms of orienting oneself...I have no idea how much work it would be add this in, as g*e and Bing do.</p>
</div>
<div id="comment-34591-info" class="comment-info">
<span class="comment-age">(03 Jul '14, 14:14)</span> <span class="comment-user userinfo">David Duffy</span>
</div>
</div>
<span id="34598"></span>
<div id="comment-34598" class="comment">
<div id="post-34598-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@andy mackey</span> <a href="https://www.openstreetmap.org/relation/8569">The lake</a> <em>has</em> a lake tag. It is tagged as <em>natural=water</em>, <em>water=lake</em> and the last change has been 11 days ago. You probably looked at the wrong object.</p>
</div>
<div id="comment-34598-info" class="comment-info">
<span class="comment-age">(03 Jul '14, 17:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="34639"></span>
<div id="comment-34639" class="comment">
<div id="post-34639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK Tks. perhaps I looked one of the bank relations which was that old and didn't have lake tag. Doing a nominatim search did show water and lake tags when I looked at that.</p>
</div>
<div id="comment-34639-info" class="comment-info">
<span class="comment-age">(04 Jul '14, 13:10)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-34587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34587-form-container" class="comment-form-container">
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

