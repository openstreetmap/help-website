+++
type = "question"
title = "Real Newbie. How to extract a boundary box from big map using windows?"
description = '''Hi to everybody! I am trying to extract a portion of Europe map (say Belgium, France, Germany, The Netherlands and UK) from the europe-latest.osm.pbf using Windows commands prompt. I succed to install the osmosis &quot;package&quot; in my machine (well, it is not enough powerful to manage the entire Europe ma...'''
date = "2022-02-15T19:14:00Z"
lastmod = "2022-02-16T10:29:00Z"
weight = 83490
keywords = [ "windows", "extract", "bbox" ]
aliases = [ "/questions/83490" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Real Newbie. How to extract a boundary box from big map using windows?](/questions/83490/real-newbie-how-to-extract-a-boundary-box-from-big-map-using-windows)

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
<span id="post-83490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83490-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to everybody! I am trying to extract a portion of Europe map (say Belgium, France, Germany, The Netherlands and UK) from the europe-latest.osm.pbf using Windows commands prompt. I succed to install the osmosis "package" in my machine (well, it is not enough powerful to manage the entire Europe map), but I can't arrive to write down the right code to perform a boundary box extrection. I'm sure that is a trivial (not to much) issue of path in order to make working Osmium commands with the target file, but really I don't know how to begin the command. All the command hints and suggestions seem to start from a basic starting point/platform that I don't know/can't find. Could someone, please, give me some hints or at least show me any link that can allow me to understand how to proceed? Thanks a lot to any one that could help me. D.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '22, 19:14</strong></p>
<img src="https://secure.gravatar.com/avatar/344bdbdcd1a959d1bb0ac9f8b58828a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shardana&#39;s gravatar image" />
<p><span>Shardana</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shardana has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83490" class="comments-container">
&#10;</div>
<div id="comment-tools-83490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83490-form-container" class="comment-form-container">
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

<span id="83491"></span>

<div id="answer-container-83491" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83491-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Shardana has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The correct way for a bbox extraction with osmosis would require the command line parameters (I am putting one per line but you need them all on the same line):</p>
<pre><code>--read-pbf europe-latest.osm.obf
--bb left=-15 bottom=41 right=16 top=62
--write-pbf myfile.osm.pbf</code></pre>
<p>The <code>--bb</code> has a couple of options which you should read up on; they will affect memory consumption as well as the question of referential integrity in your output file. The way I have written it above it will run fastest, but if a way has some nodes inside and some nodes outside your box, only the inside nodes will be copied and the way will be left with "dangling" references. Same for relations.</p>
<p>Also, try to get a copy of the "osmium" command line utility - it's made for Linux but should be available in Windows builds as well - since that will do the job a little more efficiently than osmosis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '22, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-83491" class="comments-container">
<span id="83492"></span>
<div id="comment-83492" class="comment">
<div id="post-83492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Frederik! Thanks a lot for your help, it works, but it seems my machine can't manage the task. I got this message, I think is not related to the file size, but to something else I can not manage at this time, I tried the same command with a smaller map (belgium) and getting the same output:</p>
<p><strong><em>*** La RICORSIONE BATCH supera i limiti dello STACK</em></strong> <strong><em>Conteggio ricorsione=315, utilizzo stack=90 percento</em></strong> <strong><em>ELABORAZIONE BATCH INTERROTTA</em></strong> ***</p>
<p>I'm sorry it is in Italian, I tried to find some explication but as I think you well know, as much you dig deeper as much it become harder. So, maybe, it's better to look for any alternative solutions. This afternoon I'll try to work a little on Osmium as you suggested, but if this is the starting point I really feel without any abilities by now. Thanks a new time. D.</p>
</div>
<div id="comment-83492-info" class="comment-info">
<span class="comment-age">(16 Feb '22, 10:22)</span> <span class="comment-user userinfo">Shardana</span>
</div>
</div>
<span id="83493"></span>
<div id="comment-83493" class="comment">
<div id="post-83493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It might be a case of having to set the right Java options allowing it to consume more memory, with the environment variable <code>JAVACMD_OPTIONS</code>. For osmium, you'd be looking at <a href="https://docs.osmcode.org/osmium/latest/osmium-extract.html">https://docs.osmcode.org/osmium/latest/osmium-extract.html</a></p>
</div>
<div id="comment-83493-info" class="comment-info">
<span class="comment-age">(16 Feb '22, 10:29)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-83491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83491-form-container" class="comment-form-container">
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

