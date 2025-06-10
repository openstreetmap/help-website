+++
type = "question"
title = "Nominatim PgSQL database size growing gradually"
description = '''Hi, We have installed Nominatim 2.2.0 on centos We have uploaded&#92;imported Netherlands Map. and initiated daily Auto updates using command  &quot;/utils/update.php --import-osmosis-all --no-npi&quot;  Now, every day Postgres database size growing rapidly , even though only imported NL maps.  How can I decrease...'''
date = "2014-08-05T14:29:00Z"
lastmod = "2016-07-29T12:34:00Z"
weight = 35529
keywords = [ "database", "nominatim", "size" ]
aliases = [ "/questions/35529" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim PgSQL database size growing gradually](/questions/35529/nominatim-pgsql-database-size-growing-gradually)

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
<span id="post-35529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35529-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>We have installed Nominatim 2.2.0 on centos</p>
<p>We have uploaded\imported Netherlands Map.</p>
<p>and initiated daily Auto updates using command</p>
<pre><code>&quot;/utils/update.php --import-osmosis-all --no-npi&quot;</code></pre>
<p>Now, every day Postgres database size growing rapidly , even though only imported NL maps.</p>
<p>How can I decrease or limit the size of Nominatim database to not growing gradually.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '14, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/374a88555372b3ec6b7e5accef89b9f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PrakashThakor&#39;s gravatar image" />
<p><span>PrakashThakor</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PrakashThakor has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '14, 14:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-35529" class="comments-container">
<span id="35544"></span>
<div id="comment-35544" class="comment">
<div id="post-35544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What version of PG is this ? Did you leave the autovacuum settings at their default ? Does <a href="http://bucardo.org/wiki/Check_postgres">check_postgres.pl</a> --action=bloat --db=nominatim show a lot of bloat ?</p>
</div>
<div id="comment-35544-info" class="comment-info">
<span class="comment-age">(05 Aug '14, 17:39)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="35656"></span>
<div id="comment-35656" class="comment">
<div id="post-35656-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Vincent,</p>
<ol>
<li>I have PGSQL 9.3</li>
<li>Yes , I did not change in autovaccum settings and its default.</li>
<li>"check_postgres.pl --action=bloat --db=nominatim" shown following result</li>
</ol>
<h2 id="rootnominatim-ams-check_postgres-2.21.0-.check_postgres.pl---actionbloat--dbnominatim-postgres_bloat-critical-db-nominatim-db-nominatim-index-planet_osm_ways_nodes-rows-pages1737024-shouldbe502394-3.5x-wasted-bytes10114088960-9-gb-planet_osm_ways_nodes10114088960b-public.place_addressline1059995648b-idx_search_name_nameaddress_vector1001832448b-idx_placex_pendingsector114614272b-public.search_name110084096b-public.location_area_large_11745719552b-public.placex7045120b-idx_location_area_large_117_geometry1089536b-idx_location_area_large_117_place_id0b-idx_place_addressline_address_place_id0b-idx_place_addressline_place_id0b-idx_search_name_centroid0b-idx_search_name_name_vector0b-idx_search_name_place_id0b-public.planet_osm_ways0b">[root@nominatim-ams check_postgres-2.21.0]# ./check_postgres.pl --action=bloat -db=nominatim POSTGRES_BLOAT CRITICAL: DB "nominatim" (db nominatim) index planet_osm_ways_nodes rows:? pages:1737024 shouldbe:502394 (3.5X) wasted bytes:10114088960 (9 GB) | planet_osm_ways_nodes=10114088960B public.place_addressline=1059995648B idx_search_name_nameaddress_vector=1001832448B idx_placex_pendingsector=114614272B public.search_name=110084096B public.location_area_large_117=45719552B public.placex=7045120B idx_location_area_large_117_geometry=1089536B idx_location_area_large_117_place_id=0B idx_place_addressline_address_place_id=0B idx_place_addressline_place_id=0B idx_search_name_centroid=0B idx_search_name_name_vector=0B idx_search_name_place_id=0B public.planet_osm_ways=0B</h2>
</div>
<div id="comment-35656-info" class="comment-info">
<span class="comment-age">(09 Aug '14, 11:07)</span> <span class="comment-user userinfo">PrakashThakor</span>
</div>
</div>
<span id="51167"></span>
<div id="comment-51167" class="comment">
<div id="post-51167-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was able to reduce the bloating by reindexing the affected tables, first I ran above check_postgres script to find out which tables/indexes exactly where affected:</p>
<ul>
<li>POSTGRES_BLOAT CRITICAL: DB "nominatim" (db nominatim) index idx_search_name_nameaddress_vector rows:? pages:5571228 shouldbe:1788574 (3.1X) wasted bytes:30987501568 (28 GB) * (db nominatim) table public.place_addressline rows:299672640 pages:3052511 shouldbe:2200240 (1.4X) wasted size:6981804032 (6 GB) | [...]</li>
</ul>
<p>and then ran the following commands:</p>
<ul>
<li>psql nominatim -c "reindex index idx_search_name_nameaddress_vector;"</li>
<li>psql nominatim -c "reindex table public.place_addressline;"</li>
</ul>
<p>Freed up a lot of space</p>
</div>
<div id="comment-51167-info" class="comment-info">
<span class="comment-age">(29 Jul '16, 12:34)</span> <span class="comment-user userinfo">jot</span>
</div>
</div>
</div>
<div id="comment-tools-35529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35529-form-container" class="comment-form-container">
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

<span id="35657"></span>

<div id="answer-container-35657" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35657-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-35657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you updating from the global minutely diffs? If yes, while I don't know the exact workings of nominatim, this will cause additional objects to be added outside of the area of your original extract.</p>
<p>There are numerous ways around this problem, one is to consume diffs that are specific to your region as, for example, provided by GeoFabrik <a href="http://download.geofabrik.de/europe/netherlands-updates/">http://download.geofabrik.de/europe/netherlands-updates/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '14, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '14, 12:31</strong> </span></p>
</div>
</div>
<div id="comments-container-35657" class="comments-container">
<span id="35660"></span>
<div id="comment-35660" class="comment">
<div id="post-35660-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi SimonPools,</p>
<p>Mostly I kept default setting of Nominatim , should I change replication URL to <a href="http://download.geofabrik.de/europe/netherlands-updates/">http://download.geofabrik.de/europe/netherlands-updates/</a></p>
<p>//Replication settings</p>
<p>@define('CONST_Replication_Url', 'http://planet.openstreetmap.org/replication/minute');</p>
<pre><code>    @define(&#39;CONST_Replication_MaxInterval&#39;, &#39;40000&#39;);
&#10;    @define(&#39;CONST_Replication_Update_Interval&#39;, &#39;172800&#39;);  // How often upstream publishes diffs
&#10;    @define(&#39;CONST_Replication_Recheck_Interval&#39;, &#39;900&#39;); // How long to sleep if no update found yet</code></pre>
</div>
<div id="comment-35660-info" class="comment-info">
<span class="comment-age">(09 Aug '14, 12:52)</span> <span class="comment-user userinfo">PrakashThakor</span>
</div>
</div>
<span id="35661"></span>
<div id="comment-35661" class="comment">
<div id="post-35661-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, you should change the URL. You might also want to redo your import from scratch to get rid of the unwanted world data.</p>
</div>
<div id="comment-35661-info" class="comment-info">
<span class="comment-age">(09 Aug '14, 14:31)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="35662"></span>
<div id="comment-35662" class="comment">
<div id="post-35662-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Vincent,</p>
<p>But I did initial import of only Netherland maps using netherlands-latest.osm.pbf and not the entire planet maps , AS we only required Netherlands Maps.</p>
<p>Do I need to still import from scratch.</p>
</div>
<div id="comment-35662-info" class="comment-info">
<span class="comment-age">(09 Aug '14, 14:38)</span> <span class="comment-user userinfo">PrakashThakor</span>
</div>
</div>
<span id="35664"></span>
<div id="comment-35664" class="comment">
<div id="post-35664-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Consuming worldwide diffs adds worldwide data to your db, regardless of what region the initial db contained. That's certainly what causes the rapid db growth.</p>
<p>You don't <em>have</em> to remove that data, but it's probably a good idea.</p>
</div>
<div id="comment-35664-info" class="comment-info">
<span class="comment-age">(09 Aug '14, 14:49)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35657-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35663"></span>

<div id="answer-container-35663" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35663-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As SimonPoole says, making sure you get only the local diffs is the most important step. That said, it's strange that you got all the way to a 9G/3.5x bloat. Check that <a href="http://www.postgresql.org/docs/current/static/routine-vacuuming.html">autovacuum</a> is working as expected :</p>
<pre><code>psql nominatim -c &quot;select relname,last_autovacuum from pg_stat_user_tables;&quot;</code></pre>
<p>You should see recent-ish dates for your updated tables. Check your logs for errors if not.</p>
<p>It's often a good idea to set your vacuuming more aggressively in postgresql.conf:</p>
<pre><code>autovacuum_vacuum_threshold = 5000
autovacuum_analyze_threshold = 5000
autovacuum_vacuum_scale_factor = 0.02
autovacuum_analyze_scale_factor = 0.01
autovacuum_vacuum_cost_delay = 10ms</code></pre>
<p>Also, at any time you can issue a manual full vacuum to regain space (note that some % of bloat is normal, and that doing a "full" vacuum will block other db queries) :</p>
<pre><code>vacuumdb -fz nominatim</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '14, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-35663" class="comments-container">
<span id="35665"></span>
<div id="comment-35665" class="comment">
<div id="post-35665-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Vincent I just ran query to find most space consuming tables on Nominatim db.</p>
<p>and found tables consumes most of the space in Indexing</p>
<p>for example plane_osm_ways occupies 14 GB of index</p>
<hr />
<p>Table Name ; Table_size ; Indexs_size, Total Size</p>
<hr />
<p>""public"."planet_osm_ways"";"4914 MB";"14 GB";"19 GB"</p>
<p>""public"."planet_osm_nodes"";"10 GB";"5773 MB";"16 GB"</p>
<p>""public"."placex"";"5609 MB";"10 GB";"16 GB"</p>
<p>""public"."place"";"5416 MB";"2152 MB";"7568 MB"</p>
<p>""public"."place_addressline"";"3687 MB";"3512 MB";"7200 MB"</p>
<p>""public"."new_query_log"";"6537 MB";"341 MB";"6879 MB"</p>
</div>
<div id="comment-35665-info" class="comment-info">
<span class="comment-age">(09 Aug '14, 15:03)</span> <span class="comment-user userinfo">PrakashThakor</span>
</div>
</div>
</div>
<div id="comment-tools-35663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35663-form-container" class="comment-form-container">
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

