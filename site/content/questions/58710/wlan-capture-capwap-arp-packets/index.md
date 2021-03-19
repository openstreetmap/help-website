+++
type = "question"
title = "WLAN capture capwap arp packets"
description = '''Hello,  I&#x27;m hoping someone out there can help me. i&#x27;m looking to create a capture filter. That will capture arp request/response packets from a specific wlan host that are encapsulated in capwap. The arp information for requests is located in the LLC header under type and its hex code is 0x0806.  An...'''
date = "2017-01-12T16:00:00Z"
lastmod = "2017-01-13T07:47:00Z"
weight = 58710
keywords = [ "arp", "cisco", "capwap", "capture-filter", "wlan" ]
aliases = [ "/questions/58710" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WLAN capture capwap arp packets](/questions/58710/wlan-capture-capwap-arp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58710-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm hoping someone out there can help me. i'm looking to create a capture filter. That will capture arp request/response packets from a specific wlan host that are encapsulated in capwap. The arp information for requests is located in the LLC header under type and its hex code is 0x0806.</p><p>Any ideas on this?</p></div><div id="question-tags" class="tags-container tags">arp cisco capwap capture-filter wlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '17, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/f20215beb3590c945a80e0236d70b2fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j0eCamel&#39;s gravatar image" /><p>j0eCamel<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j0eCamel has no accepted answers">0%</span></p></div></div><div id="comments-container-58710" class="comments-container"></div><div id="comment-tools-58710" class="comment-tools"></div><div class="clear"></div><div id="comment-58710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58735"></span>

<div id="answer-container-58735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58735-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It does not appear so.</p><p>Let's look at some background information.</p><ul><li>Available capture filters:<br />
<a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">http://www.tcpdump.org/manpages/pcap-filter.7.html</a></li></ul><p>So if we look at the available primitives, we do see some primitives that are specific to LLC (llc and llc Fitype). But when we enter these primitives into Wireshark and press "Compile Selected BPF's", we get the message that the llc primitives can only be used on raw ATM data. From your email above, you are not capturing ATM traffic.</p><ul><li>OK, so let's try the following capture filter: proto[expr:size]</li></ul><p>where proto = protocol, expr = offset of the field, and size = length in bytes. For example,</p><p>wlan[0:1]=0x80</p><p>would capture only Beacon frames.</p><p>So your best bet is to use the wlan[expr:size]</p><p>The problem is that the LLC must be in the same place for every frame (i.e., no added fields in certain fields.)<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '17, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-58735" class="comments-container"><span id="58736"></span><div id="comment-58736" class="comment"><div id="post-58736-score" class="comment-score"></div><div class="comment-text"><p>Sorry - my mistake on first line. It should say: "It does appear so".</p><p>My mistake</p></div><div id="comment-58736-info" class="comment-info"><span class="comment-age">(13 Jan '17, 07:48)</span> Amato_C</div></div><span id="58737"></span><div id="comment-58737" class="comment"><div id="post-58737-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the response. i'm assuming that this info (0x806) is in the same place for ever capwap arp request. i'm basing this on the fact that using the display filter "wlan.addr == &lt;mac address=""&gt; and arp" displays the capwap arp traffic for a specific device.</p><p>Also how would i go about figuring out the offset and size in the packet for wlan[expr:size]?</p></div><div id="comment-58737-info" class="comment-info"><span class="comment-age">(13 Jan '17, 08:06)</span> j0eCamel</div></div><span id="58738"></span><div id="comment-58738" class="comment"><div id="post-58738-score" class="comment-score"></div><div class="comment-text"><p>So I was able to capture some WLAN traffic that has LLC. It appears that the LLC is outside the WLAN field, so wlan[expr:size] will not work.</p><p>And I stated before, llc will only work for ATM frames according to the Wireshark "Compile selected BFS's" output.</p></div><div id="comment-58738-info" class="comment-info"><span class="comment-age">(13 Jan '17, 08:16)</span> Amato_C</div></div><span id="58740"></span><div id="comment-58740" class="comment"><div id="post-58740-score" class="comment-score"></div><div class="comment-text"><p>excuse my ignorance on this but what do you mean by "Compile selected BFS's"? But looking at the man page, there are two sections one for <strong>ether proto protocol</strong> and one for <strong>LLC</strong> which discusses 802.11 frames</p><p>which i think is the info i want to grab from or does this apply to only ATM frames you were referring to?</p><p><strong>ether proto protocol</strong> <em>the protocol identification comes from the 802.2 Logical Link Control (LLC) header, which is usually layered on top of the FDDI, Token Ring, or 802.11 header. When filtering for most protocol identifiers on FDDI, Token Ring, or 802.11, the filter checks only the protocol ID field of an LLC header in so-called SNAP format with an Organizational Unit Identifier (OUI) of 0x000000, for encapsulated Ethernet; it doesn't check whether the packet is in SNAP format with an OUI of 0x000000.</em></p><p><strong>llc</strong> <strong>IEEE 802.11 data packets;</strong></p><p>Also in these packets the 0806 hex always shows up on bytes 92-93 of the packet and bytes 84-85 for the replies. is there a capture filter to look for those values?</p></div><div id="comment-58740-info" class="comment-info"><span class="comment-age">(13 Jan '17, 09:28)</span> j0eCamel</div></div><span id="58741"></span><div id="comment-58741" class="comment"><div id="post-58741-score" class="comment-score"></div><div class="comment-text"><p>@j0eCamel</p><p>Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-58741-info" class="comment-info"><span class="comment-age">(13 Jan '17, 09:41)</span> grahamb ♦</div></div><span id="58742"></span><div id="comment-58742" class="comment not_top_scorer"><div id="post-58742-score" class="comment-score"></div><div class="comment-text"><p>@j0eCamel - sorry should have explained myself about the "Compile selected BPF's"</p><ol><li><p>Launch Wireshark Legacy. Make sure it is the Legacy version. You can determine if you are really using the Legacy version by doing the following after Wireshark launches: Help / About Wireshark / After the Compiled with you should see "GTK+". The new Wireshark will have Qt</p></li><li><p>After Wireshark Legacy is launched, select Capture / Options</p></li><li><p>In the top pane of the window, select the Interface you will capture on</p></li><li><p>In the "Capture filter" type llc</p></li><li><p>To the right of the Capture filter, you should see "Compile selected BPF's". Press it.</p></li></ol><p>A window will be displayed saying: "llc supported only on raw ATM</p><p>BPF = Berkeley Packet Filtering</p></div><div id="comment-58742-info" class="comment-info"><span class="comment-age">(13 Jan '17, 10:43)</span> Amato_C</div></div></div><div id="comment-tools-58735" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-58735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

