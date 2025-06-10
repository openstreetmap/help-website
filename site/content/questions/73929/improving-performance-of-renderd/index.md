+++
type = "question"
title = "Improving performance of renderd"
description = '''Hello, I am running my own OSM server setup as per the instructions on switch2osm.org (Manually building a tile server (18.04 LTS). Renderd (or rather PostgreSQL) is working quite slowly. From everything I have read, this is to be expected the first time that it generates tiles for an area. However,...'''
date = "2020-04-01T17:14:00Z"
lastmod = "2020-04-02T18:21:00Z"
weight = 73929
keywords = [ "performance", "tiles", "renderd", "postgresql", "rendering" ]
aliases = [ "/questions/73929" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Improving performance of renderd](/questions/73929/improving-performance-of-renderd)

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
<span id="post-73929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73929-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am running my own OSM server setup as per the instructions on switch2osm.org (<a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">Manually building a tile server (18.04 LTS)</a>.</p>
<p>Renderd (or rather PostgreSQL) is working quite slowly. From everything I have read, this is to be expected the first time that it generates tiles for an area.</p>
<p>However, are there any performance tune-ups that anyone can suggest to speed up PostgreSQL specifically for Renderd?</p>
<p>I have a m5.2xlarge machine in AWS EC2 (32 GB RAM, 1.5TB SSD (EBS), 8 vCPUs (4 Cores x 2 Threads per Core)). I think that this size of machine should perform faster than it is right now.</p>
<p>Here are some sample renderd results from "/var/log/syslog"</p>
<pre><code>Apr  1 07:54:36 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 17 83680-83687 49440-49447, age 4.69 days
Apr  1 07:54:36 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 17 83672-83679 49440-49447, age 4.69 days
Apr  1 07:54:36 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 16 41840-41847 24720-24727, age 4.12 days
Apr  1 07:54:36 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 16 41832-41839 24720-24727, age 4.12 days
Apr  1 07:54:40 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 17 83672-83679 49440-49447 in 3.643 seconds
Apr  1 07:54:40 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 15 20912-20919 12360-12367, age 3.68 days
Apr  1 07:54:40 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 17 83680-83687 49440-49447 in 3.822 seconds
Apr  1 07:54:40 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 15 20920-20927 12360-12367, age 3.56 days
Apr  1 07:54:40 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 16 41840-41847 24720-24727 in 3.339 seconds
Apr  1 07:54:40 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 14 10456-10463 6176-6183, age 3.62 days
Apr  1 07:54:40 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 16 41832-41839 24720-24727 in 3.657 seconds
Apr  1 07:54:43 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 15 20920-20927 12360-12367 in 3.146 seconds
Apr  1 07:54:43 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 15 20912-20919 12360-12367 in 3.624 seconds
Apr  1 07:54:45 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 14 10456-10463 6176-6183 in 5.515 seconds
Apr  1 07:55:13 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 13 5224-5231 3088-3095, age 3.72 days
Apr  1 07:55:18 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 13 5224-5231 3088-3095 in 4.517 seconds
Apr  1 07:55:22 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 10 656-663 384-391, age 3.08 days
Apr  1 07:55:23 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 9 320-327 192-199, age 3.10 days
Apr  1 07:55:23 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 9 328-335 192-199, age 3.10 days
Apr  1 07:55:24 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 8 160-167 88-95, age 3.05 days
Apr  1 07:55:25 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 10 656-663 384-391 in 2.751 seconds
Apr  1 07:55:25 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 8 160-167 96-103, age 3.10 days
Apr  1 07:55:30 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 9 328-335 192-199 in 7.276 seconds
Apr  1 07:55:30 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 7 80-87 48-55, age 3.05 days
Apr  1 07:55:49 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 9 320-327 192-199 in 26.345 seconds
Apr  1 07:55:49 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 7 80-87 40-47, age 3.04 days
Apr  1 07:56:18 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 8 160-167 96-103 in 53.762 seconds
Apr  1 07:56:18 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 8 136-143 88-95, new metatile
Apr  1 07:56:18 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 8 160-167 88-95 in 54.763 seconds
Apr  1 07:56:18 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 7 72-79 48-55, age 3.04 days
Apr  1 07:56:31 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 7 80-87 48-55 in 60.663 seconds
Apr  1 07:56:31 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 6 40-47 16-23, age 3.01 days
Apr  1 08:00:27 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 7 72-79 48-55 in 248.214 seconds
Apr  1 08:00:27 ip-172-30-0-160 renderd[30679]: DEBUG: START TILE ajt 8 136-143 80-87, new metatile
Apr  1 08:39:57 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 7 80-87 40-47 in 2647.823 seconds
Apr  1 09:00:17 ip-172-30-0-160 renderd[30679]: DEBUG: DONE TILE ajt 6 40-47 16-23 in 3826.766 seconds</code></pre>
<p>It gets super slow in that zoom level sweet spot of 6, 7, or 8. I understand that these intermediate zoom levels have the most data to process.</p>
<p>From various places around the web, I have gotten tidbits of information to speedup the performance. - I have set the PostgreSQL "maintenance_work_mem" setting to 64 MB (<a href="https://www.youtube.com/watch?v=Lxloo42gl8A">https://www.youtube.com/watch?v=Lxloo42gl8A</a>) - Renderd "num_threads" is the default 4 (<a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Tuning_renderd_memory_usage">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Tuning_renderd_memory_usage</a>)</p>
<p>I also came across this StackExchange post (<a href="https://gis.stackexchange.com/questions/181728/mod-tile-not-using-all-available-threads">https://gis.stackexchange.com/questions/181728/mod-tile-not-using-all-available-threads</a>) from several years ago that indicates that maybe the right indexes don't exist on my PostgreSQL setup.</p>
<p>I ran the suggested command to see the indexes</p>
<pre><code>SELECT relname, indexrelname, idx_scan, idx_tup_read, idx_tup_fetch 
FROM pg_stat_all_indexes 
WHERE schemaname = &#39;public&#39; order by 1;</code></pre>
<p>Here is the output</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screen_Shot_2020-04-01_at_9.12.25_AM.png" alt="alt text" /></p>
<p>Can anyone comment on my setup and / or suggest any way of speeding up Renderd/PostgreSQL?</p>
<p>I also tried running render_list to pre-render tiles but it ran for several hours without giving me any indication that it was doing anything - there were no messages on the screen indicating any progress, and "ps -aux" indicated that the total time run by render_list was 0:00. Maybe I was looking in the wrong place for progress information?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '20, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/1b58f01d0ae94d1c1f788e287efeacdf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Buzz1000&#39;s gravatar image" />
<p><span>Buzz1000</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Buzz1000 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '20, 18:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-73929" class="comments-container">
&#10;</div>
<div id="comment-tools-73929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73929-form-container" class="comment-form-container">
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

<span id="73967"></span>

<div id="answer-container-73967" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73967-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The numbers from renderd in /var/log/syslog are alright.</p>
<p>You just have to pre_render most of the tiles for at least up to zoom 12.</p>
<p>But the way you are telling it, your prerendering failed. Did you miss the -m {mapname} param or the -a (or --all) in your render_list call? (I think it would be -m ajt in your case).</p>
<p>You should start pre-rendering by calling</p>
<pre><code>render_list -m ajt -z 0 -Z 12 -n 4 -l 20 --all</code></pre>
<p>and watch /var/log/syslog | grep renderd to see if the prerendering is working.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '20, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-73967" class="comments-container">
<span id="73968"></span>
<div id="comment-73968" class="comment">
<div id="post-73968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for confirming the numbers.</p>
<p>I have run render_list again and am seeing progress. Thanks for pointing out to use "/var/log/syslog | grep renderd". This shows progress being made.</p>
</div>
<div id="comment-73968-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 18:15)</span> <span class="comment-user userinfo">Buzz1000</span>
</div>
</div>
<span id="73969"></span>
<div id="comment-73969" class="comment">
<div id="post-73969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you running full planet or just a country/region? If it's the former (planet) than just wait for some days now for the prerendering to run thru.</p>
</div>
<div id="comment-73969-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 18:21)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-73967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73967-form-container" class="comment-form-container">
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

