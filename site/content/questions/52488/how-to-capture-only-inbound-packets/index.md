+++
type = "question"
title = "How to capture only inbound packets?"
description = '''Is there a way to capture inbound packets only? '''
date = "2016-05-12T21:25:00Z"
lastmod = "2016-05-13T14:05:00Z"
weight = 52488
keywords = [ "inboundcapture" ]
aliases = [ "/questions/52488" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture only inbound packets?](/questions/52488/how-to-capture-only-inbound-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52488-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to capture inbound packets only?<br />
</p></div><div id="question-tags" class="tags-container tags">inboundcapture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 21:25</strong></p><img src="https://secure.gravatar.com/avatar/8b8ad317b1b08f5265a60fddf37825de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jagboy26&#39;s gravatar image" /><p>jagboy26<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jagboy26 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 May '16, 13:56</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-52488" class="comments-container"></div><div id="comment-tools-52488" class="comment-tools"></div><div class="clear"></div><div id="comment-52488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52543"></span>

<div id="answer-container-52543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52543-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you capture at wired Ethernet, it is usually enough to use capture filter <code>not ether src host yo:ur:ma:ca:dd:rr</code> to reach your goal.</p><p>NB: the reason why I have changed your original title is that there is a bunch of other questions, all dealing with the <em>reverse</em> problem - "why I can only see inbound (or only outbound) packets?". So the reason why no one has answered you yet may be that your original title was a bit repellent.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '16, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52543" class="comments-container"><span id="52556"></span><div id="comment-52556" class="comment"><div id="post-52556-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy. Even after putting the filter I see the packets. What I am trying to do is send packets using tcpreplay and monitor the same interface with dumpcap. What is see is that the packets which are being sent with tcpreplay is also captured on dumpcap, which is what I want to avoid. This is what my filter looks like: dumpcap -f "not ether src host 00:0a:f7:84:55:ec" -i eth4</p></div><div id="comment-52556-info" class="comment-info"><span class="comment-age">(13 May '16, 19:47)</span> jagboy26</div></div><span id="52558"></span><div id="comment-52558" class="comment"><div id="post-52558-score" class="comment-score"></div><div class="comment-text"><p>Before reading further, please try to remove <code>host</code> from the filter expression and try again.</p><p>If that doesn't help, I'm afraid that the reason why that capture filter doesn't work is that the pcap file you tcpreplay is not a recording of previous live traffic of your eth4 but has been taken somewhere else.</p><p>Tcpreplay replays the pcap as verbatim as possible unless you ask it to do otherwise, e.g. by rewriting the MAC address prior to replaying the frame which is probably not what you want. Therefore, I assume that the source MAC addresses of the sent frames do not match your eth4's one.</p><p>The physical direction of packets is not filterable because information about it is not part of the packet contents itself. Some space for information about packet direction is foreseen in pcapng format, which allows to augment the packet data with additional information and defines appropriate information fields which Wireshark understands. But to date no *pcap version I know provides these data, and thus does not extend the capture filter with the ability to filter on them.</p><p>So as it stands now, you'll have to use hardware to reach your goal. You may use:</p><ul><li><p>an Ethernet tap which copies each transmission direction to a separate output, which you'd connect to another NIC of your machine,</p></li><li><p>a manageable switch which allows to mirror traffic on ports and can be configured to monitor only egress (outgoing) packets of a port. Again, you'd connect the monitoring port to another NIC of your machine.</p></li></ul><p>Or, if you feel like that, you may want to modify libpcap to capture only incoming traffic.</p><p>One additional remark: if some of the MAC addresses which occur as source ones in the pcap you tcpreplay are active in the LAN to which you are connected while tcpreplaying, both the live traffic and your simulation will be affected heavily, as the switch will see the same source MAC address in packets coming in through two distinct ports.</p></div><div id="comment-52558-info" class="comment-info"><span class="comment-age">(13 May '16, 23:29)</span> sindy</div></div></div><div id="comment-tools-52543" class="comment-tools"></div><div class="clear"></div><div id="comment-52543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

