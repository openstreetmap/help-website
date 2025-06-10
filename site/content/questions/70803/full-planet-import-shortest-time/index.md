+++
type = "question"
title = "Full Planet Import Shortest Time"
description = '''Considering I can spin up any EC2 Instance (even the strongest ones) and tweaking the configuration for maximum import speed, What&#x27;s the shortest time for a full planet import using osm2pgsql tool? is there a bash script that fires osm2pgsql with dynamic values based on the current machine that is r...'''
date = "2019-09-16T14:14:00Z"
lastmod = "2019-09-16T16:45:00Z"
weight = 70803
keywords = [ "planet", "import" ]
aliases = [ "/questions/70803" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Full Planet Import Shortest Time](/questions/70803/full-planet-import-shortest-time)

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
<span id="post-70803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70803-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Considering I can spin up any EC2 Instance (even the strongest ones) and tweaking the configuration for maximum import speed, What's the shortest time for a full planet import using <code>osm2pgsql</code> tool?</p>
<p>is there a bash script that fires <code>osm2pgsql</code> with dynamic values based on the current machine that is running it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '19, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/47110f56c594a7515b757d9975b9a8c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LiorM&#39;s gravatar image" />
<p><span>LiorM</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LiorM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70803" class="comments-container">
&#10;</div>
<div id="comment-tools-70803" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70803-form-container" class="comment-form-container">
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

<span id="70804"></span>

<div id="answer-container-70804" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70804-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On a 64 GB RAM machine with fast NVMe disks you will typically achieve a full planet import (with slim mode and flatnodes) in about 14 hours. This is for old-fashioned "real" hardware. In the cloud, if RAM is not an issue at all and if you do not need updates, then the fastest imports are probably those run without <code>--slim</code>. My guess (based on smaller extracts) is that this could cut import times down to about 6 hours, but you'll need something like 512 GB of RAM (and still need fast disks). Using <code>--slim --drop</code> on a lesser-RAM machine will also be faster than 14 hours at the expense of updatability. If you have tons of RAM and need updates, then importing to a RAM disk database might be worth a try.</p>
<p>I am not aware of a script that auto-adapts values.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '19, 14:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70804" class="comments-container">
<span id="70805"></span>
<div id="comment-70805" class="comment">
<div id="post-70805-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you share the <code>osm2pgsql</code> config so it will run in ~6 hours? Plus - whats the CPU / RAM prerequisites to achieve that?</p>
<p>No need for updates.</p>
</div>
<div id="comment-70805-info" class="comment-info">
<span class="comment-age">(16 Sep '19, 14:49)</span> <span class="comment-user userinfo">LiorM</span>
</div>
</div>
<span id="70806"></span>
<div id="comment-70806" class="comment">
<div id="post-70806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I said, the 6 hours is a guess of mine; because of the high memory requirements I haven't run osm2pgsql on a planet file without --slim recently. I think if you have 512 GB of RAM and 4-8 cores you should be fine. The exact command line arguments depend on which map style you'll be using etc. but it would likely be something like:</p>
<p>osm2pgsql -d gis --hstore planet-latest.osm.pbf</p>
<p>some styles will expect you to use a special style file, a LUA transforms file, and perhaps recommend the <code>-G</code> option for building proper multipolygons, all of which have the potential of slowing things down a little. If you need LUA transforms, then building osm2gpsql with "luajit" can recover some of the time used for LUA processing. I'm not 100% sure about the <code>--cache</code> parameter, it used to be irrelevant for non-slim mode but you'll have to see. Do report back your results!</p>
</div>
<div id="comment-70806-info" class="comment-info">
<span class="comment-age">(16 Sep '19, 16:45)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70804" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70804-form-container" class="comment-form-container">
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

