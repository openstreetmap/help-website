+++
type = "question"
title = "How to enable FP-Hint, MAC-es dissector"
description = '''My traffic is built with protocols like below: IP UDP MAC-es RLC TCP but wireshark can only decode frame up to UDP layer. Aside from writing my own dissector, anything else? Thanks!'''
date = "2012-05-10T22:51:00Z"
lastmod = "2012-05-12T05:47:00Z"
weight = 10917
keywords = [ "umts", "rlc" ]
aliases = [ "/questions/10917" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to enable FP-Hint, MAC-es dissector](/questions/10917/how-to-enable-fp-hint-mac-es-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10917-score" class="post-score" title="current number of votes">0</div><span id="post-10917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My traffic is built with protocols like below: IP UDP MAC-es RLC TCP</p><p>but wireshark can only decode frame up to UDP layer. Aside from writing my own dissector, anything else?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-umts" rel="tag" title="see questions tagged &#39;umts&#39;">umts</span> <span class="post-tag tag-link-rlc" rel="tag" title="see questions tagged &#39;rlc&#39;">rlc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '12, 22:51</strong></p><img src="https://secure.gravatar.com/avatar/6b388fadeb7e3e0f4243a7f60e517bc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leonizeme&#39;s gravatar image" /><p><span>leonizeme</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leonizeme has no accepted answers">0%</span></p></div></div><div id="comments-container-10917" class="comments-container"><span id="10928"></span><div id="comment-10928" class="comment"><div id="post-10928-score" class="comment-score"></div><div class="comment-text"><p>If you are not writing out a header in the FP-hint format, I don't think it will help you.</p><p>If you <em>do</em> write out this information, you could try adding something like:</p><p>dissector_handle_t fp_hint_handle = find_dissector("fp_hint"); dissector_add_handle("udp.port", fp_hint_handle); / <em>for 'decode-as'</em> /</p><p>to proto_reg_handoff_fp_hint().</p><p>This will let you right click 'Decode as' on those PDUs and choose FP-Hint as the protocol to use. If this is useful to use, this change can be submitted. The FP-hint format doesn't look too complicated.</p></div><div id="comment-10928-info" class="comment-info"><span class="comment-age">(11 May '12, 03:39)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="10931"></span><div id="comment-10931" class="comment"><div id="post-10931-score" class="comment-score"></div><div class="comment-text"><p>Another approach would be do look at the UDP-framing that has been implemented for RLC (and used as a heuristic dissector). See <a href="http://wiki.wireshark.org/RLC">http://wiki.wireshark.org/RLC</a> for details (including test code for encoding UDP frames in this format). A similar thing is also done for LTE MAC, RLC and PDCP, but UMTS RLC is most similar in that it will also need to supply FP information. I do not have the time to implement this at the moment, but would be happy if you want to submit a patch.</p></div><div id="comment-10931-info" class="comment-info"><span class="comment-age">(11 May '12, 03:49)</span> <span class="comment-user userinfo">MartinM</span></div></div></div><div id="comment-tools-10917" class="comment-tools"></div><div class="clear"></div><div id="comment-10917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10918"></span>

<div id="answer-container-10918" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10918-score" class="post-score" title="current number of votes">0</div><span id="post-10918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you have all the other headers encapsulated, you could just remove everything up to the UDP header with the pcap editor of bittwist (bittwiste).</p><p><strong>Ubuntu:</strong></p><blockquote><p><code>apt-get install bittwist</code></p></blockquote><p>Try this first. This will remove "standard" Ethernet, IP and UDP headers.<br />
</p><blockquote><p><code>bittwiste -I orig.cap -O stripped.cap -D 42 -M 1</code></p></blockquote><p>If there are VLAN tags, IP Options, etc. you'll have to figure out the correct length with wireshark and then cut off the right number of bytes.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '12, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-10918" class="comments-container"><span id="10920"></span><div id="comment-10920" class="comment"><div id="post-10920-score" class="comment-score"></div><div class="comment-text"><p>Thanks</p><p>I tried, but I still got no decoding. I remove bytes up to UDP header, using editcap, but still no decoding of FP-hint. I have enabled FP-hint.</p><p>Could you help? Maybe I missed some settings or plug-ins?</p></div><div id="comment-10920-info" class="comment-info"><span class="comment-age">(11 May '12, 01:02)</span> <span class="comment-user userinfo">leonizeme</span></div></div><span id="10921"></span><div id="comment-10921" class="comment"><div id="post-10921-score" class="comment-score"></div><div class="comment-text"><p>can you upload 3-4 packets to <a href="http://cloudshark.org">cloudshark.org</a>?</p><p>BTW: How comes, your data is encapsulated in a UDP packet?</p></div><div id="comment-10921-info" class="comment-info"><span class="comment-age">(11 May '12, 01:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10952"></span><div id="comment-10952" class="comment"><div id="post-10952-score" class="comment-score"></div><div class="comment-text"><blockquote><p>BTW: How comes, your data is encapsulated in a UDP packet?</p></blockquote><p>Probably because it's UMTS traffic - various flavors of mobile phone network traffic seem to be encapsulated in UDP packets in order to feed them to analyzers such as Wireshark.</p><p>That means the problem isn't the UDP encapsulation, the problem is probably as described by Martin Mathieson in his comments.</p></div><div id="comment-10952-info" class="comment-info"><span class="comment-age">(11 May '12, 19:51)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="10958"></span><div id="comment-10958" class="comment"><div id="post-10958-score" class="comment-score"></div><div class="comment-text"><p>fp | mac | rlc is relayed over wires on the IuB interface, over atm or udp. We dont support decoding the real traffic like this, although Anders has been starting to configure based on signalling info.. Fp-hint and fp are not the same thing though.</p></div><div id="comment-10958-info" class="comment-info"><span class="comment-age">(12 May '12, 01:37)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="10962"></span><div id="comment-10962" class="comment"><div id="post-10962-score" class="comment-score"></div><div class="comment-text"><p>It should be possible to add preferenses(UAT) to the fp-hint dissector to set up conversation data that will dissect real FP UDP traffic.</p></div><div id="comment-10962-info" class="comment-info"><span class="comment-age">(12 May '12, 05:47)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-10918" class="comment-tools"></div><div class="clear"></div><div id="comment-10918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

