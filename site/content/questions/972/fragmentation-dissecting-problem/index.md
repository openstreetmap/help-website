+++
type = "question"
title = "Fragmentation dissecting Problem"
description = '''Hi, I&#x27;m writing a dissector for our LTE PHY packets. I have started working on fragmented packets. These are ethernet packets that are fragmented with some propriatery limitation. Nevertheless we have a PI header (under the ethernet header) that is always there in any fragment. The PI header contain...'''
date = "2010-11-16T01:44:00Z"
lastmod = "2010-11-17T10:18:00Z"
weight = 972
keywords = [ "fragmentation", "dissector" ]
aliases = [ "/questions/972" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fragmentation dissecting Problem](/questions/972/fragmentation-dissecting-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-972-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm writing a dissector for our LTE PHY packets. I have started working on fragmented packets. These are ethernet packets that are fragmented with some propriatery limitation. Nevertheless we have a PI header (under the ethernet header) that is always there in any fragment. The PI header contains what I thought is sefficient data for the fragment functions such as: size - the size of the PI message payload, Fragment (full, first, mid and last for indication as in what part of the fragmented packet are we) and sequence - message sequence index. I have used the "fragment_add_seq_check()" and the "process_reassembled_data()" functions to reassemble the packets but with no success. I get no reassembled packets. Only an indication on the fragments. I followed the "How to reassmble split packet" section 9.4 in the developers guid. I also went through the code over and over and see no problem. It seems that there is no use for the "LAST" indication of the fragmentation. After the last one I should have got a reassmbled packet. Any help will be much appriciated</p><p>Yosi</p></div><div id="question-tags" class="tags-container tags">fragmentation dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '10, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/8ab0d645ffb3d50a34f8ef582bb92061?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yosi&#39;s gravatar image" /><p>Yosi<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yosi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Nov '10, 04:34</p></div></div><div id="comments-container-972" class="comments-container"><span id="974"></span><div id="comment-974" class="comment"><div id="post-974-score" class="comment-score"></div><div class="comment-text"><p>Yosi, there is no such thing as a fragmented Ethernet frame. I'm not a developer, but I'm pretty sure all code having to do with fragments is limited to IP packets (where fragmentation occurs). But it sounds like you're doing your own header on top of Ethernet (new ethertype/LLC?).</p></div><div id="comment-974-info" class="comment-info"><span class="comment-age">(16 Nov '10, 09:12)</span> hansangb</div></div><span id="981"></span><div id="comment-981" class="comment"><div id="post-981-score" class="comment-score"></div><div class="comment-text"><p>Let me clerify. The fragmentation is not on the Ethernet of course. We are building a header on top of the ethernet. Each fragment is an ethernet packet that has a PI header with the data about the fragmented data. The PI payload is fragmented</p></div><div id="comment-981-info" class="comment-info"><span class="comment-age">(17 Nov '10, 00:09)</span> Yosi</div></div></div><div id="comment-tools-972" class="comment-tools"></div><div class="clear"></div><div id="comment-972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="989"></span>

<div id="answer-container-989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-989-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yosi, I had a look on your code on <a href="http://seclists.org/wireshark/2010/Nov/279">http://seclists.org/wireshark/2010/Nov/279</a></p><pre><code>frag_msg = fragment_add_seq_check(tvb,offset,pinfo,
          msg_id,
          dan_fragment_table,
          dan_reassembled_table,
          msg_seq,tvb_length_remaining(tvb,offset),
          (flags == FR_LAST));</code></pre><p>The <em>more_frags</em> parameter in <em>fragment_add_seq_check</em> must be <em>false</em> when you reach the last fragment, so consider using <em>(flags != FR_LAST)</em></p><p>Dev guide example might be confusing :</p><pre><code>frag_msg = fragment_add_seq_check(tvb, offset, pinfo,
    msg_seqid, /* ID for fragments belonging together */
    msg_fragment_table, /* list of message fragments */
    msg_reassembled_table, /* list of reassembled messages */
    msg_num, /* fragment sequence number */
    tvb_length_remaining(tvb, offset), /* fragment length - to the end */
    flags &amp; FL_FRAG_LAST); /* More fragments? */</code></pre><p>Emmanuel</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '10, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/2282d6ca42253cbf6aa80c00be6af1b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manux&#39;s gravatar image" /><p>manux<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manux has no accepted answers">0%</span></p></div></div><div id="comments-container-989" class="comments-container"></div><div id="comment-tools-989" class="comment-tools"></div><div class="clear"></div><div id="comment-989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

