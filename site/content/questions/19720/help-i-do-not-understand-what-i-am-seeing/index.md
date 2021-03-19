+++
type = "question"
title = "Help, I do not understand what I am seeing"
description = '''I have a NAS that is running slow, has been. When I run Wireshark while opening a file on that appliance I am seeing lots and lots of the examples below. (To me it looks like way to many) 90[TCP Dup ACK 8796#16] 6873&amp;gt;microsoft-ds [ACK] seq=27065 Ack=8756344 Win=1619 Len=0 SRE=8824884 SLE=88161 15...'''
date = "2013-03-21T11:14:00Z"
lastmod = "2013-03-21T13:14:00Z"
weight = 19720
keywords = [ "dup", "ack" ]
aliases = [ "/questions/19720" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Help, I do not understand what I am seeing](/questions/19720/help-i-do-not-understand-what-i-am-seeing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19720-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a NAS that is running slow, has been. When I run Wireshark while opening a file on that appliance I am seeing lots and lots of the examples below. (To me it looks like way to many)</p><p>90[TCP Dup ACK 8796#16] 6873&gt;microsoft-ds [ACK] seq=27065 Ack=8756344 Win=1619 Len=0 SRE=8824884 SLE=88161</p><p>1514 [TCP segment of a reasembled PDU]</p></div><div id="question-tags" class="tags-container tags">dup ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '13, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/7793a46b56e72b3f8a4f614b203825ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freebird317&#39;s gravatar image" /><p>freebird317<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freebird317 has no accepted answers">0%</span></p></div></div><div id="comments-container-19720" class="comments-container"></div><div id="comment-tools-19720" class="comment-tools"></div><div class="clear"></div><div id="comment-19720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="19722"></span>

<div id="answer-container-19722" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19722-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hard to tell without more details, but Dup ACKs are acknowledgements that were repeated (in this example 16 times, so a total of 17 identical acknowledges). This is usually a sign of either lost packets or impatient receiving nodes. Problem with NAS captures is that they get pretty big, but you could try to look for packet loss, retransmissions or zero window problems. There is a combo filter that will show you issues like that: tcp.analysis.flags.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19722" class="comments-container"></div><div id="comment-tools-19722" class="comment-tools"></div><div class="clear"></div><div id="comment-19722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19721"></span>

<div id="answer-container-19721" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19721-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Duplicate acknowledgements gets triggered when there is a packet loss. It is the client/receiver's way of notifying the server/sender that "hey i some how lost a segment can you please retransmit again"In normal case server pay attention to these duplicate acks and sends a retransmission to the client. You can set the display filter as <strong>tcp.analysis.flags</strong> to dig further.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-19721" class="comments-container"><span id="19723"></span><div id="comment-19723" class="comment"><div id="post-19723-score" class="comment-score"></div><div class="comment-text"><p>When I apply tcp.analysis.flags I get nothing but black and red with items like</p><p>TCP DUP ACK TCP Fast Retransmission TCP Retransmission TCP Out-Of-Order</p></div><div id="comment-19723-info" class="comment-info"><span class="comment-age">(21 Mar '13, 11:30)</span> freebird317</div></div><span id="19724"></span><div id="comment-19724" class="comment"><div id="post-19724-score" class="comment-score"></div><div class="comment-text"><p>It is not nothing it got everything it has to show.Those black and red items are anomalies and their remedies. For Duplicate acknowledgements the solution tcp implements is tcp retransmission/tcp fast retransmission.Closely follow a trace by right clicking on any duplicate ack packet and selecting follow tcp stream.</p></div><div id="comment-19724-info" class="comment-info"><span class="comment-age">(21 Mar '13, 11:33)</span> krishnayeddula</div></div><span id="19725"></span><div id="comment-19725" class="comment"><div id="post-19725-score" class="comment-score"></div><div class="comment-text"><p>Not always are those anomalies critical. Very often you'll see simple packet out-of-order arrivals to give you lots of duplicate acks, "TCP retransmissions" (which they aren't, just a little late) and TCP out-of-order.</p><p>In this case here I guess it is real packet loss though, because you do not get more than 1 or 2 dup acks when facing out-of-order symptoms. Here, 16 dup acks are a good sign that there is in fact real packet loss.</p></div><div id="comment-19725-info" class="comment-info"><span class="comment-age">(21 Mar '13, 11:43)</span> Jasper ♦♦</div></div><span id="19730"></span><div id="comment-19730" class="comment"><div id="post-19730-score" class="comment-score"></div><div class="comment-text"><p>Looking at frame 128 - 1514 [TCP segment of a reassembled PDU] I see , for [SEQ/ACK] I am getting [reassembled PDU in frame: 166] Looking at frame 166 I see 23 Reassembled TCP Segments below that there are links to all the 23 Reassembled TCP Segments. Does this mean I am dropping packets?</p></div><div id="comment-19730-info" class="comment-info"><span class="comment-age">(21 Mar '13, 12:43)</span> freebird317</div></div></div><div id="comment-tools-19721" class="comment-tools"></div><div class="clear"></div><div id="comment-19721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19733"></span>

<div id="answer-container-19733" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19733-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @Jasper is saying, it looks like there is indeed a bit of packet loss in your network. Assuming you are running this NAS in a local network, I can imagine 2 issues that might be causing the packet loss and therefor the slow transfer speeds:</p><ul><li>Your NAS and/or your client have a duplex mismatch on the switch that they are connected too</li><li>You have a Wifi network that might be interfered with by other networks</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19733" class="comments-container"></div><div id="comment-tools-19733" class="comment-tools"></div><div class="clear"></div><div id="comment-19733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

