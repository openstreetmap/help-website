+++
type = "question"
title = "Installing kakrueger ppa on Debian"
description = '''Hi guys, I succeeded installing my own OSM tile server on a Ubuntu 12.04. Now, I need to install it on a Debian. I tried to follow the same procedure that I used on Ubuntu but I have a problem.  I&#x27;m using kakrueger ppa (https://launchpad.net/~kakrueger/+archive/openstreetmap) but it seems to fit onl...'''
date = "2013-07-08T09:12:00Z"
lastmod = "2013-07-08T10:09:00Z"
weight = 24071
keywords = [ "kakrueger", "debian", "ubuntu" ]
aliases = [ "/questions/24071" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Installing kakrueger ppa on Debian](/questions/24071/installing-kakrueger-ppa-on-debian)

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
<span id="post-24071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24071-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I succeeded installing my own OSM tile server on a Ubuntu 12.04. Now, I need to install it on a Debian. I tried to follow the same procedure that I used on Ubuntu but I have a problem.</p>
<p>I'm using kakrueger ppa (<a href="https://launchpad.net/~kakrueger/+archive/openstreetmap)">https://launchpad.net/~kakrueger/+archive/openstreetmap)</a> but it seems to fit only Ubuntu...</p>
<p>Do you have any idea how to install it on my Debian machine?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-kakrueger" rel="tag" title="see questions tagged &#39;kakrueger&#39;">kakrueger</span> <span class="post-tag tag-link-debian" rel="tag" title="see questions tagged &#39;debian&#39;">debian</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '13, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/4015aaa7dcb688fc988901e4caaac771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalu06&#39;s gravatar image" />
<p><span>Kalu06</span><br />
<span class="score" title="140 reputation points">140</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalu06 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24071" class="comments-container">
&#10;</div>
<div id="comment-tools-24071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24071-form-container" class="comment-form-container">
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

<span id="24074"></span>

<div id="answer-container-24074" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24074-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kalu06 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not really a OSM-related problem.</p>
<p>Since Debian and Ubuntu use the same package system it is possible to add an Ubuntu repository on Debian. The command <code>add-apt-repository</code> is contained in the <code>python-software-properties</code> package since Debian wheezy and you can of course add the repository manually by editing <em>/etc/apt/sources.list</em>.</p>
<p>But this can lead to problems. Each package has a list of dependencies. These dependencies are very distribution-specific. Dependencies for Ubuntu packages are chosen in a way to match other Ubuntu packages, not to match Debian packages. Trying to install Ubuntu packages on a Debian system can lead to weird dependencies which cannot be resolved, or important other packages might get deleted in order to solve the dependencies, and so on. Make sure you know what you're doing and watch the package installation process closely.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '13, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24074" class="comments-container">
<span id="24075"></span>
<div id="comment-24075" class="comment">
<div id="post-24075-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you very much Alex. Your answer is absolutely helpful and very interesting. I'll stick to Ubuntu then.</p>
</div>
<div id="comment-24075-info" class="comment-info">
<span class="comment-age">(08 Jul '13, 10:09)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
</div>
<div id="comment-tools-24074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24074-form-container" class="comment-form-container">
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

