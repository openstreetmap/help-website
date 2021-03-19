+++
type = "question"
title = "Which IP sent the biggest amount of data?"
description = '''i have a pcap file to analyse and i want to find out which ip sent the biggest amount of data .. what is the steps?'''
date = "2017-03-27T14:34:00Z"
lastmod = "2017-03-27T14:35:00Z"
weight = 60370
keywords = [ "ip", "data" ]
aliases = [ "/questions/60370" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Which IP sent the biggest amount of data?](/questions/60370/which-ip-sent-the-biggest-amount-of-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60370-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have a pcap file to analyse and i want to find out which ip sent the biggest amount of data .. what is the steps?</p></div><div id="question-tags" class="tags-container tags">ip data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '17, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/f161c545568d63d9b939596972afde1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seeker&#39;s gravatar image" /><p>seeker<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seeker has no accepted answers">0%</span></p></div></div><div id="comments-container-60370" class="comments-container"></div><div id="comment-tools-60370" class="comment-tools"></div><div class="clear"></div><div id="comment-60370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60371"></span>

<div id="answer-container-60371" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60371-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use the Statistics menu to look at the Endpoint statistic, and select the IP tab.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '17, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60371" class="comments-container"><span id="60372"></span><div id="comment-60372" class="comment"><div id="post-60372-score" class="comment-score"></div><div class="comment-text"><p>i found tabs named (Bytes A-&gt; B) and (Bytes B-&gt;A) each tab carries a different size number, what is the difference between them?</p></div><div id="comment-60372-info" class="comment-info"><span class="comment-age">(27 Mar '17, 14:40)</span> seeker</div></div><span id="60373"></span><div id="comment-60373" class="comment"><div id="post-60373-score" class="comment-score"></div><div class="comment-text"><p>I think you went to "Conversations" instead of "Endpoints", which lists two IPs talking to each other (A and B). In the endpoint statistic, there is no A and B :-)</p></div><div id="comment-60373-info" class="comment-info"><span class="comment-age">(27 Mar '17, 14:42)</span> Jasper ♦♦</div></div><span id="60375"></span><div id="comment-60375" class="comment"><div id="post-60375-score" class="comment-score"></div><div class="comment-text"><p>in "Endpoints" there is two IPs in two separated lines, the first line the first IP sent 100 from A to B and sent 50 from B to A, the second line the second IP sent 50 from A to B and sent 100 from B to A (the reversed statics from line 1), does that mean the first IP sent the biggest amount "100"?</p></div><div id="comment-60375-info" class="comment-info"><span class="comment-age">(27 Mar '17, 14:54)</span> seeker</div></div><span id="60376"></span><div id="comment-60376" class="comment"><div id="post-60376-score" class="comment-score"></div><div class="comment-text"><p>Yes, you're right, I didn't notice, those column labels are misleading in version 2.x (I think they're plain wrong, tbh) - they should read "Tx Packets", "Tx Bytes", "RX Packets", "Rx Bytes", with "Tx" = "Transmitted" and "Rx" = "Received", as they were in version 1.x</p></div><div id="comment-60376-info" class="comment-info"><span class="comment-age">(27 Mar '17, 14:59)</span> Jasper ♦♦</div></div><span id="60377"></span><div id="comment-60377" class="comment"><div id="post-60377-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot, i should they are plain wrong too with Tx and Rx it became easier :-)</p></div><div id="comment-60377-info" class="comment-info"><span class="comment-age">(27 Mar '17, 15:04)</span> seeker</div></div><span id="60378"></span><div id="comment-60378" class="comment not_top_scorer"><div id="post-60378-score" class="comment-score"></div><div class="comment-text"><p>I added a bug report to the bugtracker here: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13526">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13526</a></p></div><div id="comment-60378-info" class="comment-info"><span class="comment-age">(27 Mar '17, 15:07)</span> Jasper ♦♦</div></div><span id="60389"></span><div id="comment-60389" class="comment not_top_scorer"><div id="post-60389-score" class="comment-score"></div><div class="comment-text"><p>And... it's fixed, in the lastest dev builds:</p><p><a href="https://www.wireshark.org/download/automated/">https://www.wireshark.org/download/automated/</a></p></div><div id="comment-60389-info" class="comment-info"><span class="comment-age">(28 Mar '17, 12:35)</span> Jasper ♦♦</div></div></div><div id="comment-tools-60371" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-60371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

