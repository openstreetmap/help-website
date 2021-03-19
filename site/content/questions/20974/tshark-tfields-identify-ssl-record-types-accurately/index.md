+++
type = "question"
title = "tshark -Tfields, identify SSL record types accurately"
description = '''I&#x27;m using tshark -Tfields to print a packet trace in a machine-readable format, and one of the things I need to extract is the SSL record type for each record in the packet, if the packet contains SSL records. If I print the ssl.record.content_type and ssl.handshake.type fields, they do not seem to ...'''
date = "2013-05-05T20:14:00Z"
lastmod = "2013-05-06T01:04:00Z"
weight = 20974
keywords = [ "ssl", "tshark" ]
aliases = [ "/questions/20974" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -Tfields, identify SSL record types accurately](/questions/20974/tshark-tfields-identify-ssl-record-types-accurately)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20974-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using <code>tshark -Tfields</code> to print a packet trace in a machine-readable format, and one of the things I need to extract is the SSL record type for each record in the packet, if the packet contains SSL records. If I print the <code>ssl.record.content_type</code> and <code>ssl.handshake.type</code> fields, they do not seem to be consistent with each other: specifically, for this packet trace</p><pre><code>$ tshark -r https_snakeoil.cap -T text | grep SSL | head -5
  4   0.000158    127.0.0.1 -&gt; 127.0.0.1    SSLv2 171 Client Hello
  6   0.002160    127.0.0.1 -&gt; 127.0.0.1    SSLv3 995 Server Hello, Certificate,
                                                      Server Hello Done
  8   2.808933    127.0.0.1 -&gt; 127.0.0.1    SSLv3 278 Client Key Exchange,
                                                      Change Cipher Spec,
                                                      Encrypted Handshake Message
  9   2.822770    127.0.0.1 -&gt; 127.0.0.1    SSLv3 141 Change Cipher Spec,
                                                      Encrypted Handshake Message
 11   2.833071    127.0.0.1 -&gt; 127.0.0.1    SSLv3 503 Application Data</code></pre><p>I get these record and handshake types:</p><pre><code>$ tshark -r https_snakeoil.cap -T fields -E separator=: -E accumulator=. \
         -e frame.number -e ssl.record.content_type -e ssl.handshake.type |
    grep -v &#39;::$&#39; | head -5
4::1
6:22.22.22:2.11.14
8:22.20.22:16
9:20.22:
11:23:</code></pre><p>Problem 1: packet 4 has handshake type 1 but no record type. WTF?<br />
Problem 2: packets 8 and 9 report no handshake type for one of the handshake records. Presumably this is because that handshake record is encrypted. This is a problem because in principle I don't know which one it is (i.e. that 16 in column 3 of packet 8 could go with either of the 22s in column 2). I can <em>assume</em> that the missing values are for 22s following a 20 (that is, ChangeCipherSpec, which turns encryption on) but I suspect this is likely to be unreliable in practice. There doesn't seem to be any way to force aggregated field values to have consistent vector lengths (e.g. <code>8:22.20.22:16..</code> would be unambigously parseable). Is there any alternative?</p></div><div id="question-tags" class="tags-container tags">ssl tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '13, 20:14</strong></p><img src="https://secure.gravatar.com/avatar/dd7cc06b1b1c347e172c6ba532937173?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zack&#39;s gravatar image" /><p>Zack<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zack has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '13, 20:15</p></div></div><div id="comments-container-20974" class="comments-container"></div><div id="comment-tools-20974" class="comment-tools"></div><div class="clear"></div><div id="comment-20974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20976"></span>

<div id="answer-container-20976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20976-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Problem 1 is caused by the fact that the client initiated the SSL session with a SSL version 2 client hello. In SSLv2, the SSL records did not have a record type. Do you still see SSLv2 client hello's in your production network?</p><p>Problem 2 is indeed caused by the fact that the second SSL handshake message in the packet is encrypted. There is currently no way to correlate multiple occurrences of multiple fields with the "-T fields" output. This cannot be solved in generic way because of the way the "-E fields" option interacts with the dissection data. For SSL handshake messages, this could be solved to add a ssl.handshake.type field for encrypted handshake messages too with a specific code.</p><p>You could also use <a href="http://wiki.wireshark.org/Lua">LUA</a> or <a href="http://wiki.wireshark.org/Mate">MATE</a> to link the values together. Or use "-T pdml" to create XML output in which the whole tree is hierarchically printed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '13, 01:04</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20976" class="comments-container"><span id="20986"></span><div id="comment-20986" class="comment"><div id="post-20986-score" class="comment-score"></div><div class="comment-text"><p>Re SSLv2 client hello, this is probably not an issue for real captures; I just didn't realize that the example HTTPS capture on the wireshark wiki was that old. I'll look into Lua; I already was going to need a postprocessing script, so that might solve two problems at once.</p></div><div id="comment-20986-info" class="comment-info"><span class="comment-age">(06 May '13, 08:47)</span> Zack</div></div><span id="20996"></span><div id="comment-20996" class="comment"><div id="post-20996-score" class="comment-score"></div><div class="comment-text"><p>On further investigation, Lua appears to have the same correlation problem: a <code>Listener.new("ip")</code> tap that uses extractors to query <code>ssl.record.content_type</code> and <code>ssl.handshake.type</code> will get arrays of length 3 and 1, respectively, for the troublesome packet 8, with no indication of the correlation. A <code>Listener.new("ssl")</code> tap is only called once, for the first SSL record in the packet. So now I'm stumped again.</p></div><div id="comment-20996-info" class="comment-info"><span class="comment-age">(06 May '13, 16:14)</span> Zack</div></div></div><div id="comment-tools-20976" class="comment-tools"></div><div class="clear"></div><div id="comment-20976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

