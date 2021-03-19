+++
type = "question"
title = "Wireshark/tcpdump doesn&#x27;t capture all packets on WiFi"
description = '''Hello, i&#x27;ve got a strange problem when I´m capturning packets in my open WiFi-Network, if I set the WIFI-Card in Monitor-Mode and start Wireshark or tcpdump many beacons and other 802.11 stuff is appears. Also some HTTP traffic is showed but i´m missing important packets which does not appear in wir...'''
date = "2015-08-11T17:06:00Z"
lastmod = "2015-08-12T16:13:00Z"
weight = 44977
keywords = [ "wifi", "packets", "lost" ]
aliases = [ "/questions/44977" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark/tcpdump doesn't capture all packets on WiFi](/questions/44977/wiresharktcpdump-doesnt-capture-all-packets-on-wifi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44977-score" class="post-score" title="current number of votes">0</div><span id="post-44977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i've got a strange problem when I´m capturning packets in my open WiFi-Network, if I set the WIFI-Card in Monitor-Mode and start Wireshark or tcpdump many beacons and other 802.11 stuff is appears. Also some HTTP traffic is showed but i´m missing important packets which does not appear in wireshark..</p><p>I guess my WiFi Card is too slow for all Packets flying arround in the Network am I right?</p><p>In also tried promiscous mode, but in this mode no packets are captured, i guess my wifi card does not support this mode.</p><p>NIC: IBM Thinkpad 11a/b/g AR5BXB6 OS: KALI Linux x86 (newest)</p><p>Please help me with suggestions or answers why i'm not recieving all packets..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '15, 17:06</strong></p><img src="https://secure.gravatar.com/avatar/259ee2a78cb465805eea49d8874ba845?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eizi&#39;s gravatar image" /><p><span>eizi</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eizi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Aug '15, 03:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-44977" class="comments-container"></div><div id="comment-tools-44977" class="comment-tools"></div><div class="clear"></div><div id="comment-44977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44979"></span>

<div id="answer-container-44979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44979-score" class="post-score" title="current number of votes">1</div><span id="post-44979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That depends. Your card only supports 11a/b/g. Other traffic may be transmitted using 11n or 11ac. In that case, you could never capture those packets.</p><p>If you are able to capture Beacons from the WiFi network that you are associted with, then look to see if there are any HT or VHT information elements. If you see them, then the AP is configured to support technoligies that your adapter cannot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '15, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44979" class="comments-container"><span id="44980"></span><div id="comment-44980" class="comment"><div id="post-44980-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the answer!</p><p>What are HT or VHT elements?</p><p>Im capturing packets on the local machine which send/recieves the packets and I capture the packets with kali Linux in monitor mode, where many sent http packets from the local machine are missing/not recieved.</p><p>So i don´t think it is a problem with the wifi standards of the wifi stick because some http packets are captured from the adapter..am I right? Or is it possible that some http packets are sent with a/b/g standard and others with 11n which the adapter cant see?</p></div><div id="comment-44980-info" class="comment-info"><span class="comment-age">(11 Aug '15, 18:24)</span> <span class="comment-user userinfo">eizi</span></div></div><span id="44981"></span><div id="comment-44981" class="comment"><div id="post-44981-score" class="comment-score"></div><div class="comment-text"><p>HT and VHT elements are located within Beacon frames sent by the AP. You should see frames that are labeled as Beacons within your capture. Look at the Info field to see the frames labeled as Beacons. Then double click a Beacon frame to view the contents.</p><p>In your original post you mentioned that the adapter was configured in monitor mode. This will capture all packets of all SSID's from the currently selected channel. Are you certain that you are only observing traffic to/from your adapter?</p></div><div id="comment-44981-info" class="comment-info"><span class="comment-age">(11 Aug '15, 18:56)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="45023"></span><div id="comment-45023" class="comment"><div id="post-45023-score" class="comment-score"></div><div class="comment-text"><p>Ok,i've disabled the n standard in the router and only allow a/b/g and noew all packets are captured! Thank you very much.</p><p>But I dont understand why some packets are transported with different standards, is that normal? i thought the router and the station aalways use the same standard?</p><p>Now i've got another question and it would be very kind if someone could also answer this question :) Now i want buy a wifi stick which supports the n standard the5 ghz frequenz spectrum, packet injection, monitor and promiscuos mode. The stick should not be very expensive about 30 euros or cheaper..5ghz is no must have..</p><p>Thank you for your answers and suggestions!</p></div><div id="comment-45023-info" class="comment-info"><span class="comment-age">(12 Aug '15, 14:53)</span> <span class="comment-user userinfo">eizi</span></div></div><span id="45026"></span><div id="comment-45026" class="comment"><div id="post-45026-score" class="comment-score"></div><div class="comment-text"><p>Please ask that question separately, so that people interested in answers to <em>that</em> question can find it. This is a Q&amp;A site, not a forum; the idea is that people should be able to try to see whether their question has already been asked and answered before asking it, so we don't want threads that involve multiple questions, we want individual questions with discussion as needed to understand the question or answer.</p></div><div id="comment-45026-info" class="comment-info"><span class="comment-age">(12 Aug '15, 16:09)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="45027"></span><div id="comment-45027" class="comment"><div id="post-45027-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But I dont understand why some packets are transported with different standards, is that normal? i thought the router and the station aalways use the same standard?</p></blockquote><p>The router - by which I presume you mean "the access point" - <em>when talking to a particular station</em> will use whatever is the appropriate standard. However, there may be multiple stations on the network, using different standards; for example, there may be one machine that only supports 11b, another that supports 11g, and still another that supports 11n). If you're capturing with a card that supports 11g but not 11n, you'll be able to see traffic to and from the 11b machine and traffic to and from the 11g machine, but <em>not</em> traffic to and from the 11n machine.</p></div><div id="comment-45027-info" class="comment-info"><span class="comment-age">(12 Aug '15, 16:13)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-44979" class="comment-tools"></div><div class="clear"></div><div id="comment-44979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

