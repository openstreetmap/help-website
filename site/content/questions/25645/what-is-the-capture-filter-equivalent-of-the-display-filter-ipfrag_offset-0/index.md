+++
type = "question"
title = "What is the capture filter equivalent of the display filter &quot;ip.frag_offset != 0&quot;"
description = '''thank you . i have one more question.  ip.frag_offset != 0(Display filter) Converted to Capture filter syntax is ip[7]&amp;amp;0xf != 0 ? i want to know right syntax.'''
date = "2013-10-04T08:19:00Z"
lastmod = "2013-10-04T08:41:00Z"
weight = 25645
keywords = [ "capture", "capture-filter", "display-filter" ]
aliases = [ "/questions/25645" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is the capture filter equivalent of the display filter "ip.frag\_offset != 0"](/questions/25645/what-is-the-capture-filter-equivalent-of-the-display-filter-ipfrag_offset-0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25645-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>thank you . i have one more question. ip.frag_offset != 0(Display filter) Converted to Capture filter syntax is ip[7]&amp;0xf != 0 ? i want to know right syntax.</p></div><div id="question-tags" class="tags-container tags">capture capture-filter display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '13, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/37ca2e5611f06fb91521aabe9f1546ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stih&#39;s gravatar image" /><p>stih<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stih has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 04 Oct '13, 08:34</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-25645" class="comments-container"></div><div id="comment-tools-25645" class="comment-tools"></div><div class="clear"></div><div id="comment-25645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25647"></span>

<div id="answer-container-25647" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25647-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>(I converted the new question in your comment to a new question)</p><p>You need to look at the <a href="http://tools.ietf.org/html/rfc791">IP RFC</a> to find detailed information about the header structure of an IP packet:</p><pre><code>    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Version|  IHL  |Type of Service|          Total Length         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |         Identification        |Flags|      Fragment Offset    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Time to Live |    Protocol   |         Header Checksum       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                       Source Address                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Destination Address                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+</code></pre><p>As you can see, the IP fragement offset is formed by the least significant 5 bits of the 6th octet and the full 7th octet (when counting from 0) of the IP header.</p><p>So you will to get those bytes with "ip[6:2]", then mask the right bits with "ip[6:2] &amp; 0x1fff" and then compare to a value. In your case:</p><pre><code>ip[6:2] &amp; 0x1fff != 0</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25647" class="comments-container"></div><div id="comment-tools-25647" class="comment-tools"></div><div class="clear"></div><div id="comment-25647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25648"></span>

<div id="answer-container-25648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25648-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As I directed you before from <a href="http://ask.wireshark.org/questions/25504/how-to-capture-based-on-ip-header-length-using-a-capture-filter">your earlier question</a>, read the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">pcap-filter</a> man page and reference <a href="http://tools.ietf.org/html/rfc791#section-3.1">RFC 791</a> to understand the IP header fields better.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25648" class="comments-container"></div><div id="comment-tools-25648" class="comment-tools"></div><div class="clear"></div><div id="comment-25648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

