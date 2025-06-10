+++
type = "question"
title = "Cannot Create Socket"
description = '''Hi, I&#x27;ve been trying to install OSM on a CentOS 6.5 VM.  I believe all of the pieces work correctly but when I try to have a tile rendered from the browser, the tile is not created. The httpd error log says: [Sat Apr 11 00:42:52 2015] [warn] [client ::1] socket connect failed for: /var/run/renderd/r...'''
date = "2015-04-11T22:25:00Z"
lastmod = "2015-04-12T16:13:00Z"
weight = 42275
keywords = [ "rendering", "tiles", "configuration", "installation" ]
aliases = [ "/questions/42275" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot Create Socket](/questions/42275/cannot-create-socket)

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
<span id="post-42275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42275-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've been trying to install OSM on a CentOS 6.5 VM. I believe all of the pieces work correctly but when I try to have a tile rendered from the browser, the tile is not created.</p>
<p>The httpd error log says: [Sat Apr 11 00:42:52 2015] [warn] [client ::1] socket connect failed for: /var/run/renderd/renderd.sock with reason: Permission denied [Sat Apr 11 00:42:52 2015] [notice] [client ::1] Failed to connect to renderer</p>
<p>Here's the directory listing: [root@localhost 9.3]# ll /var/run/renderd/ total 8 -rw-r--r--. 1 osm osm 6 Apr 11 00:22 renderd.pid srwxrwxrwx. 1 osm osm 0 Apr 11 00:22 renderd.sock -rw-r--r--. 1 osm osm 1168 Apr 11 17:01 renderd.stats</p>
<p>Apache works</p>
<p>Renderd works - generate_tiles.py runs successfully</p>
<p>Mod_tile seems to work - <a href="http://localhost/mod_tile">http://localhost/mod_tile</a> returns the stats page</p>
<p>The python installation test to import mapnik was successful.</p>
<p>Any help would be greatly appreciated. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '15, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/36fcd3b44e9b92d98c9ed56b091374d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jgllo&#39;s gravatar image" />
<p><span>jgllo</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jgllo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '15, 01:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42275" class="comments-container">
&#10;</div>
<div id="comment-tools-42275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42275-form-container" class="comment-form-container">
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

<span id="42276"></span>

<div id="answer-container-42276" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42276-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jgllo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>generate_tiles.py</code> working does <em>not</em> mean that <code>renderd</code> is working, because this program renders tiles directly without involving renderd.</p>
<p>You should try if one of the renderd client programs, e.g .<code>render_list</code>, is working; <em>that</em> would be an indication of renderd doing its job right.</p>
<p>The most likely cause of your problem is that renderd is running all right, but with the socket not being writable for the unix user under which Apache is running, the web server cannot send messages through the socket. One possible solution would be a <code>chmod a+w /var/run/renderd/renderd.sock</code> but this will only fix things until the next restart of renderd. Normally renderd takes care to create this socket in a world-writable fashion (cf. <a href="https://github.com/openstreetmap/mod_tile/blob/master/src/daemon.c#L445)">https://github.com/openstreetmap/mod_tile/blob/master/src/daemon.c#L445)</a> and it is unclear why this should not be the case on your system.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '15, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42276" class="comments-container">
<span id="42283"></span>
<div id="comment-42283" class="comment">
<div id="post-42283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! Appreciate your reply!</p>
<p>render_list did work!</p>
<p>[osm@localhost renderd]$ render_list -a -z 0 -Z 5 -f -t /var/lib/mod_tile -s /var/run/renderd/renderd.sock debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile Rendering client Starting 1 rendering threads Rendering all tiles from zoom 0 to zoom 5 Rendering all tiles for zoom 0 from (0, 0) to (0, 0) Rendering all tiles for zoom 1 from (0, 0) to (1, 1) Rendering all tiles for zoom 2 from (0, 0) to (3, 3) Rendering all tiles for zoom 3 from (0, 0) to (7, 7) Rendering all tiles for zoom 4 from (0, 0) to (15, 15) Rendering all tiles for zoom 5 from (0, 0) to (31, 31) Waiting for rendering threads to finish</p>
<hr />
<hr />
<p>Total for all tiles rendered Meta tiles rendered: Rendered 24 tiles in 18.17 seconds (1.32 tiles/s) Total tiles rendered: Rendered 1536 tiles in 18.17 seconds (84.54 tiles/s) Total tiles handled: Rendered 24 tiles in 18.17 seconds (1.32 tiles/s)</p>
<hr />
<p>Zoom 00: min: 0.6 avg: 0.6 max: 0.6 over a total of 0.6s in 1 requests Zoom 01: min: 0.6 avg: 0.6 max: 0.6 over a total of 0.6s in 1 requests Zoom 02: min: 0.9 avg: 0.9 max: 0.9 over a total of 0.9s in 1 requests Zoom 03: min: 1.3 avg: 1.3 max: 1.3 over a total of 1.3s in 1 requests Zoom 04: min: 0.4 avg: 0.9 max: 1.3 over a total of 3.4s in 4 requests Zoom 05: min: 0.2 avg: 0.7 max: 3.4 over a total of 11.3s in 16 requests</p>
<p>But chmod a+w /var/run/renderd/renderd.sock did not make a difference. Still can't get the browser to initiate tile rendering.</p>
</div>
<div id="comment-42283-info" class="comment-info">
<span class="comment-age">(12 Apr '15, 06:13)</span> <span class="comment-user userinfo">jgllo</span>
</div>
</div>
<span id="42292"></span>
<div id="comment-42292" class="comment">
<div id="post-42292-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Are you still getting '/var/run/renderd/renderd.sock with reason: Permission denied'? Is it possible that you have SELinux enabled? If yes, try disabling it and re-try.</p>
</div>
<div id="comment-42292-info" class="comment-info">
<span class="comment-age">(12 Apr '15, 13:50)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="42294"></span>
<div id="comment-42294" class="comment">
<div id="post-42294-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Disabling SELinux did it!</p>
<p>Really appreciate your help, Frederik. I've been working on this for weeks!</p>
<p>Jeff</p>
</div>
<div id="comment-42294-info" class="comment-info">
<span class="comment-age">(12 Apr '15, 16:13)</span> <span class="comment-user userinfo">jgllo</span>
</div>
</div>
</div>
<div id="comment-tools-42276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42276-form-container" class="comment-form-container">
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

