+++
type = "question"
title = "how to export marked packets to pcap"
description = '''If I have a large pcap file that was created with tcpdump and then I open it in Wireshark and using filters I find the frames I am interested in, then I want to export these frames to a new pcap file, but the Export File function doesn&#x27;t allow to save as type &#x27;pcap&#x27;. Is this possible somehow?'''
date = "2012-07-30T01:00:00Z"
lastmod = "2012-07-30T01:54:00Z"
weight = 13108
keywords = [ "export" ]
aliases = [ "/questions/13108" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how to export marked packets to pcap](/questions/13108/how-to-export-marked-packets-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13108-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I have a large pcap file that was created with tcpdump and then I open it in Wireshark and using filters I find the frames I am interested in, then I want to export these frames to a new pcap file, but the Export File function doesn't allow to save as type 'pcap'. Is this possible somehow?</p></div><div id="question-tags" class="tags-container tags">export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '12, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/0094436e83e53143228ba8b4314abc78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steinboy&#39;s gravatar image" /><p>steinboy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steinboy has no accepted answers">0%</span></p></div></div><div id="comments-container-13108" class="comments-container"></div><div id="comment-tools-13108" class="comment-tools"></div><div class="clear"></div><div id="comment-13108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13109"></span>

<div id="answer-container-13109" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13109-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Which version of Wireshark is this?</p><p>In Wireshark 1.8.0 and later, the function you want is "Export Specified Packets" in the "File" menu. Select "Marked packets only" (if you mean <em>marked</em> packets rather than, say, <em>displayed</em> packets).</p><p>In earlier versions of Wireshark, that is somewhat confusingly done in "Save As" in the "File" menu. Again, select "Marked packets only".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '12, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-13109" class="comments-container"><span id="13110"></span><div id="comment-13110" class="comment"><div id="post-13110-score" class="comment-score"></div><div class="comment-text"><p>Hi, thank you for your quick response. It is version 1.2.2., and yes, I assumed it to be in the Export menu, didn't think of looking in Save As, and my usual google search didn't bring any clues, so thankyou very much for the solution.</p></div><div id="comment-13110-info" class="comment-info"><span class="comment-age">(30 Jul '12, 03:42)</span> steinboy</div></div></div><div id="comment-tools-13109" class="comment-tools"></div><div class="clear"></div><div id="comment-13109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

