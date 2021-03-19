+++
type = "question"
title = "UDP reassembly with multiple PDUs per packet"
description = '''I am writing a dissector for a UDP protocol with the following (rather unfortunate) features:  A single PDU may (and in most cases does) span multiple packets. A single header may also span multiple packets A packet may also contain multiple PDUs, both complete and fragmented The length of a PDU is ...'''
date = "2011-08-11T12:27:00Z"
lastmod = "2011-08-16T03:03:00Z"
weight = 5656
keywords = [ "reassembly", "udp", "dissector", "pdu", "fragmentation" ]
aliases = [ "/questions/5656" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [UDP reassembly with multiple PDUs per packet](/questions/5656/udp-reassembly-with-multiple-pdus-per-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5656-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a dissector for a UDP protocol with the following (rather unfortunate) features:</p><ul><li>A single PDU may (and in most cases does) span multiple packets.</li><li>A single header may also span multiple packets</li><li>A packet may also contain multiple PDUs, both complete and fragmented</li><li>The length of a PDU is determined by a header field, but an unknown number of bytes must be read before getting to that value, as the header is preceded by a variable length delimiter</li><li>There are no sequence numbers or other ways of uniquely identifying a PDU</li><li>There is no flag indicating whether a PDU will be fragmented, or whether multiple PDUs will appear in a packet, other than by reading the length</li><li>All communications are between a single sender and receiver</li></ul><p>In practice, this means that some assembly must be done before it is even possible to determine how much assembly will be needed to complete a PDU.</p><p>I have approached this by using the various tools in reassemble.h. However, I am getting stuck in a few places, and am looking for suggestions.</p><p>My dissector essentially looks like this (pseudocode):</p><pre><code>dissect_proto(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree) {
    while [bytes remain in tvb from offset]
        if [pdu length is unknown]
            found = fragment_get(pinfo, 0, fragment_table);
            if [fragment was found]
                [loop through found-&gt;next and add total_length and data]
                buffer = tvb_new_real_data(data, total_length, total_length);
            else
                buffer = tvb_new_subset(tvb, offset, ...);

            bytes_available = tvb_length(buffer);
            pdu_length = get_pdu_length(buffer, &amp;pdu_offset);
            if [pdu length is known and is smaller than bytes remaining]
                complete = TRUE;
            /* bytes_to_consume is min(pdu_length, bytes_available) */
            pinfo-&gt;fragmented = !complete;
            head = fragment_add(tvb, offset, pinfo, 0, fragment_table,
                    offset, bytes_to_consume, !complete);
            next_tvb = process_reassembled_data(tvb, offset, pinfo, &quot;Reassembled packet&quot;, head, &amp;proto_frag_items, NULL, tree);
            offset += bytes_to_consume;</code></pre><p>Mostly, I am hung up on how to add fragments properly. I would like to be able to read part of a packet, add any portion of that from a fragmented PDU into the table, and continue looping through. As I read more PDUs out of that packet, I add fragments, marked complete, for those into the table. The last PDU would likely be incomplete, and added as well.</p><p>It appears that the fragment table is expecting a single add operation per packet. Is there a correct way to keep track of fragments when there may be multiple per packet?</p></div><div id="question-tags" class="tags-container tags">reassembly udp dissector pdu fragmentation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '11, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/d84e8965aabf69774c0bf979cf8e55e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sweetpea&#39;s gravatar image" /><p>sweetpea<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sweetpea has no accepted answers">0%</span></p></div></div><div id="comments-container-5656" class="comments-container"></div><div id="comment-tools-5656" class="comment-tools"></div><div class="clear"></div><div id="comment-5656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5671"></span>

<div id="answer-container-5671" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5671-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the looks of it your protocol is screwed up. UDP is an unreliable datagram protocol, hence does not guarantee delivery, nor sequence. Once an inconsistency occurs your dissector (and any receiver for that matter) will get out of sync.</p><p>Maybe the RTP dissector can be of help, it also runs over UDP, and contains reassembly code. Although I think it has the benefit of sequence numbers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '11, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5671" class="comments-container"><span id="5707"></span><div id="comment-5707" class="comment"><div id="post-5707-score" class="comment-score"></div><div class="comment-text"><p>The protocol is screwed up. Sadly, that doesn't eliminate the need to dissect and troubleshoot it. The main consolation is that PDUs are generally fairly small, so any dropped or out-of-sequence packets will only affect a small part of the stream.</p><p>The RTP dissector seems to depend on conversations and sequence numbers, but it does offer some hints. Setting the partial reassembly flag is one step I was missing. I'm still stumped on multiple PDUs, though.</p></div><div id="comment-5707-info" class="comment-info"><span class="comment-age">(15 Aug '11, 15:29)</span> sweetpea</div></div><span id="5709"></span><div id="comment-5709" class="comment"><div id="post-5709-score" class="comment-score"></div><div class="comment-text"><p>On the first pass through the capture, you'll see the packets in the sequence they're in inside the capture file, which is the closest approximation you'll get to the time order. Reassemble them assuming they're in the right order; if they're not, what you reassemble will be what any receiver who got them in the same order would see - if that's bogus, then what the receiver reassembles will be bogus to, so Wireshark will show you that bogosity. (I.e., given the brokenness of the protocol, the brokenness of reassembly will show you the results of the brokenness of the protocol.)</p></div><div id="comment-5709-info" class="comment-info"><span class="comment-age">(16 Aug '11, 02:56)</span> Guy Harris ♦♦</div></div><span id="5727"></span><div id="comment-5727" class="comment"><div id="post-5727-score" class="comment-score"></div><div class="comment-text"><p>Yes. I know I can't do better than the sequence coming into wireshark. Originally, I implemented all of the reassembly myself, which worked on the first pass, but not on random access when looking at actual frames in wireshark. I can understand how to parse and display PDUs based on that first pass; what's tricky is finding the correct way to store the information so that it works in random access.</p></div><div id="comment-5727-info" class="comment-info"><span class="comment-age">(17 Aug '11, 15:42)</span> sweetpea</div></div></div><div id="comment-tools-5671" class="comment-tools"></div><div class="clear"></div><div id="comment-5671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5710"></span>

<div id="answer-container-5710" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5710-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, so let's look at the protocol's (mis-)features:</p><ul><li>A single PDU may (and in most cases does) span multiple packets.</li></ul><p>That means you need to have some way of knowing when the PDU ends, i.e. when you're done with reassembly.</p><ul><li>A single header may also span multiple packets</li></ul><p>That means you need to have some way of knowing when the header ends.</p><ul><li>A packet may also contain multiple PDUs, both complete and fragmented</li></ul><p>Again, you need to know when the PDU ends, even if the entire PDU is within one UDP datagram.</p><ul><li>The length of a PDU is determined by a header field, but an unknown number of bytes must be read before getting to that value, as the header is preceded by a variable length delimiter</li></ul><p>OK, that presumably means the length tells you when the PDU ends. If the delimiter is variable-length, there has to be some way of knowing when the <em>delimiter</em> ends; what is that?</p><ul><li>There are no sequence numbers or other ways of uniquely identifying a PDU</li></ul><p>Which, as Jaap noted, means that the receiver has to assume that the packets are delivered in order, and, if they're not, it won't work correctly, so, if Wireshark doesn't reassemble the packets "correctly" in that case, it's actually correct in the sense that it'll show you what a receiver that got the UDP packets in the same order will <em>think</em> it got, even if that's not what the sender <em>intended</em> it to see.</p><ul><li>There is no flag indicating whether a PDU will be fragmented, or whether multiple PDUs will appear in a packet, other than by reading the length</li></ul><p>That's similar to many protocols running atop TCP, so that's not <em>inherently</em> insoluble. You might have to implement something similar to <code>tcp_dissect_pdus()</code> in your dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '11, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Aug '11, 16:10</p></div></div><div id="comments-container-5710" class="comments-container"><span id="5711"></span><div id="comment-5711" class="comment"><div id="post-5711-score" class="comment-score"></div><div class="comment-text"><p>Whether or not the dissector will show PDU reassembly problems experienced by the receiver also depends on where the capture is made. At the sender side all may seem nice and dandy, while at the receiver things may not be...</p></div><div id="comment-5711-info" class="comment-info"><span class="comment-age">(16 Aug '11, 05:02)</span> Jaap ♦</div></div><span id="5728"></span><div id="comment-5728" class="comment"><div id="post-5728-score" class="comment-score"></div><div class="comment-text"><p>For the moment, I'm ignoring packet loss and sequence problems.</p></div><div id="comment-5728-info" class="comment-info"><span class="comment-age">(17 Aug '11, 15:54)</span> sweetpea</div></div><span id="5729"></span><div id="comment-5729" class="comment"><div id="post-5729-score" class="comment-score"></div><div class="comment-text"><p>The delimiter looks like MSG:xxxxx[newline], where xxxxx is 1-5 characters. Following is a 2-byte PDU type, and 2 byte PDU length, then the data, then a 2-byte checksum.</p><p>Packets often come in a pattern like this:</p><pre><code>Packet 1: MSG:xxxxx[newline]
Packet 2: [type][len]
Packet 3: [data][checksum]MSG:xxxxx[newline][type][len][data][checksum]MSG:xxxxx[newline]
Packet 4: [type][len]
Packet 5: [data][checksum]
Packet 6: MSG:xxxxx[newline]</code></pre><p>...</p></div><div id="comment-5729-info" class="comment-info"><span class="comment-age">(17 Aug '11, 15:57)</span> sweetpea</div></div></div><div id="comment-tools-5710" class="comment-tools"></div><div class="clear"></div><div id="comment-5710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

