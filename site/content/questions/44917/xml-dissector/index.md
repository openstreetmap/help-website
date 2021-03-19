+++
type = "question"
title = "xml dissector"
description = '''hi all, suppose i have a xml file of a packet and DTD for this xml file. now there is an xml dissector in wireshark (epan/packet-xml.c), Can anyone please tell me that how to use all these to dissect the xml file of a packet. Or how to use the xml dissector???? thanks'''
date = "2015-08-07T02:45:00Z"
lastmod = "2015-08-07T05:41:00Z"
weight = 44917
keywords = [ "xml", "dissector" ]
aliases = [ "/questions/44917" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [xml dissector](/questions/44917/xml-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44917-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all, suppose i have a xml file of a packet and DTD for this xml file. now there is an xml dissector in wireshark (epan/packet-xml.c), Can anyone please tell me that how to use all these to dissect the xml file of a packet. Or how to use the xml dissector????</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">xml dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '15, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/4f516d44975f0778735c91ae9f71624b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zombimind&#39;s gravatar image" /><p>zombimind<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zombimind has no accepted answers">0%</span></p></div></div><div id="comments-container-44917" class="comments-container"></div><div id="comment-tools-44917" class="comment-tools"></div><div class="clear"></div><div id="comment-44917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44920"></span>

<div id="answer-container-44920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44920-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The xml dissector is used to dissect/pretty print xml inside packets, it can't be used to read xml files. If you want to pars an xml based packet file you would have to write wiretap code to do that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '15, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-44920" class="comments-container"><span id="44921"></span><div id="comment-44921" class="comment"><div id="post-44921-score" class="comment-score"></div><div class="comment-text"><p>thanks for reply anders, I will follow your suggestion..</p></div><div id="comment-44921-info" class="comment-info"><span class="comment-age">(07 Aug '15, 06:16)</span> zombimind</div></div><span id="44922"></span><div id="comment-44922" class="comment"><div id="post-44922-score" class="comment-score"></div><div class="comment-text"><p>but i can see that there is an xml dissector(epan/dissectors/packet-xml.c) already in wireshark, can you please tell me how to use it,</p></div><div id="comment-44922-info" class="comment-info"><span class="comment-age">(07 Aug '15, 06:20)</span> zombimind</div></div><span id="44923"></span><div id="comment-44923" class="comment"><div id="post-44923-score" class="comment-score"></div><div class="comment-text"><p>As per my previous answer - you can't.</p></div><div id="comment-44923-info" class="comment-info"><span class="comment-age">(07 Aug '15, 07:06)</span> Anders ♦</div></div><span id="44940"></span><div id="comment-44940" class="comment"><div id="post-44940-score" class="comment-score"></div><div class="comment-text"><p>alright anders, thanks...</p></div><div id="comment-44940-info" class="comment-info"><span class="comment-age">(09 Aug '15, 21:46)</span> zombimind</div></div></div><div id="comment-tools-44920" class="comment-tools"></div><div class="clear"></div><div id="comment-44920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

