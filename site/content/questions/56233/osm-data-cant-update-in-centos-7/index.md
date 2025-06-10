+++
type = "question"
title = "[closed] OSM data cant update in centOS 7"
description = '''Hi, We setup osm database server in centos 7.  But we cant update data in that server. Below query is running long time while trigger update. (I thing reading data is very slow or cant read) COPY planet_osm_polygon (osm_id,access,addr:housename,addr:housenumber,addr:interpolation,admin_level,aerialw...'''
date = "2017-05-19T08:23:00Z"
lastmod = "2017-05-19T09:18:00Z"
weight = 56233
keywords = [ "tiles", "slow", "postgresql", "update", "centos" ]
aliases = [ "/questions/56233" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] OSM data cant update in centOS 7](/questions/56233/osm-data-cant-update-in-centos-7)

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
<span id="post-56233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56233-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>We setup osm database server in centos 7.</p>
<p>But we cant update data in that server. Below query is running long time while trigger update. (I thing reading data is very slow or cant read)</p>
<pre><code>COPY planet_osm_polygon (osm_id,access,addr:housename,addr:housenumber,addr:interpolation,admin_level,aerialway,aeroway,amenity,area,barrier,bicycle,brand,bridge,boundary,building,
construction,covered,culvert,cutting,denomination,disused,embankment,foot,generator:source,harbour,highway,historic,horse,intermittent,junction,landuse,layer,
leisure,lock,man_made,military,motorcar,name,natural,office,oneway,operator,place,population,power,power_source,public_transport,railway,ref,religion,
route,service,shop,sport,surface,toll,tourism,tower:type,tracktype,tunnel,water,waterway,wetland,width,wood,z_order,way_area,tags,way) FROM STDIN)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '17, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>20 Jun '17, 07:42</strong> </span></p>
</div>
</div>
<div id="comments-container-56233" class="comments-container">
<span id="56235"></span>
<div id="comment-56235" class="comment">
<div id="post-56235-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need to provide more detail on what you are actually doing, including</p>
<ul>
<li><p>hardware configuration that you are using</p></li>
<li><p>how much OSM data you imported country? region? the planet?</p></li>
<li><p>are you on the initial import or are you trying to update already imported data?</p></li>
</ul>
</div>
<div id="comment-56235-info" class="comment-info">
<span class="comment-age">(19 May '17, 08:49)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="56236"></span>
<div id="comment-56236" class="comment">
<div id="post-56236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>: Thanks for your interest. My system config are: 32 core CPU, 128GB RAM &amp; 2TB HD in centos 7. Already imported OSM data for whole country. This issue occurring while update only.</p>
</div>
<div id="comment-56236-info" class="comment-info">
<span class="comment-age">(19 May '17, 09:07)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="56237"></span>
<div id="comment-56237" class="comment">
<div id="post-56237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"OSM data for whole country" - is this Vatican City, Monaco or maybe the US?</p>
</div>
<div id="comment-56237-info" class="comment-info">
<span class="comment-age">(19 May '17, 09:12)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56238"></span>
<div id="comment-56238" class="comment">
<div id="post-56238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, its for whole planet.</p>
</div>
<div id="comment-56238-info" class="comment-info">
<span class="comment-age">(19 May '17, 09:18)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-56233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56233-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Problem is not reproducible or outdated" by Rajavelu_M 20 Jun '17, 07:42

</div>

</div>

</div>

