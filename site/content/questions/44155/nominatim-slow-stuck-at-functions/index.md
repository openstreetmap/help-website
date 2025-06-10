+++
type = "question"
title = "Nominatim slow - stuck at Functions"
description = '''Nominatim 2.4 install. /usr/bin/php -Cq ./utils/setup.php --osm-file /vol/north-america-latest.osm.pbf --all --osm2pgsql-cache 7000 It runs: /home/nominatim/Nominatim-2.4.0/nominatim/nominatim -i -d nominatim -P 5432 -t 3 -r 5 -R 25 Slow - been running 12 + hours and the log is not changing. Load is...'''
date = "2015-07-13T15:11:00Z"
lastmod = "2015-07-14T04:38:00Z"
weight = 44155
keywords = [ "nominatim" ]
aliases = [ "/questions/44155" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim slow - stuck at Functions](/questions/44155/nominatim-slow-stuck-at-functions)

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
<span id="post-44155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44155-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Nominatim 2.4 install.</p>
<p>/usr/bin/php -Cq ./utils/setup.php --osm-file /vol/north-america-latest.osm.pbf --all --osm2pgsql-cache 7000</p>
<p>It runs: /home/nominatim/Nominatim-2.4.0/nominatim/nominatim -i -d nominatim -P 5432 -t 3 -r 5 -R 25</p>
<p>Slow - been running 12 + hours and the log is not changing. Load is 3 cores on a 4 core box. Last log entry is Functions.</p>
<p>Node stats: total(783686820), max(3646699746) in 2396s</p>
<p>Way stats: total(51666293), max(360069395) in 4044s</p>
<p>Relation stats: total(460477), max(5360296) in 456s</p>
<p>Setting up table: planet_osm_nodes</p>
<p>Setting up table: planet_osm_ways</p>
<p>Setting up table: planet_osm_rels</p>
<p>Going over pending ways... 0 ways are pending</p>
<p>Using 1 helper-processes ^MFinished processing 0 ways in 0 sec</p>
<p>Going over pending relations... 0 relations are pending</p>
<p>Using 1 helper-processes</p>
<p>^MFinished processing 0 relations in 0 sec</p>
<p>Stopping table: planet_osm_nodes</p>
<p>Stopping table: planet_osm_rels</p>
<p>Building index on table: planet_osm_rels</p>
<p>Stopping table: planet_osm_ways</p>
<p>Stopped table: planet_osm_nodes in 0s</p>
<p>Stopped table: planet_osm_ways in 0s</p>
<p>Stopped table: planet_osm_rels in 12s</p>
<p>node cache: stored: 645470369(82.36%), storage efficiency: 70.35% (dense blocks: 557656, sparse nodes: 173232129), hit rate: 84.20%</p>
<p>Osm2pgsql took 6910s overall</p>
<p>Functions</p>
<p>Postgres activity:</p>
<p>nominatim | 20565 | idle | select place_id from placex where rank_search = $1 and geometry_sector = $2 and indexed_status &gt; 0</p>
<p>nominatim | 20374 | idle | insert into placex (osm_type, osm_id, class, type, name, admin_level, housenumber, street, addr_place, isin, postcode, country_code, extratags, geometry) select * from place where osm_id % 3 = 0</p>
<p>nominatim | 20375 | idle | insert into placex (osm_type, osm_id, class, type, name, admin_level, housenumber, street, addr_place, isin, postcode, country_code, extratags, geometry) select * from place where osm_id % 3 = 1</p>
<p>nominatim | 20376 | idle | INSERT INTO import_status VALUES('2015-07-11 18:13')</p>
<p>nominatim | 20566 | active | update placex set indexed_status = 0 where place_id = $1</p>
<p>nominatim | 20567 | active | update placex set indexed_status = 0 where place_id = $1</p>
<p>nominatim | 20568 | active | update placex set indexed_status = 0 where place_id = $1</p>
<p>postgres | 26833 | active | SELECT datname,pid,state,query FROM pg_stat_activity;</p>
<p>Why would there be 3 of these? And what is it trying to do?</p>
<p>update placex set indexed_status = 0 where place_id = $1</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '15, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/5797740ac3d3fbda6c642449847533b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Bell&#39;s gravatar image" />
<p><span>Bill Bell</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Bell has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '15, 18:54</strong> </span></p>
</div>
</div>
<div id="comments-container-44155" class="comments-container">
<span id="44157"></span>
<div id="comment-44157" class="comment">
<div id="post-44157-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here is relevant area of TOP. Going VERY slow.</p>
<p>top - 14:16:31 up 1 day, 7:29, 1 user, load average: 3.00, 3.01, 3.00 Tasks: 145 total, 6 running, 139 sleeping, 0 stopped, 0 zombie %Cpu(s): 75.3 us, 0.1 sy, 0.0 ni, 24.6 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st KiB Mem: 31416208 total, 31201488 used, 214720 free, 172412 buffers KiB Swap: 0 total, 0 used, 0 free. 29675768 cached Mem</p>
<p>20566 postgres 20 0 4498792 3.329g 3.286g R 99.8 11.1 585:09.61 postgres<br />
20567 postgres 20 0 4504124 3.328g 3.284g R 99.8 11.1 585:06.06 postgres<br />
20568 postgres 20 0 4503440 3.292g 3.249g R 99.8 11.0 585:08.31 postgres</p>
<p>A second apart - /vol is where postgres is. 16 bytes?</p>
<p>/dev/xvdb 769018760 145604728 584327092 20% /vol</p>
<p>/dev/xvdb 769018760 145604744 584327076 20% /vol</p>
</div>
<div id="comment-44157-info" class="comment-info">
<span class="comment-age">(13 Jul '15, 15:20)</span> <span class="comment-user userinfo">Bill Bell</span>
</div>
</div>
<span id="44168"></span>
<div id="comment-44168" class="comment">
<div id="post-44168-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was using nohup and it seems that PHP stops writing to the log file. I switches to screen and it appears to log now.</p>
<p>I am playing with the postgres config, to se right memory, and right now it is running.</p>
<p>To others: use screen! If it gets stuck restart with:</p>
<p>./utils/setup.php -v --create-functions --index --create-search-indices --osm2pgsql-cache 10000</p>
</div>
<div id="comment-44168-info" class="comment-info">
<span class="comment-age">(14 Jul '15, 04:37)</span> <span class="comment-user userinfo">Bill Bell</span>
</div>
</div>
<span id="44169"></span>
<div id="comment-44169" class="comment">
<div id="post-44169-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This also helps: <a href="http://pgtune.leopard.in.ua/">http://pgtune.leopard.in.ua/</a></p>
</div>
<div id="comment-44169-info" class="comment-info">
<span class="comment-age">(14 Jul '15, 04:38)</span> <span class="comment-user userinfo">Bill Bell</span>
</div>
</div>
</div>
<div id="comment-tools-44155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44155-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

