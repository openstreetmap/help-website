+++
type = "question"
title = "Nominatim installation - Not finding proj headers"
description = '''I&#x27;m trying to install Nominatim in a CentOS 6 machine. When I execute ./configure in the Nominatim folder, I end up getting the following: checking for proj headers in /usr/include... not found checking for proj projection library... no configure: error: required library not found Already checked th...'''
date = "2013-02-26T22:13:00Z"
lastmod = "2013-10-25T16:01:00Z"
weight = 20326
keywords = [ "nominatim", "installation" ]
aliases = [ "/questions/20326" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim installation - Not finding proj headers](/questions/20326/nominatim-installation-not-finding-proj-headers)

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
<span id="post-20326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20326-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to install Nominatim in a CentOS 6 machine.</p>
<p>When I execute ./configure in the Nominatim folder, I end up getting the following:</p>
<p>checking for proj headers in /usr/include... not found checking for proj projection library... no configure: error: required library not found</p>
<p>Already checked the packages needed according to the wiki, it's all there.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '13, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/dc06a3de85eb8aa3a8331e85c1390a79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabriel_casado&#39;s gravatar image" />
<p><span>gabriel_casado</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabriel_casado has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20326" class="comments-container">
<span id="20327"></span>
<div id="comment-20327" class="comment">
<div id="post-20327-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Which "proj" packages do you have installed?</p>
</div>
<div id="comment-20327-info" class="comment-info">
<span class="comment-age">(27 Feb '13, 00:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="20328"></span>
<div id="comment-20328" class="comment">
<div id="post-20328-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@Frederik Ramm</span></p>
<p>I executed <code>yum list proj</code></p>
<p>Installed Packages proj.i386 4.8.0-3 @opengeo</p>
<p>yum list proj-devel</p>
<p>Installed Packages proj-devel.i386 4.8.0-3 @opengeo</p>
</div>
<div id="comment-20328-info" class="comment-info">
<span class="comment-age">(27 Feb '13, 01:29)</span> <span class="comment-user userinfo">gabriel_casado</span>
</div>
</div>
<span id="20343"></span>
<div id="comment-20343" class="comment">
<div id="post-20343-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@Frederik Ramm</span></p>
<p>Also:</p>
<p>proj-epsg.i386 4.8.0-3 @opengeo</p>
</div>
<div id="comment-20343-info" class="comment-info">
<span class="comment-age">(27 Feb '13, 16:24)</span> <span class="comment-user userinfo">gabriel_casado</span>
</div>
</div>
</div>
<div id="comment-tools-20326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20326-form-container" class="comment-form-container">
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

<span id="27495"></span>

<div id="answer-container-27495" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27495-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've had this happen b/c the gcc-c++.x86_64 (I guess gcc-c++.386 for you) was not installed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '13, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/d7d17c342bd5b7ddac0cbc61596a9c05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jessedp&#39;s gravatar image" />
<p><span>jessedp</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jessedp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27495" class="comments-container">
&#10;</div>
<div id="comment-tools-27495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27495-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20373"></span>

<div id="answer-container-20373" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20373-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>locate one of the proj header files with locate org_proj4_Projections.h then add that directory to the include path using -I/path/to/dir in the configure script.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '13, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-20373" class="comments-container">
&#10;</div>
<div id="comment-tools-20373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20373-form-container" class="comment-form-container">
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

