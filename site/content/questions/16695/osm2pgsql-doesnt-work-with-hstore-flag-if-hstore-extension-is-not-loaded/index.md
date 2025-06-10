+++
type = "question"
title = "osm2pgsql doesn&#x27;t work with --hstore flag if hstore extension is not loaded"
description = '''I&#x27;m trying to import some OSM data into my postgis database and can&#x27;t seem to get it to work. The data is an a US state extract from geofabrik that was further reduced using OSM convert to my study area. I checked out the data in QGIS and it looks good.  Below is the error message I receive when run...'''
date = "2012-10-05T21:16:00Z"
lastmod = "2012-10-08T19:47:00Z"
weight = 16695
keywords = [ "postgresql", "osm2pgsql", "postgis" ]
aliases = [ "/questions/16695" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgsql doesn't work with --hstore flag if hstore extension is not loaded](/questions/16695/osm2pgsql-doesnt-work-with-hstore-flag-if-hstore-extension-is-not-loaded)

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
<span id="post-16695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16695-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to import some OSM data into my postgis database and can't seem to get it to work. The data is an a US state extract from geofabrik that was further reduced using OSM convert to my study area. I checked out the data in QGIS and it looks good.</p>
<p>Below is the error message I receive when run osm2pgsql. I checked the database after running the tool and there is only one table listed "spatial_ref_sys". Any ideas what I'm doing wrong?</p>
<pre><code>C:\Users\moreland_t\Documents\OSM Playground\Data&gt;osm2pgsql tennessee.osm_RPG_01
 -d OSM -U postgres -W secretpassword  -P 5432 -S default.style --hstore
osm2pgsql SVN version 0.69-21289M
&#10;Password:
Using projection SRS 900913 (Spherical Mercator)
Setting up table: planet_osm_point
NOTICE:  table &quot;planet_osm_point&quot; does not exist, skipping
NOTICE:  table &quot;planet_osm_point_tmp&quot; does not exist, skipping
CREATE TABLE planet_osm_point ( osm_id int4,&quot;access&quot; text,&quot;addr:flats&quot; text,&quot;add
r:housenumber&quot; text,&quot;addr:interpolation&quot; text,&quot;admin_level&quot; text,&quot;aerialway&quot; tex
t,&quot;aeroway&quot; text,&quot;amenity&quot; text,&quot;area&quot; text,&quot;barrier&quot; text,&quot;bicycle&quot; text,&quot;bridg
e&quot; text,&quot;boundary&quot; text,&quot;building&quot; text,&quot;capital&quot; text,&quot;construction&quot; text,&quot;cutt
ing&quot; text,&quot;disused&quot; text,&quot;ele&quot; text,&quot;embankment&quot; text,&quot;foot&quot; text,&quot;highway&quot; text
,&quot;historic&quot; text,&quot;horse&quot; text,&quot;junction&quot; text,&quot;landuse&quot; text,&quot;layer&quot; text,&quot;learn
ing&quot; text,&quot;leisure&quot; text,&quot;lock&quot; text,&quot;man_made&quot; text,&quot;military&quot; text,&quot;motorcar&quot;
text,&quot;name&quot; text,&quot;natural&quot; text,&quot;oneway&quot; text,&quot;operator&quot; text,&quot;poi&quot; text,&quot;power&quot;
 text,&quot;power_source&quot; text,&quot;place&quot; text,&quot;railway&quot; text,&quot;ref&quot; text,&quot;religion&quot; text
,&quot;residence&quot; text,&quot;route&quot; text,&quot;service&quot; text,&quot;shop&quot; text,&quot;sport&quot; text,&quot;tourism&quot;
 text,&quot;tunnel&quot; text,&quot;waterway&quot; text,&quot;width&quot; text,&quot;wood&quot; text,&quot;z_order&quot; int4,tags
 hstore );
 failed: ERROR:  type &quot;hstore&quot; does not exist
LINE 1: ... text,&quot;width&quot; text,&quot;wood&quot; text,&quot;z_order&quot; int4,tags hstore );
                                                              ^
&#10;Error occurred, cleaning up</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '12, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/f277db511cb41024d382a849d946b4ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="T_9er&#39;s gravatar image" />
<p><span>T_9er</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="T_9er has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '12, 23:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-16695" class="comments-container">
&#10;</div>
<div id="comment-tools-16695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16695-form-container" class="comment-form-container">
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

<span id="16697"></span>

<div id="answer-container-16697" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16697-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-16697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="T_9er has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to load the "hstore" extension. How to do this depends on what version of PostgreSQL you're running; it might be as easy as typing <code>create extension hstore</code> in your psql command prompt, or you might have to install a package named postgresql-contrib and from that load the hstore.sql file. Alternatively, leave out the --hstore flag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '12, 23:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16697" class="comments-container">
<span id="16730"></span>
<div id="comment-16730" class="comment">
<div id="post-16730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply. I was able to load the hstore extension but then ran into several other problems. I'm working on a windows machince and found the following turorial every helpful in finding a fix for the issues I kept running into. <a href="https://github.com/springmeyer/win-osm-workshop/blob/master/Tutorial.md#step-6-configure-the-osm-postgis-database">https://github.com/springmeyer/win-osm-workshop/blob/master/Tutorial.md#step-6-configure-the-osm-postgis-database</a></p>
</div>
<div id="comment-16730-info" class="comment-info">
<span class="comment-age">(08 Oct '12, 15:34)</span> <span class="comment-user userinfo">T_9er</span>
</div>
</div>
<span id="16738"></span>
<div id="comment-16738" class="comment">
<div id="post-16738-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is no recent version of osm2pgsql for Windows. You may be better off running a linux VM then trying to get everything working on Windows</p>
</div>
<div id="comment-16738-info" class="comment-info">
<span class="comment-age">(08 Oct '12, 19:47)</span> <span class="comment-user userinfo">pnorman</span>
</div>
</div>
</div>
<div id="comment-tools-16697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16697-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16696"></span>

<div id="answer-container-16696" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16696-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-16696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/openstreetmap/osm2pgsql/blob/master/README#L115">RTFM</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '12, 22:18</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-16696" class="comments-container">
&#10;</div>
<div id="comment-tools-16696" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16696-form-container" class="comment-form-container">
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

