+++
type = "question"
title = "Newbie 404 Err0r"
description = '''Hello dear Community, actually i installed a MapServer by a instruction. My Server Details might be more than enough: CPU: Intel Xeon E5-2640 RAM: 40 GB SSD: TB I changed some settings into postgres.conf to set up more performance. I got some 404 Errors when i zoom in in different areas. Weirdly whe...'''
date = "2019-09-05T08:58:00Z"
lastmod = "2019-09-06T09:52:00Z"
weight = 70625
keywords = [ "error" ]
aliases = [ "/questions/70625" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie 404 Err0r](/questions/70625/newbie-404-err0r)

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
<span id="post-70625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70625-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello dear Community, actually i installed a MapServer by a instruction. My Server Details might be more than enough:</p>
<p>CPU: Intel Xeon E5-2640 RAM: 40 GB SSD: TB</p>
<p>I changed some settings into postgres.conf to set up more performance. I got some 404 Errors when i zoom in in different areas. Weirdly when i zoom in into the Area where to start the View everything works fine. But if i go elsewhere i got 404 Error when i zoom in.</p>
<p>Hope you can give me some support so that i can fix the Issue</p>
<p>Best Regards</p>
<p>Tomaten</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '19, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/5ba9518915cc99bb350a1506557b083a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tomatentheo&#39;s gravatar image" />
<p><span>Tomatentheo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tomatentheo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70625" class="comments-container">
<span id="70628"></span>
<div id="comment-70628" class="comment">
<div id="post-70628-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think for you to get appropriate answers instead of CPU details it would be more helpful to tell what instructions you followed, what software you are using, how you are accessing the tiles and what you are trying to achieve.</p>
</div>
<div id="comment-70628-info" class="comment-info">
<span class="comment-age">(05 Sep '19, 09:25)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="70632"></span>
<div id="comment-70632" class="comment">
<div id="post-70632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I followed the instruction by switch2osm.org The Software I use is Bionic Beaver. Everything i configured is using by created osm user. As first id like to handle the 404 Error so that i get renderd tiles of my request.</p>
</div>
<div id="comment-70632-info" class="comment-info">
<span class="comment-age">(05 Sep '19, 10:20)</span> <span class="comment-user userinfo">Tomatentheo</span>
</div>
</div>
</div>
<div id="comment-tools-70625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70625-form-container" class="comment-form-container">
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

<span id="70626"></span>

<div id="answer-container-70626" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70626-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is likely that the <code>mod_tile</code> in your apache server cannot contact the rendering server, or that the rendering server cannot render tiles. The reasons for this can be many (disk space issue, file permission issue, postgresql not running, renderd not running, syntax error in style file, renderer cannot connect to database, ...). You will likely find answers in the <code>error.log</code> of your apache server, and/or the <code>syslog</code> file. It might also be helpful to start renderd in foreground mode so that you can follow exactly what it does (or tries to do, or fails to do) when you request a tile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '19, 09:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70626" class="comments-container">
<span id="70638"></span>
<div id="comment-70638" class="comment">
<div id="post-70638-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One mod_tile.conf which lies into Apache2 folder loads the Module by a absoulte path. The Path /usr/lib/apache2/modules is set by user and group root.Same is with the renderd.conf which is called by absolute path with root user/group. The User osm has a folder mod_tile too but here are the user and group to set by osm. But it might be not necessary because everything is configured by the instruction. error.log: [mpm_event:notice]AH... Apache/2.4.29(Ubuntu) OpenSSL/1.1.1 configured -- resuming normal operations (sounds like ok)</p>
<p>Which File permissions should be set? Postgres is running renderd running.Which style File do you mean? If the RendererAcc cant connect to DB you shouldnt get any picture? If i run the render in foregroud the renderer can load everything.&lt;mapnik log=""&gt; send everytime warnings out and when i scroll into map the Debugger writes: START TILE ajt 9 264-271 176-183, new metatile Rendering project coordinates 9 264 176 -&gt; 626172.135713|5635549.221413 1252344.2771425|6261721.357125 to a 8 x 8 tile *Connections often very fast closed. at the end of the Debugger: DEBUG: DONE TILE ajt 9 272-279 176-183 in 231.804 seconds debug: Creating and writing a metatile</p>
</div>
<div id="comment-70638-info" class="comment-info">
<span class="comment-age">(05 Sep '19, 14:21)</span> <span class="comment-user userinfo">Tomatentheo</span>
</div>
</div>
<span id="70639"></span>
<div id="comment-70639" class="comment">
<div id="post-70639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If there was something wrong with the rendering then Apache/mod_tile would serve the already existing tiles, but not create new tiles. If you see "DONE TILE ..." messages in your log file then that is not the case though. Double-check that renderd is actually adding new files to /var/lib/mod_tile when it does that (and not elsewhere). Double-check that the Apache user has read access to all files in /var/lib/mod_tile. Also ensure that the <code>ModTileMissingRequestTimeout</code> in your Apache config is set to a reasonably high value, try 60 to begin with. Do the 404 errors happen immediately or after some time? Does the "START TILE..." happen immediately after you try to load a tile?</p>
</div>
<div id="comment-70639-info" class="comment-info">
<span class="comment-age">(05 Sep '19, 15:10)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="70655"></span>
<div id="comment-70655" class="comment">
<div id="post-70655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Frederik, sorry for that i am late back, even seen you answered. How do i check, that new tiles were added to ajt?The folder structure ist /var/lib/mod_tile/ajt/... . */ajt has 755 by osm:osm Level 0-16 are created. I set up the ModTileMissingRequestTimout up to 60. The 404 Error does happen immediatly. Do i need to restart the renderer everytime again when i reload the Apache?</p>
</div>
<div id="comment-70655-info" class="comment-info">
<span class="comment-age">(06 Sep '19, 08:21)</span> <span class="comment-user userinfo">Tomatentheo</span>
</div>
</div>
<span id="70657"></span>
<div id="comment-70657" class="comment">
<div id="post-70657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Since i changed the ModTileMissingRequestTimeout the Server runs much slower and ther Error will be shown ca 15 seconds later. A 304 error will be printed for some Requests. That is a syptom that the renderer does works right?</p>
</div>
<div id="comment-70657-info" class="comment-info">
<span class="comment-age">(06 Sep '19, 09:52)</span> <span class="comment-user userinfo">Tomatentheo</span>
</div>
</div>
</div>
<div id="comment-tools-70626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70626-form-container" class="comment-form-container">
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

