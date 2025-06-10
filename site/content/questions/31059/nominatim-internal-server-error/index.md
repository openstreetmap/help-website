+++
type = "question"
title = "Nominatim internal server error"
description = '''I&#x27;m running Nominatim on my server and I recently (2 weeks ago) imported full planet data. I&#x27;m assuming the import is complete (not sure if it is, as the output never explicitly stated &quot;finished&quot;). Here&#x27;s my import output: Done 87399141 in 624893 @ 139.862564 per second - Rank 30 ETA (seconds): -30....'''
date = "2014-02-26T19:57:00Z"
lastmod = "2014-03-04T07:30:00Z"
weight = 31059
keywords = [ "nominatim", "reversegeocoding", "error" ]
aliases = [ "/questions/31059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim internal server error](/questions/31059/nominatim-internal-server-error)

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
<span id="post-31059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31059-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm running Nominatim on my server and I recently (2 weeks ago) imported full planet data. I'm assuming the import is complete (not sure if it is, as the output never explicitly stated "finished"). Here's my import output:</p>
<pre><code>Done 87399141 in 624893 @ 139.862564 per second - Rank 30 ETA (seconds): -30.558571
Done 87399213 in 624894 @ 139.862473 per second - ETA (seconds): -31.073381
Done 87399213 in 624894 @ 139.862473 per second - FINISHED
...
CREATE INDEX
CREATE INDEX
CREATE INDEX</code></pre>
<p>Postgres doesn't appear to be doing anything either:</p>
<pre><code>[root~]# psql postgres
psql (9.1.9)
Type &quot;help&quot; for help.
&#10;postgres=# select * from pg_stat_activity;
 datid | datname  | procpid | usesysid | usename | application_name | client_addr | client_hostname | client
_port |         backend_start         |          xact_start           |          query_start          | wait
ing |          current_query
-------+----------+---------+----------+---------+------------------+-------------+-----------------+-------
------+-------------------------------+-------------------------------+-------------------------------+-----
----+---------------------------------
 12780 | postgres |   31281 |    16385 | root    | psql             |             |                 |
   -1 | 2014-02-26 11:52:00.615982-08 | 2014-02-26 11:52:10.074218-08 | 2014-02-26 11:52:10.074218-08 | f
    | select * from pg_stat_activity;
(1 row)</code></pre>
<p>Having said that, I'm trying to reverse geocode via Nominatim, but it's giving me error messages:</p>
<p>Query:</p>
<pre><code>http://my-servers-ip-address/nominatim/reverse?format=xml&amp;lat=40.731389&amp;lon=-73.998889&amp;zoom=18&amp;addressdetails=1</code></pre>
<p>Output:</p>
<pre><code>Internal Server Error
Nominatim has encountered an internal error while processing your request. This is most likely because of a bug in the software.
Details: Could not determine closest place. Feel free to report the bug in the http://trac.openstreetmap.org OSM bug database. Please include the error message above and the URL you used.</code></pre>
<p>How can I debug to see what went wrong? Could the import have gone wrong? (Nominatim, the same installation on the same machine, was working fine before I wiped the database and imported new data) Is the import actually not finished?</p>
<p>Thanks</p>
<p><strong>EDIT:</strong></p>
<p>Adding apache error message and debug=1 option in the URL:</p>
<p>Apache error message:</p>
<pre><code>[Fri Feb 28 09:56:49 2014] [error] an unknown filter was not added: proxy-html
[Fri Feb 28 09:56:49 2014] [error] [client my-ip-address] PHP Fatal error:  Cannot use object of type DB_Error as array in /postgres/OpenStreetMaps/Nominatim-2.2.0/lib/PlaceLookup.php on line 53</code></pre>
<p>Output with debug=1 option:</p>
<pre><code>string(561) &quot;select place_id,parent_place_id,rank_search from placex WHERE ST_DWithin(ST_SetSRID(ST_Point(-73.998889,40.731389),4326), geometry, 0.0008) and rank_search != 28 and rank_search &gt;= 30 and (name is not null or housenumber is not null) and class not in (&#39;waterway&#39;,&#39;railway&#39;,&#39;tunnel&#39;,&#39;bridge&#39;) and indexed_status = 0  and (ST_GeometryType(geometry) not in (&#39;ST_Polygon&#39;,&#39;ST_MultiPolygon&#39;)  OR ST_DWithin(ST_SetSRID(ST_Point(-73.998889,40.731389),4326), centroid, 0.0008)) ORDER BY ST_distance(ST_SetSRID(ST_Point(-73.998889,40.731389),4326), geometry) ASC limit 1&quot;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '14, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '14, 18:06</strong> </span></p>
</div>
</div>
<div id="comments-container-31059" class="comments-container">
<span id="31064"></span>
<div id="comment-31064" class="comment">
<div id="post-31064-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you can, amend your question by adding the relevant messages of your Apache error log file. That will make answering easier.</p>
</div>
<div id="comment-31064-info" class="comment-info">
<span class="comment-age">(26 Feb '14, 21:30)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="31069"></span>
<div id="comment-31069" class="comment">
<div id="post-31069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I added the apache error message. I'm not sure what it's telling me to do though.</p>
</div>
<div id="comment-31069-info" class="comment-info">
<span class="comment-age">(26 Feb '14, 23:10)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="31072"></span>
<div id="comment-31072" class="comment">
<div id="post-31072-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it possible that you forgot to create the www-data user before starting the import?</p>
</div>
<div id="comment-31072-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 07:23)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="31124"></span>
<div id="comment-31124" class="comment">
<div id="post-31124-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, i created www-data user for my first import (this is my second import). I rechecked by running the command again, but no difference</p>
</div>
<div id="comment-31124-info" class="comment-info">
<span class="comment-age">(28 Feb '14, 17:45)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="31139"></span>
<div id="comment-31139" class="comment">
<div id="post-31139-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems that for whatever reason the database query caused PostGIS to return an error. Check your database log file in /var/log/postgresql/ if you spot an error; or else do "su www-data", then "psql nominatim", and enter the "select place_id..." query in the psql shell. With any luck that will also return an error, and give us a hint about what is wrong.</p>
</div>
<div id="comment-31139-info" class="comment-info">
<span class="comment-age">(01 Mar '14, 23:29)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="31242"></span>
<div id="comment-31242" class="comment not_top_scorer">
<div id="post-31242-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I typed in "su www-data" from shell and I get "user www-data does not exist". Could this be the problem? If i run the query in psql shell, the query runs and I get 0 rows. No error message (unless I need to look elsewhere for the error message).</p>
</div>
<div id="comment-31242-info" class="comment-info">
<span class="comment-age">(03 Mar '14, 23:10)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="31244"></span>
<div id="comment-31244" class="comment not_top_scorer">
<div id="post-31244-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Btw, I'm on CentOS.</p>
</div>
<div id="comment-31244-info" class="comment-info">
<span class="comment-age">(04 Mar '14, 00:02)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="31252"></span>
<div id="comment-31252" class="comment not_top_scorer">
<div id="post-31252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>CentOS seems to have user <em>apache</em> instead of <em>www-data</em>.</p>
</div>
<div id="comment-31252-info" class="comment-info">
<span class="comment-age">(04 Mar '14, 07:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31059" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-31059-form-container" class="comment-form-container">
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

<span id="31066"></span>

<div id="answer-container-31066" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31066-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To debug internal server errors, add <code>debug=1</code> as a parameter to your query. This will produce a lot of debug output which also includes the original SQL error message that is the cause of the internal error. There is a good chance that you simply have a permission problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '14, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-31066" class="comments-container">
<span id="31068"></span>
<div id="comment-31068" class="comment">
<div id="post-31068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I added the error message with the debug=1 option on. I could be wrong, but it doesn't appear to be permission problem.</p>
</div>
<div id="comment-31068-info" class="comment-info">
<span class="comment-age">(26 Feb '14, 23:09)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-31066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31066-form-container" class="comment-form-container">
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

