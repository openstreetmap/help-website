+++
type = "question"
title = "Malformed NORM packets"
description = '''When I do a capture using the NORM protocol I receive an error message saying that my CMD CC packets are malformed. I believe I’ve narrowed the problem down to the Congestion Control subtree. When it reaches the Congestion Control part, Wireshark creates hundreds of Congestion Control subtrees fille...'''
date = "2013-09-11T08:15:00Z"
lastmod = "2013-09-11T11:39:00Z"
weight = 24577
keywords = [ "malformed", "norm", "congestion" ]
aliases = [ "/questions/24577" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed NORM packets](/questions/24577/malformed-norm-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24577-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I do a capture using the NORM protocol I receive an error message saying that my CMD CC packets are malformed. I believe I’ve narrowed the problem down to the Congestion Control subtree. When it reaches the Congestion Control part, Wireshark creates hundreds of Congestion Control subtrees filled completely with zeroes, creating a bigger packet than Wireshark is expecting. Here is the section of the code that dissects NORM cmd(cc) packets:</p><pre><code>static guint dissect_norm_cmd_cc(struct _norm *norm, proto_tree *tree,
 tvbuff_t *tvb, guint offset, packet_info *pinfo _U_)
{
  proto_tree_add_item(tree, hf.reserved, tvb, offset, 1, ENC_NA); offset ++;
  proto_tree_add_item(tree, hf.cc_sequence, tvb, offset, 2, ENC_BIG_ENDIAN); offset += 2;

  proto_tree_add_item(tree, hf.cc_sts, tvb, offset, 4, ENC_BIG_ENDIAN); offset += 4;
  proto_tree_add_item(tree, hf.cc_stus, tvb, offset, 4, ENC_BIG_ENDIAN); offset += 4;
  if (offset &lt; hdrlen2bytes(norm-&gt;hlen)) {
    struct _fec_ptr f;
    memset(&amp;f, 0, sizeof f);
    f.fec = &amp;norm-&gt;fec;
    f.hf = &amp;hf.fec;
    f.ett = &amp;ett.fec;
    f.prefs = &amp;preferences.fec;
    offset = dissect_norm_hdrext(norm, &amp;f, tree, tvb, offset, pinfo);
  }
  while (tvb_reported_length_remaining(tvb, offset) &gt; 0) {
    proto_item *ti, *tif;
    proto_tree *cc_tree, *flag_tree;
    double grtt;
    ti = proto_tree_add_text(tree, tvb, offset, 8, &quot;Congestion Control&quot;);
    cc_tree = proto_item_add_subtree(ti, ett.congestioncontrol);
    proto_tree_add_item(cc_tree, hf.cc_node_id, tvb, offset, 4, ENC_BIG_ENDIAN); offset += 4;
    tif = proto_tree_add_item(cc_tree, hf.cc_flags, tvb, offset, 1, ENC_BIG_ENDIAN);
    flag_tree = proto_item_add_subtree(tif, ett.flags);
    proto_tree_add_item(flag_tree, hf.cc_flags_clr, tvb, offset, 1, ENC_BIG_ENDIAN);
    proto_tree_add_item(flag_tree, hf.cc_flags_plr, tvb, offset, 1, ENC_BIG_ENDIAN);
    proto_tree_add_item(flag_tree, hf.cc_flags_rtt, tvb, offset, 1, ENC_BIG_ENDIAN);
    proto_tree_add_item(flag_tree, hf.cc_flags_start, tvb, offset, 1, ENC_BIG_ENDIAN);
    proto_tree_add_item(flag_tree, hf.cc_flags_leave, tvb, offset, 1, ENC_BIG_ENDIAN);
    offset += 1;
    grtt = UnquantizeRtt(tvb_get_guint8(tvb, offset));
    proto_tree_add_double(cc_tree, hf.cc_rtt, tvb, offset, 1, grtt); offset += 1;
    grtt = UnquantizeSendRate(tvb_get_ntohs(tvb, offset));
    proto_tree_add_double(cc_tree, hf.cc_rate, tvb, offset, 2, grtt); offset += 2;
  }
  return offset;
}</code></pre><p>The problem seems to be occurring in the “while” loop since Wireshark seems to recognize everything before that point. Sorry I cannot post a screenshot of the capture itself. I am using Wireshark-1.8.6 and the full code is located under /epan/dissectors/packet-rmt-norm.c.<br />
</p><p>I am fairly new to Wireshark so any advice on how to make Wireshark recognize this packet and fill it with useful information (activate the flags, register the node ID, etc.) would be much appreciated.</p></div><div id="question-tags" class="tags-container tags">malformed norm congestion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '13, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/64a2be75a7a31bf1ba580e40acc8dab3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Torbett&#39;s gravatar image" /><p>Torbett<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Torbett has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Sep '13, 08:32</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-24577" class="comments-container"></div><div id="comment-tools-24577" class="comment-tools"></div><div class="clear"></div><div id="comment-24577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24586"></span>

<div id="answer-container-24586" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24586-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://tools.ietf.org/html/rfc3940#section-4.2.3.4">Section 4.2.3.4 of RFC 3940</a> states, <em>"The list length can be inferred from the length of the NORM_CMD(CC) message."</em></p><p>It looks like Wireshark is assuming that all remaining bytes in the packet are part of the <code>"cc_node_list"</code>, rather than stopping dissection according to the <code>hdr_len</code> field in the <a href="http://tools.ietf.org/html/rfc3940#section-4.1">NORM Common Message Header</a>.</p><p>To quote:</p><pre><code>The 8-bit &quot;hdr_len&quot; field indicates the number of 32-bit words that
comprise the given message&#39;s header portion.  This is used to
facilitate header extensions that may be applied.  The presence of
header extensions are implied when the &quot;hdr_len&quot; value is greater
than the base value for the given message &quot;type&quot;.</code></pre><p>Please <a href="https://bugs.wireshark.org/bugzilla/">file a bug</a> and attach a sample capture file for testing. It need only be a single packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '13, 11:39</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24586" class="comments-container"><span id="24606"></span><div id="comment-24606" class="comment"><div id="post-24606-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately I'm not allowed to upload a sample capture. Do you have any suggestions about anything I can tweak in the source code on my end and fix the bug myself?</p></div><div id="comment-24606-info" class="comment-info"><span class="comment-age">(12 Sep '13, 05:02)</span> Torbett</div></div><span id="24609"></span><div id="comment-24609" class="comment"><div id="post-24609-score" class="comment-score"></div><div class="comment-text"><p>I'd suggest filing a bug report first, that way if someone decides to look into it and provide a patch, that person can post it to the bug report for you to apply and test.</p><p>If the patch turns out to be faulty in your testing, then you can either provide feedback or modify the patch yourself and post an updated patch to the bug report. After review, the patch can then be committed to the archive and scheduled to be backported, if applicable.</p><p>Filing a bug will track the problem much better than this Q&amp;A site will. (But you may reference this question in the bug report.)</p></div><div id="comment-24609-info" class="comment-info"><span class="comment-age">(12 Sep '13, 08:48)</span> cmaynard ♦♦</div></div><span id="25112"></span><div id="comment-25112" class="comment"><div id="post-25112-score" class="comment-score"></div><div class="comment-text"><p>By changing <code>while (tvb_reported_length_remaining(tvb, offset) &gt; 0</code> to <code>while (offset &lt; hdrlen2bytes(hlen))</code>, the Malformed Packet error no longer appears in my capture. However, the packet size is still huge. I'm expecting a packet size of 78 bytes and Im still getting a 2074 byte packet for CMD CC. Now instead of those all being Congestion Control Subtrees filled with zeros, 2004 of those bytes now are listed as "Payload" but they are still completely filled with zeros. Is there any way to fix this? I believe this is due to the way that <code>tvb_reported_length_remaining(tvb, offset)</code> collects its information but I could be wrong. Once again I'm sorry I can't post a sample capture.</p></div><div id="comment-25112-info" class="comment-info"><span class="comment-age">(23 Sep '13, 05:30)</span> Torbett</div></div><span id="25117"></span><div id="comment-25117" class="comment"><div id="post-25117-score" class="comment-score"></div><div class="comment-text"><p>Right, that was the change I made to resolve <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9138">bug 9138</a>.</p><p>Wireshark displays any remaining data as "payload", so the frame size is apparently too big. That's likely a bug in the sending application.</p></div><div id="comment-25117-info" class="comment-info"><span class="comment-age">(23 Sep '13, 07:51)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-24586" class="comment-tools"></div><div class="clear"></div><div id="comment-24586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

