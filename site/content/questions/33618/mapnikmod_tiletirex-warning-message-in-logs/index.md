+++
type = "question"
title = "mapnik/mod_tile/tirex warning message in logs"
description = '''Hi, I have a mapnik/mod_tile/tirex stack, which works fine to produce new tiles, but I see warning in the logs when I am requesting tiles which have been already rendered and  are expired. On the client side I still get the old tiles so it is not a problem right now but I am worried that it is wasti...'''
date = "2014-06-02T10:11:00Z"
lastmod = "2014-06-02T10:11:00Z"
weight = 33618
keywords = [ "tirex", "mod_tile" ]
aliases = [ "/questions/33618" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [mapnik/mod_tile/tirex warning message in logs](/questions/33618/mapnikmod_tiletirex-warning-message-in-logs)

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
<span id="post-33618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33618-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have a mapnik/mod_tile/tirex stack, which works fine to produce new tiles, but I see warning in the logs when I am requesting tiles which have been already rendered and are expired. On the client side I still get the old tiles so it is not a problem right now but I am worried that it is wasting resources.</p>
<p>I have installed mapnik 2.0 from distribution Debian 7.0.0 modtile from source <a href="https://github.com/openstreetmap/mod_tile">https://github.com/openstreetmap/mod_tile</a> tirex from source <a href="http://svn.openstreetmap.org/applications/utils/tirex">http://svn.openstreetmap.org/applications/utils/tirex</a></p>
<pre><code>==&gt; apache2/error.log &lt;==
--------------------------
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(1281): [client 217.198.117.32] tile_translate: uri(/tiles/15/17859/11195.png)
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(1298): [client 217.198.117.32] tile_translate: testing baseuri(/tiles/) name(default) extension(png)
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(1344): [client 217.198.117.32] tile_translate: request for default was 17859 11195 32768
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(317): [client 217.198.117.32] get_storage_backend: Retrieving storage back end for tile layer 0 in pool 7f2c71447028 and thread 139828855555904
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(339): [client 217.198.117.32] get_storage_backend: Found backends (7f2c71447e30) for this lifecycle 7f2c71447028 in thread 139828855555904
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(350): [client 217.198.117.32] get_storage_backend: Storage backend found in current lifecycle 7f2c71447028 for current tile layer 0 in thread 139828855555904
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(1383): [client 217.198.117.32] tile_translate: op(tile_serve) xml(default) mime(image/png) z(15) x(17859) y(11195)
[Mon Jun 02 10:42:05 2014] [info] [client 217.198.117.32] tile_storage_hook: handler(tile_serve), uri(/tiles/15/17859/11195.png)
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(367): [client 217.198.117.32] tile_state: determined state of default 17859 11195 15 on store 7f2c735ca1d0: Tile size: 465286, expired: 1 created: 1401143927
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(166): [client 217.198.117.32] Connecting to renderd on Unix socket /var/lib/tirex/modtile.sock
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(183): [client 217.198.117.32] socket connect succeed for: /var/lib/tirex/modtile.sock 
[Mon Jun 02 10:42:05 2014] [info] [client 217.198.117.32] Requesting style(default) z(15) x(17859) y(11195) from renderer with priority 7
[Mon Jun 02 10:42:05 2014] [warn] [client 217.198.117.32] request_tile: Failed to read response from rendering socket No such file or directory r=0
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(1186): [client 217.198.117.32] tile_handler_serve: xml(default) z(15) x(17859) y(11195)
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(1210): [client 217.198.117.32] Read tile of length 6988 from file:///var/lib/mod_tile/default/15/0/66/91/203/8.meta: 
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(367): [client 217.198.117.32] tile_state: determined state of default 17859 11195 15 on store 7f2c735ca1d0: Tile size: 465286, expired: 1 created: 1401143927
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(444): [client 217.198.117.32] expires(tile_serve), uri(/tiles/15/17859/11195.png),, path_info((null))\n
[Mon Jun 02 10:42:05 2014] [debug] ./src/mod_tile.c(494): [client 217.198.117.32] Setting tiles maxAge to 1327\n
&#10;output from  tirex-master --debug:
----------------------------------
tirex-master[20256]: connection from mod_tile accepted
tirex-master[20256]: connection from mod_tile accepted
tirex-master[20256]: connection from mod_tile accepted
tirex-master[20256]: read request from mod_tile: ver=2 cmd=7 x=17859 y=11193 z=15 map=default
tirex-master[20256]: read request from mod_tile: ver=2 cmd=7 x=17859 y=11194 z=15 map=default
tirex-master[20256]: read request from mod_tile: ver=2 cmd=7 x=17860 y=11194 z=15 map=default
tirex-master[20256]: connection from mod_tile accepted
tirex-master[20256]: connection from mod_tile accepted
tirex-master[20256]: read request from mod_tile: ver=2 cmd=7 x=17860 y=11195 z=15 map=default
tirex-master[20256]: read request from mod_tile: ver=2 cmd=7 x=17860 y=11193 z=15 map=default
tirex-master[20256]: connection from mod_tile accepted
tirex-master[20256]: read request from mod_tile: ver=2 cmd=7 x=17859 y=11195 z=15 map=default
</code></pre>
<p>while tirex-backend-manager --debug does not produce any output on the console for this request.</p>
<p>Any suggestions? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '14, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/921dd5f58004b64de234e7f9f9813a3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brunesto&#39;s gravatar image" />
<p><span>brunesto</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brunesto has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '14, 10:12</strong> </span></p>
</div>
</div>
<div id="comments-container-33618" class="comments-container">
&#10;</div>
<div id="comment-tools-33618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33618-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

