+++
type = "question"
title = "OSM &amp; Memory Map compatibility"
description = '''All, good evening Does anyone successfully use maps from OSM in Memory Map? If so, would you be kind enough to confirm the export file type &amp;amp; what you used to stitch tiles together (if not MM) Thanks Foss'''
date = "2011-02-10T22:14:00Z"
lastmod = "2013-02-07T17:32:00Z"
weight = 2919
keywords = [ "map", "osm", "memory" ]
aliases = [ "/questions/2919" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [OSM & Memory Map compatibility](/questions/2919/osm-memory-map-compatibility)

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
<span id="post-2919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2919-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>All, good evening Does anyone successfully use maps from OSM in Memory Map? If so, would you be kind enough to confirm the export file type &amp; what you used to stitch tiles together (if not MM) Thanks</p>
<p>Foss</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '11, 22:14</strong></p>
<img src="https://secure.gravatar.com/avatar/462b30ee1ac28b107987c635a83555b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fossp&#39;s gravatar image" />
<p><span>fossp</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fossp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2919" class="comments-container">
&#10;</div>
<div id="comment-tools-2919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2919-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="2922"></span>

<div id="answer-container-2922" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2922-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It should be possible to generate suitable tiles for MemoryMap EuropeanEdition versions 5 and above using OSM data, but I have not succeeded. This is the version of the software which can be used with UK Ordnance Survey StreetView Tiles. I have successfully used the latter to create a 100km square pannable map. I then used mapnik to generate tiles of identical size and projection and copying the relevant world files from (.tgw, .tab) the OSSV tiles. I suspect that I was not using a suitable bitmap format, and I have not tried subsequently.</p>
<p>As I only tried the step of generating matching tiles in a given projection (OSGB36, EPSG 27700) I do not know if it is possible to do this with the Spherical Mercator used by OSM tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '11, 23:25</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-2922" class="comments-container">
<span id="2932"></span>
<div id="comment-2932" class="comment">
<div id="post-2932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>as SK53 says the europe edition accepts scanned and some picture formats, the OS V5 version does not. I hope someone as a way of solving this.their are other mapping software products UKGPS and OZexplorer do accept scans. but like you I'm used to Memory Map</p>
</div>
<div id="comment-2932-info" class="comment-info">
<span class="comment-age">(11 Feb '11, 01:30)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-2922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2922-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19701"></span>

<div id="answer-container-19701" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19701-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>here you are the solution for your problem <a href="http://www.bel-horizon.eu/la-cartographie/open-street-map/utilisons-les-cartes-osm-dans-memory-map.html">http://www.bel-horizon.eu/la-cartographie/open-street-map/utilisons-les-cartes-osm-dans-memory-map.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '13, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/7793d59cdb9085b174739fe60fd144d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bel-horizon&#39;s gravatar image" />
<p><span>bel-horizon</span><br />
<span class="score" title="14 reputation points">14</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bel-horizon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19701" class="comments-container">
&#10;</div>
<div id="comment-tools-19701" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19701-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2940"></span>

<div id="answer-container-2940" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2940-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I also would have liked to use OSM with Memory Map. I have found quite a good alternative.It is QUO aka Mapyx they allow free use of their mapping software and now as an alternative to them selling you Ordinance Survey Map data they have it set-up to display our OpenStreetMap and it will give us OS Grid reference and create routes and connect to a GPS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '11, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '11, 10:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span></p>
</div>
</div>
<div id="comments-container-2940" class="comments-container">
&#10;</div>
<div id="comment-tools-2940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2940-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19700"></span>

<div id="answer-container-19700" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19700-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://www.bel-horizon.eu/la-cartographie/open-street-map/utilisons-les-cartes-osm-dans-memory-map.html">http://www.bel-horizon.eu/la-cartographie/open-street-map/utilisons-les-cartes-osm-dans-memory-map.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '13, 17:30</strong></p>
<img src="https://secure.gravatar.com/avatar/7793d59cdb9085b174739fe60fd144d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bel-horizon&#39;s gravatar image" />
<p><span>bel-horizon</span><br />
<span class="score" title="14 reputation points">14</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bel-horizon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19700" class="comments-container">
&#10;</div>
<div id="comment-tools-19700" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19700-form-container" class="comment-form-container">
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

