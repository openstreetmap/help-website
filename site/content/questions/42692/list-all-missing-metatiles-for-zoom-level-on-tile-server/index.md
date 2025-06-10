+++
type = "question"
title = "List all missing metatiles for zoom level on tile server"
description = '''I have a tile server based on tirex, postgres and mapnik. All metatiles are in /var/lib/tirex/tiles/. How can I get statistics on how many of the metatiles for a certain zoomlevel have been (pre)rendered, and how many are missing?  I use tirex-batch to prerender most tiles and want to make sure I do...'''
date = "2015-04-29T14:12:00Z"
lastmod = "2015-04-29T14:55:00Z"
weight = 42692
keywords = [ "tirex", "mod_tile", "mapnik", "tileserver" ]
aliases = [ "/questions/42692" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [List all missing metatiles for zoom level on tile server](/questions/42692/list-all-missing-metatiles-for-zoom-level-on-tile-server)

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
<span id="post-42692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42692-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a tile server based on tirex, postgres and mapnik. All metatiles are in /var/lib/tirex/tiles/. How can I get statistics on how many of the metatiles for a certain zoomlevel have been (pre)rendered, and how many are missing?</p>
<p>I use tirex-batch to prerender most tiles and want to make sure I do not miss any tiles accidentically.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '15, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/42c22f7724a32aa2d2e19609d8e7f1b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jnachtigall&#39;s gravatar image" />
<p><span>jnachtigall</span><br />
<span class="score" title="101 reputation points">101</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jnachtigall has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42692" class="comments-container">
&#10;</div>
<div id="comment-tools-42692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42692-form-container" class="comment-form-container">
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

<span id="42693"></span>

<div id="answer-container-42693" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42693-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jnachtigall has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If your use case is "find missing tiles, and pre-render them", then you can do</p>
<pre><code>tirex-batch -f not-exists map=mymap bbox=-180,-90,180,90 z=0-12</code></pre>
<p>or something like it; the <code>-f not-exists</code> only adds those tiles to the queue that don't already exist.</p>
<p>If you just want to know how many are missing, you can do a</p>
<pre><code>for i in `seq 3 12`
do
   echo -n $i:
   find /my/tile/dir/$i -type f -name \*meta |wc -l 
done</code></pre>
<p>You'd expect to see 4**(z-3) meta tiles on each zoom level fully rendered.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '15, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42693" class="comments-container">
&#10;</div>
<div id="comment-tools-42693" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42693-form-container" class="comment-form-container">
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

