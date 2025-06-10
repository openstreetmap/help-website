+++
type = "question"
title = "render_list does nothing at all"
description = '''I searched this forum but found nothing. Also documentation on render_list seems to be missing, where can I find that? This is my output from render_list: debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile Rendering client Starting 1 rendering threads Rendering all ...'''
date = "2021-10-21T20:50:00Z"
lastmod = "2022-09-28T13:02:00Z"
weight = 82299
keywords = [ "render_list" ]
aliases = [ "/questions/82299" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [render_list does nothing at all](/questions/82299/render_list-does-nothing-at-all)

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
<span id="post-82299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82299-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I searched this forum but found nothing. Also documentation on render_list seems to be missing, where can I find that?</p>
<p>This is my output from render_list:</p>
<pre><code>debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
Rendering client
Starting 1 rendering threads
Rendering all tiles from zoom 0 to zoom 20
Rendering all tiles for zoom 0 from (0, 0) to (0, 0)
Rendering all tiles for zoom 1 from (0, 0) to (1, 1)
Rendering all tiles for zoom 2 from (0, 0) to (3, 3)
Rendering all tiles for zoom 3 from (0, 0) to (7, 7)
Rendering all tiles for zoom 4 from (0, 0) to (15, 15)
Rendering all tiles for zoom 5 from (0, 0) to (31, 31)
Rendering all tiles for zoom 6 from (0, 0) to (63, 63)</code></pre>
<p>I tried lots of different ways to call render_list but always this result.</p>
<p>I also checked with htop, no cpu or memory activity.</p>
<p>Any help is welcome, thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Oct '21, 20:50</strong></p>
<img src="https://secure.gravatar.com/avatar/dcd4b2bb9370eab79f2f3fa650f5ed76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerb_1963&#39;s gravatar image" />
<p><span>Gerb_1963</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerb_1963 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '21, 20:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-82299" class="comments-container">
<span id="82300"></span>
<div id="comment-82300" class="comment">
<div id="post-82300-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>tried lots of different ways to call render_list but always this result.</p>
</blockquote>
<p>Could you give us a clue what you have actually tried?</p>
</div>
<div id="comment-82300-info" class="comment-info">
<span class="comment-age">(21 Oct '21, 20:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82304"></span>
<div id="comment-82304" class="comment">
<div id="post-82304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried various command lines:</p>
<ol>
<li>With or without socket;</li>
<li>With or without database specification;</li>
<li>Various zoom levels;</li>
<li>Basically anything that the help of render_list tells me and what I found on stackoverflow and similar sites.</li>
</ol>
</div>
<div id="comment-82304-info" class="comment-info">
<span class="comment-age">(22 Oct '21, 16:11)</span> <span class="comment-user userinfo">Gerb_1963</span>
</div>
</div>
<span id="82305"></span>
<div id="comment-82305" class="comment">
<div id="post-82305-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If it helps, every morning a server I look after runs</p>
<pre><code>https://github.com/SomeoneElseOSM/mod_tile/blob/zoom/rerender_low.sh</code></pre>
<p>which in turn calls "render_list":</p>
<pre><code>https://github.com/alx77/render_list_geo.pl/blob/master/render_list_geo.pl#L52</code></pre>
<p>You still haven't told us exactly what options you're trying and what the effect is (we know that no tiles are rendered, but does a request for a new tile appear in the log? Does an error occur there? You have not said), but hopefully an example of "one that does work" should help you to find out what the problem is.</p>
</div>
<div id="comment-82305-info" class="comment-info">
<span class="comment-age">(22 Oct '21, 16:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82299" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82299-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="82428"></span>

<div id="answer-container-82428" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82428-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gerb_1963 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Although "render_list" isn't directly mentioned by the switch2osm documentation, I've just tested it on a Debian 11 server set up according to those instructions. When I run</p>
<pre><code>sudo -u _renderd render_list -a -n 1  --map=s2o --tile-dir=/var/lib/mod_tile/s2o --min-zoom=0 --max-zoom=6</code></pre>
<p>I get tiles at zoom levels 0-6 rendered as expected. The "s2o" in that command refers to the entry in "renderd.conf" that I want to render tiles for, and "s2o" is what you get by default on Debian (and if I remember correctly, Ubuntu 21.04). The following is written to stdout:</p>
<pre><code>debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile/s2o
Rendering client
Starting 1 rendering threads
Rendering all tiles from zoom 0 to zoom 6
Rendering all tiles for zoom 0 from (0, 0) to (0, 0)
Rendering all tiles for zoom 1 from (0, 0) to (1, 1)
Rendering all tiles for zoom 2 from (0, 0) to (3, 3)
Rendering all tiles for zoom 3 from (0, 0) to (7, 7)
Rendering all tiles for zoom 4 from (0, 0) to (15, 15)
Rendering all tiles for zoom 5 from (0, 0) to (31, 31)
Rendering all tiles for zoom 6 from (0, 0) to (63, 63)
Waiting for rendering threads to finish
&#10;*****************************************************
*****************************************************
Total for all tiles rendered
Meta tiles rendered: Rendered 88 tiles in 236.36 seconds (0.37 tiles/s)
Total tiles rendered: Rendered 5632 tiles in 236.36 seconds (23.83 tiles/s)
Total tiles handled: Rendered 88 tiles in 236.36 seconds (0.37 tiles/s)
*****************************************************
Zoom 00: min:  2.4    avg:  2.4     max:  2.4     over a total of      2.4s in 1 requests
Zoom 01: min:  2.6    avg:  2.6     max:  2.6     over a total of      2.6s in 1 requests
Zoom 02: min:  2.8    avg:  2.8     max:  2.8     over a total of      2.8s in 1 requests
Zoom 03: min:  3.4    avg:  3.4     max:  3.4     over a total of      3.4s in 1 requests
Zoom 04: min:  1.9    avg:  2.5     max:  3.2     over a total of     10.1s in 4 requests
Zoom 05: min:  2.1    avg:  3.0     max:  5.3     over a total of     48.0s in 16 requests
Zoom 06: min:  2.0    avg:  2.6     max:  5.3     over a total of    167.2s in 64 requests
*****************************************************
*****************************************************</code></pre>
<p>in syslog, there's output as each tile is rendered:</p>
<pre><code>Oct 31 11:16:11 debianvm65 renderd[19309]: renderd[19309]: DEBUG: START TILE s2o 6 56-63 56-63, new metatile
Oct 31 11:16:11 debianvm65 renderd[19309]: renderd[19309]: Rendering projected coordinates 6 56 56 -&gt; 15028131.257100|-20037508.342800 20037508.342800|-15028131.257100 to a 8 x 8 tile
Oct 31 11:16:11 debianvm65 render_list: DEBUG: Sending render cmd(6 s2o 6/56/56) with protocol version 2 to fd 3
Oct 31 11:16:11 debianvm65 renderd[19309]: DEBUG: Got incoming request with protocol version 2
Oct 31 11:16:11 debianvm65 renderd[19309]: DEBUG: Got command RenderBulk fd(7) xml(s2o), z(6), x(56), y(56), mime(image/png), options()
Oct 31 11:16:11 debianvm65 renderd[19309]: DEBUG: START TILE s2o 6 56-63 56-63, new metatile
Oct 31 11:16:11 debianvm65 renderd[19309]: Rendering projected coordinates 6 56 56 -&gt; 15028131.257100|-20037508.342800 20037508.342800|-15028131.257100 to a 8 x 8 tile
Oct 31 11:16:14 debianvm65 renderd[19309]: renderd[19309]: DEBUG: DONE TILE s2o 6 56-63 56-63 in 2.794 seconds</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '21, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82428" class="comments-container">
<span id="82429"></span>
<div id="comment-82429" class="comment">
<div id="post-82429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you omit the "--map" parameter you might see something like this in syslog:</p>
<pre><code>Oct 31 11:01:13 debianvm65 renderd[19309]: No map for: default</code></pre>
<p>and that can cause render_list to "just sit there" waiting for a message that never comes. However, if you tell it which tiles to render, it will work.</p>
</div>
<div id="comment-82429-info" class="comment-info">
<span class="comment-age">(31 Oct '21, 11:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82431"></span>
<div id="comment-82431" class="comment">
<div id="post-82431-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi SomeoneElse,</p>
<p>That works like a charm. I wonder how you figured that out. Is it documented somewhere or does one need to be an experienced technician to be able to do this?</p>
<p>Thank you very much, I appreciate this.</p>
<p>Ciao, Gerben</p>
</div>
<div id="comment-82431-info" class="comment-info">
<span class="comment-age">(31 Oct '21, 15:09)</span> <span class="comment-user userinfo">Gerb_1963</span>
</div>
</div>
<span id="82437"></span>
<div id="comment-82437" class="comment">
<div id="post-82437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The "sudo -u _renderd render_list -a -n 1 --map=s2o --tile-dir=/var/lib/mod_tile/s2o --min-zoom=0 --max-zoom=6" part was basically me putting together a minimum set of options, based on what "render_list --help" says.</p>
<p>I initially tried it without "--map" and got the "No map for: default" error (and to be fair "render_list --help" specifically says "--map defaults to 'default'", rather than "s2o").</p>
</div>
<div id="comment-82437-info" class="comment-info">
<span class="comment-age">(31 Oct '21, 22:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82438"></span>
<div id="comment-82438" class="comment">
<div id="post-82438-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For completeness, --min-x, --min-y, --max-x and --max-y also all work as expected.</p>
</div>
<div id="comment-82438-info" class="comment-info">
<span class="comment-age">(31 Oct '21, 22:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82441"></span>
<div id="comment-82441" class="comment">
<div id="post-82441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wasn't aware that the part "sudo -u _renderd " must be in the command line. I couldn't find any documentation on that.</p>
</div>
<div id="comment-82441-info" class="comment-info">
<span class="comment-age">(01 Nov '21, 15:50)</span> <span class="comment-user userinfo">Gerb_1963</span>
</div>
</div>
<span id="82443"></span>
<div id="comment-82443" class="comment not_top_scorer">
<div id="post-82443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-21/">21.04 guide</a> does have "sudo -u _renderd" in it where it's describing commands that interact with the database. That guide says:</p>
<pre><code>“_renderd” is used for the renderd daemon, and we’ll need to make sure lots of the commands below are run as that user.</code></pre>
<p>It doesn't mention render_list at all, so doesn't explicitly say you need to run that via "sudo -u _renderd" too. Given that a few people have tripped up over render_list (see other help questions here) it might be worth mentioning, perhaps in a separate guide.</p>
</div>
<div id="comment-82443-info" class="comment-info">
<span class="comment-age">(01 Nov '21, 16:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82428" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-82428-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82442"></span>

<div id="answer-container-82442" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82442-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Conclusion: The solution to this question is that render list needs to be run in a command line with "sudo -u _renderd" in front of it. That is in an ubuntu 21.04 environment with the guide to build a tileserver from the switch2osm site.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '21, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/dcd4b2bb9370eab79f2f3fa650f5ed76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerb_1963&#39;s gravatar image" />
<p><span>Gerb_1963</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerb_1963 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82442" class="comments-container">
&#10;</div>
<div id="comment-tools-82442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82442-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82354"></span>

<div id="answer-container-82354" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82354-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As I said, I tried all options that I can think of and nothing worked. The commands that you mention are not available for me. I followed the guide to install a server on ubuntu 2104.</p>
<p>How can I check for tile requests in a log?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '21, 12:09</strong></p>
<img src="https://secure.gravatar.com/avatar/dcd4b2bb9370eab79f2f3fa650f5ed76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerb_1963&#39;s gravatar image" />
<p><span>Gerb_1963</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerb_1963 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '21, 12:12</strong> </span></p>
</div>
</div>
<div id="comments-container-82354" class="comments-container">
<span id="82355"></span>
<div id="comment-82355" class="comment">
<div id="post-82355-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>I followed the guide to install a server on ubuntu 2104.</p>
</blockquote>
<p>Which one are you following?</p>
</div>
<div id="comment-82355-info" class="comment-info">
<span class="comment-age">(25 Oct '21, 12:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82356"></span>
<div id="comment-82356" class="comment">
<div id="post-82356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're not reallly helping, forget it. This is a good reason <em>not</em> to switch to OSM. No documentation, no help.</p>
</div>
<div id="comment-82356-info" class="comment-info">
<span class="comment-age">(25 Oct '21, 12:26)</span> <span class="comment-user userinfo">Gerb_1963</span>
</div>
</div>
<span id="82358"></span>
<div id="comment-82358" class="comment">
<div id="post-82358-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>We're trying to, but if you <em>literally won't tell us the full command that you ran before an error occurred</em> you're requiring psychic powers of anyone why tries to help you.</p>
</div>
<div id="comment-82358-info" class="comment-info">
<span class="comment-age">(25 Oct '21, 12:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82354" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82354-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84959"></span>

<div id="answer-container-84959" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84959-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi. I have a similarity problem. I would like to understand if render_list is working or not. I have run:</p>
<pre><code>render_list  -a  -f  -m ajt  -z 0  -Z 10</code></pre>
<p>and I get:</p>
<pre><code>Rendering client
Starting 1 rendering threads
Rendering all tiles from zoom 0 to zoom 10
Rendering all tiles for zoom 0 from (0, 0) to (0, 0)
Rendering all tiles for zoom 1 from (0, 0) to (1, 1)
Rendering all tiles for zoom 2 from (0, 0) to (3, 3)
Rendering all tiles for zoom 3 from (0, 0) to (7, 7)
Rendering all tiles for zoom 4 from (0, 0) to (15, 15)
Rendering all tiles for zoom 5 from (0, 0) to (31, 31)
Rendering all tiles for zoom 6 from (0, 0) to (63, 63)</code></pre>
<p>But it has been standing there for more than a day. I would like to be sure it's working! Thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '22, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/03a2687b8ded72a2784e1bb2fcb4eeea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rmoggia&#39;s gravatar image" />
<p><span>rmoggia</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rmoggia has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84959" class="comments-container">
<span id="85750"></span>
<div id="comment-85750" class="comment">
<div id="post-85750-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd suggest that you look at the answer above that explains how it is supposed to work - do you get any errors in syslog?</p>
</div>
<div id="comment-85750-info" class="comment-info">
<span class="comment-age">(28 Sep '22, 13:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84959-form-container" class="comment-form-container">
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

