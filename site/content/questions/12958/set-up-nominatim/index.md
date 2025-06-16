+++
type = "question"
title = "Set up Nominatim"
description = '''I tried following the steps on https://wiki.openstreetmap.org/wiki/Nominatim/Installation after installing all prerequisits: git clone git://github.com/twain47/Nominatim.git  Compile the postgresql module:  cd module make  Compile the Nominatim tool:  cd nominatim ./autogen.sh ./configure make  It se...'''
date = "2012-05-25T22:06:00Z"
lastmod = "2012-05-31T19:28:00Z"
weight = 12958
keywords = [ "setup", "nominatim", "installation" ]
aliases = [ "/questions/12958" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Set up Nominatim](/questions/12958/set-up-nominatim)

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
<span id="post-12958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12958-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I tried following the steps on <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> after installing all prerequisits:</p>
<pre><code>git clone git://github.com/twain47/Nominatim.git</code></pre>
<p>Compile the postgresql module:</p>
<pre><code>cd module
make</code></pre>
<p>Compile the Nominatim tool:</p>
<pre><code>cd nominatim
./autogen.sh
./configure
make</code></pre>
<p>It seemed OK for all the steps until the last make that showed many messages including:</p>
<blockquote>
<p>svnversion: command not found ...</p>
</blockquote>
<p>What's the problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '12, 22:06</strong></p>
<img src="https://secure.gravatar.com/avatar/b332531100c9e5129fe96996d425b1e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TryOSM&#39;s gravatar image" />
<p><span>TryOSM</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TryOSM has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '12, 22:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-12958" class="comments-container">
&#10;</div>
<div id="comment-tools-12958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12958-form-container" class="comment-form-container">
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

<span id="12959"></span>

<div id="answer-container-12959" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12959-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems that you do not have the command 'svnversion' on your system. You can install the package <strong>subversion</strong> to get it.</p>
<p>I have added <em>git</em> and <em>subversion</em> to the requirements in the installation guide.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '12, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-12959" class="comments-container">
<span id="13026"></span>
<div id="comment-13026" class="comment">
<div id="post-13026-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks, Gnonthgol! I have got subversion installed. Now I still have one problem:</p>
<p>"geos-config: command not found"</p>
<p>Does this mean another package missing?</p>
</div>
<div id="comment-13026-info" class="comment-info">
<span class="comment-age">(28 May '12, 16:31)</span> <span class="comment-user userinfo">TryOSM</span>
</div>
</div>
<span id="13033"></span>
<div id="comment-13033" class="comment">
<div id="post-13033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, you are missing the 'libgeos-dev' package.</p>
<p>You can search for files in all packages at packages.ubuntu.com to find the package that includes the missing file or command.</p>
</div>
<div id="comment-13033-info" class="comment-info">
<span class="comment-age">(28 May '12, 20:14)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="13168"></span>
<div id="comment-13168" class="comment">
<div id="post-13168-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much!</p>
</div>
<div id="comment-13168-info" class="comment-info">
<span class="comment-age">(31 May '12, 19:28)</span> <span class="comment-user userinfo">TryOSM</span>
</div>
</div>
</div>
<div id="comment-tools-12959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12959-form-container" class="comment-form-container">
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

