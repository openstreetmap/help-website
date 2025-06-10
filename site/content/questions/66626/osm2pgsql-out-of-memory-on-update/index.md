+++
type = "question"
title = "osm2pgsql out of memory on update"
description = '''Hi, I&#x27;ve successfully imported the whole planet and the rendering works (slowly, but that&#x27;s another problem). I&#x27;ve tried to update using the openstreetmap-tile-update-expire script, but it keep using all the RAM available and been killed, despite the fact that I&#x27;m using flag-nodes and that I tried t...'''
date = "2018-11-02T09:33:00Z"
lastmod = "2018-11-02T09:33:00Z"
weight = 66626
keywords = [ "update", "ram", "osm2pgsql", "memory" ]
aliases = [ "/questions/66626" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql out of memory on update](/questions/66626/osm2pgsql-out-of-memory-on-update)

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
<span id="post-66626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66626-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I've successfully imported the whole planet and the rendering works (slowly, but that's another problem). I've tried to update using the openstreetmap-tile-update-expire script, but it keep using all the RAM available and been killed, despite the fact that I'm using flag-nodes and that I tried to limitate the RAM usage with the -C option. I have 32Gb of RAM + the same in SWAP, so it doesn't make any sense to me. I've tried the -C option with only 8gb and the same append, it seems this option is not working as I expected.</p>
<p>The exact command used:</p>
<pre><code>osm2pgsql -a --slim -G --hstore --hstore-match-only -S /path/to/my/script --flat-nodes /path/to/flat_nodes.bin -e13-20  -d gis -C 8000 -o &quot;$EXPIRY_FILE.$$&quot; $CHANGE_FILE</code></pre>
<p>I've watched it working while monitoring the RAM usage, it's working fine at the beginning but as it progress, it's using more and more RAM, probably a memory leak somewhere but I can't find where and why... The RAM usage inscrease until it reaches the maximum, then after "Left to process: 6221" the process was killed.</p>
<p>Does someone have any idea of what's appening?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-ram" rel="tag" title="see questions tagged &#39;ram&#39;">ram</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '18, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/32a7da9bf999cc0ea4f6befea00edd8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voharunado&#39;s gravatar image" />
<p><span>voharunado</span><br />
<span class="score" title="66 reputation points">66</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voharunado has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66626" class="comments-container">
&#10;</div>
<div id="comment-tools-66626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66626-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

