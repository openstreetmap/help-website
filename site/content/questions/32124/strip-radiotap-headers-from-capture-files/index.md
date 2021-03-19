+++
type = "question"
title = "Strip radiotap headers from capture files?"
description = '''I am capturing the first 200 bytes of each packet going through my wireless interface in monitoring mode. To access tcp headers, I can read the pcap file in wireshark or tcpdump, ignore the protection bit, and input my router pass-phrase as a key to decode it: http://ask.wireshark.org/questions/3011...'''
date = "2014-04-23T13:32:00Z"
lastmod = "2014-04-23T15:31:00Z"
weight = 32124
keywords = [ "wireless", "pcap", "monitoring", "radiotap", "tcpdump" ]
aliases = [ "/questions/32124" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Strip radiotap headers from capture files?](/questions/32124/strip-radiotap-headers-from-capture-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32124-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am capturing the first 200 bytes of each packet going through my wireless interface in monitoring mode. To access tcp headers, I can read the pcap file in wireshark or tcpdump, ignore the protection bit, and input my router pass-phrase as a key to decode it: <a href="http://ask.wireshark.org/questions/30115/display-decrypted-wlan-traffic-that-has-the-protected-bit-set">http://ask.wireshark.org/questions/30115/display-decrypted-wlan-traffic-that-has-the-protected-bit-set</a></p><p>I would like to use the packet capture with tools such as tcptrace, which expect IP headers instead of radiotap headers in the first byte. Is there a way to strip the radiotap headers from a pcap and create a tcpdump like capture which starts with IP headers? Can it be done using editcap or tshark?</p><p>This is exactly the same as a previous question asked: <a href="https://www.wireshark.org/lists/wireshark-users/201002/msg00127.html">https://www.wireshark.org/lists/wireshark-users/201002/msg00127.html</a> which did not have a follow-up</p></div><div id="question-tags" class="tags-container tags">wireless pcap monitoring radiotap tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/e215c4ae46510022a144b4996b15e528?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shahifaqeer&#39;s gravatar image" /><p>shahifaqeer<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shahifaqeer has no accepted answers">0%</span></p></div></div><div id="comments-container-32124" class="comments-container"></div><div id="comment-tools-32124" class="comment-tools"></div><div class="clear"></div><div id="comment-32124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32132"></span>

<div id="answer-container-32132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32132-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I can read the pcap file in wireshark or tcpdump, ignore the protection bit, and input my router pass-phrase as a key to decode it:</p></blockquote><p>O.K., so you are <strong>decrypting</strong> the wifi traffic in the pcap.</p><p>Now, just stripping the radiotap header from the encrypted frames does not make much sense. So, you need a method to save the <strong>decrypted</strong> wifi frames into a new pcap file and then strip the wifi headers. However, there is currently no good method in Wireshark to do that.</p><p>So, you need a different tool, like one of the following</p><ul><li><strong>airdecap-ng</strong> <a href="http://www.aircrack-ng.org/doku.php?id=airdecap-ng">http://www.aircrack-ng.org/doku.php?id=airdecap-ng</a></li><li><strong>dot11decrypt</strong> <a href="https://github.com/mfontanini/dot11decrypt">https://github.com/mfontanini/dot11decrypt</a></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32132" class="comments-container"><span id="32149"></span><div id="comment-32149" class="comment"><div id="post-32149-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I played with scapy yesterday - and it seems like a very easy and good tool to accomplish what I need. It is possible to strip the radiotap headers and save new packets after, the only problem is decoding frames in scapy. Any ideas on how to ignore the Dot11WEP there?</p><p>Will try dot11decrypt and report if it solved the problem.</p></div><div id="comment-32149-info" class="comment-info"><span class="comment-age">(24 Apr '14, 07:45)</span> shahifaqeer</div></div></div><div id="comment-tools-32132" class="comment-tools"></div><div class="clear"></div><div id="comment-32132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

