+++
type = "question"
title = "Cannot write filtered fields from .pcap file to text file"
description = '''I have a .pcap file which I got after using sniffer tool from mikrotik router. I used the command tshark -r macpack.pcap -T fields -E occurrence=f -e eth.addr &amp;gt; output.txt ,to filter mac addresses and store it in output.txt file. When I open output.txt in gedit it shows nothing. When I open macpa...'''
date = "2016-07-30T11:22:00Z"
lastmod = "2016-07-30T12:27:00Z"
weight = 54461
keywords = [ "mikrotik", "tshark", "wireshark" ]
aliases = [ "/questions/54461" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot write filtered fields from .pcap file to text file](/questions/54461/cannot-write-filtered-fields-from-pcap-file-to-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54461-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a .pcap file which I got after using sniffer tool from mikrotik router. I used the command tshark -r macpack.pcap -T fields -E occurrence=f -e eth.addr &gt; output.txt ,to filter mac addresses and store it in output.txt file. When I open output.txt in gedit it shows nothing. When I open macpack.pcap file in wireshark it shows the captured packets. What am I missing? . Also can anybody tell me field names for extracting ssid and signal strength as well</p></div><div id="question-tags" class="tags-container tags">mikrotik tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '16, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/557d426153aa6950b4ae3541a97ab03d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tatsugot&#39;s gravatar image" /><p>tatsugot<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tatsugot has no accepted answers">0%</span></p></div></div><div id="comments-container-54461" class="comments-container"></div><div id="comment-tools-54461" class="comment-tools"></div><div class="clear"></div><div id="comment-54461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54463"></span>

<div id="answer-container-54463" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54463-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Open the file in GUI Wireshark, go through the packet dissection pane, and click on the individual fields you want to have in your tshark output. Each time you click on a field, you'll see its description and its short name (in parentheses) in the left bottom corner of the Wireshark window. You can also right-click the field in the packet dissection pane and choose <code>Copy -&gt; Field Name</code> from the context menu to get the short name into clipboard.</p><p>As for <code>eth.addr</code>, such field does not exist in the wireless protocol hierarchy. You have to use <code>wlan.addr</code> instead (which represents any of <code>wlan.sa</code>, <code>wlan.ta</code>, <code>wlan.da</code>, <code>wlan.ra</code>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '16, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jul '16, 12:39</p></div></div><div id="comments-container-54463" class="comments-container"></div><div id="comment-tools-54463" class="comment-tools"></div><div class="clear"></div><div id="comment-54463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

