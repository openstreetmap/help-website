+++
type = "question"
title = "View bits of packet in received order?"
description = '''Is there a way to view the bits of any generalized packet in the order of receipt? I&#x27;m running into issues understanding what bits should be where in the transmission so I&#x27;d like to see exactly what&#x27;s being sent/received and in what order. Thanks'''
date = "2016-07-28T10:20:00Z"
lastmod = "2016-07-28T13:23:00Z"
weight = 54408
keywords = [ "capture", "pcap", "binary" ]
aliases = [ "/questions/54408" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [View bits of packet in received order?](/questions/54408/view-bits-of-packet-in-received-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54408-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to view the bits of any generalized packet in the order of receipt? I'm running into issues understanding what bits should be where in the transmission so I'd like to see exactly what's being sent/received and in what order.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">capture pcap binary</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '16, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/a1033299daeadd58baa84ebb03359076?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smcfalls&#39;s gravatar image" /><p>smcfalls<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smcfalls has no accepted answers">0%</span></p></div></div><div id="comments-container-54408" class="comments-container"><span id="54410"></span><div id="comment-54410" class="comment"><div id="post-54410-score" class="comment-score"></div><div class="comment-text"><p>I don't understand your question. Could you elaborate?</p></div><div id="comment-54410-info" class="comment-info"><span class="comment-age">(28 Jul '16, 10:24)</span> cmaynard ♦♦</div></div><span id="54415"></span><div id="comment-54415" class="comment"><div id="post-54415-score" class="comment-score"></div><div class="comment-text"><p>@cmaynard I want completely un-parsed data. Before wireshark has done any manipulations at all.</p></div><div id="comment-54415-info" class="comment-info"><span class="comment-age">(28 Jul '16, 12:21)</span> smcfalls</div></div><span id="54417"></span><div id="comment-54417" class="comment"><div id="post-54417-score" class="comment-score"></div><div class="comment-text"><p>Wireshark doesn't manipulate anything. It just displays decoded information. If you don't need that, look at the hex view, it's what was found on the wire.</p></div><div id="comment-54417-info" class="comment-info"><span class="comment-age">(28 Jul '16, 12:58)</span> Jasper ♦♦</div></div><span id="54418"></span><div id="comment-54418" class="comment"><div id="post-54418-score" class="comment-score"></div><div class="comment-text"><p>@Jasper Interesting. I'm looking at BTLE packets specifically, and I know that bytes are transmitted with the least significant bit first, and the hex view does not reflect this.</p></div><div id="comment-54418-info" class="comment-info"><span class="comment-age">(28 Jul '16, 13:14)</span> smcfalls</div></div><span id="54420"></span><div id="comment-54420" class="comment"><div id="post-54420-score" class="comment-score"></div><div class="comment-text"><p>have you tried looking at the packet contents in a hex editor? It should be identical to the hex view in Wireshark</p></div><div id="comment-54420-info" class="comment-info"><span class="comment-age">(28 Jul '16, 13:19)</span> Jasper ♦♦</div></div><span id="54422"></span><div id="comment-54422" class="comment not_top_scorer"><div id="post-54422-score" class="comment-score"></div><div class="comment-text"><p>That's a different issue, not so much related to Wireshark. For each media and protocol, the order of bits in transmission is given, so the hardware and drivers assemble it into bytes the right way and send the message further or store it into file already as a sequence of bytes. Wireshark has no access to the bit order.</p></div><div id="comment-54422-info" class="comment-info"><span class="comment-age">(28 Jul '16, 13:24)</span> sindy</div></div></div><div id="comment-tools-54408" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-54408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54421"></span>

<div id="answer-container-54421" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54421-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm looking at BTLE packets specifically, and I know that bytes are transmitted with the least significant bit first, and the hex view does not reflect this.</p></blockquote><p>Wireshark runs on computers that are byte-addressed, not bit-addressed; it's bit-parallel, not bit-serial. <em>Networks</em> tend to be bit-serial, so that the notion of bit order is relevant. As memory and processors are bit-parallel, the hardware that receives bits from the wire has to assemble the bits into bytes and put those bytes into memory; that hardware puts the least significant bit of a byte into the least significant bit of a byte, as it should do.</p><p>So this isn't a function of Wireshark, or libpcap, or your OS - it's a function of the hardware. For networks in which the least significant bit is transmitted first - which includes an obscure network called "IEEE Std 802.3", sometimes also called "Ethernet" - the first transmitted bit will be at the bottom of a byte in tcpdump, Wireshark, snoop, and almost all, if not all, other network analyzers. You'll just have to live with that - just look at the bytes bottom-bit first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '16, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jul '16, 13:24</p></div></div><div id="comments-container-54421" class="comments-container"><span id="54424"></span><div id="comment-54424" class="comment"><div id="post-54424-score" class="comment-score"></div><div class="comment-text"><p>Knowing that debugging at wire level is sometimes a pain and that seeing the bit stream may help reveal e.g. some synchronisation issues, I'd replace @Guy Harris' suggestion to "learn to live with that" by a suggestion to use a script which you would feed with the exported data and it would convert it into a binary dump, maybe both possible ways at once, such as</p><pre><code>c7 45 19
MSB first: 11000111 01000101 00011001
LSB first: 11100011 10100010 10011000</code></pre></div><div id="comment-54424-info" class="comment-info"><span class="comment-age">(28 Jul '16, 13:35)</span> sindy</div></div><span id="54425"></span><div id="comment-54425" class="comment"><div id="post-54425-score" class="comment-score"></div><div class="comment-text"><p>Another possibility would be to enhance Wireshark so that the raw data pane has three display modes for the binary data - as bytes, as bits with the high-order bit first, as bits with the low-order bit first.</p></div><div id="comment-54425-info" class="comment-info"><span class="comment-age">(28 Jul '16, 13:58)</span> Guy Harris ♦♦</div></div><span id="54436"></span><div id="comment-54436" class="comment"><div id="post-54436-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris, I didn't dare to even think about such possibility :-) But as you've come with it yourself, should I file an enhancement at Bugzilla? As the bit order on the wire is unambiguously defined for all encapsulations related to physical interface type (Ethernet, HDLC-based protocols), it'd be fine to augment the parameter set of each encapsulation with that information and have it visualised in the mode switch of the raw data pane.</p></div><div id="comment-54436-info" class="comment-info"><span class="comment-age">(29 Jul '16, 02:28)</span> sindy</div></div><span id="54439"></span><div id="comment-54439" class="comment"><div id="post-54439-score" class="comment-score"></div><div class="comment-text"><p>A bitstream view, which would allow you to show bit masks in the bitstream as well?</p></div><div id="comment-54439-info" class="comment-info"><span class="comment-age">(29 Jul '16, 04:44)</span> Jaap ♦</div></div></div><div id="comment-tools-54421" class="comment-tools"></div><div class="clear"></div><div id="comment-54421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54416"></span>

<div id="answer-container-54416" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54416-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't want Wireshark analyzing packets, you can disable all the protocol dissectors via: <code>Analyze -&gt; Enabled Protocols... -&gt; Disable All -&gt; OK</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '16, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54416" class="comments-container"><span id="54419"></span><div id="comment-54419" class="comment"><div id="post-54419-score" class="comment-score"></div><div class="comment-text"><p>I'll look into that, thank you. Edit: Helpful, but it doesn't show the actual order of receipt, with least significant bit first. I'm beginning to suspect that the problem is my capture device.</p></div><div id="comment-54419-info" class="comment-info"><span class="comment-age">(28 Jul '16, 13:14)</span> smcfalls</div></div><span id="54423"></span><div id="comment-54423" class="comment"><div id="post-54423-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm looking at BTLE packets specifically, and I know that bytes are transmitted with the least significant bit first, and the hex view does not reflect this.</p></blockquote><p>Now that you added that comment, it helps makes things clearer, and so I think <a href="https://ask.wireshark.org/users/79/guy-harris">Guy Harris</a>'s answer is the one you're looking for.</p></div><div id="comment-54423-info" class="comment-info"><span class="comment-age">(28 Jul '16, 13:30)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-54416" class="comment-tools"></div><div class="clear"></div><div id="comment-54416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

