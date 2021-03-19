+++
type = "question"
title = "tshark protocol statistic differs from wireshark"
description = '''I tried to get protocol statistic using wireshark with &quot;Statistics -&amp;gt; Protocol Hierarchy&quot; and using tshark with &quot;-r test.pcap -qz io,phs &amp;gt; stat.txt&quot; from pcap file. And for a number of pcap files i got different results (slightly). What does it mean? May be i do somewhat wrong? I like what pro...'''
date = "2016-07-28T02:16:00Z"
lastmod = "2016-07-28T02:16:00Z"
weight = 54394
keywords = [ "tshark", "protocol_hierarchy" ]
aliases = [ "/questions/54394" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark protocol statistic differs from wireshark](/questions/54394/tshark-protocol-statistic-differs-from-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54394-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to get protocol statistic using wireshark with "Statistics -&gt; Protocol Hierarchy" and using tshark with "-r test.pcap -qz io,phs &gt; stat.txt" from pcap file. And for a number of pcap files i got different results (slightly). What does it mean? May be i do somewhat wrong? I like what produce wireshark, but i need to use tshark and tshark's results grieves me.</p><p>Below i upload two examples as wireshark and tshark protocol hierarchy results.</p><p>At least here we see the difference in BitTorrent section. (Right click -&gt; View Image, for zoom)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/1_htlt3DQ.jpg" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/2_RPOZB4a.jpg" alt="alt text" /></p><p>Second example. Two protocol trees instead of one.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/4.jpg" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/3_EBDoFCj.jpg" alt="alt text" /></p><p>I can if need upload other examples of various results, which another nature.</p><p>Tshark protocol hierarchy results in txt format needs me to parse and represents their in another view.</p><p>I use latest version of wireshark and tshark, 2.0.4, and i tried to use last stable version 1.12.12, same results.</p><p>Thanks in advance.</p><p>ps Sorry for my bad english, its not my native language</p></div><div id="question-tags" class="tags-container tags">tshark protocol_hierarchy</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '16, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/dd29bff42a12be41e857e88cb5a255ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guitarkiller86&#39;s gravatar image" /><p>guitarkiller86<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guitarkiller86 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jul '16, 02:20</p></div></div><div id="comments-container-54394" class="comments-container"></div><div id="comment-tools-54394" class="comment-tools"></div><div class="clear"></div><div id="comment-54394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

