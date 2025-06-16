+++
type = "question"
title = "Pink tiles in map"
description = '''Hi, I have problem with OSM. When I browse http://localhost/osm/slippymap.html I have pink baground.   renderd -f -c /etc/renderd.conf gave me: renderd[2229]: An error occurred while loading the map layer &#x27;default&#x27;: : FATAL: role &quot;www-data&quot; does not exist (encountered during parsing of layer &#x27;landco...'''
date = "2013-11-21T12:34:00Z"
lastmod = "2013-11-21T15:36:00Z"
weight = 28333
keywords = [ "pink", "failed", "tailes", "socket", "connect" ]
aliases = [ "/questions/28333" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Pink tiles in map](/questions/28333/pink-tiles-in-map)

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
<span id="post-28333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28333-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have problem with OSM. When I browse <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a> I have pink baground. renderd -f -c /etc/renderd.conf gave me:</p>
<p>renderd[2229]: An error occurred while loading the map layer 'default': :</p>
<p>FATAL: role "www-data" does not exist (encountered during parsing of layer 'landcover' in map '/etc/mapnik-osm-data/osm.xml')</p>
<p>renderd[2229]: An error occurred while loading the map layer 'default': : FATAL: role "www-data" does not exist (encountered during parsing of layer 'landcover' in map '/etc/mapnik-osm-data/osm.xml')</p>
<p>renderd[2229]: An error occurred while loading the map layer 'default': : FATAL: role "www-data" does not exist (encountered during parsing of layer 'landcover' in map '/etc/mapnik-osm-data/osm.xml')</p>
<p>renderd[2229]: An error occurred while loading the map layer 'default': : FATAL: role "www-data" does not exist (encountered during parsing of layer 'landcover' in map '/etc/mapnik-osm-data/osm.xml')</p>
<p>And apache gave errors:</p>
<p>[Thu Nov 21 13:16:08 2013] [notice] [client 127.0.0.1] Failed to connect to renderer, referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>[Thu Nov 21 13:16:08 2013] [info] [client 127.0.0.1] tile_storage_hook: handler(tile_serve), uri(/osm/10/528/360.png), filename(/var/lib/mod_tile/default/10/0/0/33/22/8.meta), path_info((null)), referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>[Thu Nov 21 13:16:08 2013] [info] [client 127.0.0.1] tile_storage_hook: handler(tile_serve), uri(/osm/10/538/354.png), filename(/var/lib/mod_tile/default/10/0/0/33/22/128.meta), path_info((null)), referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>[Thu Nov 21 13:16:08 2013] [warn] [client 127.0.0.1] socket connect failed for: /var/run/renderd/renderd.sock with reason: Connection refused, referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>[Thu Nov 21 13:16:08 2013] [warn] [client 127.0.0.1] socket connect failed for: /var/run/renderd/renderd.sock with reason: Connection refused, referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>[Thu Nov 21 13:16:08 2013] [notice] [client 127.0.0.1] Failed to connect to renderer, referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>[Thu Nov 21 13:16:08 2013] [notice] [client 127.0.0.1] Failed to connect to renderer, referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>[Thu Nov 21 13:16:08 2013] [info] [client 127.0.0.1] tile_storage_hook: handler(tile_serve), uri(/osm/10/538/360.png), filename(/var/lib/mod_tile/default/10/0/0/33/22/136.meta), path_info((null)), referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>[Thu Nov 21 13:16:08 2013] [warn] [client 127.0.0.1] socket connect failed for: /var/run/renderd/renderd.sock with reason: Connection refused, referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>[Thu Nov 21 13:16:08 2013] [notice] [client 127.0.0.1] Failed to connect to renderer, referer: <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a></p>
<p>Could somebody help me resolve problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pink" rel="tag" title="see questions tagged &#39;pink&#39;">pink</span> <span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span> <span class="post-tag tag-link-tailes" rel="tag" title="see questions tagged &#39;tailes&#39;">tailes</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-connect" rel="tag" title="see questions tagged &#39;connect&#39;">connect</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '13, 12:34</strong></p>
<img src="https://secure.gravatar.com/avatar/477f3eed98cb4e1746b79f26c0f1aff9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonny1998&#39;s gravatar image" />
<p><span>jonny1998</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonny1998 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28333" class="comments-container">
<span id="28336"></span>
<div id="comment-28336" class="comment">
<div id="post-28336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does the comment by Vincent to <a href="/questions/19525/error-when-try-to-use-nominatim-pgsql-role-www-data-is-not-permitted-to-log-in">this answer</a> resolve the problem?</p>
</div>
<div id="comment-28336-info" class="comment-info">
<span class="comment-age">(21 Nov '13, 13:17)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28333-form-container" class="comment-form-container">
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

<span id="28338"></span>

<div id="answer-container-28338" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28338-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This seems to be a priviliges problem as jonny1998 says.</p>
<p>You can alter it directly using <strong>psql</strong> shell or purge and update like the package <strong>installer</strong> does:<br />
<code>sudo /usr/bin/install-postgis-osm-user.sh gis www-data</code><br />
see <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '13, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-28338" class="comments-container">
&#10;</div>
<div id="comment-tools-28338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28338-form-container" class="comment-form-container">
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

