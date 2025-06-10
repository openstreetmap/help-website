+++
type = "question"
title = "Russian states are missing in the whole asia map"
description = '''Can someone give any suggestion how can I append missing states (everything left of Moscow, including Moscow) to the russian map in the whole asian file? I tried  osmium merge ./asia-latest.osm.pbf ./northwestern-fed-district-latest.osm.pbf ./central-fed-district-latest.osm.pbf -o merged.pbf  and it...'''
date = "2020-03-06T08:36:00Z"
lastmod = "2020-03-06T12:21:00Z"
weight = 73414
keywords = [ "osmium", "merge", "osmconvert", "asia", "map" ]
aliases = [ "/questions/73414" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Russian states are missing in the whole asia map](/questions/73414/russian-states-are-missing-in-the-whole-asia-map)

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
<span id="post-73414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73414-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can someone give any suggestion how can I append missing states (everything left of Moscow, including Moscow) to the russian map in the whole asian file? I tried</p>
<pre><code>osmium merge ./asia-latest.osm.pbf ./northwestern-fed-district-latest.osm.pbf ./central-fed-district-latest.osm.pbf -o merged.pbf</code></pre>
<p>and it crashed when porting nodes to the database: Processing: Node(1255048k 1457.7k/s) Way(156069k 11.50k/s) Relation(0 0.00/s)result COPY END for planet_osm_ways failed: ERROR: duplicate key value violates unique constraint "planet_osm_ways_pkey" DETAIL: Key (id)=(23535867) already exists. CONTEXT: COPY planet_osm_ways, line 119375 DB copy thread failed: Ending COPY mode</p>
<p>Then I tried converting all files to "o5m" extension and run:</p>
<pre><code>osmconvert centr.o5m sev_zapad.o5m asia.o5m -o=merge_again.osm.pbf</code></pre>
<p>Now it all just turned out to give me the same asia map with no tiles added.</p>
<p>Update:</p>
<p>it turned out that when I manually zoomed closer, some mssing tiles were served, but at lower (0-6) zooms I still get empty tiles. Another thing: after I cleared "/var/lib/mod_tile" folder of rendered tiles and tried to draw the map, there didn't seem to be any rendering done, linke there is another place where already rendered tiles are stored. Is it possible that Mapnik keeps some separate cache for it tiles? How can I clear it?</p>
<p>And another problem, after I run:</p>
<pre><code>render_list -a -Z 10 -n 5 --socket=/var/run/renderd/renderd.sock -m ajt -f</code></pre>
<p>the systems starts doing something very hard (all 5 cores are loaded at 100%) but new maps in "/var/lib/mod_tile" appear at a very slow rate. I have already run this command with the previous map and it took less then a couple seconds to render 0-8 zoom levels, and now it took about 10 minutes and the processor was left covered in sweat. Why is that?</p>
<p>Another update:</p>
<p>Actually the command</p>
<pre><code>osmconvert centr.o5m sev_zapad.o5m asia.o5m -o=merge_again.osm.pbf</code></pre>
<p>worked ok. It was just that I had to use -f with a render_list to rerender all prevous blank tiles so they get updated with new data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-asia" rel="tag" title="see questions tagged &#39;asia&#39;">asia</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '20, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/7d9dea8db6c9981b45d28f28bb29f49d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartman1&#39;s gravatar image" />
<p><span>kartman1</span><br />
<span class="score" title="38 reputation points">38</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartman1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>06 Mar '20, 12:23</strong> </span></p>
</div>
</div>
<div id="comments-container-73414" class="comments-container">
&#10;</div>
<div id="comment-tools-73414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73414-form-container" class="comment-form-container">
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

<span id="73418"></span>

<div id="answer-container-73418" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73418-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kartman1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>osmium merge</code> is supposed to handle duplicates but there may be corner cases where this will fail, especially if you are using files that were not downloaded at the same time.</p>
<p>What I would suggest that you do is, rather than using an Asia extract and trying to add pieces to it, create your own extract from the planet file:</p>
<ol>
<li>download <code>planet-latest.osm.pbf</code></li>
<li>create an extract with <code>osmium extract</code></li>
<li>feed that into <code>osm2pgsql</code></li>
</ol>
<p>The extract creation is documented on <a href="https://docs.osmcode.org/osmium/latest/osmium-extract.html">https://docs.osmcode.org/osmium/latest/osmium-extract.html</a> - basically if you can work with a rectangular area you would call</p>
<pre><code>osmium extract --bbox 24.52,7.64,172.88,77.15 -s smart planet-latest.osm.pbf -o myfile.osm.pbf</code></pre>
<p>and if you'd rather cut out a polygon you would have to define a simple outline first e.g. using QGIS (save as GeoJSON) or JOSM (save as poly file), then use the <code>--polygon</code> flag instead of <code>--bbox</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '20, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '20, 10:42</strong> </span></p>
</div>
</div>
<div id="comments-container-73418" class="comments-container">
<span id="73422"></span>
<div id="comment-73422" class="comment">
<div id="post-73422-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I'll mark it as an answer though I didn't try it, because the command from the question actually worked.</p>
</div>
<div id="comment-73422-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 12:21)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
</div>
<div id="comment-tools-73418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73418-form-container" class="comment-form-container">
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

