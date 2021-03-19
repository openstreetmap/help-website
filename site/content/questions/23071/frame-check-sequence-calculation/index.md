+++
type = "question"
title = "Frame check sequence calculation"
description = '''Hello, I am trying to calculate the FCS for ipv4/ipv6 packets. I use the following algorithm:  I get the hex string of the whole frame (from ethernet layer to data incapsulated inside tcp/udp) I transform it into a binary string I negate the first 32 bits I reverse the order of the bits in each byte...'''
date = "2013-07-17T06:22:00Z"
lastmod = "2013-07-17T16:05:00Z"
weight = 23071
keywords = [ "crc32", "fcs" ]
aliases = [ "/questions/23071" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Frame check sequence calculation](/questions/23071/frame-check-sequence-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23071-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to calculate the FCS for ipv4/ipv6 packets.</p><p>I use the following algorithm:</p><ol><li>I get the hex string of the whole frame (from ethernet layer to data incapsulated inside tcp/udp)</li><li>I transform it into a binary string</li><li>I negate the first 32 bits</li><li>I reverse the order of the bits in each byte in the whole frame</li><li>I xor the first 33 elements of the binary string with 100000100110000010001110110110111 and trim the left zeros</li><li>I repeat step 5 until my binary string has a length less or equal to 32</li><li>I negate all the bits</li><li>I transform the binary string into a hex string</li></ol><p>And that is my algorithm. Wireshark says it's wrong, and I'm sure he's right, but I don't know what I did wrong.</p><p>I learned about it here: <a href="http://cs.nju.edu.cn/yangxc/dcc_teach/fcs-calc.pdf">http://cs.nju.edu.cn/yangxc/dcc_teach/fcs-calc.pdf</a></p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags">crc32 fcs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '13, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/b68fad6a138a4a8e90f659020ff5b705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maio&#39;s gravatar image" /><p>Maio<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maio has no accepted answers">0%</span></p></div></div><div id="comments-container-23071" class="comments-container"></div><div id="comment-tools-23071" class="comment-tools"></div><div class="clear"></div><div id="comment-23071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23088"></span>

<div id="answer-container-23088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23088-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The PDF mentions <strong>NTCIP</strong> and <strong>AB 3418</strong>.</p><blockquote><p>Cite: <strong>NTCIP and AB 3418 protocol</strong> developers typically use the inverse polynomial method <strong>to calculate the Frame Check Sequence (FCS)</strong>.</p></blockquote><p>If you try to create an FCS for an ethernet frame with a method defined for NTCIP it may not work for one of the following reasons:</p><ul><li>either: the FCS algorithm for ethernet is different. Then that's the reason for the discrepancy.</li><li>or: the FCS algorithm defined in the PDF (for NTCIP) is the same as for ethernet (I did not check). In that case, your implementation is buggy.</li></ul><p>For a detailed information how to calculate the FCS please check the following file:</p><blockquote><p><a href="http://www.xilinx.com/support/documentation/application_notes/xapp209.pdf">http://www.xilinx.com/support/documentation/application_notes/xapp209.pdf</a></p></blockquote><p>You can also read the Wireshark source code:</p><p><strong>packet-eth.c:add_ethernet_trailer()</strong></p><pre><code>        guint32 fcs = crc32_802_tvb(tvb, tvb_length(tvb) - 4);</code></pre><p><strong>crc32-tvb.c:</strong></p><pre><code>crc32_802_tvb(tvbuff_t *tvb, guint len)
{
    guint32 c_crc;
c_crc = crc32_ccitt_tvb(tvb, len);

/* Byte reverse. */
c_crc = GUINT32_SWAP_LE_BE(c_crc);

return ( c_crc );</code></pre><p>}</p></pre><br />
<p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '13, 16:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-23088" class="comments-container"><span id="23089"></span><div id="comment-23089" class="comment"><div id="post-23089-score" class="comment-score">1</div><div class="comment-text"><p>To my great surprise, "AB" in "AB 3418" stands for "Assembly Bill", as in "California Assembly BIll 3418" (I've lived here 28 years, so I should've recognized it :-)); that bill, passed by the California state legislature specified that traffic signal controllers in California installed in 1996 or later must have a standard control protocol; the California Department of Transportation published <a href="http://www.dot.ca.gov/hq/traffops/elecsys/reports/ab3418sp.pdf">a specification for that protocol</a>, which runs over 1200 baud RS-232.</p><p>The protocol was based on a draft of a US Department of Transportation(?) standard, the "National Transportation Control/ITS Communications Protocol" - that's "NTCIP". I infer from section 4.3.2 "Data Link Layer Protocol" of the CA DOT specification that it's based on HDLC, so the CRC would presumably be the one specified for HDLC.</p><p>The 32-bit HDLC CRC and the Ethernet CRC use the same polynomial; there might be a byte-order difference, however.</p></div><div id="comment-23089-info" class="comment-info"><span class="comment-age">(17 Jul '13, 18:04)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-23088" class="comment-tools"></div><div class="clear"></div><div id="comment-23088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

