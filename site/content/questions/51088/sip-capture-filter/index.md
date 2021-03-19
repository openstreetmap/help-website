+++
type = "question"
title = "sip capture filter"
description = '''Hi I have been trying to catch sip protocol packets but while capturing. Since my pc is doing a lot of sniffing already I would like to have capture filter instead display filter used. Also its not an option to &quot;parse&quot; already captured traffic (pcap files). My pc has only 1 quad core cpu... and its ...'''
date = "2016-03-22T06:50:00Z"
lastmod = "2016-03-22T08:39:00Z"
weight = 51088
keywords = [ "sip" ]
aliases = [ "/questions/51088" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [sip capture filter](/questions/51088/sip-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51088-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I have been trying to catch sip protocol packets but while capturing. Since my pc is doing a lot of sniffing already I would like to have capture filter instead display filter used. Also its not an option to "parse" already captured traffic (pcap files). My pc has only 1 quad core cpu... and its almost all the time 100% used. As far as Im filtering via tshark on port 5060 or 5070 some packets are captured but I know 'few' is a lot less than I expect. Filtering all traffic captured by other tshark process I can find lets say a lot of those sip packets. My question is: how to set filter to catch only sip packets.</p></div><div id="question-tags" class="tags-container tags">sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '16, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/6c0c3bad20319826f78cb6d517831b95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jacetyh&#39;s gravatar image" /><p>jacetyh<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jacetyh has no accepted answers">0%</span></p></div></div><div id="comments-container-51088" class="comments-container"></div><div id="comment-tools-51088" class="comment-tools"></div><div class="clear"></div><div id="comment-51088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51095"></span>

<div id="answer-container-51095" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51095-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are two aspects to your question.</p><p>One is that for long-term capturing without immediate analysis, it is far better to use dumpcap instead of tshark, as it does less (no display filter processing) so it takes less CPU, and as it does not gradually eat all available memory (search through this site for older Questions dealing with "memory problem").</p><p>Another one is how to identify SIP packets using a capture filter. If you say that a capture filter <code>port 5060 or 5070</code> is too narrow as it misses some SIP traffic, it would mean that there are SIP messages where both source and destination port numbers differ from the two above.</p><p>Under specific conditions, you could use a capture filter like <code>(udp[8:4] = 0x5349502f and udp[12:4] = 0x322e3020) or (udp[8:4] = 0x494e5649 &amp; 0x3f3f3f3f and udp[12:3] &amp; 0x3f3f3f = 0x544520) or (udp[8:4] &amp; 0x3f3f3f3f3f = 0x42594520) or ...</code> i.e. you would look for the <code>SIP/2.0</code> keyword followed by a space character, by which all SIP responses begin, and for names of all known SIP methods followed by a space character at the beginning of UDP payload of each packet, because the <code>SIP/2.0</code> keyword in requests is not on a fixed place in the packet. The example covers <code>INVITE</code> and <code>BYE</code> and the <code>&amp; 0x3f...</code> is there to ignore letter case, because use of any (even mixed) case is allowed (although rarely used) for notation of SIP methods.</p><p>This approach will not work for SIP over TCP transport because you cannot rely on SIP messages to start at TCP packet payload.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '16, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '16, 08:40</p></div></div><div id="comments-container-51095" class="comments-container"><span id="51113"></span><div id="comment-51113" class="comment"><div id="post-51113-score" class="comment-score"></div><div class="comment-text"><p>so to sum up, the best way to capture sip is to use display filter in tshark? I'm very new at this. I spent a lot of time googling the best way for that and, failed. Im considering setting priority to lowest possible for this instance of tshark. Btw where can I find info about filters you mention (udp[8:4] = 0x5349502f and etc) I would like to get more into details on this topic.</p></div><div id="comment-51113-info" class="comment-info"><span class="comment-age">(23 Mar '16, 01:09)</span> jacetyh</div></div><span id="51115"></span><div id="comment-51115" class="comment"><div id="post-51115-score" class="comment-score"></div><div class="comment-text"><blockquote><p>the best way to capture sip is to use display filter in tshark?</p></blockquote><p>As always, it depends on the particular scenario:</p><ul><li><p>if your primary concern is not to miss a single SIP packet in an environment you know nothing about, then yes, you have to give Wireshark/tshark a chance to let the SIP heuristic dissector inspect each UDP and TCP packet, because it is not rare that SIP uses other ports than 5060. Even SIP dialogs which started at 5060 as at least one of the ports may migrate away from it.</p></li><li><p>if, however, low resource consumption and/or potentially infinite duration of the capture is what bothers you most, and you can use the knowledge about which scenarios exist in that network and which don't, based on analysis of short-term capturing using Wireshark/tshark, you may be able to use a capture filter based on a set of ports and IP addresses.</p></li></ul><blockquote><p>where can I find info about filters you mention</p></blockquote><p>A good starting point are the examples <a href="https://wiki.wireshark.org/CaptureFilters">here</a>, for detailed formal syntax look <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">here</a>. The hex strings I've given in my example are ASCII strings - <code>SIP/</code>, <code>2.0</code>, <code>INVI</code>, <code>TE</code>, and <code>BYE</code>. The maximum size of data which can be accessed using a single <code>proto[start:size]</code> expression is 4 bytes. The whole thing is in fact a simple heuristic filter, you would have to add all SIP methods which can be expected in your scenarios. I've already listed its limitations.</p></div><div id="comment-51115-info" class="comment-info"><span class="comment-age">(23 Mar '16, 03:10)</span> sindy</div></div><span id="51117"></span><div id="comment-51117" class="comment"><div id="post-51117-score" class="comment-score"></div><div class="comment-text"><p>Thanks, for now its all I needed, I mean lecture and knowledge. For now Ill use display filter, but I will change it to some more suitable for my needs, someday.</p></div><div id="comment-51117-info" class="comment-info"><span class="comment-age">(23 Mar '16, 03:50)</span> jacetyh</div></div></div><div id="comment-tools-51095" class="comment-tools"></div><div class="clear"></div><div id="comment-51095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

