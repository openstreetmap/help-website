+++
type = "question"
title = "App development using OpenStreetMap"
description = '''Hi Everyone, My name is Olivier Matthys. I&#x27;m sales and marketing executive for an IT company in Belgium and one of our specialties is mobile app development. i&#x27;ve been searching for some time now to find the right answer about the usages of Openstreetmap... but no succes so far :). One of our custom...'''
date = "2012-06-25T09:31:00Z"
lastmod = "2012-06-25T09:48:00Z"
weight = 13755
keywords = [ "mobile", "development", "app", "games", "application" ]
aliases = [ "/questions/13755" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [App development using OpenStreetMap](/questions/13755/app-development-using-openstreetmap)

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
<span id="post-13755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13755-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Everyone,</p>
<p>My name is Olivier Matthys. I'm sales and marketing executive for an IT company in Belgium and one of our specialties is mobile app development. i've been searching for some time now to find the right answer about the usages of Openstreetmap... but no succes so far :).</p>
<p>One of our customers came up with an idea and asked us if we could develop it.</p>
<p>De development shouldn't be a problem, but offcourse we have to be sure whether we can use Openstreetmap in the application.</p>
<p>The application would be a sort of a 'shooter game'(nothing spectacular :)) where people can see on the map where their opponents are (more like a paintball game but your smartphone, it also uses nicknames instead of real names etc for privacy reasons), and therefore we would like to use Openstreetmap. As our customer really wants to spread the game worldwide they decided to do the hosting thereselves. And ofcourse if the app would be a success, donations for the free use of Open street map would be no problem.</p>
<p>But my questions is simple: Can our developers use the API's etc and general use of Open street map for the game?</p>
<p>Thanks in advance and have a nice day!</p>
<p>Olivier Matthys</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-app" rel="tag" title="see questions tagged &#39;app&#39;">app</span> <span class="post-tag tag-link-games" rel="tag" title="see questions tagged &#39;games&#39;">games</span> <span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '12, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/b66a8590112a78e04fafc9ffd4724cef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Olivier%20Matthys&#39;s gravatar image" />
<p><span>Olivier Matthys</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Olivier Matthys has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13755" class="comments-container">
&#10;</div>
<div id="comment-tools-13755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13755-form-container" class="comment-form-container">
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

<span id="13756"></span>

<div id="answer-container-13756" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13756-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-13756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's probably some confusion of terms here. OpenStreetMap has an API but we call that the "editing API", it is for access to our raw data and it is unlikely that you want to use that in the game (and you wouldn't be allowed to).</p>
<p>What Google et al. call their "API", a collection of Javascript code that enables you to access their servers, doesn't exist in OSM. Instead, you would use third-party libraries like OpenLayers or Leaflet to display OSM maps in a browser, or other platform-specific libraries to display OSM data. These are not part of OSM but made by others; some are proprietary, some are open source.</p>
<p>You are always free to download our raw data in the form of our <a href="http://wiki.openatreetmap.org/wiki/Planet.osm">Planet file</a> or an extract thereof, and process it into a form that you can use for your game, and host the result yourself. For 2D maps people usually set up a tile server themselves and produce map tiles (PNG images) from the data; I don't know if your requirements for the game are different. The <a href="http://www.switch2osm.org/">http://www.switch2osm.org/</a> web site has some information about setting up tile servers, and also has pointers to businesses willing to help you with that if required.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '12, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13756" class="comments-container">
&#10;</div>
<div id="comment-tools-13756" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13756-form-container" class="comment-form-container">
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

