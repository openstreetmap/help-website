+++
type = "question"
title = "tcp_dissect_pdu Warning C4013, C4024 and C4047"
description = '''Hi, I&#x27;m currently writing a Wireshark Dissector for a custom message. I&#x27;m trying to dissect the complete TCP Stream and am trying to implement tcp_dissect_pdus to solve this problem. I have the following functions:  (Get foo message length function)  1555 static guint   1556 get_foo_message_len(pack...'''
date = "2015-07-30T14:56:00Z"
lastmod = "2015-07-30T15:37:00Z"
weight = 44655
keywords = [ "tcp_dissect_pdus", "reassembly", "tcp" ]
aliases = [ "/questions/44655" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tcp\_dissect\_pdu Warning C4013, C4024 and C4047](/questions/44655/tcp_dissect_pdu-warning-c4013-c4024-and-c4047)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44655-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm currently writing a Wireshark Dissector for a custom message. I'm trying to dissect the complete TCP Stream and am trying to implement <em>tcp_dissect_pdus</em> to solve this problem. I have the following functions:</p><pre><code> (Get foo message length function)
 1555     static guint 
 1556     get_foo_message_len(packet_info *pinfo _U_, tvbuff_t *tvb, int offset, void *data _U_)
 1557     {
 1558        return (guint)tvb_get_ntohl(tvb, offset+8);
 1559     }

     (dissect foo function)
 1562     static int 
 1563     dissect_foo(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data)
 1564     {
 1565       tcp_dissect_pdus(tvb, pinfo, tree, TRUE, 56, get_foo_message_len, 
 1566                        dissect_foo_message(tvb, pinfo, tree, data), data);
 1567     
 1568       return tvb_captured_length(tvb);
 1569     }

 (dissect foo message function)
 1573     static int
 1574     dissect_foo_message(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data _U_ )
 1575     {
 1576       guint32 size = tvb_captured_length(tvb);
 1577       guint32 offset = 0;
 1578       proto_item *ti = NULL;
 1579       proto_tree *hdr_tree = NULL;
 1580       proto_tree *second_tree = NULL;
        ...
 1641        return tvb_captured_length(tvb);
 1642     }

 (proto_reg_handoff_foo function)
 2942     void proto_reg_handoff_foo(void) {
 2943     //static dissector_handle_t foo_handle;
 2944     static dissector_handle_t foo_tcp_handle;

 2946     //foo_handle = create_dissector_handle(dissect_foo, proto_foo);
 2947     foo_tcp_handle = new_create_dissector_handle(dissect_foo, proto_foo);

 2949     //dissector_add_uint(&quot;tcp.port&quot;, FOO_PORT, foo_handle);
 2950     dissector_add_uint(&quot;tcp.port&quot;, FOO_PORT, foo_tcp_handle);
 2951     }</code></pre><p>And I'm getting the following errors:</p><pre><code> register.c
 packet-foo.c
 packet-foo.c(1565) : error C2220: warning treated as error - no &#39;object&#39; file generated
 packet-foo.c(1565) : warning C4013: &#39;dissect_foo_message&#39; undefined; assuming extern returning int
 packet-foo.c(1565) : warning C4047: &#39;function&#39; : &#39;new_dissector_t&#39; differs in levels of indirection from &#39;int&#39;
 packet-foo.c(1565) : warning C4024: &#39;tcp_dissect_pdus&#39; : different types f
 or formal and actual parameter 7
 NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\amd64\cl.EXE&quot;&#39; : return code &#39;0x2&#39;
 Stop.
 NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\amd64\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
 Stop.
 NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\amd64\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
 Stop.</code></pre><p>I'm currently running Windows 7 Enterprise, Visual Studio 2013 Pro, Qt 5.4, and working on Wireshark 1.99.7 Development Version.</p><p>I've used the Wireshark dissector.README file, the Developer's Guide, and various sites with information about how to use <em>tcp_dissect_pdus</em> and I haven't found any solution to this problem.</p><p>My main goal is to reassemble all the TCP packets and dissect them in technically one big packet since the data that's being sent in every packet is broken into several packets. And inside those several packets are various headers for the information. Each set of information can have a different length. It's just one giant packet broken into many smaller ones for transport.</p><p>Any type of information or advice can help.</p><p>Thank you for your time.</p></div><div id="question-tags" class="tags-container tags">tcp_dissect_pdus reassembly tcp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/66d32f7338820e81bed11c109bb8eaea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J1Ronnie&#39;s gravatar image" /><p>J1Ronnie<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J1Ronnie has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jul '15, 15:01</p></div></div><div id="comments-container-44655" class="comments-container"></div><div id="comment-tools-44655" class="comment-tools"></div><div class="clear"></div><div id="comment-44655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44657"></span>

<div id="answer-container-44657" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44657-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a basic C issue of scope.</p><p>Either move the definition of the <code>dissect_foo_message</code> function before it's used in <code>dissect_foo()</code>, or add a forward declaration before its use.</p><p>In C, if you call a function before its been defined, or a forward declaration has been made, then the compiler assumes the function type is <code>int func(void)</code>. As this is different from the type signature of the 7th parameter to <code>tcp_dissect_pdus()</code> which is <code>new_dissector_t</code> (from packet-tcp.h) which in turn is <code>typedef int (*new_dissector_t)(tvbuff_t *, packet_info *, proto_tree *, void *) (from packet.h)</code>, then the errors you see are generated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '15, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44657" class="comments-container"><span id="44658"></span><div id="comment-44658" class="comment"><div id="post-44658-score" class="comment-score"></div><div class="comment-text"><p>Oh wow... that fixed it!!! Thank you!!!</p></div><div id="comment-44658-info" class="comment-info"><span class="comment-age">(30 Jul '15, 15:46)</span> J1Ronnie</div></div></div><div id="comment-tools-44657" class="comment-tools"></div><div class="clear"></div><div id="comment-44657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

