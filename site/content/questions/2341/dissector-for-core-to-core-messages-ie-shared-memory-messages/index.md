+++
type = "question"
title = "dissector for core to core messages, ie shared memory messages"
description = '''I have to write a dissector for core to core messages. These are the messages send between nodes in a shared memory.  So on top of what protocol must this be based?? Is it possible that i design core to core in such a way that it is not based on top of any protocol at all?? Real Confusion, Please he...'''
date = "2011-02-15T01:29:00Z"
lastmod = "2011-02-15T04:27:00Z"
weight = 2341
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/2341" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dissector for core to core messages, ie shared memory messages](/questions/2341/dissector-for-core-to-core-messages-ie-shared-memory-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2341-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to write a dissector for core to core messages. These are the messages send between nodes in a shared memory.</p><p>So on top of what protocol must this be based?? Is it possible that i design core to core in such a way that it is not based on top of any protocol at all??</p><p>Real Confusion, Please help anyone?? Sid</p></div><div id="question-tags" class="tags-container tags">dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '11, 01:29</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2341" class="comments-container"><span id="2345"></span><div id="comment-2345" class="comment"><div id="post-2345-score" class="comment-score"></div><div class="comment-text"><p>Is that possible only if I am capturing in pcap format?? I have a trace to check out my output but that is in cap format.</p><p>By the way, I wrote the dissector for core to core messages. On compiling wireshark compiles perfectly fine. In my source code I have called the ethernet dissector. I have used the following lines.</p><p>//to call ethernet dissector</p><p>int reported_length;</p><p>reported _ length = tvb_length(tvb)-offset;</p><p>next _ tvb = tvb _ new _ subset(tvb, offset, reported_length, -1);</p><p>call _ dissector(eth _ withoutfcs _ handle, next _ tvb, pinfo,tree);</p><p>//In the proto_ reg_ handoff_ccm function</p><pre><code>    dissector_handle_t ccm_handle;
    eth_withoutfcs_handle = find_dissector(&quot;eth_withoutfcs&quot;);

ccm_handle = new_create_dissector_handle(dissect_ccm, proto_ccm);
    dissector_add(&quot;wtap_encap&quot;, WTAP_ENCAP_CCM, ccm_handle);</code></pre><p>However, when I run wireshark after compiling and open a trace that I have for core to core messages, it shows a blank trace. It says, no packets captured.</p><p>Is there a problem with my code?? Please help??</p><p>Thanks and Regards, Sidharth</p></div><div id="comment-2345-info" class="comment-info"><span class="comment-age">(15 Feb '11, 05:44)</span> sid</div></div><span id="2346"></span><div id="comment-2346" class="comment"><div id="post-2346-score" class="comment-score"></div><div class="comment-text"><ol><li><p>I suggest that you move this discussion to the [email protected] mailing list. ask.wireshark.org is not really intended for extended discussions.</p></li><li><p>When writing a dissector, the normal starting point is a specification of the protocol. Is there a specification ? Can you provide a link to same ?</p></li></ol><p>3.If you only have a capture, things get more difficult.</p><p>re: "a trace that I have for core to core messages"</p><p>What does capinfos say about the trace ?</p><p>(Please use [email protected] to continue this discussion).</p></div><div id="comment-2346-info" class="comment-info"><span class="comment-age">(15 Feb '11, 07:37)</span> Bill Meier ♦♦</div></div><span id="2359"></span><div id="comment-2359" class="comment"><div id="post-2359-score" class="comment-score"></div><div class="comment-text"><p>Hey Bill, (first, thanks indeed for your time. Really appreciate)</p><p>//I am giving you a specification of the protocol. And by the way, I have subscribed to wireshark-dev mailing list. I will move the discussion there. In the meantime, please keep the discussion alive. Thanks. And by the way, I am relatively new to this . So how to find out what capinfos say about the trace??</p><p>thanks,</p><p>typedef struct nspr_ c2ctrace_v23</p><p>{</p><pre><code>    NSPR_HEADER3B_V22(c2c); /* long performance header */

   u08bits c2c_MsgType_MsgPrio;/* Higher order 4 bits is for Type, Lower Order 4 bits for Priority */
    u64bits c2c_AbsTimeHighHdr; /*High resolution absolute time in nanosec*/
    u16bits c2c_MsgSizeOrg;
    u08bits c2c_MsgCoreid; /* Core on which this message captured */
    u08bits c2c_Reserved[3];
    u08bits c2c_SrcCoreid;
    u08bits c2c_DestCoreid;
    u08bits c2c_Message[0];</code></pre><p>} nspr_ c2ctrace_ v23_t;</p></div><div id="comment-2359-info" class="comment-info"><span class="comment-age">(15 Feb '11, 21:19)</span> sid</div></div></div><div id="comment-tools-2341" class="comment-tools"></div><div class="clear"></div><div id="comment-2341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2343"></span>

<div id="answer-container-2343" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2343-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you can capture into pcap format files, you can use one of the user defined DLT's (147-162). You can set in the Wireshark preferences, in DLT_USER, the relation between this DLT and your protocol dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '11, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2343" class="comments-container"></div><div id="comment-tools-2343" class="comment-tools"></div><div class="clear"></div><div id="comment-2343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

