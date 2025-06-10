+++
type = "question"
title = "How long should minutely and hourly diff take with 8GB memory?"
description = '''How long does it take for you in a moderate server with 8GB RAM? We have experience that update takes significantly longer than actual time period, so which creates ever-growing time lag. '''
date = "2010-09-20T10:27:00Z"
lastmod = "2010-09-20T12:50:00Z"
weight = 862
keywords = [ "diff", "osm2pgsql", "osmosis", "server" ]
aliases = [ "/questions/862" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How long should minutely and hourly diff take with 8GB memory?](/questions/862/how-long-should-minutely-and-hourly-diff-take-with-8gb-memory)

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
<span id="post-862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-862-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How long does it take for you in a moderate server with 8GB RAM? We have experience that update takes significantly longer than actual time period, so which creates ever-growing time lag.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '10, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ff53f6579540c3da3a1ad5180515cc67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JaakL&#39;s gravatar image" />
<p><span>JaakL</span><br />
<span class="score" title="42 reputation points">42</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JaakL has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '10, 13:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-862" class="comments-container">
&#10;</div>
<div id="comment-tools-862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-862-form-container" class="comment-form-container">
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

<span id="863"></span>

<div id="answer-container-863" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-863-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The wiki page for <a href="http://wiki.openstreetmap.org/wiki/SotM_2010_session:Tuning_the_Mapnik_Rendering_Chain">my SotM performance talk</a> has an SVG image for a 8 GB RAM machine showing that you should be able to process a daily diff in under 10 hours. This is an osm2pgsql import however; in case you are talking about an APIDB import using Osmosis, that is likely to take longer. For osm2pgsql, we have seen that using PostgreSQL 8.4 was much slower than 8.3, so make sure you're not running 8.4. Of course, the usual database tuning tips apply (are your imports perhaps interrupted by an auto-vacuum process? can you afford the risk of having fsync=off? have you increased your shared_buffers from the default?). Sometimes, running an "analyze" command on the database also helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '10, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-863" class="comments-container">
<span id="865"></span>
<div id="comment-865" class="comment">
<div id="post-865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! I have actually seen the slides and your presentation, my question was specifically about minutely and hourly diffs. We had hourly diff import test run of 25 hours or so. We use SAS drives in RAID-0, which should give good raw IO speed, and have applied the basic DB optimizations (no vacuum, increased shared_buffers).</p>
</div>
<div id="comment-865-info" class="comment-info">
<span class="comment-age">(20 Sep '10, 12:50)</span> <span class="comment-user userinfo">JaakL</span>
</div>
</div>
</div>
<div id="comment-tools-863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-863-form-container" class="comment-form-container">
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

