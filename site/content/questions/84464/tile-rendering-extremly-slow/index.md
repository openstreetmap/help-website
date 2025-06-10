+++
type = "question"
title = "Tile rendering extremly slow"
description = '''I imported the planet and tried to zoom on New York as an exmple. It took like 5 Minutes to load tiles. Examples of a tile loading time at zoom 12: Queued at 42.90 s Started at 42.91 s Resource Scheduling  Queueing 1.79 ms Connection Start  Stalled 15.61 s Request/Response  Request sent 80 μs Waitin...'''
date = "2022-05-13T13:47:00Z"
lastmod = "2022-05-16T08:16:00Z"
weight = 84464
keywords = [ "rendering", "renderd", "postgresql", "osm2pgsql", "tileserver" ]
aliases = [ "/questions/84464" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tile rendering extremly slow](/questions/84464/tile-rendering-extremly-slow)

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
<span id="post-84464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84464-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I imported the planet and tried to zoom on New York as an exmple. It took like 5 Minutes to load tiles.</p>
<p><strong>Examples of a tile loading time at zoom 12:</strong></p>
<pre><code>Queued at 42.90 s
Started at 42.91 s
Resource Scheduling     
Queueing 1.79 ms
Connection Start        
Stalled 15.61 s
Request/Response        
Request sent    80 μs
Waiting (TTFB) 119.53 ms
Content Download 1.50 ms
Total       15.73 s
&#10;Queued at 42.90 s
Started at 42.90 s
Resource Scheduling     
Queueing 1.44 ms
Connection Start        
Stalled 3.86 ms
DNS Lookup 23 μs
Initial connection 28.44 ms
Request/Response        
Request sent 42 μs
Waiting (TTFB) 15.42 s
Content Download 1.17 ms
Total       15.46 s</code></pre>
<p>Stalled and Waiting (TTFB) are always almost 90% of loading time !</p>
<p><strong>Machine specs:</strong></p>
<pre><code>128GB Ram
16 Cores</code></pre>
<p>I used the openstreetmap carto style .</p>
<p><strong>My import command:</strong></p>
<pre><code>docker run -v /home/admin_akanea/planet-latest.osm.pbf:/data/region.osm.pbf -v osm-data:/data/database/ -v osm-tiles:/data/tiles/ -e &quot;FLAT_NODES=enabled&quot; overv/openstreetmap-tile-server import</code></pre>
<p><strong>My run commande:</strong></p>
<pre><code>docker run --restart=always -p 80:80 -p 443:443 -e THREADS=8 -e &quot;OSM2PGSQL_EXTRA_ARGS=-C 16107&quot; --shm-size=&quot;2GB&quot; -v /var/www/html/gis-frontend:/var/www/html -v osm-data:/data/database/ -v osm-tiles:/data/tiles/ -d overv/openstreetmap-tile-server run</code></pre>
<p><strong>My render command:</strong></p>
<pre><code>sudo -u renderer renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p><strong>My renderd.conf:</strong></p>
<pre><code>[renderd]
num_threads=8
tile_dir=/var/lib/mod_tile
stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input
font_dir=/usr/share/fonts
font_dir_recurse=1
&#10;[ajt]
URI=/tile/
TILEDIR=/var/lib/mod_tile
XML=/home/renderer/src/openstreetmap-carto/mapnik.xml
HOST=localhost
TILESIZE=256
MAXZOOM=20</code></pre>
<p><strong>My Apache conf:</strong></p>
<pre><code>&lt;VirtualHost *:80&gt;
&#10;ServerAdmin admin@admin.com
&#10;LoadTileConfigFile /usr/local/etc/renderd.conf
ModTileRenderdSocketName /var/run/renderd/renderd.sock
ModTileRequestTimeout 500
ModTileMissingRequestTimeout 500
ModTileMaxLoadMissing 50
&#10;DocumentRoot /var/www/html/live
Alias /beta /var/www/html/beta
Alias /pilot /var/www/html/pilot
&#10;LogLevel info
ErrorLog /var/log/apache2/error_http_osm.log
CustomLog /var/log/apache2/access_http_osm.log combined
&#10;&lt;IfDefine ALLOW_CORS&gt;
    Header set Access-Control-Allow-Origin &quot;*&quot;
