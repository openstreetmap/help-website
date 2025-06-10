+++
type = "question"
title = "Nominatim installation error: Out of memory for node cache dense index"
description = '''I am installing Nominatim on my Ubuntu server 14.04 through this link and trying to load OSM data into my postgreSQL database. For loading into my database I am using this command as given in the link: ~/Nominatim/utils/setup.php --osm-file data/latest.osm.pbf --all --osm2pgsql-cache 1024 2&amp;gt;&amp;amp;...'''
date = "2015-08-12T18:49:00Z"
lastmod = "2015-08-13T05:44:00Z"
weight = 44750
keywords = [ "openstreetmap", "osm", "nominatim", "postgresql", "osm2pgsql" ]
aliases = [ "/questions/44750" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim installation error: Out of memory for node cache dense index](/questions/44750/nominatim-installation-error-out-of-memory-for-node-cache-dense-index)

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
<span id="post-44750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44750-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am installing Nominatim on my Ubuntu server 14.04 through this <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">link</a> and trying to load OSM data into my postgreSQL database. For loading into my database I am using this command as given in the link:</p>
<pre><code>~/Nominatim/utils/setup.php   --osm-file data/latest.osm.pbf   --all --osm2pgsql-cache 1024 2&gt;&amp;1   | tee setup.log</code></pre>
<p>But it is throwing an error</p>
<pre><code>Using projection SRS 4326 (Latlong)
NOTICE:  table &quot;place&quot; does not exist, skipping
NOTICE:  type &quot;keyvalue&quot; does not exist, skipping
NOTICE:  type &quot;wordscore&quot; does not exist, skipping
NOTICE:  type &quot;stringlanguagetype&quot; does not exist, skipping
NOTICE:  type &quot;keyvaluetype&quot; does not exist, skipping
NOTICE:  function get_connected_ways(pg_catalog.int4[]) does not exist,  skipping
Allocating memory for dense node cache
Out of memory for node cache dense index, try using &quot;--cache-strategy  sparse&quot; instead
Error occurred, cleaning up
ERROR: Error executing external command: /home/nominatim/Nominatim /osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 256 -P 5432 -d nominatim /home/nominatim/data/latest.osm.pbf
Error executing external command: /home/nominatim/Nominatim/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 256 -P 5432 -d nominatim /home/nominatim/data/latest.osm.pbf</code></pre>
<p>My ubuntu has 7GB of RAM and I am not sure why this error is coming. I ran the above command by reducing the cache size to 512 and then 256 but it is running into same error. I am not sure how to use <code>--cache-strategy sparse</code> in the given command.</p>
<p>Screenshot of my Error: <a href="http://i.stack.imgur.com/wjE2n.jpg"><img src="http://i.stack.imgur.com/wjE2n.jpg" alt="enter image description here" /></a></p>
<p>Could anybody help with the setup?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '15, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/b4d7e238ae2638257c3d613bc27836f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rakesh534&#39;s gravatar image" />
<p><span>Rakesh534</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rakesh534 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-44750" class="comments-container">
<span id="44752"></span>
<div id="comment-44752" class="comment">
<div id="post-44752-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>cross post: <a href="http://gis.stackexchange.com/questions/158051/nominatim-installation-error-out-of-memory-for-node-cache-dense-index">http://gis.stackexchange.com/questions/158051/nominatim-installation-error-out-of-memory-for-node-cache-dense-index</a></p>
</div>
<div id="comment-44752-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 19:07)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-44750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44750-form-container" class="comment-form-container">
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

<span id="44755"></span>

<div id="answer-container-44755" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44755-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have resolved this issue.</p>
<p>Go through this link and follow all the instructions posted there.</p>
<p><a href="https://github.com/twain47/Nominatim/issues/306">Problem Resolved</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '15, 05:44</strong></p>
<img src="https://secure.gravatar.com/avatar/b4d7e238ae2638257c3d613bc27836f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rakesh534&#39;s gravatar image" />
<p><span>Rakesh534</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rakesh534 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44755" class="comments-container">
&#10;</div>
<div id="comment-tools-44755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44755-form-container" class="comment-form-container">
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

