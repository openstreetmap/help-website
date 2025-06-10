+++
type = "question"
title = "Rendered Command Execution time"
description = '''I executed command &quot;renderd -f -c /usr/local/etc/renderd.conf&quot;. I want to know how much time will it take to completely load India map tiles on local.'''
date = "2019-06-06T06:59:00Z"
lastmod = "2019-06-06T14:34:00Z"
weight = 69483
keywords = [ "execution_time", "rendered" ]
aliases = [ "/questions/69483" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rendered Command Execution time](/questions/69483/rendered-command-execution-time)

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
<span id="post-69483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69483-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I executed command "renderd -f -c /usr/local/etc/renderd.conf". I want to know how much time will it take to completely load India map tiles on local.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-execution_time" rel="tag" title="see questions tagged &#39;execution_time&#39;">execution_time</span> <span class="post-tag tag-link-rendered" rel="tag" title="see questions tagged &#39;rendered&#39;">rendered</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '19, 06:59</strong></p>
<img src="https://secure.gravatar.com/avatar/8310002871cb38b24453e184d4afa3d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Puranjay&#39;s gravatar image" />
<p><span>Puranjay</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Puranjay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69483" class="comments-container">
<span id="69484"></span>
<div id="comment-69484" class="comment">
<div id="post-69484-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I assume this largely depend on CPU, memory, disk speed. Since you provide none of those parameters, I would expect it will be hard to answer your questions.</p>
</div>
<div id="comment-69484-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 10:02)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="69489"></span>
<div id="comment-69489" class="comment">
<div id="post-69489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But when I was following the wiki docs there was no command to provide the CPU parameters. It was asked only in osm2pgsql command.</p>
</div>
<div id="comment-69489-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 10:53)</span> <span class="comment-user userinfo">Puranjay</span>
</div>
</div>
<span id="69491"></span>
<div id="comment-69491" class="comment">
<div id="post-69491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm guessing you've followed <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> and got as far as "Running renderd for the first time"?</p>
</div>
<div id="comment-69491-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 11:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69493"></span>
<div id="comment-69493" class="comment">
<div id="post-69493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, exactly. But I want to know how much time will it take for execution of this command.</p>
</div>
<div id="comment-69493-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 11:30)</span> <span class="comment-user userinfo">Puranjay</span>
</div>
</div>
<span id="69494"></span>
<div id="comment-69494" class="comment">
<div id="post-69494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am getting "debug: Creating and writing a metatile to /var/lib/mod_tile/ajt/0/0/0/0/0/0.meta" in console.</p>
</div>
<div id="comment-69494-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 11:31)</span> <span class="comment-user userinfo">Puranjay</span>
</div>
</div>
<span id="69495"></span>
<div id="comment-69495" class="comment not_top_scorer">
<div id="post-69495-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Strictly speaking, "renderd -f -c /usr/local/etc/renderd.conf" will never "finish executing" because it's a server that sits there until you tell it to stop (when running interactively like this, usually by pressing ^c).</p>
</div>
<div id="comment-69495-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 11:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69483" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-69483-form-container" class="comment-form-container">
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

<span id="69485"></span>

<div id="answer-container-69485" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69485-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After you've done that, renderd will just sit there waiting for connections. When you request a local tile, you'll see "START TILE" and "END TILE" in the output. The second line tells you how long it took to do that tile. Tiles at different zoom levels will take different amounts of time to render.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '19, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-69485" class="comments-container">
<span id="69488"></span>
<div id="comment-69488" class="comment">
<div id="post-69488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will se "Start tile" and "End Tile" after execution of this command..Am I right?</p>
</div>
<div id="comment-69488-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 10:52)</span> <span class="comment-user userinfo">Puranjay</span>
</div>
</div>
<span id="69490"></span>
<div id="comment-69490" class="comment">
<div id="post-69490-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here's an example from a <a href="https://map.atownsend.org.uk/maps/map/map.html">server</a> of mine . I zoomed in so that the web browser asked for some tiles, and the results (in my case from syslog as that's where renderd output is going) are as follows:</p>
<pre><code>renderaccount@map:~$ sudo tail -f /var/log/syslog | grep &quot; TILE &quot;
[sudo] password for ajtown:
Jun  6 12:04:44 map renderd[1727]: DEBUG: START TILE ajt 13 4072-4079 2632-2639, age 10000.12 days
Jun  6 12:04:44 map renderd[1727]: DEBUG: START TILE ajt 13 4064-4071 2632-2639, age 10000.12 days
Jun  6 12:04:49 map renderd[1727]: DEBUG: DONE TILE ajt 13 4072-4079 2632-2639 in 5.013 seconds
Jun  6 12:04:50 map renderd[1727]: DEBUG: DONE TILE ajt 13 4064-4071 2632-2639 in 5.491 seconds</code></pre>
<p>So rerendering those two tiles at zoom 13 took 5 seconds each.</p>
</div>
<div id="comment-69490-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 11:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69496"></span>
<div id="comment-69496" class="comment">
<div id="post-69496-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I will run this command before "renderd -f -c /usr/local/etc/renderd.conf" it won't show anything because tiles are still being loaded.</p>
</div>
<div id="comment-69496-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 11:50)</span> <span class="comment-user userinfo">Puranjay</span>
</div>
</div>
<span id="69497"></span>
<div id="comment-69497" class="comment">
<div id="post-69497-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't understand that last comment?</p>
</div>
<div id="comment-69497-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 11:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69498"></span>
<div id="comment-69498" class="comment">
<div id="post-69498-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Puranjay, I have the feeling you are under the misconception that renderd is loading all the possible tiles from somewhere in one go. Instead it is sort of a server that renders (builds) a tile at at time from the data file on request as soon as it is asked to supply one to e.g. a web server. (I hope I explained that right, I am by no means an expert on this)</p>
</div>
<div id="comment-69498-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 12:55)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="69499"></span>
<div id="comment-69499" class="comment not_top_scorer">
<div id="post-69499-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I was thinking that rendered is loading all the tiles. So what command should be used for viewing the tiles?</p>
</div>
<div id="comment-69499-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 13:25)</span> <span class="comment-user userinfo">Puranjay</span>
</div>
</div>
<span id="69500"></span>
<div id="comment-69500" class="comment not_top_scorer">
<div id="post-69500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Point a web browser at the web server that has mod_tile installed, which passes the tile render request to renderd.</p>
<p>The relevant line in the switch2osm guide is the one that says "Point a web browser at: <a href="http://yourserveripaddress/hot/0/0/0.png">http://yourserveripaddress/hot/0/0/0.png".</a></p>
</div>
<div id="comment-69500-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 13:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69501"></span>
<div id="comment-69501" class="comment not_top_scorer">
<div id="post-69501-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok got it. Where can I change the zoom level for tile?</p>
</div>
<div id="comment-69501-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 13:37)</span> <span class="comment-user userinfo">Puranjay</span>
</div>
</div>
<span id="69502"></span>
<div id="comment-69502" class="comment not_top_scorer">
<div id="post-69502-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the web browser. <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> suggests "In order to see tiles, we’ll cheat and use an html file “sample_leaflet.html” in mod_tile’s “extras” folder".</p>
</div>
<div id="comment-69502-info" class="comment-info">
<span class="comment-age">(06 Jun '19, 14:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69485" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-69485-form-container" class="comment-form-container">
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

