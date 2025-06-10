+++
type = "question"
title = "Can I reverse geocoding from my local OSM server?"
description = '''Hi, I installed a local osm tile server follows &quot;https://wiki.debian.org/OSM/tileserver/jessie&quot; instructions. So, I have a mapserver on &quot;http://localhost/osm_tiles/0/0/0.png&quot; site. I visualized my map with LeafletJS, it&#x27;s works fine. My question: if I positioning my map to a point (lat/long coordina...'''
date = "2016-03-24T07:11:00Z"
lastmod = "2016-03-25T07:15:00Z"
weight = 48806
keywords = [ "reversegeocoding" ]
aliases = [ "/questions/48806" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can I reverse geocoding from my local OSM server?](/questions/48806/can-i-reverse-geocoding-from-my-local-osm-server)

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
<span id="post-48806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48806-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I installed a local osm tile server follows "https://wiki.debian.org/OSM/tileserver/jessie" instructions.</p>
<p>So, I have a mapserver on "http://localhost/osm_tiles/0/0/0.png" site.</p>
<p>I visualized my map with LeafletJS, it's works fine.</p>
<p>My question: if I positioning my map to a point (lat/long coordinates) how I get this point local info (city name, street name etc...) ?</p>
<p>How do I reverse geocoding from my system? (I don't want to do it from outter source)</p>
<p>Thanks for your answers.</p>
<p>Ps.: sorry for my bad english...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '16, 07:11</strong></p>
<img src="https://secure.gravatar.com/avatar/84c5ab85a03a233efb2fa8b36b4df26b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leslie%20Gal&#39;s gravatar image" />
<p><span>Leslie Gal</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leslie Gal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48806" class="comments-container">
&#10;</div>
<div id="comment-tools-48806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48806-form-container" class="comment-form-container">
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

<span id="48807"></span>

<div id="answer-container-48807" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48807-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Leslie Gal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will have to set up a Nominatim server for address search and reverse geocoding. Check out <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">http://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> for detailed instructions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '16, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/2ab3f311e46e4ba07af9ad75d4a3dc31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jot&#39;s gravatar image" />
<p><span>jot</span><br />
<span class="score" title="511 reputation points">511</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jot has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '16, 08:14</strong> </span></p>
</div>
</div>
<div id="comments-container-48807" class="comments-container">
<span id="48841"></span>
<div id="comment-48841" class="comment">
<div id="post-48841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank for your answers Frederik and jot. Both answers is perfect for me. One-one green pipeline to you! Thanks again.</p>
</div>
<div id="comment-48841-info" class="comment-info">
<span class="comment-age">(25 Mar '16, 07:15)</span> <span class="comment-user userinfo">Leslie Gal</span>
</div>
</div>
</div>
<div id="comment-tools-48807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48807-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48809"></span>

<div id="answer-container-48809" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48809-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Installing your own Nominatim instance with a separate copy of the data is the best way to do it. However if you only use it occasionally and you don't mind a small performance penalty you can also hack together a few PostGIS queries that will give you the nearest street, city and so on from a normal rendering database, for example to find the nearest street to a point with the coordinates mylat,mylon you would do something like</p>
<pre><code>SELECT highway,name
FROM planet_osm_line
WHERE highway IS NOT NULL
AND ST_DWITHIN(way, ST_MAKEPOINT(mylon, mylat), 300)
ORDER BY ST_DISTANCE(way, ST_MAKEPOINT(mylon, mylat))
LIMIT 1</code></pre>
<p>or to find the city boundary that contains the point,</p>
<pre><code>SELECT name
FROM planet_osm_polygon
WHERE boundary=&#39;administrative&#39;
AND ST_CONTAINS(way, ST_MAKEPOINT(mylon, mylat))</code></pre>
<p>You might have to wrap the ST_MAKEPOINT in a ST_SETSRID(..., 3857) or ST_SETSRID(..., 900913) depending on your setup.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '16, 08:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48809" class="comments-container">
&#10;</div>
<div id="comment-tools-48809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48809-form-container" class="comment-form-container">
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

