+++
type = "question"
title = "Using map of my city on offline Intranet"
description = '''Hi, I need to share a map of my city on our Intranet, we don&#x27;t have Internet connexion on it. We need more than a picture of the map, we need to search street name. I know how to export data from OpenStreetMap but I don&#x27;t know how put it on my web server (IIS). Thanks for your help. Bests regards. P...'''
date = "2013-03-29T09:27:00Z"
lastmod = "2013-03-29T10:13:00Z"
weight = 21059
keywords = [ "intranet", "offline" ]
aliases = [ "/questions/21059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using map of my city on offline Intranet](/questions/21059/using-map-of-my-city-on-offline-intranet)

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
<span id="post-21059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21059-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need to share a map of my city on our Intranet, we don't have Internet connexion on it. We need more than a picture of the map, we need to search street name. I know how to export data from OpenStreetMap but I don't know how put it on my web server (IIS).</p>
<p>Thanks for your help.</p>
<p>Bests regards.</p>
<p>Pierre</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intranet" rel="tag" title="see questions tagged &#39;intranet&#39;">intranet</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '13, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/1538329f3854e91b1177904f8988e3d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZeMuRDoCK&#39;s gravatar image" />
<p><span>ZeMuRDoCK</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZeMuRDoCK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21059" class="comments-container">
&#10;</div>
<div id="comment-tools-21059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21059-form-container" class="comment-form-container">
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

<span id="21061"></span>

<div id="answer-container-21061" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21061-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll need to setup your own tile server (to display the map) and nominatim server (to search for addresses). <a href="http://switch2osm.org/serving-tiles/">switch2osm</a> has a <a href="http://switch2osm.org/serving-tiles/">good tutorial on serving tiles</a>, and the <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">nominatim installation</a> instructions can be found on the <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">wiki</a>.</p>
<p>Hum, those instructions are for Linux servers though. All the tools should work on Windows, but I do not know of a tutorial for that platform. Maybe an easyer solution would be to use a <a href="http://wiki.openstreetmap.org/wiki/Virtual_machine_image">ready-made virtual machine image</a> to run the osm services.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '13, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '13, 10:19</strong> </span></p>
</div>
</div>
<div id="comments-container-21061" class="comments-container">
&#10;</div>
<div id="comment-tools-21061" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21061-form-container" class="comment-form-container">
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

