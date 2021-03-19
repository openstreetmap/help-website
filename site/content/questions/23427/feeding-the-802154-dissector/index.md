+++
type = "question"
title = "Feeding the 802.15.4 Dissector"
description = '''Hello, I&#x27;m using Wireshark to read from a pipe and i&#x27;m using the native IEEE 802.15.4 dissector, but I&#x27;m having trouble feeding Wireshark the proper bytes. I&#x27;ve tried to search but I can&#x27;t find the right sequence of bytes the dissector is waiting. Can anyone help me? Thanks in advance.'''
date = "2013-07-29T07:48:00Z"
lastmod = "2013-07-30T22:34:00Z"
weight = 23427
keywords = [ "802.15.4", "dissector" ]
aliases = [ "/questions/23427" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Feeding the 802.15.4 Dissector](/questions/23427/feeding-the-802154-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23427-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm using Wireshark to read from a pipe and i'm using the native IEEE 802.15.4 dissector, but I'm having trouble feeding Wireshark the proper bytes. I've tried to search but I can't find the right sequence of bytes the dissector is waiting.</p><p>Can anyone help me? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">802.15.4 dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '13, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/9ecb1d42c1a0436bb3a9348b8861daa4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="funguy&#39;s gravatar image" /><p>funguy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="funguy has no accepted answers">0%</span></p></div></div><div id="comments-container-23427" class="comments-container"></div><div id="comment-tools-23427" class="comment-tools"></div><div class="clear"></div><div id="comment-23427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23457"></span>

<div id="answer-container-23457" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23457-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>802.15.4 dissector does following in proto_reg_handoff_ieee802154:</p><pre><code>dissector_add_uint(&quot;wtap_encap&quot;, WTAP_ENCAP_IEEE802_15_4, ieee802154_handle);
dissector_add_uint(&quot;wtap_encap&quot;, WTAP_ENCAP_IEEE802_15_4_NONASK_PHY, ieee802154_nonask_phy_handle);
dissector_add_uint(&quot;wtap_encap&quot;, WTAP_ENCAP_IEEE802_15_4_NOFCS, ieee802154_nofcs_handle);
dissector_add_uint(&quot;sll.ltype&quot;, LINUX_SLL_P_IEEE802154, ieee802154_handle);</code></pre><p>If you look into wiretap/pcap-common.c you will find that following linktypes are assigned for the WTAP_ENCAP_ defines:</p><pre><code>/* IEEE 802.15.4 Wireless PAN */
{ 195, WTAP_ENCAP_IEEE802_15_4 },
...
/* IEEE 802.15.4 Wireless PAN non-ASK PHY */
{ 215, WTAP_ENCAP_IEEE802_15_4_NONASK_PHY },
...
/* IEEE 802.15.4 Wireless PAN no fcs */
{ 230, WTAP_ENCAP_IEEE802_15_4_NOFCS },</code></pre><p>Now, get over to the tcpdump linktypes [1] and check the descriptions for 195, 215, 230. Choose the one that is closest match to your data and then set that number as linktype in pcap header.</p><p>[1] <a href="http://www.tcpdump.org/linktypes.html">http://www.tcpdump.org/linktypes.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '13, 22:34</strong></p><img src="https://secure.gravatar.com/avatar/96637248dab9a269e98fbf0344e26a93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="desowin&#39;s gravatar image" /><p>desowin<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="desowin has no accepted answers">0%</span></p></div></div><div id="comments-container-23457" class="comments-container"></div><div id="comment-tools-23457" class="comment-tools"></div><div class="clear"></div><div id="comment-23457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

