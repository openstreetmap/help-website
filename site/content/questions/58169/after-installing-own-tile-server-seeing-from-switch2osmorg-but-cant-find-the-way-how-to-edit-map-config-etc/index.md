+++
type = "question"
title = "After installing own tile server seeing from switch2osm.org but can&#x27;t find the way how to edit map, config etc."
description = '''Hi, I have followed the procedure of creating own title server from switch2osm.org, we have config well but now we are in trouble we don&#x27;t know what to do next how to see have map &amp;amp; edit it for our use. We are stuck after successfully creating title server. Kindly I request provide some links to...'''
date = "2017-08-12T08:50:00Z"
lastmod = "2017-08-13T14:50:00Z"
weight = 58169
keywords = [ "what_next", "tileserver" ]
aliases = [ "/questions/58169" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [After installing own tile server seeing from switch2osm.org but can't find the way how to edit map, config etc.](/questions/58169/after-installing-own-tile-server-seeing-from-switch2osmorg-but-cant-find-the-way-how-to-edit-map-config-etc)

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
<span id="post-58169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58169-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have followed the procedure of creating own title server from switch2osm.org, we have config well but now we are in trouble we don't know what to do next how to see have map &amp; edit it for our use. We are stuck after successfully creating title server.</p>
<p>Kindly I request provide some links to help us moving further steps.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-what_next" rel="tag" title="see questions tagged &#39;what_next&#39;">what_next</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '17, 08:50</strong></p>
<img src="https://secure.gravatar.com/avatar/8a7dd8039b32a4e720977f3f34621670?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ranveerneemkar&#39;s gravatar image" />
<p><span>ranveerneemkar</span><br />
<span class="score" title="9 reputation points">9</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ranveerneemkar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58169" class="comments-container">
<span id="58283"></span>
<div id="comment-58283" class="comment">
<div id="post-58283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you mean by "edit it for our use"? What do you actually want to change?</p>
</div>
<div id="comment-58283-info" class="comment-info">
<span class="comment-age">(13 Aug '17, 14:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58169-form-container" class="comment-form-container">
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

<span id="58264"></span>

<div id="answer-container-58264" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58264-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Running a tile server only has a peripheral bearing on running an API server with editor and so on.</p>
<p>For installing an instance of the so called "rails port" see here: <a href="https://github.com/openstreetmap/openstreetmap-website">https://github.com/openstreetmap/openstreetmap-website</a> and <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</a></p>
<p>Note that you will need to set up replication and consume diffs on your tile server from your rails-post instance. Doing that is not well documented and you will need to figure things out yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '17, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-58264" class="comments-container">
&#10;</div>
<div id="comment-tools-58264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58264-form-container" class="comment-form-container">
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

