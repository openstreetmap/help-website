+++
type = "question"
title = "Has anyone successfully loaded OSM to PostgreSQL with osm2pgsql on Windows lately?"
description = '''I can&#x27;t seem to find any clear and current documentation on the process and am stuck here: E:&#92;GIS_Data&#92;OSM&amp;gt;osm2pgsql -v -U maugust -W -s --host localhost 4096 -S default.s tyle -d POSTGIS US-WEST-LATEST.OSM.BZ2 osm2pgsql SVN version 0.69-21289M Password: Using projection SRS 900913 (Spherical Mer...'''
date = "2014-05-28T17:15:00Z"
lastmod = "2014-05-28T21:49:00Z"
weight = 33533
keywords = [ "pgsql", "osm", "osm2pgsql", "database" ]
aliases = [ "/questions/33533" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Has anyone successfully loaded OSM to PostgreSQL with osm2pgsql on Windows lately?](/questions/33533/has-anyone-successfully-loaded-osm-to-postgresql-with-osm2pgsql-on-windows-lately)

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
<span id="post-33533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33533-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can't seem to find any clear and current documentation on the process and am stuck here:</p>
<p>E:\GIS_Data\OSM&gt;osm2pgsql -v -U maugust -W -s --host localhost 4096 -S default.s tyle -d POSTGIS US-WEST-LATEST.OSM.BZ2 osm2pgsql SVN version 0.69-21289M</p>
<p>Password: Using projection SRS 900913 (Spherical Mercator) Setting up table: planet_osm_point NOTICE: table "planet_osm_point" does not exist, skipping NOTICE: table "planet_osm_point_tmp" does not exist, skipping PREPARE get_way (int4) AS SELECT AsText(way) FROM planet_osm_point WHERE osm_id = $1; failed: ERROR: function astext(geometry) does not exist LINE 1: PREPARE get_way (int4) AS SELECT AsText(way) FROM planet_osm... ^ HINT: No function matches the given name and argument types. You might need to add explicit type casts.</p>
<p>Error occurred, cleaning up</p>
<p>I've read this <a href="http://forum.openstreetmap.org/viewtopic.php?id=16350">http://forum.openstreetmap.org/viewtopic.php?id=16350</a> which seems to indicate that some things in Post GIS 2.0+ are broken for windows? Are there any workarounds for this, and any further, renamed columns/fields, etc.? or are Windows users at PostGIS 2.0 simply unable to load OSM data with osm2pgsql?</p>
<p>Thanks for any suggestions!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pgsql" rel="tag" title="see questions tagged &#39;pgsql&#39;">pgsql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '14, 17:15</strong></p>
<img src="https://secure.gravatar.com/avatar/61dfcaeba5e4f2391b670792231ac31f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aug_aug&#39;s gravatar image" />
<p><span>aug_aug</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aug_aug has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33533" class="comments-container">
<span id="33540"></span>
<div id="comment-33540" class="comment">
<div id="post-33540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So I made it past the above when I ran basically all of the tweaks here:</p>
<p><a href="https://github.com/springmeyer/win-osm-workshop/blob/master/Tutorial.md#step-6-configure-the-osm-postgis-database">https://github.com/springmeyer/win-osm-workshop/blob/master/Tutorial.md#step-6-configure-the-osm-postgis-database</a></p>
<p>...now my osm data appears to load into my PostGIS database however now I'm stuck at a "key (id) = xxx...duplicate key value violates unique constraint..." error - anyone have any ideas?</p>
</div>
<div id="comment-33540-info" class="comment-info">
<span class="comment-age">(28 May '14, 20:59)</span> <span class="comment-user userinfo">aug_aug</span>
</div>
</div>
<span id="33543"></span>
<div id="comment-33543" class="comment">
<div id="post-33543-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I load stuff into PostgrSQL/PostGis on Windows all the time (both on XP SP3 and Windows 8.1). My main config is PostgreSQL 9.3 and PostGIS 2.x: you really need to give versions (and possibly dates) of all major components. Not sure that this help forum is place to solve what look like problems specific to your config.</p>
</div>
<div id="comment-33543-info" class="comment-info">
<span class="comment-age">(28 May '14, 21:48)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="33544"></span>
<div id="comment-33544" class="comment">
<div id="post-33544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In particular check this question: <a href="https://help.openstreetmap.org/questions/24070/failed-error-duplicate-key-value-violates-unique-constraint">https://help.openstreetmap.org/questions/24070/failed-error-duplicate-key-value-violates-unique-constraint</a></p>
</div>
<div id="comment-33544-info" class="comment-info">
<span class="comment-age">(28 May '14, 21:49)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33533" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33533-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

