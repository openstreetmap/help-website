+++
type = "question"
title = "osmosis update.php --import-osmosis-all --no-npi fail"
description = '''Hi All I&#x27;m new here and I hope I&#x27;m writing on the right session. I have installed Nominatim 2.3.1 following the wiki guide at the page https://wiki.openstreetmap.org/wiki/Nominatim/Installation on centOS 6.6 minimal. I have java 1.7 version, I imported the montecarlo map and everything goes fine. I c...'''
date = "2015-05-20T13:55:00Z"
lastmod = "2017-03-21T18:39:00Z"
weight = 43132
keywords = [ "osmosis" ]
aliases = [ "/questions/43132" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis update.php --import-osmosis-all --no-npi fail](/questions/43132/osmosis-updatephp-import-osmosis-all-no-npi-fail)

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
<span id="post-43132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43132-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All I'm new here and I hope I'm writing on the right session. I have installed Nominatim 2.3.1 following the wiki guide at the page <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> on centOS 6.6 minimal. I have java 1.7 version, I imported the montecarlo map and everything goes fine. I configure it with apache and I reach the openstreetmap home pag at localhost and I obtain the xml address from a latitude and longitude parameters.</p>
<p>Now i would like to keep my map updated and I download (and unpack) osmosis latest version. I edited my local.php as follows:</p>
<pre><code>&lt;?php
   // Paths
   @define(&#39;CONST_Postgresql_Version&#39;, &#39;9.4&#39;);
   @define(&#39;CONST_Postgis_Version&#39;, &#39;2.1&#39;);
   @define(&#39;CONST_Path_Postgresql_Contrib&#39;, &#39;/usr/pgsql-9.4/share/contrib&#39;);
   // Website settings
   @define(&#39;CONST_Website_BaseURL&#39;, &#39;http://192.168.56.101/nominatim/&#39;);
   // Osmosis settings, SOLO PER INSTALLAZIONE OSMOSIS!!
   @define(&#39;CONST_Osmosis_Binary&#39;, &#39;/srv/osmosis/bin/osmosis&#39;);
   @define(&#39;CONST_Replication_Url&#39;, &#39;http://download.geofabrik.de/europe/monaco-updates&#39;);
   @define(&#39;CONST_Replication_MaxInterval&#39;, &#39;40000&#39;);     
   @define(&#39;CONST_Replication_Update_Interval&#39;, &#39;86400&#39;); 
   @define(&#39;CONST_Replication_Recheck_Interval&#39;, &#39;900&#39;);</code></pre>
<p>I have no configuration.txt on my nominatim/settings folder than I start with the follow command:</p>
<pre><code>./utils/setup.php --osmosis-init</code></pre>
<p>and the script ended ok</p>
<pre><code>./utils/setup.php --create-functions --enable-diff-updates</code></pre>
<p>and the script ended ok than when I run the last script</p>
<pre><code>./utils/update.php --import-osmosis-all --no-npi</code></pre>
<p>the script doesn't end!! I redirect the standard output and error and I post here just a little piece. I don't know what's wrong (and if there's something wrong), how can I verify if the updates goes fine? How long the script must run (10 minutes? 5m?)? Follow pieces of output and error:</p>
<pre><code>2015-05-20 08:47:18 Replication Delay is 2419260
/srv/osmosis/bin/osmosis --read-replication-interval workingDirectory=/srv/Nominatim-2.3.1/settings --simplify-change --write-xml-change /srv/Nominatim-2.3.1/data/osmosischange.osc
mag 20, 2015 10:47:19 AM org.openstreetmap.osmosis.core.Osmosis run
INFORMAZIONI: Osmosis Version 0.43.1
mag 20, 2015 10:47:20 AM org.openstreetmap.osmosis.core.Osmosis run
INFORMAZIONI: Preparing pipeline.
mag 20, 2015 10:47:20 AM org.openstreetmap.osmosis.core.Osmosis run
INFORMAZIONI: Launching pipeline execution.
mag 20, 2015 10:47:20 AM org.openstreetmap.osmosis.core.Osmosis run
INFORMAZIONI: Pipeline executing, waiting for completion.
mag 20, 2015 10:47:20 AM org.openstreetmap.osmosis.core.Osmosis run
INFORMAZIONI: Pipeline complete.
mag 20, 2015 10:47:20 AM org.openstreetmap.osmosis.core.Osmosis run
INFORMAZIONI: Total execution time: 1762 milliseconds.
string(120) &quot;INSERT INTO import_osmosis_log values (&#39;2015-04-22T20:21:03Z&#39;,419,&#39;2015-05-20 08:47:18&#39;,&#39;2015-05-20 08:47:20&#39;,&#39;osmosis&#39;)&quot;
2015-05-20 08:47:20 Completed osmosis step for 2015-04-22T20:21:03Z in 0.03 minutes
/srv/Nominatim-2.3.1/osm2pgsql/osm2pgsql -klas -C 2000 -O gazetteer -d nominatim -P 5432 /srv/Nominatim-2.3.1/data/osmosischange.osc
osm2pgsql SVN version 0.85.0 (64bit id space)
&#10;Using projection SRS 4326 (Latlong)
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=2000MB, maxblocks=256000*8192, allocation method=11
Mid: pgsql, scale=10000000 cache=2000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /srv/Nominatim-2.3.1/data/osmosischange.osc
&#10;Processing: Node(0k 0.0k/s) Way(0k 0.00k/s) Relation(0 0.00/s)  parse time: 0s
&#10;Node stats: total(1), max(2680832184) in 0s
Way stats: total(0), max(0) in 0s
Relation stats: total(0), max(0) in 0s
node cache: stored: 1(100.00%), storage efficiency: 0.10% (dense blocks: 1, sparse nodes: 0), hit rate: -nan%
Stopping table: planet_osm_ways
Stopping table: planet_osm_rels
Stopped table: planet_osm_ways in 0s
Stopped table: planet_osm_rels in 0s
Stopping table: planet_osm_nodes
Stopped table: planet_osm_nodes in 0s
&#10;Osm2pgsql took 1s overall
string(122) &quot;INSERT INTO import_osmosis_log values (&#39;2015-04-22T20:21:03Z&#39;,419,&#39;2015-05-20 08:47:20&#39;,&#39;2015-05-20 08:47:21&#39;,&#39;osm2pgsql&#39;)&quot;
2015-05-20 08:47:21 Completed osm2pgsql step for 2015-04-22T20:21:03Z in 0.02 minutes
/srv/Nominatim-2.3.1/nominatim/nominatim -i -d nominatim -P 5432 -t 1
nominatim version 2.4
&#10;Starting indexing rank (0 to 30) using 1 threads
Starting rank 0
  Done 0 in 0 @ 0.000000 per second - FINISHED                      
Starting rank 1
  Done 0 in 0 @ 0.000000 per second - FINISHED                      
Starting rank 2
.....</code></pre>
<p>until 30 is reached. Than the script repeat output similar to above until the server where it reach the state.txt goes down</p>
<pre><code>......
INFORMAZIONI: Pipeline executing, waiting for completion.
mag 20, 2015 10:47:46 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
GRAVE: Thread for task 1-read-replication-interval failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to read the state from the server.
    at org.openstreetmap.osmosis.replication.common.ServerStateReader.getServerState(ServerStateReader.java:114)
    at org.openstreetmap.osmosis.replication.common.ServerStateReader.getServerState(ServerStateReader.java:63)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.download(BaseReplicationDownloader.java:244)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.runImpl(BaseReplicationDownloader.java:302)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.run(BaseReplicationDownloader.java:381)
    at java.lang.Thread.run(Thread.java:745)
Caused by: java.io.IOException: Server returned HTTP response code: 500 for URL: http://download.geofabrik.de/europe/monaco-updates/000/000/779.state.txt
    at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1627)
    at org.openstreetmap.osmosis.replication.common.ServerStateReader.getServerState(ServerStateReader.java:95)
    ... 5 more</code></pre>
<p>I just want that my nominatim map updates itself daily automatical.. Maybe I just have to edit local.php and don't run others scripts?? Please help me. Thank you all</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '15, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/baa53b81d8a54ef27c893d8bc1c4ea0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="developer_afbnet&#39;s gravatar image" />
<p><span>developer_af...</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="developer_afbnet has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '15, 14:01</strong> </span></p>
</div>
</div>
<div id="comments-container-43132" class="comments-container">
<span id="55218"></span>
<div id="comment-55218" class="comment">
<div id="post-55218-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>was there ever any movement on this?</p>
</div>
<div id="comment-55218-info" class="comment-info">
<span class="comment-age">(21 Mar '17, 18:39)</span> <span class="comment-user userinfo">olearytd12</span>
</div>
</div>
</div>
<div id="comment-tools-43132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43132-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

