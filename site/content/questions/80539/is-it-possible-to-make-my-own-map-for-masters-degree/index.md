+++
type = "question"
title = "Is it possible to make my own map for master&#x27;s degree?"
description = '''Hi, I&#x27;m doing my master&#x27;s degree project and on this part I want to make a map using OSM where I want to display some points which represent the possition (Lat and Long) of some buses. I already have done it making my own local server with rendered map from OSM and displaying those points using java...'''
date = "2021-06-12T14:57:00Z"
lastmod = "2021-06-20T13:31:00Z"
weight = 80539
keywords = [ "project", "josm", "newbie", "osm2pgsql" ]
aliases = [ "/questions/80539" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to make my own map for master's degree?](/questions/80539/is-it-possible-to-make-my-own-map-for-masters-degree)

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
<span id="post-80539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80539-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm doing my master's degree project and on this part I want to make a map using OSM where I want to display some points which represent the possition (Lat and Long) of some buses. I already have done it making my own local server with rendered map from OSM and displaying those points using javascript over my html index of my tile. But my idea is to store data from my OCB into the OSM database (my own database to dont "break" OSM database) and be able to display those points as they were points of interest on the map like monuments, gas stations, etc). As summary of end application, is to see where those points (buses) are when I "refresh" the page to load the map.</p>
<p>I'm not sure if here is the correct place to ask for this or even if it is possible to do, but I'm new using OSM so I have to ask :)</p>
<p>Thanks in advance for your answers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-project" rel="tag" title="see questions tagged &#39;project&#39;">project</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '21, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/54b2d4cc7c0a519a1bc849428f3c166f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adriano&#39;s gravatar image" />
<p><span>Adriano</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adriano has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80539" class="comments-container">
&#10;</div>
<div id="comment-tools-80539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80539-form-container" class="comment-form-container">
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

<span id="80557"></span>

<div id="answer-container-80557" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80557-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>I'm not sure if I correctly understand your project.</p>
<p>But if you want to display dynamic data, you don't want to embed it in raster tiles. Keep it above, tweak your javascript so that it blends nicely. If you use leaflet, have a look at this <a href="https://leafletjs.com/examples/custom-icons/">page</a> to design your own marker. A small one without shadow could probably pass for a feature of the basemap.</p>
<p>Raster tile generators are optimized for more or less static data, with cache and stuff, so clients will reload the same tiles. Also the OSM database and surrounding tools are not meant for dynamic data, you will be on your own I'm afraid. Last hitch, I think, generating tiles is expensive, you don't want to do it all the time of your thesis...</p>
<p>Or you go for vector tiles, but it's a brand new world ! ;-)</p>
<p>If you want a top level example, have a look at <a href="https://github.com/nagix/mini-tokyo-3d">mini-tokyo-3d</a>, it's amazing (and open source).</p>
<p>Best regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '21, 20:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80557" class="comments-container">
<span id="80636"></span>
<div id="comment-80636" class="comment">
<div id="post-80636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank for your answer mate. Yes, all the info I have checked says the same about dynamic representation so I'll check other options</p>
</div>
<div id="comment-80636-info" class="comment-info">
<span class="comment-age">(20 Jun '21, 13:31)</span> <span class="comment-user userinfo">Adriano</span>
</div>
</div>
</div>
<div id="comment-tools-80557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80557-form-container" class="comment-form-container">
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

