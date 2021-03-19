+++
type = "question"
title = "Generate pcap file for foo dissector protocol"
description = '''Hey, Where can I get a foo.pcap file to test with the dissector?  I couldn&#x27;t find an example file in the Developer Guide, if there isn&#x27;t one how can I generate a pcap file? I tried serializing a struct conforming to the foo protocol in C++ but wireshark won&#x27;t open it. Any ideas?'''
date = "2013-11-20T03:52:00Z"
lastmod = "2015-02-24T22:36:00Z"
weight = 27155
keywords = [ "dissector", "pcap", "wireshark" ]
aliases = [ "/questions/27155" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Generate pcap file for foo dissector protocol](/questions/27155/generate-pcap-file-for-foo-dissector-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27155-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, Where can I get a foo.pcap file to test with the dissector? I couldn't find an example file in the Developer Guide, if there isn't one how can I generate a pcap file?</p><p>I tried serializing a struct conforming to the foo protocol in C++ but wireshark won't open it.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags">dissector pcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/10ba80b2d73f068e916ba35852a8a436?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lews%20Therin&#39;s gravatar image" /><p>Lews Therin<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lews Therin has one accepted answer">100%</span></p></div></div><div id="comments-container-27155" class="comments-container"></div><div id="comment-tools-27155" class="comment-tools"></div><div class="clear"></div><div id="comment-27155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27156"></span>

<div id="answer-container-27156" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27156-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to write a file in pcap or pcap-ng format for Wireshark to be able to open it. You can find descriptions of the file formats on the <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">Libpcap File Format</a> and <a href="http://wiki.wireshark.org/Development/PcapNg">PcapNg</a> wiki pages. Alternatively you can play with <a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">text2pcap</a> if you don't have a trace of a proper message exchange for your protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Nov '13, 07:33</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-27156" class="comments-container"></div><div id="comment-tools-27156" class="comment-tools"></div><div class="clear"></div><div id="comment-27156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40060"></span>

<div id="answer-container-40060" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40060-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check this out. A nice python file to meet your needs :) <a href="https://ask.wireshark.org/questions/18191/how-do-i-make-a-dissector-handle-a-particular-ethertype-ethernet-type-field-value">https://ask.wireshark.org/questions/18191/how-do-i-make-a-dissector-handle-a-particular-ethertype-ethernet-type-field-value</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '15, 22:36</strong></p><img src="https://secure.gravatar.com/avatar/fc7cd2942568a7b2705e55b532ff85c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mojo0809&#39;s gravatar image" /><p>Mojo0809<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mojo0809 has no accepted answers">0%</span></p></div></div><div id="comments-container-40060" class="comments-container"></div><div id="comment-tools-40060" class="comment-tools"></div><div class="clear"></div><div id="comment-40060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

