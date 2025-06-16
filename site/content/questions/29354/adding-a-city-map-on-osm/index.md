+++
type = "question"
title = "adding a city map on osm"
description = '''Dear experts of OSM Suppose I am given a map file of our city as shape file. Now, I want to import that into my local osm database so that i can browse different layers of the map in different zoom levels. Then, once the city residents update any object in my city, other residents will be able to se...'''
date = "2013-12-27T06:38:00Z"
lastmod = "2013-12-27T10:40:00Z"
weight = 29354
keywords = [ "to", "shape", "osm" ]
aliases = [ "/questions/29354" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [adding a city map on osm](/questions/29354/adding-a-city-map-on-osm)

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
<span id="post-29354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29354-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear experts of OSM</p>
<p>Suppose I am given a map file of our city as shape file. Now, I want to import that into my local osm database so that i can browse different layers of the map in different zoom levels. Then, once the city residents update any object in my city, other residents will be able to see that layered update. Any suggestion from where i start. I apologize as a newbie and thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span> <span class="post-tag tag-link-shape" rel="tag" title="see questions tagged &#39;shape&#39;">shape</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '13, 06:38</strong></p>
<img src="https://secure.gravatar.com/avatar/7ca5c1be3cfc90f13ed04f4c1a313ce5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdrahman&#39;s gravatar image" />
<p><span>mdrahman</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdrahman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29354" class="comments-container">
<span id="29356"></span>
<div id="comment-29356" class="comment">
<div id="post-29356-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Maybe it's my lack of english, but can you please explain the points of "browse different layers" and "layred update"? I don't have an exact idea of what you try to create :(</p>
</div>
<div id="comment-29356-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 07:36)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="29361"></span>
<div id="comment-29361" class="comment">
<div id="post-29361-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What type of object updation you are planning??</p>
</div>
<div id="comment-29361-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 08:46)</span> <span class="comment-user userinfo">GoldenCompass</span>
</div>
</div>
</div>
<div id="comment-tools-29354" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29354-form-container" class="comment-form-container">
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

<span id="29367"></span>

<div id="answer-container-29367" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29367-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note that there may be license implications - if you are using an empty database and import a city shape file then you are fine, but if you pre-load the database with OSM data and your users use that OSM data when they submit updates, then these updates would be derived from OSM and have to be made available under the ODbL (see our <a href="https://wiki.openstreetmap.org/wiki/Legal%20FAQ">Legal FAQ).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29367" class="comments-container">
&#10;</div>
<div id="comment-tools-29367" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29367-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29363"></span>

<div id="answer-container-29363" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29363-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi feel free to build your map locally using OSM maps and probably copy protected data as long as it is not uploaded into the OSM database. Read these lines or pages as well, <a href="https://www.openstreetmap.org/copyright/en">https://www.openstreetmap.org/copyright/en</a> See these around or about making local maps as well, <a href="https://help.openstreetmap.org/search/?csrfmiddlewaretoken=05c414b585eec063c16f1338f1d620e9&amp;q=local+maps&amp;Submit=Search&amp;t=question">https://help.openstreetmap.org/search/?csrfmiddlewaretoken=05c414b585eec063c16f1338f1d620e9&amp;q=local+maps&amp;Submit=Search&amp;t=question</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 08:56</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-29363" class="comments-container">
&#10;</div>
<div id="comment-tools-29363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29363-form-container" class="comment-form-container">
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

