+++
type = "question"
title = "Getting way from OSM data"
description = '''I have imported osm data into PostgreSQL using this command osmosis --read-pbf bangladesh-latest.osm.pbf &#92;  --write-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot; &#92;  user=&quot;openstreetmap&quot; password=&quot;&quot; validateSchemaVersion=&quot;no&quot; Now how can i get all the ways of a city(or a bounding region).'''
date = "2018-03-31T15:20:00Z"
lastmod = "2018-05-11T02:53:00Z"
weight = 62875
keywords = [ "map", "pbf", "postgresql", "way" ]
aliases = [ "/questions/62875" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting way from OSM data](/questions/62875/getting-way-from-osm-data)

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
<span id="post-62875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62875-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have imported osm data into PostgreSQL using this command</p>
<p><code>osmosis --read-pbf bangladesh-latest.osm.pbf \ --write-apidb host="localhost" database="openstreetmap" \ user="openstreetmap" password="" validateSchemaVersion="no"</code></p>
<p>Now how can i get all the ways of a city(or a bounding region).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '18, 15:20</strong></p>
<img src="https://secure.gravatar.com/avatar/7da63bcb858ed2c1e1f25aa2d3d00106?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_partha&#39;s gravatar image" />
<p><span>_partha</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_partha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '18, 22:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62875" class="comments-container">
<span id="63416"></span>
<div id="comment-63416" class="comment">
<div id="post-63416-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>with postgis, you have just to intersect you box with the col way ( example : select * from planet_osm_way where "way" &amp;&amp; ST_SetSRID ('BOX3D(-11704037.77103247 4811252.308384717, -11660010.04274018 4855280.036677003)'::box3d, 3857) ; )</p>
</div>
<div id="comment-63416-info" class="comment-info">
<span class="comment-age">(11 May '18, 02:53)</span> <span class="comment-user userinfo">AntaC</span>
</div>
</div>
</div>
<div id="comment-tools-62875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62875-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

