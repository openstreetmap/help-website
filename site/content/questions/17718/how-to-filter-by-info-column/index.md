+++
type = "question"
title = "How to filter by Info column?"
description = '''Is it possible to filter a Wireshark session by the Info column? If so, how? For example: I would like to filter packets with an expression that looks something like: Filter: info.contains== GET / foo.cgi?a=bar  Update  The answer by Syn_bit is good and fine. However, using that syntax I&#x27;m unable to...'''
date = "2013-01-16T06:48:00Z"
lastmod = "2017-04-12T20:48:00Z"
weight = 17718
keywords = [ "filter", "info" ]
aliases = [ "/questions/17718" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter by Info column?](/questions/17718/how-to-filter-by-info-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17718-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to filter a Wireshark session by the Info column? If so, how?</p><p>For example: I would like to filter packets with an expression that looks something like:</p><p>Filter: <code>info.contains== GET / foo.cgi?a=bar</code></p><p><strong>Update</strong></p><p>The answer by Syn_bit is good and fine. However, using that syntax I'm unable to filter the info column if the data in the info column is within [brackets].</p><p>For example: Here's a copy of a packet that contains "ZeroWindowProbeAck" in the info column.</p><pre><code>10.10.6.106 10.10.6.222 TCP 60 [TCP ZeroWindowProbeAck] [TCP ZeroWindow] http &gt; ldxp [ACK]</code></pre><p>I tried filtering by using this syntax:</p><p>Filter: <code>tcp contains "ZeroWindowProbeAck"</code></p><p>Unfortunately, however, this produced zero results.</p><p>My guess is that the text that is within brackets are not a part of the actual packet which would explain why I didn't get any search results. So, I took a gander at the actual packet to determine if there is anything in there that is synonymous with searching for ZeroWindowProbeAck, but I couldn't find anything.</p><p>Is it possible to search for text that is within brackets? If so, how?</p><p>FYI - Here is the full Wireshark packet of the summarized packet that I noted above. Do you see anything in there that would allow me to search for the ZeroWindowProbeAck info?</p><pre><code>No.     Time           Source                Destination           Protocol Length Info
  57569 4492.821600000 10.10.6.106           10.10.6.222           TCP      60     [TCP ZeroWindowProbeAck] [TCP ZeroWindow] http &gt; ldxp [ACK] Seq=1 Ack=1 Win=0 Len=0 MSS=1460

Frame 57569: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
    Interface id: 0
    WTAP_ENCAP: 1
    Arrival Time: Jan 17, 2013 07:27:49.434311000 Pacific Standard Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1358436469.434311000 seconds
    [Time delta from previous captured frame: 0.001530000 seconds]
    [Time delta from previous displayed frame: 0.001530000 seconds]
    [Time since reference or first frame: 4492.821600000 seconds]
    Frame Number: 57569
    Frame Length: 60 bytes (480 bits)
    Capture Length: 60 bytes (480 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ip:tcp]
    [Coloring Rule Name: Bad TCP]
    [Coloring Rule String: tcp.analysis.flags &amp;&amp; !tcp.analysis.window_update]
Ethernet II, Src: JkMicros_e4:6e:2e (00:90:c2:e4:6e:2e), Dst: Ibm_7a:a3:f7 (00:0d:60:7a:a3:f7)
    Destination: Ibm_7a:a3:f7 (00:0d:60:7a:a3:f7)
        Address: Ibm_7a:a3:f7 (00:0d:60:7a:a3:f7)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: JkMicros_e4:6e:2e (00:90:c2:e4:6e:2e)
        Address: JkMicros_e4:6e:2e (00:90:c2:e4:6e:2e)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IP (0x0800)
    Padding: c308
Internet Protocol Version 4, Src: 10.10.6.106 (10.10.6.106), Dst: 10.10.6.222 (10.10.6.222)
    Version: 4
    Header length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
    Total Length: 44
    Identification: 0x371c (14108)
    Flags: 0x00
        0... .... = Reserved bit: Not set
        .0.. .... = Don&#39;t fragment: Not set
        ..0. .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 64
    Protocol: TCP (6)
    Header checksum: 0x2255 [correct]
        [Good: True]
        [Bad: False]
    Source: 10.10.6.106 (10.10.6.106)
    Destination: 10.10.6.222 (10.10.6.222)
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]
Transmission Control Protocol, Src Port: http (80), Dst Port: ldxp (4042), Seq: 1, Ack: 1, Len: 0
    Source port: http (80)
    Destination port: ldxp (4042)
    [Stream index: 4549]
    Sequence number: 1    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header length: 24 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 0
    [Calculated window size: 0]
    [Window size scaling factor: -2 (no window scaling used)]
    Checksum: 0xcb16 [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    Options: (4 bytes), Maximum segment size
        Maximum segment size: 1460 bytes
            Kind: MSS size (2)
            Length: 4
            MSS Value: 1460
    [SEQ/ACK analysis]
        [TCP Analysis Flags]
            [This is a ZeroWindow segment]
                [Expert Info (Warn/Sequence): Zero window]
                    [Message: Zero window]
                    [Severity level: Warn]
                    [Group: Sequence]
            [This is an ACK to a TCP zero-window-probe]
                [Expert Info (Note/Sequence): Zero window probe ACK]
                    [Message: Zero window probe ACK]
                    [Severity level: Note]
                    [Group: Sequence]</code></pre></div><div id="question-tags" class="tags-container tags">filter info</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '13, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/1259897b9b42059302967b55c0dc2228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTM&#39;s gravatar image" /><p>KTM<br />
<span class="score" title="76 reputation points">76</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTM has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jan '13, 09:47</p></div></div><div id="comments-container-17718" class="comments-container"></div><div id="comment-tools-17718" class="comment-tools"></div><div class="clear"></div><div id="comment-17718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="17719"></span>

<div id="answer-container-17719" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17719-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The info column is not a general field, so it can't be filtered on. However, the information in the info column is a summary of the information in the fields of the highest layer protocol. So you can use the specific protocol fields to filter on.</p><p>For your example you could use:</p><ul><li>http contains "GET / foo.cgi?a=bar"</li><li>frame contains "GET / foo.cgi?a=bar" (if you don't care if the string is inside HTTP packets)</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '13, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17719" class="comments-container"><span id="17722"></span><div id="comment-17722" class="comment"><div id="post-17722-score" class="comment-score"></div><div class="comment-text"><p>Thanks, SYN-bit.</p><p>For future user's that find this post useful: Take note that the expression's argument is case sensitive.</p></div><div id="comment-17722-info" class="comment-info"><span class="comment-age">(16 Jan '13, 07:56)</span> KTM</div></div></div><div id="comment-tools-17719" class="comment-tools"></div><div class="clear"></div><div id="comment-17719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17753"></span>

