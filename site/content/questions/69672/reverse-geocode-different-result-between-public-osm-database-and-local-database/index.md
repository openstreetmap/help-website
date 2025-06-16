+++
type = "question"
title = "Reverse geocode different result between public osm database and local database"
description = '''I have a problem with the result of reverse geocoding. I have created a local instance of openstreet with an Italy OSM database downloaded from geofabrik. The local instance daily updates the database. When I search an address with public request: https://nominatim.openstreetmap.org/reverse?format=x...'''
date = "2019-06-19T13:03:00Z"
lastmod = "2019-06-19T14:54:00Z"
weight = 69672
keywords = [ "geocode", "local" ]
aliases = [ "/questions/69672" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse geocode different result between public osm database and local database](/questions/69672/reverse-geocode-different-result-between-public-osm-database-and-local-database)

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
<span id="post-69672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69672-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a problem with the result of reverse geocoding. I have created a local instance of openstreet with an Italy OSM database downloaded from geofabrik. The local instance daily updates the database. When I search an address with public request:</p>
<p><a href="https://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=41.9189&amp;lon=12.52001&amp;zoom=18&amp;accept-language=it">https://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=41.9189&amp;lon=12.52001&amp;zoom=18&amp;accept-language=it</a></p>
<p>The result of road is: "Viale Ventuno Aprile"</p>
<p>But when I call my local instance with the same request the result of road is different. Why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocode" rel="tag" title="see questions tagged &#39;geocode&#39;">geocode</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '19, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/140f75303f0de1e13abf0713e9c5b2f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matteo&#39;s gravatar image" />
<p><span>Matteo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matteo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69672" class="comments-container">
<span id="69673"></span>
<div id="comment-69673" class="comment">
<div id="post-69673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please show / explain the difference.</p>
</div>
<div id="comment-69673-info" class="comment-info">
<span class="comment-age">(19 Jun '19, 13:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="69674"></span>
<div id="comment-69674" class="comment">
<div id="post-69674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Online instance:</p>
<p>&lt;reversegeocode timestamp="Wed, 19 Jun 19 13:52:27 +0000" attribution="Data © OpenStreetMap contributors, ODbL 1.0. &amp;lt;a href=" http:="" www.openstreetmap.org="" copyright""=""&gt;https://www.openstreetmap.org/copyright" querystring="format=xml&amp;lat=41.9189&amp;lon=12.52001&amp;zoom=18&amp;accept-language=it"&gt; &lt;result place_id="199361633" osm_type="relation" osm_id="5459681" ref="Q. V" lat="41.91649835" lon="12.5197118043497" boundingbox="41.9027733,41.930266,12.5013138,12.5325107"&gt; Quartiere V Nomentano, Viale Ventuno Aprile, San Lorenzo, Municipio Roma II, Roma, RM, LAZ, 00162, Italia &lt;/result&gt; &lt;addressparts&gt; &lt;address29&gt;Quartiere V Nomentano&lt;/address29&gt; &lt;road&gt;Viale Ventuno Aprile&lt;/road&gt; &lt;neighbourhood&gt;San Lorenzo&lt;/neighbourhood&gt; &lt;suburb&gt;Municipio Roma II&lt;/suburb&gt; &lt;city&gt;Roma&lt;/city&gt; &lt;county&gt;RM&lt;/county&gt; &lt;state&gt;LAZ&lt;/state&gt; &lt;postcode&gt;00162&lt;/postcode&gt; &lt;country&gt;Italia&lt;/country&gt; &lt;country_code&gt;it&lt;/country_code&gt; &lt;/addressparts&gt; &lt;/reversegeocode&gt;</p>
</div>
<div id="comment-69674-info" class="comment-info">
<span class="comment-age">(19 Jun '19, 14:53)</span> <span class="comment-user userinfo">Matteo</span>
</div>
</div>
<span id="69675"></span>
<div id="comment-69675" class="comment">
<div id="post-69675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Local instance:</p>
<p><a href="http://localhost/nominatim/reverse?format=xml&amp;lat=41.9189&amp;lon=12.52001&amp;zoom=18&amp;accept-language=it">http://localhost/nominatim/reverse?format=xml&amp;lat=41.9189&amp;lon=12.52001&amp;zoom=18&amp;accept-language=it</a></p>
<p>&lt;reversegeocode timestamp="Wed, 19 Jun 19 13:53:40 +0000" attribution="Data © OpenStreetMap contributors, ODbL 1.0. &amp;lt;a href=" http:="" www.openstreetmap.org="" copyright""=""&gt;https://www.openstreetmap.org/copyright" querystring="format=xml&amp;lat=41.9189&amp;lon=12.52001&amp;zoom=18&amp;accept-language=it"&gt; &lt;result place_id="7767144" osm_type="relation" osm_id="5459681" ref="Q. V" lat="41.91649835" lon="12.5197118043497" boundingbox="41.9027733,41.930266,12.5013138,12.5325107"&gt; Quartiere V Nomentano, Via Antonio Gallonio, San Lorenzo, Municipio Roma II, Roma, RM, LAZ, 00162, Italia &lt;/result&gt; &lt;addressparts&gt; &lt;address29&gt;Quartiere V Nomentano&lt;/address29&gt; &lt;road&gt;Via Antonio Gallonio&lt;/road&gt; &lt;neighbourhood&gt;San Lorenzo&lt;/neighbourhood&gt; &lt;suburb&gt;Municipio Roma II&lt;/suburb&gt; &lt;city&gt;Roma&lt;/city&gt; &lt;county&gt;RM&lt;/county&gt; &lt;state&gt;LAZ&lt;/state&gt; &lt;postcode&gt;00162&lt;/postcode&gt; &lt;country&gt;Italia&lt;/country&gt; &lt;country_code&gt;it&lt;/country_code&gt; &lt;/addressparts&gt; &lt;/reversegeocode&gt;</p>
</div>
<div id="comment-69675-info" class="comment-info">
<span class="comment-age">(19 Jun '19, 14:54)</span> <span class="comment-user userinfo">Matteo</span>
</div>
</div>
<span id="69676"></span>
<div id="comment-69676" class="comment">
<div id="post-69676-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See the &lt;road&gt; tag</p>
</div>
<div id="comment-69676-info" class="comment-info">
<span class="comment-age">(19 Jun '19, 14:54)</span> <span class="comment-user userinfo">Matteo</span>
</div>
</div>
</div>
<div id="comment-tools-69672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69672-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

