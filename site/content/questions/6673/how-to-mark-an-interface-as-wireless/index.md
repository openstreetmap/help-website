+++
type = "question"
title = "How to mark an interface as wireless?"
description = '''Hello, my Intel 3945ABG adapter running the 10.5.1.75-driver is not shown as wireless, so I can&#x27;t set any channels or wireless settings. Promiscous mode works fine, I see a lot of packets from other computers in my WLAN.  Is there any way to tell Wireshark that this is a wireless card? Thx in advanc...'''
date = "2011-10-01T06:10:00Z"
lastmod = "2011-10-01T12:45:00Z"
weight = 6673
keywords = [ "interface" ]
aliases = [ "/questions/6673" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to mark an interface as wireless?](/questions/6673/how-to-mark-an-interface-as-wireless)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6673-score" class="post-score" title="current number of votes">0</div><span id="post-6673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>my Intel 3945ABG adapter running the 10.5.1.75-driver is not shown as wireless, so I can't set any channels or wireless settings. Promiscous mode works fine, I see a lot of packets from other computers in my WLAN. Is there any way to tell Wireshark that this is a wireless card?</p><p>Thx in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '11, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/c0de55ca8bbf7c854816a60adb301343?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flash007&#39;s gravatar image" /><p><span>flash007</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flash007 has no accepted answers">0%</span></p></div></div><div id="comments-container-6673" class="comments-container"></div><div id="comment-tools-6673" class="comment-tools"></div><div class="clear"></div><div id="comment-6673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6677"></span>

<div id="answer-container-6677" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6677-score" class="post-score" title="current number of votes">2</div><span id="post-6677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flash007 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No. Wireshark does not itself include any code to talk to individual network adapters; it relies on the OS's drivers and on its mechanisms for doing captures on network adapters (or, on Windows, on the OS's NDIS mechanism and WinPcap's code that plugs into NDIS to capture traffic), so it has to rely on the OS to provide capture support, including anything special for wireless adapters.</p><p>On Windows, support for capturing on wireless interfaces is very limited; it does not include setting channels, for example. Even the less-limited support on some UN<em>Xes (Linux,</em> BSD, Mac OS X) does not support setting channels inside Wireshark; the only Wi-Fi adapters on which you can set the channel inside Wireshark are AirPcap adapters, which have their own special driver with which Wireshark communicates.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '11, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6677" class="comments-container"></div><div id="comment-tools-6677" class="comment-tools"></div><div class="clear"></div><div id="comment-6677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

