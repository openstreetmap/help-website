+++
type = "question"
title = "Exporting Indoor map from openstreetmap"
description = '''Dear friends I have created map for our college building as following  http://www.openstreetmap.org/?lat=19.0753930807114&amp;amp;lon=72.9924237728119&amp;amp;zoom=18 This map has building interiors .you can see by adding data overlay . But due to limitations on zoom I cannot export the internal structure o...'''
date = "2012-02-13T18:01:00Z"
lastmod = "2020-05-14T07:34:00Z"
weight = 10572
keywords = [ "rendering", "android", "indoor", "export", "osm" ]
aliases = [ "/questions/10572" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Exporting Indoor map from openstreetmap](/questions/10572/exporting-indoor-map-from-openstreetmap)

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
<span id="post-10572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10572-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear friends I have created map for our college building as following <a href="http://www.openstreetmap.org/?lat=19.0753930807114&amp;lon=72.9924237728119&amp;zoom=18">http://www.openstreetmap.org/?lat=19.0753930807114&amp;lon=72.9924237728119&amp;zoom=18</a></p>
<p>This map has building interiors .you can see by adding data overlay .</p>
<p>But due to limitations on zoom I cannot export the internal structure of the mapped building I want to use this map on android phones for indoor navigation .But how to export the higher zoomed levels from osm ? How to render this map on android smartphone ?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '12, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a56f90750476bb5d076033dd5b0822f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teksan&#39;s gravatar image" />
<p><span>teksan</span><br />
<span class="score" title="45 reputation points">45</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teksan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10572" class="comments-container">
<span id="10577"></span>
<div id="comment-10577" class="comment">
<div id="post-10577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the building "transparent" enough for GPS the Oruxmaps app may work for <a href="http://you.It">you.It</a> will zoom my small house and garden to high levels</p>
</div>
<div id="comment-10577-info" class="comment-info">
<span class="comment-age">(13 Feb '12, 21:12)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-10572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10572-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="10575"></span>

<div id="answer-container-10575" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10575-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="teksan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you could do is to download OSM data in <a href="http://maperitive.net">Maperitive</a>. The default zoom limit is 19, but you can set it to a different value by typing the following command:</p>
<pre><code>set-setting name=map.max-zoom value=30</code></pre>
<p>Then you can export the map in a higher zoom.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '12, 19:14</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-10575" class="comments-container">
&#10;</div>
<div id="comment-tools-10575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10575-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10580"></span>

<div id="answer-container-10580" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10580-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looking at the building, I would probably be able to guess what most of the lines mean, but that is not something map data should rely on. Most of the lines seem untagged so it won't be visible on any rendered map - disregarding the zoom level.</p>
<p>For indoor mapping look at this <a href="http://wiki.openstreetmap.org/wiki/IndoorOSM">proposal</a>. It seems better than reinventing the wheel. You might get your building <a href="http://indoorosm.uni-hd.de/">here</a>. :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '12, 22:11</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-10580" class="comments-container">
&#10;</div>
<div id="comment-tools-10580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10580-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10589"></span>

<div id="answer-container-10589" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10589-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the special map service by <a href="http://www.flosm.de/html/POI-Karte.html">flosm.de</a> ... it can display OSM data as vector graphic, and you can zoom in much more than on <a href="http://osm.org">osm.org</a>. But be aware that this service might be some days behind to have recently edited OSM data.</p>
<p>For android devices there are some apps that can display OSM data also in vector form. I can recommend OsmAnd ... you can create your own recent vector maps if you need ... always try latest development version from <a href="http://osmand.net"></a><a href="http://osmand.net">osmand.net</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '12, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Feb '12, 16:25</strong> </span></p>
</div>
</div>
<div id="comments-container-10589" class="comments-container">
&#10;</div>
<div id="comment-tools-10589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10589-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10576"></span>

<div id="answer-container-10576" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10576-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM data has no zoom levels, only renderers impose this. If you render your own images with one of the many <a href="http://wiki.openstreetmap.org/wiki/Renderer">tools</a> (or even make a renderer of your own) you can display as much detail as you want. You can also render objects that the OSM site do not show.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '12, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-10576" class="comments-container">
&#10;</div>
<div id="comment-tools-10576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10576-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74799"></span>

<div id="answer-container-74799" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74799-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-74799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Such a great project, in the indoor map projects default zoom is 19 you can change the zoom level by giving the command.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '20, 07:34</strong></p>
<img src="https://secure.gravatar.com/avatar/d65bf3b998394330195797de81ff2de4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smith%20Hennry&#39;s gravatar image" />
<p><span>Smith Hennry</span><br />
<span class="score" title="-20 reputation points">-20</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smith Hennry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74799" class="comments-container">
&#10;</div>
<div id="comment-tools-74799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74799-form-container" class="comment-form-container">
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

