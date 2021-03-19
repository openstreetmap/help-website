+++
type = "question"
title = "how to convert the user-defined item in hr_tree to a human-readable format"
description = '''I created two items (stamp1 and stamp2 in hr_tree) to label special useful bytes with the following line of code in packet-eth.c: proto_tree_add_item(fh_tree, vtime_id, trailer_tvb, (trailer_length - 8), 8, FALSE);  Here&#x27;s the decoding with the items added:  Frame 1: 69 bytes on wire (552 bits), 69 ...'''
date = "2011-10-04T05:26:00Z"
lastmod = "2011-10-04T09:21:00Z"
weight = 6696
keywords = [ "development" ]
aliases = [ "/questions/6696" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to convert the user-defined item in hr\_tree to a human-readable format](/questions/6696/how-to-convert-the-user-defined-item-in-hr_tree-to-a-human-readable-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6696-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I created two items (<code>stamp1</code> and <code>stamp2</code> in <code>hr_tree</code>) to label special useful bytes with the following line of code in <code>packet-eth.c</code>:</p><pre><code>proto_tree_add_item(fh_tree, vtime_id, trailer_tvb, (trailer_length - 8), 8, FALSE);</code></pre><p>Here's the decoding with the items added:</p><hr /><pre><code>Frame 1: 69 bytes on wire (552 bits), 69 bytes captured (552 bits)
Ethernet II, Src: JuniperN_17:d0:85 (00:05:85:17:d0:85), Dst: Cisco_ef:fd:00 (00:1b:0d:ef:fd:00)
    Destination: Cisco_ef:fd:00 (00:1b:0d:ef:fd:00)
    Source: JuniperN_17:d0:85 (00:05:85:17:d0:85)
    Type: IP (0x0800)
    stamp1: 4e64885133d37df8
    stamp2: 04
    Trailer: 000000000000
Internet Protocol Version 4, Src: 111.72.163.42 (111.72.163.42), Dst: 219.141.191.132 (219.141.191.132)
Transmission Control Protocol, Src Port: 61294 (61294), Dst Port: https (443), Seq: 1, Ack: 1, Len: 0
    Source port: 61294 (61294)
    Destination port: https (443)
    [Stream index: 0]
    Sequence number: 1    (relative sequence number)
    Acknowledgement number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x10 (ACK)
    Window size value: 64860
    [Calculated window size: 64860]
    [Window size scaling factor: -1 (unknown)]
    Checksum: 0x1541 [validation disabled]</code></pre><hr /><p>But <code>stamp1</code> is in hex format, which is difficult to understand. I want it in a human-readable format, such as epoch time, instead of the hex string. I've no idea how to do this. Please advise.</p></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '11, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/e9d668dd28830dd8f79d4dbb56e5f2bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam&#39;s gravatar image" /><p>Sam<br />
<span class="score" title="51 reputation points">51</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Oct '11, 07:13</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6696" class="comments-container"><span id="6699"></span><div id="comment-6699" class="comment"><div id="post-6699-score" class="comment-score"></div><div class="comment-text"><p>How have you added your <code>stamp1</code> and <code>stamp2</code> fields? Can you post the code changes?</p></div><div id="comment-6699-info" class="comment-info"><span class="comment-age">(04 Oct '11, 06:05)</span> multipleinte...</div></div><span id="6700"></span><div id="comment-6700" class="comment"><div id="post-6700-score" class="comment-score"></div><div class="comment-text"><p><strong>Sure, please see below key code:</strong></p><p>*proto_tree_add_item(fh_tree, stamp1_id, trailer_tvb, (trailer_length - 9), 8, FALSE);</p><p>proto_tree_add_item(fh_tree, stamp2_id, trailer_tvb, (trailer_length - 1), 1, FALSE);*</p><p><strong>In addtion, the below elements need be added:</strong></p><p>*{ &amp;hf_eth_stamp1,</p><p>{ "stamp1", "eth.stamp1", FT_BYTES, BASE_NONE, NULL, 0x0, "Ethernet stamp1", HFILL }},</p><p>{ &amp;hf_eth_stamp2,</p><p>{ "stamp2", "eth.stamp2", FT_BYTES, BASE_NONE, NULL, 0x0, "Ethernet stamp2", HFILL }}*</p></div><div id="comment-6700-info" class="comment-info"><span class="comment-age">(04 Oct '11, 06:26)</span> Sam</div></div><span id="6701"></span><div id="comment-6701" class="comment"><div id="post-6701-score" class="comment-score"></div><div class="comment-text"><p>Btw, Which files include the Epoch time convert function, it maybe useful, I can try it.</p></div><div id="comment-6701-info" class="comment-info"><span class="comment-age">(04 Oct '11, 06:33)</span> Sam</div></div></div><div id="comment-tools-6696" class="comment-tools"></div><div class="clear"></div><div id="comment-6696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6709"></span>

