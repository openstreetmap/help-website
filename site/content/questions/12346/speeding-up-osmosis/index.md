+++
type = "question"
title = "Speeding up Osmosis"
description = '''I have a 8G RAM and trying to split the Planet OSM files to multiple continents, countries and regions. It took more than 1 day to split the Planet OSM to continent based OSM files. To split the continent OSM bz2 files further to smaller countries is taking more time. For example, the split of Asia ...'''
date = "2012-04-25T08:41:00Z"
lastmod = "2012-04-25T08:48:00Z"
weight = 12346
keywords = [ "increase", "performance", "slow", "split", "osmosis" ]
aliases = [ "/questions/12346" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Speeding up Osmosis](/questions/12346/speeding-up-osmosis)

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
<span id="post-12346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12346-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a 8G RAM and trying to split the Planet OSM files to multiple continents, countries and regions. It took more than 1 day to split the Planet OSM to continent based OSM files. To split the continent OSM bz2 files further to smaller countries is taking more time. For example, the split of Asia osm bz2 file has been running since 2 days. The max heap value set to JVM is 5G. Any suggestions to speed up Osmosis?</p>
<p>Thanks</p>
<p>Kris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-increase" rel="tag" title="see questions tagged &#39;increase&#39;">increase</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '12, 08:41</strong></p>
<img src="https://secure.gravatar.com/avatar/382f63907e37a769341f345c01d8e8df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kris&#39;s gravatar image" />
<p><span>kris</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kris has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12346" class="comments-container">
&#10;</div>
<div id="comment-tools-12346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12346-form-container" class="comment-form-container">
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

<span id="12347"></span>

<div id="answer-container-12347" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12347-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Never use bz2 with osmosis, it's a performance killer. Use pbf files if you can, and for your intermediate products (i.e. if the only reason you're making asia.osm.pbf is that you want to further split it in a second step) add the <code>compress=none</code> flag to <code>--write-pbf</code> (don't worry, the resulting file will only be twice the size, not ten times).</p>
<p>If you cannot use pbf files, at least use gz instead of bz2; if you really really have to use bz2, use an external program (<code>bzcat planet.osm.bz2 | osmosis --read-xml -</code>).</p>
<p>Generously use <code>--buffer bufferCapacity=12000</code>, and if you have two disks in your system, try to read from one while writing to the other.</p>
<p>The fastest way to split a planet file into components is to use Peter Koerner's <a href="https://github.com/MaZderMind/osm-history-splitter">OSM history splitter</a> instead of Osmosis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '12, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12347" class="comments-container">
&#10;</div>
<div id="comment-tools-12347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12347-form-container" class="comment-form-container">
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

