+++
type = "question"
title = "How to tell if OSM2PGSQL finished successfully?"
description = '''Hi there. Thank you for your help in advance! I am new to setting up my own OSM Tile Server. I followed the instructions here: https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/ Question: My question is how to determine if osm2pgsql has finished successfully while runnin...'''
date = "2020-03-30T17:17:00Z"
lastmod = "2020-03-30T19:08:00Z"
weight = 73870
keywords = [ "planet", "osm2pgsql", "success" ]
aliases = [ "/questions/73870" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to tell if OSM2PGSQL finished successfully?](/questions/73870/how-to-tell-if-osm2pgsql-finished-successfully)

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
<span id="post-73870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73870-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there. Thank you for your help in advance!</p>
<p>I am new to setting up my own OSM Tile Server. I followed the instructions here: <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/</a></p>
<p>Question: My question is how to determine if osm2pgsql has finished successfully while running the command in the background?</p>
<p>Note: This is related to importing the Planet OSM file (more details below). The test import of Azerbaijan detailed in the setup instructions did work as documented, so I know the basic setup is working.</p>
<p>I reviewed the "/var/log/syslog" file and I don't see any messages "success" related to "osm". However, several times when the import failed, there were messages related to the failure - mainly that osm2pgsql had been killed.</p>
<p>Can anyone suggest how I can validate that osm2pgsql did indeed finish successfully? Or is there another place I should be looking for logs?</p>
<p>More Details (in case these help):</p>
<p>I was able to get the basic server running and did the test included in the instructions and confirmed that the software was running properly.</p>
<p>I then imported the Planet OSM file. This required several attempts and tweaks and I referred to multiple helpful pages and posts on the web.</p>
<p>I "think" I was finally successful in importing the Planet OSM file with the following command: sudo -u ubuntu osm2pgsql -d gis --create --slim --flat-nodes 'nodes.bin' --cache-strategy dense -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/planet-latest.osm.pbf &gt;out.txt 2&gt;/dev/null &amp;</p>
<p>My machine is an AWS EC2 m5.2xlarge instance (8 vCPUs and 32 GB RAM) with a 1.3 TB Disk - EBS Volume).</p>
<p>I think peak disk usage reached about 1.2 TB and it took 3 days to run.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-success" rel="tag" title="see questions tagged &#39;success&#39;">success</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '20, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/1b58f01d0ae94d1c1f788e287efeacdf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Buzz1000&#39;s gravatar image" />
<p><span>Buzz1000</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Buzz1000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73870" class="comments-container">
<span id="73873"></span>
<div id="comment-73873" class="comment">
<div id="post-73873-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If anything is going to run for a while, I tend to use "screen" and detach (using ^a^d) from it while doing something else. Then "screen -r" to reconnect to see how the process is getting along. That way you'll always see the last line of any output.</p>
<p>You can also try redirecting output, or using typescript, but osm2pgsql is quite verbose.</p>
</div>
<div id="comment-73873-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 17:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73874"></span>
<div id="comment-73874" class="comment">
<div id="post-73874-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the ideas. I tried redirecting the output to a file initially but as you said, it is quite verbose and I got worried that just the output would eat up all my disk space.</p>
<p>I'll give "screen+detach" a try. In case you know this off the top and if you will indulge a newb question - will "screen+detach" work even if I log off the machine or do I have to keep the same SSH session alive all through the import? Unfortunately I have to log off once I start the job so I need a way that keeps stuff running even then.</p>
</div>
<div id="comment-73874-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 18:07)</span> <span class="comment-user userinfo">Buzz1000</span>
</div>
</div>
<span id="73877"></span>
<div id="comment-73877" class="comment">
<div id="post-73877-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>will "screen+detach" work even if I log off the machine</p>
</blockquote>
<p>yes</p>
<blockquote>
<p>or do I have to keep the same SSH session alive all through the import?</p>
</blockquote>
<p>If something kills the "SCREEN" process then bad things will happen. Otherwise you'll see something like this:</p>
<pre><code>me@mymachine:~$ ps -ef | grep 1628
ajtown    1628     1  0 Mar02 ?        00:00:08 SCREEN
ajtown    1629  1628  0 Mar02 pts/1    00:00:00 /bin/bash
ajtown   25162 25135  0 20:04 pts/2    00:00:00 grep --color=auto 1628</code></pre>
<p>"pts/1" is running something via screen, and has been since March 2nd. The original session was logged out, but I can reconnect via "screen -r" any time I want. What I can't guarantee is what happens when your machine completely runs out of memory - my experience is that osm2pgsql would be killed and not "SCREEN", but I can't guarantee that.</p>
</div>
<div id="comment-73877-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 19:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73870-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

