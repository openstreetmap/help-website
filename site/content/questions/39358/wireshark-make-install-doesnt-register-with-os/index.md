+++
type = "question"
title = "Wireshark make install doesnt register with OS"
description = '''I&#x27;ve succefully build wireshark on Mint 17.1 Cinnamon. I am able to run it from /usr/local/bin. Iam also able to run it from a terminal window but I am unable to find the launcher in the start menu. How can i solve this? Registering the install properly with the OS?'''
date = "2015-01-22T07:11:00Z"
lastmod = "2015-01-23T04:14:00Z"
weight = 39358
keywords = [ "make", "wireshark", "mint", "install", "linux" ]
aliases = [ "/questions/39358" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark make install doesnt register with OS](/questions/39358/wireshark-make-install-doesnt-register-with-os)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39358-score" class="post-score" title="current number of votes">0</div><span id="post-39358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've succefully build wireshark on <code>Mint 17.1 Cinnamon</code>. I am able to run it from <code>/usr/local/bin</code>. Iam also able to run it from a terminal window but I am unable to find the launcher in the start menu.</p><p>How can i solve this? Registering the install properly with the OS?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-mint" rel="tag" title="see questions tagged &#39;mint&#39;">mint</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '15, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/27fcbc2c78dd2c12e7b0de7b08efc891?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maarten&#39;s gravatar image" /><p><span>Maarten</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maarten has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '15, 07:12</strong> </span></p></div></div><div id="comments-container-39358" class="comments-container"></div><div id="comment-tools-39358" class="comment-tools"></div><div class="clear"></div><div id="comment-39358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39364"></span>

<div id="answer-container-39364" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39364-score" class="post-score" title="current number of votes">0</div><span id="post-39364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you build the deb package as well and installed that? The <code>install</code> target just installs a local copy of Wireshark (hence /usr/local/bin), while the installation of the full package takes care of the steps to properly integrate the application with the rest of the desktop environment. There's also the <code>install-desktop-files</code> target at least tries to copy the desktop files to the right place, but YMMV.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '15, 04:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39364" class="comments-container"></div><div id="comment-tools-39364" class="comment-tools"></div><div class="clear"></div><div id="comment-39364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

