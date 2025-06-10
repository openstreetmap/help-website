+++
type = "question"
title = "Osmosis PostgreSQL error"
description = '''A week ago, I used Osmosis to import osc files into PostgreSQL with this code: osmosis --rxc source&#92;osc&#92;xyz.osc --wpc database=gps user=myuser password=mypassword  All went well, and today I tried to run this code with a different osc file, and it failed with this error message: ... SEVERE: Thread f...'''
date = "2017-09-13T17:14:00Z"
lastmod = "2017-09-28T12:09:00Z"
weight = 59610
keywords = [ "openstreetmap", "postgresql", "osm", "postgis", "osmosis" ]
aliases = [ "/questions/59610" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis PostgreSQL error](/questions/59610/osmosis-postgresql-error)

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
<span id="post-59610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59610-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A week ago, I used Osmosis to import osc files into PostgreSQL with this code:</p>
<pre><code>osmosis --rxc source\osc\xyz.osc --wpc database=gps user=myuser password=mypassword</code></pre>
<p>All went well, and today I tried to run this code with a different osc file, and it failed with this error message:</p>
<p>...</p>
<p>SEVERE: Thread for task 1-rxc failed org.springframework.jdbc.BadSqlGrammarException: PreparedStatementCallback; bad SQL grammar [INSERT INTO nodes(id, version, user_id, tstamp, changeset_id, tags, geom) VALUES (?, ?, ?, ?, ?, ?, ?)]; nested exception is org.postgresql.util.PSQLException: Can't infer the SQL type to use for an instance of java.util.HashMap. Use setObject() with an explicit Types value to specify the type to use.</p>
<p>...</p>
<p>Can you help solve this? I have a pgsnapshot schema with the linestring.sql, Osmosis version is 0.45, PostgreSQL version is 9.5.6, PostGIS version: 2.3.3</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '17, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/bd59a1956b8ee779ec94d29e78596b72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="horvatha&#39;s gravatar image" />
<p><span>horvatha</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="horvatha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59610" class="comments-container">
<span id="59856"></span>
<div id="comment-59856" class="comment">
<div id="post-59856-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i have the same exact error and its driving me crazy!! i wish i can help you but i also posted this question. If i get an answer myself i will be sure to share it with you! Im curious though, you were able to get it work once for you, then now it doesnt work? From the very first time i tried to apply a change file i started receiving this error. The only difference with error is the sql query. Mine is this</p>
<p>[UPDATE nodes SET id = ?, version = ?, user_id = ?, tstamp = ?, changeset_id = ?, tags = ?, geom = ? WHERE id = ?]</p>
</div>
<div id="comment-59856-info" class="comment-info">
<span class="comment-age">(26 Sep '17, 20:07)</span> <span class="comment-user userinfo">Asinger321</span>
</div>
</div>
<span id="59866"></span>
<div id="comment-59866" class="comment">
<div id="post-59866-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I installed osmosis 0.40.1 with apt install osmosis and now it works. Installed the pgsnapshot_schema.sql and linestring.sql (version 0.6). No more error messages. Hope it will work for you, too!</p>
</div>
<div id="comment-59866-info" class="comment-info">
<span class="comment-age">(28 Sep '17, 12:09)</span> <span class="comment-user userinfo">horvatha</span>
</div>
</div>
</div>
<div id="comment-tools-59610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59610-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

