+++
type = "question"
title = "Packet loss and Jitter in a Skype communication"
description = '''Hi,  I captured the traffic during a skype conversation in the two end points. Then I have decoded the UDP&#x27;s packets with an RTP protocol, in this way i&#x27;m able to see the timestamps of each packet. But, when I go to the option Telephony--&amp;gt;RTP--&amp;gt;show all the streams.., in the fields : loss pack...'''
date = "2012-10-24T04:47:00Z"
lastmod = "2012-10-24T07:21:00Z"
weight = 15221
keywords = [ "skype" ]
aliases = [ "/questions/15221" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet loss and Jitter in a Skype communication](/questions/15221/packet-loss-and-jitter-in-a-skype-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15221-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I captured the traffic during a skype conversation in the two end points. Then I have decoded the UDP's packets with an RTP protocol, in this way i'm able to see the timestamps of each packet. But, when I go to the option Telephony--&gt;RTP--&gt;show all the streams.., in the fields : loss packets and jitter appears always a 0, and I don't know why. Somebody can help me?</p><p>My objective is to do an study of the packets loss and jitter between a skype conversation.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">skype</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '12, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/96dc4282b6b2916bfdc223c7082d8140?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vickynp123&#39;s gravatar image" /><p>Vickynp123<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vickynp123 has no accepted answers">0%</span></p></div></div><div id="comments-container-15221" class="comments-container"></div><div id="comment-tools-15221" class="comment-tools"></div><div class="clear"></div><div id="comment-15221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15227"></span>

<div id="answer-container-15227" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15227-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Skype doesn't use RTP. It uses its own proprietary protocol so trying to decode its traffic as RTP isn't likely going to work out very well.</p><p>For some more info about the protocol (and the beginnings of a Skype dissector in Wireshark) see Wiki's <a href="http://wiki.wireshark.org/Skype">Skype page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '12, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-15227" class="comments-container"><span id="15241"></span><div id="comment-15241" class="comment"><div id="post-15241-score" class="comment-score"></div><div class="comment-text"><p>Ok, thanks. So, somebody knows any other VoIP application that works with RTP for be able with to study the jitter and the packet losses with wireshark?¿?</p><p>Thanks</p></div><div id="comment-15241-info" class="comment-info"><span class="comment-age">(24 Oct '12, 23:39)</span> Vickynp123</div></div><span id="15282"></span><div id="comment-15282" class="comment"><div id="post-15282-score" class="comment-score"></div><div class="comment-text"><p>I have found one that is exactly the software i was looking for, their name is express talk, now I can see the value of the jitter and the packets loss!</p></div><div id="comment-15282-info" class="comment-info"><span class="comment-age">(25 Oct '12, 08:26)</span> Vickynp123</div></div></div><div id="comment-tools-15227" class="comment-tools"></div><div class="clear"></div><div id="comment-15227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

