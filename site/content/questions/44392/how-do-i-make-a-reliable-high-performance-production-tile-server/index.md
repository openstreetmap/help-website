+++
type = "question"
title = "How do I make a reliable, high performance production tile server?"
description = '''I have my own OSM tile server that I set up following the instructions (with local changes) on switch2osm here: https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/ It&#x27;s hosted on &quot;the cloud&quot;, including using an iSCSI drive for the data. Recently, a network error caused the di...'''
date = "2015-07-23T16:13:00Z"
lastmod = "2015-07-26T05:32:00Z"
weight = 44392
keywords = [ "caching", "performance", "tileserver", "rendering" ]
aliases = [ "/questions/44392" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I make a reliable, high performance production tile server?](/questions/44392/how-do-i-make-a-reliable-high-performance-production-tile-server)

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
<span id="post-44392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44392-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have my own OSM tile server that I set up following the instructions (with local changes) on switch2osm here: <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></p>
<p>It's hosted on "the cloud", including using an iSCSI drive for the data. Recently, a network error caused the disk to crash. Luckily, we could save it, but the server was down for a day. Now I am looking to improve the situation to provide better service in 2 respects:</p>
<ol>
<li>Reduced risk of long downtime</li>
<li>Better performance</li>
</ol>
<p>As you can imagine, the performance for creating tiles is not great. Sometimes it takes HOURS. We also want to start using the tile server in production and cannot reasonably allow days of downtime.</p>
<p>Are there any reference setups, best practices, etc.? Anyone want to share their hardware configuration?</p>
<p>We have thought of a few options:</p>
<ol>
<li>Upgrading the server to use local SSD storage. Provide backup/restore mechanism that would have downtime of a few hours in case of hard disk or server crash.</li>
<li>Similar to above but with 2 load balanced servers. This would be twice as expensive but would reduce downtime significantly</li>
<li>Provide RAID on the local hard disks. I'm not sure this pays for itself. Am I wrong?</li>
<li>Keep a low performance, low reliability tile server, but put a cache server (or several) in front of it. Precompute all of the tiles. Should the tile server die, the cache server would continue serving tiles until the tile server could be rebuilt (which takes weeks).</li>
</ol>
<p>Any and all opinions, recommendations, and details would be welcome!</p>
<p>Thanks, Harold Ship</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-caching" rel="tag" title="see questions tagged &#39;caching&#39;">caching</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '15, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/7111e460b42d95ecc8f802215e342cd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haroldship1&#39;s gravatar image" />
<p><span>haroldship1</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haroldship1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '15, 16:16</strong> </span></p>
</div>
</div>
<div id="comments-container-44392" class="comments-container">
&#10;</div>
<div id="comment-tools-44392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44392-form-container" class="comment-form-container">
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

<span id="44395"></span>

<div id="answer-container-44395" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44395-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Local SSD is a must. You haven't said if you're running a world-wide server or just a regional one. Precomputing <em>all</em> tiles world-wide is not feasible. You'd usually pre-compute z0-12 or 0-13 and then render the rest on-demand. Having multiple identical servers helps against server failure, but you might also get away with having a "clone" of the main server that keeps only the rendering database and not the update tables, so if the main server fails the clone can at least produce tiles, just not update them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '15, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-44395" class="comments-container">
<span id="44405"></span>
<div id="comment-44405" class="comment">
<div id="post-44405-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And iSCSI is just a terrible idea for both performance and reliability. Do not use iSCSI unless you can be very lax on both those criterias, or unless you're using software that is specifically tailored for this kind of hardware (Postgresql isn't).</p>
<p>I ignored that warning once and we paid that with cripling downtimes and limiting performance. We'll be glad when those servers get decomissioned this year.</p>
</div>
<div id="comment-44405-info" class="comment-info">
<span class="comment-age">(24 Jul '15, 10:50)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="44431"></span>
<div id="comment-44431" class="comment">
<div id="post-44431-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok I will push for the SSD. When you say it's a must, do you mean for the DB or also for the tiles cache?</p>
</div>
<div id="comment-44431-info" class="comment-info">
<span class="comment-age">(26 Jul '15, 05:28)</span> <span class="comment-user userinfo">haroldship1</span>
</div>
</div>
<span id="44432"></span>
<div id="comment-44432" class="comment">
<div id="post-44432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, we are trying to run the whole world, so precomputing up to say level 13 might be what we'll do. I guess if/once we have SSD we can re-evaluate the performance.</p>
</div>
<div id="comment-44432-info" class="comment-info">
<span class="comment-age">(26 Jul '15, 05:29)</span> <span class="comment-user userinfo">haroldship1</span>
</div>
</div>
<span id="44433"></span>
<div id="comment-44433" class="comment">
<div id="post-44433-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, what happened for us was a network switch died and corrupted our iSCSI volume. So I guess I am also learning the hard way. Luckily fsck recovered it.</p>
</div>
<div id="comment-44433-info" class="comment-info">
<span class="comment-age">(26 Jul '15, 05:31)</span> <span class="comment-user userinfo">haroldship1</span>
</div>
</div>
</div>
<div id="comment-tools-44395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44395-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44393"></span>

<div id="answer-container-44393" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44393-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, this doesn't seem to be an FAQ about OSM, but a need for server experts.</p>
<p>Have a look at <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">Commercial_OSM_Software_and_Services</a> for instant advices.</p>
<p>After own internet seraching I only found:</p>
<p><a href="http://www.geofabrik.de/media/2012-09-08-osm2pgsql-performance.pdf">http://www.geofabrik.de/media/2012-09-08-osm2pgsql-performance.pdf</a></p>
<p>Some server hardware stuff is mentioned there.</p>
<p>Asking the guys from geofabrik directly about your aim cannot be bad.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '15, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-44393" class="comments-container">
<span id="44434"></span>
<div id="comment-44434" class="comment">
<div id="post-44434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you I'll use this to negotiate with the IT department.</p>
</div>
<div id="comment-44434-info" class="comment-info">
<span class="comment-age">(26 Jul '15, 05:32)</span> <span class="comment-user userinfo">haroldship1</span>
</div>
</div>
</div>
<div id="comment-tools-44393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44393-form-container" class="comment-form-container">
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

