+++
type = "question"
title = "Wireshark on osx 10.5 prompts to install X11 for osx 10.3 even though X11 already installed"
description = '''I just downloaded the latest wireshark for osx. When I try to launch it, I get a message &quot;Failed to start X11. Wireshark.app requires Apples X11, which is freely downloadable from Apples website for Panther (10.3.x) and available as an optional install from the installation DVD for Tiger (10.4.x) us...'''
date = "2010-11-24T12:14:00Z"
lastmod = "2011-04-14T15:36:00Z"
weight = 1114
keywords = [ "osx" ]
aliases = [ "/questions/1114" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on osx 10.5 prompts to install X11 for osx 10.3 even though X11 already installed](/questions/1114/wireshark-on-osx-105-prompts-to-install-x11-for-osx-103-even-though-x11-already-installed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1114-score" class="post-score" title="current number of votes">1</div><span id="post-1114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just downloaded the latest wireshark for osx.</p><p>When I try to launch it, I get a message "Failed to start X11. Wireshark.app requires Apples X11, which is freely downloadable from Apples website for Panther (10.3.x) and available as an optional install from the installation DVD for Tiger (10.4.x) users."</p><p>Then there is a button "get X11 for Panther".</p><p>I'm not using 10.3, I'm on 10.5. I also have X11 installed and use it regularly for other applications.</p><p>What is the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '10, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/9092b0de812ede484df38b2a6e93c5c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bea&#39;s gravatar image" /><p><span>bea</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bea has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Nov '10, 12:19</strong> </span></p></div></div><div id="comments-container-1114" class="comments-container"></div><div id="comment-tools-1114" class="comment-tools"></div><div class="clear"></div><div id="comment-1114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3504"></span>

<div id="answer-container-3504" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3504-score" class="post-score" title="current number of votes">0</div><span id="post-3504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm on OSX Snow Leopard (10.6.7) and had the same problem. Upgrading to the latest XQuartz release didn't help. I solved it by doing the following:</p><ul><li>Replacing the PATH entry in my ~/.MacOSX/environment.plist file with an export PATH= statment in ~/.profile.</li><li><a href="http://xquartz.macosforge.org/trac/wiki/X11-UsersFAQ#UninstallSnowLeopard">Uninstalling XQuartz</a>.</li><li>Re-installing X11 from the Snow Leopard install disk's Optional Installs.</li><li>Installing the latest OSX 10.6.7 Update Combo available on the <a href="http://support.apple.com/downloads">Apple downloads site</a>. (Merely running Software Update from the Apple menu was not enough.) This solved a png library issue that prevented Wireshark from running even after the X11 error was fixed.</li><li>Re-installing Wireshark.</li></ul><p>I'm sure I logged out and restarted in between some of those steps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '11, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/6895fa36a8420e8bd8c1bba353558e17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="foresto&#39;s gravatar image" /><p><span>foresto</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="foresto has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Apr '11, 15:38</strong> </span></p></div></div><div id="comments-container-3504" class="comments-container"></div><div id="comment-tools-3504" class="comment-tools"></div><div class="clear"></div><div id="comment-3504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

