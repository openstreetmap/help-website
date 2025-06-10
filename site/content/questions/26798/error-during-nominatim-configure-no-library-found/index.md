+++
type = "question"
title = "Error during Nominatim configure - no library found"
description = '''I have a machine running CentOS and I followed the instructions on http://wiki.openstreetmap.org/wiki/Nominatim/Installation and have installed all the software listed there. But when I try to run ./configure on Nominatim, I am getting the following output: checking for proj headers in /usr/include....'''
date = "2013-09-26T23:04:00Z"
lastmod = "2013-09-30T19:31:00Z"
weight = 26798
keywords = [ "header", "nominatim", "projection" ]
aliases = [ "/questions/26798" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Error during Nominatim configure - no library found](/questions/26798/error-during-nominatim-configure-no-library-found)

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
<span id="post-26798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26798-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a machine running CentOS and I followed the instructions on <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">http://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> and have installed all the software listed there.</p>
<p>But when I try to run ./configure on Nominatim, I am getting the following output:</p>
<pre><code>checking for proj headers in /usr/include... not found
checking for proj projection library... no
configure: error: required library not found</code></pre>
<p>Someone in the forum suggested to find "org_proj4_Projections.h" file and add the directory path in the configure script, so did a search for the file:</p>
<pre><code># find / -name org_proj4_Projections.h
/usr/include/org_proj4_Projections.h</code></pre>
<p>and the header apparently is there in /user/include directory. What could the problem be? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '13, 23:04</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Sep '13, 01:16</strong> </span></p>
</div>
</div>
<div id="comments-container-26798" class="comments-container">
&#10;</div>
<div id="comment-tools-26798" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26798-form-container" class="comment-form-container">
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

<span id="26833"></span>

<div id="answer-container-26833" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26833-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="baekacaek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was faced with the same issue on Fedora 19. After a lot of digging into the configure script, realized that I had to install gcc-c++ package.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '13, 22:06</strong></p>
<img src="https://secure.gravatar.com/avatar/eae790503a48a8b0f7c392c6a5152cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chatman&#39;s gravatar image" />
<p><span>chatman</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chatman has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-26833" class="comments-container">
<span id="26877"></span>
<div id="comment-26877" class="comment">
<div id="post-26877-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>My goodness, thank you so much! This solved the problem. Hopefully they update the guide to include installation of gcc-c++</p>
</div>
<div id="comment-26877-info" class="comment-info">
<span class="comment-age">(30 Sep '13, 19:27)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="26878"></span>
<div id="comment-26878" class="comment">
<div id="post-26878-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Apparently, someone updated the wiki to include gcc-c++ in the installation guide. Cheers.</p>
</div>
<div id="comment-26878-info" class="comment-info">
<span class="comment-age">(30 Sep '13, 19:31)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-26833" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26833-form-container" class="comment-form-container">
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

