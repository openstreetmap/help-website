+++
type = "question"
title = "osmosis import : duplicate key value violates unique constraint"
description = '''Hello everyone, I had successfully installed openstreetmap-website on Ubuntu 14.04. Now I&#x27;am trying to import a pbf file into the &quot;openstreetmap&quot; database using the following command: osmosis --read-pbf /home/osm-data/my_citie.osm.pbf --write-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot; user=&quot;pos...'''
date = "2015-10-16T09:04:00Z"
lastmod = "2015-10-16T16:20:00Z"
weight = 45930
keywords = [ "osm", "osmosis" ]
aliases = [ "/questions/45930" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis import : duplicate key value violates unique constraint](/questions/45930/osmosis-import-duplicate-key-value-violates-unique-constraint)

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
<span id="post-45930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45930-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I had successfully installed openstreetmap-website on Ubuntu 14.04. Now I'am trying to import a pbf file into the "openstreetmap" database using the following command:</p>
<p><code>osmosis --read-pbf /home/osm-data/my_citie.osm.pbf --write-apidb host="localhost" database="openstreetmap" user="postgres" password="*********" validateSchemaVersion="no</code></p>
<p>but I still get this error:</p>
<pre><code>org.postgresql.util.PSQLException: ERROR: duplicate key value violates unique constraint &quot;current_nodes_pkey1&quot;</code></pre>
<p>Note: Osmosis Version is 0.40.1<br />
I installed it with "sudo apt-get install osmosis"<br />
PBF file downloded from Mapzen Metro Extracts<br />
PostgreSQL version is 9.3</p>
<p>I need your help please</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '15, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/7355dafb903301c43c303a104c75f265?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AYARI&#39;s gravatar image" />
<p><span>AYARI</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AYARI has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '15, 09:15</strong> </span></p>
</div>
</div>
<div id="comments-container-45930" class="comments-container">
<span id="45936"></span>
<div id="comment-45936" class="comment not_top_scorer">
<div id="post-45936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does the full error message state which key is duplicated?</p>
</div>
<div id="comment-45936-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 09:59)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45937"></span>
<div id="comment-45937" class="comment not_top_scorer">
<div id="post-45937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, this is the full message :</p>
<pre><code>Caused by: org.postgresql.util.PSQLException: ERROR: duplicate key value violates unique constraint &quot;nodes_pkey&quot; Détail : Key (node_id, version)=(27564968, 67) already exists.</code></pre>
</div>
<div id="comment-45937-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 10:09)</span> <span class="comment-user userinfo">AYARI</span>
</div>
</div>
<span id="45939"></span>
<div id="comment-45939" class="comment">
<div id="post-45939-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Maybe the extract is broken, you could try a different <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">extract</a>. And/or a newer osmosis version (the latest version is 0.44.1) but a duplicated key or a duplicated node sounds weird.</p>
</div>
<div id="comment-45939-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 10:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45940"></span>
<div id="comment-45940" class="comment not_top_scorer">
<div id="post-45940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried with another extract from geofabrik, but I always get the same error.</p>
<p>How can I install the latest osmosis version ?? apt-get always install 0.40.1</p>
</div>
<div id="comment-45940-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 11:16)</span> <span class="comment-user userinfo">AYARI</span>
</div>
</div>
<span id="45941"></span>
<div id="comment-45941" class="comment">
<div id="post-45941-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You have to <a href="https://wiki.openstreetmap.org/wiki/Osmosis">download</a> it yourself, unpack it and run it via <code>./osmosis-latest/bin/osmosis</code> (or whatever path you extracted it to).</p>
</div>
<div id="comment-45941-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 11:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45942"></span>
<div id="comment-45942" class="comment not_top_scorer">
<div id="post-45942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As an aside, it might be worth adding (or asking in another question) what you're planning to use a copy of the OSM website with Tunis data in it for - there might be an easier way to achieve what you're trying to do by some other method.</p>
</div>
<div id="comment-45942-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 11:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45952"></span>
<div id="comment-45952" class="comment">
<div id="post-45952-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>finally solved</p>
<p>I used the latest version of osmosis (0.44.1) and a ".bz2" osm file that I downloaded from geofabrik, now the import goes without any error.</p>
<p>But I still do not understand the issue</p>
</div>
<div id="comment-45952-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 14:11)</span> <span class="comment-user userinfo">AYARI</span>
</div>
</div>
<span id="45953"></span>
<div id="comment-45953" class="comment">
<div id="post-45953-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>SomeoneElse :</p>
<p>I'am using Tunis data just for test, but I'am working on the whole planet database for map rendering, geocoding and routing..</p>
</div>
<div id="comment-45953-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 14:23)</span> <span class="comment-user userinfo">AYARI</span>
</div>
</div>
<span id="45956"></span>
<div id="comment-45956" class="comment not_top_scorer">
<div id="post-45956-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you're interested in rendering, geocoding and routing, then an APIDB may not be the way to go. For rendering in the same way as osm.org, see <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a> (though other renderers are available), for geocoding see <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> (again, other geocoders exist), for routing perhaps some of the examples from <a href="https://wiki.openstreetmap.org/wiki/Routing#Developers">https://wiki.openstreetmap.org/wiki/Routing#Developers</a> .</p>
</div>
<div id="comment-45956-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 14:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45957"></span>
<div id="comment-45957" class="comment">
<div id="post-45957-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>According to <a href="https://github.com/openstreetmap/osmosis/blob/master/package/changes.txt">changes.txt</a> version 0.44.1 fixed an issue with "duplicate way nodes in pgsnapshot module" which could be the reason for your error. Or one of the many other fixes between version 0.40.1 and 0.44.1.</p>
</div>
<div id="comment-45957-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 16:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45930" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-45930-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

