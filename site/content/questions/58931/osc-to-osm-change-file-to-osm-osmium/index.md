+++
type = "question"
title = "OSC to OSM - Change file to OSM osmium"
description = '''Is it possible to use the derive-changes command to get an osc change file of the difference between two time periods and then convert that osc file to osm file for visualization purposes? Is it safe to assume that it will show only the data that was modified between the two time periods? Thanks!'''
date = "2017-09-02T20:04:00Z"
lastmod = "2017-09-03T22:03:00Z"
weight = 58931
keywords = [ "osmium", "visualization", "change" ]
aliases = [ "/questions/58931" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSC to OSM - Change file to OSM osmium](/questions/58931/osc-to-osm-change-file-to-osm-osmium)

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
<span id="post-58931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to use the <strong>derive-changes</strong> command to get an osc change file of the difference between two time periods and then convert that osc file to osm file for visualization purposes? Is it safe to assume that it will show only the data that was modified between the two time periods?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-visualization" rel="tag" title="see questions tagged &#39;visualization&#39;">visualization</span> <span class="post-tag tag-link-change" rel="tag" title="see questions tagged &#39;change&#39;">change</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '17, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/862ad51c251682f7af001a6cb0e487c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walshep&#39;s gravatar image" />
<p><span>walshep</span><br />
<span class="score" title="86 reputation points">86</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walshep has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted <strong>02 Sep '17, 20:07</strong> </span></p>
</div>
</div>
<div id="comments-container-58931" class="comments-container">
<span id="58932"></span>
<div id="comment-58932" class="comment">
<div id="post-58932-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just a comment on the side: I hope you realize that geometry in the OSM data model is carried by the nodes only. So for example moving a node of a way will not create a new version of that way (adding of deleting a node, or changing the tags -will- create a new version).</p>
<p>If you are visualizing changes of OSM data between points in time you need to take this into account.</p>
</div>
<div id="comment-58932-info" class="comment-info">
<span class="comment-age">(02 Sep '17, 21:34)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58931-form-container" class="comment-form-container">
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

<span id="58948"></span>

<div id="answer-container-58948" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58948-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="walshep has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, that doesn't work. The change file doesn't contain enough information to do the actual rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '17, 19:33</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-58948" class="comments-container">
<span id="58951"></span>
<div id="comment-58951" class="comment">
<div id="post-58951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did attempt it to compare 2012 and 2013 data and I noticed that it didn't include everything I saw from a snapshot osm file of the 2013 data that I generated with the "time-filter" command. How would you recommend isolating just the changes? Would importing the data into QGIS and just processing it there to remove duplicates be the best option? Thanks!</p>
</div>
<div id="comment-58951-info" class="comment-info">
<span class="comment-age">(03 Sep '17, 22:03)</span> <span class="comment-user userinfo">walshep</span>
</div>
</div>
</div>
<div id="comment-tools-58948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58948-form-container" class="comment-form-container">
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