&lt;/IfDefine&gt;
&#10;#RewriteEngine On
#RewriteCond %{HTTPS} off
#RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}
&lt;/VirtualHost&gt;</code></pre>
<p><strong>My Postgres conf:</strong></p>
<pre><code>max_connections = 500
shared_buffers = 32GB
temp_buffers = 8GB
work_mem = 2GB
maintenance_work_mem = 5GB
effective_io_concurrency = 1000
max_worker_processes = 8
max_parallel_workers_per_gather = 4
max_parallel_workers = 8
max_parallel_maintenance_workers = 2
fsync off
synchronous_commit off
wal_buffers = -1
checkpoint_completion_target = 0.9
min_wal_size = 50GB
max_wal_size = 5GB
random_page_cost = 1.1
effective_cache_size = 96GB
default_statistics_target = 100
autovacuum = on</code></pre>
<p><strong>Postgres indexes list:</strong></p>
<pre><code>    SELECT
      schema_name,
      relname,
      pg_size_pretty(table_size) AS size,
      table_size
    FROM (
           SELECT
             pg_catalog.pg_namespace.nspname           AS schema_name,
             relname,
             pg_relation_size(pg_catalog.pg_class.oid) AS table_size
           FROM pg_catalog.pg_class
             JOIN pg_catalog.pg_namespace ON relnamespace = pg_catalog.pg_namespace.oid
         ) t
    WHERE schema_name NOT LIKE &#39;pg_%&#39;
    ORDER BY table_size DESC;
    schema_name     |                   relname                   |    size    |  table_size
