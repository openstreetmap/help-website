+++
type = "question"
title = "Nominatim slow query"
description = ''' I recently imported the nominatim with full planet and queries are undesirable performance. The first query, before the cache is created, takes longer than 20 seconds and sometimes I see this error:    Internal Server Error Nominatim has encountered an internal error while accessing the database. T...'''
date = "2018-08-14T18:43:00Z"
lastmod = "2018-08-15T00:21:00Z"
weight = 65346
keywords = [ "slow", "search", "nominatim", "query", "performance" ]
aliases = [ "/questions/65346" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim slow query](/questions/65346/nominatim-slow-query)

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
<span id="post-65346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65346-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently imported the nominatim with full planet and queries are undesirable performance. The first query, before the cache is created, takes longer than 20 seconds and sometimes I see this error:</p>
<pre><code>Internal Server Error
Nominatim has encountered an internal error while accessing the database. This may happen because the database is broken or because of a bug in the software. If you think it is a bug, feel free to report it over on Github. Please include the URL that caused the problem and the complete error details below.
Message: Could not lookup place
SQL Error: DB Error: unknown error
Details:
SELECT     osm_type,    osm_id,    class,    type,    admin_level,    rank_search,    rank_address,    min(place_id) AS place_id,    min(parent_place_id) AS parent_place_id,    -1 as housenumber,    country_code,get_address_by_language(place_id,-1,ARRAY[&#39;short_name&#39;,&#39;name&#39;,&#39;brand&#39;,&#39;official_name&#39;,&#39;ref&#39;,&#39;type&#39;]) AS langaddress,    get_name_by_language(name,ARRAY[&#39;short_name&#39;,&#39;name&#39;,&#39;brand&#39;,&#39;official_name&#39;,&#39;ref&#39;,&#39;type&#39;]) AS placename,    get_name_by_language(name, ARRAY[&#39;ref&#39;]) AS ref,    avg(ST_X(centroid)) AS lon,     avg(ST_Y(centroid)) AS lat,     COALESCE(importance,0.75-(rank_search::float/40)) AS importance, (SELECT max(ai_p.importance * (ai_p.rank_address + 2))   FROM place_addressline ai_s, placex ai_p   WHERE ai_s.place_id = min(CASE WHEN placex.rank_search &lt; 28 THEN placex.place_id ELSE placex.parent_place_id END)     AND ai_p.place_id = ai_s.address_place_id      AND ai_s.isaddress      AND ai_p.importance is not null) AS addressimportance,    (extratags-&gt;&#39;place&#39;) AS extra_place  FROM placex WHERE place_id in (92672355,196842012,4488269,196732908,48310082,160137,91687842,70711723,83690356,77366185,74053027,92460750,82583385,113120861,177719652,86034442,82755806,76866792,83301006,92789547)    AND (        placex.rank_address between 0 and 30     OR (extratags-&gt;&#39;place&#39;) = &#39;city&#39;       )     AND linked_place_id is null  GROUP BY      osm_type,      osm_id,      class,      type,      admin_level,      rank_search,      rank_address,      housenumber,     country_code,      importance,      langaddress,      placename,      ref,      extratags-&gt;&#39;place&#39;  [nativecode=ERROR:  canceling statement due to statement timeout
CONTEXT:  PL/pgSQL function get_addressdata(bigint,integer) line 103 at FOR over SELECT rows
PL/pgSQL function get_address_by_language(bigint,integer,text[]) line 12 at FOR over SELECT rows]
</code></pre>
<hr />
<p>Due to the delay of the queries I thought the problem was the lack of some index and then I executed:</p>
<pre><code>nohup ./utils/setup.php --create-search-indices --ignore-errors &amp;
&#10;Output:
&#10;2018-08-13 20:59:56 == Create Search indices
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
    LANGUAGE = (unset),
    LC_ALL = (unset),
    LC_CTYPE = &quot;UTF-8&quot;,
    LANG = &quot;en_US.UTF-8&quot;
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale (&quot;en_US.UTF-8&quot;).
ERROR:  relation &quot;idx_word_word_id&quot; already exists
ERROR:  relation &quot;idx_search_name_nameaddress_vector&quot; already exists
ERROR:  relation &quot;idx_search_name_name_vector&quot; already exists
ERROR:  relation &quot;idx_search_name_centroid&quot; already exists
ERROR:  relation &quot;idx_place_addressline_address_place_id&quot; already exists
ERROR:  relation &quot;idx_placex_rank_address&quot; already exists
ERROR:  relation &quot;idx_placex_pendingsector&quot; already exists
ERROR:  relation &quot;idx_placex_parent_place_id&quot; already exists
ERROR:  relation &quot;idx_placex_reverse_geometry&quot; already exists
ERROR:  relation &quot;idx_location_area_country_place_id&quot; already exists
ERROR:  relation &quot;idx_osmline_parent_place_id&quot; already exists
ERROR:  relation &quot;idx_search_name_country_centroid&quot; already exists
NOTICE:  index &quot;place_id_idx&quot; does not exist, skipping
ERROR:  relation &quot;idx_place_osm_unique&quot; already exists
ERROR:  relation &quot;idx_postcode_id&quot; already exists
ERROR:  relation &quot;idx_postcode_postcode&quot; already exists
Summary of warnings:
&#10;
2018-08-14 02:23:14 == Setup finished.
</code></pre>
<p>What does this line mean? NOTICE: index "place_id_idx" does not exist, skipping</p>
<hr />
<p>After that, I turn on the postgresql log and called the search api with these parameters:</p>
<pre><code>http://nominatim.dev/nominatim/search.php?format=jsonv2&amp;addressdetails=1&amp;q=cancun
&#10;Logs:
&#10;2018-08-14 14:30:49 UTC [2489-1] www-data@nominatim LOG:  duration: 16092.775 ms  statement: SELECT     osm_type,    osm_id,    class,    type,    admin_level,    rank_search,    rank_address,    min(place_id) AS place_id,    min(parent_place_id) AS parent_place_id,    -1 as housenumber,    country_code,get_address_by_language(place_id,-1,ARRAY[&#39;short_name:en-en&#39;,&#39;name:en-en&#39;,&#39;short_name:en&#39;,&#39;name:en&#39;,&#39;short_name&#39;,&#39;name&#39;,&#39;brand&#39;,&#39;official_name:en-en&#39;,&#39;official_name:en&#39;,&#39;official_name&#39;,&#39;ref&#39;,&#39;type&#39;]) AS langaddress,    get_name_by_language(name,ARRAY[&#39;short_name:en-en&#39;,&#39;name:en-en&#39;,&#39;short_name:en&#39;,&#39;name:en&#39;,&#39;short_name&#39;,&#39;name&#39;,&#39;brand&#39;,&#39;official_name:en-en&#39;,&#39;official_name:en&#39;,&#39;official_name&#39;,&#39;ref&#39;,&#39;type&#39;]) AS placename,    get_name_by_language(name, ARRAY[&#39;ref&#39;]) AS ref,    avg(ST_X(centroid)) AS lon,     avg(ST_Y(centroid)) AS lat,     COALESCE(importance,0.75-(rank_search::float/40)) AS importance, (SELECT max(ai_p.importance * (ai_p.rank_address + 2))   FROM place_addressline ai_s, placex ai_p   WHERE ai_s.place_id = min(CASE WHEN placex.rank_search &lt; 28 THEN placex.place_id ELSE placex.parent_place_id END)     AND ai_p.place_id = ai_s.address_place_id      AND ai_s.isaddress      AND ai_p.importance is not null) AS addressimportance,    (extratags-&gt;&#39;place&#39;) AS extra_place  FROM placex WHERE place_id in (197441826,111603036,182595459,139694930,144830394,118512715,74049435,99932703,159450111,141912308,112119380,80303695,80305679,112647794,80522782,115827503,128389572,149585949,74675442,150225528)    AND (        placex.rank_address between 0 and 30     OR (extratags-&gt;&#39;place&#39;) = &#39;city&#39;       )     AND linked_place_id is null  GROUP BY      osm_type,      osm_id,      class,      type,      admin_level,      rank_search,      rank_address,      housenumber,     country_code,      importance,      langaddress,      placename,      ref,      extratags-&gt;&#39;place&#39;
&#10;2018-08-14 14:31:35 UTC [2490-1] ERROR:  function transliteration(text) does not exist at character 23
2018-08-14 14:31:35 UTC [2490-2] HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
2018-08-14 14:31:35 UTC [2490-3] QUERY:  SELECT gettokenstring(transliteration(name))
2018-08-14 14:31:35 UTC [2490-4] CONTEXT:  PL/pgSQL function public.make_standard_name(text) line 5 at assignment
    automatic analyze of table &quot;nominatim.public.placex&quot;
</code></pre>
<p>Looking at the logs I thought some functions might be missing, and execute this:</p>
<pre><code>nohup ./utils/setup.php --create-functions --ignore-errors &amp;
&#10;2018-08-14 14:48:04 == Create Functions
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
    LANGUAGE = (unset),
    LC_ALL = (unset),
    LC_CTYPE = &quot;UTF-8&quot;,
    LANG = &quot;en_US.UTF-8&quot;
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale (&quot;en_US.UTF-8&quot;).
NOTICE:  drop cascades to function get_addressdata(bigint,integer)
NOTICE:  drop cascades to function get_wikipedia_match(hstore,character varying)
Summary of warnings:
&#10;
2018-08-14 14:48:04 == Setup finished.
</code></pre>
<hr />
<p>Some info about my installation:</p>
<pre><code>Nominatim version 3.1.0
&#10;Ec2 t2.2xlarge with T2 Unlimited | vCPU 8 | 32GB RAM | SSD 870 GB gp2 2610/3000 IOPS
&#10; Postgresql configurations:
- shared_buffers = 2GB
- maintenance_work_mem = 10GB
- work_mem = 50MB
- effective_cache_size = 24GB
- synchronous_commit = off
- checkpoint_timeout = 10min
- checkpoint_completion_target = 0.9
- fsync = on
- full_page_writes = on
- random_page_cost = 1.1
- wal_buffers = 16MB
- max_worker_processes = 8
&#10;df -h
&#10;Filesystem      Size  Used Avail Use% Mounted on
udev             16G     0   16G   0% /dev
tmpfs           3.2G  9.5M  3.2G   1% /run
/dev/xvda1      844G  674G  170G  80% /
tmpfs            16G  4.0K   16G   1% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs            16G     0   16G   0% /sys/fs/cgroup
/dev/loop0       13M   13M     0 100% /snap/amazon-ssm-agent/295
/dev/loop1       87M   87M     0 100% /snap/core/4917
/dev/loop2       87M   87M     0 100% /snap/core/4830
/dev/loop3       87M   87M     0 100% /snap/core/5145
tmpfs           3.2G     0  3.2G   0% /run/user/1000
&#10;free -h 
&#10;              total        used        free      shared  buff/cache   available
Mem:            31G        171M         29G        115M        1.5G         30G
Swap:            0B          0B          0B
&#10;nominatim=# \d search_name
                Table &quot;public.search_name&quot;
       Column       |          Type           | Modifiers
--------------------+-------------------------+-----------
 place_id           | bigint                  |
 importance         | double precision        |
 search_rank        | smallint                |
 address_rank       | smallint                |
 name_vector        | integer[]               |
 nameaddress_vector | integer[]               |
 country_code       | character varying(2)    |
 centroid           | geometry(Geometry,4326) |
Indexes:
    &quot;idx_search_name_centroid&quot; gist (centroid)
    &quot;idx_search_name_name_vector&quot; gin (name_vector) WITH (fastupdate=off)
    &quot;idx_search_name_nameaddress_vector&quot; gin (nameaddress_vector) WITH (fastupdate=off)
    &quot;idx_search_name_place_id&quot; btree (place_id)
&#10;nominatim=# \d placex
                   Table &quot;public.placex&quot;
     Column      |            Type             | Modifiers
-----------------+-----------------------------+-----------
 place_id        | bigint                      | not null
 parent_place_id | bigint                      |
 linked_place_id | bigint                      |
 importance      | double precision            |
 indexed_date    | timestamp without time zone |
 geometry_sector | integer                     |
 rank_address    | smallint                    |
 rank_search     | smallint                    |
 partition       | smallint                    |
 indexed_status  | smallint                    |
 osm_id          | bigint                      | not null
 osm_type        | character(1)                | not null
 class           | text                        | not null
 type            | text                        | not null
 name            | hstore                      |
 admin_level     | smallint                    |
 address         | hstore                      |
 extratags       | hstore                      |
 geometry        | geometry(Geometry,4326)     | not null
 wikipedia       | text                        |
 country_code    | character varying(2)        |
 housenumber     | text                        |
 postcode        | text                        |
 centroid        | geometry(Geometry,4326)     |
Indexes:
    &quot;idx_place_id&quot; UNIQUE, btree (place_id)
    &quot;idx_placex_adminname&quot; btree (make_standard_name(name -&gt; &#39;name&#39;::text), rank_search) WHERE osm_type = &#39;N&#39;::bpchar AND rank_search &lt; 26
    &quot;idx_placex_geometry&quot; gist (geometry)
    &quot;idx_placex_linked_place_id&quot; btree (linked_place_id) WHERE linked_place_id IS NOT NULL
    &quot;idx_placex_osmid&quot; btree (osm_type, osm_id)
    &quot;idx_placex_parent_place_id&quot; btree (parent_place_id) WHERE parent_place_id IS NOT NULL
    &quot;idx_placex_pendingsector&quot; btree (rank_search, geometry_sector) WHERE indexed_status &gt; 0
    &quot;idx_placex_rank_address&quot; btree (rank_address)
    &quot;idx_placex_rank_search&quot; btree (rank_search)
    &quot;idx_placex_reverse_geometry&quot; gist (geometry) WHERE rank_search &lt;&gt; 28 AND (name IS NOT NULL OR housenumber IS NOT NULL) AND (class &lt;&gt; ALL (ARRAY[&#39;waterway&#39;::text, &#39;railway&#39;::text, &#39;tunnel&#39;::text, &#39;bridge&#39;::text, &#39;man_made&#39;::text]))
Triggers:
    placex_before_delete AFTER DELETE ON placex FOR EACH ROW EXECUTE PROCEDURE placex_delete()
    placex_before_insert BEFORE INSERT ON placex FOR EACH ROW EXECUTE PROCEDURE placex_insert()
    placex_before_update BEFORE UPDATE ON placex FOR EACH ROW EXECUTE PROCEDURE placex_update()
</code></pre>
<hr />
<p>I did not come up with a solution with no command executed</p>
<h3 id="what-else-can-i-do-to-try-to-solve-this">What else can I do to try to solve this?</h3>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '18, 18:43</strong></p>
<img src="https://secure.gravatar.com/avatar/1c276cd38b3a8114089732886a47d6d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnosis7&#39;s gravatar image" />
<p><span>gnosis7</span><br />
<span class="score" title="19 reputation points">19</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnosis7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65346" class="comments-container">
<span id="65347"></span>
<div id="comment-65347" class="comment">
<div id="post-65347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Running the ./utils/setup.php --index command seems to stuck in:</p>
<p>Starting rank 4 Done 0 in 0 @ 0.000000 per second - FINISHED</p>
</div>
<div id="comment-65347-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 18:49)</span> <span class="comment-user userinfo">gnosis7</span>
</div>
</div>
</div>
<div id="comment-tools-65346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65346-form-container" class="comment-form-container">
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

<span id="65348"></span>

<div id="answer-container-65348" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65348-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gnosis7 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overall the output and setup looks good, nothing catches my eye immediately.</p>
<p>You can ignore the "function transliteration(text) does not exist" warning. That happens during postgresql vacuum process and not user query. The function does exists because it's used during data import and every/most user queries. More details in <a href="https://github.com/openstreetmap/Nominatim/issues/1097">https://github.com/openstreetmap/Nominatim/issues/1097</a></p>
<p>Did the initial import happen with the Nominatim-3.1 release (<a href="https://www.nominatim.org/release-history/)">https://www.nominatim.org/release-history/)</a> or did you upgrade the software in the meantime? Is the current installed version 3.1 or latest master? I'm not recommending a version, it just helps to figure out which indices should exist because that keeps changing.</p>
<p>Try running test queries with 'EXPLAIN', see a similar discussion at <a href="https://github.com/openstreetmap/Nominatim/issues/1023#issuecomment-384441294">https://github.com/openstreetmap/Nominatim/issues/1023#issuecomment-384441294</a></p>
<p>It might be easier to move the discussion to <a href="https://github.com/openstreetmap/Nominatim/issues/">https://github.com/openstreetmap/Nominatim/issues/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '18, 21:24</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-65348" class="comments-container">
<span id="65349"></span>
<div id="comment-65349" class="comment">
<div id="post-65349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Mtmail, thanks for the help! My installation comes from this link: <a href="https://nominatim.org/release/Nominatim-3.1.0.tar.bz2">https://nominatim.org/release/Nominatim-3.1.0.tar.bz2</a> Regarding the tests of queries, I'll send in github.</p>
</div>
<div id="comment-65349-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 22:09)</span> <span class="comment-user userinfo">gnosis7</span>
</div>
</div>
<span id="65350"></span>
<div id="comment-65350" class="comment">
<div id="post-65350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://github.com/openstreetmap/Nominatim/issues/1139">https://github.com/openstreetmap/Nominatim/issues/1139</a></p>
</div>
<div id="comment-65350-info" class="comment-info">
<span class="comment-age">(15 Aug '18, 00:21)</span> <span class="comment-user userinfo">gnosis7</span>
</div>
</div>
</div>
<div id="comment-tools-65348" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65348-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

