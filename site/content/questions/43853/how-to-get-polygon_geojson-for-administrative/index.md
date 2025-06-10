+++
type = "question"
title = "how to get polygon_geojson for administrative"
description = '''Hi to all, I want to get geojson value for a region(city/state/country). I tried as http://nominatim.openstreetmap.org/search?q=chennai,India&amp;amp;polygon_geojson=1&amp;amp;format=json&amp;amp;limit=1 But it did not give geojson(return geojson for few regions only). If I remove limit, http://nominatim.openst...'''
date = "2015-06-30T08:22:00Z"
lastmod = "2015-06-30T10:30:00Z"
weight = 43853
keywords = [ "administrative", "search", "nominatim", "osm", "geojson" ]
aliases = [ "/questions/43853" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to get polygon_geojson for administrative](/questions/43853/how-to-get-polygon_geojson-for-administrative)

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
<span id="post-43853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43853-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all,</p>
<p>I want to get geojson value for a region(city/state/country). I tried as <a href="http://nominatim.openstreetmap.org/search?q=chennai,India&amp;polygon_geojson=1&amp;format=json&amp;limit=1">http://nominatim.openstreetmap.org/search?q=chennai,India&amp;polygon_geojson=1&amp;format=json&amp;limit=1</a> But it did not give geojson(return geojson for few regions only). If I remove limit, <a href="http://nominatim.openstreetmap.org/search?q=chennai,India&amp;polygon_geojson=1&amp;format=json">http://nominatim.openstreetmap.org/search?q=chennai,India&amp;polygon_geojson=1&amp;format=json</a> It will return multiple values, geojson also available for <strong>type = administrative</strong>. So Now i want to a single API for get geojson for a region with type=adminstrative. Any suggestions?</p>
<p>Thanks Rajavelu</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '15, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '15, 08:25</strong> </span></p>
</div>
</div>
<div id="comments-container-43853" class="comments-container">
&#10;</div>
<div id="comment-tools-43853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43853-form-container" class="comment-form-container">
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

<span id="43857"></span>

<div id="answer-container-43857" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43857-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For smallish areas use Overpass-Turbo. The client side code in Overpass-Turbo enables the queried OSM data to saved directly as geojson. Once the data gets too big you run into problems both with server-side timeouts (and potentially blocks), and/or client-side memory issues.</p>
<p><a href="http://overpass-turbo.eu/s/abF">This</a> is an example of a simple Overpass-Turbo query for admin units around Chennai. It can be refined by asking only for certain levels of admin units, and by using the area feature to restrict the request to a specific polygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '15, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-43857" class="comments-container">
&#10;</div>
<div id="comment-tools-43857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43857-form-container" class="comment-form-container">
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

