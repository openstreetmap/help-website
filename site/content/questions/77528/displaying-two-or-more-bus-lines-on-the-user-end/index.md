+++
type = "question"
title = "Displaying two or more bus lines on the user end"
description = '''Hello, I would like to know how to show multiple bus lines simultaneously on the map. For example, how to superpose these two bus lines : https://www.openstreetmap.org/relation/1255722 et https://www.openstreetmap.org/relation/9433940 ?'''
date = "2020-11-12T22:39:00Z"
lastmod = "2020-11-13T17:13:00Z"
weight = 77528
keywords = [ "bus_route", "public-transport" ]
aliases = [ "/questions/77528" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Displaying two or more bus lines on the user end](/questions/77528/displaying-two-or-more-bus-lines-on-the-user-end)

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
<span id="post-77528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77528-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I would like to know how to show multiple bus lines simultaneously on the map. For example, how to superpose these two bus lines : <a href="https://www.openstreetmap.org/relation/1255722">https://www.openstreetmap.org/relation/1255722</a> et <a href="https://www.openstreetmap.org/relation/9433940">https://www.openstreetmap.org/relation/9433940</a> ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus_route" rel="tag" title="see questions tagged &#39;bus_route&#39;">bus_route</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '20, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/9195948db109315ae02636b590cb75d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="julef&#39;s gravatar image" />
<p><span>julef</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="julef has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77528" class="comments-container">
&#10;</div>
<div id="comment-tools-77528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77528-form-container" class="comment-form-container">
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

<span id="77529"></span>

<div id="answer-container-77529" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77529-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="julef has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could try this query at <a href="https://overpass-turbo.eu/s/102O">Overpass Turbo</a>:</p>
<pre><code>[out:xml][timeout:25];
&#10;(
relation(1255722);
relation(9433940);
);
&#10;out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '20, 00:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-77529" class="comments-container">
<span id="77539"></span>
<div id="comment-77539" class="comment">
<div id="post-77539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Very good, it works well enough for me. ;)</p>
</div>
<div id="comment-77539-info" class="comment-info">
<span class="comment-age">(13 Nov '20, 17:13)</span> <span class="comment-user userinfo">julef</span>
</div>
</div>
</div>
<div id="comment-tools-77529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77529-form-container" class="comment-form-container">
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

