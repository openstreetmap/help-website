+++
type = "question"
title = "SIP flow sequence wrongly sorted"
description = '''Hello, i have two SIP Flows. When i open the flow sequence, the Sequence is sorted by call ID, but should be sorted according to the time. It has worked before, and i don&#x27;t know what has changed. Thanks for your Help, Regards, Volker NOT-OK  OK '''
date = "2017-05-02T01:32:00Z"
lastmod = "2017-05-04T16:23:00Z"
weight = 61151
keywords = [ "sip", "flowgraph" ]
aliases = [ "/questions/61151" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SIP flow sequence wrongly sorted](/questions/61151/sip-flow-sequence-wrongly-sorted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61151-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i have two SIP Flows. When i open the flow sequence, the Sequence is sorted by call ID, but should be sorted according to the time. It has worked before, and i don't know what has changed.</p><p>Thanks for your Help,</p><p>Regards,</p><p>Volker</p><p>NOT-OK <img src="https://osqa-ask.wireshark.org/upfiles/wireshark-flow-wrong.PNG" alt="Wrong sorting" /> OK <img src="https://osqa-ask.wireshark.org/upfiles/wireshark-flow-All-OK.PNG" alt="All OK" /></p></div><div id="question-tags" class="tags-container tags">sip flowgraph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '17, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/03550c7393fbcc9ec331d59e552a325e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="volker&#39;s gravatar image" /><p>volker<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="volker has no accepted answers">0%</span></p></img></div></div><div id="comments-container-61151" class="comments-container"><span id="61159"></span><div id="comment-61159" class="comment"><div id="post-61159-score" class="comment-score"></div><div class="comment-text"><p><em>It has worked before, and i don't know what has changed.</em></p><p>Please elaborate. Which version of Wireshark does or does not work? What OS? Are you testing with the same capture data on both versions of Wireshark?</p><p>If you provide a capture file instead of screenshots, someone <em>might</em> be able to better help you. Post to any file sharing site, such as cloudshark, dropbox, pastebin, ...</p></div><div id="comment-61159-info" class="comment-info"><span class="comment-age">(02 May '17, 07:27)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-61151" class="comment-tools"></div><div class="clear"></div><div id="comment-61151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61246"></span>

<div id="answer-container-61246" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61246-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can you confirm that the frame numbers of these packets increment chronologically?</p><p>I ask this question because the flow chart does not sort the arrows by time, but rather by packet number. If you took two SIP Call ID's and merged them into one trace file by "appending" or "prepending" rather than sorting chronologically, then you will end up with the "Not OK" result that you showed in your screenshot.</p><p>I just tested this on 2.2.0 and confirmed this is the case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '17, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></img></div></div><div id="comments-container-61246" class="comments-container"><span id="61253"></span><div id="comment-61253" class="comment"><div id="post-61253-score" class="comment-score"></div><div class="comment-text"><p>Hi Quadratic,</p><p>you are right this is the Problem. Thanks a lot.</p><p>Regards, Volker</p></div><div id="comment-61253-info" class="comment-info"><span class="comment-age">(05 May '17, 10:56)</span> volker</div></div><span id="61254"></span><div id="comment-61254" class="comment"><div id="post-61254-score" class="comment-score"></div><div class="comment-text"><p>Hi Quadratic,</p><p>thanks again. Please add your comment as the Answer than we close this. I have use the tool "reordercap" under linux and i have what i need.</p><p>Regards, Volker</p></div><div id="comment-61254-info" class="comment-info"><span class="comment-age">(05 May '17, 12:21)</span> volker</div></div><span id="61262"></span><div id="comment-61262" class="comment"><div id="post-61262-score" class="comment-score"></div><div class="comment-text"><p>Great - It's an "answer" now. :)</p></div><div id="comment-61262-info" class="comment-info"><span class="comment-age">(05 May '17, 15:48)</span> Quadratic</div></div></div><div id="comment-tools-61246" class="comment-tools"></div><div class="clear"></div><div id="comment-61246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

