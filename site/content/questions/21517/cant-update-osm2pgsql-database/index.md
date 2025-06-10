+++
type = "question"
title = "Can&#x27;t update osm2pgsql database"
description = '''Hi Alex_Z, &#x27;fraid this is post is not an answer but a me-too. I am hoping you resolved your problem and can let me know how... I have got my system set up a bit simpler, with only the one database &#x27;gis&#x27;, used for rendering tiles. I set everything up mostly according to the instructions on switch2osm...'''
date = "2013-04-14T09:21:00Z"
lastmod = "2013-04-15T23:06:00Z"
weight = 21517
keywords = [ "osm2pgsql", "mapnik", "update" ]
aliases = [ "/questions/21517" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't update osm2pgsql database](/questions/21517/cant-update-osm2pgsql-database)

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
<span id="post-21517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Alex_Z, 'fraid this is post is not an answer but a me-too. I am hoping you resolved your problem and can let me know how... I have got my system set up a bit simpler, with only the one database 'gis', used for rendering tiles. I set everything up mostly according to the instructions on switch2osm.org but it is proving a bit of a struggle, mostly because I only have a slow old machine available to use for the installation.</p>
<p>Because of space and time constraints I did not use the full planet but used a map of GB downloaded from geofabrik. When rendered it I was able to use mobac to supply myself and some friends with some atlases for our mobile phones, so the main aim was achieved.</p>
<p>After about 10 days I thought I had better set up a system to update the database so I followed the instructions in Minutely_Mapnik for a daily update. The resulting merged update file was 1G+ which seemed a bit large but I went ahead. Unfortunately the m/c hung that evening and I think it was a memory problem so I ran it again the next day without anything much else running and the osm2pgsql run completed in about 10 hours.New tiles were being rendered and everything seemed ok. So the day after that success I thought I would continue with the latest daily update (from geofabrik) but for no reason I can understand yet this won't enter the database, and I have the same errors you reported:</p>
<p>%osm2pgsql -a -v -dgis -C1600 -e18 -oexpire-list -s --drop changes.osc.gz</p>
<p>osm2pgsql SVN version 0.81.0 (64bit id space)</p>
<p>Using projection SRS 900913 (Spherical Mercator)</p>
<p>Setting up table: planet_osm_point</p>
<p>NOTICE: table "planet_osm_point_tmp" does not exist, skipping</p>
<p>Setting up table: planet_osm_line</p>
<p>etc... ..until</p>
<p>Allocating memory for sparse node cache</p>
<p>Node-cache: cache=1600MB, maxblocks=0*204801, allocation method=8192</p>
<p>Mid: pgsql, scale=100 cache=1600</p>
<p>Setting up table: planet_osm_nodes</p>
<p>PREPARE insert_node (int8, int4, int4, text[]) AS INSERT INTO planet_osm_nodes VALUES ($1,$2,$3,$4);</p>
<p>PREPARE get_node (int8) AS SELECT lat,lon,tags FROM planet_osm_nodes WHERE id = $1 LIMIT 1;</p>
<p>PREPARE delete_node (int8) AS DELETE FROM planet_osm_nodes WHERE id = $1;</p>
<p>failed: ERROR: relation "planet_osm_nodes" does not exist</p>
<p>LINE 1: ...rt_node (int8, int4, int4, text[]) AS INSERT INTO planet_osm...</p>
<pre><code>                                                         ^</code></pre>
<p>Error occurred, cleaning up</p>
<hr />
<p>I don't know how to query the database effectively from a command line to confirm if planet_osm_nodes is there or not, but I am right now running renderd, which is querying the db of course, and I am watching the logs in pg_activity, all seems well and tiles are appearing.</p>
<p>Minutely Mapnik had another suggestion for updating the database using osmosis, so I tried that too. Perhaps a bit foolish of me 'cos I don't know what it is doing exactly. I got errors again :-(</p>
<p>%osmosis --read-xml-change file="changes.osc.gz" --write-pgsql-change database=gis Apr 14, 2013 8:31:39 AM org.openstreetmap.osmosis.core.Osmosis run</p>
<p>INFO: Osmosis Version 0.43-SNAPSHOT</p>
<p>Apr 14, 2013 8:31:42 AM org.java.plugin.registry.xml.ManifestParser &lt;init&gt;</p>
<p>INFO: got SAX parser factory - org.apache.xerces.jaxp.SAXParserFactoryImpl@681db8</p>
<p>...more stuff until...</p>
<p>Apr 14, 2013 8:19:43 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion</p>
<p>SEVERE: Thread for task 1-read-xml-change failed</p>
<p>org.springframework.jdbc.BadSqlGrammarException: StatementCallback; bad SQL grammar [SELECT version FROM schema_info]; nested exception is org.postgresql.util.PSQLException: ERROR: relation "schema_info" does not exist</p>
<p>...and so on...</p>
<p>Anybody any ideas about what I have done wrong? I have a copy of the database from before the updates and I will probably go back to that and go through the update steps again to see if I can find where I went wrong.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '13, 09:21</strong></p>
<img src="https://secure.gravatar.com/avatar/1bca123c0c1f7ff52cb5ac0972837cc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Panca%20Kanga&#39;s gravatar image" />
<p><span>Panca Kanga</span><br />
<span class="score" title="30 reputation points">30</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Panca Kanga has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted to question <strong>14 Apr '13, 11:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-21517" class="comments-container">
<span id="21520"></span>
<div id="comment-21520" class="comment">
<div id="post-21520-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Converted to question rather than just a 'me too' on someone else's post.</p>
</div>
<div id="comment-21520-info" class="comment-info">
<span class="comment-age">(14 Apr '13, 11:46)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21517-form-container" class="comment-form-container">
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

<span id="21534"></span>

<div id="answer-container-21534" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21534-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is guessing a bit of what might have gone wrong, but one possible issue is your use of "--drop"</p>
<p>osm2pgsql creates two sets of tables. 1) The rendering tables "planet_osm_point" "planet_osm_line" "planet_osm_roads" and "planet_osm_polygon" and 2) the "slim mode" tables "planet_osm_nodes" "planet_osm_ways" and "planet_osm_rels".</p>
<p>For rendering, only the rendering tables are needed. These contain a lossy (not all tags and data are needed), transformed ( using postgis geometries rather than OSM nodes and ways) version of the OSM data optimised for rendering.</p>
<p>In the slim mode tables on the other hand, the (more or less) original OSM data is stored. This is necessary during the initial import if you don't have enough memory to store everything in RAM and for updating the data with the diff files. It is however not necessary for rendering with renderd.</p>
<p>The --drop option deletes the slim mode tables after the initial import. This is useful if you don't intend to run updates, as it saves time during the initial import and reduces the amount of disk space you need by about half.</p>
<p>If you do want to run updates, you will need to re-import the entire data (UK) from scratch in slim mode and without the --drop option. After that you should be able to do diff imports as described above. But again make sure you don't have the --drop option specified.</p>
<p>1Gb+ for a single days update seems excessive (if that is the compressed size). You can get daily diffs covering the entire planet at <a href="http://planet.openstreetmap.org/replication/day/000/000/">http://planet.openstreetmap.org/replication/day/000/000/</a> and they are about 50 - 100Mb compressed. You can also get daily diff files only for GB at <a href="http://download.geofabrik.de/europe/great-britain-updates/000/000/">http://download.geofabrik.de/europe/great-britain-updates/000/000/</a> which are about 1 - 5Mb in size.</p>
<p>With regard to osmosis, I don't think you can mix osm2pgsql and osmosis databases, as they use an entirely different data layout in the database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '13, 01:57</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-21534" class="comments-container">
&#10;</div>
<div id="comment-tools-21534" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21534-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21562"></span>

<div id="answer-container-21562" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21562-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you very much apmon , that was very clear and helpful, not least because you confirm what I was beginning to suspect about the --drop flag.</p>
<p>I think there were 3 possible contributing causes for the problem I was having:</p>
<ol>
<li>I misused the --drop flag of osm2pgsql</li>
<li>My machine ran out of memory and hung while the database was updating. I had to switch it off to reboot it.</li>
<li>I may have been using a corrupted changes.osc.gz file.</li>
</ol>
<p>The results of these 3 things may have been cumulative but I suspect my inclusion of the --drop flag would have been enough.</p>
<h2 id="the-rest-of-this-email-is-just-an-extension-on-the-above-observation.">The rest of this email is just an extension on the above observation.</h2>
<p>apmon&gt; osm2pgsql creates two sets of tables...</p>
<p>I don't know anything about the structure of the database so this is interesting to find out. Thanks for the explanation.</p>
<p>After I wrote to help.openstreetmap I continued trying to check out what I had done wrong. First I made a new directory-dump of my database. When I compared that dump with the original one it was much smaller in size and contained fewer files. So then I looked up the appropriate pgsql syntax to list the tables and confirmed (as per the error message) that my problem, planet_osm_nodes, among others was indeed missing.</p>
<p>apmon&gt; The --drop option deletes the slim mode tables after the initial import...</p>
<p>osm2pgsql --help suggested that --drop deleted "temporary tables after import", so that misled me, though checking again I see there is a rider: "(no updates)"which was doubtless intended to warn against using --drop with updates. So that would completely explain my lost tables.</p>
<p>I 'drop'ed the existing (broken) database and reloaded the good copy from the dump I made at the end of March.</p>
<p>apmon&gt;If you do want to run updates, you will need to re-import the entire data (UK) from scratch in slim mode ...</p>
<p>In normal circumstances it would be a bit daft rebuild the db from a dump, wouldn't it? It took about as long to load it back in as it takes to download and instal an up-to-date version of the UK db. But it did take me back to where I was so I could try to check the wrong steps I had made.</p>
<p>With the database back I used wget to get the next change file:</p>
<p>%wget <a href="http://download.geofabrik.de/europe/great-britain-updates/000/000/026.osc.g">http://download.geofabrik.de/europe/great-britain-updates/000/000/026.osc.g</a></p>
<p>(I used wget to get one file because I was not entirely sure if I had set up the osmosis replication command correctly).</p>
<p>and used osm2pgsql to add that (Even before your reply I was suspicious about te --drop flag and did not include it):</p>
<p>%osm2pgsql -a -dgis -v -e6-15 -oexpire-list26 -s 026.osc.gz</p>
<p>All the tables were still there. So that was clearly a step in the right direction for me.</p>
<p>So next I set the maxInterval option in configuration.txt to 86400 sec (1 day) and used osmosis to get the next change file in my sequence:</p>
<p>osmosis --read-replication-interval workingDirectory=./ --simplify-change --write-xml-change change27.osc.gz</p>
<p>and added it to the database. All ok.</p>
<p>apmon&gt;...make sure you don't have the --drop option specified.</p>
<p>I was going to try adding a group of changes with the --drop flag included in the osm2pgsql line (just to see what would happen) but I think basically, and thanks to your reply, I can now say "QED" and not risk destroying the db again.</p>
<p>apmon&gt;1Gb+ for a single days update seems excessive (if that is the compressed size)</p>
<p>Originally I had used osmosis to download and merge about 10 days worth of change files, which might explain why the change.osc.gz file was so large. I have deleted the file now so can't confirm the size again. Maybe I just read the output from ls -l wrong. I am quite capable of such a thing.</p>
<p>I have experimented a bit more, and currently, with my setup I can only download one daily file at a time with the above osmosis command. If I put a period of two days (172800 secs) in the config.txt file (or a 0) and try to download and merge two (or more) daily files the command drops out with errors. The errors scrolled off the top of the screen and were not obvious so this is what leads me to think I had previously been using a corrupted change file.</p>
<p>I don't think it is worth reporting this as a bug as the m/c I am using is only a 5 year old laptop installed with fedora18 and with &lt;1G memory and a 1.6GHz Pentium III CPU. I expect it is complicit with whatever faults I might see.</p>
<p>BTW. There is also a bit-count difference between the files returned by osmosis and those downloaded by wget:</p>
<p>ls -l changes-28.osc.gz 028.osc.gz -rw-rw-r--. 1 paka paka 1505042 Mar 31 02:43 028.osc.gz -rw-rw-r--. 1 paka paka 1505053 Apr 15 14:03 changes-28.osc.gz</p>
<p>If you unzip them and run od -x on them they don't look like the same file. I don't know what the significance of that is. Though I assume it is a result of the --simplify-change flag.</p>
<p>apmon&gt;With regard to osmosis, I don't think you can mix osm2pgsql and osmosis databases, as they use an entirely different data layout in the database.</p>
<p>Thank you again. That is worth noting too. Looking back through the osmosis_detailed_usage in the wiki I realised that, as you say, it explains that I would need to do some more work to alter the configuration of the db to work with osmosis.</p>
<p>As I don't exactly understand what it is that should be done - The wiki admits at one point that the term `schema' (the subject of the error when I ran the osmosis command) is context dependant - so I think I will leave well alone, (for now:-) and stick with using osm2pgsql for updating the db.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '13, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/1bca123c0c1f7ff52cb5ac0972837cc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Panca%20Kanga&#39;s gravatar image" />
<p><span>Panca Kanga</span><br />
<span class="score" title="30 reputation points">30</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Panca Kanga has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21562" class="comments-container">
&#10;</div>
<div id="comment-tools-21562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21562-form-container" class="comment-form-container">
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

