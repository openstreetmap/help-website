+++
type = "question"
title = "How to get the administrative region (admin_level=4) a place belongs to?"
description = '''I&#x27;m using PyOsmium. Given a node on OpenStreetMap, for example a village or a city like Chicago, how should I derive information such as the admin_level=4 region it is located in (in this case Illinois), and the country it belongs to (the USA)? In addition to it, I would also like to derive informat...'''
date = "2021-07-27T12:40:00Z"
lastmod = "2021-08-26T09:54:00Z"
weight = 81089
keywords = [ "openstreetmap", "tags", "relations", "pyosmium" ]
aliases = [ "/questions/81089" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the administrative region (admin_level=4) a place belongs to?](/questions/81089/how-to-get-the-administrative-region-admin_level4-a-place-belongs-to)

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
<span id="post-81089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81089-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using PyOsmium. Given a node on OpenStreetMap, for example a village or a city like <a href="https://www.openstreetmap.org/node/153388690">Chicago</a>, how should I derive information such as the <code>admin_level=4</code> region it is located in (in this case Illinois), and the country it belongs to (the USA)? In addition to it, I would also like to derive information on the country (in this example, the USA).</p>
<p>This probably involves using <code>ref</code>s and relations, but I don't quite know what strategy I should use to get this information (as efficiently as possible). Can you help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-pyosmium" rel="tag" title="see questions tagged &#39;pyosmium&#39;">pyosmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '21, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/d089777d2df0dd15dd795f6f274255fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fsaler&#39;s gravatar image" />
<p><span>fsaler</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fsaler has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81089" class="comments-container">
&#10;</div>
<div id="comment-tools-81089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81089-form-container" class="comment-form-container">
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

<span id="81090"></span>

<div id="answer-container-81090" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81090-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will save yourself a lot of trouble if you can afford to run a local "Nominatim" installation and then simply use Nominatim's reverse geocoding ability. Alternatively, try "Photon" for the same purpose; there are ready-to-go Photon data dumps available for download, obviating the need for a database and an import process.</p>
<p>Otherwise, the likely easiest path is to pre-filter a planet file with the command-line osmium utility (only keep stuff tagged boundary=administrative and with an admin_level of interest to you), then load the entirety of that file into Pyosmium, construct geometries, use the Pyosmium/Shapely interoperability to stuff the geometries into a Shapely R-Tree. Once that is done, you can efficiently query which administrative bounding boxes a point is in; if this yields more than one result (eg half the points in New Mexico are also in the Texas bounding box), you need to do proper (and more costly) point-in-polygon checks for the resulting polygons but that is also easy with Shapely.</p>
<p>A third option is to do essentially what I wrote above but employ a PostGIS database to do it, i.e. load admin boundaries into PostGIS with osm2pgsql, then run SQL queries to find which polygons a point is in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '21, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '21, 17:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span></p>
</div>
</div>
<div id="comments-container-81090" class="comments-container">
<span id="81497"></span>
<div id="comment-81497" class="comment">
<div id="post-81497-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm going to try the Photon route, it sounds smartest. Where can I find the data dumps you mention? I need one for the whole planet, but I don't need data on ways or most kinds of features, only inhabited places (hamlet or bigger).</p>
</div>
<div id="comment-81497-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 09:54)</span> <span class="comment-user userinfo">fsaler</span>
</div>
</div>
</div>
<div id="comment-tools-81090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81090-form-container" class="comment-form-container">
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

