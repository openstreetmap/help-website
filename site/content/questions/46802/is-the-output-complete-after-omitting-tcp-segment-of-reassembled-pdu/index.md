+++
type = "question"
title = "Is the output complete after omitting [TCP segment of reassembled PDU]?"
description = '''If the tshark -r dumpfile output contains the type [TCP segment of a reassembled PDU], as in  81 3.164109000 4.5.6.7 -&amp;gt; 12.13.14.15 TLSv1.2 609 Application Data 83 3.164523000 4.5.6.7 -&amp;gt; 12.13.14.15 TCP 2802 [TCP segment of a reassembled PDU] 85 3.277723000 4.5.6.7 -&amp;gt; 12.13.14.15 TLSv1.2 41...'''
date = "2015-10-21T08:43:00Z"
lastmod = "2015-10-21T09:29:00Z"
weight = 46802
keywords = [ "reassembly", "tshark", "capture-file" ]
aliases = [ "/questions/46802" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is the output complete after omitting \[TCP segment of reassembled PDU\]?](/questions/46802/is-the-output-complete-after-omitting-tcp-segment-of-reassembled-pdu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46802-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If the <code>tshark -r dumpfile</code> output contains the type <em>[TCP segment of a reassembled PDU]</em>, as in</p><p>81 3.164109000 4.5.6.7 -&gt; 12.13.14.15 TLSv1.2 609 Application Data<br />
83 3.164523000 4.5.6.7 -&gt; 12.13.14.15 TCP 2802 [TCP segment of a reassembled PDU]<br />
85 3.277723000 4.5.6.7 -&gt; 12.13.14.15 TLSv1.2 4170 Application Data</p><p><a href="https://www.wireshark.org/lists/wireshark-users/200805/msg00206.html">it</a> <a href="http://serverfault.com/questions/516401/why-does-wireshark-think-this-frame-is-a-tcp-segment-of-a-reassembled-pdu">is</a> <a href="https://www.wireshark.org/lists/wireshark-users/200806/msg00047.html">clear</a> <a href="http://stackoverflow.com/questions/12836944/how-wireshark-marks-some-packets-as-tcp-segment-of-a-reassembled-pdu">that</a> <a href="http://superuser.com/questions/255157/tcp-segment-of-a-reassembled-pdu">this</a> <a href="http://fixunix.com/tcp-ip/66988-tcp-segment-reassembled-pdu-errors.html">means</a> several TCP segments containing an application-level PDU (in this case, TLSv1.2).</p><p>If it is omitted from the output (via further processing, f.ex. <code>grep</code>), does the rest still <em>contain all the information about the flows</em>, or not?</p><p>In other words, can one see from the remaining lines (here lines 81 and 85), how much (in this case TLS) data flowed from whom to whom?</p></div><div id="question-tags" class="tags-container tags">reassembly tshark capture-file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '15, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/0f479a594deab60e820a84e87409f955?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user1234&#39;s gravatar image" /><p>user1234<br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user1234 has one accepted answer">50%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Oct '15, 06:12</p></div></div><div id="comments-container-46802" class="comments-container"></div><div id="comment-tools-46802" class="comment-tools"></div><div class="clear"></div><div id="comment-46802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46804"></span>

<div id="answer-container-46804" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46804-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>If <strong>it is omitted</strong> from the output,</p></blockquote><p>I'm not sure what you mean by that (what is 'it'), but to answer your question:</p><blockquote><p>does the trace still contain all the information about the flows, or not?</p></blockquote><p>It depends mainly on the following conditions (at least):</p><ul><li>did you capture all flows (capture filters)</li><li>did you experience packet loss (on the line, within the capture system)</li></ul><p>So, if there is no '[TCP segment of a reassembled PDU]' and none of the conditions above are true, you can still have the full TCP session data in the pcap file. It means that it was not necessary for the application dissector to reassemble several TCP frames to get all required application data.</p><p>I hope I got your question right !?!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '15, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '15, 09:31</p></div></div><div id="comments-container-46804" class="comments-container"><span id="46806"></span><div id="comment-46806" class="comment"><div id="post-46806-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much so far. I captured all flows before (via <code>tshark -w</code>) and did not experience packet loss. The question is about the output of <code>tshark -r</code>, which parses a pcap file. Regards</p></div><div id="comment-46806-info" class="comment-info"><span class="comment-age">(21 Oct '15, 09:47)</span> user1234</div></div><span id="46817"></span><div id="comment-46817" class="comment"><div id="post-46817-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The question is about the output of tshark -r, which parses a pcap file.</p></blockquote><p>can you please elaborate? What is your question regarding the output of tshark? Maybe an example helps to understand what you need.</p></div><div id="comment-46817-info" class="comment-info"><span class="comment-age">(21 Oct '15, 13:02)</span> Kurt Knochner ♦</div></div><span id="46827"></span><div id="comment-46827" class="comment"><div id="post-46827-score" class="comment-score"></div><div class="comment-text"><p>In order to analyze packet data (<a href="https://en.wikipedia.org/wiki/Traffic_analysis),">https://en.wikipedia.org/wiki/Traffic_analysis),</a> it helps to remove redundant messages, such as ACKs, ARP requests, etc.</p><p>Is line 83 redundant, or does it contain relevant information? Do the 4170 segments of line 85 contain the 2802 of line 83?</p></div><div id="comment-46827-info" class="comment-info"><span class="comment-age">(22 Oct '15, 02:47)</span> user1234</div></div><span id="46830"></span><div id="comment-46830" class="comment"><div id="post-46830-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is line 83 redundant, or does it contain relevant information?</p></blockquote><p>It depends on what you want to analyze. If it's the TCP behavior (SEQ, ACK), then it's relevant. If you want to decrpyt the payload, it's relevant. If you want to count the transmitted bytes, it might be relevant, but you can also deduce that from the SEQ/ACK numbers. In other cases it might be irrelevant.</p><blockquote><p>it helps to remove redundant messages, such as ACKs, ARP requests, etc.</p></blockquote><p>ACKs are not "redundant". Duplicate ACKs are redundant.</p><blockquote><p>In order to analyze packet data</p></blockquote><p>What kind of analysis do you need, where regular ACKs would be a problem?</p></div><div id="comment-46830-info" class="comment-info"><span class="comment-age">(22 Oct '15, 07:09)</span> Kurt Knochner ♦</div></div><span id="46876"></span><div id="comment-46876" class="comment not_top_scorer"><div id="post-46876-score" class="comment-score"></div><div class="comment-text"><blockquote><p>What kind of analysis do you need, where regular ACKs would be a problem?</p></blockquote><p>I need to analyse the TLS stream, which packets are sent and received, and in what order.</p></div><div id="comment-46876-info" class="comment-info"><span class="comment-age">(23 Oct '15, 05:37)</span> user1234</div></div><span id="46877"></span><div id="comment-46877" class="comment"><div id="post-46877-score" class="comment-score">1</div><div class="comment-text"><p>well, then you can't omit those frames, because they are part of the TCP/TLS conversation.</p></div><div id="comment-46877-info" class="comment-info"><span class="comment-age">(23 Oct '15, 06:04)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46804" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-46804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