--------------------+---------------------------------------------+------------+--------------
 public             | planet_osm_polygon                          | 151 GB     | 162362638336
 public             | planet_osm_polygon_way_idx                  | 84 GB      |  90535403520
 public             | planet_osm_line                             | 82 GB      |  87825956864
 public             | planet_osm_line_way_idx                     | 33 GB      |  35687972864
 public             | planet_osm_point                            | 24 GB      |  25987817472
 public             | planet_osm_polygon_nobuilding               | 13 GB      |  13502365696
 public             | planet_osm_polygon_osm_id_idx               | 12 GB      |  13105840128
 public             | planet_osm_point_way_idx                    | 9109 MB    |   9551224832
 public             | planet_osm_roads                            | 8650 MB    |   9070534656
 public             | idx_poly_text_poly                          | 8309 MB    |   8712740864
 public             | planet_osm_line_label                       | 7751 MB    |   8127275008
 public             | idx_line_name                               | 7377 MB    |   7735803904
 public             | planet_osm_line_name                        | 7346 MB    |   7702609920
 public             | planet_osm_line_osm_id_idx                  | 5354 MB    |   5614149632
 public             | idx_poly_idlanduse                          | 4732 MB    |   4961574912
 public             | planet_osm_polygon_way_area_z10             | 4469 MB    |   4686422016
 public             | planet_osm_point_osm_id_idx                 | 3692 MB    |   3871670272
 public             | planet_osm_roads_way_idx                    | 1748 MB    |   1833238528
 public             | idx_line_ref                                | 1476 MB    |   1547665408
 public             | idx_line_waterway                           | 1420 MB    |   1489387520
 public             | planet_osm_line_waterway                    | 1402 MB    |   1470603264
 public             | idx_point_power                             | 1267 MB    |   1328185344
 public             | idx_point_natural                           | 1036 MB    |   1086332928
 public             | idx_point_highway                           | 962 MB     |   1008328704
 public             | planet_osm_polygon_water                    | 852 MB     |    893165568
 public             | planet_osm_polygon_name                     | 692 MB     |    725213184
 public             | idx_line_access                             | 631 MB     |    661463040
 public             | idx_point_amenity                           | 617 MB     |    646799360
 public             | idx_poly_wayarea_text                       | 612 MB     |    642195456
 public             | idx_poly_amenity                            | 521 MB     |    546209792
 public             | planet_osm_roads_roads_ref                  | 360 MB     |    377847808
 public             | planet_osm_roads_osm_id_idx                 | 330 MB     |    345915392
 public             | idx_point_place                             | 321 MB     |    336666624
 public             | idx_point_barrier                           | 310 MB     |    325574656
 public             | idx_line_bridge                             | 297 MB     |    311795712
 public             | planet_osm_point_place                      | 296 MB     |    309960704
 public             | idx_point_shop                              | 212 MB     |    222355456
 public             | idx_line_tunnel                             | 193 MB     |    202244096
 public             | idx_line_railway                            | 179 MB     |    187981824
 public             | planet_osm_roads_admin                      | 175 MB     |    183640064
 public             | planet_osm_polygon_way_area_z6              | 171 MB     |    179650560
 public             | idx_point_railway                           | 143 MB     |    150208512
 public             | idx_point_man_made                          | 128 MB     |    134463488
 public             | idx_point_tourism                           | 115 MB     |    120553472
 public             | idx_line_power                              | 95 MB      |    100032512
 public             | planet_osm_line_river                       | 85 MB      |     89628672
 public             | icesheet_outlines                           | 69 MB      |     72638464
 public             | idx_point_historic                          | 52 MB      |     54231040
 public             | idx_point_leisure                           | 46 MB      |     48545792
 public             | idx_poly_barrier                            | 42 MB      |     43565056
 public             | idx_line_cutline                            | 15 MB      |     15392768
 public             | icesheet_polygons                           | 13 MB      |     13524992
 public             | idx_point_waterway                          | 12 MB      |     12468224
 public             | simplified_water_polygons                   | 10 MB      |     10567680
 public             | planet_osm_roads_admin_low                  | 10 MB      |     10518528
 public             | idx_poly_aeroway                            | 8920 kB    |      9134080
 public             | water_polygons                              | 8328 kB    |      8527872
 public             | idx_point_aeroway                           | 8024 kB    |      8216576
 public             | idx_point_aerialway                         | 7800 kB    |      7987200
 public             | idx_point_landuse                           | 7048 kB    |      7217152
 public             | spatial_ref_sys                             | 6936 kB    |      7102464
 public             | icesheet_outlines_way_idx                   | 3744 kB    |      3833856
 public             | planet_osm_polygon_military                 | 3216 kB    |      3293184
 public             | idx_point_military                          | 2480 kB    |      2539520
 public             | ferry_idx                                   | 2008 kB    |      2056192
 public             | planet_osm_line_ferry                       | 1744 kB    |      1785856
 public             | idx_line_aerialway                          | 1608 kB    |      1646592
 public             | icesheet_polygons_way_idx                   | 784 kB     |       802816
 public             | water_polygons_way_idx                      | 696 kB     |       712704
 public             | simplified_water_polygons_way_idx           | 664 kB     |       679936
 public             | spatial_ref_sys_pkey                        | 304 kB     |       311296
 public             | idx_poly_aerialway                          | 232 kB     |       237568
 public             | planet_osm_polygon_admin                    | 224 kB     |       229376
 public             | ne_110m_admin_0_boundary_lines_land         | 96 kB      |        98304
 information_schema | sql_features                                | 64 kB      |        65536</code></pre>
<p><em>planet_osm_line_way_idx</em> and <em>planet_osm_polygon_way_idx</em> are present on top of all the indices mentioned on the OSM github documentation.</p>
<p><strong>Postgres used indices</strong></p>
<pre><code>SELECT relname, indexrelname, idx_scan, idx_tup_read, idx_tup_fetch FROM pg_stat_all_indexes WHERE
   schemaname = &#39;public&#39;;
    relname         |                indexrelname    | idx_scan | idx_tup_read | idx_tup_fetch
