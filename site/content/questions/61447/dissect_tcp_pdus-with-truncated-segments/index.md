+++
type = "question"
title = "dissect_tcp_pdus with truncated segments"
description = '''I created a lua script to dissect DoIP messages. The header is pretty simple: A version byte, a byte with the bitwise invert of the version, the payload type as two bytes and the payload length as 4 bytes.   function get_doip_length(tvb, pinfo, offset)  -- Callback function to decide how long a PDU ...'''
date = "2017-05-16T15:53:00Z"
lastmod = "2017-05-16T17:32:00Z"
weight = 61447
keywords = [ "tcp_dissect_pdus", "lua", "dissector", "truncated" ]
aliases = [ "/questions/61447" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [dissect\_tcp\_pdus with truncated segments](/questions/61447/dissect_tcp_pdus-with-truncated-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61447-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I created a lua script to dissect DoIP messages. The header is pretty simple: A version byte, a byte with the bitwise invert of the version, the payload type as two bytes and the payload length as 4 bytes.</p><pre><code>function get_doip_length(tvb, pinfo, offset)
    -- Callback function to decide how long a PDU is, so that
    -- Wireshark can reassemble it for us
    local version = tvb(offset, 1):uint()
    local inverse_version = tvb(offset+1, 1):uint()

    if version == 0x02 and inverse_version == 0xFD then
        local payload_length = tvb(offset+4, 4):uint()
        return payload_length + 8 -- Payload length + header size
    else
        return 8 -- Unknown protocol, assume only header is to be reassembled
        -- According to https://www.wireshark.org/lists/wireshark-dev/201610/msg00057.html
    end
end

function doip.dissector(tvb, pinfo, tree)
    dissect_tcp_pdus(tvb, tree, 8, get_doip_length, dissect_doip_pdu)
end</code></pre><p>This works well when the trace is complete. I have payloads of about 16K, which is 12 TCP frames. The 11 first TCP frames are marked <code>[TCP segment of a reassembled PDU]</code> and the last one contains the proper protocol name and all the data.</p><p>However, I sometimes trace also on a small device using <code>tcpdump -s128</code>, because the throughtput is too low <em>(over UART...)</em> and it's better for me to not have the full payload but not drop packets.</p><p>In this case, the dissector doesn't work as expected. The first frame of the PDU is marked as the reassembly, and the length is indeed 16K. But all the 11 remaining frames are not taken into account. Rather, <code>dissect_tcp_pdus</code> tries to match them to a new PDU. I would expect that <code>dissect_tcp_pdus</code> could at least reassemble all the segments, even if the data is not captured (Tvb has indeed a <code>:len()</code> and a <code>:reported_len()</code> functions).</p><p>Is there someting I do wrong?</p></div><div id="question-tags" class="tags-container tags">tcp_dissect_pdus lua dissector truncated</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '17, 15:53</strong></p><img src="https://secure.gravatar.com/avatar/d1a425c7654aa63519f4f45710e2f54c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cilyan&#39;s gravatar image" /><p>Cilyan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cilyan has no accepted answers">0%</span></p></div></div><div id="comments-container-61447" class="comments-container"></div><div id="comment-tools-61447" class="comment-tools"></div><div class="clear"></div><div id="comment-61447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61449"></span>

<div id="answer-container-61449" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61449-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there someting I do wrong?</p></blockquote><p>Yes.</p><p>What you're doing wrong is assuming that <code>tcp_dissect_pdus()</code>, which is what the Lua <code>dissect_tcp_pdus</code> function uses, works with packets cut short with a snapshot length. It doesn't.</p><p>Wireshark reassembly does <em>not</em> reassemble partially-captured fragments, so, no, <code>dissect_tcp_pdus</code> can't, and won't, reassemble all the segments even if the data is not captured.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '17, 17:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '17, 17:32</p></div></div><div id="comments-container-61449" class="comments-container"><span id="61454"></span><div id="comment-61454" class="comment"><div id="post-61454-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks. That's a bit sad, isn't it? :)</p></div><div id="comment-61454-info" class="comment-info"><span class="comment-age">(17 May '17, 00:33)</span> Cilyan</div></div><span id="61473"></span><div id="comment-61473" class="comment"><div id="post-61473-score" class="comment-score"></div><div class="comment-text"><p>Yes. There are limits on how much reassembly etc. can be done in that case. With TCP, you have packets for protocols running atop TCP beginning at arbitrary points in the packet, with either length fields or some other delimiting mechanism. If, for example, you slice off the last part of a TCP segment that contains the beginning of a packet, and that's continued in the next TCP segment, it'd be impossible for the dissector to recognize the stuff in the next TCP segment as being a continuation of that packet, and to know when the next packet after that begins, unless it can search heuristically for the beginning of a packet.</p><p>There's <em>some</em> more stuff Wireshark could do, but the general problem of handling packets on a TCP stream if packet slicing is done is insoluble.</p></div><div id="comment-61473-info" class="comment-info"><span class="comment-age">(17 May '17, 22:03)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-61449" class="comment-tools"></div><div class="clear"></div><div id="comment-61449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

