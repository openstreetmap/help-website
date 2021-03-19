+++
type = "question"
title = "PcapNg and Wireless Data"
description = '''For my project ( Wireless Envoirment ) I am Capturing traffic using wireshark and saving it in PcapNg format. Later I want to retrieve this information to get network layer and above layer information. But PcapNg man page says { Features not yet in pcap-ng:-&amp;gt; Wireless spectrum information / physi...'''
date = "2014-02-12T10:09:00Z"
lastmod = "2014-02-12T16:37:00Z"
weight = 29788
keywords = [ "wireless", "sniffing", "pcapng", "intrusion", "wireshark" ]
aliases = [ "/questions/29788" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [PcapNg and Wireless Data](/questions/29788/pcapng-and-wireless-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29788-score" class="post-score" title="current number of votes">0</div><span id="post-29788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For my project ( Wireless Envoirment ) I am Capturing traffic using wireshark and saving it in PcapNg format. Later I want to retrieve this information to get network layer and above layer information. But PcapNg man page says { Features not yet in pcap-ng:-&gt; Wireless spectrum information / physical layer meta-data } So as I dont want information about physical layer data. Though Can I get network layer wireless data from pcap-ng file... and second thing can I use payload information from this pcap-ng file for intrusion detection..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-intrusion" rel="tag" title="see questions tagged &#39;intrusion&#39;">intrusion</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '14, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/4f2e12b298828a7bdd200478480606da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WIDS&#39;s gravatar image" /><p><span>WIDS</span><br />
<span class="score" title="25 reputation points">25</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WIDS has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Feb '14, 10:30</strong> </span></p></div></div><div id="comments-container-29788" class="comments-container"></div><div id="comment-tools-29788" class="comment-tools"></div><div class="clear"></div><div id="comment-29788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29802"></span>

<div id="answer-container-29802" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29802-score" class="post-score" title="current number of votes">1</div><span id="post-29802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="WIDS has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Pcap-ng and pcap are both formats that support all the packet types describe in <a href="http://www.tcpdump.org/linktypes.html">the tcpdump.org list of link-layer header types</a>. This includes the <code>LINKTYPE_IEEE802_11</code> type (in which packets begin with an IEEE 802.11 header) and the <code>LINKTYPE_IEEE802_11_PRISM</code>, <code>LINKTYPE_IEEE802_11_RADIOTAP</code>, <code>LINKTYPE_IEEE802_11_AVS</code>, and <code>LINKTYPE_PPI</code> types (in which packets either begin with a header giving some physical layer meta-data for the packet - pcap-ng doesn't have anything in the general format to support physical layer meta-data for individual packets, but it doesn't <em>have</em> to, and, in fact, shouldn't, do so - or begin with the "PPI" header, which can include physical-layer meta-data for the packet. (As the page you mentioned, <a href="http://wiki.wireshark.org/Development/PcapNg">the pcap-ng page on the Wireshark wiki</a>, currently says in the "Features not yet in pcap-ng" list, it doesn't support "Wireless spectrum information / physical layer meta-data (<em>other than what's already carried in headers such as the radiotap header for 802.11</em>)"; I've italicized the important part here. I will update that page to clarify that it will probably never do so, as "what's already carried in headers" will be sufficient.)</p><p>Capturing on an 802.11 interface when not in monitor mode will probably give you packets with fake Ethernet headers rather than the packets' actual 802.11 headers.</p><p>In either case, if you want the network-layer information, you will have to check the Ethernet or 802.11 header to see what protocol is above the link layer, ignore packets where the protocol isn't what you're interested in, and then skip past the link-layer header (and radio meta-data/PPI header, if it's present) and process the network-layer header.</p><p>Note that if you are capturing in monitor mode, the packets will be encrypted if you're on a "protected" (WEP or WPA/WPA2) network, and you will need to decrypt the payload in order to be able to process the network-layer header.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Feb '14, 16:40</strong> </span></p></div></div><div id="comments-container-29802" class="comments-container"></div><div id="comment-tools-29802" class="comment-tools"></div><div class="clear"></div><div id="comment-29802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

