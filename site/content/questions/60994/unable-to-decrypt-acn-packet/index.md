+++
type = "question"
title = "Unable to decrypt ACN packet"
description = '''Hello, I need to analyse some ACN packets. It should be possible with Wireshark, because ACN is on the wireshark wiki. But if I test it I only see a unanalysed UDP packet. is this a bug or is it just me?  Greetings, Koen Van der Aa'''
date = "2017-04-23T13:29:00Z"
lastmod = "2017-04-24T22:23:00Z"
weight = 60994
keywords = [ "acn" ]
aliases = [ "/questions/60994" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decrypt ACN packet](/questions/60994/unable-to-decrypt-acn-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60994-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I need to analyse some ACN packets. It should be possible with Wireshark, because ACN is on the wireshark wiki. But if I test it I only see a unanalysed UDP packet. is this a bug or is it just me?</p><p>Greetings,</p><p>Koen Van der Aa</p></div><div id="question-tags" class="tags-container tags">acn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '17, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/8d7248d32fa12892a5cefbfd43a38d83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoenGSF&#39;s gravatar image" /><p>KoenGSF<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoenGSF has no accepted answers">0%</span></p></div></div><div id="comments-container-60994" class="comments-container"><span id="61017"></span><div id="comment-61017" class="comment"><div id="post-61017-score" class="comment-score"></div><div class="comment-text"><p>Hi thanks for your reaction.</p><p>This is my packet it looks good to me <img src="https://osqa-ask.wireshark.org/upfiles/sACN_packet.jpg" alt="alt text" /></p></div><div id="comment-61017-info" class="comment-info"><span class="comment-age">(24 Apr '17, 12:47)</span> KoenGSF</div></div><span id="61018"></span><div id="comment-61018" class="comment"><div id="post-61018-score" class="comment-score"></div><div class="comment-text"><p>Can you share the raw capture file? Not only a screenshot?</p></div><div id="comment-61018-info" class="comment-info"><span class="comment-age">(24 Apr '17, 12:57)</span> Uli</div></div><span id="61019"></span><div id="comment-61019" class="comment"><div id="post-61019-score" class="comment-score"></div><div class="comment-text"><p>i don't know how to share it on the forum so i made a link to it.</p><p>I also can't analyse the standaard wireshark packet so i think ACN is not include.</p><p><a href="https://wiki.wireshark.org/ACN">Acn Wiki with the standaard packet</a></p><p><a href="https://1drv.ms/u/s!AqzSjoM2GmrcoaR-GINwgVGwd9AO8g">My Packet</a></p></div><div id="comment-61019-info" class="comment-info"><span class="comment-age">(24 Apr '17, 13:35)</span> KoenGSF</div></div></div><div id="comment-tools-60994" class="comment-tools"></div><div class="clear"></div><div id="comment-60994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61022"></span>

<div id="answer-container-61022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61022-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Got it: you first have to enable the 'ACN over UDP' protocol.</p><p>To do so go to "Analyze' -&gt; 'Enabled Protocols' and enable 'acn_udp'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '17, 22:23</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></img></div></div><div id="comments-container-61022" class="comments-container"><span id="61027"></span><div id="comment-61027" class="comment"><div id="post-61027-score" class="comment-score"></div><div class="comment-text"><p>Thank You Uli!</p><p>This was indeed the solution.</p></div><div id="comment-61027-info" class="comment-info"><span class="comment-age">(25 Apr '17, 03:01)</span> KoenGSF</div></div></div><div id="comment-tools-61022" class="comment-tools"></div><div class="clear"></div><div id="comment-61022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

