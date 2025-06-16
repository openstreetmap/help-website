+++
type = "question"
title = "Osmosis Replication"
description = '''I&#x27;ve managed to setup both locally tile_server and API on rails-port. Their dbs are populated with local copy of maps. Im able to preview tiles and download rawdata from API using JOSM. When im uploading changes back to API server i cannot see the changes on tiles, which is ok because they have sepe...'''
date = "2016-06-01T15:44:00Z"
lastmod = "2016-09-12T08:21:00Z"
weight = 49958
keywords = [ "replication", "api", "osmosis", "railsport" ]
aliases = [ "/questions/49958" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis Replication](/questions/49958/osmosis-replication)

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
<span id="post-49958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49958-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've managed to setup both locally tile_server and API on rails-port. Their dbs are populated with local copy of maps. Im able to preview tiles and download rawdata from API using JOSM. When im uploading changes back to API server i cannot see the changes on tiles, which is ok because they have seperate databases.</p>
<p>I assume replication is needed.</p>
<p>I've gone through <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Replication">https://wiki.openstreetmap.org/wiki/Osmosis/Replication</a> and <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.43">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.43</a></p>
<p>Right now im a bit stuck because, when i tried to use</p>
<p>osmosis --replicate-apidb</p>
<p>I ended up with new folder called replicate which has state.txt replicate.lock files and 000 folder and inside this folder i have 001.state.txt and 001.osc.gz</p>
<p>but it appears that there is no data, like if there were no changes at all.</p>
<p>i've also tried osmosis -q --replicate-apidb iterations=0 minInterval=10000 maxInterval=60000 authFile=dbAuth.txt --send-replication-sequence port=8081 --write-replication workingDirectory=data</p>
<p>but here i end up with error message: Task type write-replication doesn't exist.</p>
<p>It seems that im missing some steps but i have no clue where to look.</p>
<p>Right now i want just to update my tile_server db with my recent change, but when this works i would like to set osmosis to do it automatically every hour or minute, so that i dont bother anymore with console.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-replication" rel="tag" title="see questions tagged &#39;replication&#39;">replication</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '16, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/016ab1463a1f9187246270165f1a0a25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorax&#39;s gravatar image" />
<p><span>jorax</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorax has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49958" class="comments-container">
<span id="49971"></span>
<div id="comment-49971" class="comment">
<div id="post-49971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Today i tried to make one-off data migration.</p>
<p>osmosis --read-apidb-change authFile=Auth.txt validateSchemaVersion=no intervalBegin="2016-05-29_00:00:00" --write-xml-change</p>
<p>THis produced change.osc with the data i want so big success</p>
<p>Now something is wrong with db:</p>
<p>osmosis --read-xml-change --write-pgsql-change authfile=Auth.txt validateSchemaVersion=no</p>
<p>this results in error:</p>
<p>org.springframework.jdbc.BadSqlGrammarException: PreparedStatementCallback; bad SQL grammar [SELECT id, name FROM users WHERE id = ?]; nested exception is org.postgresql.util.PSQLException: ERROR: relation "users" does not exist</p>
<p>So i tried osm2pgsql</p>
<p>osm2pgsql -l --append --database gis --username root --slim --cache 2048 change.osc</p>
<p>This ends up with another error:</p>
<p>Osm2pgsql failed due to ERROR: result COPY_END for planet_osm_polygon failed: ERROR: Geometry SRID (4326) does not match column SRID (900913) CONTEXT: COPY planet_osm_polygon, line 1, column way: "SRID=4326;POLYGON ((9.6640657999999995 53.5647483999999992, 9.6643272000000007 53.5649425000000008, ..."</p>
</div>
<div id="comment-49971-info" class="comment-info">
<span class="comment-age">(02 Jun '16, 09:31)</span> <span class="comment-user userinfo">jorax</span>
</div>
</div>
<span id="49982"></span>
<div id="comment-49982" class="comment">
<div id="post-49982-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok above comment is almost ok, problem was with flag -l. After removing this flag, i managed to import change.osc file. But still this is a manual process. My goal is to have this automatically.</p>
</div>
<div id="comment-49982-info" class="comment-info">
<span class="comment-age">(03 Jun '16, 09:08)</span> <span class="comment-user userinfo">jorax</span>
</div>
</div>
<span id="51996"></span>
<div id="comment-51996" class="comment">
<div id="post-51996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you success to set the osmosis replication task automatically? Can you tell me how to make it automatically?</p>
</div>
<div id="comment-51996-info" class="comment-info">
<span class="comment-age">(12 Sep '16, 08:21)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-49958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49958-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

