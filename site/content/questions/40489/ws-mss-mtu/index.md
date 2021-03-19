+++
type = "question"
title = "WS / MSS / MTU"
description = '''hi all, i have a question. i spent some time reading about TCP Window Size , Maximum Segment Size (MSS) and Maximum Transmission Unit (MTU).  Let&#x27;s assume that the receiver window size is 16,384 bytes which means that the sender can send up to 16,384 bytes before stopping to wait for an acknowledgem...'''
date = "2015-03-11T14:30:00Z"
lastmod = "2015-03-11T14:48:00Z"
weight = 40489
keywords = [ "ws" ]
aliases = [ "/questions/40489" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [WS / MSS / MTU](/questions/40489/ws-mss-mtu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40489-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all,</p><p>i have a question. i spent some time reading about TCP Window Size , Maximum Segment Size (MSS) and Maximum Transmission Unit (MTU).</p><p>Let's assume that the receiver window size is 16,384 bytes which means that the sender can send up to 16,384 bytes before stopping to wait for an acknowledgement. Let's also assume that the maximum segment size is 1024. This means that the sender can send 1024 bytes 16 times before it will stop sending and wait for an acknowledgement. So when A is the sender and B is the receiver we will always look and take into count the values provided from host B, right ? i mean it's WS and MSS ?</p><p>one more thing , while reading about MTU i came across this :</p><p><a href="http://kb.linksys.com/Linksys/GetArticle.aspx?docid=fbf8e8564632422eaa8ea80bf9dcba64_386.xml">http://kb.linksys.com/Linksys/GetArticle.aspx?docid=fbf8e8564632422eaa8ea80bf9dcba64_386.xml</a></p><p>setting up the correct MTU size. on my router it was configured by default 1500 bytes i followed the steps and it looks like fragmentation would stop to occur at 1470 bytes . would this really make such a big difference in performance when i change it to 1470 bytes ?</p><p>also does it often happen that because the MMS is bigger then the MTU that fragmentation occurs ?</p><p>thank you in advance for all of your answers</p><p>regards</p><p>Adam</p></div><div id="question-tags" class="tags-container tags">ws</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '15, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-40489" class="comments-container"></div><div id="comment-tools-40489" class="comment-tools"></div><div class="clear"></div><div id="comment-40489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40491"></span>

<div id="answer-container-40491" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40491-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. The sender has to always pay attention to the window size of the receiver, because it cannot send more than that without acknowledgement - otherwise, the receiver will most likely discard further segments if the window size is exceeded. The MSS is something where it makes sense for the sender not to exceed the value of the receiver, because it must assume that larger segments are not going to get through.</p><p>It is wise to try to avoid fragmentation, because it puts additional load on the systems involved, so if you know that the MTU of 1500 is too big you should reduce it until fragmentation is not an issue anymore. Reducing the MTU will lower the efficiency, but it will probably hurt more if packets have to be fragmented.</p><p>MSS can never be bigger than the MTU (it's actually at least 40 bytes less, 20 bytes for the TCP header, 20 bytes for the IPv4 header). That's because if you reduce MTU, MSS is automatically reduced as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40491" class="comments-container"></div><div id="comment-tools-40491" class="comment-tools"></div><div class="clear"></div><div id="comment-40491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40493"></span>

<div id="answer-container-40493" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40493-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When A is sending, it takes into account the last seen WS from B and visa versa. MSS is a different story. It is deducted from the local interface that is used for sending the data. However, it can be changed by using the TCP option to set the MSS. In that case it uses the MSS as it has been received. Please note that any hop in between B and A can change the value of the MSS option to prevent fragmentation taking place later on.</p><p>Consider a network where there is an IPsec tunnel somewhere in the middle. And let's assume the IPsec headers take 50 extra bytes. If B sends a MSS of 1460 (based on its ethernet interface), the VPN router can lower this to 1410. So when A sends TCP segments of 1410, it will be 1450 bytes on the network and the IPsec headers can still be added without the need to fragment the packet.</p><p>Then MTU is always just a local thing of the data link layer. This means between A and B there can be mediums with larger MTU sizes and also mediums with lower MTU values.</p><p>There might not be a big performance hit when fragmentation occurs. However, some devices don't work really well with fragmentation. For instance, some firewalls by default won't pass fragmented traffic.</p><p>If a frame is too big to forward on the next link, because the MTU of the next link is smaller than the packet size, then fragmentation occurs. A router never segments traffic at the TCP layer, it is only aware of the IP datagram and will split it up if necessary to forward it towards the destination.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 14:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40493" class="comments-container"><span id="40494"></span><div id="comment-40494" class="comment"><div id="post-40494-score" class="comment-score"></div><div class="comment-text"><p>So MSS is determined during the initial handshake? now im confused... So each hope will change the MSS? Not fragment the packet? where do we get the MSS value from? Is it the NIC's driver? How is MSS able to prevent fragmentation? so if we now that data needs to go outside our LAN it will takeq thew MSS fromq the router?</p></div><div id="comment-40494-info" class="comment-info"><span class="comment-age">(11 Mar '15, 15:10)</span> adasko</div></div><span id="40495"></span><div id="comment-40495" class="comment"><div id="post-40495-score" class="comment-score">1</div><div class="comment-text"><p>Yes, MSS is determined in the handshake. Both nodes see what the other MSS is, and usually both use the lower value.</p><p>Each hop <strong>can</strong> change the MSS, not <strong>will</strong>. Some devices do it because they know the MTU is too small for the MSS seen in the packet. MSS is usually derived from the MTU. The NIC driver knows the MTU of the medium, and MSS is calculated from it.</p></div><div id="comment-40495-info" class="comment-info"><span class="comment-age">(11 Mar '15, 15:57)</span> Jasper ♦♦</div></div><span id="40507"></span><div id="comment-40507" class="comment"><div id="post-40507-score" class="comment-score"></div><div class="comment-text"><p>i see. so both MS and MSS are defined on the Transport Layer, right ? and MMS is the number of bytes that can be send at a time ? so this determines how big a single packet will on the Network Layer, yes ? if yes, i'm a bit confused because i red that the MTU is determined by the Data Link Layer and the value is then past over to the Network Layer... so for me to get it right. transport layer says the MSS is xyz so in the network layer packets are created with this size but then while moving them to Layer 2 it sees that the link will not be able to handle this size of packets and asks to fragment them (so fragmentation will occur on Layer 3 , yes? )</p><p>thank's for any response</p></div><div id="comment-40507-info" class="comment-info"><span class="comment-age">(12 Mar '15, 01:40)</span> adasko</div></div></div><div id="comment-tools-40493" class="comment-tools"></div><div class="clear"></div><div id="comment-40493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

