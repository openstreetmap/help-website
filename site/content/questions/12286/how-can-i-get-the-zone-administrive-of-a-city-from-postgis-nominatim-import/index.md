+++
type = "question"
title = "How can I get the zone administrive of a city from postgis (nominatim import)?"
description = '''I posted on stackoverflow before to find this website. so here is my my post.  http://stackoverflow.com/questions/10242129/how-can-i-get-the-zone-administrive-of-a-city-from-postgis-nominatim-import  I retreived europe.osm database with osm2pgsql. And now I try to exploit it. Is there a way to get t...'''
date = "2012-04-23T15:52:00Z"
lastmod = "2012-04-24T13:35:00Z"
weight = 12286
keywords = [ "nominatim", "osm2pgsql", "database" ]
aliases = [ "/questions/12286" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I get the zone administrive of a city from postgis (nominatim import)?](/questions/12286/how-can-i-get-the-zone-administrive-of-a-city-from-postgis-nominatim-import)

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
<span id="post-12286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12286-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I posted on stackoverflow before to find this website. so here is my my post.</p>
<p><a href="http://stackoverflow.com/questions/10242129/how-can-i-get-the-zone-administrive-of-a-city-from-postgis-nominatim-import">http://stackoverflow.com/questions/10242129/how-can-i-get-the-zone-administrive-of-a-city-from-postgis-nominatim-import</a><br />
</p>
<p>I retreived europe.osm database with osm2pgsql. And now I try to exploit it. Is there a way to get the state, country, region, from a way like a town hamlet locality or city?</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Nominatim">https://wiki.openstreetmap.org/wiki/Nominatim</a><br />
<a href="https://github.com/twain47/Nominatim">https://github.com/twain47/Nominatim</a><br />
</p>
<p>databases osm format :<br />
<a href="http://download.geofabrik.de/osm/europe/">http://download.geofabrik.de/osm/europe/</a><br />
here is the database schema :<br />
<a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/schema">https://wiki.openstreetmap.org/wiki/Osm2pgsql/schema</a></p>
<p><strong>if someone can provide me the SQL Query to retreive the information.</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '12, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/6c6458929c11785783ae7ca2e5bc3d56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christophe%20DEBOVE&#39;s gravatar image" />
<p><span>Christophe D...</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christophe DEBOVE has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '12, 08:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></br></p>
</div>
</div>
<div id="comments-container-12286" class="comments-container">
&#10;</div>
<div id="comment-tools-12286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12286-form-container" class="comment-form-container">
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

<span id="12312"></span>

<div id="answer-container-12312" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12312-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Christophe DEBOVE has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I presume you have a full Nominatim installation as described on the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">installation page</a> not just an osm2pgsql import.</p>
<p>Doing SQL queries on the database directly is a bit involved. You can get administrative information much easier by sending reverse requests directly to your local installation. If you have the OSM id of your way, send something like: <a href="http://your.local.nominatim.server/reverse?osm_type=W&amp;osm_id=%3Cosm"><code>http://your.local.nominatim.server/reverse?osm_type=W&amp;osm_id=&lt;osm</code></a><code> id&gt;</code> and process the XML returned.</p>
<p>If you still want to go down the SQL road, have a look at the <code>placex</code> and <code>place_addressline</code> tables. The former contains all OSM objects and the latter the relationship between them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '12, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '12, 10:34</strong> </span></p>
</div>
</div>
<div id="comments-container-12312" class="comments-container">
<span id="12315"></span>
<div id="comment-12315" class="comment">
<div id="post-12315-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks I didn't make the full nominatim install because I've allready a geo request system, I need just to make an import to my system.</p>
</div>
<div id="comment-12315-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 09:23)</span> <span class="comment-user userinfo">Christophe D...</span>
</div>
</div>
<span id="12316"></span>
<div id="comment-12316" class="comment">
<div id="post-12316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry but there is not place_addressline table</p>
</div>
<div id="comment-12316-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 10:22)</span> <span class="comment-user userinfo">Christophe D...</span>
</div>
</div>
<span id="12317"></span>
<div id="comment-12317" class="comment">
<div id="post-12317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <code>placex</code> and <code>place_addressline</code> tables are part of the full Nominatim import. If you don't want to do the full import, there is no point in importing the gazetteer schema in the first place.</p>
</div>
<div id="comment-12317-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 10:40)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="12331"></span>
<div id="comment-12331" class="comment">
<div id="post-12331-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok I will follow the full installation. Thx</p>
</div>
<div id="comment-12331-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 13:35)</span> <span class="comment-user userinfo">Christophe D...</span>
</div>
</div>
</div>
<div id="comment-tools-12312" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12312-form-container" class="comment-form-container">
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

