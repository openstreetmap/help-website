+++
type = "question"
title = "Tiles seemingly not generating"
description = '''When I select a boundary box for tiles, they don&#x27;t generate. But when I have the boundary box be the entire world, the tiles generate. When I look at what has been generated, it is a blank world except for the state that I am trying to generate tiles for. I have imported the state into the database,...'''
date = "2011-10-26T19:34:00Z"
lastmod = "2011-10-27T09:53:00Z"
weight = 8673
keywords = [ "generate_tiles" ]
aliases = [ "/questions/8673" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tiles seemingly not generating](/questions/8673/tiles-seemingly-not-generating)

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
<span id="post-8673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8673-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I select a boundary box for tiles, they don't generate. But when I have the boundary box be the entire world, the tiles generate. When I look at what has been generated, it is a blank world except for the state that I am trying to generate tiles for. I have imported the state into the database, but I can't seem to get tiles to generate when I specify the boundary box. What can I do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '11, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/48980c72ff56a285d3689c40bc272e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NDFobia1158&#39;s gravatar image" />
<p><span>NDFobia1158</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NDFobia1158 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8673" class="comments-container">
<span id="8674"></span>
<div id="comment-8674" class="comment">
<div id="post-8674-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you give more backgroud information? What exactly are you trying to do? What program are you using to generate tiles? Have you followed some guides?</p>
</div>
<div id="comment-8674-info" class="comment-info">
<span class="comment-age">(26 Oct '11, 19:43)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="8676"></span>
<div id="comment-8676" class="comment">
<div id="post-8676-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am trying to get tiles generated for the southern part of California. I am using Mapnik to generate the tiles. I am following the mapnik guide on the osm wiki.</p>
</div>
<div id="comment-8676-info" class="comment-info">
<span class="comment-age">(26 Oct '11, 19:53)</span> <span class="comment-user userinfo">NDFobia1158</span>
</div>
</div>
</div>
<div id="comment-tools-8673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8673-form-container" class="comment-form-container">
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

<span id="8675"></span>

<div id="answer-container-8675" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8675-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps you have the coordinates in the wrong variables. It happened to me too. If you call a function similar to generate(bbox(x1,y1,x2,y2),zoomlvl, name). Make sure your x's and y's are given correct values.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '11, 19:44</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Oct '11, 19:45</strong> </span></p>
</div>
</div>
<div id="comments-container-8675" class="comments-container">
&#10;</div>
<div id="comment-tools-8675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8675-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8680"></span>

<div id="answer-container-8680" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8680-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please look for error messages mapnik produces. Perhaps this similar question can give you some hints: <a href="http://help.openstreetmap.org/questions/8506/mapnik-image-generations-returns-error">http://help.openstreetmap.org/questions/8506/mapnik-image-generations-returns-error</a></p>
<p>If you get tiles, but all are empty, perhaps the extent bounds in inc/datasource-settings.xml.inc is wrong.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '11, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/baddeab22266e1533be4ba4c9f3deb49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajoessen&#39;s gravatar image" />
<p><span>ajoessen</span><br />
<span class="score" title="168 reputation points">168</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajoessen has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-8680" class="comments-container">
&#10;</div>
<div id="comment-tools-8680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8680-form-container" class="comment-form-container">
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

