+++
type = "question"
title = "https://{a,b,c}.tile.openstreetmap.org/crossdomain.xml not found"
description = '''Crossdomain.xml files on https://{a,b,c}.tile.openstreetmap.org/crossdomain.xml are not found since November 27, thus our flex application can not load map tiles. Is there any changes?'''
date = "2020-11-30T12:48:00Z"
lastmod = "2020-12-01T07:18:00Z"
weight = 77792
keywords = [ "flex", "crossdomain" ]
aliases = [ "/questions/77792" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [https://{a,b,c}.tile.openstreetmap.org/crossdomain.xml not found](/questions/77792/httpsabctileopenstreetmaporgcrossdomainxml-not-found)

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
<span id="post-77792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77792-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Crossdomain.xml files on https://{a,b,c}.tile.openstreetmap.org/crossdomain.xml are not found since November 27, thus our flex application can not load map tiles. Is there any changes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-flex" rel="tag" title="see questions tagged &#39;flex&#39;">flex</span> <span class="post-tag tag-link-crossdomain" rel="tag" title="see questions tagged &#39;crossdomain&#39;">crossdomain</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '20, 12:48</strong></p>
<img src="https://secure.gravatar.com/avatar/788bfde7ddcb8b89b1fafd6d1777e987?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rojda&#39;s gravatar image" />
<p><span>rojda</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rojda has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77792" class="comments-container">
<span id="77795"></span>
<div id="comment-77795" class="comment">
<div id="post-77795-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I can browse to that file fine from here, so the output of <a href="https://tile.openstreetmap.org/cgi-bin/debug">https://tile.openstreetmap.org/cgi-bin/debug</a> might help in case the issue is server specific</p>
</div>
<div id="comment-77795-info" class="comment-info">
<span class="comment-age">(30 Nov '20, 13:53)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77792-form-container" class="comment-form-container">
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

<span id="77806"></span>

<div id="answer-container-77806" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77806-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-77806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for reporting the problem - my colleague is working on fixing it.</p>
<p>In the meantime please don't hardcode the names of the upstream render servers like that as it's extremely antisocial.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '20, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-77806" class="comments-container">
<span id="77820"></span>
<div id="comment-77820" class="comment">
<div id="post-77820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for that</p>
</div>
<div id="comment-77820-info" class="comment-info">
<span class="comment-age">(01 Dec '20, 07:18)</span> <span class="comment-user userinfo">rojda</span>
</div>
</div>
</div>
<div id="comment-tools-77806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77806-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77807"></span>

<div id="answer-container-77807" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77807-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-77807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The missing file is simply an error that is being fixed as I type.</p>
<p>Please do not hack around such issues but instead simply report them in the right place <a href="https://github.com/openstreetmap/operations">https://github.com/openstreetmap/operations</a> (your solution a) doesn't go through the tile cache, b) is going to break the next time a server is changed).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '20, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-77807" class="comments-container">
<span id="77819"></span>
<div id="comment-77819" class="comment">
<div id="post-77819-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, i'll change them back.</p>
</div>
<div id="comment-77819-info" class="comment-info">
<span class="comment-age">(01 Dec '20, 07:17)</span> <span class="comment-user userinfo">rojda</span>
</div>
</div>
</div>
<div id="comment-tools-77807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77807-form-container" class="comment-form-container">
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

