+++
type = "question"
title = "Osmium: Working with History: time-filter Warning"
description = '''running the following command: osmium time-filter country.osh.pbf 2011-03-03T23:59:59Z -o country2011.osh.pbf Receiving the following warning &quot;You are writing to a file marked as having multiple object versions, but there will be only a single version of each object&quot;  What does this mean exactly? Wh...'''
date = "2017-08-24T23:52:00Z"
lastmod = "2017-08-27T23:58:00Z"
weight = 58814
keywords = [ "osmium", "history" ]
aliases = [ "/questions/58814" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmium: Working with History: time-filter Warning](/questions/58814/osmium-working-with-history-time-filter-warning)

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
<span id="post-58814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58814-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>running the following command:</p>
<p>osmium time-filter country.osh.pbf 2011-03-03T23:59:59Z -o country2011.osh.pbf</p>
<p>Receiving the following warning "You are writing to a file marked as having multiple object versions, but there will be only a single version of each object"</p>
<p>What does this mean exactly?</p>
<p>What I'm trying to do is extract the history for that country from inception till March 3rd 2011. Am I using the right command?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '17, 23:52</strong></p>
<img src="https://secure.gravatar.com/avatar/862ad51c251682f7af001a6cb0e487c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walshep&#39;s gravatar image" />
<p><span>walshep</span><br />
<span class="score" title="86 reputation points">86</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walshep has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58814" class="comments-container">
&#10;</div>
<div id="comment-tools-58814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58814-form-container" class="comment-form-container">
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

<span id="58815"></span>

<div id="answer-container-58815" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58815-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-58815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="walshep has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osmium autodetects the file ending <code>.osh</code> as a history file (which can contain multiple versions of the same object) and <code>.osm</code> as a non-history file (which contains at most one version of an OSM object). So you are reading from a history file and writing to a history file. But we know that the output will only contain at most one version of any object, that's what this command is for. So you should use an <code>.osm</code> suffix and you'll not get the warning.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '17, 07:22</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-58815" class="comments-container">
<span id="58840"></span>
<div id="comment-58840" class="comment">
<div id="post-58840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for clarifying Jochen. I needed an osh.pbf so I just used the following</p>
<p>osmium timefilter country.osh.pbf 2007-03-03T23:59:59Z 2011-03-03T23:59:59Z -o country2011.osh.pbf to get the output I needed.</p>
</div>
<div id="comment-58840-info" class="comment-info">
<span class="comment-age">(27 Aug '17, 23:58)</span> <span class="comment-user userinfo">walshep</span>
</div>
</div>
</div>
<div id="comment-tools-58815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58815-form-container" class="comment-form-container">
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

