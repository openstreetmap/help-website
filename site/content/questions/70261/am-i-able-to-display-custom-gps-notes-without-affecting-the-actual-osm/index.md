+++
type = "question"
title = "Am I able to display custom gps notes without affecting the actual OSM?"
description = '''I am a new user, I am working on a project for a local group of pokemon go players, We have a telegram group to coordinates raids, and report new nest changes. I am working on a telegram bot in python to maintain the new nest rotation map, so there&#x27;s less maintenance for admins. We have it setup whe...'''
date = "2019-07-31T20:58:00Z"
lastmod = "2019-08-01T08:12:00Z"
weight = 70261
keywords = [ "openstreetmap", "editing", "question" ]
aliases = [ "/questions/70261" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Am I able to display custom gps notes without affecting the actual OSM?](/questions/70261/am-i-able-to-display-custom-gps-notes-without-affecting-the-actual-osm)

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
<span id="post-70261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70261-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am a new user, I am working on a project for a local group of pokemon go players, We have a telegram group to coordinates raids, and report new nest changes. I am working on a telegram bot in python to maintain the new nest rotation map, so there's less maintenance for admins. We have it setup where the gps markers on google maps are the icons of pokemon, I would like to replicate that using openstreetmaps, but from what I understand any changes I make are actual edits to the map. I do not want to do that for this project. I did some googling and I came across about private layers, and another one was geojson, but I am not sure if that is what I need for my project, and would like to know what my other options are. Any help would be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '19, 20:58</strong></p>
<img src="https://secure.gravatar.com/avatar/b4a1028edd057cf98a6b33dbee2bc5e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andyroo89&#39;s gravatar image" />
<p><span>Andyroo89</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andyroo89 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70261" class="comments-container">
&#10;</div>
<div id="comment-tools-70261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70261-form-container" class="comment-form-container">
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

<span id="70264"></span>

<div id="answer-container-70264" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70264-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You want to display points on top of an OSM map and periodically change them? You can do that with <a href="https://wiki.openstreetmap.org/wiki/UMap">uMap</a> for example. Or you set something up on your server with the help of <a href="https://leafletjs.com/">Leaflet</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '19, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-70264" class="comments-container">
<span id="70267"></span>
<div id="comment-70267" class="comment">
<div id="post-70267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh that might work out, So the difference between leaflet and uMap is that I can do this on osm servers, while leaflet lets me host it myself, and still do what I want?</p>
</div>
<div id="comment-70267-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 22:16)</span> <span class="comment-user userinfo">Andyroo89</span>
</div>
</div>
<span id="70274"></span>
<div id="comment-70274" class="comment">
<div id="post-70274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, there are more differences.</p>
<p>Leaflet is a framework and many contributors have provided plugins to allow many different features to be added. With the Leaflet base you allow for serving maps, with different plugins you can then customize the map controls, display markers, allow for interactions, etc. You are very flexible but have to configure your Leaflet yourself.</p>
<p>uMap has a nice UI which allows for easy access and modifying by either the creator only or also other editors. You can install your own uMap on your server or use one of the existing public services. uMap is quite powerful but limited to what is provided.</p>
</div>
<div id="comment-70274-info" class="comment-info">
<span class="comment-age">(01 Aug '19, 08:12)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-70264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70264-form-container" class="comment-form-container">
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

