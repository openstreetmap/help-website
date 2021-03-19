+++
type = "question"
title = "dvb-s2_bb dissector not found"
description = '''Hello. I&#x27;m trying to make wireshark analyze the file with a pure dvb-s2 stream (without encapsulation in ethernet header). I didn&#x27;t find such a type for the libpcap or pcap-ng header. So I generated a file with a type 147 (DLT USER 0) and then tried to represent this type as dvb-s2-bb in wireshark. ...'''
date = "2013-12-06T03:37:00Z"
lastmod = "2013-12-06T06:23:00Z"
weight = 27857
keywords = [ "dissector" ]
aliases = [ "/questions/27857" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dvb-s2\_bb dissector not found](/questions/27857/dvb-s2_bb-dissector-not-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27857-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I'm trying to make wireshark analyze the file with a pure dvb-s2 stream (without encapsulation in ethernet header). I didn't find such a type for the libpcap or pcap-ng header. So I generated a file with a type 147 (DLT USER 0) and then tried to represent this type as dvb-s2-bb in wireshark. If I've got it right, I must enter the dissector name in the "Payload protocol" field. I tried the names "DVB-S2", "dvb-s2", "dvb-s2-bb" but they didn't work - I received the message "error in column 'Payload protocol': dissector not found". Then accordingly to the list in menu "Internals -&gt; Supported protocols (slow!)" I tried "dvb-s2_bb" but it wasn't recognized also. What am I doing wrong and where could I find the real list of all possible dissectors? Thank you and sorry for my english.</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '13, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/1ae4ee30c957f4fe55361fe2372b4b49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zaytsev%20Artem&#39;s gravatar image" /><p>Zaytsev Artem<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zaytsev Artem has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Dec '13, 03:39</p></div></div><div id="comments-container-27857" class="comments-container"></div><div id="comment-tools-27857" class="comment-tools"></div><div class="clear"></div><div id="comment-27857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27869"></span>

<div id="answer-container-27869" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27869-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunaltly the dissector isn't registered by name so you can't call it from the "USER DLT" without a code change like:</p><p>register_dissector("dvb_s2_bb", dissect_dvb_s2_bb, proto_dvb_s2_bb);</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '13, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-27869" class="comments-container"><span id="27871"></span><div id="comment-27871" class="comment"><div id="post-27871-score" class="comment-score"></div><div class="comment-text"><p>Thank you, but could you additionally clarify if there's an opportunity to see the list of all the registered dissectors anywhere? Or the only way to know about registration is to look through the source code of a concrete dissector? And as little-off-topic: what is the real reasonable purpose for the dissectors to be registered? Why not to register all dissectors automatically?</p></div><div id="comment-27871-info" class="comment-info"><span class="comment-age">(06 Dec '13, 07:44)</span> Zaytsev Artem</div></div></div><div id="comment-tools-27869" class="comment-tools"></div><div class="clear"></div><div id="comment-27869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

