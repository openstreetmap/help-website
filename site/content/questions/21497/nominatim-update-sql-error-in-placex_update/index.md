+++
type = "question"
title = "Nominatim update sql error in placex_update"
description = '''When running the incremental update script for nominatim, I get a sql error. I recently updated from osmosis 0.35 to 0.42 and updated nominatim to the latest git revision. Is that a red hearing or is there new breakage? ./utils/update.php --import-osmosis-all --no-npi /var/www/Nominate/osm2pgsql/osm...'''
date = "2013-04-13T02:33:00Z"
lastmod = "2013-04-16T18:09:00Z"
weight = 21497
keywords = [ "import", "nominatim", "update", "osmosis" ]
aliases = [ "/questions/21497" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim update sql error in placex_update](/questions/21497/nominatim-update-sql-error-in-placex_update)

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
<span id="post-21497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21497-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When running the incremental update script for nominatim, I get a sql error. I recently updated from osmosis 0.35 to 0.42 and updated nominatim to the latest git revision. Is that a red hearing or is there new breakage?</p>
<pre><code>./utils/update.php --import-osmosis-all --no-npi
/var/www/Nominate/osm2pgsql/osm2pgsql -U apache -klas -C 2000 -O gazetteer -d nominatim /var/www/Nominate/data/osmosischange.osc
osm2pgsql SVN version 0.81.0 (64bit id space)
&#10;Using projection SRS 4326 (Latlong)
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=2000MB, maxblocks=256001*8192, allocation method=11
Mid: pgsql, scale=10000000 cache=2000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /var/www/Nominate/data/osmosischange.osc
Processing: Node(136k 2.1k/s) Way(18k 0.36k/s) Relation(87 43.50/s)  parse time: 119s
&#10;Node stats: total(136962), max(2227049854) in 65s
Way stats: total(18889), max(212923522) in 52s
Relation stats: total(87), max(2843176) in 2s
node cache: stored: 134790(100.00%), storage efficiency: 87.00% (dense blocks: 133, sparse nodes: 9373), hit rate: 36.94%
Stopping table: planet_osm_nodes
Stopped table: planet_osm_nodes in 0s
Stopping table: planet_osm_rels
Stopping table: planet_osm_ways
Stopped table: planet_osm_ways in 0s
Stopped table: planet_osm_rels in 0s
&#10;Osm2pgsql took 119s overall
Completed for 2013-03-26T21:10:03Z in 1.98 minutes
string(127) &quot;INSERT INTO import_osmosis_log values (&#39;2013-03-26T21:10:03Z&#39;,32804717,&#39;2013-04-13 01:03:35&#39;,&#39;2013-04-13 01:05:34&#39;,&#39;osm2pgsql&#39;)&quot;
/var/www/Nominate/nominatim/nominatim -i -d nominatim -t 1
nominatim SVN version 2.1-git-a1670fa
&#10;Starting indexing rank (0 to 30) using 1 threads
Starting rank 0
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 1
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 2
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 3
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 4
  Done 1 in 0 @ 1.000000 per second - ETA (seconds): 0.000000
  Done 1 in 0 @ 1.000000 per second - FINISHED
&#10;Starting rank 5
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 6
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 7
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 8
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 9
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 10
index_placex: UPDATE failed: ERROR:  column &quot;importance&quot; is of type double precision but expression is of type integer[]
LINE 2:       in_name_vector, in_geometry)
              ^
HINT:  You will need to rewrite or cast the expression.
QUERY:  INSERT INTO search_name_39 values (in_place_id, in_rank_search, in_rank_address, 
      in_name_vector, in_geometry)
CONTEXT:  PL/pgSQL function insertsearchname(integer,bigint,character varying,integer[],integer[],integer,integer,double precision,geometry,geometry) line 89 at SQL statement
PL/pgSQL function placex_update() line 635 at assignment
Error: 1</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '13, 02:33</strong></p>
<img src="https://secure.gravatar.com/avatar/705d24784cee7f6cddc6a1e4211513cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="montanalow&#39;s gravatar image" />
<p><span>montanalow</span><br />
<span class="score" title="40 reputation points">40</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="montanalow has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '13, 14:14</strong> </span></p>
</div>
</div>
<div id="comments-container-21497" class="comments-container">
<span id="21500"></span>
<div id="comment-21500" class="comment">
<div id="post-21500-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Umm, don't you think that some accompanying text (a question! pointing out the error, so not every need to scan the text) might be useful? Just throwing some error output at other people's head is not that nice. ;-)</p>
</div>
<div id="comment-21500-info" class="comment-info">
<span class="comment-age">(13 Apr '13, 13:27)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="21502"></span>
<div id="comment-21502" class="comment">
<div id="post-21502-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Sorry, I was just a bit confused and not quite sure what exactly to ask. I've edited in a bit of a question.</p>
</div>
<div id="comment-21502-info" class="comment-info">
<span class="comment-age">(13 Apr '13, 14:15)</span> <span class="comment-user userinfo">montanalow</span>
</div>
</div>
<span id="21535"></span>
<div id="comment-21535" class="comment">
<div id="post-21535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just guessing, but depending on how long ago you did the last update, is it possible that the database schema has changed since then? If it is easy to do (doesn't take to long as you are not using the full planet), you might want to try and re-import the data with the new version of the tools.</p>
</div>
<div id="comment-21535-info" class="comment-info">
<span class="comment-age">(15 Apr '13, 02:02)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="21537"></span>
<div id="comment-21537" class="comment">
<div id="post-21537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I started a fresh full planet import about 12 days ago, with the most recent version of nominatim at the time. This is the first time I've attempted an incremental update to nominatim. Does nominatim include migrations to update the database schema that I should check?</p>
</div>
<div id="comment-21537-info" class="comment-info">
<span class="comment-age">(15 Apr '13, 03:02)</span> <span class="comment-user userinfo">montanalow</span>
</div>
</div>
</div>
<div id="comment-tools-21497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21497-form-container" class="comment-form-container">
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

<span id="21573"></span>

<div id="answer-container-21573" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21573-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-21573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The database schema changed with <a href="https://github.com/twain47/Nominatim/commit/23d303124e903e58e5c95890868de8c62304946f">this commit</a>. There are no migration scripts but the manual steps to do the migration are described in <a href="https://github.com/twain47/Nominatim/pull/45">this pull request</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '13, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-21573" class="comments-container">
<span id="21607"></span>
<div id="comment-21607" class="comment">
<div id="post-21607-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again, that fixed things up.</p>
</div>
<div id="comment-21607-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 18:09)</span> <span class="comment-user userinfo">montanalow</span>
</div>
</div>
</div>
<div id="comment-tools-21573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21573-form-container" class="comment-form-container">
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

