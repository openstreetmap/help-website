+++
type = "question"
title = "Building a tile server"
description = '''Hi forum, I tried to follow the interesting tutorial (  switch2osm.org/manually-building-a-tile-server-16-04-2-lts) for building an independent tile server for Ubuntu 16.04. I started with a new Ubuntu server in a virtualbox machine.  Unfortunately it does not work and I can not understand why.  On ...'''
date = "2018-04-11T09:22:00Z"
lastmod = "2018-04-14T06:44:00Z"
weight = 62975
keywords = [ "tileserver" ]
aliases = [ "/questions/62975" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Building a tile server](/questions/62975/building-a-tile-server)

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
<span id="post-62975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62975-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi forum,</p>
<p>I tried to follow the interesting tutorial ( <a href="http://switch2osm.org/manually-building-a-tile-server-16-04-2-lts">switch2osm.org/manually-building-a-tile-server-16-04-2-lts</a>) for building an independent tile server for Ubuntu 16.04.</p>
<p>I started with a new Ubuntu server in a virtualbox machine. Unfortunately it does not work and I can not understand why.</p>
<p>On the browser <code>the requested URL /hot/0/0/0.png was not found on this server (err 404)</code>. On the server side, we can read <code>Received request for map mayer 'ajt' which failed to load</code>.</p>
<p>When I launch the renderd, an error occurs which is</p>
<pre><code>&quot;An error occured while loading the map layer &#39;ajt&#39; : Postgis Plugin : ERROR relation     &quot;planet_osm_polygon&quot; does not exist.</code></pre>
<p>I had to make a mistake somewhere.</p>
<p>Does anyone have a suggestion to help me ?</p>
<p>Thanks a lot &amp; sorry for that newbie issue.</p>
<p>Sincerely,</p>
<p>David.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '18, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/25014ac16171dd1384ecebfd57764e18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="draimond&#39;s gravatar image" />
<p><span>draimond</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="draimond has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '18, 00:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span></p>
</div>
</div>
<div id="comments-container-62975" class="comments-container">
<span id="62976"></span>
<div id="comment-62976" class="comment">
<div id="post-62976-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd suggest that you restart "renderd" and post the errors that you see there in a github gist or similar, and then post a link to that here.</p>
</div>
<div id="comment-62976-info" class="comment-info">
<span class="comment-age">(11 Apr '18, 11:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62975-form-container" class="comment-form-container">
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

<span id="62986"></span>

<div id="answer-container-62986" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62986-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-62986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If "planet_osm_polygon" does not exist, then something has gone wrong at the osm2pgsql step.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '18, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-62986" class="comments-container">
<span id="62992"></span>
<div id="comment-62992" class="comment">
<div id="post-62992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Thanks a lot. You are right. I had a problem at this stage. I did the whole procedure again and it works now. Regards. David.</p>
</div>
<div id="comment-62992-info" class="comment-info">
<span class="comment-age">(14 Apr '18, 06:44)</span> <span class="comment-user userinfo">draimond</span>
</div>
</div>
</div>
<div id="comment-tools-62986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62986-form-container" class="comment-form-container">
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

