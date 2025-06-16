+++
type = "question"
title = "Tile server randomly &quot;freezes&quot; for about 10 minutes at a time"
description = '''Follow-up to my previous (bad) question. I managed to catch one of these freezes and monitor the syslog and server behavior. The &quot;freeze&quot; does not need a server restart. It would actually work itself out in about 5-10 minutes. First of all, this is what I see on the map that is using my tile server....'''
date = "2019-04-16T17:10:00Z"
lastmod = "2019-04-24T03:24:00Z"
weight = 68818
keywords = [ "tiles", "renderd", "tileserver" ]
aliases = [ "/questions/68818" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tile server randomly "freezes" for about 10 minutes at a time](/questions/68818/tile-server-randomly-freezes-for-about-10-minutes-at-a-time)

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
<span id="post-68818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68818-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Follow-up to my <a href="/questions/68666/tile-server-randomly-freezes-requiring-a-server-restart">previous (bad) question</a>. I managed to catch one of these freezes and monitor the <code>syslog</code> and server behavior. The "freeze" does not need a server restart. It would actually work itself out in about 5-10 minutes.</p>
<p>First of all, this is <a href="https://i.gyazo.com/9940234404a03e005218db28df6e95b6.png">what I see on the map</a> that is using my tile server. Requests for (pre-rendered) tiles are all stuck.</p>
<p>Here's what my <a href="https://i.gyazo.com/6a22f60b6ba19583162f2f750be4d6f1.png">VPS monitoring looks like</a>. Look at the bottom chart "Bandwidth Public". As you can see, the server is operating normally and suddenly has a huge drop in outbound bandwidth, which means the server stopped serving tiles. All other system stats look normal.</p>
<p>Looking at the syslog, here is the section of output code during the freeze. The freeze began at around 15:33 and ended about 10 minutes later. The anomaly code is at 15:37, where there were a bunch of outputs like <code>Created slice User Slice of root</code> and <code>Reached target Sockets</code>. However the freeze began at 15:33, so 4 minutes before the weird output began.</p>
<p>During the freeze, there was a 1 minute period at 15:39 when it successfully served some tiles, before freezing up for another 3-4 minutes. After 15:44, the tile server went back to normal.</p>
<pre><code>Apr 16 15:33:49 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36325), y(47623), mime(image/png), options()
Apr 16 15:33:49 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:33:51 tilerserver2 renderd[2542]: DEBUG: DONE TILE ajt 17 36320-36327 47616-47623 in 2.639 seconds
Apr 16 15:35:01 tilerserver2 CRON[26475]: (root) CMD (command -v debian-sa1 &gt; /dev/null &amp;&amp; debian-sa1 1 1)
Apr 16 15:35:01 tilerserver2 CRON[26477]: (root) CMD (if [ -x /etc/munin/plugins/apt_all ]; then /etc/munin/plugins/apt_all update 7200 12 &gt;/dev/null; elif [ -x /etc/munin/plugins/apt ]; then /etc/munin/plugins/apt update 7200 12 &gt;/dev/null; fi)
Apr 16 15:35:01 tilerserver2 CRON[26478]: (munin) CMD (if [ -x /usr/bin/munin-cron ]; then /usr/bin/munin-cron; fi)
Apr 16 15:37:56 tilerserver2 systemd[1]: Created slice User Slice of root.
Apr 16 15:37:56 tilerserver2 systemd[1]: Starting User Manager for UID 0...
Apr 16 15:37:56 tilerserver2 systemd[1]: Started Session 2590 of user root.
Apr 16 15:37:56 tilerserver2 systemd[26804]: Reached target Sockets.
Apr 16 15:37:56 tilerserver2 systemd[26804]: Reached target Timers.
Apr 16 15:37:56 tilerserver2 systemd[26804]: Reached target Paths.
Apr 16 15:37:56 tilerserver2 systemd[26804]: Reached target Basic System.
Apr 16 15:37:56 tilerserver2 systemd[26804]: Reached target Default.
Apr 16 15:37:56 tilerserver2 systemd[26804]: Startup finished in 30ms.
Apr 16 15:37:56 tilerserver2 systemd[1]: Started User Manager for UID 0.
Apr 16 15:38:22 tilerserver2 systemd[1]: Started Session 2591 of user root.
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36576), y(47867), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: START TILE ajt 17 36576-36583 47864-47871, age 3.02 days
Apr 16 15:39:09 tilerserver2 renderd[2542]: Rendering projected coordinates 17 36576 47864 -&gt; -8854465.356560|5400734.670520 -8852019.371654|5403180.655425 to a 8 x 8 tile
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36576), y(47866), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36577), y(47866), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36576), y(47865), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 13, number 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36577), y(47868), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 1 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(13) xml(ajt), z(17), x(36577), y(47865), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 13 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36576), y(47868), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36578), y(47865), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36578), y(47867), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36578), y(47866), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36577), y(47867), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36578), y(47868), mime(image/png), options()
Apr 16 15:39:09 tilerserver2 renderd[2542]: DEBUG: Connection 0, fd 12 closed, now 0 left
Apr 16 15:39:13 tilerserver2 renderd[2542]: DEBUG: DONE TILE ajt 17 36576-36583 47864-47871 in 3.652 seconds
Apr 16 15:40:01 tilerserver2 CRON[26922]: (root) CMD (if [ -x /etc/munin/plugins/apt_all ]; then /etc/munin/plugins/apt_all update 7200 12 &gt;/dev/null; elif [ -x /etc/munin/plugins/apt ]; then /etc/munin/plugins/apt update 7200 12 &gt;/dev/null; fi)
Apr 16 15:40:01 tilerserver2 CRON[26923]: (munin) CMD (if [ -x /usr/bin/munin-cron ]; then /usr/bin/munin-cron; fi)
Apr 16 15:40:34 tilerserver2 systemd[1]: Started Session 2594 of user root.
Apr 16 15:43:45 tilerserver2 systemd[1]: Started Session 2595 of user root.
Apr 16 15:44:08 tilerserver2 renderd[2542]: DEBUG: Got incoming connection, fd 12, number 1
Apr 16 15:44:08 tilerserver2 renderd[2542]: DEBUG: Got incoming request with protocol version 2
Apr 16 15:44:08 tilerserver2 renderd[2542]: DEBUG: Got command RenderLow fd(12) xml(ajt), z(17), x(36536), y(47857), mime(image/png), options()</code></pre>
<p>Apache2 <code>access.log</code> during a freeze. There is a gap between 14:01 and 14:06 when server is not taking any requests (the freeze).</p>
<pre><code>69.158.20.237 - - [23/Apr/2019:14:01:17 +0000] &quot;GET /hot/17/36646/47835.png HTTP/1.1&quot; 200 18392 &quot;https://www.mysite.ca/map/43.651611&amp;-79.360015&amp;17&quot; &quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36&quot;
69.158.20.237 - - [23/Apr/2019:14:01:17 +0000] &quot;GET /hot/17/36646/47833.png HTTP/1.1&quot; 200 17406 &quot;https://www.mysite.ca/map/43.651611&amp;-79.360015&amp;17&quot; &quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36&quot;
69.158.20.237 - - [23/Apr/2019:14:01:17 +0000] &quot;GET /hot/17/36646/47836.png HTTP/1.1&quot; 200 30092 &quot;https://www.mysite.ca/map/43.651611&amp;-79.360015&amp;17&quot; &quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36&quot;
184.175.22.23 - - [23/Apr/2019:14:01:18 +0000] &quot;GET /hot/14/4572/5978.png HTTP/1.1&quot; 200 73673 &quot;https://www.mysite.ca/map/43.658775&amp;-79.464724&amp;13&quot; &quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36&quot;
69.158.20.237 - - [23/Apr/2019:14:01:18 +0000] &quot;GET /hot/17/36647/47835.png HTTP/1.1&quot; 200 16931 &quot;https://www.mysite.ca/map/43.653908&amp;-79.353299&amp;17&quot; &quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36&quot;
72.139.207.185 - - [23/Apr/2019:14:06:14 +0000] &quot;GET /hot/14/4560/5972.png HTTP/1.1&quot; 200 31375 &quot;https://www.mysite.ca/map/43.741305&amp;-79.805202&amp;14&quot; &quot;Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36&quot;
72.139.207.185 - - [23/Apr/2019:14:06:14 +0000] &quot;GET /hot/14/4561/5972.png HTTP/1.1&quot; 200 49864 &quot;https://www.mysite.ca/map/43.741305&amp;-79.805202&amp;14&quot; &quot;Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36&quot;
72.139.207.185 - - [23/Apr/2019:14:06:14 +0000] &quot;GET /hot/14/4557/5972.png HTTP/1.1&quot; 200 17749 &quot;https://www.mysite.ca/map/43.741305&amp;-79.805202&amp;14&quot; &quot;Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36&quot;
184.175.22.23 - - [23/Apr/2019:14:06:14 +0000] &quot;GET /hot/13/2284/2990.png HTTP/1.1&quot; 200 88895 &quot;https://www.mysite.ca/map/43.666105&amp;-79.444001&amp;14&quot; &quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36&quot;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '19, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/b1e3fbb6f31c5e0144e7b18fcd7d5d33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valachio&#39;s gravatar image" />
<p><span>valachio</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valachio has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Apr '19, 16:52</strong> </span></p>
</div>
</div>
<div id="comments-container-68818" class="comments-container">
&#10;</div>
<div id="comment-tools-68818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68818-form-container" class="comment-form-container">
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

