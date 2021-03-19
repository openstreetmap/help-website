+++
type = "question"
title = "How to reassemble packet in text-based protocol"
description = '''I have created a dissector for a line-based protocol but have some problems when data are bigger than packet size. When the data is too big, I need to reassemble a number of packets to have a complete data before processing it. Here you can find a part of my dissector. I need your help for if (packe...'''
date = "2011-04-06T09:34:00Z"
lastmod = "2011-04-07T23:16:00Z"
weight = 3379
keywords = [ "development", "dissector", "reassemble", "tcp" ]
aliases = [ "/questions/3379" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to reassemble packet in text-based protocol](/questions/3379/how-to-reassemble-packet-in-text-based-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3379-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have created a dissector for a line-based protocol but have some problems when data are bigger than packet size. When the data is too big, I need to reassemble a number of packets to have a complete data before processing it. Here you can find a part of my dissector. I need your help for <code>if (packet_end != 0x0A){} else {}</code>. I don't know how proceed and what functions to use for reassembling packets.</p><pre><code>static void dissect__textbasedprotocol(tvbuff_t *tvb, packet_info *pinfo,
                                       proto_tree *tree)
{
    guint8 packet_end = 0;
    tvbuff_t *working_tvb = NULL;
    gint offset_actu = 0;
    packet_end = tvb_get_guint8(
        tvb, tvb_reported_length_remaining(tvb, offset_actu) - 1);
    if (packet_end != 0x0A) // end of this packet is NOT end of data
    {
    } else {
        working_tvb = tvb; // packet contain an complete data \n and terminated.
    }
    while (tvb_reported_length_remaining(working_tvb, offset_actu) &gt; 0) {
        // Dissector work with complete command \n terminated.
    }
}</code></pre></div><div id="question-tags" class="tags-container tags">development dissector reassemble tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '11, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/c492c0694d9771d0dd649cc6e230e70d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thibault&#39;s gravatar image" /><p>Thibault<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thibault has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '14, 10:53</p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-3379" class="comments-container"></div><div id="comment-tools-3379" class="comment-tools"></div><div class="clear"></div><div id="comment-3379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3396"></span>

<div id="answer-container-3396" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3396-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When you have to reassemble payload of a protocol without a length header, you should use the point <em>2.7.2 Modifying the pinfo struct.</em> of the README.developer.</p><p>BTW: this section has a code fragment, that works with strings terminated by a <code>'\0'</code>. Try toreplace <code>'\0'</code> by <code>'\n'</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '11, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/585595b6a24df9b742ebc186788e9a8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harper&#39;s gravatar image" /><p>harper<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harper has no accepted answers">0%</span></p></div></div><div id="comments-container-3396" class="comments-container"></div><div id="comment-tools-3396" class="comment-tools"></div><div class="clear"></div><div id="comment-3396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

