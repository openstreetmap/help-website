+++
type = "question"
title = "Import error with Nominatim installation: No Data and DB Error: insufficient permissions"
description = '''I&#x27;m on Debian Squeeze and following http://wiki.openstreetmap.org/wiki/Nominatim/Installation . I&#x27;m at the point where I import the OSM file ( http://wiki.openstreetmap.org/wiki/Nominatim/Installation#Import_and_index_OSM_data ): time php -d error_reporting=E_ALL ./utils/setup.php --osm-file austria...'''
date = "2012-04-26T12:35:00Z"
lastmod = "2013-06-13T13:25:00Z"
weight = 12373
keywords = [ "nominatim", "installation", "postgres" ]
aliases = [ "/questions/12373" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Import error with Nominatim installation: No Data and DB Error: insufficient permissions](/questions/12373/import-error-with-nominatim-installation-no-data-and-db-error-insufficient-permissions)

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
<span id="post-12373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12373-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm on Debian Squeeze and following <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">http://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> . I'm at the point where I import the OSM file ( <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation#Import_and_index_OSM_data">http://wiki.openstreetmap.org/wiki/Nominatim/Installation#Import_and_index_OSM_data</a> ):</p>
<p><code>time php -d error_reporting=E_ALL ./utils/setup.php --osm-file austria.osm --all</code></p>
<p>I'm using a specific country as opposed to the whole planet and the setup runs for about 13 minutes and ends with:</p>
<pre><code>INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
COMMIT
SET
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
ALTER TABLE
Import
Using projection SRS 4326 (Latlong)
NOTICE:  table &quot;place&quot; does not exist, skipping
NOTICE:  type &quot;keyvalue&quot; does not exist, skipping
NOTICE:  type &quot;wordscore&quot; does not exist, skipping
NOTICE:  type &quot;stringlanguagetype&quot; does not exist, skipping
NOTICE:  type &quot;keyvaluetype&quot; does not exist, skipping
NOTICE:  function get_connected_ways(pg_catalog.int4[]) does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=15000MB, maxblocks=1920001*8192, allocation method=11
Mid: pgsql, scale=10000000 cache=15000
Setting up table: planet_osm_nodes
NOTICE:  table &quot;planet_osm_nodes&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_nodes_pkey&quot; for table &quot;planet_osm_nodes&quot;
Setting up table: planet_osm_ways
NOTICE:  table &quot;planet_osm_ways&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_ways_pkey&quot; for table &quot;planet_osm_ways&quot;
Setting up table: planet_osm_rels
NOTICE:  table &quot;planet_osm_rels&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_rels_pkey&quot; for table &quot;planet_osm_rels&quot;
&#10;Reading in file: austria.osm
Processing: Node(16412k 72.6k/s) Way(1550k 8.12k/s) Relation(28484 1017.29/s)  parse time: 445s
&#10;Node stats: total(16412032), max(1543457158) in 226s
Way stats: total(1550680), max(140997267) in 191s
Relation stats: total(28484), max(1907412) in 28s
node cache: stored: 16412032(100.00%), storage efficiency: 67.22% (dense blocks: 1301, sparse nodes: 15387701), hit rate: 97.81%
Stopping table: planet_osm_nodes
Stopping table: planet_osm_rels
Building index on table: planet_osm_rels (fastupdate=off)
Stopping table: planet_osm_ways
Building index on table: planet_osm_ways (fastupdate=off)
Stopped table: planet_osm_nodes in 0s
Stopped table: planet_osm_rels in 0s
Stopped table: planet_osm_ways in 355s
&#10;Osm2pgsql took 800s overall
osm2pgsql SVN version 0.80.0 (32bit id space)
&#10;ERROR: No Data
No Data
&#10;real    13m37.663s
user    4m18.800s
sys     0m7.800s</code></pre>
<p>I grepped the source for <em>No Data</em> and found this in <code>util/setup.php</code>:</p>
<pre><code>123         $oDB =&amp; getDB();
124         $x = $oDB-&gt;getRow(&#39;select * from place limit 1&#39;);
125         if (!$x || PEAR::isError($x)) fail(&#39;No Data&#39;);</code></pre>
<p>But what puzzles me is that I see there <strong>is</strong> actually data there:</p>
<pre><code>$ psql nominatim
psql (8.4.11)
Type &quot;help&quot; for help.
&#10;nominatim=# select count(*) from place;
  count
---------
 1788758
(1 row)</code></pre>
<p>I re-ran the command with additional debug info in the <code>setup.php</code> script to echo the PEAR error, in case it is one, and got this:</p>
<pre><code>Message: DB Error: insufficient permissions
ERROR: No Data
No Data</code></pre>
<p>I then discovered that the table <code>place</code> has been created with the owner <code>postgres</code>; this is the use under which I executed the whole setup utility and which has local ident rights to do everything (default setup).</p>
<p>I did this because the guide mentions:</p>
<blockquote>
<p>You also need a user with superuser rights for the account that is doing the import. You must not run the import as user www-data.</p>
</blockquote>
<p>However it seems the import script is using different users when doing the stuff and I'm not sure how to handle this. I set proper credentials in <code>settings/local.php</code>, but it seems the actual import with <code>osm2pgsql</code> is done with my CLI user <code>postgres</code> and when the script tries to access the database it is my configured username (which is just <code>nominatim</code> per the examples; this is only a postgresql user, not a system account).</p>
<p>What is the proper procedure for the import?</p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '12, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/e9d5ea594974c3409d40e7cd373c7005?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Markus&#39;s gravatar image" />
<p><span>Markus</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Markus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12373" class="comments-container">
&#10;</div>
<div id="comment-tools-12373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12373-form-container" class="comment-form-container">
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

<span id="12384"></span>

<div id="answer-container-12384" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12384-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Markus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The import script currently still assumes in many places that you are using a postgres user with the same name as the CLI user doing the import. You need to create such a user (with -s, to give it superuser rights), make sure you have set up postgres that it allows local peer identification and in your <code>settings.local</code> use a DSN without credentials.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '12, 20:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-12384" class="comments-container">
<span id="12385"></span>
<div id="comment-12385" class="comment">
<div id="post-12385-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@lonvia</span>: thanks a lot, that was it. It is even stated <em>clearly</em> in the text I quoted: "You also need a user with superuser rights...", I've no idea how I missed that.</p>
</div>
<div id="comment-12385-info" class="comment-info">
<span class="comment-age">(26 Apr '12, 22:31)</span> <span class="comment-user userinfo">Markus</span>
</div>
</div>
<span id="23266"></span>
<div id="comment-23266" class="comment">
<div id="post-23266-score" class="comment-score">
-1
</div>
<div class="comment-text">
<p>Hi Ionvia,</p>
<p>I think I'm having the same issue. What did you do exactly?</p>
<p>Thanks, Lucas</p>
</div>
<div id="comment-23266-info" class="comment-info">
<span class="comment-age">(12 Jun '13, 13:49)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
<span id="23323"></span>
<div id="comment-23323" class="comment">
<div id="post-23323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you read lonvias answer right above yours?</p>
</div>
<div id="comment-23323-info" class="comment-info">
<span class="comment-age">(13 Jun '13, 11:59)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="23336"></span>
<div id="comment-23336" class="comment">
<div id="post-23336-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Since then I figured it out. Thanks anyway.</p>
</div>
<div id="comment-23336-info" class="comment-info">
<span class="comment-age">(13 Jun '13, 13:25)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
</div>
<div id="comment-tools-12384" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12384-form-container" class="comment-form-container">
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

