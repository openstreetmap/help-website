+++
type = "question"
title = "reassembly not working for LTE-based protocol"
description = '''Hi,  Im writing a dissector for our LTE based protocol. Iam working on fragmented packets.  These are ethernet packets that are fragmented with some limitation message payload size , Fragment beginning, mid and last for indication as in what part of the fragment packet. I have used the &quot;fragment_add...'''
date = "2014-12-10T11:38:00Z"
lastmod = "2014-12-10T11:38:00Z"
weight = 38514
keywords = [ "reassembly" ]
aliases = [ "/questions/38514" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [reassembly not working for LTE-based protocol](/questions/38514/reassembly-not-working-for-lte-based-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38514-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Im writing a dissector for our LTE based protocol. Iam working on fragmented packets. These are ethernet packets that are fragmented with some limitation message payload size , Fragment beginning, mid and last for indication as in what part of the fragment packet. I have used the "fragment_add_seq_check()" and the "process_reassembled_data()" functions to reassemble the packets but not worked out.</p><pre><code>         frag_head = fragment_add_seq_check(&amp;lte_reassembly_table, tvb, 
                     offset,/* This is not zero iam processing in mid
                     pinfo,
                     msg_seqnum, 
      /* ID for fragments belonging together my begin mid last message will have the same seq number*/
                      NULL,
                      msg_seqid, /* message sequence id  I hv set to 0,1,2  */
                      tvb_length_remaining(tvb,offset), /* fragment length - to the end */
                      more_frags); /* More fragments? set to FALSE when last fragment*/

                                            save_fragmented = pinfo-&gt;fragmented;
                                            pinfo-&gt;fragmented = save_fragmented;</code></pre><p>I get no reassembled packets. Fragment not working. Any help will be much appreciated</p></div><div id="question-tags" class="tags-container tags">reassembly</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '14, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/5d1d9f9786aaec70ca3233405dcba067?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vinod&#39;s gravatar image" /><p>Vinod<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vinod has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Dec '14, 18:17</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-38514" class="comments-container"></div><div id="comment-tools-38514" class="comment-tools"></div><div class="clear"></div><div id="comment-38514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

