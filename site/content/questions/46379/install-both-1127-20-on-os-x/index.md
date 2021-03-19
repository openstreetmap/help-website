+++
type = "question"
title = "Install both 1.12.7 &amp; 2.0 on OS X"
description = '''How can I install 2 different versions on OS X? By default, the installation happens in /Applications/Wireshark. I tried to rename the bundle to Wireshark_2.0.0 and install 1.12.7, but nothing appears: No new Wireshark app'''
date = "2015-10-06T05:01:00Z"
lastmod = "2015-10-09T06:29:00Z"
weight = 46379
keywords = [ "osx", "installation" ]
aliases = [ "/questions/46379" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Install both 1.12.7 & 2.0 on OS X](/questions/46379/install-both-1127-20-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46379-score" class="post-score" title="current number of votes">0</div><span id="post-46379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I install 2 different versions on OS X? By default, the installation happens in /Applications/Wireshark.</p><p>I tried to rename the bundle to Wireshark_2.0.0 and install 1.12.7, but nothing appears: No new Wireshark app</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '15, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-46379" class="comments-container"></div><div id="comment-tools-46379" class="comment-tools"></div><div class="clear"></div><div id="comment-46379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46406"></span>

<div id="answer-container-46406" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46406-score" class="post-score" title="current number of votes">1</div><span id="post-46406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TomLaBaude has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm pretty sure the package installer uses Wireshark's bundle identifier (<a href="https://developer.apple.com/library/mac/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html">CFBundleIdentifier</a>) to locate the application bundle. This is convenient because you can move the Wireshark.app directory around and rename it. It's not so convenient because no matter where Wireshark.app is or what it's called, the installer will track it down.</p><p>You should be able to work around this by doing something like the following:</p><ol><li>Install version X</li><li>Rename /Applications/Wireshark.app to /Applications/Wireshark X.app</li><li>Zip up /Applications/Wireshark X.app</li><li>Remove /Applications/Wireshark X.app</li><li>Install version Y</li><li>(Optional) Rename /Applications/Wireshark.app to /Applications/Wireshark Y.app</li><li>Unzip Wireshark X.app.</li></ol><p>Note that upgrading from here gets tricky since you now have two apps with the same bundle identifier. In the long term we should probably make Wireshark a drag-installer like most other OS X applications.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '15, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-46406" class="comments-container"><span id="46432"></span><div id="comment-46432" class="comment"><div id="post-46432-score" class="comment-score"></div><div class="comment-text"><p>Works like a charm, thanks Gerald!</p></div><div id="comment-46432-info" class="comment-info"><span class="comment-age">(09 Oct '15, 06:29)</span> <span class="comment-user userinfo">TomLaBaude</span></div></div></div><div id="comment-tools-46406" class="comment-tools"></div><div class="clear"></div><div id="comment-46406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

