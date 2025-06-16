+++
type = "question"
title = "Error while installing Nominatim"
description = '''I am following steps given on https://wiki.openstreetmap.org/wiki/Nominatim/Installation to install Nominatim on my system. But while setting up postgresql, when I enter command - sudo service postgresql initdb, I receive an error message: &quot;Missing SERVICE_URI environment variable&quot; I don&#x27;t understand...'''
date = "2013-04-16T11:16:00Z"
lastmod = "2016-12-13T07:45:00Z"
weight = 21579
keywords = [ "postgresql", "nominatim", "installation" ]
aliases = [ "/questions/21579" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error while installing Nominatim](/questions/21579/error-while-installing-nominatim)

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
<span id="post-21579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21579-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am following steps given on <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> to install Nominatim on my system. But while setting up postgresql, when I enter command - sudo service postgresql initdb, I receive an error message: "Missing SERVICE_URI environment variable" I don't understand what value should I set for SERVICE_URI as environment variable. I searched over internet, but couldn't find any solution to it. Please help me with this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '13, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/8ecd380d754a6f288b7149f977b7f676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roshannerd&#39;s gravatar image" />
<p><span>roshannerd</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roshannerd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21579" class="comments-container">
<span id="21668"></span>
<div id="comment-21668" class="comment">
<div id="post-21668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it may be helpful if you would describe what your system is (operating system, version) and if you would cite the full error message.</p>
</div>
<div id="comment-21668-info" class="comment-info">
<span class="comment-age">(20 Apr '13, 02:33)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21579-form-container" class="comment-form-container">
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

<span id="53512"></span>

<div id="answer-container-53512" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53512-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The message comes from a proprietary tool that is called <code>service</code>. Apparently the poster is my colleague. The correct executable is <code>/sbin/service</code> and the full command should be <code>sudo /sbin/service postgresql initdb</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '16, 22:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9ea807427fcbc7607d99626dc7cbaf23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="proski&#39;s gravatar image" />
<p><span>proski</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="proski has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53512" class="comments-container">
<span id="53522"></span>
<div id="comment-53522" class="comment">
<div id="post-53522-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A third-party tool calling itself <code>service</code>? Oh dear...</p>
</div>
<div id="comment-53522-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 07:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53512-form-container" class="comment-form-container">
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