--------------------+--------------------------------+----------+--------------+--------------
 spatial_ref_sys    | spatial_ref_sys_pkey           |        0 |            0 |             0
 planet_osm_roads   | planet_osm_roads_way_idx       |       15 |      2138301 |         29584
 planet_osm_roads   | planet_osm_roads_osm_id_idx    |       18 |     18174150 |             0
 planet_osm_roads   | planet_osm_roads_admin         |      288 |       882471 |        400284
 planet_osm_roads   | planet_osm_roads_admin_low     |        6 |        16986 |         16986
 planet_osm_roads   | planet_osm_roads_roads_ref     |       22 |       528508 |        308310
 external_data      | external_data_pkey             |        0 |            0 |             0
 planet_osm_point   | planet_osm_point_osm_id_idx    |        0 |            0 |             0
 planet_osm_point   | planet_osm_point_place         |      199 |      1487141 |       1487141
 planet_osm_point   | idx_point_aerialway            |       68 |        13617 |             0
 planet_osm_point   | idx_point_aeroway              |        0 |            0 |             0
 planet_osm_point   | idx_point_amenity              |       66 |        61187 |             0
 planet_osm_point   | idx_point_barrier              |       66 |        28584 |             0
 planet_osm_point   | idx_point_highway              |       84 |        61419 |         61419
 planet_osm_point   | idx_point_historic             |       66 |         1184 |             0
 planet_osm_point   | idx_point_landuse              |        0 |            0 |             0
 planet_osm_point   | idx_point_leisure              |        0 |            0 |             0
 planet_osm_point   | idx_point_lock                 |        0 |            0 |             0
 planet_osm_point   | idx_point_man_made             |       66 |         7185 |             0
 planet_osm_point   | idx_point_military             |        0 |            0 |             0
 planet_osm_point   | idx_point_natural              |       28 |        22390 |         22390
 planet_osm_point   | idx_point_place                |       17 |          815 |           815
 planet_osm_point   | idx_point_power                |       47 |        10545 |         10545
 planet_osm_point   | idx_point_railway              |      202 |        70737 |             0
 planet_osm_point   | idx_point_shop                 |        0 |            0 |             0
 planet_osm_point   | idx_point_tourism              |        0 |            0 |             0
 planet_osm_point   | idx_point_waterway             |       19 |            8 |             8
 planet_osm_point   | planet_osm_point_way_idx       |      282 |     40882004 |      12771340
 icesheet_polygons  | icesheet_polygons_way_idx      |      103 |            2 |             2
 planet_osm_line    | planet_osm_line_way_idx        |     3747 |     52539025 |      21471779
 planet_osm_line    | planet_osm_line_osm_id_idx     |        0 |            0 |             0
 planet_osm_line    | planet_osm_line_ferry          |      160 |         2100 |          2100
 planet_osm_line    | planet_osm_line_label          |       37 |        44611 |         44611
 planet_osm_line    | planet_osm_line_river          |       29 |       138888 |        138888
 planet_osm_line    | planet_osm_line_waterway       |       89 |        69436 |         69436
 planet_osm_line    | idx_line_ref                   |      101 |       127452 |        127452
 planet_osm_line    | idx_line_tunnel                |        0 |            0 |             0
 planet_osm_line    | idx_line_waterway              |       93 |        40684 |         40684
 planet_osm_line    | ferry_idx                      |        0 |            0 |             0
 planet_osm_line    | idx_line_access                |        0 |            0 |             0
 planet_osm_line    | idx_line_aerialway             |        0 |            0 |             0
 planet_osm_line    | idx_line_bridge                |      151 |       343569 |        343569
 planet_osm_line    | idx_line_cutline               |       47 |            1 |             1
 planet_osm_line    | idx_line_name                  |        0 |            0 |             0
 planet_osm_line    | idx_line_power                 |       75 |         1888 |          1888
 planet_osm_line    | idx_line_railway               |      403 |       961742 |        780485
 planet_osm_line    | planet_osm_line_name           |       64 |       379879 |        379879
 water_polygons     | water_polygons_way_idx         |       87 |          195 |           195
 icesheet_outlines  | icesheet_outlines_way_idx      |      103 |            8 |             8
 planet_osm_polygon | planet_osm_polygon_way_idx     |      920 |    168508409 |      76768381
 planet_osm_polygon | planet_osm_polygon_osm_id_idx  |      440 |          440 |             0
 planet_osm_polygon | planet_osm_polygon_admin       |      204 |          704 |           704
 planet_osm_polygon | planet_osm_polygon_military    |       96 |         3816 |          3816
 planet_osm_polygon | planet_osm_polygon_name        |      264 |      3867380 |       3867380
 planet_osm_polygon | planet_osm_polygon_nobuilding  |       76 |      1963628 |        798344
 planet_osm_polygon | planet_osm_polygon_water       |      100 |      1222659 |        796849
 planet_osm_polygon | planet_osm_polygon_way_area_z10|       89 |      7167601 |        514467
 planet_osm_polygon | planet_osm_polygon_way_area_z6 |       42 |        80558 |         29574
 planet_osm_polygon | idx_poly_idlanduse             |       47 |        96564 |         96564
 planet_osm_polygon | idx_poly_wayarea_text          |        0 |            0 |             0
 planet_osm_polygon | idx_poly_text_poly             |      175 |     12853588 |       2815848
 planet_osm_polygon | idx_poly_aerialway             |        0 |            0 |             0
 planet_osm_polygon | idx_poly_aeroway               |        0 |            0 |             0
 planet_osm_polygon | idx_poly_amenity               |        0 |            0 |             0</code></pre>
