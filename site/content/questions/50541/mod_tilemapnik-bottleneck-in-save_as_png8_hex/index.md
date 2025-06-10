+++
type = "question"
title = "mod_tile/mapnik bottleneck in save_as_png8_hex?"
description = '''I am setting up a tile server using the latest mod_tile build, so Mapnik 3.0.12. I noticed after doing all optimizations that some tiles were still serving particularly slowly so I:  Turned all layers off in the XML so it is only rendering the map background Changed the tile directory to a RAM-mount...'''
date = "2016-06-30T19:46:00Z"
lastmod = "2016-07-02T16:25:00Z"
weight = 50541
keywords = [ "development", "performance", "mod_tile", "mapnik", "tileserver" ]
aliases = [ "/questions/50541" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [mod_tile/mapnik bottleneck in save_as_png8_hex?](/questions/50541/mod_tilemapnik-bottleneck-in-save_as_png8_hex)

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
<span id="post-50541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50541-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am setting up a tile server using the latest mod_tile build, so Mapnik 3.0.12. I noticed after doing all optimizations that some tiles were still serving particularly slowly so I:</p>
<ul>
<li>Turned all layers off in the XML so it is only rendering the map background</li>
<li>Changed the tile directory to a RAM-mounted filesystem</li>
<li>Ran perf for 60 seconds and dragged around a slippy map a whole load to render lots of background-only tiles (not science, I know)</li>
</ul>
<p>The result is a lot of tile requests with TTFB latencies ranging from 2ms to 600ms and a perf log that looks like this:</p>
<p><img src="http://help.openstreetmap.org/upfiles/write-png-perf.png" alt="perf log" /></p>
<p>A background tile looks like this, no interaction required:</p>
<p><img src="http://help.openstreetmap.org/upfiles/oceantile.png" alt="ocean tile" /></p>
<p>The server has loads of head room (2x Intel Xeon 5500s and 32GB of RAM). Any ideas?</p>
<p><strong>Edit:</strong> The tiles with long waits are the ones which cause a new metatile to be rendered. If I watch the requests come through on the server all meta tiles are taking about the same time to render:</p>
<pre><code>renderd[3150]: DEBUG: DONE TILE default 19 2848-2855 424-431 in 0.551 seconds
renderd[3150]: DEBUG: DONE TILE default 19 2848-2855 416-423 in 0.523 seconds
renderd[3174]: DEBUG: DONE TILE default 19 2856-2863 416-423 in 0.557 seconds
renderd[3174]: DEBUG: DONE TILE default 19 2856-2863 416-423 in 0.550 seconds
renderd[3174]: DEBUG: DONE TILE default 19 2864-2871 416-423 in 0.551 seconds
renderd[3174]: DEBUG: DONE TILE default 19 2864-2871 416-423 in 0.561 seconds
renderd[3174]: DEBUG: DONE TILE default 19 2864-2871 416-423 in 0.561 seconds</code></pre>
<p>Is this a regular time for a 2048 x 2048px metatile? If I replace the background image with a colour it drops to about 450ms.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '16, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0c3c9aeb9895679ea13a8776fcbd362f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeterDevoy&#39;s gravatar image" />
<p><span>PeterDevoy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeterDevoy has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '16, 16:26</strong> </span></p>
</div>
</div>
<div id="comments-container-50541" class="comments-container">
<span id="50549"></span>
<div id="comment-50549" class="comment">
<div id="post-50549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe more relevant to create an issue in mod_tile or mapnik github? Or the tile-serving@ mailing list.</p>
</div>
<div id="comment-50549-info" class="comment-info">
<span class="comment-age">(01 Jul '16, 21:33)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
<span id="50559"></span>
<div id="comment-50559" class="comment">
<div id="post-50559-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Devs are a bit slow responding to issues on the repos, I will try the mailing list, thanks.</p>
</div>
<div id="comment-50559-info" class="comment-info">
<span class="comment-age">(02 Jul '16, 12:42)</span> <span class="comment-user userinfo">PeterDevoy</span>
</div>
</div>
<span id="50563"></span>
<div id="comment-50563" class="comment">
<div id="post-50563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>btw: the screenshot above shows save_as_png8_<strong>hex</strong> with 41%.</p>
<p>Follow up post is here: <a href="https://lists.openstreetmap.org/pipermail/tile-serving/2016-July/003961.html">https://lists.openstreetmap.org/pipermail/tile-serving/2016-July/003961.html</a></p>
</div>
<div id="comment-50563-info" class="comment-info">
<span class="comment-age">(02 Jul '16, 15:45)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="50566"></span>
<div id="comment-50566" class="comment">
<div id="post-50566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, well spotted, I have updated the title.</p>
</div>
<div id="comment-50566-info" class="comment-info">
<span class="comment-age">(02 Jul '16, 16:25)</span> <span class="comment-user userinfo">PeterDevoy</span>
</div>
</div>
</div>
<div id="comment-tools-50541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50541-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

