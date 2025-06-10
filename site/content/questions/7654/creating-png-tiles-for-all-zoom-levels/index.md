+++
type = "question"
title = "Creating PNG tiles for all zoom levels"
description = '''I wish to make a local copy of 256x256 tiles for my country at all zoom levels. This is for use with a Rohde &amp;amp; Schwarz PR100 receiver. There is freely available software from Rohde &amp;amp; Schwarz which downloads the tiles from OSM and places them in separate folders depending on zoom level - http...'''
date = "2011-09-06T09:04:00Z"
lastmod = "2011-09-09T09:11:00Z"
weight = 7654
keywords = [ "tiles", "pr100", "schwarz", "mapnik", "rohde" ]
aliases = [ "/questions/7654" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Creating PNG tiles for all zoom levels](/questions/7654/creating-png-tiles-for-all-zoom-levels)

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
<span id="post-7654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7654-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I wish to make a local copy of 256x256 tiles for my country at all zoom levels. This is for use with a Rohde &amp; Schwarz PR100 receiver. There is freely available software from Rohde &amp; Schwarz which downloads the tiles from OSM and places them in separate folders depending on zoom level - <a href="http://www2.rohde-schwarz.com/en/products/radiomonitoring/receivers/PR100-%7C-Software-%7C-24-%7C-5286.html.">http://www2.rohde-schwarz.com/en/products/radiomonitoring/receivers/PR100-|-Software-|-24-|-5286.html.</a></p>
<p>However I want to be able to generate these tiles myself locally as using data from a .osm.bz2 file as using the above software is time consuming and is obviously a strain on the OSMs servers.</p>
<p>What is the most straight forward way of achieving this? I have PostgreSQL with PostGIS and HOTOSM with Mapnik installed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-pr100" rel="tag" title="see questions tagged &#39;pr100&#39;">pr100</span> <span class="post-tag tag-link-schwarz" rel="tag" title="see questions tagged &#39;schwarz&#39;">schwarz</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-rohde" rel="tag" title="see questions tagged &#39;rohde&#39;">rohde</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '11, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/e6bde46d07a0d8a1921ff4bf4c03d25c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hurleytom&#39;s gravatar image" />
<p><span>hurleytom</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hurleytom has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7654" class="comments-container">
<span id="7749"></span>
<div id="comment-7749" class="comment">
<div id="post-7749-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just as a brief comment: thank you for being considerate to the OSM servers!</p>
</div>
<div id="comment-7749-info" class="comment-info">
<span class="comment-age">(09 Sep '11, 09:11)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7654-form-container" class="comment-form-container">
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

<span id="7662"></span>

<div id="answer-container-7662" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7662-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the python script <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py">generate_tiles.py</a> which is in the mapnik distribution to batch render areas. Another (more complicated) approach is using tile-server tools like renderd or tirex. You can find more information in the osm wiki, e.g. <a href="http://wiki.openstreetmap.org/wiki/Tiles">here</a> and <a href="http://wiki.openstreetmap.org/wiki/Creating_your_own_tiles">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '11, 11:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '11, 11:34</strong> </span></p>
</div>
</div>
<div id="comments-container-7662" class="comments-container">
&#10;</div>
<div id="comment-tools-7662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7662-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7748"></span>

<div id="answer-container-7748" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7748-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One way to do this is to use Maperitive (depending on the size of the country): <a href="http://braincrunch.tumblr.com/post/9921938947/maperitive-tutorial-a-hiking-web-map-in-ten-easy-steps">Maperitive Tutorial: A Hiking Web Map In Ten Easy Steps</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '11, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-7748" class="comments-container">
&#10;</div>
<div id="comment-tools-7748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7748-form-container" class="comment-form-container">
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

