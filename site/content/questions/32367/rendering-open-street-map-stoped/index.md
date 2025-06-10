+++
type = "question"
title = "Rendering “Open street map” stoped"
description = '''I am trying to build my own OpenStreetMap Server on - Ubuntu Server 12.04  I am following this instruction: http://www.slideshare.net/MarcHuang1/osm-installation-en  Everything is working quite fine and I can look map through web browser but there is some areas and zoom level which just don&#x27;t render...'''
date = "2014-04-14T18:25:00Z"
lastmod = "2014-04-27T13:06:00Z"
weight = 32367
keywords = [ "openstreetmap", "rendering", "renderd" ]
aliases = [ "/questions/32367" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering “Open street map” stoped](/questions/32367/rendering-open-street-map-stoped)

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
<span id="post-32367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32367-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to build my own OpenStreetMap Server on - Ubuntu Server 12.04<br />
I am following this instruction: <a href="http://www.slideshare.net/MarcHuang1/osm-installation-en">http://www.slideshare.net/MarcHuang1/osm-installation-en</a><br />
</p>
<p>Everything is working quite fine and I can look map through web browser but there is some areas and zoom level which just don't render(they stay gray even after waiting long time).<br />
At the same time <strong>renderd</strong> itself gives the following output:</p>
<pre><code>renderd[2374]: DEBUG: Got incoming connection, fd 28, number 9
renderd[2374]: DEBUG: Got incoming connection, fd 29, number 10
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(28) xml(default), z(13), x(3931), y(3057), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(29) xml(default), z(13), x(3933), y(3057), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming connection, fd 30, number 11
renderd[2374]: DEBUG: Got incoming connection, fd 31, number 12
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(30) xml(default), z(13), x(3932), y(3056), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(31) xml(default), z(13), x(3932), y(3057), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming connection, fd 32, number 13
renderd[2374]: DEBUG: Got incoming connection, fd 33, number 14
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(32) xml(default), z(13), x(3931), y(3056), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(33) xml(default), z(13), x(3933), y(3056), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming connection, fd 34, number 15
renderd[2374]: DEBUG: Got incoming connection, fd 35, number 16
renderd[2374]: DEBUG: Got incoming connection, fd 36, number 17
renderd[2374]: DEBUG: Got incoming connection, fd 37, number 18
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(37) xml(default), z(13), x(3933), y(3055), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(36) xml(default), z(13), x(3931), y(3055), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(35) xml(default), z(13), x(3932), y(3058), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(34) xml(default), z(13), x(3932), y(3055), mime(image/png), options()
renderd[2374]: DEBUG: Connection 8, fd 28 closed, now 17 left
renderd[2374]: DEBUG: Connection 8, fd 29 closed, now 16 left
renderd[2374]: DEBUG: Got incoming connection, fd 28, number 17
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(28) xml(default), z(13), x(3933), y(3058), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming connection, fd 29, number 18
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(29) xml(default), z(13), x(3931), y(3058), mime(image/png), options()
renderd[2374]: DEBUG: Connection 8, fd 30 closed, now 17 left
renderd[2374]: DEBUG: Connection 8, fd 31 closed, now 16 left
renderd[2374]: DEBUG: Connection 9, fd 33 closed, now 15 left
renderd[2374]: DEBUG: Connection 8, fd 32 closed, now 14 left
renderd[2374]: DEBUG: Got incoming connection, fd 30, number 15
renderd[2374]: DEBUG: Got incoming connection, fd 31, number 16
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(31) xml(default), z(13), x(3934), y(3056), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(30) xml(default), z(13), x(3930), y(3056), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming connection, fd 32, number 17
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(32) xml(default), z(13), x(3930), y(3057), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming connection, fd 33, number 18
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(33) xml(default), z(13), x(3934), y(3057), mime(image/png), options()
renderd[2374]: DEBUG: Connection 11, fd 37 closed, now 17 left
renderd[2374]: DEBUG: Connection 10, fd 36 closed, now 16 left
renderd[2374]: DEBUG: Connection 9, fd 35 closed, now 15 left
renderd[2374]: DEBUG: Connection 8, fd 34 closed, now 14 left
renderd[2374]: DEBUG: Got incoming connection, fd 34, number 15
renderd[2374]: DEBUG: Got incoming connection, fd 35, number 16
renderd[2374]: DEBUG: Got incoming connection, fd 36, number 17
renderd[2374]: DEBUG: Got incoming connection, fd 37, number 18
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(35) xml(default), z(13), x(3934), y(3055), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(36) xml(default), z(13), x(3930), y(3058), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(37) xml(default), z(13), x(3934), y(3058), mime(image/png), options()
renderd[2374]: DEBUG: Got incoming request with protocol version 2
renderd[2374]: DEBUG: Got command RenderPrio fd(34) xml(default), z(13), x(3930), y(3055), mime(image/png), options()
renderd[2374]: DEBUG: Connection 8, fd 28 closed, now 17 left
renderd[2374]: DEBUG: Connection 8, fd 29 closed, now 16 left
renderd[2374]: DEBUG: Connection 9, fd 31 closed, now 15 left
renderd[2374]: DEBUG: Connection 9, fd 32 closed, now 14 left
renderd[2374]: DEBUG: Connection 8, fd 30 closed, now 13 left
renderd[2374]: DEBUG: Connection 8, fd 33 closed, now 12 left
renderd[2374]: DEBUG: Connection 9, fd 35 closed, now 11 left
renderd[2374]: DEBUG: Connection 9, fd 36 closed, now 10 left
renderd[2374]: DEBUG: Connection 9, fd 37 closed, now 9 left
renderd[2374]: DEBUG: Connection 8, fd 34 closed, now 8 left</code></pre>
<p>From here it doesn't go any futher and map in webbrowser will be fully grey</p>
<p><br />
I also tryed to Pre-render tiles form zoom levels 0 to 18 with the following command:<br />
<code>render_list --all --force --socket=/var/run/renderd/renderd.sock --min-zoom=0 --max-zoom=18 </code></p>
<p>The output for this is: <code> debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile Rendering client Starting 1 rendering threads Rendering all tiles from zoom 0 to zoom 18 Rendering all tiles for zoom 0 from (0, 0) to (0, 0) Rendering all tiles for zoom 1 from (0, 0) to (1, 1) Rendering all tiles for zoom 2 from (0, 0) to (3, 3) Rendering all tiles for zoom 3 from (0, 0) to (7, 7) Rendering all tiles for zoom 4 from (0, 0) to (15, 15) Rendering all tiles for zoom 5 from (0, 0) to (31, 31) Rendering all tiles for zoom 6 from (0, 0) to (63, 63) </code></p>
<p>It stops on zoom level 6 and don't go any futher even with two days waiting. Seems like something is stopping him to finish rendering but I don't know what.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '14, 18:25</strong></p>
<img src="https://secure.gravatar.com/avatar/65147ae2ebe710b83f86701fde23a25a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hukko&#39;s gravatar image" />
<p><span>hukko</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hukko has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-32367" class="comments-container">
&#10;</div>
<div id="comment-tools-32367" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32367-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="32688"></span>

