+++
type = "question"
title = "Database size of nonimatim vs osm2pgsql"
description = '''I am new to nominatim, and I was under the impression that nominatim uses osm2pgsql to import the data into a Postgresql/Postgis database.  However, I noticed there is a huge difference between the database size of a pure osm2pgsql imported map, and the same map imported by Nominatim.  A map of just...'''
date = "2017-03-05T13:19:00Z"
lastmod = "2017-03-05T23:00:00Z"
weight = 54916
keywords = [ "nominatim", "osm2pgsql" ]
aliases = [ "/questions/54916" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Database size of nonimatim vs osm2pgsql](/questions/54916/database-size-of-nonimatim-vs-osm2pgsql)

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
<span id="post-54916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54916-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to nominatim, and I was under the impression that nominatim uses osm2pgsql to import the data into a Postgresql/Postgis database.</p>
<p>However, I noticed there is a huge difference between the database size of a pure osm2pgsql imported map, and the same map imported by Nominatim.</p>
<p>A map of just 3.2Mb ends up in a database 80Mb with osm2pgsql. The same map ends up 265Mb when imported with Nominatim using setup.php --osm-file --osm2pgsql-cache 1024.</p>
<p>Why is nominatim creating so much extra data for the same thing? It is 3 times as much as pure osm2pgsql. I noticed the database tables are also quite different.</p>
<p>Is there a way to reduce this data size used by nominatim? Do I have something wrong?</p>
<p>I want to import the full planet OSM file, and I read that the full planet ends up taking like 800Gb. But with the ratio I got, it is going to end up taking 3Tb!</p>
<p>Would be good if someone could explain the difference and the relationship between the two, because it is not clear to me what is nominatim doing with osm2pgsql if the data structures are different.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '17, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/e01618347bd158e35c34cce5bc006a92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbx1&#39;s gravatar image" />
<p><span>jbx1</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbx1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54916" class="comments-container">
&#10;</div>
<div id="comment-tools-54916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54916-form-container" class="comment-form-container">
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

<span id="54930"></span>

<div id="answer-container-54930" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54930-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim uses a different configuration file (well runs contains C++ code, so it's more like a plugin, <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/output-gazetteer.cpp)">https://github.com/openstreetmap/osm2pgsql/blob/master/output-gazetteer.cpp)</a> when importing. It needs some map features and tags that are irrelevant for rendering e.g. postal code boundaries or the operator tag.</p>
<p>The first step to reduce the Nominatim data size is to import less data, e.g. is every country in the world needed? Next would be not importing the US TIGER data. A third option is not (hourly/daily/weekly) updating data, in that case you can delete a lot of tables.</p>
<p>The 800GB requirement (<a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Hardware)">https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Hardware)</a> might be outdated. The last full planet import I ran came just short of 500GB. OpenStreetMap data keeps growing every month and Postgres fragments the database with every small update (let's say it leaves empty spots on the harddrive when deleting rows) so I wouldn't recommend a standard 480GB drive yet. But it's certainty not the 3TB you calculated based on a 3.2MB input file.</p>
<blockquote>
<p>it is not clear to me what is nominatim doing with osm2pgsql if the data structures are different.</p>
</blockquote>
<p>Nominatim uses osm2pgsql to import the data structures it needs based on its own configuration and use-case. When you setup a setup a server for map tile rendering and search (Nominatim) that data needs to go into separate database. (related question: <a href="https://help.openstreetmap.org/questions/52978/possible-to-use-one-db-for-nominatim-and-tile-server)">https://help.openstreetmap.org/questions/52978/possible-to-use-one-db-for-nominatim-and-tile-server)</a> Yes, it's seems like a huge waste to have most data twice but the systems aren't connected and there's no plans to have them use the same data structures.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '17, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-54930" class="comments-container">
<span id="54931"></span>
<div id="comment-54931" class="comment">
<div id="post-54931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. Just to clarify, my use case is geocoding and reverse geocoding, not a tile server. I am not importing any US data, the test I have done is with a small european country. My worry was because if a 3.2Mb map ended up taking 265Mb, by simple proportion, without TIGER or anything, if the osm full planet file is 37GB, I was concerned it would end up some 3TB. 500GB (even 800GB) is quite managable.</p>
</div>
<div id="comment-54931-info" class="comment-info">
<span class="comment-age">(05 Mar '17, 23:00)</span> <span class="comment-user userinfo">jbx1</span>
</div>
</div>
</div>
<div id="comment-tools-54930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54930-form-container" class="comment-form-container">
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

