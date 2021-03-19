+++
type = "question"
title = "Viewing RSSI value in Wireshark"
description = '''In Wireshark Version 1.8.2, I tried Edit -&amp;gt; Preferences... -&amp;gt; Columns -&amp;gt; Press &quot;Add&quot; button -&amp;gt; As &quot;Field type&quot; I choose &quot;IEEE 802.11 RSSI&quot; and finally I choose name &quot;RSSI&quot; and click on &quot;Apply&quot; button. The column appeared but there are no values in the column. After reading (http://ask.wi...'''
date = "2013-02-11T06:11:00Z"
lastmod = "2013-02-12T04:21:00Z"
weight = 18484
keywords = [ "rssi" ]
aliases = [ "/questions/18484" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Viewing RSSI value in Wireshark](/questions/18484/viewing-rssi-value-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18484-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark Version 1.8.2, I tried Edit -&gt; Preferences... -&gt; Columns -&gt; Press "Add" button -&gt; As "Field type" I choose "IEEE 802.11 RSSI" and finally I choose name "RSSI" and click on "Apply" button. The column appeared but there are no values in the column.</p><p>After reading (<a href="http://ask.wireshark.org/questions/14963/how-to-get-the-field-did-unknown-4041-into-the-column),">http://ask.wireshark.org/questions/14963/how-to-get-the-field-did-unknown-4041-into-the-column),</a> I compiled Wireshark Version 1.8.5 from source but still no values are appearing.</p><p>The data was previously collected using pcap and I'm now opening it in Wireshark, how can I view the RSSI values ?<br />
</p></div><div id="question-tags" class="tags-container tags">rssi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '13, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/d32ee4c04465fdb7b316b82f61410f85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="heidi-ann&#39;s gravatar image" /><p>heidi-ann<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="heidi-ann has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-18484" class="comments-container"><span id="18486"></span><div id="comment-18486" class="comment"><div id="post-18486-score" class="comment-score"></div><div class="comment-text"><p>I've now tried compiling wireshark-1.9.0-SVN-47630.tar.bz2 from <a href="http://www.wireshark.org/download/automated/src/">http://www.wireshark.org/download/automated/src/</a> but that failed so now I'm trying wireshark-1.9.0-SVN-47626.tar.bz2</p></div><div id="comment-18486-info" class="comment-info"><span class="comment-age">(11 Feb '13, 07:33)</span> heidi-ann</div></div><span id="18538"></span><div id="comment-18538" class="comment"><div id="post-18538-score" class="comment-score"></div><div class="comment-text"><p>I've compiled wireshark-1.9.0-SVN-47626.tar.bz2 from source and there are still no RSSI values</p></div><div id="comment-18538-info" class="comment-info"><span class="comment-age">(12 Feb '13, 03:31)</span> heidi-ann</div></div><span id="18558"></span><div id="comment-18558" class="comment"><div id="post-18558-score" class="comment-score"></div><div class="comment-text"><p>Nobody here suggested compiling newer versions, because no matter <em>WHAT</em> version you compile, if you captured on an adapter the driver for which supplies radiotap, you will not get RSSI values, as those drivers do not something called "RSSI". They supply signal strength indicators in decibels; see my answer to your question. For PPI or AVS headers, they <em>might</em> provide RSSI values, or they might not.</p></div><div id="comment-18558-info" class="comment-info"><span class="comment-age">(12 Feb '13, 11:04)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18484" class="comment-tools"></div><div class="clear"></div><div id="comment-18484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18523"></span>

<div id="answer-container-18523" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18523-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're assuming the values are there to view.</p><p>Note, first of all, that IEEE Std 802.11-2012 uses "RSSI" in at least two different senses:</p><ul><li>Section 14.3.3.3 "RXVECTOR RSSI" clause says "The RSSI is an optional parameter that has a value of 0 to RSSI Max. This parameter is a measure by the PHY of the energy observed at the antenna used to receive the current PPDU. RSSI shall be measured between the beginning of the SFD and the end of the PLCP HEC. RSSI is intended to be used in a relative manner. Absolute accuracy of the RSSI reading is not specified."</li><li>Table 6-7—ESS "Link Parameter Set" talks about "DataFrameRSSI" and "BeaconRSSI" , and says they are "The received signal strength in dBm of received {Data,Beacon} frames from the network."</li></ul><p>There is no field in <a href="http://www.radiotap.org/defined-fields">the set of defined radiotap fields</a> that corresponds to the first of those two meanings; there are only fields that correspond to the signal strength as <a href="http://www.radiotap.org/defined-fields/dB%20antenna%20signal">dB from an arbitrary point</a> (useful only for comparing with other dB values on the same interface, as the arbitrary point may be different for different adapters but will be the same for all packets from the same adapter), and as <a href="http://www.radiotap.org/defined-fields/Antenna%20signal">dB relative to 1 milliwatt</a>. The latter is the second of those two meanings.</p><p><em>If</em> your pcap has radiotap headers, then, with current versions of Wireshark, those values will be shown in the RSSI column, followed by "dB" or "dBm". Most *BSD and Linux drivers use radiotap, so, if you're capturing on FreeBSD, NetBSD, DragonFly BSD, or Linux, those are the values you will get. OpenBSD is using their own incompatible version of radiotap, <a href="http://www.radiotap.org/suggested-fields/RSSI">which uses a defined value for another field for RSSI</a>. I don't know whether Wireshark supports that. OS X drivers also use radiotap as one form of radio data.</p><p>If your pcap has PPI headers, which are supported by AirPcap devices on Windows and with at least some drivers on some versions of OS X, those also only supply the RSSI as dBm.</p><p>If your pcap has AVS headers, they might provide either "raw" RSSI values in the sense of the first definition, "normalized" versions of those values scaled to a range of 0-1000, or dBm values. Those will also be displayed in the RSSI column.</p><p>If your pcap has Prism headers, they might also provide an RSSI value.</p><p>All of those header formats allow a driver <em>not</em> to supply signal strength values, so the adapter or its driver might not be supplying them, in which case you can't see them in the capture.</p><p>In addition, on Linux and OS X, you won't get <em>any</em> radio information unless the capture was done in monitor mode.</p><p>So, unless the packet details show a radiotap, AVS, PPI, or Prism header, <em>and</em> that header includes an signal strength value, your pcap doesn't <em>have</em> any signal strength information in it to show, and there's nothing that Wireshark can do to show it.</p><p>If your reference to <a href="http://ask.wireshark.org/questions/14963/how-to-get-the-field-did-unknown-4041-into-the-column">this question</a> means that you have Prism headers in your pcap (that's what the question is about), then note that no driver <em>I</em> saw for Linux that supplies Prism headers supplies any sort of signal strength indicator; in that case, you may have a network adapter that doesn't supply signal strength values to the host, or a driver for that adapter that doesn't supply those values in captured packets.</p><p>What hardware were you doing this capture on, and what software was it running (if it's a Linux distribution, say which one)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '13, 18:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Feb '13, 11:48</p></div></div><div id="comments-container-18523" class="comments-container"></div><div id="comment-tools-18523" class="comment-tools"></div><div class="clear"></div><div id="comment-18523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18541"></span>

<div id="answer-container-18541" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18541-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I tried Edit -&gt; Preferences... -&gt; Columns -&gt; Press "Add" button -&gt; As "Field type" I choose "IEEE 802.11 RSSI" and finally I choose name "RSSI" and click on "Apply" button. The column appeared but there are no values in the column.</p></blockquote><p>As @Guy Harris said, maybe there are no RSSI values in your capture file.</p><p>Please try the following capture file: <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=Http.cap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=Http.cap</a></p><p>Now you should see RSSI values in the column (I do see the values with Wireshark 1.8.4 on Windows XP). If you still don't see those values on your system, please report back.</p><p>BTW: Do you see a <strong>PPI</strong> header (next to the frame header) in your capture file?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '13, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '13, 04:22</p></div></div><div id="comments-container-18541" class="comments-container"><span id="18564"></span><div id="comment-18564" class="comment"><div id="post-18564-score" class="comment-score"></div><div class="comment-text"><p>Note that PPI headers are not guaranteed to contain an "RSSI" value, in the sense of a value described in the specification as "RSSI", or in the sense of "a value between 0 and RSSI_Max" - they contain dBm values, but not raw RSSI values, in captures on my MacBook Pro.</p></div><div id="comment-18564-info" class="comment-info"><span class="comment-age">(12 Feb '13, 12:11)</span> Guy Harris ♦♦</div></div><span id="18565"></span><div id="comment-18565" class="comment"><div id="post-18565-score" class="comment-score"></div><div class="comment-text"><p>Well, that's another problem ;-)</p></div><div id="comment-18565-info" class="comment-info"><span class="comment-age">(12 Feb '13, 12:14)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18541" class="comment-tools"></div><div class="clear"></div><div id="comment-18541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

