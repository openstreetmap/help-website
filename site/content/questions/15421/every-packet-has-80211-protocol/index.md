+++
type = "question"
title = "Every Packet has 802.11 Protocol"
description = '''I&#x27;m using Wireshark on Backtrack and have a Broadcom 4322 Wifi Card running in monitor mode (airmon-ng). When I&#x27;m capturing the data of an open network, all packets seem to have the same protocol: 802.11. Also, I can&#x27;t read any data in this packets. I guess that these packets actually belong to anot...'''
date = "2012-10-31T08:27:00Z"
lastmod = "2017-04-30T20:49:00Z"
weight = 15421
keywords = [ "protocol", "802.11", "monitor" ]
aliases = [ "/questions/15421" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Every Packet has 802.11 Protocol](/questions/15421/every-packet-has-80211-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15421-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Wireshark on Backtrack and have a Broadcom 4322 Wifi Card running in monitor mode (airmon-ng). When I'm capturing the data of an open network, all packets seem to have the same protocol: 802.11. Also, I can't read any data in this packets. I guess that these packets actually belong to another protocol (http, tcp,...), has anybody an idea how i can get to that data?</p></div><div id="question-tags" class="tags-container tags">protocol 802.11 monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '12, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/82c6a854f0d66dcf9b1727f4e6c49523?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="__TOXIC&#39;s gravatar image" /><p>__TOXIC<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="__TOXIC has no accepted answers">0%</span></p></div></div><div id="comments-container-15421" class="comments-container"></div><div id="comment-tools-15421" class="comment-tools"></div><div class="clear"></div><div id="comment-15421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15424"></span>

<div id="answer-container-15424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15424-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, if you're capturing in monitor mode on an 802.11 interface, obviously all packets will have 802.11 as a protocol. :-)</p><p>What's happening is presumably that they don't have any <em>higher-level</em> protocols.</p><p>Is this truly an "open" network in the sense that you don't have to supply a password to connect to it? If you have to supply a password, it's not "open" in that sense, and the packets are probably encrypted, in which case you need to <a href="http://wiki.wireshark.org/HowToDecrypt802.11">supply the password to Wireshark so that it can decrypt it</a> and, if it's a WPA or WPA2 network, rather than a WEP network, you also have to catch the initial setup packets when you connect (as that page notes).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '12, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Oct '12, 09:52</p></div></div><div id="comments-container-15424" class="comments-container"><span id="15426"></span><div id="comment-15426" class="comment"><div id="post-15426-score" class="comment-score"></div><div class="comment-text"><p>That's what I meant, I only see 802.11 and a few ARP protocol packets.</p><p>Yes it's really open, i also tryed it with an encrypted wifi and supplying the passphrase - gave me the same result.</p></div><div id="comment-15426-info" class="comment-info"><span class="comment-age">(31 Oct '12, 11:29)</span> __TOXIC</div></div><span id="15427"></span><div id="comment-15427" class="comment"><div id="post-15427-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I only see 802.11 and a few ARP protocol packets.</p></blockquote><p>OK, that's very different from "every packet has 802.11 protocol"; apparently, those ARP packets, at least, aren't encrypted.</p><p>Are the other packet 802.11 data packets or are they management or control packets?</p></div><div id="comment-15427-info" class="comment-info"><span class="comment-age">(31 Oct '12, 11:45)</span> Guy Harris ♦♦</div></div><span id="15432"></span><div id="comment-15432" class="comment"><div id="post-15432-score" class="comment-score"></div><div class="comment-text"><p>OK, I'm sorry, I'm just getting startet with networks.</p><p>They are all management/control packets, so apperently the others are missing?</p></div><div id="comment-15432-info" class="comment-info"><span class="comment-age">(31 Oct '12, 12:14)</span> __TOXIC</div></div><span id="15433"></span><div id="comment-15433" class="comment"><div id="post-15433-score" class="comment-score"></div><div class="comment-text"><p>Possibly. Is there anybody else on the network fetching stuff from the Web or playing audio/video over the Web while you're capturing? Try capturing when you know somebody's fetching something big, and see whether that traffic shows up or not.</p></div><div id="comment-15433-info" class="comment-info"><span class="comment-age">(31 Oct '12, 12:29)</span> Guy Harris ♦♦</div></div><span id="15434"></span><div id="comment-15434" class="comment"><div id="post-15434-score" class="comment-score"></div><div class="comment-text"><p>I just tried to capture while a youtube video was streaming on another pc - but wireshark didn't show anything except 802.11 and ARP.</p></div><div id="comment-15434-info" class="comment-info"><span class="comment-age">(31 Oct '12, 13:28)</span> __TOXIC</div></div><span id="15435"></span><div id="comment-15435" class="comment not_top_scorer"><div id="post-15435-score" class="comment-score"></div><div class="comment-text"><p>Are all the packets you're seeing sent to a broadcast (or multicast?) MAC address? I.e., is the DA field ff:ff:ff:ff:ff:ff (or possibly another "group" address)?</p></div><div id="comment-15435-info" class="comment-info"><span class="comment-age">(31 Oct '12, 14:23)</span> Guy Harris ♦♦</div></div><span id="15461"></span><div id="comment-15461" class="comment not_top_scorer"><div id="post-15461-score" class="comment-score"></div><div class="comment-text"><p>No, only a few of them are broadcasts - most are unicasts.</p></div><div id="comment-15461-info" class="comment-info"><span class="comment-age">(01 Nov '12, 04:25)</span> __TOXIC</div></div></div><div id="comment-tools-15424" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-15424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61132"></span>

<div id="answer-container-61132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61132-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are probably in monitor mode. When set to monitor mode, all I see are 802.11 protocol packets.</p><p>See <a href="https://ask.wireshark.org/questions/22980/wireshark-only-shows-one-protocol-in-capture">https://ask.wireshark.org/questions/22980/wireshark-only-shows-one-protocol-in-capture</a> for an in-depth discussion.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '17, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/0f7cac8d8416ca66066bae84329a4fe0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paolodm&#39;s gravatar image" /><p>paolodm<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paolodm has no accepted answers">0%</span></p></div></div><div id="comments-container-61132" class="comments-container"><span id="61133"></span><div id="comment-61133" class="comment"><div id="post-61133-score" class="comment-score"></div><div class="comment-text"><blockquote><p>When set to monitor mode, all I see are 802.11 protocol packets.</p></blockquote><p>As per my answers to this question and to the other question you pointed to, they're probably encrypted packets.</p></div><div id="comment-61133-info" class="comment-info"><span class="comment-age">(30 Apr '17, 20:58)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-61132" class="comment-tools"></div><div class="clear"></div><div id="comment-61132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

