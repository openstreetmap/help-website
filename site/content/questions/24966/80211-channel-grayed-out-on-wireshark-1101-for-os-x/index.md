+++
type = "question"
title = "802.11 Channel grayed out on Wireshark 1.10.1 for OS X"
description = '''I&#x27;m trying to do WiFi capture on my Mac, but I can&#x27;t seem to select the channel I want to capture on. The 802.11 Channel, Channel Offset, FCS Filter, and Wireless Settings are all grayed out. Here is my configuration:  Wireshark 1.10.1 (SVN Rev 50926) OS X 10.8.5  Capture Options:  Link-layer header...'''
date = "2013-09-19T12:32:00Z"
lastmod = "2013-09-19T21:20:00Z"
weight = 24966
keywords = [ "osx", "mac", "802.11" ]
aliases = [ "/questions/24966" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [802.11 Channel grayed out on Wireshark 1.10.1 for OS X](/questions/24966/80211-channel-grayed-out-on-wireshark-1101-for-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24966-score" class="post-score" title="current number of votes">0</div><span id="post-24966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to do WiFi capture on my Mac, but I can't seem to select the channel I want to capture on. The 802.11 Channel, Channel Offset, FCS Filter, and Wireless Settings are all grayed out. Here is my configuration:</p><ul><li>Wireshark 1.10.1 (SVN Rev 50926)</li><li>OS X 10.8.5</li></ul><p>Capture Options:</p><ul><li>Link-layer header type: 802.11 plus radiotap header</li><li>Promiscuous mode: enabled</li><li>Monitor mode: enabled</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '13, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/24fad929236ae147d8ccfb56847888ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elin05&#39;s gravatar image" /><p><span>elin05</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elin05 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '13, 13:15</strong> </span></p></div></div><div id="comments-container-24966" class="comments-container"><span id="24968"></span><div id="comment-24968" class="comment"><div id="post-24968-score" class="comment-score"></div><div class="comment-text"><p>Can you show us what is the output of <code>wireshark -D</code> command given from you terminal.</p><p>BTW: can you run wireshark from terminal <code>wireshark</code> and see if you see any error on the terminal after wireshark window is opened.</p></div><div id="comment-24968-info" class="comment-info"><span class="comment-age">(19 Sep '13, 12:52)</span> <span class="comment-user userinfo">Edmond</span></div></div><span id="24969"></span><div id="comment-24969" class="comment"><div id="post-24969-score" class="comment-score"></div><div class="comment-text"><p>I always run it from the OS GUI. I get "command not found" when typing "wireshark" in the Terminal.</p></div><div id="comment-24969-info" class="comment-info"><span class="comment-age">(19 Sep '13, 13:03)</span> <span class="comment-user userinfo">elin05</span></div></div><span id="24975"></span><div id="comment-24975" class="comment"><div id="post-24975-score" class="comment-score"></div><div class="comment-text"><p>It looks strange. I've installed it from .dmg and have the same OS version you have and:</p><p><code>XQuartz 2.7.4 (xorg-server 1.13.0)</code></p><p><code>wireshark 1.10.1 (SVN Rev 50926 from /trunk-1.10)</code></p><p>My which command gives me this path for wireshark</p><p><code>/usr/local/bin/wireshark</code></p><p>Give it a try to see what logs do you get on terminal. If your wireshark is not even in that path and you can't find where it is, check system logs</p><p><code>tail -f /var/log/system.log</code></p><p>and open <code>wireshark</code> from GUI.</p><p>What type of installation did you do? Is it possible to reinstall it again? When you mount the .dmg image you will see a <code>Read me first.rtf</code>. Try reading it if you want to uninstall your current wireshark installation.</p><p>Let us know.</p></div><div id="comment-24975-info" class="comment-info"><span class="comment-age">(19 Sep '13, 15:35)</span> <span class="comment-user userinfo">Edmond</span></div></div></div><div id="comment-tools-24966" class="comment-tools"></div><div class="clear"></div><div id="comment-24966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24979"></span>

<div id="answer-container-24979" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24979-score" class="post-score" title="current number of votes">1</div><span id="post-24979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="elin05 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm trying to do WiFi capture on my Mac, but I can't seem to select the channel I want to capture on.</p></blockquote><p>That's because Wireshark doesn't include any code to support using, for example, the <a href="https://developer.apple.com/library/mac/documentation/Networking/Reference/CoreWLANFrameworkRef/_index.html">CoreWLAN framework</a> to control the channel for AirPort devices, as nobody's written that code.</p><p>The fact that those options are there at all is arguably a bug; they shouldn't be there on OS X unless and until Wireshark supports them on OS X.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '13, 21:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24979" class="comments-container"></div><div id="comment-tools-24979" class="comment-tools"></div><div class="clear"></div><div id="comment-24979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

