+++
type = "question"
title = "Error while extracting merged database for Nominatim. Help!"
description = '''I merged Europe and North America .os.bz2 files from http://download.geofabrik.de/ using the command osmium merge country1.osm.bz2 country2.osm.bz2 -o together.osm.bz2. Then I started extraction of the merged file using the command ./utils/setup.php --osm-file together.osm.bz2 --all 2&amp;gt;&amp;amp;1 | te...'''
date = "2020-08-06T06:10:00Z"
lastmod = "2020-08-09T10:29:00Z"
weight = 76029
keywords = [ "osmium", "merge", "nominatim", "extract" ]
aliases = [ "/questions/76029" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error while extracting merged database for Nominatim. Help!](/questions/76029/error-while-extracting-merged-database-for-nominatim-help)

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
<span id="post-76029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76029-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I merged Europe and North America .os.bz2 files from <strong><em><a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a></em></strong> using the command <strong><em>osmium merge country1.osm.bz2 country2.osm.bz2 -o together.osm.bz2</em></strong>. Then I started extraction of the merged file using the command <strong><em>./utils/setup.php --osm-file together.osm.bz2 --all 2&gt;&amp;1 | tee setup.log</em></strong>. After running this command I got the error below:</p>
<pre><code>2020-08-05 01:40:59 == WARNING: resetting threads to 1
2020-08-05 01:40:59 == module path: /srv/nominatim/build/module
2020-08-05 01:40:59 == Create DB
2020-08-05 01:40:59 == Setup DB
Postgres version found: 10
Postgis version found: 2.4
 set_config
------------
&#10;(1 row)
&#10;2020-08-05 01:41:04 == Import data
osm2pgsql version 1.2.0 (v3.5.0-67-g8201c7f)
&#10;Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=46413MB, maxblocks=742608*65536, allocation method=11
Mid: pgsql, cache=46413
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
Parsing gazetteer style file &#39;/srv/nominatim/Nominatim/settings/import-full.style&#39;.
Using projection SRS 4326 (Latlong)
NOTICE:  table &quot;place&quot; does not exist, skipping
&#10;Reading in file: /srv/nominatim/build/europe-north-america.osm.bz2
Using XML parser.
Processing: Node(3824539k 228.0k/s) Way(413495k 49.59k/s) Relation(6198427 5019.0/s)  parse time: 26344s
Node stats: total(3824539161), max(7771142999) in 16771s
Way stats: total(413495830), max(832369740) in 8338s
Relation stats: total(6198427), max(11366925) in 1235s
result COPY END for planet_osm_rels failed: ERROR:  duplicate key value violates unique constraint &quot;planet_osm_rels_pkey&quot;
DETAIL:  Key (id)=(11980) already exists.
CONTEXT:  COPY planet_osm_rels, line 3143
&#10;DB copy thread failed: Ending COPY mode
ERROR: No Data
string(7) &quot;No Data&quot;</code></pre>
<p><strong>After this extraction stopped. What could have had caused it and how to solve this issue?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '20, 06:10</strong></p>
<img src="https://secure.gravatar.com/avatar/e268298e773338d7203d941c245ebff4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saurav1997&#39;s gravatar image" />
<p><span>Saurav1997</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saurav1997 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '20, 13:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-76029" class="comments-container">
<span id="76030"></span>
<div id="comment-76030" class="comment">
<div id="post-76030-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please do not just paste an error here. Describe what you tried to do. This should also include a description where you got your data from and how you merged it.</p>
</div>
<div id="comment-76030-info" class="comment-info">
<span class="comment-age">(06 Aug '20, 07:49)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="76031"></span>
<div id="comment-76031" class="comment">
<div id="post-76031-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Originally posted at <a href="https://github.com/osm-search/Nominatim/issues/1905">https://github.com/osm-search/Nominatim/issues/1905</a> (now closed as duplicate for this question)</p>
</div>
<div id="comment-76031-info" class="comment-info">
<span class="comment-age">(06 Aug '20, 07:49)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="76033"></span>
<div id="comment-76033" class="comment">
<div id="post-76033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for not giving a proper description. I have added a new question with proper details. Link: <a href="/questions/76032/error-while-extracting-merged-database-for-nominatim">https://help.openstreetmap.org/questions/76032/error-while-extracting-merged-database-for-nominatim</a></p>
</div>
<div id="comment-76033-info" class="comment-info">
<span class="comment-age">(06 Aug '20, 08:06)</span> <span class="comment-user userinfo">Saurav1997</span>
</div>
</div>
<span id="76034"></span>
<div id="comment-76034" class="comment">
<div id="post-76034-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't add a new question. Edit this question instead.</p>
</div>
<div id="comment-76034-info" class="comment-info">
<span class="comment-age">(06 Aug '20, 12:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="76036"></span>
<div id="comment-76036" class="comment">
<div id="post-76036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have edited it.</p>
</div>
<div id="comment-76036-info" class="comment-info">
<span class="comment-age">(06 Aug '20, 13:48)</span> <span class="comment-user userinfo">Saurav1997</span>
</div>
</div>
</div>
<div id="comment-tools-76029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76029-form-container" class="comment-form-container">
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

<span id="76078"></span>

<div id="answer-container-76078" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76078-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The error message isn't easy to read, but the important detail is this part: "planet_osm_rels failed: ERROR: duplicate key value violates unique constraint". And it even says what the id is: 11980. So presumably the relation 11980 was in together.osm.bz2 twice. This relation is the France relation and France has many overseas departments etc. so it might well be that it was in the Europe and North America extracts.</p>
<p>Now the question is why was it in the merged files twice? The most probably reason is that you downloaded the two original extracts at different points in time and they both contained different versions of the same relation. In that case osmium merge will leave both in there, as documented in the man page: "Do not use this command to merge non-history files with data from different points in time. It will not work correctly." But this is guess work, because I don't know what's in the files you downloaded. You can check this with "osmium getid".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '20, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-76078" class="comments-container">
&#10;</div>
<div id="comment-tools-76078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76078-form-container" class="comment-form-container">
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

