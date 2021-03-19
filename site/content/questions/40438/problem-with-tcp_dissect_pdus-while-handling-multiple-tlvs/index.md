+++
type = "question"
title = "problem with tcp_dissect_pdus while handling multiple TLVs"
description = '''Hello Experts, I have developed a customized wireshark plugin to decode our proprietary protocol in a TCP message. As we all know, TCP is byte stream oriented protocol hence one application message is not guaranteed in one TCP message. (one TCP message might contain many full messages / partial mess...'''
date = "2015-03-10T09:45:00Z"
lastmod = "2015-03-10T09:45:00Z"
weight = 40438
keywords = [ "tcp_dissect_pdus", "mutiple", "tlv" ]
aliases = [ "/questions/40438" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [problem with tcp\_dissect\_pdus while handling multiple TLVs](/questions/40438/problem-with-tcp_dissect_pdus-while-handling-multiple-tlvs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40438-score" class="post-score" title="current number of votes">0</div><span id="post-40438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Experts,</p><p>I have developed a customized wireshark plugin to decode our proprietary protocol in a TCP message. As we all know, TCP is byte stream oriented protocol hence one application message is not guaranteed in one TCP message. (one TCP message might contain many full messages / partial message). To handle the above scenario I am making use of tcp_dissect_pdus() that will wait until specified bytes are accumulated and calls the specified function accordingly. My 1 complete application message contains 68 bytes fixed header + 2 TLV structures inside it where in, I am required to obtain the length of the 1st TLV's length (1 byte) and move those many number of bytes + Tag&amp; length (length of 2nd TLV is 2 bytes as value can be upto 64435) and then wait until the 2nd TLV's length number of bytes are available and then perform the decoding.</p><p>Problem:- Hence I tried using tcp_dissect_pdus() twice like given below:</p><p>/<em>After getting 70 bytes obtain length of 1st TLV and then call the function which calculates the length of the 2nd TLV and finally calls the main decoding logic</em>/</p><p>static void dissect_dsr(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree <em>tree, void</em> data <em>U</em>) { tcp_dissect_pdus(tvb, pinfo, tree, dsr_desegment,70, get_dsr_tgtID_len, dissect_dsr_pdu, data);<br />
}</p><p>static void dissect_dsr_pdu(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree <em>tree, void</em> data <em>U</em>) { tcp_dissect_pdus(tvb, pinfo, tree, dsr_desegment,(70+tgtIDlen+3), get_dsr_pdu_len, dissect_dsr_message, data); }</p><p>Main decoding logic: static void dissect_dsr_message(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree <em>tree, void</em> data <em>U</em>) { }</p><p>Query: Whether the above approach that I am using is valid? I am facing a problem where in 1st tcp_dissect_pdus() is calling the function properly but 2nd tcp_dissect_pdus() is not calling the decoding function at all.</p><p>Experts, Can you please help me out by sharing your valuable knowledge on this whether what should be done to handle this multiple TLV's scenario. ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_dissect_pdus" rel="tag" title="see questions tagged &#39;tcp_dissect_pdus&#39;">tcp_dissect_pdus</span> <span class="post-tag tag-link-mutiple" rel="tag" title="see questions tagged &#39;mutiple&#39;">mutiple</span> <span class="post-tag tag-link-tlv" rel="tag" title="see questions tagged &#39;tlv&#39;">tlv</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '15, 09:45</strong></p><img src="https://secure.gravatar.com/avatar/dafc36fc00117ac212888f2e683c56ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunilking&#39;s gravatar image" /><p><span>sunilking</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunilking has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-40438" class="comments-container"></div><div id="comment-tools-40438" class="comment-tools"></div><div class="clear"></div><div id="comment-40438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

