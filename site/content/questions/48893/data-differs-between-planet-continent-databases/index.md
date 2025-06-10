+++
type = "question"
title = "data differs between planet &amp; continent Databases"
description = '''Hi to all, I have 2 different database setup first one contains planet data got from http://planet.osm.org/  and the second one contains NorthAmerica data got from http://download.geofabrik.de/  I got different geocode result from both database setup. For ex: q=9153 East Maple Lane Scottsdale 85255 ...'''
date = "2016-03-29T10:49:00Z"
lastmod = "2016-03-30T20:04:00Z"
weight = 48893
keywords = [ "openstreetmap", "planet", "nominatim", "osm", "geofabrik" ]
aliases = [ "/questions/48893" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [data differs between planet & continent Databases](/questions/48893/data-differs-between-planet-continent-databases)

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
<span id="post-48893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48893-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all,</p>
<p>I have 2 different database setup first one contains planet data got from <a href="http://planet.osm.org/">http://planet.osm.org/</a> and the second one contains NorthAmerica data got from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a></p>
<p>I got different geocode result from both database setup.</p>
<p>For ex: <strong>q=9153 East Maple Lane Scottsdale 85255</strong> gives empty data from planet DB, but got result from NorthAmerica DB.</p>
<p>Similarly I triggered geocode for 1000 address, and 150 results are differs between both DBs &amp; NorthAmerica setup give better results.</p>
<p>How it is possible ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '16, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '16, 17:16</strong> </span></p>
</div>
</div>
<div id="comments-container-48893" class="comments-container">
<span id="48907"></span>
<div id="comment-48907" class="comment">
<div id="post-48907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Some detailed examples would not hurt. Would guess some results may differ because there is something named similarly outside the North America also.</p>
</div>
<div id="comment-48907-info" class="comment-info">
<span class="comment-age">(29 Mar '16, 16:42)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="48914"></span>
<div id="comment-48914" class="comment">
<div id="post-48914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please report a bug in <a href="https://github.com/twain47/nominatim/issues">https://github.com/twain47/nominatim/issues</a> as something surely is off. Please include the location of East Maple Lane:</p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=293858094">http://nominatim.openstreetmap.org/details.php?place_id=293858094</a></p>
</div>
<div id="comment-48914-info" class="comment-info">
<span class="comment-age">(29 Mar '16, 18:25)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="48955"></span>
<div id="comment-48955" class="comment">
<div id="post-48955-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please see <a href="https://github.com/twain47/Nominatim/issues/419">https://github.com/twain47/Nominatim/issues/419</a></p>
</div>
<div id="comment-48955-info" class="comment-info">
<span class="comment-age">(30 Mar '16, 20:04)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
</div>
<div id="comment-tools-48893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48893-form-container" class="comment-form-container">
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

<span id="48954"></span>

<div id="answer-container-48954" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48954-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This can happen as a result of the continuous update process of the database. When the database on osm.org was originally imported, the relation that describes the boundary of Scottsdale was probably broken and so the road was assigned to a different city. Meanwhile that mistake has been fixed in the OSM database but not all addresses in the Nominatim database have been updated yet. Your own database used the newer OSM data and therefore got the address right.</p>
<p>I've now applied a forced update to the city of Scottsdale and all is well again on osm.org.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '16, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-48954" class="comments-container">
&#10;</div>
<div id="comment-tools-48954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48954-form-container" class="comment-form-container">
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

