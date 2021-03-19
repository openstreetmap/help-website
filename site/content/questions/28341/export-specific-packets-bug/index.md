+++
type = "question"
title = "&quot;Export specific packets&quot; bug ?"
description = '''Hi, I can&#x27;t use export specific packets, whenever I try to save a filtred packet wireshark is closed and nothing is saved. I&#x27;ve tried with marked packet, range and only displayed but nothing work. The thing is that I&#x27;ve already used this tool and it worked. Since that time I Upgraded my version of W...'''
date = "2013-12-23T07:35:00Z"
lastmod = "2013-12-23T08:22:00Z"
weight = 28341
keywords = [ "specific", "packets", "export" ]
aliases = [ "/questions/28341" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# ["Export specific packets" bug ?](/questions/28341/export-specific-packets-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28341-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I can't use export specific packets, whenever I try to save a filtred packet wireshark is closed and nothing is saved. I've tried with marked packet, range and only displayed but nothing work.</p><p>The thing is that I've already used this tool and it worked. Since that time I Upgraded my version of Wireshark ( revision=52637 ).</p><p>Any idea on how to fix it ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">specific packets export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '13, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p>Afrim<br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-28341" class="comments-container"></div><div id="comment-tools-28341" class="comment-tools"></div><div class="clear"></div><div id="comment-28341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28343"></span>

<div id="answer-container-28343" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28343-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, what you describe looks like bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9287">9287</a> that got fixed in revision 52740. Upgrade your local copy to a newer release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '13, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-28343" class="comments-container"><span id="28354"></span><div id="comment-28354" class="comment"><div id="post-28354-score" class="comment-score"></div><div class="comment-text"><p>Fine, thank you :)</p></div><div id="comment-28354-info" class="comment-info"><span class="comment-age">(24 Dec '13, 00:20)</span> Afrim</div></div><span id="28361"></span><div id="comment-28361" class="comment"><div id="post-28361-score" class="comment-score"></div><div class="comment-text"><p>Ok now wireshark is not starting at all. No error message, nothing. Only load screen but no wireshark starting, when I look at the process I see wireshark but it end when load screen disappear.</p><p>This is a new problem should I start a new question ?</p><p>Edit : Ok the error message is "Unhandled exception at 0x0108add4 in wireshark.exe: 0xC0000005: Access violation reading location 0xbaadf00d." and it occur in <code>test_if_on()</code> function (airpcap_loader.c).</p></div><div id="comment-28361-info" class="comment-info"><span class="comment-age">(24 Dec '13, 02:28)</span> Afrim</div></div><span id="28364"></span><div id="comment-28364" class="comment"><div id="post-28364-score" class="comment-score"></div><div class="comment-text"><p><em>This is a new problem should I start a new question ?</em></p><p>Yes.</p></div><div id="comment-28364-info" class="comment-info"><span class="comment-age">(24 Dec '13, 05:35)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-28343" class="comment-tools"></div><div class="clear"></div><div id="comment-28343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

