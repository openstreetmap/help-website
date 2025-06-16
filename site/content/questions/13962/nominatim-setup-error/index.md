+++
type = "question"
title = "nominatim setup error"
description = '''Hello, I follow the install instraction on the nominatim wicki for version V2. Compiling with made give the following messages: undefined reference to &#x27;Bz2_bzReadClose&#x27; undefined reference to &#x27;xmlReaderForIO&#x27; and more of this messages.... System is ubuntu 12.04 LTS 64 Bit. Can anyone help me to comp...'''
date = "2012-07-03T10:09:00Z"
lastmod = "2012-07-03T14:14:00Z"
weight = 13962
keywords = [ "setup", "nominatim", "reference" ]
aliases = [ "/questions/13962" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim setup error](/questions/13962/nominatim-setup-error)

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
<span id="post-13962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13962-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I follow the install instraction on the nominatim wicki for version V2.</p>
<p>Compiling with made give the following messages:</p>
<p>undefined reference to 'Bz2_bzReadClose' undefined reference to 'xmlReaderForIO' and more of this messages....</p>
<p>System is ubuntu 12.04 LTS 64 Bit.</p>
<p>Can anyone help me to compile nominatim? What is wrong.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-reference" rel="tag" title="see questions tagged &#39;reference&#39;">reference</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '12, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/9a31a7056440abd1ef62c2be15bfe52c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raplin&#39;s gravatar image" />
<p><span>raplin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raplin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13962" class="comments-container">
&#10;</div>
<div id="comment-tools-13962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13962-form-container" class="comment-form-container">
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

<span id="13964"></span>

<div id="answer-container-13964" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13964-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are missing the xml2 and bz2 libraries, see the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Ubuntu.2FDebian">first part of installation instructions</a>:</p>
<pre><code>sudo apt-get install libxml2-dev libbz2-dev</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '12, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-13964" class="comments-container">
<span id="13965"></span>
<div id="comment-13965" class="comment">
<div id="post-13965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, but there are installed!!</p>
</div>
<div id="comment-13965-info" class="comment-info">
<span class="comment-age">(03 Jul '12, 11:44)</span> <span class="comment-user userinfo">raplin</span>
</div>
</div>
<span id="13967"></span>
<div id="comment-13967" class="comment">
<div id="post-13967-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Looks like there was a bug in the configure system. Hopefully fixed now. Please update your version of Nominatim and try again.</p>
</div>
<div id="comment-13967-info" class="comment-info">
<span class="comment-age">(03 Jul '12, 14:14)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-13964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13964-form-container" class="comment-form-container">
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

