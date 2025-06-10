+++
type = "question"
title = "Own OSM tile server not rendering Tiles"
description = '''A few days ago, I have mounted my own Tile server and I have used it for one week without problems, now I get the message 404 (Not Found) when Im navigating to parts of the world I did not navigate for the past week. Meaning, all Tiles that I had seen when everything was working OK, I can see them n...'''
date = "2019-02-05T16:46:00Z"
lastmod = "2019-02-05T19:18:00Z"
weight = 67884
keywords = [ "rendering", "tileserver" ]
aliases = [ "/questions/67884" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Own OSM tile server not rendering Tiles](/questions/67884/own-osm-tile-server-not-rendering-tiles)

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
<span id="post-67884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67884-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A few days ago, I have mounted my own Tile server and I have used it for one week without problems, now I get the message 404 (Not Found) when Im navigating to parts of the world I did not navigate for the past week. Meaning, all Tiles that I had seen when everything was working OK, I can see them now allright, (seems like they are somehow cached?), but the parts of the map I did not navigate or Zoomed in when everything was working allright, throws that error and does not return any Tile.</p>
<p>Is there a way to know that my server is working OK?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '19, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9ae0c5f5d68d1969f28ebdc5a89d18a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leo_1991&#39;s gravatar image" />
<p><span>Leo_1991</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leo_1991 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '19, 16:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span></p>
</div>
</div>
<div id="comments-container-67884" class="comments-container">
<span id="67885"></span>
<div id="comment-67885" class="comment">
<div id="post-67885-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What software are you using to render the tiles?</p>
</div>
<div id="comment-67885-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 16:47)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="67886"></span>
<div id="comment-67886" class="comment">
<div id="post-67886-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>According to this guide: <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a></p>
<p>Its called "Renderd"</p>
</div>
<div id="comment-67886-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 17:01)</span> <span class="comment-user userinfo">Leo_1991</span>
</div>
</div>
<span id="67887"></span>
<div id="comment-67887" class="comment">
<div id="post-67887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you try and request tiles, what is written to "/var/log/syslog"?</p>
</div>
<div id="comment-67887-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 17:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67888"></span>
<div id="comment-67888" class="comment">
<div id="post-67888-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Got this when panning a little to the left in the map. Not sure what it really means tough :/</p>
<p>Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Got incoming request with protocol version 2 Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Sending render cmd(4 ajt 13/2710/4968) with protocol version 2 to fd 9 Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Sending render cmd(4 ajt 13/2710/4967) with protocol version 2 to fd 10 Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Got command RenderPrio fd(7) xml(ajt), z(13), x(2712), y(4969), mime(image/png), options() Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Connection 0, fd 8 closed, now 3 left Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Connection 0, fd 9 closed, now 2 left Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Connection 0, fd 10 closed, now 1 left</p>
</div>
<div id="comment-67888-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 17:48)</span> <span class="comment-user userinfo">Leo_1991</span>
</div>
</div>
<span id="67889"></span>
<div id="comment-67889" class="comment not_top_scorer">
<div id="post-67889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Got incoming connection, fd 7, number 1 Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Got incoming connection, fd 8, number 2 Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Got incoming request with protocol version 2 Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Got command RenderPrio fd(7) xml(ajt), z(13), x(2710), y(4969), mime(image/png), options() Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Got incoming connection, fd 9, number 3 Feb 5 14:46:23 UBUNTU-PC renderd[1891]: Received request for map layer 'ajt' which failed to load Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Got incoming request with protocol version 2 Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Sending render cmd(4 ajt 13/2710/4969) with protocol version 2 to fd 7 Feb 5 14:46:23 UBUNTU-PC renderd[1891]: DEBUG: Got command RenderPrio fd(8) xml(ajt), z(13), x(2711), y(4969), mime(image/png), options()</p>
</div>
<div id="comment-67889-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 17:50)</span> <span class="comment-user userinfo">Leo_1991</span>
</div>
</div>
<span id="67890"></span>
<div id="comment-67890" class="comment not_top_scorer">
<div id="post-67890-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can see a " Received request for map layer 'ajt' which failed to load", Is that ok? :s</p>
</div>
<div id="comment-67890-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 17:51)</span> <span class="comment-user userinfo">Leo_1991</span>
</div>
</div>
<span id="67891"></span>
<div id="comment-67891" class="comment">
<div id="post-67891-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"Received request for map layer 'ajt' which failed to load" is not OK. If you do a "sudo /etc/init.d/renderd reload" it'll write why that map layer failed to load to "/var/log/syslog".</p>
</div>
<div id="comment-67891-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 17:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67892"></span>
<div id="comment-67892" class="comment not_top_scorer">
<div id="post-67892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Allright! I did a sudo /etc/init.d/renderd reload Then what was being written to syslog did not show any error, it started as normal.. Then I did sudo /etc/init.d/renderd reload but said service was not initiated... And then I did a sudo /etc/init.d/renderd start Then I went to my map and now everything renders perfectly! SomeoneElse you are the Boss! :D :D</p>
<p>Tough I dont know why it has stopped in the first place, I can keep working now :), Thank you very much!!</p>
</div>
<div id="comment-67892-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 18:12)</span> <span class="comment-user userinfo">Leo_1991</span>
</div>
</div>
<span id="67893"></span>
<div id="comment-67893" class="comment not_top_scorer">
<div id="post-67893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Though I dont know why it has stopped in the first place,</p>
</blockquote>
<p>... well that will be in "syslog" somewhere - just search from somewhere where tiles were loading for the first "failed to load" and see what else was happening then. It could be one of a number of things, such as out of memory.</p>
</div>
<div id="comment-67893-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 18:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67894"></span>
<div id="comment-67894" class="comment not_top_scorer">
<div id="post-67894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Allright, I will look into it!</p>
</div>
<div id="comment-67894-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 19:16)</span> <span class="comment-user userinfo">Leo_1991</span>
</div>
</div>
</div>
<div id="comment-tools-67884" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-67884-form-container" class="comment-form-container">
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

<span id="67895"></span>

<div id="answer-container-67895" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67895-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to <a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneElse</a> comment, I can see how was renderd working via "$ cat /var/log/syslog".</p>
<p>To make the service work again I did a "sudo /etc/init.d/renderd reload", and then a sudo /etc/init.d/renderd.</p>
<p>Everything is working fine now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '19, 19:18</strong></p>
<img src="https://secure.gravatar.com/avatar/9ae0c5f5d68d1969f28ebdc5a89d18a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leo_1991&#39;s gravatar image" />
<p><span>Leo_1991</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leo_1991 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67895" class="comments-container">
&#10;</div>
<div id="comment-tools-67895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67895-form-container" class="comment-form-container">
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

