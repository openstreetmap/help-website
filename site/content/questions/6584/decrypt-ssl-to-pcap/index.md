+++
type = "question"
title = "decrypt ssl to pcap"
description = '''Hi, I&#x27;m trying to decrypt an ssl conversation using the ssl key.  This is working in the wireshark gui. When I try to decrypt in tshark, this is also working, but I wan to decrypt it and save the result as a pcap file. This doesn&#x27;t work. When I use : tshark -o &quot;ssl.desegment_ssl_records: TRUE&quot; -o &quot;s...'''
date = "2011-09-27T02:34:00Z"
lastmod = "2011-09-27T06:22:00Z"
weight = 6584
keywords = [ "ssl", "pcap", "decrypt" ]
aliases = [ "/questions/6584" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [decrypt ssl to pcap](/questions/6584/decrypt-ssl-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6584-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to decrypt an ssl conversation using the ssl key.<br />
</p><p>This is working in the wireshark gui.<br />
When I try to decrypt in tshark, this is also working, but I wan to decrypt it and save the result as a pcap file. This doesn't work.<br />
When I use : tshark -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list: 10.135.56.22,443,http,/trace/test/test.pem" -t ad -r 443_test.pcap -w decrypted.pcap<br />
the result is the same as the input-file.<br />
</p><p>Is there a way I can decrypt via cli to a pcap file?<br />
I want to use the resulting pcap-file as input for tcpick, so I can save complete TCP sessions.</p></div><div id="question-tags" class="tags-container tags">ssl pcap decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '11, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/eb50bff83ed5e9b771d595c492350720?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fcozijnsen&#39;s gravatar image" /><p>fcozijnsen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fcozijnsen has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-6584" class="comments-container"></div><div id="comment-tools-6584" class="comment-tools"></div><div class="clear"></div><div id="comment-6584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6590"></span>

<div id="answer-container-6590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6590-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The short answer: Wireshark/tshark aren't capable of saving decrypted packets to a pcap file.</p><p>See message thread starting at http://www.wireshark.org/lists/wireshark-users/201105/msg00000.html for some (possibly) relevant information.</p><p>See especially: http://www.wireshark.org/lists/wireshark-users/201105/msg00002.html</p><p>A Google search may find further info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '11, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Sep '11, 06:38</p></div></div><div id="comments-container-6590" class="comments-container"><span id="6591"></span><div id="comment-6591" class="comment"><div id="post-6591-score" class="comment-score"></div><div class="comment-text"><p>Is there an other way to create seperate files for each communication session? I'm now using tcpick to seperate the tcp streams from each other (and save each stream in a file) but this doesn't support ssl. I rather use wireshark, but is this even possible?</p></div><div id="comment-6591-info" class="comment-info"><span class="comment-age">(27 Sep '11, 06:28)</span> fcozijnsen</div></div></div><div id="comment-tools-6590" class="comment-tools"></div><div class="clear"></div><div id="comment-6590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

