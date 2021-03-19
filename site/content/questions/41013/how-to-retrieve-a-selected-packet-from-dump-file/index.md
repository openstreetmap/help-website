+++
type = "question"
title = "How to retrieve a selected packet from dump file?"
description = '''Hi all, I am new to wireshark, I know that I am asking a silly doubt. in case of wireshark, once we start the capture we can dump each packet using pcap_dump() method. but how to retrieve a selected packet from dump file once we click on the selected row from listview in UI? Is there any offset for ...'''
date = "2015-03-30T07:19:00Z"
lastmod = "2015-03-30T08:10:00Z"
weight = 41013
keywords = [ "c", "pcap", "dumpcap", "wireshark" ]
aliases = [ "/questions/41013" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to retrieve a selected packet from dump file?](/questions/41013/how-to-retrieve-a-selected-packet-from-dump-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41013-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I am new to wireshark, I know that I am asking a silly doubt. in case of wireshark, once we start the capture we can dump each packet using pcap_dump() method. but how to retrieve a selected packet from dump file once we click on the selected row from listview in UI? Is there any offset for each packet? how can we get a pointer to each packet? How wireshark is giving the description of each packet once we select on row?</p><p>thanks , sathish</p></div><div id="question-tags" class="tags-container tags">c pcap dumpcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '15, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/74ab8994ff0e776c06c6b4f14f4dfca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sathish308&#39;s gravatar image" /><p>sathish308<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sathish308 has no accepted answers">0%</span></p></div></div><div id="comments-container-41013" class="comments-container"></div><div id="comment-tools-41013" class="comment-tools"></div><div class="clear"></div><div id="comment-41013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41021"></span>

<div id="answer-container-41021" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41021-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how can we get a pointer to each packet?</p></blockquote><p>pcap and pcap-ng files have a defined structure.</p><blockquote><p><a href="https://wiki.wireshark.org/Development/LibpcapFileFormat">https://wiki.wireshark.org/Development/LibpcapFileFormat</a><br />
<a href="https://wiki.wireshark.org/Development/PcapNg">https://wiki.wireshark.org/Development/PcapNg</a><br />
</p></blockquote><p>So, if you want to simulate the Wireshark behavior, you'll have to read all frames in memory and do the book keeping yourself. This means: You need to build an internal data structure in RAM which allows you to access every frame directly.</p><p>The other way would be to simply read the capture file and "skip" to frame number x by reading and forgetting those frames you don't need.</p><p>Please see PCAP programming tutorial on the net:</p><blockquote><p><a href="http://www.tcpdump.org/pcap.htm">http://www.tcpdump.org/pcap.htm</a><br />
<a href="http://homes.di.unimi.it/~gfp/SiRe/2002-03/progetti/libpcap-tutorial.html">http://homes.di.unimi.it/~gfp/SiRe/2002-03/progetti/libpcap-tutorial.html</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '15, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Mar '15, 08:11</p></div></div><div id="comments-container-41021" class="comments-container"><span id="41143"></span><div id="comment-41143" class="comment"><div id="post-41143-score" class="comment-score"></div><div class="comment-text"><p>hi, kurt</p><p>here I can do like this,</p><p>if I need 100th packet I can keep it in a while loop as int count=1; while(count&lt;=100) { packet_next_ex(); count++; if(count==100) { then I can take the data;} } I can get the selected packet data. but, will it be good solution? if my requirement is 100000 packet, then loop has to run for 100000 times. I think it is time consuming process. can you suggest me which is good solution for it....</p></div><div id="comment-41143-info" class="comment-info"><span class="comment-age">(02 Apr '15, 05:36)</span> sathish308</div></div><span id="41149"></span><div id="comment-41149" class="comment"><div id="post-41149-score" class="comment-score"></div><div class="comment-text"><p>Please add more details (maybe with an example), as I don't understand what you are trying to do.</p></div><div id="comment-41149-info" class="comment-info"><span class="comment-age">(02 Apr '15, 06:41)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-41021" class="comment-tools"></div><div class="clear"></div><div id="comment-41021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

