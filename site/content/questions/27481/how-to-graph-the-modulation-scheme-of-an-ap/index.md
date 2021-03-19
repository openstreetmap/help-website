+++
type = "question"
title = "How to graph the modulation scheme of an AP"
description = '''So I have crated a network on ns-3 as part of a college assignment, this network consists of a node that moves at 1m/s and an access point, the application writes a pcap file for me that captures all the traffic. I have been able to graph the evolution of the throughput received by the client vs. ti...'''
date = "2013-11-27T03:41:00Z"
lastmod = "2013-11-27T05:02:00Z"
weight = 27481
keywords = [ "access", "modulation", "pcap", "wireshark" ]
aliases = [ "/questions/27481" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to graph the modulation scheme of an AP](/questions/27481/how-to-graph-the-modulation-scheme-of-an-ap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27481-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I have crated a network on ns-3 as part of a college assignment, this network consists of a node that moves at 1m/s and an access point, the application writes a pcap file for me that captures all the traffic. I have been able to graph the evolution of the throughput received by the client vs. time but the final part of the assignment is to graph how the modulation scheme of the AP changes through time. Is this possible in wireshark</p></div><div id="question-tags" class="tags-container tags">access modulation pcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '13, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/43e6858cd072a78c375d312b659fdcce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="benny&#39;s gravatar image" /><p>benny<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="benny has no accepted answers">0%</span></p></div></div><div id="comments-container-27481" class="comments-container"></div><div id="comment-tools-27481" class="comment-tools"></div><div class="clear"></div><div id="comment-27481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27483"></span>

<div id="answer-container-27483" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27483-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>to graph how the <strong>modulation scheme</strong> of the AP changes through time.</p></blockquote><p>if you mean the 'real' modulation scheme OFDM, etc., then the answer is: Yes (to a certain extent).</p><p>Both the radiotap and PPI header contain some information if OFDM was used.</p><blockquote><p>radiotap.channel.type.ofdm radiotap.xchannel.type.ofdm</p></blockquote><p>See all radiotap fields</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/r/radiotap.html">http://www.wireshark.org/docs/dfref/r/radiotap.html</a></p></blockquote><p>The equivalent information for a PPI header</p><blockquote><p>ppi.80211-common.chan.type.ofdm (and others)</p></blockquote><p>See all PPI fields</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/p/ppi.html">http://www.wireshark.org/docs/dfref/p/ppi.html</a></p></blockquote><p>If 'modulation scheme' is something different for you, please add more information to your question.</p><p>BTW: For both encapsulation types (radiotap and PPI), you can also graph the signal strength. See the links above for those fields.</p><p><strong>HINT</strong> if NS3 does <strong>not</strong> provide those encapsulation types, you will not be able to graph those values.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '13, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27483" class="comments-container"></div><div id="comment-tools-27483" class="comment-tools"></div><div class="clear"></div><div id="comment-27483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

