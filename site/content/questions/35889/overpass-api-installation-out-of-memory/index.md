+++
type = "question"
title = "Overpass API installation &#x27;Out of memory&#x27;"
description = '''Hi all,  I&#x27;m trying to install an overpass implementation on a custom server (to free resources on the public server), but im running into an &#x27;out of memory&#x27; error while trying to build the database for a small .bz2 file (for the UK).  As the documentation states, 1GB ram is the minimum for the serv...'''
date = "2014-08-16T12:48:00Z"
lastmod = "2014-09-14T19:43:00Z"
weight = 35889
keywords = [ "overpass", "api", "installation", "error" ]
aliases = [ "/questions/35889" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API installation 'Out of memory'](/questions/35889/overpass-api-installation-out-of-memory)

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
<span id="post-35889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35889-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I'm trying to install an overpass implementation on a custom server (to free resources on the public server), but im running into an 'out of memory' error while trying to build the database for a small .bz2 file (for the UK).</p>
<p>As the documentation states, 1GB ram is the minimum for the server install.</p>
<p>My server has 3072MB RAM, 512MB VSWAP, quad core, 275 GB SSD-Cached.</p>
<p>I have already set up the overpass api on a 4GB RAM server (with lower spec on everything else).</p>
<p>Should my server be able to run this? I also tried to install the API with a 512MB ram server before now, and the install ran for 10mins before terminating but on this new server it terminates almost immediately.</p>
<p>The error itself (from dmesg) is</p>
<p><code>[4551398.870288] Out of memory in UB 25187: OOM killed process 21091 (update_database) score 0 vm:4228424kB, rss:3102376kB, swap:503952kB</code>.</p>
<p>Regards and many thanks,</p>
<p>George</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '14, 12:48</strong></p>
<img src="https://secure.gravatar.com/avatar/001dba1b5051c50ad90d82f873ecea0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister&#39;s gravatar image" />
<p><span>gmeister</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35889" class="comments-container">
<span id="36770"></span>
<div id="comment-36770" class="comment">
<div id="post-36770-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Did you try to bump up your swap space to say 8-16GB?</p>
</div>
<div id="comment-36770-info" class="comment-info">
<span class="comment-age">(11 Sep '14, 19:08)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="36818"></span>
<div id="comment-36818" class="comment">
<div id="post-36818-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hey, Thanks for the reply, I managed to avoid the out of memory error by adding <code>--flush-size=1</code> as a parameter when calling update_database, so in my case, adding it to the last line in the <code>init_osm3s.sh</code> script. Ill add this to the wiki.</p>
</div>
<div id="comment-36818-info" class="comment-info">
<span class="comment-age">(14 Sep '14, 19:43)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
</div>
<div id="comment-tools-35889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35889-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

