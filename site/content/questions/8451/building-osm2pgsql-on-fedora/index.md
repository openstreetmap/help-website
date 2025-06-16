+++
type = "question"
title = "Building Osm2pgsql on Fedora"
description = '''I&#x27;ve been following the directions located here, but when I run &quot;./configure&quot; I get this at the bottom: checking for xml2-config... /usr/bin/xml2-config checking for xml2 libraries... yes checking for zlib headers in /user/include... not found checking for zlib compression library not found I then t...'''
date = "2011-10-14T15:27:00Z"
lastmod = "2011-10-15T20:21:00Z"
weight = 8451
keywords = [ "not", "found", "zlib" ]
aliases = [ "/questions/8451" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Building Osm2pgsql on Fedora](/questions/8451/building-osm2pgsql-on-fedora)

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
<span id="post-8451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8451-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been following the directions located <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql#From_source_.28generic.29">here</a>, but when I run "./configure" I get this at the bottom:<br />
<br />
checking for xml2-config... /usr/bin/xml2-config<br />
checking for xml2 libraries... yes<br />
checking for zlib headers in /user/include... not found<br />
checking for zlib compression library not found<br />
<br />
I then tried to install zlib, but it was already installed. I reinstalled zlib and I still get the same error. What am I doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-found" rel="tag" title="see questions tagged &#39;found&#39;">found</span> <span class="post-tag tag-link-zlib" rel="tag" title="see questions tagged &#39;zlib&#39;">zlib</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '11, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/48980c72ff56a285d3689c40bc272e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NDFobia1158&#39;s gravatar image" />
<p><span>NDFobia1158</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NDFobia1158 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8451" class="comments-container">
<span id="8456"></span>
<div id="comment-8456" class="comment">
<div id="post-8456-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>checking for zlib headers in /user/include... not found</p>
</blockquote>
<p>If you have really copied-pasted that, I think something is wrong about the path "/user/include" for searching the headers…</p>
</div>
<div id="comment-8456-info" class="comment-info">
<span class="comment-age">(14 Oct '11, 16:40)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-8451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8451-form-container" class="comment-form-container">
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

<span id="8452"></span>

<div id="answer-container-8452" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8452-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="NDFobia1158 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know fedora package naming, but I think you have to install something like zlib-dev in order to have headers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '11, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8452" class="comments-container">
<span id="8453"></span>
<div id="comment-8453" class="comment">
<div id="post-8453-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just tried doing that and I apparently already have that installed as well. I just reinstalled it and I am still getting the same result.</p>
</div>
<div id="comment-8453-info" class="comment-info">
<span class="comment-age">(14 Oct '11, 16:12)</span> <span class="comment-user userinfo">NDFobia1158</span>
</div>
</div>
<span id="8454"></span>
<div id="comment-8454" class="comment">
<div id="post-8454-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I suppose you have installed the packages list given on the wiki?</p>
<blockquote>
<p>yum install geos-devel proj-devel postgresql-devel libxml2-devel bzip2-devel gcc-c++ protobuf-c-devel autoconf automake libtool</p>
</blockquote>
</div>
<div id="comment-8454-info" class="comment-info">
<span class="comment-age">(14 Oct '11, 16:33)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="8458"></span>
<div id="comment-8458" class="comment">
<div id="post-8458-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess I overlooked that step. After installing what wasn't already installed from that list, I got it working. Thanks.</p>
</div>
<div id="comment-8458-info" class="comment-info">
<span class="comment-age">(14 Oct '11, 17:10)</span> <span class="comment-user userinfo">NDFobia1158</span>
</div>
</div>
<span id="8461"></span>
<div id="comment-8461" class="comment">
<div id="post-8461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you can close this question. Thanks.</p>
</div>
<div id="comment-8461-info" class="comment-info">
<span class="comment-age">(15 Oct '11, 20:21)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-8452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8452-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8455"></span>

<div id="answer-container-8455" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8455-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>checking for zlib headers in /user/include... not found</p>
</blockquote>
<p>If you have really copied-pasted that, I think something is wrong about the path "/user/include" for searching the headers…</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '11, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8455" class="comments-container">
&#10;</div>
<div id="comment-tools-8455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8455-form-container" class="comment-form-container">
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

