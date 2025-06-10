+++
type = "question"
title = "Error when compiling osm2world code with myEclipse"
description = ''' Have anyone of you encountered this? How to deal with it? Thanks.'''
date = "2013-08-18T09:40:00Z"
lastmod = "2013-08-18T10:46:00Z"
weight = 25539
keywords = [ "osm2world" ]
aliases = [ "/questions/25539" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error when compiling osm2world code with myEclipse](/questions/25539/error-when-compiling-osm2world-code-with-myeclipse)

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
<span id="post-25539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25539-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="http://c.hiphotos.baidu.com/zhidao/wh%3D600%2C800/sign=6efcabc03b292df59796a4138c017058/2934349b033b5bb533f84e1137d3d539b600bc36.jpg" alt="alt text" /></p>
<p>Have anyone of you encountered this? How to deal with it? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2world" rel="tag" title="see questions tagged &#39;osm2world&#39;">osm2world</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '13, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/17c3dc3471d4c2221801906c7a545ed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%E7%8E%8B%E5%BD%A6%E6%96%87&#39;s gravatar image" />
<p><span>王彦文</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="王彦文 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-25539" class="comments-container">
<span id="25541"></span>
<div id="comment-25541" class="comment">
<div id="post-25541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interestingly <a href="http://osm2world.org/contact/">osm2world's contact page</a> does suggest here as a place for technical questions.</p>
</div>
<div id="comment-25541-info" class="comment-info">
<span class="comment-age">(18 Aug '13, 10:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="25545"></span>
<div id="comment-25545" class="comment">
<div id="post-25545-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Error messages should always be posted as <em>text</em> so that other users can find this question and possible answers when searching for the error.</p>
</div>
<div id="comment-25545-info" class="comment-info">
<span class="comment-age">(18 Aug '13, 10:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25539-form-container" class="comment-form-container">
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

<span id="25543"></span>

<div id="answer-container-25543" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25543-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That problem occurs because <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Collections.html#emptyIterator%28%29">Collections.emptyIterator</a> is only available in Java 7 and higher. OSM2World is supposed to target Java 6, but sometimes things like this slip in.</p>
<p>I believe the latest version of the code is clean (as of now). That particular occurrence was fixed in a <a href="https://github.com/tordanik/OSM2World/commit/b229409cb58e41af697e789ab70a169a2281e921">recent commit</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '13, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-25543" class="comments-container">
&#10;</div>
<div id="comment-tools-25543" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25543-form-container" class="comment-form-container">
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

