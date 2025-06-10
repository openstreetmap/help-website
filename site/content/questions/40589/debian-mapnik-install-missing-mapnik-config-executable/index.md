+++
type = "question"
title = "Debian Mapnik install missing &quot;mapnik-config&quot; executable."
description = '''Hi, I&#x27;m trying to install Mapnik on Debian using the instruction at https://github.com/mapnik/mapnik/wiki/DebianInstallation. It says to install do: apt-get install libmapnik2-2.0 mapnik-utils  I did that but the very first thing the &quot;Getting Started&quot; tutorial at the same site (https://github.com/ma...'''
date = "2015-01-25T07:51:00Z"
lastmod = "2015-01-25T09:11:00Z"
weight = 40589
keywords = [ "mapnik" ]
aliases = [ "/questions/40589" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Debian Mapnik install missing "mapnik-config" executable.](/questions/40589/debian-mapnik-install-missing-mapnik-config-executable)

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
<span id="post-40589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40589-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to install Mapnik on Debian using the instruction at <a href="https://github.com/mapnik/mapnik/wiki/DebianInstallation">https://github.com/mapnik/mapnik/wiki/DebianInstallation</a>. It says to install do:</p>
<pre><code>apt-get install libmapnik2-2.0 mapnik-utils</code></pre>
<p>I did that but the very first thing the "Getting Started" tutorial at the same site (<a href="https://github.com/mapnik/mapnik/wiki/GettingStartedInPython)">https://github.com/mapnik/mapnik/wiki/GettingStartedInPython)</a> says is to run:</p>
<pre><code>mapnik-config -v # should return a version number.</code></pre>
<p>The tutorial goes on to say you need 2.x, which I assume mean 2.0 or greater, and that you may get error in 2.0. But I don't get errors - the program just does not exist. I also tries to install from wheezy backports but that didn't work either. Surely someone else has had this issue but I can't find anything.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '15, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e1430f9a10b98409c90b5a0f78c15ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mapgenius323&#39;s gravatar image" />
<p><span>mapgenius323</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mapgenius323 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '15, 08:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-40589" class="comments-container">
&#10;</div>
<div id="comment-tools-40589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40589-form-container" class="comment-form-container">
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

<span id="40590"></span>

<div id="answer-container-40590" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40590-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mapgenius323 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to <a href="https://packages.debian.org/search?searchon=contents&amp;keywords=mapnik-config&amp;mode=path&amp;suite=stable&amp;arch=any">packages.debian.org</a> the binary <code>mapnik-config</code> is contained in the package <code>libmapnik2-dev</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '15, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40590" class="comments-container">
<span id="40591"></span>
<div id="comment-40591" class="comment">
<div id="post-40591-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah thx. Thought it might be. I was yet confirm that as I can't get that installed just yet as I have some dep conflicts to sort out. Should be OK though.</p>
</div>
<div id="comment-40591-info" class="comment-info">
<span class="comment-age">(25 Jan '15, 09:11)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
</div>
<div id="comment-tools-40590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40590-form-container" class="comment-form-container">
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

