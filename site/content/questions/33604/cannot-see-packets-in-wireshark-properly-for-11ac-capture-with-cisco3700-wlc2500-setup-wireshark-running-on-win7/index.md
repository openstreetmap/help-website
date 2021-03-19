+++
type = "question"
title = "Cannot see packets in Wireshark properly for 11ac capture with Cisco3700 + WLC2500 setup (Wireshark running on Win7)"
description = '''Followed steps mentioned at https://supportforums.cisco.com/document/75236/collecting-wireless-sniffer-trace-using-cisco-lightweight-ap-sniffer-mode Setup used is Cisco WLC 2500 + Cisco LAP 3700 in Sniffer mode. Win7 (64-bit) machine running Wireshark (v1.11.3) is connected over Ethernet with captur...'''
date = "2014-06-09T23:14:00Z"
lastmod = "2014-06-12T15:47:00Z"
weight = 33604
keywords = [ "peekremote" ]
aliases = [ "/questions/33604" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot see packets in Wireshark properly for 11ac capture with Cisco3700 + WLC2500 setup (Wireshark running on Win7)](/questions/33604/cannot-see-packets-in-wireshark-properly-for-11ac-capture-with-cisco3700-wlc2500-setup-wireshark-running-on-win7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33604-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Followed steps mentioned at <a href="https://supportforums.cisco.com/document/75236/collecting-wireless-sniffer-trace-using-cisco-lightweight-ap-sniffer-mode">https://supportforums.cisco.com/document/75236/collecting-wireless-sniffer-trace-using-cisco-lightweight-ap-sniffer-mode</a></p><p>Setup used is Cisco WLC 2500 + Cisco LAP 3700 in Sniffer mode.</p><p>Win7 (64-bit) machine running Wireshark (v1.11.3) is connected over Ethernet with capture filter "udp port 5555".</p><p>The packets after decode with peekremote do not show up correctly. The beacons and other some control packets (RTS/CTS) come up fine, but Data packets are not coming up correctly. Any idea what might be the problem ?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/snapshot.jpg" alt="alt text" /></p><p>I have also tried with v1.6.8 as mentioned in the Cisco link, but see the same problem. ALl the 802.11 QoS data packets show up as below:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/123.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">peekremote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '14, 23:14</strong></p><img src="https://secure.gravatar.com/avatar/43e2d9c38f7fe55143e0606580e503bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sudheer&#39;s gravatar image" /><p>Sudheer<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sudheer has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jun '14, 11:37</p></div></div><div id="comments-container-33604" class="comments-container"></div><div id="comment-tools-33604" class="comment-tools"></div><div class="clear"></div><div id="comment-33604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33754"></span>

<div id="answer-container-33754" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33754-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As the response to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10177">bug 10177</a> says, you used a capture filter of "udp port 5555", which means that only the first fragment of a fragmented IP packet will be captured. This prevents Wireshark from reassembling a UDP packet that requires more than one fragment (in this case, a sufficiently large 802.11 packet sent by the AP would have to be fragmented).</p><p>What would be best would be if libpcap/WinPcap supported the PEEKREMOTE protocol as a remote capture protocol, in which case libpcap would listen on a UDP socket to which the AP sent packets, letting the IP layer on the OS of the machine running Wireshark do the reassembly, and not requiring a capture filter (instead, the capture filter would apply to the 802.11 packets encapsulated inside the PEEKREMOTE protocol).</p><p>However, remote capture support for libpcap/WinPcap is still a work in progress, so, instead, try a filter that matches either the first fragment of a UDP packet to port 5555 <em>OR</em> fragments other than the first fragment:</p><pre><code>udp port 5555 or (ip[6:2] &amp; 0x1fff)  !=  0</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-33754" class="comments-container"></div><div id="comment-tools-33754" class="comment-tools"></div><div class="clear"></div><div id="comment-33754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33714"></span>

<div id="answer-container-33714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33714-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Any idea what might be the problem ?</p></blockquote><p>From the link you posted:</p><p>Cite: "(Note: <strong>you must use wireshark 1.6.8 or earlier</strong>, newer versions have this support broken and the packets will not be decoded correctly) follow the steps below:"</p><p>So, it looks like the Cisco protocol is not being decoded correctly with Wireshark &gt; 1.6.8. If that is true (please test it with 1.6.8), could you please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and attach a sample capture file.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jun '14, 07:06</p></div></div><div id="comments-container-33714" class="comments-container"><span id="33716"></span><div id="comment-33716" class="comment"><div id="post-33716-score" class="comment-score"></div><div class="comment-text"><p>This may have recently been fixed. Try the latest buildbot build.</p></div><div id="comment-33716-info" class="comment-info"><span class="comment-age">(12 Jun '14, 08:02)</span> Anders ♦</div></div><span id="33732"></span><div id="comment-33732" class="comment"><div id="post-33732-score" class="comment-score"></div><div class="comment-text"><p>I have also tried with v1.6.8 as mentioned in the Cisco link, but see the same problem.</p><p>Placed a snapshot in the question section.</p></div><div id="comment-33732-info" class="comment-info"><span class="comment-age">(12 Jun '14, 11:35)</span> Sudheer</div></div><span id="33734"></span><div id="comment-33734" class="comment"><div id="post-33734-score" class="comment-score"></div><div class="comment-text"><p>can you post a sample capture file somewhere (google drive, dropbox, cloudshark.org)?</p></div><div id="comment-33734-info" class="comment-info"><span class="comment-age">(12 Jun '14, 11:39)</span> Kurt Knochner ♦</div></div><span id="33751"></span><div id="comment-33751" class="comment"><div id="post-33751-score" class="comment-score"></div><div class="comment-text"><p>I have filed a bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10177">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10177</a></p><p>Above link has sample pcap files.</p></div><div id="comment-33751-info" class="comment-info"><span class="comment-age">(12 Jun '14, 14:28)</span> Sudheer</div></div></div><div id="comment-tools-33714" class="comment-tools"></div><div class="clear"></div><div id="comment-33714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

