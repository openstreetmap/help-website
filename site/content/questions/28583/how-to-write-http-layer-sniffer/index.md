+++
type = "question"
title = "How to write http layer sniffer"
description = '''I asked similar question at StackOverflow. I want to write an application layer sniffer (SMTP/ftp/http). Based on my searchs, first (and perhaps hardest!) step is to reassemble the tcp stream of the sniffed connections. Indeed, what I need is something like the &quot;follow TCP stream&quot; option of wireshar...'''
date = "2014-01-05T05:03:00Z"
lastmod = "2014-01-09T06:08:00Z"
weight = 28583
keywords = [ "tshark", "followtcpstream" ]
aliases = [ "/questions/28583" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to write http layer sniffer](/questions/28583/how-to-write-http-layer-sniffer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28583-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I asked similar question at StackOverflow.</p><p>I want to write an application layer sniffer (SMTP/ftp/http).</p><p>Based on my searchs, first (and perhaps hardest!) step is to reassemble the tcp stream of the sniffed connections.</p><p>Indeed, what I need is something like the "follow TCP stream" option of wireshark, but I need a tool which do it on live interface and automatically. As I know, Tshark can extract TCP streams data from the saved pcap files automatically (<a href="http://ask.wireshark.org/questions/17903/how-do-i-view-all-streams-in-follow-tcp-streams">link</a>) but not from live interfaces. Can Tshark do it on live interfaces???</p><p>As I know, TCPflow can do exactly what I want, however, it can not handle IP defragmentation and SSL connections (I want to analyse the SSL content in the case I have the server private key).</p><p>Any suggestion about mentioned tools or any other useful tool is welcome.</p><p>Thanks in advance, Dan.</p></div><div id="question-tags" class="tags-container tags">tshark followtcpstream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '14, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/a2836861f98534378602f3ba50e7e2ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dani--&#39;s gravatar image" /><p>Dani--<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dani-- has no accepted answers">0%</span></p></div></div><div id="comments-container-28583" class="comments-container"><span id="28587"></span><div id="comment-28587" class="comment"><div id="post-28587-score" class="comment-score"></div><div class="comment-text"><p>TCPflow does not need to handle IP fragmentation because IP fragmentation should not happen for TCP. It is only used for UDP and ICMP, but not TCP since TCP has it's own segmentation mechanisms.</p></div><div id="comment-28587-info" class="comment-info"><span class="comment-age">(05 Jan '14, 09:13)</span> Jasper ♦♦</div></div></div><div id="comment-tools-28583" class="comment-tools"></div><div class="clear"></div><div id="comment-28583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28728"></span>

<div id="answer-container-28728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28728-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you want to write your own sniffer, the best you can do is to look at other code and learn from it.</p><p>AFIAK tcpick is able to do TCP reassembly (not sure about IP defragmentation).</p><blockquote><p><a href="http://tcpick.sourceforge.net/">http://tcpick.sourceforge.net/</a></p></blockquote><p>or take a look at</p><blockquote><p><a href="http://www.xplico.org">http://www.xplico.org</a><br />
<a href="http://justniffer.sourceforge.net/">http://justniffer.sourceforge.net/</a><br />
</p></blockquote><p>or search google for 'libpcap IP defragmentation' for sample code how to do that ;-)</p><p>Now, IP defragmentation and TCP reassembly is the 'easy' part.</p><blockquote><p>I want to analyse the SSL content in the case I have the server private key</p></blockquote><p>Decrypting SSL/TLS is not that easy and there are only few open source tools available that can do it. Obviously Wireshark can do it, but the code of Wireshark is pretty complex.</p><p>Take a look at the code of ssldump. That's (probably) much easier to understand than Wireshark ;-)</p><blockquote><p><a href="http://www.rtfm.com/ssldump/">http://www.rtfm.com/ssldump/</a></p></blockquote><p>Now it's up to you to take all those examples and create your own http sniffer. Good luck !</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '14, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-28728" class="comments-container"></div><div id="comment-tools-28728" class="comment-tools"></div><div class="clear"></div><div id="comment-28728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28585"></span>

<div id="answer-container-28585" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28585-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Regarding HTTP - maybe fiddler can do the trick? <a href="http://fiddler2.com/">Fiddler website</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '14, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/94630d1ea1108afeafb344e884044d15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boaz%20Galil&#39;s gravatar image" /><p>Boaz Galil<br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boaz Galil has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-28585" class="comments-container"><span id="28696"></span><div id="comment-28696" class="comment"><div id="post-28696-score" class="comment-score"></div><div class="comment-text"><p>Thanks Boaz, But I want to sniff http traffic to many server not from my host!</p></div><div id="comment-28696-info" class="comment-info"><span class="comment-age">(08 Jan '14, 21:41)</span> Dani--</div></div></div><div id="comment-tools-28585" class="comment-tools"></div><div class="clear"></div><div id="comment-28585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

