+++
type = "question"
title = "Scan / Capture NetBIOS traffic from a particular IP and or Range"
description = '''Hi, new to Wireshark and eager to learn more about it,but I got into it for a specific reason. Trying to learn on my feet but so much to take in, so I thought I would ask the experts for some help and guidance. First Part. I am wanting to monitor a particular IP address on our network for NetBIOS tr...'''
date = "2016-05-27T23:59:00Z"
lastmod = "2016-05-28T13:29:00Z"
weight = 53022
keywords = [ "netbios" ]
aliases = [ "/questions/53022" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Scan / Capture NetBIOS traffic from a particular IP and or Range](/questions/53022/scan-capture-netbios-traffic-from-a-particular-ip-and-or-range)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53022-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, new to Wireshark and eager to learn more about it,but I got into it for a specific reason. Trying to learn on my feet but so much to take in, so I thought I would ask the experts for some help and guidance.</p><p><strong>First Part</strong>. I am wanting to monitor a particular IP address on our network for NetBIOS traffic. What would be the best filters to use for this.</p><p><strong>Second Part</strong>: Same as above but to scan a range of IP's.</p><p>I want to be able to run the scan. Then disable NetBIOS over TCP/IP. Run a second scan and show the results between the two.</p><p>Would really appreciate some guidance on this.</p><p>Thanks all</p></div><div id="question-tags" class="tags-container tags">netbios</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '16, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/9c57c5eea9c6a4ad0f6eeabe99d5516d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d95gas&#39;s gravatar image" /><p>d95gas<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="d95gas has no accepted answers">0%</span></p></div></div><div id="comments-container-53022" class="comments-container"></div><div id="comment-tools-53022" class="comment-tools"></div><div class="clear"></div><div id="comment-53022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53028"></span>

<div id="answer-container-53028" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53028-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First you need to be sure about your <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">capture setup</a> to make sure you get to see the network traffic in the first place.</p><p>Second you can apply <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html">a capture filter</a> to (in real time) filter out all IP traffic from a single IP or subnet</p><p>Up to now you limited the traffic to the relevant addresses, now you need to filter for the protocol. You can either filter on the port this traffic usually flows through (that can be used in a capture filter as well), or be used as a display filter (for limiting what's to be displayed). Since display filters have full access to the dissected protocols, these can also be for <a href="https://wiki.wireshark.org/NetBIOS/NetBIOS">the NetBIOS protocol itself</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '16, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53028" class="comments-container"><span id="53032"></span><div id="comment-53032" class="comment"><div id="post-53032-score" class="comment-score"></div><div class="comment-text"><p>And NetBIOS-over-TCP traffic will be traffic to or from ports 137, 138, and 139 - and if you also include SMB-over-TCP, that's port 445. So you can use the <code>port</code> keyword in a capture filter to limit the capture to those ports.</p></div><div id="comment-53032-info" class="comment-info"><span class="comment-age">(28 May '16, 23:46)</span> Guy Harris ♦♦</div></div><span id="53179"></span><div id="comment-53179" class="comment"><div id="post-53179-score" class="comment-score"></div><div class="comment-text"><p>Many thanks for response, exactly the information I was looking for..... I shall go away and do some more testing on my home LAN, see what interesting info I can see.</p><p>Many thanks</p></div><div id="comment-53179-info" class="comment-info"><span class="comment-age">(03 Jun '16, 08:24)</span> d95gas</div></div><span id="53181"></span><div id="comment-53181" class="comment"><div id="post-53181-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-53181-info" class="comment-info"><span class="comment-age">(03 Jun '16, 09:13)</span> Jaap ♦</div></div></div><div id="comment-tools-53028" class="comment-tools"></div><div class="clear"></div><div id="comment-53028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

