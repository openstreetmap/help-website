+++
type = "question"
title = "Duplicate key error when appending diffs with osm2pgsql"
description = '''Hi, I imported a planet pbf with osm2pgsql using this command line: osm2pgsql -c -k -d &amp;lt;dbname&amp;gt; -s -G -K -U &amp;lt;user&amp;gt; -W -H &amp;lt;host&amp;gt; -S &amp;lt;custom.style&amp;gt; planet-200224.osm.pbf I&#x27;m now trying to update with minutely diffs and keep getting duplicate key errors no matter what settings I...'''
date = "2020-03-12T22:42:00Z"
lastmod = "2020-03-17T06:06:00Z"
weight = 73498
keywords = [ "planet", "diff", "pbf", "osm2pgsql", "osmosis" ]
aliases = [ "/questions/73498" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate key error when appending diffs with osm2pgsql](/questions/73498/duplicate-key-error-when-appending-diffs-with-osm2pgsql)

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
<span id="post-73498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73498-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I imported a planet pbf with osm2pgsql using this command line:</p>
<p>osm2pgsql -c -k -d &lt;dbname&gt; -s -G -K -U &lt;user&gt; -W -H &lt;host&gt; -S &lt;custom.style&gt; planet-200224.osm.pbf</p>
<p>I'm now trying to update with minutely diffs and keep getting duplicate key errors no matter what settings I try. The command line for diffs is:</p>
<p>osmosis --rri workingDirectory=/mnt/OSM/osmosis-minutely/ --sc --wxc - | osm2pgsql -a -k -d &lt;dbname&gt; -P 5432 -s -G -K -U &lt;user&gt; -W -H &lt;host&gt; -S custom.style -</p>
<p>I'm using 64-bit osm2pgsql (v 1.2.1). I've tried adding swap space, specifying multiple -C values (2000 up to 16000), number of processes from 1 to 8, importing 60 seconds at a time up to 1 hour, always the same error.</p>
<p>The error I'm getting is this:</p>
<p><img src="/upfiles/Screen_Shot_2020-03-12_at_3.42.57_PM.png" alt="alt text" /></p>
<p>Thanks in advance for any assistance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '20, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/3d2f621468caf19f818a4efaf77c4a0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skmoore&#39;s gravatar image" />
<p><span>skmoore</span><br />
<span class="score" title="25 reputation points">25</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skmoore has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '20, 22:43</strong> </span></p>
</div>
</div>
<div id="comments-container-73498" class="comments-container">
<span id="73509"></span>
<div id="comment-73509" class="comment">
<div id="post-73509-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there any danger in removing the unique constraint on the id column from the nodes/ways/rels tables in Postgres to work around this?</p>
</div>
<div id="comment-73509-info" class="comment-info">
<span class="comment-age">(13 Mar '20, 23:09)</span> <span class="comment-user userinfo">skmoore</span>
</div>
</div>
<span id="73510"></span>
<div id="comment-73510" class="comment">
<div id="post-73510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What's in the change file that you get the error with?</p>
</div>
<div id="comment-73510-info" class="comment-info">
<span class="comment-age">(13 Mar '20, 23:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73511"></span>
<div id="comment-73511" class="comment">
<div id="post-73511-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I get it with any change file. Whether its minutely/hourly, etc. I have it scheduled with cron and I've let it run for several hours, get the same error for each changeset.</p>
<p>I have seen it successfully process a minutely diff a couple of times though, which is weird. That makes me think it's more of a RAM issue on the server, but there appears to plenty of free RAM...</p>
<p>It's a 4 core 16gb ec2 instance connecting to an RDS Postgres instance.</p>
</div>
<div id="comment-73511-info" class="comment-info">
<span class="comment-age">(13 Mar '20, 23:45)</span> <span class="comment-user userinfo">skmoore</span>
</div>
</div>
<span id="73512"></span>
<div id="comment-73512" class="comment">
<div id="post-73512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(perhaps I should have been more precise in the question).</p>
<p>What data is there in the change file that is interpreted as a duplicate key?</p>
</div>
<div id="comment-73512-info" class="comment-info">
<span class="comment-age">(13 Mar '20, 23:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73513"></span>
<div id="comment-73513" class="comment">
<div id="post-73513-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems to almost always be a node (think I saw an error on a way a couple times). I've checked the nodes table in the database for several of the duplicate features, some exist there and some do not.</p>
</div>
<div id="comment-73513-info" class="comment-info">
<span class="comment-age">(13 Mar '20, 23:49)</span> <span class="comment-user userinfo">skmoore</span>
</div>
</div>
<span id="73514"></span>
<div id="comment-73514" class="comment not_top_scorer">
<div id="post-73514-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For example, the last time I ran it I got this error, the node is question does not exist in the Postgres database:</p>
<p>Processing: Node(170k 0.2k/s) Way(0k 0.00k/s) Relation(0 0.00/s)DB writer thread failed due to ERROR: result COPY_END for planet_osm_nodes failed: ERROR: duplicate key value violates unique constraint "planet_osm_nodes_pkey" DETAIL: Key (id)=(33442470) already exists. CONTEXT: COPY planet_osm_nodes, line 40</p>
</div>
<div id="comment-73514-info" class="comment-info">
<span class="comment-age">(13 Mar '20, 23:55)</span> <span class="comment-user userinfo">skmoore</span>
</div>
</div>
</div>
<div id="comment-tools-73498" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-73498-form-container" class="comment-form-container">
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

<span id="73523"></span>

<div id="answer-container-73523" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73523-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to remove duplicates from the change file before importing into osm2pgsql. In osmosis the relevant option is called <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.47#--simplify-change_.28--simc.29"><code>--simplify-change</code> (<code>--simc</code>)</a>. So your command line should be this:</p>
<pre><code>osmosis --rri workingDirectory=/mnt/OSM/osmosis-minutely/ --simc --wxc - | ...</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '20, 10:46</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-73523" class="comments-container">
<span id="73563"></span>
<div id="comment-73563" class="comment">
<div id="post-73563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting, that seems to have worked but I don't recall needing that option in the past. Thanks so much for your help!</p>
</div>
<div id="comment-73563-info" class="comment-info">
<span class="comment-age">(17 Mar '20, 06:06)</span> <span class="comment-user userinfo">skmoore</span>
</div>
</div>
</div>
<div id="comment-tools-73523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73523-form-container" class="comment-form-container">
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

