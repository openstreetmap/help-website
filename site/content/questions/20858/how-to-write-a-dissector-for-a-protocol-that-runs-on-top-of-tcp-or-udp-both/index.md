+++
type = "question"
title = "How to write a dissector for a protocol that runs on top of TCP or UDP both"
description = '''I&#x27;m a long time developer who is new to wireshark. I&#x27;m actually trying to update the built in C12.22 dissector that is for TCP currently to also use UDP as well, everything else the same. If someone could just send me a new x64 1.8.6 asn1.dll that would be super awesome. If not please tell me how to...'''
date = "2013-04-30T23:10:00Z"
lastmod = "2013-05-01T00:31:00Z"
weight = 20858
keywords = [ "udp", "dissector", "tcp" ]
aliases = [ "/questions/20858" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to write a dissector for a protocol that runs on top of TCP or UDP both](/questions/20858/how-to-write-a-dissector-for-a-protocol-that-runs-on-top-of-tcp-or-udp-both)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20858-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a long time developer who is new to wireshark. I'm actually trying to update the built in C12.22 dissector that is for TCP currently to also use UDP as well, everything else the same. If someone could just send me a new x64 1.8.6 asn1.dll that would be super awesome. If not please tell me how to setup a new dissector or modify the C12.22 dissector to use both TCP and UDP underneath. Thanks.</p></div><div id="question-tags" class="tags-container tags">udp dissector tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '13, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/6190acb3ec65bd179cfb482ea5cc46af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AceHack&#39;s gravatar image" /><p>AceHack<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AceHack has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Apr '13, 23:12</p></div></div><div id="comments-container-20858" class="comments-container"></div><div id="comment-tools-20858" class="comment-tools"></div><div class="clear"></div><div id="comment-20858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20861"></span>

<div id="answer-container-20861" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20861-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Raise a bug report, including a small sample trace to try a patch with.</p><p>A patch would look something like:</p><pre><code>Index: asn1/c1222/packet-c1222-template.c
===================================================================
--- asn1/c1222/packet-c1222-template.c  (revision 49103)
+++ asn1/c1222/packet-c1222-template.c  (working copy)
@@ -79,6 +79,7 @@
 #define C1222_CMD_TIMING_SETUP 0x71

 static dissector_handle_t c1222_handle=NULL;
+static dissector_handle_t c1222_udp_handle=NULL;

 /* Initialize the protocol and registered fields */
 static int proto_c1222 = -1;
@@ -993,7 +994,7 @@
  * \param tree
  */
 static void
-dissect_c1222_full(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
+dissect_c1222_common(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
 {
     proto_item      *c1222_item = NULL;
     proto_tree     *c1222_tree = NULL;
@@ -1041,7 +1042,7 @@
 dissect_c1222(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
 {
     tcp_dissect_pdus(tvb, pinfo, tree, c1222_desegment, 5,
-           get_c1222_message_len, dissect_c1222_full);
+           get_c1222_message_len, dissect_c1222_common);
 }

 /*--- proto_register_c1222 -------------------------------------------*/
@@ -1328,7 +1329,9 @@

     if( !initialized ) {
         c1222_handle = create_dissector_handle(dissect_c1222, proto_c1222);
+               c1222_udp_handle = create_dissector_handle(dissect_c1222_common,
 proto_c1222);
         dissector_add_uint(&quot;tcp.port&quot;, global_c1222_port, c1222_handle);
+        dissector_add_uint(&quot;udp.port&quot;, global_c1222_port, c1222_udp_handle);
         initialized = TRUE;
     }
 }</code></pre><p>and regenerate the dissector(run nmake in the asn1/c1222 dir and then in top dir).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '13, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 May '13, 01:37</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-20861" class="comments-container"><span id="20864"></span><div id="comment-20864" class="comment"><div id="post-20864-score" class="comment-score"></div><div class="comment-text"><p>Comitted the patch in Committed revision 49104. (Related bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8620)">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8620)</a></p></div><div id="comment-20864-info" class="comment-info"><span class="comment-age">(01 May '13, 01:39)</span> Anders ♦</div></div></div><div id="comment-tools-20861" class="comment-tools"></div><div class="clear"></div><div id="comment-20861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

