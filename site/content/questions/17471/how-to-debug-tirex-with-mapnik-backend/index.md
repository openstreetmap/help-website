+++
type = "question"
title = "How to debug tirex with mapnik backend"
description = '''I have installed tirex and the mapnik backend. The test tiles from tirex are working fine, but if I use a real mapnik map, and access the tile server I am getting a 404 error after some seconds. How can I debug this issue? I am getting only a fee lines of log output: ==&amp;gt; /var/log/syslog &amp;lt;==  =...'''
date = "2012-11-04T19:55:00Z"
lastmod = "2012-11-04T20:05:00Z"
weight = 17471
keywords = [ "tirex", "mapnik" ]
aliases = [ "/questions/17471" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to debug tirex with mapnik backend](/questions/17471/how-to-debug-tirex-with-mapnik-backend)

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
<span id="post-17471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17471-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed tirex and the mapnik backend.</p>
<p>The test tiles from tirex are working fine, but if I use a real mapnik map, and access the tile server I am getting a 404 error after some seconds.</p>
<p>How can I debug this issue?</p>
<p>I am getting only a fee lines of log output:</p>
<pre><code>==&gt; /var/log/syslog &lt;==
&#10;==&gt; /var/log/tirex/jobs.log &lt;==
&#10;==&gt; /var/log/apache2/error.log &lt;==
&#10;==&gt; /var/log/apache2/other_vhosts_access.log &lt;==
&#10;==&gt; /var/log/apache2/error.log &lt;==
[Sun Nov 04 19:54:23 2012] [info] [client 10.0.2.2] tile_storage_hook: handler(tile_serve), uri(/osm/1/1/1.png), filename(/var/lib/mod_tile/example/1/0/0/0/0/0.meta), path_info((null))
[Sun Nov 04 19:54:23 2012] [info] [client 10.0.2.2] Requesting style(example) z(1) x(1) y(1) from renderer with priority 5
&#10;==&gt; /var/log/apache2/other_vhosts_access.log &lt;==
tile.mytileserver.org:80 10.0.2.2 - - [04/Nov/2012:19:54:23 +0000] &quot;GET /osm/1/1/1.png HTTP/1.1&quot; 404 502 &quot;-&quot; &quot;Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0&quot;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '12, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17471" class="comments-container">
&#10;</div>
<div id="comment-tools-17471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17471-form-container" class="comment-form-container">
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

<span id="17472"></span>

<div id="answer-container-17472" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17472-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>in /etc/tirex/mapnik.conf set</p>
<pre><code>#  syslog facility
syslog_facility=daemon
&#10;#  activate this to see debug messages from renderer
debug=1</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '12, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17472" class="comments-container">
&#10;</div>
<div id="comment-tools-17472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17472-form-container" class="comment-form-container">
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

