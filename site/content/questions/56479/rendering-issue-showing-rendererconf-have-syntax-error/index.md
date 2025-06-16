+++
type = "question"
title = "Rendering issue showing renderer.conf have syntax error"
description = '''I have been following this link to install on centos most of the steps work except for the style style step had issues. My current issue this An error occurred while loading the map layer &#x27;default&#x27;: Could not create datasource for type: &#x27;postgis&#x27; (searched for datasource plugins in &#x27;/usr/local/lib/m...'''
date = "2017-06-06T20:34:00Z"
lastmod = "2017-06-11T17:01:00Z"
weight = 56479
keywords = [ "rendering" ]
aliases = [ "/questions/56479" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering issue showing renderer.conf have syntax error](/questions/56479/rendering-issue-showing-rendererconf-have-syntax-error)

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
<span id="post-56479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56479-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been following this link to install on centos most of the steps work except for the style style step had issues. My current issue this An error occurred while loading the map layer 'default': Could not create datasource for type: 'postgis' (searched for datasource plugins in '/usr/local/lib/mapnik/input') encountered during parsing of layer 'landuse_gen0' in Layer at line 262 of '/usr/local/share/maps/style/OSMBright/OSMBright.xml'. Below is my renderd.conf</p>
<pre><code>[renderd]
socketname=/var/run/renderd/renderd.sock
plugins_dir=/usr/local/lib/mapnik/input
font_dir=/usr/share/fonts/ 
XML=/usr/local/share/maps/style/OSMBright/OSMBright.xml
HOST=localhost
&#10;[mapnik]
socketname=/var/run/renderd/renderd.sock
plugins_dir=/usr/local/lib/mapnik/input
font_dir=/usr/share/fonts/ 
XML=/usr/local/share/maps/style/OSMBright/OSMBright.xml
HOST=localhost
;plugins_dir=/usr/lib/mapnik/input
;font_dir=/usr/share/fonts/truetype
font_dir_recurse=1
&#10;[default]
socketname=/var/run/renderd/renderd.sock
plugins_dir=/usr/local/lib/mapnik/input
font_dir=/usr/share/fonts/ 
XML=/usr/local/share/maps/style/OSMBright/OSMBright.xml
HOST=localhost</code></pre>
<p>The issue in my OSMBright.xml is pointing to this lines. &lt;layer name="landuse_gen0" status="on" srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=<a href="https://help.openstreetmap.org/users/2957/nullpointer"></a><a href="https://help.openstreetmap.org/users/2957/nullpointer">@null</a></a> +wktext +no_defs +over"&gt; &lt;stylename&gt;landuse_gen0&lt;/stylename&gt; &lt;datasource&gt; &lt;parameter name="dbname"&gt;&lt;![CDATA[gis]]&gt;&lt;/parameter&gt; &lt;parameter name="extent"&gt;&lt;![CDATA[-20037508.34,-20037508.34,20037508.34,20037508.34]]&gt;&lt;/parameter&gt; &lt;parameter name="geometry_field"&gt;&lt;![CDATA[way]]&gt;&lt;/parameter&gt; &lt;parameter name="id"&gt;&lt;![CDATA[landuse_gen0]]&gt;&lt;/parameter&gt; &lt;parameter name="key_field"&gt;&lt;![CDATA[]]&gt;&lt;/parameter&gt; &lt;parameter name="project"&gt;&lt;![CDATA[osm-bright-imposm]]&gt;&lt;/parameter&gt; &lt;parameter name="srs"&gt;&lt;![CDATA[+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=<a href="https://help.openstreetmap.org/users/2957/nullpointer"></a><a href="https://help.openstreetmap.org/users/2957/nullpointer">@null</a></a> +wktext +no_defs +over]]&gt;&lt;/parameter&gt; &lt;parameter name="table"&gt;&lt;![CDATA[( SELECT way, way_area AS area, COALESCE(landuse, leisure, "natural", highway, amenity, tourism) AS type FROM planet_osm_polygon WHERE way_area &gt; 100000 ORDER BY way_area DESC ) AS data]]&gt;&lt;/parameter&gt; &lt;parameter name="type"&gt;&lt;![CDATA[postgis]]&gt;&lt;/parameter&gt; &lt;/datasource&gt; &lt;/layer&gt;</p>
<p>I have installed all of this yum install postgresql96-libs postgresql96-contrib postgresql96-devel</p>
<p>yum install postgis2_96 postgis2_96-client postgis2_96-utils and rebuild mapnik yet the same issue.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '17, 20:34</strong></p>
<img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" />
<p><span>newbie14</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '17, 03:49</strong> </span></p>
</div>
</div>
<div id="comments-container-56479" class="comments-container">
<span id="56500"></span>
<div id="comment-56500" class="comment">
<div id="post-56500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have tried DROP DATABASE gis; and repeat these steps again sudo -u postgres createuser -s osm sudo -u postgres createuser apache sudo -u postgres createdb -E UTF8 -O osm gis sudo -u postgres psql \c gis CREATE EXTENSION postgis; ALTER TABLE geometry_columns OWNER TO osm; ALTER TABLE spatial_ref_sys OWNER TO osm; \q yet the same results I get issue on the ould not create datasource for type: 'postgis' (searched for datasource plugins in '/usr/local/lib/mapnik/input')</p>
</div>
<div id="comment-56500-info" class="comment-info">
<span class="comment-age">(07 Jun '17, 18:26)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
</div>
<div id="comment-tools-56479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56479-form-container" class="comment-form-container">
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

<span id="56483"></span>

<div id="answer-container-56483" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56483-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You've got a series of issues there:</p>
<ol>
<li>Ignore the iniparser errors</li>
<li>Fix the font directory in the config to where the fonts actually live (and install whatever fonts are needed)</li>
<li>Fix the path to the mapnik.xml file in the config to point to wherever you created it.</li>
</ol>
<p>You'll want to fix the database access issue that you logged <a href="/questions/56477/osm2pgsql-connection-to-database-failed-fatal-ident-authentication-failed-for-user-postgres">here</a> first though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '17, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-56483" class="comments-container">
<span id="56485"></span>
<div id="comment-56485" class="comment">
<div id="post-56485-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have actually encountered a lot of problem like not var/run/renderd directory etc all I have build and settle. I also had issue with font so I just took the dejavu-fonts-ttf-2.33 from the mapnik and dump into /usr/share/fonts. Most issue resolved now I got one issue which I am stucked An error occurred while loading the map layer 'default': Could not create datasource for type: 'postgis' (searched for datasource plugins in '/usr/local/lib/mapnik/input') encountered during parsing of layer 'landuse_gen0' in Layer at line 262 of '/usr/local/share/maps/style/OSMBright/OSMBright.xml'</p>
</div>
<div id="comment-56485-info" class="comment-info">
<span class="comment-age">(07 Jun '17, 03:45)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56530"></span>
<div id="comment-56530" class="comment">
<div id="post-56530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re postgis, I'm guessing that you haven't configured postgis for your database properly. Beyond that it's difficult to say (and I've no ideas what gotchas you'll see with a postgis install with postgres 9.6 on Centos).</p>
</div>
<div id="comment-56530-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 13:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56560"></span>
<div id="comment-56560" class="comment">
<div id="post-56560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneelse</a> I have tried many method remove the 9.6 and install 9.5 and ensure all the postgis have been installed cause else this command CREATE EXTENSION postgis; should not work right. So I tried all its still facing the same issue. I think looks like centos is not ready for this osm.</p>
</div>
<div id="comment-56560-info" class="comment-info">
<span class="comment-age">(09 Jun '17, 16:42)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56561"></span>
<div id="comment-56561" class="comment">
<div id="post-56561-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneelse</a> it looks more like a mapnik issue missing the postgis in its input file.</p>
</div>
<div id="comment-56561-info" class="comment-info">
<span class="comment-age">(09 Jun '17, 16:45)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56562"></span>
<div id="comment-56562" class="comment">
<div id="post-56562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>I think looks like centos is not ready for this osm.</p>
</blockquote>
<p>I'm sure that it'd be possible to get it working (and <a href="https://github.com/lijenpan/osm/blob/master/osm-centos7.md">https://github.com/lijenpan/osm/blob/master/osm-centos7.md</a> covers postgis of course) but it was never going to be as straightforward as the alternatives, unfortunately, as mentioned way back on <a href="https://forum.openstreetmap.org/viewtopic.php?pid=648795#p648795">https://forum.openstreetmap.org/viewtopic.php?pid=648795#p648795</a> .</p>
<p>At some point someone (maybe even me) will have a go at a Cantos "switch2osm" example including the jumping through hoops that you need to do for node and carto with the latest osm-carto style, but it's some way down the list for me alas.</p>
<p>Edit:</p>
<blockquote>
<p><a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneelse</a> it looks more like a mapnik issue missing the postgis in its input file.</p>
</blockquote>
<p>Quite possibly, but mapnik is something that I poke only with a very long stick when absolutely necessary :)</p>
</div>
<div id="comment-56562-info" class="comment-info">
<span class="comment-age">(09 Jun '17, 16:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56569"></span>
<div id="comment-56569" class="comment not_top_scorer">
<div id="post-56569-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneelse</a> ok I got not choice I will getting ready a new machine with ubuntu16.04 cause I wasted a lot of time on centos now is leading no where. So for ubuntu it must a be minimal installation does it need gui or will do with out it? What else I will need to be prepared for this?</p>
</div>
<div id="comment-56569-info" class="comment-info">
<span class="comment-age">(10 Jun '17, 06:15)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56580"></span>
<div id="comment-56580" class="comment not_top_scorer">
<div id="post-56580-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd start with <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> (I updated it yesterday to work with newer "carto" versions). No GUI needed, just Ubuntu server 16.04 LTS.</p>
</div>
<div id="comment-56580-info" class="comment-info">
<span class="comment-age">(11 Jun '17, 17:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56483" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-56483-form-container" class="comment-form-container">
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

