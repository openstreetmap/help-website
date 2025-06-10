+++
type = "question"
title = "404 not rendering after some time running fine"
description = '''I&#x27;ve been using open street maps for a while on our own server. The installation guides have been very easy to follow and generally the system has been working really well. We recently (~2-3 months ago) upgraded with a fresh install to update our maps and update the server to Ubuntu 20.04 using inst...'''
date = "2021-05-06T00:01:00Z"
lastmod = "2021-05-06T00:01:00Z"
weight = 80016
keywords = [ "rendering" ]
aliases = [ "/questions/80016" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [404 not rendering after some time running fine](/questions/80016/404-not-rendering-after-some-time-running-fine)

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
<span id="post-80016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80016-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been using open street maps for a while on our own server. The installation guides have been very easy to follow and generally the system has been working really well. We recently (~2-3 months ago) upgraded with a fresh install to update our maps and update the server to Ubuntu 20.04 using instructions here:</p>
<p><a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a></p>
<p>As usual the installation was easy and the system was up and running importing data (dedicated Ec2 instance). After the import the system seemed to be working well.</p>
<p>However about every 6-12 hours we find that something in the system causes the tile rendering to start to fail, resulting in 404's on the calls to the tiles that haven't been rendered before.</p>
<p>The previous version we were running (about 18-24 months old) had this issue occasionally, we found by restarting the process roughly daily, the problem was never an issue. However in this latest installation, the restart of apache and rendered doesn't recover the process of tile rendering.</p>
<p>In the logs I can see lines like this</p>
<pre><code>May  5 22:35:21 renderd[39527]: DEBUG: Connection 1, fd 37 closed, now 2 left
May  5 22:35:21 DEBUG: Got incoming request with protocol version 2
May  5 22:34:26 renderd[39527]: DEBUG: Got command Dirty fd(36) xml(ajt), z(18), x(241694), y(151967), mime(image/png), options()
May  5 22:34:26 renderd[39527]: DEBUG: Sending NotDone response(4)</code></pre>
<p>I haven't had much luck finding logs that provide a clear error. The only thing that seems to help is to restart the whole server, after which it redneres fine for another 6-12 hours before failing again.</p>
<p>So 2 questions:</p>
<ul>
<li>How can I find logs that indicate what's wrong to try and resolve this issue?</li>
<li>How should I 'restart' the render process to ensure it starts working again (restarting the whole server should be unnecessary)</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '21, 00:01</strong></p>
<img src="https://secure.gravatar.com/avatar/143bcc0d47dc0d07f9abb1333f8011fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brian%20WM&#39;s gravatar image" />
<p><span>Brian WM</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brian WM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80016" class="comments-container">
&#10;</div>
<div id="comment-tools-80016" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80016-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

