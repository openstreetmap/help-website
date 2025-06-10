+++
type = "question"
title = "mapnik-german osm style, problem with views in postgres database"
description = '''Hi, I am trying to get the german mapnik style to work on Ubuntu 12.04 as proposed by the SVN README: &amp;gt; To deploy this style use the supplied default.style file for &amp;gt; osm2pgsql and import data using the hstore extension of &amp;gt; PostgreSQL (--hstore --hstore-match-only switches of osm2pgsql). &amp;...'''
date = "2012-12-29T14:24:00Z"
lastmod = "2015-04-27T15:49:00Z"
weight = 18752
keywords = [ "style", "mapnik-german", "mapnik", "postgis", "postgres" ]
aliases = [ "/questions/18752" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [mapnik-german osm style, problem with views in postgres database](/questions/18752/mapnik-german-osm-style-problem-with-views-in-postgres-database)

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
<span id="post-18752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18752-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to get the german mapnik style to work on Ubuntu 12.04 as proposed by the <a href="http://svn.openstreetmap.org/applications/rendering/mapnik-german/">SVN</a> README:</p>
<pre><code>&gt; To deploy this style use the supplied default.style file for
&gt; osm2pgsql and import data using the hstore extension of
&gt; PostgreSQL (--hstore --hstore-match-only switches of osm2pgsql).
&gt;
&gt; To keep the database compatible to the &quot;original&quot; Mapnik style we
&gt; now use views instead of tables. SQL scripts to set up these views
&gt; are supplied in the views directory.</code></pre>
<p>I create my database using sachsen.osm from geofabrik and osm2pgsql from the ppa:kakrueger/openstreetmap (osm2pgsql SVN version 0.81.0 (64bit id space))</p>
<pre><code>osm2pgsql -m -d osm --hstore -W -S /path/to/mapnik-german/views/default.style  mapnik/sachsen.osm</code></pre>
<p>Then I create the views that are supposed to be used by the germany mapnik style:</p>
<pre><code>sudo -u postgres psql osm &lt; mapnik-german/views/view-line.sql
sudo -u postgres psql osm &lt; mapnik-german/views/view-point.sql
sudo -u postgres psql osm &lt; mapnik-german/views/view-polygon.sql
sudo -u postgres psql osm &lt; mapnik-german/views/view-roads.sql</code></pre>
<p>Then I create a new directory "mapnik-de" containing the <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/">mapnik-repo</a>. I copy <a href="http://svn.openstreetmap.org/applications/rendering/mapnik-german/">mapnik-german</a> ontop of that (is that the way to go?) and copy all the template files to inc files in mapnik-de/inc-de/. I use mapnik-de as working directory.</p>
<p>Now, when I try to generate my xml file</p>
<pre><code>./generate_xml.py --dbname osm --host &#39;localhost&#39; --user USERNAME --port 5432 --password &#39;PASSWORD&#39; --inc inc-de  osm-de.xml &gt; osm-local.xml</code></pre>
<p>I get the following error:</p>
<pre><code>/usr/lib/pymodules/python2.7/mapnik2/__init__.py:27: DeprecationWarning:  mapnik2 module has been deprecated,
        please use &#39;import mapnik&#39; 
  warnings.warn(msg, DeprecationWarning)
Traceback (most recent call last):
  File &quot;./generate_xml.py&quot;, line 204, in &lt;module&gt;
    serialize(template_xml,options)
  File &quot;./generate_xml.py&quot;, line 80, in serialize
    mapnik.load_map(m,xml,True)
RuntimeError: Postgis Plugin: PSQL error:
ERROR:  column &quot;wood&quot; does not exist
LINE 1: ...enity,landuse,leisure,man_made,military,&quot;natural&quot;,wood,power...
                                                             ^
Full sql was: &#39;SELECT * FROM (select way,aeroway,amenity,landuse,leisure,man_made,military,&quot;natural&quot;,wood,power,tourism,coalesce(&quot;name:de&quot;,name) as name,highway,
       case when religion in (&#39;christian&#39;,&#39;jewish&#39;) then religion else &#39;INT-generic&#39;::text end as religion
       from planet_osm_polygon
       where landuse is not null
          or leisure is not null
          or aeroway in (&#39;apron&#39;,&#39;aerodrome&#39;)
          or amenity in (&#39;parking&#39;,&#39;university&#39;,&#39;college&#39;,&#39;school&#39;,&#39;hospital&#39;,&#39;kindergarten&#39;,&#39;grave_yard&#39;,&#39;prison&#39;)
          or military in (&#39;barracks&#39;,&#39;danger_area&#39;)
          or &quot;natural&quot; in (&#39;field&#39;,&#39;beach&#39;,&#39;desert&#39;,&#39;heath&#39;,&#39;mud&#39;,&#39;grassland&#39;,&#39;wood&#39;,&#39;sand&#39;,&#39;scrub&#39;)
          or power in (&#39;station&#39;,&#39;sub_station&#39;,&#39;generator&#39;)
          or tourism in (&#39;attraction&#39;,&#39;camp_site&#39;,&#39;caravan_site&#39;,&#39;picnic_site&#39;,&#39;zoo&#39;)
          or highway in (&#39;services&#39;,&#39;rest_area&#39;)
       order by z_order,way_area desc
      ) as leisure LIMIT 0&#39;
  encountered during parsing of layer &#39;landcover&#39; in Layer at line 381 of &#39;osm-de.xml&#39;</code></pre>
<p>I am using mapnik 2.1.0 from the ppa:mapnik/v2.1.0</p>
<p>To me it looks like the generated views are not correctly accessed. When I use a custom default.style file with osm2pgsql that contains "wood" and a couple more, then this error does not show and I can create tiles.</p>
<p>I am not used to postgresql or postgis. Maybe I just understood something wrong? I took a look with pgadmin3 and there are the four views and except view_osmde_roads they all contain the column "wood".</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-mapnik-german" rel="tag" title="see questions tagged &#39;mapnik-german&#39;">mapnik-german</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '12, 14:24</strong></p>
<img src="https://secure.gravatar.com/avatar/8841f5a6a609b7eb4cb703f440ffc5e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skaiwalker&#39;s gravatar image" />
<p><span>skaiwalker</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skaiwalker has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Dec '12, 14:39</strong> </span></p>
</div>
</div>
<div id="comments-container-18752" class="comments-container">
&#10;</div>
<div id="comment-tools-18752" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18752-form-container" class="comment-form-container">
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

<span id="18753"></span>

<div id="answer-container-18753" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18753-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="skaiwalker has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your Mapnik style is trying to access the tables directly instead of the generated views.</p>
<p>I would assume that your prefix entity in settings.xml.inc is wrong.</p>
<p>It should contain &lt;!ENTITY prefix "view_osmde"&gt; instead of &lt;!ENTITY prefix "planet_osm"&gt;</p>
<p>Sven</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '12, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ed4b275dcccc85019201630e7cf0e3b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giggls&#39;s gravatar image" />
<p><span>giggls</span><br />
<span class="score" title="126 reputation points">126</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giggls has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-18753" class="comments-container">
<span id="18756"></span>
<div id="comment-18756" class="comment">
<div id="post-18756-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Sven,<br />
I simply forgot the "--prefix" option in generate_xml.py.</p>
<p>But there is another problem with the database. My generate_xml.py command now looks like this:</p>
<pre><code>./mapnik/generate_xml.py \
 --host &#39;localhost&#39; \
 --port 5432 \
 --dbname osm \
 --prefix view_osmde \
 --user postgres \
 --password &#39;USERPWD&#39; \
 --inc /home/USERNAME/osm/mapnik-german/inc-de \
 --world_boundaries /home/USERNAME/osm/mapnik/world_boundaries \
 /home/USERNAME/osm/mapnik-german/osm-de.xml &gt; /home/USERNAME/osm/mapnik-german/osm-local.xml</code></pre>
<p>And it works.</p>
<p>When I run generate_tiles.py, it only generates 0/0/0.png and I get errors like this:</p>
<pre><code>Exception in thread Thread-1:
Traceback (most recent call last):
  File &quot;/usr/lib/python2.7/threading.py&quot;, line 551, in __bootstrap_inner
    self.run()
  File &quot;/usr/lib/python2.7/threading.py&quot;, line 504, in run
    self.__target(*self.__args, **self.__kwargs)
  File &quot;./mapnik-german/generate_tiles.py&quot;, line 115, in loop
    self.render_tile(tile_uri, x, y, z)
  File &quot;./mapnik-german/generate_tiles.py&quot;, line 97, in render_tile
    mapnik.render(self.m, im)
RuntimeError: PostGIS: geometry name lookup failed for table &#39;view_osmde_point&#39;. Please manually provide the &#39;geometry_field&#39; parameter or add an entry in the geometry_columns for &#39;view_osmde_point&#39;.</code></pre>
<p>What does that mean? Cheers!</p>
</div>
<div id="comment-18756-info" class="comment-info">
<span class="comment-age">(29 Dec '12, 18:57)</span> <span class="comment-user userinfo">skaiwalker</span>
</div>
</div>
</div>
<div id="comment-tools-18753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18753-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18759"></span>

<div id="answer-container-18759" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18759-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After some googling I found this function "populate_geometry_columns()" and it seemed to do the job:</p>
<pre><code>sudo -u postgres psql -d osm
SELECT populate_geometry_columns();</code></pre>
<p>Creating tiles with german style now works.<br />
Can you please confirm that I did the right thing? I will write up a short Quickstart guide and upload it to the repo.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '12, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/8841f5a6a609b7eb4cb703f440ffc5e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skaiwalker&#39;s gravatar image" />
<p><span>skaiwalker</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skaiwalker has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-18759" class="comments-container">
<span id="42616"></span>
<div id="comment-42616" class="comment">
<div id="post-42616-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I had the same problem and that solved it for me too!</p>
</div>
<div id="comment-42616-info" class="comment-info">
<span class="comment-age">(27 Apr '15, 15:49)</span> <span class="comment-user userinfo">milkbread</span>
</div>
</div>
</div>
<div id="comment-tools-18759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18759-form-container" class="comment-form-container">
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

