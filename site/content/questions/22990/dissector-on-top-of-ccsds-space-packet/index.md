+++
type = "question"
title = "Dissector on top of CCSDS Space Packet"
description = '''Hello,  I have written a dissector that works on top of the Space Packet protocol (packet-ccsds) that at the same time works on top UDP in my application. My question is: As the protocol is not working neither on top of UDP nor on TCP how should I code the protocol registration in this case? More sp...'''
date = "2013-07-16T00:59:00Z"
lastmod = "2013-07-16T08:06:00Z"
weight = 22990
keywords = [ "proto_register", "dissector", "protocol" ]
aliases = [ "/questions/22990" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector on top of CCSDS Space Packet](/questions/22990/dissector-on-top-of-ccsds-space-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22990-score" class="post-score" title="current number of votes">0</div><span id="post-22990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have written a dissector that works on top of the Space Packet protocol (packet-ccsds) that at the same time works on top UDP in my application. My question is: As the protocol is not working neither on top of UDP nor on TCP how should I code the protocol registration in this case? More specifically, how should be the "proto_reg_handoff" routine?</p><p>This routine for CCSDS is the following:</p><pre><code>proto_reg_handoff_ccsds(void){
dissector_add_handle ( &quot;udp.port&quot;, find_dissector(&quot;ccsds&quot;) ); /* for &#39;decode as&#39; */
data_handle = find_dissector(&quot;data&quot;);}</code></pre><p>But as this protocol works on top of CCSDS I do not know how to modify it.</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_register" rel="tag" title="see questions tagged &#39;proto_register&#39;">proto_register</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '13, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/fb277051913f5111a6888c8c1fa78bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juan_Kash&#39;s gravatar image" /><p><span>Juan_Kash</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juan_Kash has no accepted answers">0%</span></p></div></div><div id="comments-container-22990" class="comments-container"></div><div id="comment-tools-22990" class="comment-tools"></div><div class="clear"></div><div id="comment-22990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22991"></span>

<div id="answer-container-22991" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22991-score" class="post-score" title="current number of votes">2</div><span id="post-22991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Juan_Kash has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have no idea how CCSDS works but how does the actual protocol stack find the next protocol to hand off to? You will have to add code to the CCSDS dissector to hand of to the next protocol either by a preferense or by adding a register table where sub dissector can register or some other method.(register_dissector_table())</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-22991" class="comments-container"><span id="23003"></span><div id="comment-23003" class="comment"><div id="post-23003-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the answer! I added a register table to ccsds:</p><p>ccsds_dissector_table = register_dissector_table("ccsds.apid", "CCSDS apid", FT_UINT16, BASE_DEC);</p><p>And also modify the proto_reg_handoff of my protocol this way:</p><p>void proto_reg_handoff_cfdp(void) { dissector_handle_t cfdp_handle; cfdp_handle = create_dissector_handle(dissect_cfdp, proto_cfdp);<br />
dissector_add_uint("ccsds.apid", 2045, cfdp_handle); }</p><p>I can see it in the menu Internal-&gt; Dissector tables but still does not work. By doing it this way the protocol is supposed to be dissected automatically or do I have to use the menu Decode as...?</p></div><div id="comment-23003-info" class="comment-info"><span class="comment-age">(16 Jul '13, 05:00)</span> <span class="comment-user userinfo">Juan_Kash</span></div></div><span id="23004"></span><div id="comment-23004" class="comment"><div id="post-23004-score" class="comment-score">1</div><div class="comment-text"><p>In the CCDSDS dissector do you use the dissector table to call the "next" dissetor for the payload? Something like this from the GTP dissector: if (length &gt; 2) { next_tvb = tvb_new_subset(tvb, offset, length-2, length-2); if(!dissector_try_uint(gtp_priv_ext_dissector_table, ext_id, next_tvb, pinfo, ext_tree_priv_ext)){ proto_tree_add_item(ext_tree_priv_ext, hf_gtp_ext_val, tvb, offset, length - 2, ENC_NA); } }</p></div><div id="comment-23004-info" class="comment-info"><span class="comment-age">(16 Jul '13, 05:06)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="23041"></span><div id="comment-23041" class="comment"><div id="post-23041-score" class="comment-score"></div><div class="comment-text"><p>Ok, now the protocol gets called from CCSDS. Thank you!</p></div><div id="comment-23041-info" class="comment-info"><span class="comment-age">(16 Jul '13, 08:04)</span> <span class="comment-user userinfo">Juan_Kash</span></div></div><span id="23044"></span><div id="comment-23044" class="comment"><div id="post-23044-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-23044-info" class="comment-info"><span class="comment-age">(16 Jul '13, 08:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-22991" class="comment-tools"></div><div class="clear"></div><div id="comment-22991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

