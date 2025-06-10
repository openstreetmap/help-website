+++
type = "question"
title = "iD editor in an own web project: click on a list item and jump to the coordinate of the object in iD"
description = '''Hello. I would like to embed the iD-Editor into an own web project. What I have is a list of osm-objects which I am interested in which would be displayed next to the iD &quot;frame&quot;. With a click on a list item I would like to jump to the coordinate of the object and select it. Is it possible to solve t...'''
date = "2017-03-09T08:13:00Z"
lastmod = "2017-03-10T06:57:00Z"
weight = 55003
keywords = [ "ideditor", "development", "javascript" ]
aliases = [ "/questions/55003" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [iD editor in an own web project: click on a list item and jump to the coordinate of the object in iD](/questions/55003/id-editor-in-an-own-web-project-click-on-a-list-item-and-jump-to-the-coordinate-of-the-object-in-id)

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
<span id="post-55003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55003-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello.</p>
<p>I would like to embed the iD-Editor into an own web project. What I have is a list of osm-objects which I am interested in which would be displayed next to the iD "frame". With a click on a list item I would like to jump to the coordinate of the object and select it. Is it possible to solve this programmatically with javascript? Is there some kind of API for iD to achieve this?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '17, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d001d4c331042ef1dade5af6ed5f7ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="autumnus&#39;s gravatar image" />
<p><span>autumnus</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="autumnus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Mar '17, 00:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-55003" class="comments-container">
&#10;</div>
<div id="comment-tools-55003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55003-form-container" class="comment-form-container">
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

<span id="55011"></span>

<div id="answer-container-55011" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55011-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Okay, I found a solution myself:</p>
<p>With the help of this API</p>
<p><a href="https://github.com/openstreetmap/iD/blob/master/API.md">https://github.com/openstreetmap/iD/blob/master/API.md</a></p>
<p>I can construct an URL with osm_type, osm_id and coordinate that does what I want.</p>
<p>And then with the help of that:</p>
<p><a href="http://stackoverflow.com/questions/18145273/how-to-load-an-external-webpage-into-a-div-of-a-html-page">http://stackoverflow.com/questions/18145273/how-to-load-an-external-webpage-into-a-div-of-a-html-page</a></p>
<p>I display the result in a <code>&lt;div&gt;</code>.</p>
<p>By the way: I use a self hosted iD Editor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '17, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d001d4c331042ef1dade5af6ed5f7ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="autumnus&#39;s gravatar image" />
<p><span>autumnus</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="autumnus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '17, 13:09</strong> </span></p>
</div>
</div>
<div id="comments-container-55011" class="comments-container">
<span id="55013"></span>
<div id="comment-55013" class="comment">
<div id="post-55013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for sharing! :)</p>
</div>
<div id="comment-55013-info" class="comment-info">
<span class="comment-age">(10 Mar '17, 00:15)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="55018"></span>
<div id="comment-55018" class="comment">
<div id="post-55018-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are welcome!</p>
<p>But if anybody maybe has a more elegant solution...</p>
</div>
<div id="comment-55018-info" class="comment-info">
<span class="comment-age">(10 Mar '17, 06:57)</span> <span class="comment-user userinfo">autumnus</span>
</div>
</div>
</div>
<div id="comment-tools-55011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55011-form-container" class="comment-form-container">
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

