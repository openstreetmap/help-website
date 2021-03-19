+++
type = "question"
title = "Retransmission vs keep-alive - bad seq number"
description = '''Pkt #3 is lost in transit. Packet 4 is a retransmit (based on timing and changed timing when rto is changed). Shown as keep-alive due to incorrect Seq number in pkt 4.  So two issues, why is Seq incorrect in #4 and how can WireShark figure out it is a retransmit vs keep-alive. link:capture'''
date = "2016-10-27T07:41:00Z"
lastmod = "2016-11-01T07:25:00Z"
weight = 56739
keywords = [ "ack_lost_seq", "tcp_retransmission", "keep-alive" ]
aliases = [ "/questions/56739" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Retransmission vs keep-alive - bad seq number](/questions/56739/retransmission-vs-keep-alive-bad-seq-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56739-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Pkt #3 is lost in transit. Packet 4 is a retransmit (based on timing and changed timing when rto is changed). Shown as keep-alive due to incorrect Seq number in pkt 4.<br />
</p><p>So two issues, why is Seq incorrect in #4 and how can WireShark figure out it is a retransmit vs keep-alive.</p><p>link:<a href="https://drive.google.com/file/d/0Bww-llCEGqMedVlpYnRaTXBpT00/view?usp=sharing" title="Capture">capture</a></p></div><div id="question-tags" class="tags-container tags">ack_lost_seq tcp_retransmission keep-alive</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '16, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/1aaaed196aa9c036c56f4db5a4fceb10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="devilbob&#39;s gravatar image" /><p>devilbob<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="devilbob has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-56739" class="comments-container"><span id="56748"></span><div id="comment-56748" class="comment"><div id="post-56748-score" class="comment-score"></div><div class="comment-text"><p>Are the TCP CRC errors and undersized packets also present in the original capture (before sanitizing it)? If so, the capture quality isn't really that good...</p></div><div id="comment-56748-info" class="comment-info"><span class="comment-age">(27 Oct '16, 10:39)</span> Jasper ♦♦</div></div><span id="56752"></span><div id="comment-56752" class="comment"><div id="post-56752-score" class="comment-score"></div><div class="comment-text"><p>No, the CRC errors are a function of the sanitizing. Not sure why you are saying the packets are undersized. They all look good to me.</p></div><div id="comment-56752-info" class="comment-info"><span class="comment-age">(27 Oct '16, 12:54)</span> devilbob</div></div><span id="56754"></span><div id="comment-56754" class="comment"><div id="post-56754-score" class="comment-score"></div><div class="comment-text"><p>Jasper has meant, that the first packet has a size of 74 Byte. The second is 58 Byte. But the other packets are only 54 Byte long. That can normally not be. If we trace on a host the local packets might be under 64 byte. But the incomming packets are normally never under 64 byte.</p></div><div id="comment-56754-info" class="comment-info"><span class="comment-age">(27 Oct '16, 13:15)</span> Christian_R</div></div><span id="56758"></span><div id="comment-56758" class="comment"><div id="post-56758-score" class="comment-score"></div><div class="comment-text"><p>Could you provide the output of :</p><p><code>tshark -r retran_anon.pcapng -otcp.relative_sequence_numbers:FALSE -T fields -e frame.number -e frame.len -e tcp.seq -e tcp.ack -e tcp.len -e tcp.window_size</code></p><p>It would show if the sanitizing might have messed with some of the TCP headers...</p></div><div id="comment-56758-info" class="comment-info"><span class="comment-age">(27 Oct '16, 15:38)</span> SYN-bit ♦♦</div></div><span id="56761"></span><div id="comment-56761" class="comment"><div id="post-56761-score" class="comment-score"></div><div class="comment-text"><p>@devilbob thanks, I think I need to adjust the Tracewrangler default setting a bit.</p></div><div id="comment-56761-info" class="comment-info"><span class="comment-age">(27 Oct '16, 15:53)</span> Jasper ♦♦</div></div></div><div id="comment-tools-56739" class="comment-tools"></div><div class="clear"></div><div id="comment-56739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="56741"></span>

<div id="answer-container-56741" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56741-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The RFC 1122 definition of KEEP-ALIVE is next SEQ -1:</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '16, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '16, 08:09</p></div></div><div id="comments-container-56741" class="comments-container"><span id="56742"></span><div id="comment-56742" class="comment"><div id="post-56742-score" class="comment-score"></div><div class="comment-text"><p>I wonder if the client is upset because the server's SYN, ACK response has a window scale of 0?</p></div><div id="comment-56742-info" class="comment-info"><span class="comment-age">(27 Oct '16, 08:01)</span> grahamb ♦</div></div><span id="56743"></span><div id="comment-56743" class="comment"><div id="post-56743-score" class="comment-score"></div><div class="comment-text"><p>@grahamb: Not only the window scaling is not advertised but the entire window is zero. Yeah I think that is the reason why the session looks so strange. At the beginning. In Packet #5 the system sets the Window to 4096 Byte. But the client never tells the server what he wants from the server. At the end the 8.x.x.x closes the session.</p></div><div id="comment-56743-info" class="comment-info"><span class="comment-age">(27 Oct '16, 08:12)</span> Christian_R</div></div><span id="56744"></span><div id="comment-56744" class="comment"><div id="post-56744-score" class="comment-score"></div><div class="comment-text"><p>@Christian_R, I meant window size.</p></div><div id="comment-56744-info" class="comment-info"><span class="comment-age">(27 Oct '16, 08:16)</span> grahamb ♦</div></div><span id="56745"></span><div id="comment-56745" class="comment"><div id="post-56745-score" class="comment-score"></div><div class="comment-text"><p>@grahamb :)</p></div><div id="comment-56745-info" class="comment-info"><span class="comment-age">(27 Oct '16, 08:19)</span> Christian_R</div></div><span id="56751"></span><div id="comment-56751" class="comment"><div id="post-56751-score" class="comment-score"></div><div class="comment-text"><p>However keep-alives shouldn't happen till after two hours of idle.</p><p>Part of the issue is the window size. All connections with this server have the window size set to 0 in the syn/ack. Normally when it sees the 3rd packet it sends a window size update with ACK=1 and SEQ=1. When the ACK isn't received, then the retransmission is seen as the ACK but what would be the window update has ack=0 and we seem to ignore it except to resend a dup ACK which they ignore.</p><p>I have set the rto to 10 seconds and the other end does not resend the syn/ack in that time before we send the retransmission. Now trying with 30 seconds.</p></div><div id="comment-56751-info" class="comment-info"><span class="comment-age">(27 Oct '16, 12:53)</span> devilbob</div></div><span id="56753"></span><div id="comment-56753" class="comment not_top_scorer"><div id="post-56753-score" class="comment-score"></div><div class="comment-text"><pre><code>However keep-alives shouldn&#39;t happen till after two hours of idle</code></pre><p>That´s not the whole true. 2 hours is the default for keep alives, but the time must be configurable. So I don´t know what time your system has configured.</p><p>BTW: About what OS do we speak?</p></div><div id="comment-56753-info" class="comment-info"><span class="comment-age">(27 Oct '16, 13:10)</span> Christian_R</div></div><span id="56768"></span><div id="comment-56768" class="comment not_top_scorer"><div id="post-56768-score" class="comment-score"></div><div class="comment-text"><p>Maybe the following situation has happened here. But the text is from the year 1989. So I am really not sure:</p><pre><code>Unfortunately, some misbehaved TCP implementations fail
to respond to a segment with SEG.SEQ = SND.NXT-1 unless
the segment contains data.  Alternatively, an
implementation could determine whether a peer responded
correctly to keep-alive packets with no garbage data
octet.</code></pre></div><div id="comment-56768-info" class="comment-info"><span class="comment-age">(27 Oct '16, 22:36)</span> Christian_R</div></div></div><div id="comment-tools-56741" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-56741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56759"></span>

<div id="answer-container-56759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56759-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the SEQ and ACK numbers were not anonymized, then I would say that both TCP implementations have issues.</p><p>10.1.2.3 should not send frame #4, as there is no data to retransmit. The phantom byte in the SYN has been acknowledged in frame #2 and therefor it is the duty of 8.7.6.5 to retransmit the SYN/ACK if the ACK got lost.</p><p>8.7.6.5 however should not use an ACK of 0 in frame #5 as it already acknowledged the phantom byte of the SYN in frame #2, therefor the ACK should be 1 (even though it should not send an ACK in the first place as there was no data received).</p><p>Are both systems using a custom TCP/IP implementation?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '16, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-56759" class="comments-container"><span id="56862"></span><div id="comment-56862" class="comment"><div id="post-56862-score" class="comment-score"></div><div class="comment-text"><p>No, 10.1.2.3 is using vanilla RHEL 6.8. Not sure what the other end is running. I do know they have an F5 in the mix but they have been unable to provide captures. Not really sure why not but they claim not to be able to. I did at one point get a capture from their firewall, one direction used public address and the other direction used private addresses. Looked like we were seeing one direction on pre-NAT and the other post-NAT.</p></div><div id="comment-56862-info" class="comment-info"><span class="comment-age">(31 Oct '16, 05:56)</span> devilbob</div></div></div><div id="comment-tools-56759" class="comment-tools"></div><div class="clear"></div><div id="comment-56759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56899"></span>

<div id="answer-container-56899" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56899-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I now understand this capture. The other end is misbehaving, but the "keep-alives" shown in wireshark are in this case zero-window probes. I didn't realize that zero-window probes use the same timer as rto. So the syn/ack said zero window and we want to start this conversation so we probe.</p><p>I'm good with this now I just have to get the capture from the other end to confirm.</p><p>Thanks for all the input.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/1aaaed196aa9c036c56f4db5a4fceb10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="devilbob&#39;s gravatar image" /><p>devilbob<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="devilbob has no accepted answers">0%</span></p></div></div><div id="comments-container-56899" class="comments-container"></div><div id="comment-tools-56899" class="comment-tools"></div><div class="clear"></div><div id="comment-56899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

