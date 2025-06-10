+++
type = "question"
title = "Building a Tileserver - PostGIS Errors"
description = '''Hey there, I am working with this tutorial https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ and get the following Errors after running &quot;renderd -f -c /usr/local/etc/renderd.conf&quot;:  An error occurred while loading the map layer &#x27;ajt&#x27;: Postgis Plugin: ERROR: relation &quot;planet_osm_pol...'''
date = "2017-12-14T13:28:00Z"
lastmod = "2017-12-15T13:14:00Z"
weight = 61183
keywords = [ "openstreetmap", "postgis", "tileserver" ]
aliases = [ "/questions/61183" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Building a Tileserver - PostGIS Errors](/questions/61183/building-a-tileserver-postgis-errors)

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
<span id="post-61183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61183-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey there, I am working with this tutorial <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> and get the following Errors after running "renderd -f -c /usr/local/etc/renderd.conf":</p>
<pre><code> An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;planet_osm_polygon&quot; does not exist LINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM planet_osm_polygon WHERE ...
&#10;in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM planet_osm_polygon WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 618 of &#39;/home/gsits/src/openstreetmap-carto/mapnik.xml&#39;renderd[19152]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;planet_osm_polygon&quot; does not existLINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM planet_osm_polygon WHERE ...
&#10;in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM planet_osm_polygon WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39; encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 618 of &#39;/home/gsits/src/openstreetmap-carto/mapnik.xml&#39;</code></pre>
<p>Any idea what that means and how to fix this?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '17, 13:28</strong></p>
<img src="https://secure.gravatar.com/avatar/fd29f6ff9fde6417ba9cd2ebaa2d0568?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thal0n&#39;s gravatar image" />
<p><span>Thal0n</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thal0n has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61183" class="comments-container">
<span id="61184"></span>
<div id="comment-61184" class="comment">
<div id="post-61184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks as though you never imported any data.</p>
</div>
<div id="comment-61184-info" class="comment-info">
<span class="comment-age">(14 Dec '17, 13:40)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="61186"></span>
<div id="comment-61186" class="comment">
<div id="post-61186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When trying to insert the data into the database it says: Setting up table: planet_osm_point Osm2pgsql failed due to ERROR: CREATE UNLOGGED TABLE planet_osm_point (osm_id int8,"access" text,"addr:housename" text,"addr:housenumber" text,"admin_level" text,"aerialway" text,"aeroway" text,"amenity" text,"barrier" text,"boundary" text,"building" text,"highway" text,"historic" text,"junction" text,"landuse" text,"layer" int4,"leisure" text,"lock" text,"man_made" text,"military" text,"name" text,"natural" text,"oneway" text,"place" text,"power" text,"railway" text,"ref" text,"religion" text,"shop" text,"tourism" text,"water" text,"waterway" text,"tags" hstore,way geometry(POINT,3857) ) WITH ( autovacuum_enabled = FALSE ) failed: ERROR: type "hstore" does not exist LINE 1: ...tourism" text,"water" text,"waterway" text,"tags" hstore,way...</p>
</div>
<div id="comment-61186-info" class="comment-info">
<span class="comment-age">(14 Dec '17, 14:09)</span> <span class="comment-user userinfo">Thal0n</span>
</div>
</div>
<span id="61199"></span>
<div id="comment-61199" class="comment">
<div id="post-61199-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Did you run the line CREATE EXTENSION hstore;?</p>
</div>
<div id="comment-61199-info" class="comment-info">
<span class="comment-age">(15 Dec '17, 07:44)</span> <span class="comment-user userinfo">Math_1985</span>
</div>
</div>
<span id="61205"></span>
<div id="comment-61205" class="comment">
<div id="post-61205-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What does "sudo apt list --installed | grep -i postgres" say?</p>
<p>I've seen similar problems on a 14.04 machine that had been upgraded from 12.04 to 14.04, and had ended up with two versions of postgres installed. The initial error suggested that hstore was missing, but the actual issue was that I had a mixture of two postgres versions. Completely removing postgres via "sudo apt-get --purge remove" with each of the installed packages and then reinstalling it worked for me (of course, this would only make sense to you if your problem is the same and you don't need that older version for something else).</p>
</div>
<div id="comment-61205-info" class="comment-info">
<span class="comment-age">(15 Dec '17, 13:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61183-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

