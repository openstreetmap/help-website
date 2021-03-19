+++
type = "question"
title = "Netscreen firewall Snoop detail captured for tunnel interface"
description = '''Hi team, I am a Netscreen Firewall user, I tried doing a snoop detail on tunnel interface, however couldn&#x27;t open it in wireshark. 2530000.0: tunnel.50(it) vpn=AU-4350-vpn type=ipsec proto=0x0800  10.10.10.1 -&amp;gt; 224.0.0.5/89  vhl=45, tos=c0, id=520, frag=0000, ttl=1 tlen=228  ospf:ver=2, type=1, le...'''
date = "2012-09-13T22:45:00Z"
lastmod = "2012-09-16T04:15:00Z"
weight = 14255
keywords = [ "firewall", "netscreen" ]
aliases = [ "/questions/14255" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Netscreen firewall Snoop detail captured for tunnel interface](/questions/14255/netscreen-firewall-snoop-detail-captured-for-tunnel-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14255-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi team,</p><p>I am a Netscreen Firewall user, I tried doing a snoop detail on tunnel interface, however couldn't open it in wireshark.</p><pre><code>2530000.0: tunnel.50(it) vpn=AU-4350-vpn type=ipsec proto=0x0800
              10.10.10.1 -&gt; 224.0.0.5/89
              vhl=45, tos=c0, id=520, frag=0000, ttl=1 tlen=228
              ospf:ver=2, type=1, len=208
              45 c0 00 e4 da 0c 00 00 01 59 77 c8 0a a6 7b 81     E........Yw...{.
              e0 00 00 05 02 01 00 d0 0a a6 91 c1 00 00 00 00     ................
              a4 16 00 00 00 00 00 00 00 00 00 00 ff ff ff 80     ................
              00 0a 02 01 00 00 00 28 00 00 00 00 00 00 00 00     .......(........
              0a a6 7b be 0a a6 7b 9b 0a a6 7b b1 cb d0 41 03     ..{...{...{...A.
              0a a6 7b 8c 0a a6 7b 82 c0 a8 19 fe 0a a6 7b 8f     ..{...{.......{.
              ac 2b 05 01 0a a6 7b 8a 0a a6 7b a2 0a a6 7b a0     .+....{...{...{.
              cb 2d af 8d 0a a6 7b 9e 0a a6 7b 83 0a a6 7b 8e     .-....{...{...{.
              0a a6 7b 98 cb 2d cd 8d 0a a6 7b b7 0a a6 7b a9     ..{..-....{...{.
              0a a6 7b 90 0a a6 7b 91 cb d9 12 94 cb de 49 1e     ..{...{.......I.
              0a a6 7b 8d 0a a6 7b 95 0a a6 7b b5 0a a6 7b 87     ..{...{...{...{.
              0a a6 7b 8b c0 a8 16 fe 0a a6 7b 95 0a a6 7b ac     ..{.......{...{.
              0a a6 7b 94 c0 a8 17 fe c0 a8 1b fe cb c1 dc 37     ..{............7
              0a a6 7b a5 ac 10 04 fd 0a a6 7b a8 0a a6 7b a6     ..{.......{...{.
              0a a6 7b ae                                         ..{.</code></pre><p>Though the snoop on ethernet interface opens pretty fine.</p><p>Could you please look into it and see if any slight code change is required to incorporate this as well.</p><p>Thanks in advance</p><p>Regards Srb</p></div><div id="question-tags" class="tags-container tags">firewall netscreen</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '12, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/eb73c811e8842e6d78df88e0c3724628?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sarab&#39;s gravatar image" /><p>Sarab<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sarab has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Sep '12, 14:02</p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-14255" class="comments-container"></div><div id="comment-tools-14255" class="comment-tools"></div><div class="clear"></div><div id="comment-14255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14258"></span>

<div id="answer-container-14258" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14258-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately it is not real easy to add support for snoop output for a tunnel. First of all, the function that checks whether a valid packet header is found needs to find the packet length. It scans one line at the moment, so for this output it needs to start parsing multiple lines to find the packet length.</p><p>But the biggest difference between this output and output of other interface types is that there is no link layer, it is only the IP header and IP payload. Currently there is no linklayer type for just raw IP (as far as I know off). At least it is not supported in the "Frame" dissector.</p><p>This means that either:</p><ol><li>A new link-layer type needs to be defined and code to support it needs to be written to the "Frame" dissector -or-</li><li>A dummy link layer needs to be added to the packet</li></ol><p>Option 2 is easier to implement, but more of a dirty hack in my opinion, as you show a link layer in Wireshark that is not really in the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 00:35</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14258" class="comments-container"><span id="14292"></span><div id="comment-14292" class="comment"><div id="post-14292-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Currently there is no linklayer type for just raw IP (as far as I know off).</p></blockquote><p><code>WTAP_ENCAP_RAW_IP</code> in Wiretap; that's what, for example, the pcap link-layer header type <code>LINKTYPE_RAW</code>, as per <a href="http://www.tcpdump.org/linktypes.html">the link-layer header types list at</a> <a href="http://tcpdump.org">tcpdump.org</a>, maps to.</p></div><div id="comment-14292-info" class="comment-info"><span class="comment-age">(15 Sep '12, 02:22)</span> Guy Harris ♦♦</div></div><span id="14295"></span><div id="comment-14295" class="comment"><div id="post-14295-score" class="comment-score">1</div><div class="comment-text"><p>OK, I should have done my research first :-)</p><p>Looking a bit more thorough through the code, there is already support for WTAP_ENCAP_RAW_IP in epan/dissectors/packet-raw.c.</p><p>So actually adding support for netscreen snoop output for tunnel interfaces would involve changing wiretap/netscreen.c to:</p><ul><li>handle packet headers that do not contain a packet length</li><li>add interpretation of raw ip packets and give them type WTAP_ENCAP_RAW_IP</li></ul><p>That should not be too hard, but unfortunately my time is limited at the moment. I'll see if I can find some time the coming weeks.</p></div><div id="comment-14295-info" class="comment-info"><span class="comment-age">(15 Sep '12, 04:48)</span> SYN-bit ♦♦</div></div><span id="14299"></span><div id="comment-14299" class="comment"><div id="post-14299-score" class="comment-score"></div><div class="comment-text"><p>Thanks everyone ....</p><p>@ Syn-bit : Please do update this thread once this is done and later I can update the Juniper forum so that everyone is aware that the support for tunnel interface snoop is there on wireshark :)</p></div><div id="comment-14299-info" class="comment-info"><span class="comment-age">(15 Sep '12, 22:18)</span> Sarab</div></div><span id="14588"></span><div id="comment-14588" class="comment"><div id="post-14588-score" class="comment-score"></div><div class="comment-text"><p>Hi Syn-Bit, Did you get chance to update the code regarding this issue ?</p><p>Thanks Sarab</p></div><div id="comment-14588-info" class="comment-info"><span class="comment-age">(28 Sep '12, 03:47)</span> Sarab</div></div></div><div id="comment-tools-14258" class="comment-tools"></div><div class="clear"></div><div id="comment-14258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14301"></span>

<div id="answer-container-14301" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14301-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you have the raw packet bytes here (from IP up) you could edit those into a format that text2pcap and File|Import... can take. Without having a go at it, it only needs to get an offset at the start of each line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '12, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14301" class="comments-container"><span id="14307"></span><div id="comment-14307" class="comment"><div id="post-14307-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap,</p><p>I tried using text2pcap using raw data, that converts it to pcap however the file doesn't show the details then. e.g in the data paart it doesnt show OSPF details.</p></div><div id="comment-14307-info" class="comment-info"><span class="comment-age">(16 Sep '12, 18:58)</span> Sarab</div></div></div><div id="comment-tools-14301" class="comment-tools"></div><div class="clear"></div><div id="comment-14301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

