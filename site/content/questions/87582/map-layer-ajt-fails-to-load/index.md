+++
type = "question"
title = "map layer &#x27;ajt&#x27; fails to load"
description = '''After following the tutorial from Switch2OSM I ran into the following error after running this command: renderd -f -c /usr/local/etc/renderd.conf and launching the server through the web browser using this address: http://localhost/hot/0/0/0.png renderd[64331]: An error occurred while loading the ma...'''
date = "2023-08-01T22:18:00Z"
lastmod = "2023-08-01T23:17:00Z"
weight = 87582
keywords = [ "openstreetmap", "switch2osm", "mapnik" ]
aliases = [ "/questions/87582" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [map layer 'ajt' fails to load](/questions/87582/map-layer-ajt-fails-to-load)

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
<span id="post-87582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87582-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After following the tutorial from <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">Switch2OSM</a> I ran into the following error after running this command: <strong>renderd -f -c /usr/local/etc/renderd.conf</strong> and launching the server through the web browser using this address: <strong><a href="http://localhost/hot/0/0/0.png">http://localhost/hot/0/0/0.png</a></strong></p>
<p><code>renderd[64331]: An error occurred while loading the map layer 'ajt': Could not create datasource for type: 'postgis' (no datasource plugin directories have been successfully registered) encountered during parsing of layer 'landcover-low-zoom' in Layer at line 803 of '/home/user/src/openstreetmap-carto/mapnik.xml' renderd[64331]: DEBUG: Got incoming connection, fd 7, number 1 renderd[64331]: DEBUG: Got incoming request with protocol version 2 renderd[64331]: DEBUG: Got command RenderPrio fd(7) xml(ajt), z(0), x(0), y(0), mime(image/png), options() renderd[64331]: Received request for map layer 'ajt' which failed to load renderd[64331]: DEBUG: Sending render cmd(4 ajt 0/0/0) with protocol version 2 to fd 7 renderd[64331]: DEBUG: Connection 0, fd 7 closed, now 0 left</code></p>
<p>After doing some research I haven't found anything useful to solve this problem. Any help would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '23, 22:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0e2a88b26a54f5e9d752e94acaca8f24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JaimeMiranda57&#39;s gravatar image" />
<p><span>JaimeMiranda57</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JaimeMiranda57 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '23, 22:23</strong> </span></p>
</div>
</div>
<div id="comments-container-87582" class="comments-container">
&#10;</div>
<div id="comment-tools-87582" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87582-form-container" class="comment-form-container">
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

<span id="87583"></span>

<div id="answer-container-87583" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87583-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing that the bit that you're missing is the "While still working as the “postgres” user, set up PostGIS on the PostgreSQL database" part of that page.</p>
<p>Another possibility is that the "plugins_dir" setting in your "renderd.conf" is wrong - have a look below "/usr/lib/mapnik/" and see what there is.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '23, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87583" class="comments-container">
<span id="87584"></span>
<div id="comment-87584" class="comment">
<div id="post-87584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I run the command <code>createdb -E UTF8 -O myUsername gis</code> the database is successfully created. After that I keep following the tutorial, type in psql in terminal, I get the <strong>"postgres=#"</strong> prompt, and right after that I type in <code>\c gis</code> and get the <strong>"You are now connected to database ‘gis’ as user 'postgres'"</strong>. I'm guessing that that's what you mean by the first sentence in your answer? So to my understanding I am still working as the "postgres" user, correct? If that's not it I'm misunderstanding and if so, could you please clarify? Thanks.</p>
<p>I checked "/usr/lib/mapnik" and there's another folder inside that directory called "3.1". If I <code>cd</code> into that directory, there's another directory inside called "input". So, in essence, this is the path "/usr/lib/mapnik/3.1/input" and inside that I have 10 .input files.</p>
</div>
<div id="comment-87584-info" class="comment-info">
<span class="comment-age">(01 Aug '23, 23:17)</span> <span class="comment-user userinfo">JaimeMiranda57</span>
</div>
</div>
</div>
<div id="comment-tools-87583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87583-form-container" class="comment-form-container">
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

