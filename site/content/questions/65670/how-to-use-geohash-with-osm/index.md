+++
type = "question"
title = "How to use Geohash with OSM?"
description = '''OSM offer a simple and standard way to express a link to a map feature geometry, for example the Singapore&#x27;s Merlion Fountain is openstreetmap.org/way/182819157 ... So, how to do similar thing to a box represented by its w21z76281 ~5m×5m Geohash box at an OSM map? There are an OSM&#x27;s API that I can u...'''
date = "2018-09-01T11:39:00Z"
lastmod = "2018-09-01T12:57:00Z"
weight = 65670
keywords = [ "latlong" ]
aliases = [ "/questions/65670" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use Geohash with OSM?](/questions/65670/how-to-use-geohash-with-osm)

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
<span id="post-65670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65670-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OSM offer a simple and standard way to express a link to a map feature geometry, for example the <a href="https://www.wikidata.org/wiki/Q208760">Singapore's Merlion Fountain</a> is <a href="https://www.openstreetmap.org/way/182819157">openstreetmap.org/way/182819157</a> ... So, how to do similar thing to a box represented by its <code>w21z76281</code> ~5m×5m <strong>Geohash box at an OSM map</strong>? There are an OSM's API that I can use by HTTP GET?</p>
<p><img src="https://help.openstreetmap.org/upfiles/merlion01.png" alt="alt text" /></p>
<p>Geohash is a <a href="https://en.wikipedia.org/wiki/De_facto_standard"><em>de facto</em> standard</a> to enconde LatLong in only one (base32) number, accepted by PostGIS and many others, see <a href="https://postgis.net/docs/ST_GeoHash.html"><em>ST_GeoHash()</em> function</a>.</p>
<hr />
<p>PS1: the non-OSM <a href="http://geohash.org/w21z76281">geohash.org/w21z76281</a> is ugly (no zoom no box) and points to GoogleMap. As <a href="https://help.openstreetmap.org/users/10973/maxerickson"></a><a href="https://help.openstreetmap.org/users/10973/maxerickson">@Maxerickson</a></a> pointed, <a href="http://geohash.org/w21z76281?format=osm">geohash.org/w21z76281?format=osm</a> will be near it, but there are no box renderization, and it is a non-OSM's domain name (not really-open as <code>Wikidata.org</code> or open-and-reliable as <code>OSM.ORG</code> or <code>OpenStreetMap.org</code>).</p>
<p>PS2: there are something better to illustrate the resolution box, but also GoogleMap, <a href="https://www.movable-type.co.uk/scripts/geohash.html">movable-type.co.uk/scripts/geohash</a> you can see a box... with some work you can see changing to 9-characters and copy/paste "w21z76281".</p>
<hr />
<p><strong>Example</strong> of GoogleMap's renderization,<br />
<img src="https://help.openstreetmap.org/upfiles/merlion02_74Q5qV0.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latlong" rel="tag" title="see questions tagged &#39;latlong&#39;">latlong</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '18, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '18, 13:23</strong> </span></p>
</div>
</div>
<div id="comments-container-65670" class="comments-container">
&#10;</div>
<div id="comment-tools-65670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65670-form-container" class="comment-form-container">
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

<span id="65671"></span>

<div id="answer-container-65671" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On their <a href="http://geohash.org/site/tips.html">tips and tricks</a> page they show how to redirect to osm:</p>
<p><a href="http://geohash.org/w21z76281?format=osm">http://geohash.org/w21z76281?format=osm</a></p>
<p>For more geohash features on the openstreetmap.org website, the likely answer is that you would have to implement it and then advocate for it's inclusion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '18, 11:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</img>
</div>
</div>
<div id="comments-container-65671" class="comments-container">
<span id="65673"></span>
<div id="comment-65673" class="comment">
<div id="post-65673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/10973/maxerickson"></a><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a>, it is a "blind link", with no box, no "resolution clues" about the Geohash of the link. There are something similar to the cited <a href="https://www.movable-type.co.uk/scripts/geohash.html">movable-type.co.uk/scripts/geohash</a> with some e box renderization? And some that is OSM.ORG or Wikidata.org or OpenStreetMap.org (... domain that is really open and reliable)</p>
</div>
<div id="comment-65673-info" class="comment-info">
<span class="comment-age">(01 Sep '18, 12:57)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-65671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65671-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

