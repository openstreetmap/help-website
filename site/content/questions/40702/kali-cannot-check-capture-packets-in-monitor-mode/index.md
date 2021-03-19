+++
type = "question"
title = "Kali cannot check &quot;Capture packets in monitor mode&quot;"
description = '''I am running Kali and the &quot;Capture packets in monitor mode&quot; for eth1 is grayed out. what do I do?'''
date = "2015-03-19T16:21:00Z"
lastmod = "2015-03-20T01:10:00Z"
weight = 40702
keywords = [ "ethernet", "monitor", "linux" ]
aliases = [ "/questions/40702" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Kali cannot check "Capture packets in monitor mode"](/questions/40702/kali-cannot-check-capture-packets-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40702-score" class="post-score" title="current number of votes">0</div><span id="post-40702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Kali and the "Capture packets in monitor mode" for eth1 is grayed out. what do I do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '15, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/e5bc2d4abb366dbb3545211bdec75b42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BryMasters01&#39;s gravatar image" /><p><span>BryMasters01</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BryMasters01 has no accepted answers">0%</span></p></div></div><div id="comments-container-40702" class="comments-container"></div><div id="comment-tools-40702" class="comment-tools"></div><div class="clear"></div><div id="comment-40702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40709"></span>

<div id="answer-container-40709" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40709-score" class="post-score" title="current number of votes">0</div><span id="post-40709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Install aircrack-ng, run airmon-ng on eth1, and then capture on whatever device that script says to. See <a href="https://wiki.wireshark.org/CaptureSetup/WLAN?highlight=%28airmon-ng%29#Linux">the section on Linux monitor mode in the Wireshark Wiki page on capturing on WLAN interfaces</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '15, 23:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40709" class="comments-container"></div><div id="comment-tools-40709" class="comment-tools"></div><div class="clear"></div><div id="comment-40709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40713"></span>

<div id="answer-container-40713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40713-score" class="post-score" title="current number of votes">0</div><span id="post-40713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't believe that eth1 is your wireless interface. First you have to put the interface in monitor mode using iwconfig or airmon-ng. Then depending on what you used you will select wlan0 or mon0 in Wireshark. If it doesn't work make sure you are using the right chipset/drivers. Some don't support monitor mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '15, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-40713" class="comments-container"></div><div id="comment-tools-40713" class="comment-tools"></div><div class="clear"></div><div id="comment-40713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