<div id="answer-container-17753" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17753-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Items shown in brackets in the Info column are not necessarily actually present in the frame, which is why you can't find them using the "contains" operator. An item enclosed in brackets is information provided by Wireshark <em>about</em> the frame. There is no "TCP ZeroWindowProbeACK" string or value in the frame. Because Wireshark has seen previous frames, it is able to tell you that this frame is an acknowledgment to a zero window probe, but that information is not contained within the frame itself.</p><p>You can still filter on that attribute, but you need a different syntax. In this case, "tcp.analysis.zero_window_probe_ack" will show you all the frames that are acknowledgments to zero windows probes.</p><p>PS: In the future, when you want to follow up on someone's answer, it would be better to add a comment rather than to edit the original question. It's difficult to follow the conversation if the original question keeps changing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '13, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '13, 11:27</p></div></div><div id="comments-container-17753" class="comments-container"><span id="17755"></span><div id="comment-17755" class="comment"><div id="post-17755-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that answer, Jim. It works great. +1</p><p>Regarding your P.S. - I will remember that. I should have created a new question entirely.</p></div><div id="comment-17755-info" class="comment-info"><span class="comment-age">(17 Jan '13, 11:06)</span> KTM</div></div></div><div id="comment-tools-17753" class="comment-tools"></div><div class="clear"></div><div id="comment-17753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60795"></span>

<div id="answer-container-60795" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60795-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had to in the past filter by "Application Data" Info column</p><p>I did following:</p><ul><li>In the search field/panel, selected "Packet Details" then "String"</li><li>then typed "Application Data"</li><li>then the search result highlighted the exact field in the Packet Details where it appears</li><li>I Right clicked on the field in the Packet Details &gt; Select Add as a Column</li><li>then go to Edit &gt; Preferences &gt; Columns</li><li>And checked what exactly is the filter for it</li><li>In my case it turned out to be ssl.record.content_type</li><li>Then I noticed that the index for this field in Packet Details was set to "23"</li><li>so i filtered display by ssl.record.content_type == 23</li></ul><p>Hope that helps.</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 20:48</strong></p><img src="https://secure.gravatar.com/avatar/3c9ea34649c8d322e9cfd6dca1280643?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="evgenia&#39;s gravatar image" /><p>evgenia<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="evgenia has no accepted answers">0%</span></p></div></div><div id="comments-container-60795" class="comments-container"></div><div id="comment-tools-60795" class="comment-tools"></div><div class="clear"></div><div id="comment-60795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