<span id="68821"></span>

<div id="answer-container-68821" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68821-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe have a look to the load at that moment. I see you have munin running, what do munin graphs look like?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '19, 05:58</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-68821" class="comments-container">
<span id="68893"></span>
<div id="comment-68893" class="comment">
<div id="post-68893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <a href="https://i.gyazo.com/6a22f60b6ba19583162f2f750be4d6f1.png">system load at the moment is normal</a>. See the bottom chart (Bandwidth Public). The dip on the right is when the freeze happened. All other system stats look normal, apart from a very small spike in CPU.</p>
<p>I looked through the munin logs. Is there a particular one I should look at? There are <code>munin-graph</code>, <code>munin-update</code>, <code>munin-limits</code>, <code>munin-html</code>, <code>munin-node</code>. I looked through all of them. I tried to compare the munin logs when during a freeze, and when the tile server was serving normally, I couldn't see a difference in the logs.</p>
</div>
<div id="comment-68893-info" class="comment-info">
<span class="comment-age">(23 Apr '19, 15:48)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
</div>
<div id="comment-tools-68821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68821-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68844"></span>

<div id="answer-container-68844" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68844-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>During the freeze, there was a 1 minute period at 15:39 when it successfully served some tiles, before freezing up for another 3-4 minutes. After 15:44, the tile server went back to normal.</code></pre>
<p>Looking at the log, it was serving tiles OK to 15:39 and no requests pending at 15:39, so it's not surprising that things went quiet until 15:44. IF you were trying to send requests in in that time they weren't reaching apache (or at least not mod_tile).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '19, 01:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-68844" class="comments-container">
<span id="68892"></span>
<div id="comment-68892" class="comment">
<div id="post-68892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for delayed response.</p>
<p>The website is always serving ~100 users at any point of time, so there is a constant stream of requests coming in. I was trying to use the website myself at the time and map tiles were not loading.</p>
<p>If the requests were not reaching Apache/mod_tile at that time, any idea why not? Did Apache freeze? Did mod_tile freeze? Why does the issue resolve itself in 10 minutes?</p>
</div>
<div id="comment-68892-info" class="comment-info">
<span class="comment-age">(23 Apr '19, 15:40)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
<span id="68894"></span>
<div id="comment-68894" class="comment">
<div id="post-68894-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I found something. I looked through Apache2's <code>access.log</code>. During the freeze, <code>access.log</code> showed no requests during the freeze. On average there should be about 10 requests per second.</p>
<p>So it would seem that the requests are not reaching Apache...</p>
<p>Apache's <code>error.log</code> showed no errors during the freeze</p>
</div>
<div id="comment-68894-info" class="comment-info">
<span class="comment-age">(23 Apr '19, 16:18)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
<span id="68896"></span>
<div id="comment-68896" class="comment">
<div id="post-68896-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Then maybe the requests did not reach the server at all: network issue?</p>
</div>
<div id="comment-68896-info" class="comment-info">
<span class="comment-age">(23 Apr '19, 20:51)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
<span id="68898"></span>
<div id="comment-68898" class="comment">
<div id="post-68898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(at the risk of stating the bleeding obvious) perhaps you could script some web page accesses locally to show up periodically in apache's access log to see if they stop when the server "freezes". If they don't, it's an external network issue.</p>
</div>
<div id="comment-68898-info" class="comment-info">
<span class="comment-age">(23 Apr '19, 21:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="68903"></span>
<div id="comment-68903" class="comment">
<div id="post-68903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5587/yvecai">@yvecai</a> The server is running fine during the freeze. But it does seem any tile requests are being ignored by Apache for some reason... What is causing Apache to ignore tile requests for 5 minutes at a time, randomly?</p>
</div>
<div id="comment-68903-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 03:24)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
</div>
<div id="comment-tools-68844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68844-form-container" class="comment-form-container">
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