<div id="answer-container-6709" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6709-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand you correctly, you can accomplish what you want with something like this:</p><pre><code>{ &amp;hf_eth_stamp1,
{ &quot;stamp1&quot;, &quot;eth.stamp1&quot;, FT_ABSOLUTE_TIME, ABSOLUTE_TIME_UTC, NULL, 0x0, &quot;Ethernet stamp1&quot;, HFILL }},</code></pre><p>Note the different ftype and display base; these allow you to have the Wireshark back end do most of the heavy lifting. Then, in your <code>proto_dissect_*</code> function:</p><pre><code>proto_tree_add_item(fh_tree, stamp1_id, trailer_tvb, (trailer_length - 9), 8, ENC_BIG_ENDIAN | ENC_TIME_TIMESPEC);</code></pre><p>Note here that the endianness and time encoding are specified; currently, these will evaluate to 0 (<code>FALSE</code>), but if they change in the future, this scheme will keep your dissector from breaking as it is used internally. Finally, as Jaap mentioned in his answer, you should look into the provided documentation for hints on how to accomplish what you want. I will leave <code>stamp2</code> to you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '11, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-6709" class="comments-container"><span id="6710"></span><div id="comment-6710" class="comment"><div id="post-6710-score" class="comment-score"></div><div class="comment-text"><p>It works follow your code, thank you very much, Multipleinterfaces.</p><p>Sam</p></div><div id="comment-6710-info" class="comment-info"><span class="comment-age">(04 Oct '11, 09:54)</span> Sam</div></div><span id="6728"></span><div id="comment-6728" class="comment"><div id="post-6728-score" class="comment-score"></div><div class="comment-text"><p>If it works, then the thing to do now is to accept the answer so this question is no longer listed as unanswered.</p></div><div id="comment-6728-info" class="comment-info"><span class="comment-age">(04 Oct '11, 17:31)</span> cmaynard ♦♦</div></div><span id="6733"></span><div id="comment-6733" class="comment"><div id="post-6733-score" class="comment-score"></div><div class="comment-text"><p>Ok, but how to take out it from the unansered list? I check the FAQ but no any related instructions described.</p></div><div id="comment-6733-info" class="comment-info"><span class="comment-age">(05 Oct '11, 03:42)</span> Sam</div></div><span id="6734"></span><div id="comment-6734" class="comment"><div id="post-6734-score" class="comment-score"></div><div class="comment-text"><p>Mark the answer as accepted by clicking the icon next to it (I think it's a check mark.</p></div><div id="comment-6734-info" class="comment-info"><span class="comment-age">(05 Oct '11, 03:59)</span> grahamb ♦</div></div><span id="6735"></span><div id="comment-6735" class="comment"><div id="post-6735-score" class="comment-score"></div><div class="comment-text"><p>Okay, thanks.</p></div><div id="comment-6735-info" class="comment-info"><span class="comment-age">(05 Oct '11, 05:17)</span> Sam</div></div></div><div id="comment-tools-6709" class="comment-tools"></div><div class="clear"></div><div id="comment-6709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6704"></span>

<div id="answer-container-6704" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6704-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Read up on FT_BYTES and companions in doc/README.developer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '11, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6704" class="comments-container"></div><div id="comment-tools-6704" class="comment-tools"></div><div class="clear"></div><div id="comment-6704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

