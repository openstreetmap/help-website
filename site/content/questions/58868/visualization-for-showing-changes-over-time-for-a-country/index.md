+++
type = "question"
title = "Visualization for showing changes over time for a country"
description = '''I&#x27;ve downloaded and have a .osm file of the data (nodes, ways, areas) as it looked over a country in 2011 and in 2017. I have the changeset and history files as well. I&#x27;d like to create a map with a time slider showing contributions as they occurred. On a black country background, I&#x27;d like to displa...'''
date = "2017-08-30T15:42:00Z"
lastmod = "2017-08-31T08:21:00Z"
weight = 58868
keywords = [ "visualization", "change" ]
aliases = [ "/questions/58868" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Visualization for showing changes over time for a country](/questions/58868/visualization-for-showing-changes-over-time-for-a-country)

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
<span id="post-58868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58868-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've downloaded and have a .osm file of the data (nodes, ways, areas) as it looked over a country in 2011 and in 2017. I have the changeset and history files as well.</p>
<p>I'd like to create a map with a time slider showing contributions as they occurred. On a black country background, I'd like to display compounding changes in a subtle color (grey or white) and as the slider advances, for every iteration (be it month or year) highlight in a brighter color the changes/additions that were made during that time iteration (be it a year or a month). As it advances to the next iteration those changes are no longer highlighted but are added to the compounding overall changes that are grey or white.</p>
<p>I think I would need to use the history and changeset files to derive a .osm snapshot of the nodes, ways, areas that were added during each iteration in time (2011, 2012, 2013...2017 if I was doing years). If I then combine them into one csv file could I then add them to say CARTODB and make this visualization?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-visualization" rel="tag" title="see questions tagged &#39;visualization&#39;">visualization</span> <span class="post-tag tag-link-change" rel="tag" title="see questions tagged &#39;change&#39;">change</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '17, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/862ad51c251682f7af001a6cb0e487c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walshep&#39;s gravatar image" />
<p><span>walshep</span><br />
<span class="score" title="86 reputation points">86</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walshep has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58868" class="comments-container">
<span id="58873"></span>
<div id="comment-58873" class="comment">
<div id="post-58873-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This seems to be the same question as <a href="https://gis.stackexchange.com/questions/253723/visualization-options-for-showing-changes-in-osm-over-time-for-a-country">https://gis.stackexchange.com/questions/253723/visualization-options-for-showing-changes-in-osm-over-time-for-a-country</a> .</p>
</div>
<div id="comment-58873-info" class="comment-info">
<span class="comment-age">(30 Aug '17, 16:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="58874"></span>
<div id="comment-58874" class="comment">
<div id="post-58874-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I deleted that one. Edited it and posting here as I think OSM help forum is more appropriate.</p>
</div>
<div id="comment-58874-info" class="comment-info">
<span class="comment-age">(30 Aug '17, 17:08)</span> <span class="comment-user userinfo">walshep</span>
</div>
</div>
</div>
<div id="comment-tools-58868" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58868-form-container" class="comment-form-container">
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

<span id="58883"></span>

<div id="answer-container-58883" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58883-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="walshep has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your project is quite ambitious and you can't expect a complete solution to your question here. There are many ways to go about this.</p>
<p>Here is one piece of the puzzle: You can use the <a href="http://docs.osmcode.org/osmium/latest/osmium-time-filter.html">time-filter</a> command of <a href="http://osmcode.org/osmium-tool/">osmium-tool</a> to get each point in time you want out of the history file. After that any of the usual ways of rendering the data works and you can generate a map image for each point in time and the combine them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '17, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-58883" class="comments-container">
&#10;</div>
<div id="comment-tools-58883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58883-form-container" class="comment-form-container">
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

