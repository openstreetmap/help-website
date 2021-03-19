+++
type = "question"
title = "How does a dissector report payload back to Wireshark?"
description = '''If I&#x27;m writing a dissector for a protocol whose payload could contain a message in another protocol, how do I signal that fact to Wireshark? How do I let Wireshark know that my dissector hasn&#x27;t fully consumed all the bytes in tvb? From the docs: &quot;Every dissection starts with the Frame dissector whic...'''
date = "2015-11-25T05:23:00Z"
lastmod = "2015-11-25T05:53:00Z"
weight = 47965
keywords = [ "dissector" ]
aliases = [ "/questions/47965" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How does a dissector report payload back to Wireshark?](/questions/47965/how-does-a-dissector-report-payload-back-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47965-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I'm writing a dissector for a protocol whose payload could contain a message in another protocol, how do I signal that fact to Wireshark? How do I let Wireshark know that my dissector hasn't fully consumed all the bytes in tvb?</p><p>From the docs:</p><p>"Every dissection starts with the Frame dissector which dissects the packet details of the capture file itself (e.g. timestamps). From there it passes the data on to the lowest-level data dissector, e.g. the Ethernet dissector for the Ethernet header. The payload is then passed on to the next dissector (e.g. IP) and so on."</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '15, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/141bf84491a151af8ece1484967838d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdgarrison&#39;s gravatar image" /><p>mdgarrison<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdgarrison has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '15, 06:13</p></div></div><div id="comments-container-47965" class="comments-container"></div><div id="comment-tools-47965" class="comment-tools"></div><div class="clear"></div><div id="comment-47965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47966"></span>

<div id="answer-container-47966" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47966-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should call the sub-dissector directly. See README.dissector "Section 1.7 Calling other dissectors".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47966" class="comments-container"><span id="47967"></span><div id="comment-47967" class="comment"><div id="post-47967-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer; I'm thinking more about how a dissector like IP works; it parses its header fields then returns a pointer to the remaining data back to Wireshark, who then invokes the TCP dissector. (Or does the IP dissector call a TCP sub-dissector automatically?)</p><p>Who invokes the TCP dissector -- Wireshark or the IP dissector?</p><p>TIA!</p></div><div id="comment-47967-info" class="comment-info"><span class="comment-age">(25 Nov '15, 06:01)</span> mdgarrison</div></div><span id="47968"></span><div id="comment-47968" class="comment"><div id="post-47968-score" class="comment-score"></div><div class="comment-text"><p>I think it's the IP dissector.</p><p>The IPv4 (and v6) dissector calls ip_try_dissect(), which calls dissectors that have registered in the "ip.proto" table, using the protocol value in the ip header field as the index in the table.</p><p>The tcp dissector registers in that table with its proto value (6).</p><p>Dissector tables are discussed in README.dissector "Section 1.7.1. Dissector Tables".</p></div><div id="comment-47968-info" class="comment-info"><span class="comment-age">(25 Nov '15, 06:22)</span> grahamb ♦</div></div><span id="47974"></span><div id="comment-47974" class="comment"><div id="post-47974-score" class="comment-score"></div><div class="comment-text"><p>Thanks, and that makes sense; the mechanism that's tripping me up is this: It seems to be the responsibility of a dissector to report back any 'undissected' bytes to Wireshark, so that when another dissector's called, its tvb points to the undissected data.<br />
</p><p>How do I (as a dissector) let Wireshark know that there's data remaining left over from my dissection?</p><p>(I appreciate the efforts to explain this, btw -- I'm having difficulty in formulating the right question!)</p></div><div id="comment-47974-info" class="comment-info"><span class="comment-age">(25 Nov '15, 07:42)</span> mdgarrison</div></div><span id="47976"></span><div id="comment-47976" class="comment"><div id="post-47976-score" class="comment-score"></div><div class="comment-text"><p>Assuming you're writing a "new" style dissector (all dissectors should be "new" style, there's a big effort on to convert the old ones), i.e. your dissector registers with new_register_dissector() or via new_create_dissector_handle() then your "dissection" function should be of type new_dissector_t and return an int, which is the amount of data in the protocols PDU.</p><p>See the header for the typedef of new_dissector_t in epan/packet.h:</p><pre><code>/*
 * Dissector that returns:
 *
 *  The amount of data in the protocol&#39;s PDU, if it was able to
 *  dissect all the data;
 *
 *  0, if the tvbuff doesn&#39;t contain a PDU for that protocol;
 *
 *  The negative of the amount of additional data needed, if
 *  we need more data (e.g., from subsequent TCP segments) to
 *  dissect the entire PDU.
 */
typedef int (*new_dissector_t)(tvbuff_t *, packet_info *, proto_tree *, void *);</code></pre></div><div id="comment-47976-info" class="comment-info"><span class="comment-age">(25 Nov '15, 08:01)</span> grahamb ♦</div></div><span id="47977"></span><div id="comment-47977" class="comment"><div id="post-47977-score" class="comment-score"></div><div class="comment-text"><p>When you want to call another dissector on the remaining bytes of a TVB then (usually) you'll want to create a new subset TVB that contains only the (so far undissected - because it's your protocol's payload) bytes. You can then pass that new TVB to the next dissector (so it sees only the thus-far-undissected bytes).</p><p>The API you want is something like <code>tvb_new_subset()</code> (sorry, it's too painful from here to look up the exact API).</p></div><div id="comment-47977-info" class="comment-info"><span class="comment-age">(25 Nov '15, 08:13)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-47966" class="comment-tools"></div><div class="clear"></div><div id="comment-47966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

