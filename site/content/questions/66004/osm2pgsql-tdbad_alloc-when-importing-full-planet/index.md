+++
type = "question"
title = "osm2pgsql td::bad_alloc when importing full planet"
description = '''Hi, I&#x27;ve imported France successfully and now I&#x27;m trying to import the full planet but can&#x27;t get to the end of it. I&#x27;ve logged the output of osm2pgsql and seen a bad_alloc message: osm2pgsql version 0.96.0 (64 bit id space)  Using built-in tag processing pipeline Using projection SRS 3857 (Spherical...'''
date = "2018-09-21T16:26:00Z"
lastmod = "2018-09-27T16:08:00Z"
weight = 66004
keywords = [ "allocate", "ram", "osm2pgsql", "memory" ]
aliases = [ "/questions/66004" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql td::bad_alloc when importing full planet](/questions/66004/osm2pgsql-tdbad_alloc-when-importing-full-planet)

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
<span id="post-66004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66004-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've imported France successfully and now I'm trying to import the full planet but can't get to the end of it. I've logged the output of osm2pgsql and seen a bad_alloc message:</p>
<pre><code>osm2pgsql version 0.96.0 (64 bit id space)
&#10;Using built-in tag processing pipeline
Using projection SRS 3857 (Spherical Mercator)
Setting up table: planet_osm_point
Setting up table: planet_osm_line
Setting up table: planet_osm_polygon
Setting up table: planet_osm_roads
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=18000MB, maxblocks=288000*65536, allocation method=11
Mid: loading persistent node cache from /home/renderer/data/flat_nodes/flat_nodes.bin
Mid: pgsql, cache=18000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /data.osm.pbf
Using PBF parser.
Processing: Node(4725081k 9431.3k/s) Way(523620k 4.45k/s) Relation(646430 43.55/s)terminate called after throwing an instance of &#39;std::bad_alloc&#39;
  what():  std::bad_alloc</code></pre>
<p><strong>And I also have some errors and fatals on the postgresql logs (EOF, terminating connection), but I supposed both are linked:</strong></p>
<pre><code>2018-09-20 21:35:26.442 GMT [134] LOG:  unexpected EOF on client connection with an open transaction
2018-09-20 21:35:26.442 GMT [138] LOG:  incomplete message from client
2018-09-20 21:35:26.442 GMT [138] CONTEXT:  COPY planet_osm_rels, line 646433
2018-09-20 21:35:26.442 GMT [138] STATEMENT:  COPY planet_osm_rels FROM STDIN;
&#10;2018-09-20 21:35:26.442 GMT [133] LOG:  incomplete message from client
2018-09-20 21:35:26.442 GMT [133] CONTEXT:  COPY planet_osm_line, line 116
2018-09-20 21:35:26.442 GMT [133] STATEMENT:  COPY planet_osm_line (osm_id,&quot;access&quot;,&quot;admin_level&quot;,&quot;aerialway&quot;,&quot;aeroway&quot;,&quot;amenity&quot;,&quot;area&quot;,&quot;barrier&quot;,&quot;bridge&quot;,&quot;boundary&quot;,&quot;building&quot;,&quot;highway&quot;,&quot;landuse&quot;,&quot;layer&quot;,&quot;leisure&quot;,&quot;name&quot;,&quot;int_name&quot;,&quot;natural&quot;,&quot;oneway&quot;,&quot;place&quot;,&quot;population&quot;,&quot;railway&quot;,&quot;ref&quot;,&quot;service&quot;,&quot;tourism&quot;,&quot;tunnel&quot;,&quot;water&quot;,&quot;waterway&quot;,&quot;wetland&quot;,&quot;z_order&quot;,&quot;way_area&quot;,&quot;piste:type&quot;,&quot;piste:difficulty&quot;,tags,way) FROM STDIN
2018-09-20 21:35:26.442 GMT [135] LOG:  unexpected EOF on client connection with an open transaction
2018-09-20 21:35:26.444 GMT [137] LOG:  unexpected EOF on client connection with an open transaction
2018-09-20 21:35:26.447 GMT [133] ERROR:  unexpected EOF on client connection with an open transaction
2018-09-20 21:35:26.447 GMT [133] CONTEXT:  COPY planet_osm_line, line 116
2018-09-20 21:35:26.447 GMT [133] STATEMENT:  COPY planet_osm_line (osm_id,&quot;access&quot;,&quot;admin_level&quot;,&quot;aerialway&quot;,&quot;aeroway&quot;,&quot;amenity&quot;,&quot;area&quot;,&quot;barrier&quot;,&quot;bridge&quot;,&quot;boundary&quot;,&quot;building&quot;,&quot;highway&quot;,&quot;landuse&quot;,&quot;layer&quot;,&quot;leisure&quot;,&quot;name&quot;,&quot;int_name&quot;,&quot;natural&quot;,&quot;oneway&quot;,&quot;place&quot;,&quot;population&quot;,&quot;railway&quot;,&quot;ref&quot;,&quot;service&quot;,&quot;tourism&quot;,&quot;tunnel&quot;,&quot;water&quot;,&quot;waterway&quot;,&quot;wetland&quot;,&quot;z_order&quot;,&quot;way_area&quot;,&quot;piste:type&quot;,&quot;piste:difficulty&quot;,tags,way) FROM STDIN
2018-09-20 21:35:26.449 GMT [138] ERROR:  unexpected EOF on client connection with an open transaction
2018-09-20 21:35:26.449 GMT [138] CONTEXT:  COPY planet_osm_rels, line 646433
2018-09-20 21:35:26.449 GMT [138] STATEMENT:  COPY planet_osm_rels FROM STDIN;
&#10;2018-09-20 21:35:26.451 GMT [136] ERROR:  unexpected EOF on client connection with an open transaction
2018-09-20 21:35:26.451 GMT [136] CONTEXT:  COPY planet_osm_nodes, line 1
2018-09-20 21:35:26.451 GMT [136] STATEMENT:  COPY planet_osm_nodes FROM STDIN;
&#10;2018-09-20 21:35:26.453 GMT [132] LOG:  incomplete message from client
2018-09-20 21:35:26.482 GMT [136] FATAL:  terminating connection because protocol synchronization was lost
2018-09-20 21:35:26.494 GMT [136] LOG:  could not send data to client: Broken pipe
2018-09-20 21:35:26.498 GMT [138] FATAL:  terminating connection because protocol synchronization was lost
2018-09-20 21:35:26.498 GMT [138] LOG:  could not send data to client: Broken pipe
2018-09-20 21:35:26.647 GMT [133] FATAL:  terminating connection because protocol synchronization was lost
2018-09-20 21:35:26.647 GMT [133] LOG:  could not send data to client: Broken pipe</code></pre>
<p>I was importing with the following command:</p>
<p><code>osm2pgsql -d ${DBNAME} -H ${DBHOST} -P ${DBPORT} -U ${DBUSER} --create --slim -G --hstore --hstore-match-only -C 8000 --number-processes 8 -S /home/renderer/src/custom.style --flat-nodes /home/renderer/data/flat_nodes/flat_nodes.bin /data.osm.pbf</code></p>
<p>I have 32Gb of RAM, 8 cores, 1Gb of SWAP and 1Tb SSD (that's why I'm using flat-nodes). I've also tried with the -C option at 18000 (I've seen somewhere that beyond that value there was no difference). But I still have the issue. I really don't see how I could have a memory problem knowing that when I checked the usage during the import, I was around 20Gb of use max...</p>
<p>I've seen <a href="https://github.com/openstreetmap/osm2pgsql/issues/855">this github issue</a> where it is advised to increase swap size but it seems strange to me, isn't the swap supposed to be used then de RAM is full? Anyway this would be a last resort solution. Also a guy suggest to remove the -C option and that will let osm2pgsql use what it needs, so I'm trying that right now but it seems strange too because I've seen in <a href="http://www.volkerschatz.com/net/osm/osm2pgsql-usage.html">that doc</a> that the default value is 800 if the parameter is not written.</p>
<p>I'm monitoring the usage of my server with this last solution just now, and the swap is almost full (960/1021MB), while the RAM is free (only 2Gb used on 32...).</p>
<p>Does anybody have any idea of where this problem may come from? And what I should do to successfully import the whole planet?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-allocate" rel="tag" title="see questions tagged &#39;allocate&#39;">allocate</span> <span class="post-tag tag-link-ram" rel="tag" title="see questions tagged &#39;ram&#39;">ram</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '18, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/32a7da9bf999cc0ea4f6befea00edd8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voharunado&#39;s gravatar image" />
<p><span>voharunado</span><br />
<span class="score" title="66 reputation points">66</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voharunado has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66004" class="comments-container">
&#10;</div>
<div id="comment-tools-66004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66004-form-container" class="comment-form-container">
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

