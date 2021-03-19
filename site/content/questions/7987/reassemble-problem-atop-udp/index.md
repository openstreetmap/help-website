+++
type = "question"
title = "Reassemble Problem atop UDP"
description = '''hi, so i am developing a dissector for decoding a specified protocol atop udp. so the whole data is in the pdu of udp. so i cannot show you the code because of it is not allowed to me! so i describe.  There was another reassemble problem here in the askings by chris: so i looked and tryed anything b...'''
date = "2011-12-15T07:38:00Z"
lastmod = "2011-12-15T15:22:00Z"
weight = 7987
keywords = [ "fragment", "linkingcolors", "problem", "dissector", "reassemble" ]
aliases = [ "/questions/7987" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reassemble Problem atop UDP](/questions/7987/reassemble-problem-atop-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7987-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>so i am developing a dissector for decoding a specified protocol atop udp. so the whole data is in the pdu of udp.</p><p>so i cannot show you the code because of it is not allowed to me!</p><p>so i describe.</p><p>There was another reassemble problem here in the askings by chris: so i looked and tryed anything but it does not work.</p><p>ok, for example there are four packets noticed. these four belong together. so they have an sequence id which i am using in frag_msg for reassembling. More Over in the protocl is specified a msg_number and a total number. in example case these on is 4. so now i want to reassemble these 4 packets with the same sequence id. so i get 4 fragments. YES???</p><p>ok my code gets 4 packets but never i see in the info column "Reassembled Message"?</p><p>so the packets have some header stuff which i hang on the display tree and after a few steps my reassemble code is used. now in the packet its possible that maybe one block beginning in the first packet has 3000byte. so in the first there are maybe 800 byte i have to decode in the following way. After the header there is a blockinfo with how much byte it does have and so on. If this bytecount is longer than the packet i have to use the payload of the second packet.</p><p>so i thought reassembling puts me the wohle rest of every payload of the "linked" packets to this new_tvb and shows "Reassembled message", but this does not work. but for correct decoding i have to get all of these payload in ones because of how i described one block can "overlap" in to the payload of the next package.</p><p>so some more information: before reassembling i put the header infos and other stuff to the visible tree in wireshark and after this i reassemble. My whole dissecting code is just in one dissect function? Could this be the problem? Do i have to first reassemble and then calling a new one dissector??</p><p>i dont know, 3 weeks of working so hard and i does not have any idea.</p><p>One more to reassemble.</p><p>How i can make it possible to add links between the fragments that are belonging together, so the first packet should have a link in the dissector tree to the second packet, you know?</p><p>so after all, my dissector is written as a plugin it isnt a build in!</p><p>sorry for bad englisch</p><p>if something missing to understand it completely plz answer also!</p><p>plz help me!!!</p><p>one thing to add. how can i change the highlight colors in wireshark. so maybe if i have packet of this type i want green backing. is there any possibility to set these colours within the dissector so something like</p><p>if message reassembled -&gt; backing color = green</p><p>thanks a lot!!!!</p></div><div id="question-tags" class="tags-container tags">fragment linkingcolors problem dissector reassemble</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '11, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/b19995667dd7e285be5ed8c1ac50cf74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anthracis&#39;s gravatar image" /><p>Anthracis<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anthracis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '11, 07:47</p></div></div><div id="comments-container-7987" class="comments-container"><span id="7988"></span><div id="comment-7988" class="comment"><div id="post-7988-score" class="comment-score"></div><div class="comment-text"><p>i had forgotton. my control if more fragments are avaible ist something like this:</p><p>msg_number &lt; total_number</p><p>so it should work but it doesnt!</p></div><div id="comment-7988-info" class="comment-info"><span class="comment-age">(15 Dec '11, 07:40)</span> Anthracis</div></div></div><div id="comment-tools-7987" class="comment-tools"></div><div class="clear"></div><div id="comment-7987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8000"></span>

<div id="answer-container-8000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8000-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since we cannot see your code, and your description is 'complex', I would recommend to look at the RTP dissector. It runs on top of UDP and has reassembly build in. You can learn and copy from that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '11, 15:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8000" class="comments-container"><span id="8035"></span><div id="comment-8035" class="comment"><div id="post-8035-score" class="comment-score"></div><div class="comment-text"><p>thx so far i will have a look at</p></div><div id="comment-8035-info" class="comment-info"><span class="comment-age">(19 Dec '11, 02:49)</span> Anthracis</div></div></div><div id="comment-tools-8000" class="comment-tools"></div><div class="clear"></div><div id="comment-8000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

