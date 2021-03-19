+++
type = "question"
title = "Passing data between packets (and not between dissectors)"
description = '''Hello, I am writing a dissector and I would like to recover some information contained in a packet A, which is sent first, and pass it to a packet B.  For example, sometimes my protocol have fragmented data (the B packet may be too large and is then concatenated into several smaller packets) but the...'''
date = "2013-08-21T01:22:00Z"
lastmod = "2013-08-27T07:29:00Z"
weight = 23894
keywords = [ "packets", "passing", "data", "between" ]
aliases = [ "/questions/23894" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Passing data between packets (and not between dissectors)](/questions/23894/passing-data-between-packets-and-not-between-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23894-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am writing a dissector and I would like to recover some information contained in a packet A, which is sent first, and pass it to a packet B. For example, sometimes my protocol have fragmented data (the B packet may be too large and is then concatenated into several smaller packets) but the information on how this packet is fragmented is embedded in the previous packet (the packet A). Hence, I would like to save these fragmentation parameters from packet A and use them to recover (to defragment) the packet B. Is this possible ?</p><p>Thank you for your help!</p></div><div id="question-tags" class="tags-container tags">packets passing data between</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p>Afrim<br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-23894" class="comments-container"></div><div id="comment-tools-23894" class="comment-tools"></div><div class="clear"></div><div id="comment-23894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23907"></span>

<div id="answer-container-23907" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23907-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at reassembly.[ch] in the epan dir. Read readme.dissector (TCP reassembly) and check out dissectors using the reassembly interface. If you need to preserve information between packets the conversations interface my be what you need possibly paired with "p_get_proto_data()". Note that packets are only read sequentially on the first pass after that a packet may be accessed randomly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-23907" class="comments-container"><span id="23910"></span><div id="comment-23910" class="comment"><div id="post-23910-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders,</p><p>Reassembly is not a problem I already succeeded in data reassembling but the fragmentation parameters were within the packet. I have seen the conversation interface in some protocols (SMTP) and I wasn't sure if it was what i needed. Also I tried "p_get_proto_data()" but not paired with conversation interface (It was definitely useless since pinfo is cleared for every packet).</p><p>I will take a look at the conversation interface.</p><p>Thank you for your answer.</p></div><div id="comment-23910-info" class="comment-info"><span class="comment-age">(21 Aug '13, 08:23)</span> Afrim</div></div></div><div id="comment-tools-23907" class="comment-tools"></div><div class="clear"></div><div id="comment-23907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24098"></span>

<div id="answer-container-24098" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24098-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, conversation interface seems to be what I need but something is wrong when I try to use it. Like I said on my first post I have two packets (lets say A and B) the information I want to save is in packet A so when Packet A is detected in my protocol I save informations using :</p><p>conversation_new(pinfo-&gt;fd-&gt;num, &amp;pinfo-&gt;src, &amp;pinfo-&gt;dst, pinfo-&gt;ptype, pinfo-&gt;srcport, pinfo-&gt;destport, 0);</p><p>And then when Packet B is detected I call :</p><p>find_conversation(pinfo-&gt;fd-&gt;num, &amp;pinfo-&gt;src, &amp;pinfo-&gt;dst, pinfo-&gt;ptype, pinfo-&gt;srcport, pinfo-&gt;destport, 0);</p><p>But this always return NULL value.</p><p>Ofc I call conversation_add_proto_data() to save the data I want to reuse in Packet B.</p><p>Did I missed something ?</p><p>EDIT : Ok I found my msitake problem resolved :)</p><p>EDIT2 : I was setting short addresses with 4 bytes instead of 2. The 2 more bytes were not equal in packet A and packet B so when I pass src/dst addresses in create/find conversation it fail ofc.</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '13, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p>Afrim<br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Aug '13, 12:27</p></div></div><div id="comments-container-24098" class="comments-container"><span id="24105"></span><div id="comment-24105" class="comment"><div id="post-24105-score" class="comment-score"></div><div class="comment-text"><p>So for the benefit of others what was the mistake?</p><p>Please edit your "answer" with the correct solution.</p></div><div id="comment-24105-info" class="comment-info"><span class="comment-age">(27 Aug '13, 10:01)</span> grahamb ♦</div></div></div><div id="comment-tools-24098" class="comment-tools"></div><div class="clear"></div><div id="comment-24098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