<span id="66015"></span>

<div id="answer-container-66015" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66015-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Surprisingly enough software changes now and then and you shouldn't be assuming that tips given for older version still apply now.</p>
<p>Current versions of osm2pgsql use a much more efficient caching algorithm and will not degrade as much as previous ones, which essentially required a cache large enough to keep all nodes in memory.</p>
<p>In any case 1GB swap is not going to get you anywhere, 64 would be more like it (don't forget you have pgsql processes any lots of other stuff running during the import too), maybe even 128.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '18, 08:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '18, 08:37</strong> </span></p>
</div>
</div>
<div id="comments-container-66015" class="comments-container">
<span id="66032"></span>
<div id="comment-66032" class="comment">
<div id="post-66032-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for that advice, it still seems strange to me because I thought the RAM was used first, so with 32Gb of it, I assume I wouldn't need much swap. Anyway, I tried this weekend to remove de -C option (as advised in the github issue I linked) and the process terminated without the bad_alloc message. I still have an error but not related to memory, so if it works, I'll stay with that.</p>
</div>
<div id="comment-66032-info" class="comment-info">
<span class="comment-age">(24 Sep '18, 10:26)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="66035"></span>
<div id="comment-66035" class="comment">
<div id="post-66035-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I successfully passed the processing step by removing the <code>-C</code> option from my osm2pgsql command. The process didn't go further but for a totally different reason not relevant to this topic. But I still wonder if this advice I've seen on github is good, because it seems to me that this will tell osm2pgsql to use only 800Mb of RAM so this will inevitably slow down the process no? It may have allowed me to continue the process beyond the processing step but I'm afraid I will loose a lot of time for the rest of the import...</p>
</div>
<div id="comment-66035-info" class="comment-info">
<span class="comment-age">(24 Sep '18, 15:19)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="66071"></span>
<div id="comment-66071" class="comment">
<div id="post-66071-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can now confirm that removing the -C option worked.</p>
<p>However the full planet import took almost 3 days (244721s), but I just wanted it to work so it's fine for me.</p>
</div>
<div id="comment-66071-info" class="comment-info">
<span class="comment-age">(27 Sep '18, 16:08)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
</div>
<div id="comment-tools-66015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66015-form-container" class="comment-form-container">
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

