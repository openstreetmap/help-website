+++
type = "question"
title = "IPv6 Router Solicitation"
description = '''Hello everyone, Wireshark is a nice product for analyzing LAN traffic. There seems to be a hole though in ICMPv6 sniffing implementation: I cannot see anywhere the ability to filter IPv6 Router Solicitation messages.'''
date = "2013-03-22T08:08:00Z"
lastmod = "2013-06-09T18:22:00Z"
weight = 19753
keywords = [ "icmpv6", "rs" ]
aliases = [ "/questions/19753" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [IPv6 Router Solicitation](/questions/19753/ipv6-router-solicitation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19753-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>Wireshark is a nice product for analyzing LAN traffic.</p><p>There seems to be a hole though in ICMPv6 sniffing implementation: I cannot see anywhere the ability to filter IPv6 Router Solicitation messages.</p></div><div id="question-tags" class="tags-container tags">icmpv6 rs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '13, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/c86fb9accfde44bdbe661d8582c39b7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="actionmystique&#39;s gravatar image" /><p>actionmystique<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="actionmystique has no accepted answers">0%</span></p></div></div><div id="comments-container-19753" class="comments-container"></div><div id="comment-tools-19753" class="comment-tools"></div><div class="clear"></div><div id="comment-19753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="19754"></span>

<div id="answer-container-19754" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19754-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When analyzing IPv6 traffic in Wireshark, you can simply use the filter <code>icmpv6.type==133</code> to show only "Router Solicitation" messages.</p><p>When capturing, things get a little complicated. The BPF language is not yet updated to look into icmp6 headers. You can simply filter for icmp6 messages with the capture filter <code>icmp6</code>, but looking for a specific type does not work:</p><pre><code>$ tcpdump -i en0 -d icmp6[1]=133
tcpdump: IPv6 upper-layer protocol is not supported by proto[x]
$</code></pre><p>As long as there are no extension headers in the IPv6 header, you can use the filter ip6[40]=133 to capture only "Router Solicitation" messages.</p><p>To add this functionality, you can better report this at <a href="http://www.tcpdump.org/">http://www.tcpdump.org/</a>, as the bpf filter engine is implemented in libpcap/winpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '13, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '13, 08:55</p></div></div><div id="comments-container-19754" class="comments-container"><span id="19756"></span><div id="comment-19756" class="comment"><div id="post-19756-score" class="comment-score"></div><div class="comment-text"><p>Isn't the type for Router Solicitation 133? 135 is for Neighbor solicitation.</p></div><div id="comment-19756-info" class="comment-info"><span class="comment-age">(22 Mar '13, 08:34)</span> grahamb ♦</div></div><span id="19757"></span><div id="comment-19757" class="comment"><div id="post-19757-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your prompt answers.</p><p>The issue is that Router Solicitations don't even show up in the list of packets decoded by Wireshark.</p><p>I'm currently using Wireshark on a link between 2 routers in GNS3. One has an IPV6 statically configured address and is sending regular RA messages on the link. The other router has an interface configured with SLAAC, meaning it is waiting for a RA from the other router to auto-configure its IPv6 interface.</p><p>At bootup, I know the second router sends an RS to the first one since there's a 'debug ipv6 nd' on the latter. [I would like to upload a screenshot but apparently the permission is denied (errno 13)].</p><p>However no RS is shown in Wireshark, without any capture or display filter applied ...</p></div><div id="comment-19757-info" class="comment-info"><span class="comment-age">(22 Mar '13, 08:44)</span> actionmystique</div></div><span id="19758"></span><div id="comment-19758" class="comment"><div id="post-19758-score" class="comment-score"></div><div class="comment-text"><p>OOPs, my mistake. There was an display filter applied.</p><p>However, <strong>icmpv6.type == 135</strong> is <strong>Neighbor</strong> Solicitation, <strong>not Router</strong> Solicitation</p><p>icmpv6.type == 133 is correct.</p><p>Sorry!</p></div><div id="comment-19758-info" class="comment-info"><span class="comment-age">(22 Mar '13, 08:54)</span> actionmystique</div></div><span id="19759"></span><div id="comment-19759" class="comment"><div id="post-19759-score" class="comment-score"></div><div class="comment-text"><p>Thanks @Grahamb, I corrected it :-)</p></div><div id="comment-19759-info" class="comment-info"><span class="comment-age">(22 Mar '13, 08:56)</span> SYN-bit ♦♦</div></div><span id="19760"></span><div id="comment-19760" class="comment"><div id="post-19760-score" class="comment-score"></div><div class="comment-text"><p>It seems that 133 and 135 are easily confused today.</p></div><div id="comment-19760-info" class="comment-info"><span class="comment-age">(22 Mar '13, 09:11)</span> grahamb ♦</div></div></div><div id="comment-tools-19754" class="comment-tools"></div><div class="clear"></div><div id="comment-19754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19755"></span>

<div id="answer-container-19755" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19755-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I presume you're meaning a capture filter and that there no icmpv6 equivalent of <code>icmp[icmptype] == icmp-routersolicit</code>. This appears to be true, but is more an issue for the pcap and WinPCap folks rather than Wireshark.</p><p>You can use a display filter though: icmpv6.type == 133</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '13, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19755" class="comments-container"></div><div id="comment-tools-19755" class="comment-tools"></div><div class="clear"></div><div id="comment-19755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21861"></span>

<div id="answer-container-21861" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21861-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>99 125.294551000 fe80::ffff:ffff:fffe ff02::2 ICMPv6 103 Router Solicitation</p><p>100 125.331293000 fe80::8000:f227:bec8:6189 fe80::ffff:ffff:fffe ICMPv6 151 Router Advertisement</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '13, 18:22</strong></p><img src="https://secure.gravatar.com/avatar/5d68ccbe5ffd8a4f4cf106aef265a5df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris222444&#39;s gravatar image" /><p>Chris222444<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris222444 has no accepted answers">0%</span></p></div></div><div id="comments-container-21861" class="comments-container"><span id="21871"></span><div id="comment-21871" class="comment"><div id="post-21871-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure what this is an "answer" to? Wireshark can dissect ICMPv6, the original query was about capture filters for ICMPv6.</p></div><div id="comment-21871-info" class="comment-info"><span class="comment-age">(10 Jun '13, 03:10)</span> grahamb ♦</div></div></div><div id="comment-tools-21861" class="comment-tools"></div><div class="clear"></div><div id="comment-21861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

