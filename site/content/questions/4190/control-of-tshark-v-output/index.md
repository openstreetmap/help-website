+++
type = "question"
title = "control of tshark -V output"
description = '''Is there a way to print the packet details of only a specific layer/protocol while ignoring or summarizing the rest? For example, I want to compress this: Frame 1: 48 bytes on wire (384 bits), 48 bytes captured (384 bits)  Arrival Time: May 22, 2011 02:07:16.384560000 PDT  Epoch Time: 1306217236.384...'''
date = "2011-05-23T23:18:00Z"
lastmod = "2011-05-24T01:48:00Z"
weight = 4190
keywords = [ "tshark" ]
aliases = [ "/questions/4190" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [control of tshark -V output](/questions/4190/control-of-tshark-v-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4190-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to print the packet details of only a specific layer/protocol while ignoring or summarizing the rest? For example, I want to compress this:</p><pre><code>Frame 1: 48 bytes on wire (384 bits), 48 bytes captured (384 bits)
    Arrival Time: May 22, 2011 02:07:16.384560000 PDT
    Epoch Time: 1306217236.384560000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 0.000000000 seconds]
    Frame Number: 1
    Frame Length: 48 bytes (384 bits)
    Capture Length: 48 bytes (384 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ip:udp:foo]
Ethernet II, Src: Abcd_FF:FF:FF (FF:FF:FF:FF:FF:FF), Dst: Cisco-Li_FF:FF:FF (FF:FF:FF:FF:FF:FF)
    Destination: 
        Address: 
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
    Source: 
        Address: 
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
    Type: IP (0x0800)
Internet Protocol, Src: 192.168.1.2 (192.168.1.2), Dst: 1.2.3.4 (1.2.3.4)
    Version: 4
    Header length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00)
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..0. = ECN-Capable Transport (ECT): 0
        .... ...0 = ECN-CE: 0
    Total Length: 34
    Identification: 0x6af2 (27378)
    Flags: 0x00
        0... .... = Reserved bit: Not set
        .0.. .... = Don&#39;t fragment: Not set
        ..0. .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 64
    Protocol: UDP (17)
    Header checksum: 0x0000 [validation disabled]
        [Good: False]
        [Bad: False]
    Source: 192.168.1.2 (192.168.1.2)
    Destination: 1.2.3.4 (1.2.3.4)
User Datagram Protocol, Src Port: 49589 (49589), Dst Port: cbt (7777)
    Source port: 49589 (49589)
    Destination port: cbt (7777)
    Length: 14
    Checksum: 0xc64f [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
Foo Protocol
        Field A: 68656c
        Field B: 0xf4240</code></pre><p>into this:</p><pre><code> Frame 1: 48 bytes on wire (384 bits), 48 bytes captured (384 bits)
 Internet Protocol, Src: 192.168.1.2 (192.168.1.2), Dst: 1.2.3.4 (1.2.3.4)
 User Datagram Protocol, Src Port: 49589 (49589), Dst Port: cbt (7777)
 Foo Protocol
        Field A: 68656c
        Field B: 0xf4240</code></pre></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '11, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-4190" class="comments-container"></div><div id="comment-tools-4190" class="comment-tools"></div><div class="clear"></div><div id="comment-4190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4191"></span>

<div id="answer-container-4191" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4191-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that is possible, but was only added to the repository very recently. I'm not sure whether it has made it into 1.6.0rc1 but you could try. If it's not in there, you'd have to use an <a href="http://www.wireshark.org/download/automated/">automated build</a> version, compile your own or wait for 1.7.0 to come out.</p><p>From the 'tshark -h' output:</p><pre><code>-O &lt;protocols&gt;           Only show packet details of these protocols, comma
                         separated</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '11, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4191" class="comments-container"></div><div id="comment-tools-4191" class="comment-tools"></div><div class="clear"></div><div id="comment-4191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

