+++
type = "question"
title = "tile server image generation speed"
description = '''i set up a map server on ubuntu 18.4 the vm have 8 core cpu and also 16 gig of ram i just imported great Britain pbf data but the map generation speed is very low some time it need 10-15 seconds for generate tiles and also some time it dont create any thing due to timeouterror this is a part of pgsq...'''
date = "2020-07-12T17:08:00Z"
lastmod = "2020-07-12T17:08:00Z"
weight = 75676
keywords = [ "generate_tiles", "tiles", "tileserver" ]
aliases = [ "/questions/75676" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tile server image generation speed](/questions/75676/tile-server-image-generation-speed)

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
<span id="post-75676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75676-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i set up a map server on ubuntu 18.4 the vm have 8 core cpu and also 16 gig of ram i just imported great Britain pbf data</p>
<p>but the map generation speed is very low</p>
<p>some time it need 10-15 seconds for generate tiles and also some time it dont create any thing due to timeouterror this is a part of pgsql configs</p>
<pre><code>lbmap@tracker-map:~$ grep ^VmPeak /proc/16364/status
VmPeak:  4492940 kB
lbmap@tracker-map:~$ cat /proc/meminfo | grep -i huge
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
HugePages_Total:    7570
HugePages_Free:     5465
HugePages_Rsvd:        4
HugePages_Surp:        0
Hugepagesize:       2048 kB</code></pre>
<p>how can i get a better performance?!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '20, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0cc5add59daed413ca657703467678ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peiman2&#39;s gravatar image" />
<p><span>peiman2</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peiman2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75676" class="comments-container">
&#10;</div>
<div id="comment-tools-75676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75676-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

