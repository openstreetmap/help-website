+++
type = "question"
title = "Can not capture tcp packets (rt2800usb driver)"
description = '''Hi everybody I am using Alfa AWUS036H usb Wifi device with Arch Linux (kernel 4.3.3) to capture wifi traffic. I have setup an open access point which should be easy to sniff. I tried for many days but couldn&#x27;t catch any tcp data. There were numerous protocols like 802.11 broadcasts, NBNS, UDP, ICMPv...'''
date = "2016-01-10T10:30:00Z"
lastmod = "2016-01-13T05:12:00Z"
weight = 49055
keywords = [ "wifi", "driver", "tcp" ]
aliases = [ "/questions/49055" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can not capture tcp packets (rt2800usb driver)](/questions/49055/can-not-capture-tcp-packets-rt2800usb-driver)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49055-score" class="post-score" title="current number of votes">0</div><span id="post-49055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody</p><p>I am using Alfa AWUS036H usb Wifi device with Arch Linux (kernel 4.3.3) to capture wifi traffic. I have setup an open access point which should be easy to sniff. I tried for many days but couldn't catch any tcp data. There were numerous protocols like 802.11 broadcasts, NBNS, UDP, ICMPv6, ARP, SSDP, LLMNR etc but no tcp.</p><p>Then I booted a live kali cd and <em>repeated the same procedure exactly</em>. This time everything worked fine and there was plentiful tcp traffic.</p><p>My question is: While both Arch and Kali systems are using the same driver (rt2800usb), why can't I capture tcp on Arch?</p><p>Regards</p><hr /><hr /><p>edit:</p><p>Just tested everything once again. Both Kali and Arch are using version 2.3.0 of rt2800usb driver. I put the device in monitor mode using 'airmon-ng start wlan0'. Then start capturing data using 'airodump-ng wlan0mon' so I start seeing info about nearby access points. At this stage I start data capture on Wireshark. Here onwards, Kali gives loads of tcp data but Arch doesn't capture a single tcp packet.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-driver" rel="tag" title="see questions tagged &#39;driver&#39;">driver</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '16, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/2a1ab09c008a17322d2abaae18a5863f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fulcrumm&#39;s gravatar image" /><p><span>fulcrumm</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fulcrumm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jan '16, 14:48</strong> </span></p></div></div><div id="comments-container-49055" class="comments-container"></div><div id="comment-tools-49055" class="comment-tools"></div><div class="clear"></div><div id="comment-49055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49060"></span>

<div id="answer-container-49060" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49060-score" class="post-score" title="current number of votes">0</div><span id="post-49060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My question is: While both Arch and Kali systems are using the same driver (rt2800usb), why can't I capture tcp on Arch?</p></blockquote><p>if you <strong>really (really)</strong> repeated the <strong>EXACT same procedure</strong> on both systems, the only logical answer would be: The <strong>driver version</strong> in Arch Linux and Kali is different and that's the reason why it fails on Arch and works on Kali.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '16, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-49060" class="comments-container"><span id="49065"></span><div id="comment-49065" class="comment"><div id="post-49065-score" class="comment-score"></div><div class="comment-text"><p>Please see the updated post.</p></div><div id="comment-49065-info" class="comment-info"><span class="comment-age">(10 Jan '16, 14:48)</span> <span class="comment-user userinfo">fulcrumm</span></div></div><span id="49087"></span><div id="comment-49087" class="comment"><div id="post-49087-score" class="comment-score"></div><div class="comment-text"><p>O.K. then maybe different versions of <strong>libpcap</strong>, <strong>Wireshark</strong> or even <strong>airodump-ng</strong>?</p></div><div id="comment-49087-info" class="comment-info"><span class="comment-age">(11 Jan '16, 08:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="49165"></span><div id="comment-49165" class="comment"><div id="post-49165-score" class="comment-score"></div><div class="comment-text"><p>Yes, Kali and Arch were using different versions of all these software. It took hours but I was finally able to install the same versions on Arch as those on Kali (libpcap 1.6.2, aircrack-ng 1:1.2-2-rc2, wireshark 1.12.6). Still no luck capturing any TCP.</p></div><div id="comment-49165-info" class="comment-info"><span class="comment-age">(13 Jan '16, 05:07)</span> <span class="comment-user userinfo">fulcrumm</span></div></div><span id="49166"></span><div id="comment-49166" class="comment"><div id="post-49166-score" class="comment-score"></div><div class="comment-text"><p>O.K. one last thing. Can you please check TCP offloading in both kernels?</p><blockquote><p>ethtool -k</p></blockquote><p>is there any difference that could explain the behaviour?</p></div><div id="comment-49166-info" class="comment-info"><span class="comment-age">(13 Jan '16, 05:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-49060" class="comment-tools"></div><div class="clear"></div><div id="comment-49060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

