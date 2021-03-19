+++
type = "question"
title = "decode rtcp"
description = '''hi guys,i am trying to decode rtcp app data using my own dissector can anyone suggest how to proceed?'''
date = "2017-02-18T01:31:00Z"
lastmod = "2017-02-18T06:14:00Z"
weight = 59522
keywords = [ "rtcp" ]
aliases = [ "/questions/59522" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [decode rtcp](/questions/59522/decode-rtcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59522-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,i am trying to decode rtcp app data using my own dissector can anyone suggest how to proceed?</p></div><div id="question-tags" class="tags-container tags">rtcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '17, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/4175e12d54c0b11b1d8a5fb592555a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lucky15&#39;s gravatar image" /><p>lucky15<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lucky15 has no accepted answers">0%</span></p></div></div><div id="comments-container-59522" class="comments-container"></div><div id="comment-tools-59522" class="comment-tools"></div><div class="clear"></div><div id="comment-59522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59529"></span>

<div id="answer-container-59529" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59529-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's this dissector table called <code>rtcp.app.name</code> which you can register to with your application name. Then your registered handler will be called with a TVB containing the APP option data. Look at the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-rtcp.c;hb=HEAD#l1964">packet-rtcp.c</a> dissector code for details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '17, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59529" class="comments-container"><span id="59534"></span><div id="comment-59534" class="comment"><div id="post-59534-score" class="comment-score"></div><div class="comment-text"><p>thank you for answering..but i have the same app name for all the subtypes.,can i decode based on subtype also?</p></div><div id="comment-59534-info" class="comment-info"><span class="comment-age">(18 Feb '17, 10:33)</span> lucky15</div></div><span id="59538"></span><div id="comment-59538" class="comment"><div id="post-59538-score" class="comment-score"></div><div class="comment-text"><p>In fact you're getting the whole APP packet, not just the application data contained within. So the subtype is in there as well.</p></div><div id="comment-59538-info" class="comment-info"><span class="comment-age">(19 Feb '17, 02:11)</span> Jaap ♦</div></div></div><div id="comment-tools-59529" class="comment-tools"></div><div class="clear"></div><div id="comment-59529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