<p>The last two columns are interesting : <em>idx_tup_read</em> and <em>idx_tup_fetch</em>. Especially <em>idx_tup_fetch</em> counts how many rows are returned directly from the index without scanning the table itselt. We can see that <em>planet_osm_line_way_idx</em> and <em>planet_osm_polygon_way_idx</em> are well used.</p>
<p><strong>Postgres explain analyze requests:</strong></p>
<pre><code>explain analyze SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;name&quot;,&quot;way_area&quot; FROM (select way,way_area,name
from planet_osm_polygon
where name is not null
and (waterway is null or waterway != &#39;riverbank&#39;)
and place is null
order by way_area desc
) as text WHERE &quot;way&quot; &amp;&amp; ST_SetSRID(&#39;BOX3D(1171604.841520746 6470654.265434774,1172064.955953034 6470860.847424781)&#39;::box3d, 900913);
                                                                                                                                                            QUERY PLAN
&#10;-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------
 Subquery Scan on text  (cost=6.14..6.28 rows=1 width=55) (actual time=39.916..111.339 rows=26 loops=1)
   -&gt;  Sort  (cost=6.14..6.15 rows=1 width=226) (actual time=36.297..36.311 rows=26 loops=1)
         Sort Key: planet_osm_polygon.way_area DESC
         Sort Method: quicksort  Memory: 28kB
         -&gt;  Index Scan using planet_osm_polygon_way_idx on planet_osm_polygon  (cost=0.55..6.13 rows=1 width=226) (actual time=6.615..36.254 rows=26 loops=1)
               Index Cond: (way &amp;&amp; &#39;01030000A031BF0D00010000000500000053E76DD794E0314122E2FC90FFAE5841000000000000000053E76DD794E0314126353C3633AF584100000000000000008A56B9F460E2314126353C3633AF584100000000000000008A56B9F460E2314122E2FC90FFAE584
1000000000000000053E76DD794E0314122E2FC90FFAE58410000000000000000&#39;::geometry)
               Filter: ((name IS NOT NULL) AND (place IS NULL) AND ((waterway IS NULL) OR (waterway &lt;&gt; &#39;riverbank&#39;::text)))
               Rows Removed by Filter: 29
 Planning Time: 2.620 ms
 Execution Time: 111.408 ms
(10 rows)</code></pre>
<p><em>planet_osm_polygon_way_idx</em> is used and the execution time is 111.408 ms (not minutes as I have on my browser) !</p>
<p><strong>Important is that the postgres and tile server are running in docker containers.</strong></p>
<p>If you need any more information just ask and thanks for the reading and for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '22, 13:47</strong></p>
<img src="https://secure.gravatar.com/avatar/4b54c1e96079cace9610d4a444944462?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hamza&#39;s gravatar image" />
<p><span>Hamza</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hamza has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 May '22, 15:44</strong> </span></p>
</div>
</div>
<div id="comments-container-84464" class="comments-container">
<span id="84467"></span>
<div id="comment-84467" class="comment">
<div id="post-84467-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You have given a lot of information but one crucial bit is missing: What kind of disks do you have in your machine? Do you have local, non-virtualised NVMe/SSD? Or old-style magentic disks? Or maybe some sort of SAN or other network-attached disk? How long did the initial planet import take?</p>
</div>
<div id="comment-84467-info" class="comment-info">
<span class="comment-age">(13 May '22, 16:29)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="84487"></span>
<div id="comment-84487" class="comment">
<div id="post-84487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply, it's a VM with a disk that uses an SSD SAN as PVSCSI (para virtualized). Planet import took almost 28 hours.</p>
</div>
<div id="comment-84487-info" class="comment-info">
<span class="comment-age">(16 May '22, 08:16)</span> <span class="comment-user userinfo">Hamza</span>
</div>
</div>
</div>
<div id="comment-tools-84464" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84464-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

