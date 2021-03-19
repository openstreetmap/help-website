+++
type = "question"
title = "SSL state/ decoder states and conditions for failure of ssl decryption"
description = '''With this link is attached a sample pcap file along with the ssl keylog file and debug file.  I am unable to understand why Wireshark would not decrypt the data for some ssl application data packets. This data was captured with a website request from chromium and some cipher suites blacklisted (0xcc...'''
date = "2016-12-29T14:01:00Z"
lastmod = "2016-12-31T05:16:00Z"
weight = 58424
keywords = [ "sslkeylogfile", "ssl", "reassembly", "follow_ssl_stream", "ssl_decrypt" ]
aliases = [ "/questions/58424" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SSL state/ decoder states and conditions for failure of ssl decryption](/questions/58424/ssl-state-decoder-states-and-conditions-for-failure-of-ssl-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58424-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With <a href="https://drive.google.com/open?id=0B6unL1yNveR6UDV5TjltTUdad1U">this link is attached</a> a sample pcap file along with the ssl keylog file and debug file.</p><p>I am unable to understand why Wireshark would not decrypt the data for some ssl application data packets. This data was captured with a website request from chromium and some cipher suites blacklisted (0xcca8, 0xcca9). After perusing through the debug file, I found three common ssl states - 0x2BF, 0x3BF, 0x7BF</p><p>On seeing, packet number 594 and 1002, I do not understand why one packet was decrypted while the other was not. The keylog file captured the client random and master secret as it was able decrypt some of the packets (decoder exists for those packets).</p><p>Can somebody please help me understand the different ssl states that a dissector can obtain and what do they mean. Specifically, what are the cases in which a decoder variable would fail to be created (assume, no memory leaks and memory abundance on the computer).</p><p>As I understand, for decryption of ssl packets - You need</p><ol><li>Capture of the complete handshake.</li><li>The session key either from the keylog file or the private key from the server/client.</li></ol><p>A further concept/follow through for this question is to try to find a solution to this problem.</p><p>If there are two computers set up such as this -</p><p>Comp A ----------Bridged --------&gt; Comp B -----------&gt; Internet</p><p>Computer B has some firewall rules that initially blocks ssl application data packets but after execution of a script, allows all packets to pass through.</p><p>Wireshark is running on Comp A and Comp B and capture packets respectively as pcap A and pcap B. pcap B contains all packets (any dropped packets from the firewall rule also).</p><p>Then given a keylog file captured on comp A, is it possible to match and verify the decrypted content of all packets captured on both computers. ?</p><p>I tried to export the decrypted http objects and do a hash of the contents, but the match would always fail (as some packets would decrypt and some would not).</p><p>In particular, I also made the following observations -</p><ol><li><p>TCP reassembly happened differently on both computers (Does this lead to a difference in arrival of ssl states for the ssl session).</p></li><li><p>A certain subset of data application packets for a pair of ip addresses contain different lengths. (when matched on both the computers. I do not know why this happens as the computer is only forwarding packets).</p></li><li><p>Because data application packets on both computers have different lengths, they decrypt with different data and a simple hash for decrypted content fails.</p></li></ol><p>What would be the best way to match and verify the decrypted contents on both the computers ?</p></div><div id="question-tags" class="tags-container tags">sslkeylogfile ssl reassembly follow_ssl_stream ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '16, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/c28011fe6d6c690149158e45cf811175?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mac9393&#39;s gravatar image" /><p>mac9393<br />
<span class="score" title="36 reputation points">36</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mac9393 has no accepted answers">0%</span></p></div></div><div id="comments-container-58424" class="comments-container"><span id="58428"></span><div id="comment-58428" class="comment"><div id="post-58428-score" class="comment-score"></div><div class="comment-text"><p>I think you can try using the "ignore mac failed" param in the ssl options, If you are sure that the computer B just forwards the packets.</p><p>"Then given a keylog file captured on comp A, is it possible to match and verify the decrypted content of all packets captured on both computers. ?"</p><p>If you are sure that the computer B just forwards the packets then, the symmetric key should probably be same and you should be able to decrypt the packets in both the pcaps.</p><p>From your description it feels like the computer B probably does more than just forwarding are you sure it is not a proxy?</p></div><div id="comment-58428-info" class="comment-info"><span class="comment-age">(29 Dec '16, 22:30)</span> koundi</div></div><span id="58463"></span><div id="comment-58463" class="comment"><div id="post-58463-score" class="comment-score"></div><div class="comment-text"><p>Please see the capture files on both the computers. <a href="https://drive.google.com/open?id=0Bz5corUPBatBWWpXTFYwWjdfS0k">https://drive.google.com/open?id=0Bz5corUPBatBWWpXTFYwWjdfS0k</a></p></div><div id="comment-58463-info" class="comment-info"><span class="comment-age">(02 Jan '17, 09:45)</span> mac9393</div></div><span id="58464"></span><div id="comment-58464" class="comment"><div id="post-58464-score" class="comment-score"></div><div class="comment-text"><p>Both the capture files in theory should contain the same data but are reassembled differently, with different packet lengths etc.</p><p>The gateway computer (bridged interface) just forwards the packets.</p></div><div id="comment-58464-info" class="comment-info"><span class="comment-age">(02 Jan '17, 09:48)</span> mac9393</div></div><span id="58465"></span><div id="comment-58465" class="comment"><div id="post-58465-score" class="comment-score"></div><div class="comment-text"><p>I am not sure how do I verify contents of both the capture files correctly.</p></div><div id="comment-58465-info" class="comment-info"><span class="comment-age">(02 Jan '17, 10:02)</span> mac9393</div></div></div><div id="comment-tools-58424" class="comment-tools"></div><div class="clear"></div><div id="comment-58424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58439"></span>

<div id="answer-container-58439" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58439-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Frame 594 is part of <code>tcp.stream==1</code> for which the full handshake is available. Frame 1002 is part of <code>tcp.stream==0</code> for which the handshake is missing and therefore Wireshark has no idea what ciphers are in use (using <code>tcp.port==38476</code> also did not show other packets for this connection).</p><p>In the current dissector (for TLS &lt;= 1.2), the common states (after <strong>completing the handshake</strong>) are:</p><ul><li>A RSA key exchange is in use and a private key file was provided. The encrypted premaster secret can be decrypted and transformed into a master secret.</li><li>A master secret is available via a lookup in the keylog file and based on any of the Client Hello random value or Session ID.</li><li>No secrets are available so no decryption is possible.</li></ul><p>In your case the handshake is missing, so no decryption is possible since the parameters are unknown.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '16, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-58439" class="comments-container"></div><div id="comment-tools-58439" class="comment-tools"></div><div class="clear"></div><div id="comment-58439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

