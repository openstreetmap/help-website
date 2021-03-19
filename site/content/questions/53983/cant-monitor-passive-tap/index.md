+++
type = "question"
title = "Can&#x27;t monitor passive tap"
description = '''Windows 10 laptop with current version of Wireshark allows me to monitor passive tap traffic on built-in port but not USB network adapter. I can monitor traffic on USB network adapter only when that adapter is getting normal network traffic, so not from the passive tap.  I have tried Win10pcap as we...'''
date = "2016-07-11T08:42:00Z"
lastmod = "2016-07-13T12:50:00Z"
weight = 53983
keywords = [ "passive", "windows", "taps", "tap", "usb" ]
aliases = [ "/questions/53983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't monitor passive tap](/questions/53983/cant-monitor-passive-tap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53983-score" class="post-score" title="current number of votes">0</div><span id="post-53983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Windows 10 laptop with current version of Wireshark allows me to monitor passive tap traffic on built-in port but not USB network adapter. I can monitor traffic on USB network adapter only when that adapter is getting normal network traffic, so not from the passive tap.<br />
</p><p>I have tried Win10pcap as well as WinPCap, I have tried various settings.<br />
</p><p>When I'm using the Windows network connections control panel (even with Wireshark not running), I see the built-in network interface (connected to one of the passive taps) alternating in status from Enabled to Network Connection Unplugged, etc., and Wireshark shows activity on that interface. But the USB network adapter just sits at the "Network Connection Unplugged" status. From that, I infer that the problem is before Wireshark.<br />
</p><p>Note that I've used multiple USB network adapters with the same result, and that all of them work fine for connecting to a normal network, just not for a passive tap.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-passive" rel="tag" title="see questions tagged &#39;passive&#39;">passive</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-taps" rel="tag" title="see questions tagged &#39;taps&#39;">taps</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '16, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/7ae0895fe90f9097fba5cd1d9ad2d7b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wnstrickland&#39;s gravatar image" /><p><span>wnstrickland</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wnstrickland has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jul '16, 09:05</strong> </span></p></div></div><div id="comments-container-53983" class="comments-container"></div><div id="comment-tools-53983" class="comment-tools"></div><div class="clear"></div><div id="comment-53983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54010"></span>

<div id="answer-container-54010" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54010-score" class="post-score" title="current number of votes">0</div><span id="post-54010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would assume that the "passive tap" is so much passive that it only feeds the Rx direction of the port, so if the network card (regardless whether it is connected to the system bus or using USB) is configured for speed and duplex negotiation, it cannot get past the negotiation phase because no negotiation phase ever happens.</p><p>So you'll have to dive into the network card settings and try to set a fixed speed of the card (of course one matching the speed of the monitored connection) and disable negotiation. This is vendor specific so it may not be possible in your case. Plus some vendors support a single setting (auto-negotiation or a choice of a fixed speed/duplex combination which disables negotiation) and some control negotiation and speed/duplex settings separately (meaning that if you set fixed speed and duplex values, they still can be indicated to the connected equipment using the negotiation process, except that no others will be suggested/accepted).</p><p>My Win10 are not in English so I cannot give you the exact path names, but you'd start by opening the "Network connections and sharing center", choose "change adaptor settings" at the left of it, right-click on the adaptor in question in the list and choose "properties", and click the "configure" button at the upper right corner of the window that opens. This opens another window, and your luck is waiting at the leftmost but one tab. There is a list of various settings and one or two of these may do what you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '16, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jul '16, 12:04</strong> </span></p></div></div><div id="comments-container-54010" class="comments-container"><span id="54045"></span><div id="comment-54045" class="comment"><div id="post-54045-score" class="comment-score"></div><div class="comment-text"><p>I can find that. Thanks for the suggestion, sindy -- I'll give it a try.<br />
There are so many settings I couldn't try every possibility!</p></div><div id="comment-54045-info" class="comment-info"><span class="comment-age">(13 Jul '16, 12:50)</span> <span class="comment-user userinfo">wnstrickland</span></div></div></div><div id="comment-tools-54010" class="comment-tools"></div><div class="clear"></div><div id="comment-54010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

