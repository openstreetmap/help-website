+++
type = "question"
title = "Decode IP within USB?"
description = '''How to decode IP within USB datastream? Scenario: Cradlepoint MBR900 switch/router with USB port, with Verizon 3G data dongle providing Wireless data network access. I want to see the traffic between the MBR900 and the dongle. I suspect a USB TAP/Splitter will be needed so the Tx/Rx is split to the ...'''
date = "2014-12-09T09:52:00Z"
lastmod = "2014-12-10T18:23:00Z"
weight = 38498
keywords = [ "ip", "usb" ]
aliases = [ "/questions/38498" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Decode IP within USB?](/questions/38498/decode-ip-within-usb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38498-score" class="post-score" title="current number of votes">0</div><span id="post-38498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to decode IP within USB datastream?</p><p>Scenario: Cradlepoint MBR900 switch/router with USB port, with Verizon 3G data dongle providing Wireless data network access.</p><p>I want to see the traffic between the MBR900 and the dongle. I suspect a USB TAP/Splitter will be needed so the Tx/Rx is split to the RX of two separate USB ports on my capture host.</p><p>Then the two received streams will need to be merged into a single capture file.</p><p>Then is it possible to decode USB as the underlying protocol like Ethernet is decoded, with IP on top of that?</p><p>Possible? I've not found a method yet, and my search-fu seems to be lacking today...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '14, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/3c76e8578fbf2b0be0f712daec76e0ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="intermediateWireshark&#39;s gravatar image" /><p><span>intermediate...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="intermediateWireshark has no accepted answers">0%</span></p></div></div><div id="comments-container-38498" class="comments-container"><span id="38519"></span><div id="comment-38519" class="comment"><div id="post-38519-score" class="comment-score"></div><div class="comment-text"><p>For those unfamiliar with the <a href="https://cradlepoint.com/sites/default/files/productdocs/CradlePoint_MBR900_QSG_sm.pdf">CradlePoint MBR900</a>, it's a Wi-Fi router that can either take an Ethernet cable to a cable modem/DSL modem/fibre whatever <em>or</em> a mobile-phone-network adapter plugged into a USB port as its Internet connection.</p></div><div id="comment-38519-info" class="comment-info"><span class="comment-age">(10 Dec '14, 18:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-38498" class="comment-tools"></div><div class="clear"></div><div id="comment-38498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="38499"></span>

<div id="answer-container-38499" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38499-score" class="post-score" title="current number of votes">1</div><span id="post-38499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, it's possible to capture USB packet with usbmon (on Linux) or USPpcap (on Windows). Then depending on the USB dongle enumeration (will it be CDC-ECM, NCM, MBIM?) Wireshark 1.12.2 might be able to decode decode the encapsulated Ethernet / IP packets.</p><p>Note that so as to get the best USB dissection as possible, it is highly recommended to plug the dongle after starting usbmon / USBPcap so that USB enumeration is part of the capture (this way Wireshark knows which endpoint corresponds to what).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '14, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Dec '14, 10:12</strong> </span></p></div></div><div id="comments-container-38499" class="comments-container"><span id="38500"></span><div id="comment-38500" class="comment"><div id="post-38500-score" class="comment-score"></div><div class="comment-text"><p>See also: <a href="http://wiki.wireshark.org/CaptureSetup/USB">http://wiki.wireshark.org/CaptureSetup/USB</a></p></div><div id="comment-38500-info" class="comment-info"><span class="comment-age">(09 Dec '14, 10:24)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-38499" class="comment-tools"></div><div class="clear"></div><div id="comment-38499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38501"></span>

<div id="answer-container-38501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38501-score" class="post-score" title="current number of votes">0</div><span id="post-38501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't have login access to the Cradlepoint, then you may need to purchase a USB analyzer. There are several products available. The following short list is just a small sample of some of them and not meant to be an endorsement of any particular vendor or product:</p><ul><li><a href="http://www.totalphase.com/products/usbguide/">TotalPhase USB Analyzers</a></li><li><a href="http://www.fte.com/products/FTS4USB-CPAS.aspx">Frontline Test Equipment's ComProbe USB 2.0 Protocol Analyzer - FTS4USB(TM)</a></li></ul><p>A related question: <a href="https://ask.wireshark.org/questions/28310/hardware-for-capture-usb-data-packet">https://ask.wireshark.org/questions/28310/hardware-for-capture-usb-data-packet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '14, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-38501" class="comments-container"><span id="38503"></span><div id="comment-38503" class="comment"><div id="post-38503-score" class="comment-score"></div><div class="comment-text"><p>I do have management access to the MBR900, but it's a pretty limited device. I'm attempting to determine if the MBR900 or Verizon is blocking non-passive FTP traffic (I think it's Verizon, actually). Thanks for the links, I'll check them out.</p></div><div id="comment-38503-info" class="comment-info"><span class="comment-age">(09 Dec '14, 11:47)</span> <span class="comment-user userinfo">intermediate...</span></div></div></div><div id="comment-tools-38501" class="comment-tools"></div><div class="clear"></div><div id="comment-38501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38510"></span>

<div id="answer-container-38510" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38510-score" class="post-score" title="current number of votes">0</div><span id="post-38510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi</p><p>I don't think you need USB Analyzer.</p><p>All you need is openwrt distro loaded onto your router and you'll be able to run tcpdump and extract IP data straight out of the box.</p><p>Regards</p><p>m</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '14, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-38510" class="comments-container"><span id="38511"></span><div id="comment-38511" class="comment"><div id="post-38511-score" class="comment-score"></div><div class="comment-text"><p>OpenWRT would maybe an option if CRADLEPOINT were supported.</p></div><div id="comment-38511-info" class="comment-info"><span class="comment-age">(10 Dec '14, 09:25)</span> <span class="comment-user userinfo">intermediate...</span></div></div></div><div id="comment-tools-38510" class="comment-tools"></div><div class="clear"></div><div id="comment-38510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

