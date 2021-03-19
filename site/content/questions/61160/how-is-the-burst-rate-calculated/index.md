+++
type = "question"
title = "How is the burst rate calculated?"
description = '''When you go to &quot;Packet Lengths&quot; in the Statistics menu, you get the following:  My question is this: how are these values calculated? Are their formulas somewhere in the documentation, and if so, where? I&#x27;m especially interested in knowing how the &quot;burst rate&quot; is calculated. Another thing: is it pos...'''
date = "2017-05-02T08:12:00Z"
lastmod = "2017-05-02T08:26:00Z"
weight = 61160
keywords = [ "statistics", "burst", "packet", "wireshark" ]
aliases = [ "/questions/61160" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How is the burst rate calculated?](/questions/61160/how-is-the-burst-rate-calculated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61160-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When you go to "Packet Lengths" in the Statistics menu, you get the following:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_026_jnaz5hL.png" alt="alt text" /></p><p>My question is this: how are these values calculated? Are their formulas somewhere in the documentation, and if so, where?</p><p>I'm especially interested in knowing how the "burst rate" is calculated.</p><p>Another thing: is it possible to obtain this data through tshark? Thanks!</p></div><div id="question-tags" class="tags-container tags">statistics burst packet wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '17, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/d558cf05b6d572a77a868f3c4a394b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="workin221&#39;s gravatar image" /><p>workin221<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="workin221 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-61160" class="comments-container"></div><div id="comment-tools-61160" class="comment-tools"></div><div class="clear"></div><div id="comment-61160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61161"></span>

<div id="answer-container-61161" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61161-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Once <a href="https://ask.wireshark.org/users/3386/amato_c">@Amato</a>-C and I had evaluated it for this question: <a href="https://ask.wireshark.org/questions/42545/what-data-does-burst-rate-and-burst-start-provide-in-statistics-packet-lengths">https://ask.wireshark.org/questions/42545/what-data-does-burst-rate-and-burst-start-provide-in-statistics-packet-lengths</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '17, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-61161" class="comments-container"><span id="61165"></span><div id="comment-61165" class="comment"><div id="post-61165-score" class="comment-score"></div><div class="comment-text"><p>So, if I understand correctly, does this mean that the capture is divided and analyzed with a window of, say, 10ms, and the burst rate is the maximum number of packets sent in any such intervals?</p></div><div id="comment-61165-info" class="comment-info"><span class="comment-age">(02 May '17, 09:51)</span> workin221</div></div><span id="61166"></span><div id="comment-61166" class="comment"><div id="post-61166-score" class="comment-score">1</div><div class="comment-text"><p>Yes that is true.</p></div><div id="comment-61166-info" class="comment-info"><span class="comment-age">(02 May '17, 09:57)</span> Christian_R</div></div><span id="61167"></span><div id="comment-61167" class="comment"><div id="post-61167-score" class="comment-score"></div><div class="comment-text"><p>I see, thank you. Do you know if it's possible to obtain this information through tshark? I'm trying to write a python script that extracts this kind of information from a pcap file. I guess I can always do it "manually" though.</p></div><div id="comment-61167-info" class="comment-info"><span class="comment-age">(02 May '17, 10:08)</span> workin221</div></div></div><div id="comment-tools-61161" class="comment-tools"></div><div class="clear"></div><div id="comment-61161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

