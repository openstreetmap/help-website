+++
type = "question"
title = "LTE SIB12 decoding message getting malformed packet with Number of pages should be &lt;=15 (found 65)"
description = '''Hi All,  While decoding LTE SIB12 message i&#x27;m getting malformed packet with &quot;Number of pages should be &amp;lt;=15 (found 65)&quot; and after looking into wireshark source code nb_of_pages set to 15 if it is more than 15. Can you please help me to understand why this required ? is it mandatory as per 3GPP sp...'''
date = "2016-08-16T06:53:00Z"
lastmod = "2016-08-16T12:06:00Z"
weight = 54866
keywords = [ "cmas", "sib12", "rrc", "lte" ]
aliases = [ "/questions/54866" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [LTE SIB12 decoding message getting malformed packet with Number of pages should be &lt;=15 (found 65)](/questions/54866/lte-sib12-decoding-message-getting-malformed-packet-with-number-of-pages-should-be-15-found-65)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54866-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, While decoding LTE SIB12 message i'm getting malformed packet with "Number of pages should be &lt;=15 (found 65)" and after looking into wireshark source code nb_of_pages set to 15 if it is more than 15. Can you please help me to understand why this required ? is it mandatory as per 3GPP specification ? Thanks in advance.</p><pre><code>nb_of_pages = tvb_get_guint8(warning_msg_seg_tvb, 0);
ti = proto_tree_add_uint(tree, hf_lte_rrc_warningMessageSegment_nb_pages, warning_msg_seg_tvb, 0, 1, nb_of_pages);
if (nb_of_pages &gt; 15) {
    expert_add_info_format(pinfo, ti, &amp;ei_lte_rrc_number_pages_le15,
                           &quot;Number of pages should be &lt;=15 (found %u)&quot;, nb_of_pages);
    nb_of_pages = 15;
}</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_image_6kYzUu6.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">cmas sib12 rrc lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '16, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/31e49cc408ac91f6ab78d6fe89a84dd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="svr&#39;s gravatar image" /><p>svr<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="svr has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 Aug '16, 07:17</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54866" class="comments-container"></div><div id="comment-tools-54866" class="comment-tools"></div><div class="clear"></div><div id="comment-54866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54878"></span>

<div id="answer-container-54878" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54878-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This requirement comes from 3GPP 23.041 chapter 9.3.35, that's why I added this expert info.</p><p>If you share the pcap file, I will be able to confirm whether the value 65 is really encoded (in that case Wireshark is right) or if this is a decoding error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '16, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-54878" class="comments-container"><span id="54892"></span><div id="comment-54892" class="comment"><div id="post-54892-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, Thank you. I'm capturing logs from RRC layer and format of message is eth:ipv4:udp:1 byte header to identify logical channel:RRC Byte.</p><p>For decoding CMAS, calling wireshark built-in dissector "lte-rrc.bcch.dl.sch".</p><p>I don't know how to upload file here. So sharing through wiki send</p><p>Wireshark pcap: <a href="http://wikisend.com/download/937472/CMAS_Wireshark.pcap">http://wikisend.com/download/937472/CMAS_Wireshark.pcap</a> lua script : <a href="http://wikisend.com/download/101712/lterrc.lua">http://wikisend.com/download/101712/lterrc.lua</a></p></div><div id="comment-54892-info" class="comment-info"><span class="comment-age">(16 Aug '16, 23:25)</span> svr</div></div><span id="54923"></span><div id="comment-54923" class="comment"><div id="post-54923-score" class="comment-score">1</div><div class="comment-text"><p>Your script was missing a line:</p><p>dissector:call(payload,pinfo,tree)</p><p>But once added, I could decode your framing protocol.</p><p>The first byte of the reassembled Warning Message Content E-UTRAN IE is indeed 0x41, which means 65. This does not comply with 3GPP specification. BTW the whole buffer is not compliant with the encoding specified in 23.041 chapter 9.3.35. After manually modifying LTE RRC dissector, it looks like the buffer lacks the number of pages indicated in the fist byte and contains the text: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZAB</p><p>Your test tool used to generate this SIB12 (I guess this does not come from a live network) must be reworked.</p><p>If I answered your question, do not forget to accept it by clicking on the check mark next to the answer. It will help others.</p></div><div id="comment-54923-info" class="comment-info"><span class="comment-age">(17 Aug '16, 10:04)</span> Pascal Quantin</div></div></div><div id="comment-tools-54878" class="comment-tools"></div><div class="clear"></div><div id="comment-54878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

