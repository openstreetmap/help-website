+++
type = "question"
title = "Hardware Configuration for a Production Tile Server with high usage and serving multiple styles?"
description = '''Hello, I&#x27;m in the process to set up a production tile server that can serve multiple styles. I want to know what dedicated server I have to choose and what should be perfect configuration for it My requirements are:  high usage, maybe max 20-30k users at the same time during spikes whole world cover...'''
date = "2018-07-25T19:24:00Z"
lastmod = "2018-07-26T21:37:00Z"
weight = 64925
keywords = [ "openstreetmap", "hardware", "hardwarerequirements", "tileserver" ]
aliases = [ "/questions/64925" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Hardware Configuration for a Production Tile Server with high usage and serving multiple styles?](/questions/64925/hardware-configuration-for-a-production-tile-server-with-high-usage-and-serving-multiple-styles)

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
<span id="post-64925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm in the process to set up a production tile server that can serve multiple styles. I want to know what dedicated server I have to choose and what should be perfect configuration for it</p>
<p>My requirements are:</p>
<ol>
<li>high usage, maybe max 20-30k users at the same time during spikes</li>
<li>whole world coverage, limiting max zoom to 18 is ok</li>
<li>tiles size is 256*256</li>
<li>updating my db everyday</li>
<li>I'd like to provide at least 3 map styles.</li>
</ol>
<p>I need your advice on-</p>
<ol>
<li>No of vCpu required</li>
<li>RAM Size</li>
<li>Swap Partition Size</li>
<li>Do I need a Raid array for tile cache?(If yes what should be an ideal raid level)</li>
<li>SSD Size and No of SSDs required</li>
<li>HDD Size and No of HDDs required</li>
<li>Boot Drive Size and Do I need a SSD Drive as boot drive</li>
</ol>
<p>Thanks in advance for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-hardware" rel="tag" title="see questions tagged &#39;hardware&#39;">hardware</span> <span class="post-tag tag-link-hardwarerequirements" rel="tag" title="see questions tagged &#39;hardwarerequirements&#39;">hardwarerequirements</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '18, 19:24</strong></p>
<img src="https://secure.gravatar.com/avatar/943a788b771da12a63057582fbf250b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anuranpal&#39;s gravatar image" />
<p><span>anuranpal</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anuranpal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '18, 04:33</strong> </span></p>
</div>
</div>
<div id="comments-container-64925" class="comments-container">
<span id="64941"></span>
<div id="comment-64941" class="comment">
<div id="post-64941-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Duplicate question deleted.</p>
</div>
<div id="comment-64941-info" class="comment-info">
<span class="comment-age">(26 Jul '18, 10:26)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64925-form-container" class="comment-form-container">
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

<span id="64954"></span>

<div id="answer-container-64954" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64954-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="anuranpal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a community help forum. What you seem to be after is not general help, but specific consulting to help you achieve your goals in a specific commercial project. Consider getting commercial advice.</p>
<p>Generally, the server performance has two aspects: How quickly new tiles can be rendered, and how quickly existing tiles can be served from the cache. A tertiary aspect is how quickly you will be able to apply updates.</p>
<p>Rendering speed depends mostly on how fast your database disks are and how well engineered the style is. You cannot work without SSDs, and for a high end server you should consult with your vendor about what setup gives you the lowest latency and fastest random I/O access. A standard server with 64 GB RAM, 4 quad-core CPUs and fast SSDs with the standard OSM Carto style will give you a rendering performance in the general range of 1-5 metatiles per second (64-320 tiles per second). On lower zoom levels this performance will be much worse, and it is not unheard of for certain metatiles on z6 or z7 to take 120 seconds and longer to render, even if fast disks are available.</p>
<p>Tile access speed depends on the speed of the disks that hold your cache. Massive random I/O is not so important here so it is <em>normally</em> ok to use standard disks. Network I/O can become an issue. Your requirements are massive. 30k tiles "at once", let's say within the same 5 second interval, means 6k tiles per second, with an average tile size of 10kb that's 60 MB per second read from disk and a 500 mBit/s link saturated.</p>
<p>You might get to a point here where it could make sense to have one or more caches in front of your tile server, so that the caches, which would be easily scalable, could take the brunt of the high load. But this depends heavily on your usage scenario, and whether people are likely to request the same tiles often.</p>
<p>You will roughly need about 1TB of SSD space for the DB, 300 GB of tile cache per style, 64 GB RAM, 8 CPUs. Boot drive size is really not an issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '18, 21:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64954" class="comments-container">
&#10;</div>
<div id="comment-tools-64954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64954-form-container" class="comment-form-container">
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