<div id="answer-container-32688" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32688-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem was that files in directory <strong><em>/var/run/renderd/</em></strong> didn't have execution premission so I chmod the directory and it startert rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '14, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/65147ae2ebe710b83f86701fde23a25a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hukko&#39;s gravatar image" />
<p><span>hukko</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hukko has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-32688" class="comments-container">
&#10;</div>
<div id="comment-tools-32688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32688-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32386"></span>

<div id="answer-container-32386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32386-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have to ask the silly question: do you have enough disk space? I don't know if rendering needs /tmp for anything, but could it be running out of space? Or /var?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '14, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/b95d3c8204ce3675edc226a8a55b7067?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jack%20the%20Ripper&#39;s gravatar image" />
<p><span>Jack the Ripper</span><br />
<span class="score" title="280 reputation points">280</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jack the Ripper has one accepted answer">12%</span> </br></p>
</div>
</div>
<div id="comments-container-32386" class="comments-container">
<span id="32388"></span>
<div id="comment-32388" class="comment">
<div id="post-32388-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My linux server has 97GB xfs filesytem from which 79 GB is free.</p>
</div>
<div id="comment-32388-info" class="comment-info">
<span class="comment-age">(15 Apr '14, 21:22)</span> <span class="comment-user userinfo">hukko</span>
</div>
</div>
<span id="32390"></span>
<div id="comment-32390" class="comment">
<div id="post-32390-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That takes care of the space question, then.</p>
<p>Um. My basic other two thoughts are look in /var/log/messages (maybe tail -f it while your render is running), and maybe even /var/log/Xorg.0.log (or wherever Ubuntu is puting the Xorg log these days, I haven't kept up) and see if you notice any warnings or errors that seem relevant.</p>
</div>
<div id="comment-32390-info" class="comment-info">
<span class="comment-age">(15 Apr '14, 22:08)</span> <span class="comment-user userinfo">Jack the Ripper</span>
</div>
</div>
</div>
<div id="comment-tools-32386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32386-form-container" class="comment-form-container">
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

