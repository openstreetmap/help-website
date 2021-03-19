+++
type = "question"
title = "Info monitoring Bandwidth"
description = '''Hi,  i have need of monitoring Bandwidth with wireshark. I have activated the sniffing on my pc and I start to transfer the big file (1GB) on the other pc on my network. I have activated the control traffic and I&#x27;m monitoring the bandwidth in Statistics -&amp;gt; Conversation The bandwidth is 71 Mbits/s...'''
date = "2017-09-29T06:06:00Z"
lastmod = "2017-09-29T12:59:00Z"
weight = 63675
keywords = [ "bandwidth" ]
aliases = [ "/questions/63675" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Info monitoring Bandwidth](/questions/63675/info-monitoring-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63675-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i have need of monitoring Bandwidth with wireshark. I have activated the sniffing on my pc and I start to transfer the big file (1GB) on the other pc on my network. I have activated the control traffic and I'm monitoring the bandwidth in Statistics -&gt; Conversation The bandwidth is 71 Mbits/s, egual to 8,8 MByte/s, while the network NIC showed 11MByte/s. Which it is true? How Wireshark calculate the Bandwidth? Best regards Riccardo</p></div><div id="question-tags" class="tags-container tags">bandwidth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '17, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/e8830ff77184c9f7c1acb6a5c0594259?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Riccardo1987&#39;s gravatar image" /><p>Riccardo1987<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Riccardo1987 has no accepted answers">0%</span></p></div></div><div id="comments-container-63675" class="comments-container"></div><div id="comment-tools-63675" class="comment-tools"></div><div class="clear"></div><div id="comment-63675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63678"></span>

<div id="answer-container-63678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63678-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe (someone may correct me) that Wireshark is only going to be telling you the bandwidth used by the bytes it can see. So if you're capturing IP over Ethernet (a common example) Wireshark normally sees the Ethernet header, the IP header, then whatever payload you've got.</p><p>What Wireshark <strong>won't</strong> see is what the NIC didn't pass up. Sticking with the Ethernet example this means you probably didn't capture the Ethernet FCS (checksum) nor the preamble, start of frame delimiter, nor the inter-packet gap (see Wikipedia's <a href="https://en.wikipedia.org/wiki/Ethernet_frame#Structure">Ethernet frame</a> page for some details).</p><p>Your NIC, however, is probably taking all those other fields into account in its count of bytes transmitted/received which then affects the bit rate you see.</p><p>Which is true? If my theory is correct I'd say the NIC is more accurate. But I'm not sure I'd say Wireshark is wrong: it would actually be quite hard for it to know for sure that it's really looking at packets captured over Ethernet (as opposed to the many things out there that give Wireshark fake Ethernet headers and the like).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '17, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-63678" class="comments-container"><span id="63680"></span><div id="comment-63680" class="comment"><div id="post-63680-score" class="comment-score"></div><div class="comment-text"><p>Not to forget that capturing locally on a system involved in the transfer isn't usually going to give you exact numbers. For that, an independent, listen-only capture device is required, and the frame drops need to be zero.</p></div><div id="comment-63680-info" class="comment-info"><span class="comment-age">(30 Sep '17, 12:46)</span> Jasper ♦♦</div></div><span id="63684"></span><div id="comment-63684" class="comment"><div id="post-63684-score" class="comment-score"></div><div class="comment-text"><p>Hi, thank you so much. Then, if I'm monitoring bandwidth on my NIC of the firewall with wireshark, i don't consider the results completely correct, it's just?</p></div><div id="comment-63684-info" class="comment-info"><span class="comment-age">(02 Oct '17, 00:54)</span> Riccardo1987</div></div></div><div id="comment-tools-63678" class="comment-tools"></div><div class="clear"></div><div id="comment-63678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

