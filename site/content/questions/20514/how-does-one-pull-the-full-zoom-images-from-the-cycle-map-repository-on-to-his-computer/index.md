+++
type = "question"
title = "How does one pull the full zoom images from the Cycle Map Repository on to his computer?"
description = '''My goal is to pull every single tile (by tile, I mean the rendered square images that are loaded as you scroll through the map) of the fully zoomed cycle map, and save them as a separate file onto my computer. I plan to use the height maps provided as a means to generate my own &quot;Tactical&quot; map for an...'''
date = "2013-03-06T02:24:00Z"
lastmod = "2013-03-06T17:13:00Z"
weight = 20514
keywords = [ "python", "height", "tiles", "api", "cycle" ]
aliases = [ "/questions/20514" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does one pull the full zoom images from the Cycle Map Repository on to his computer?](/questions/20514/how-does-one-pull-the-full-zoom-images-from-the-cycle-map-repository-on-to-his-computer)

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
<span id="post-20514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20514-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My goal is to pull every single tile (by tile, I mean the rendered square images that are loaded as you scroll through the map) of the fully zoomed cycle map, and save them as a separate file onto my computer. I plan to use the height maps provided as a means to generate my own "Tactical" map for an opensource online game that I am developing. My basic plan is to do a basic</p>
<pre><code>if color of top left pixel == &quot;e7da81&quot;:
   set height to 86
elif color of top left pixel == &quot;e7da82&quot;:
   set height to 87</code></pre>
<p>(Ugly code? Yes, but it doesnt need to be quick; just functional.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-height" rel="tag" title="see questions tagged &#39;height&#39;">height</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-cycle" rel="tag" title="see questions tagged &#39;cycle&#39;">cycle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '13, 02:24</strong></p>
<img src="https://secure.gravatar.com/avatar/006f679d771a6c053258c1b53a165e10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akiva&#39;s gravatar image" />
<p><span>Akiva</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akiva has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '13, 03:01</strong> </span></p>
</div>
</div>
<div id="comments-container-20514" class="comments-container">
&#10;</div>
<div id="comment-tools-20514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20514-form-container" class="comment-form-container">
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

<span id="20520"></span>

<div id="answer-container-20520" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20520-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-20520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, <strong>DON'T EVEN TRY TO DO THIS</strong>. Read the <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">Tile Usage Policy</a>.</p>
<p>Tile scraping imposes a very high load on servers and will result in your IP address being blocked. CycleMap is owned and run by a private individual who may have to meet server costs from his own income.</p>
<p>Second, if you want a large volume of tiles, you must generate your own, or pay someone for them.</p>
<p>If, as it appears from my reading of your question, you merely want tiles with contour lines, then it is fairly simple to generate your own (although for the whole world this will take a long time &amp; lots of disk space). <a href="http://wiki.openstreetmap.org/wiki/Srtm">SRTM</a> data can be downloaded and there are many tools for manipulating it.</p>
<p>Note that most tiled maps do not render more than a very small fraction of the most detailed tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '13, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-20520" class="comments-container">
<span id="20536"></span>
<div id="comment-20536" class="comment">
<div id="post-20536-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That was very helpful. Two follow up questions; How large do you suppose the repository of tiles would be? How much do you suppose is reasonable to pay the for a mass download?</p>
</div>
<div id="comment-20536-info" class="comment-info">
<span class="comment-age">(06 Mar '13, 16:49)</span> <span class="comment-user userinfo">Akiva</span>
</div>
</div>
<span id="20538"></span>
<div id="comment-20538" class="comment">
<div id="post-20538-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>A quick look at this table will tell you how many tiles make up the world at each level: <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Zoom_levels.">http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Zoom_levels.</a> With 68 700 million tiles at level 18 in a naive implementation you need that many file handles in your system and anywhere from a few hundred bytes / tile. I think you want to think about alternatives.</p>
</div>
<div id="comment-20538-info" class="comment-info">
<span class="comment-age">(06 Mar '13, 17:13)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20520-form-container" class="comment-form-container">
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

