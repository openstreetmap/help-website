+++
type = "question"
title = "osm2pgsql import getting killed"
description = '''When I try to import planet-latest.osm.pbf I get the following error: /usr/local/bin/osm2pgsql --create --flat-nodes --slim --username postgres --password --hstore --hstore-match-only --number-processes 6 --cache 50000 --style default.style --input-reader pbf planet-latest.osm.pbf osm2pgsql SVN vers...'''
date = "2015-11-12T15:42:00Z"
lastmod = "2015-11-13T22:33:00Z"
weight = 46544
keywords = [ "import", "osm2pgsql" ]
aliases = [ "/questions/46544" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgsql import getting killed](/questions/46544/osm2pgsql-import-getting-killed)

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
<span id="post-46544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46544-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I try to import planet-latest.osm.pbf I get the following error:</p>
<pre><code>/usr/local/bin/osm2pgsql --create --flat-nodes --slim --username postgres --password --hstore --hstore-match-only --number-processes 6 --cache 50000 --style default.style --input-reader pbf planet-latest.osm.pbf
osm2pgsql SVN version 0.89.0-dev (64 bit id space)
&#10;Using built-in tag processing pipeline  
Using projection SRS 900913 (Spherical Mercator)  
Setting up table: planet_osm_point  
Setting up table: planet_osm_line  
Setting up table: planet_osm_polygon  
Setting up table: planet_osm_roads  
Allocating memory for dense node cache  
Allocating dense node cache in one big chunk  
Allocating memory for sparse node cache  
Sharing dense sparse  
Node-cache: cache=50000MB, maxblocks=800000*65536, allocation method=3  
Mid: Ram, scale=100  
Reading in file: planet-latest.osm.pbf  
Using PBF parser.  
Processing: Node(3095464k 2705.8k/s) Way(53703k 29.11k/s) Relation(0 0.00/s)Killed</code></pre>
<p>Here is the message I get from dmesg:</p>
<pre><code>Out of memory: Kill process 23636 (osm2pgsql) score 953 or sacrifice child  
Killed process 23636 (osm2pgsql) total-vm:75687764kB, anon-rss:60639884kB, file-rss:0kB</code></pre>
<p>do I need more that 50GB RAM to import the planet file?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '15, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '15, 14:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/390c3a1e9ea7b1f10deea61828ad66eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lightsider&#39;s gravatar image" />
<p><span>Lightsider</span><br />
<span class="score" title="1540 reputation points"><span>1.5k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span></p>
</div>
</div>
<div id="comments-container-46544" class="comments-container">
&#10;</div>
<div id="comment-tools-46544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46544-form-container" class="comment-form-container">
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

<span id="46575"></span>

<div id="answer-container-46575" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46575-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="khamooshi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To import the whole planet, you need to use slim mode, but with your command line you are saving the flat nodes in a file called <code>--slim</code>. Add a file name after <code>--flat-nodes</code>.</p>
<p>Also, <code>-C 28000</code> is plenty of cache to store all nodes in RAM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '15, 22:33</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-46575" class="comments-container">
&#10;</div>
<div id="comment-tools-46575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46575-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46545"></span>

<div id="answer-container-46545" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46545-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>--cache 50000</code> means you are assigning 50000 MB (50 GB) of your memory as node cache. This is too high when having "only" 50 GB of RAM. I'm not familiar with osm2pgsql so I can't suggest a good value for this option, but try to assign less than all your available RAM to it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '15, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46545" class="comments-container">
<span id="46546"></span>
<div id="comment-46546" class="comment">
<div id="post-46546-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually I have 60GB RAM, and I assigned 50GB. I also tried with 40GB, same thing happened!</p>
</div>
<div id="comment-46546-info" class="comment-info">
<span class="comment-age">(12 Nov '15, 15:58)</span> <span class="comment-user userinfo">khamooshi</span>
</div>
</div>
<span id="46548"></span>
<div id="comment-46548" class="comment">
<div id="post-46548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... and I think (based on the fact that you've asked other questions about rendering) that other (smaller) imports have worked OK in the past?</p>
</div>
<div id="comment-46548-info" class="comment-info">
<span class="comment-age">(12 Nov '15, 16:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46563"></span>
<div id="comment-46563" class="comment">
<div id="post-46563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I didn't set up the other severs, so I don't know how they did it! btw, I use --flat-nodes and different projection.</p>
</div>
<div id="comment-46563-info" class="comment-info">
<span class="comment-age">(13 Nov '15, 08:42)</span> <span class="comment-user userinfo">khamooshi</span>
</div>
</div>
</div>
<div id="comment-tools-46545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46545-form-container" class="comment-form-container">
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

