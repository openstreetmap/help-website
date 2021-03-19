+++
type = "question"
title = "&quot;Capture session could not be initiated&quot;, but then it can be"
description = '''I&#x27;m using wireshark 1.6.7 on Linux Mint 13 &quot;Maya&quot; Xfce on an old Dell 23 bit PC. The Wifi harward is a Linksys USB Wifi adapter (WUSB600N). First, I run airmon-ng in a terminal session to create the mon0 device that is in monitor mode. Then I run wireshark (not as root because I set unix capabilitie...'''
date = "2012-11-20T22:09:00Z"
lastmod = "2012-11-22T19:25:00Z"
weight = 16139
keywords = [ "captureerror", "capture", "monitor", "capture-setup" ]
aliases = [ "/questions/16139" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["Capture session could not be initiated", but then it can be](/questions/16139/capture-session-could-not-be-initiated-but-then-it-can-be)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16139-score" class="post-score" title="current number of votes">0</div><span id="post-16139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using wireshark 1.6.7 on Linux Mint 13 "Maya" Xfce on an old Dell 23 bit PC. The Wifi harward is a Linksys USB Wifi adapter (WUSB600N).</p><p>First, I run airmon-ng in a terminal session to create the mon0 device that is in monitor mode. Then I run wireshark (not as root because I set unix capabilities for dumpcap).</p><p>If I try to start a capture by clicking on mon0 in the "Start Capture on interface" list on the home "page" of wireshark, I get the dialog box saying "Capture session could not be initiated (That device doesn't support monitor mode). Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified." Then I click OK to get rid of the message.</p><p>Next, I click on the "Interface List" button or text and the dynamic "Wireshark: Capture Interfaces" dialog box pops up. If I click on the Start button for mon0, I get the same error message and click OK.</p><p>Next, I click on the Options button (to the right of the Start button) for mon0 in the same dialog box. This time something strange happens. A different error box appears saying "The capabilities of the capture device 'mon0' could not be obtained (That device doesn't support monitor mode). Please check..." But the error box is immediately covered by the "Wireshark: Capture Options" dialog box (CO box). If I move the CO box and click OK on the error box to get rid of it and then click Start on the CO box, Voila! The capture starts! And yes, it is indeed a monitor-style capture (ie I can see all 802.11 packets).</p><p>When I first configured and ran wireshark, I didn't have this problem. But the very first time I exited and restarted wireshark, the problem began.</p><p>Why am I getting the "Capture session could not be initiated" error message, when clearly it CAN BE initiated, albeit in a roundabout way (ie only using the Start button on the Capture Options dialog)?</p><p>Note that it doesn't matter whether the promiscuous mode radio button in the CO box is checked or not, and of course when I try to check the monitor mode radio button, I get the error message that it can't be set, so the monitor mode radio button remains blank.</p><p>Any help on how to eliminate this annoying behavior from an otherwise great experience with wireshark would be greatly appreciated. Thanks!</p><p>-- Nick</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-captureerror" rel="tag" title="see questions tagged &#39;captureerror&#39;">captureerror</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-capture-setup" rel="tag" title="see questions tagged &#39;capture-setup&#39;">capture-setup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '12, 22:09</strong></p><img src="https://secure.gravatar.com/avatar/3f79c4d3a7e2262fee930a8af3abb5cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ironick&#39;s gravatar image" /><p><span>ironick</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ironick has no accepted answers">0%</span></p></div></div><div id="comments-container-16139" class="comments-container"></div><div id="comment-tools-16139" class="comment-tools"></div><div class="clear"></div><div id="comment-16139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16220"></span>

<div id="answer-container-16220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16220-score" class="post-score" title="current number of votes">0</div><span id="post-16220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Don't bother checking the monitor mode box (and un-check it if it's checked) if you're capturing on a monitor-mode device. If you do, Wireshark tries to use the libpcap APIs for turning monitor mode on, and those APIs don't work well with mac80211 devices, <em>even on monitor-mode interfaces</em>, if libpcap isn't built with libnl, and on Debian and derivatives such as Ubuntu and Mint, it's not built with libnl. If that's not checked, Wireshark will just try to do a regular capture, which will capture in monitor mode in that device.</p><p>I suspect the same would apply to tcpdump, dumpcap, and TShark when using the -I command-line flag to request monitor mode.</p><p>This needs to be fixed by changing libpcap to directly talk to netlink sockets rather than using the ever-changing libnl library (where "changing" means "changing in ways that change the API"); the Debian folks are loath to build libpcap with libnl due to the fact that there are, as of now, 3 different incompatible versions of libnl.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '12, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16220" class="comments-container"><span id="16229"></span><div id="comment-16229" class="comment"><div id="post-16229-score" class="comment-score"></div><div class="comment-text"><p>As I tried to make clear in my description, I was never able to check the monitor mode box.</p></div><div id="comment-16229-info" class="comment-info"><span class="comment-age">(22 Nov '12, 19:25)</span> <span class="comment-user userinfo">ironick</span></div></div></div><div id="comment-tools-16220" class="comment-tools"></div><div class="clear"></div><div id="comment-16220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

