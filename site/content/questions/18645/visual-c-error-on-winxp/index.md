+++
type = "question"
title = "Visual C++ error on WinXP"
description = '''Dear Sir, My environemnt is Windows XP with SP3 and using WireShark version 1.8.5 &amp;amp; 1.6.13. All of versions will occur same question &quot;Visual C++ error&quot;. I don&#x27;t know this is a limitation of Wireshark of shareware or any request I need to prepare? Regards, Kuoyang'''
date = "2013-02-14T22:18:00Z"
lastmod = "2013-02-15T22:42:00Z"
weight = 18645
keywords = [ "question" ]
aliases = [ "/questions/18645" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Visual C++ error on WinXP](/questions/18645/visual-c-error-on-winxp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18645-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Sir,</p><p>My environemnt is Windows XP with SP3 and using WireShark version 1.8.5 &amp; 1.6.13. All of versions will occur same question "Visual C++ error".</p><p>I don't know this is a limitation of Wireshark of shareware or any request I need to prepare?</p><p>Regards, Kuoyang</p></div><div id="question-tags" class="tags-container tags">question</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '13, 22:18</strong></p><img src="https://secure.gravatar.com/avatar/d80d0e1198bd3e605a58db57148b28e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kuoyang&#39;s gravatar image" /><p>Kuoyang<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kuoyang has no accepted answers">0%</span></p></div></div><div id="comments-container-18645" class="comments-container"><span id="18646"></span><div id="comment-18646" class="comment"><div id="post-18646-score" class="comment-score"></div><div class="comment-text"><p>You have to explain the problem better, when do you get the error? when starting wireshark? or when reading in a capture file? or?</p></div><div id="comment-18646-info" class="comment-info"><span class="comment-age">(14 Feb '13, 23:01)</span> Anders ♦</div></div><span id="18664"></span><div id="comment-18664" class="comment"><div id="post-18664-score" class="comment-score"></div><div class="comment-text"><p>Dear Anders,</p><p>Thanks for your reply. 1. I have setup the WireShark save the trace file when every 10 min or the trace file size is over 5MB automatically. 2. I captured the network traffic between Server with Printer. 3. If the Server have not submit job to Printer, the network traffice of Server with Printer is SNMP only and WireShark is workable very long time and will not crash or occur any problem. The trace file will generate very well. 4. But when Server submit a job to Printer, the network traffic became busy, the Wireshark would save trace file per 10 min and 5MB, but will occur Visual C++ runtime error. 5. I have changed another NB and did same test, I got same result. So I did not think the problem on NB or memory of NB.</p><p>Regards, Kuoyang Hu</p></div><div id="comment-18664-info" class="comment-info"><span class="comment-age">(15 Feb '13, 21:30)</span> Kuoyang</div></div></div><div id="comment-tools-18645" class="comment-tools"></div><div class="clear"></div><div id="comment-18645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18665"></span>

<div id="answer-container-18665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18665-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>From your additional comments this seems to be an out of memory error. See the <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">Out of Memory</a> wiki page for more info.</p><p>The issue occurs because Wireshark (and TShark) accumulate info such as conversations and do not release this memory. For long-term captures you should use <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> which is installed alongside Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '13, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18665" class="comments-container"><span id="18669"></span><div id="comment-18669" class="comment"><div id="post-18669-score" class="comment-score"></div><div class="comment-text"><p>Dear Grahamb,</p><p>I think it is a key issue. Because of I always capture the trace long time. I will do this on Monday &amp; thanks again.</p></div><div id="comment-18669-info" class="comment-info"><span class="comment-age">(16 Feb '13, 02:56)</span> Kuoyang</div></div><span id="18724"></span><div id="comment-18724" class="comment"><div id="post-18724-score" class="comment-score"></div><div class="comment-text"><p>Thank Grahamb provide me this useful information and I could capture a long-term network traffic (from 1700 ~ 0315). I don't know why the comamand would terminate at AM 0315. I will try again. Thanks again. Kuoyang</p></div><div id="comment-18724-info" class="comment-info"><span class="comment-age">(18 Feb '13, 16:53)</span> Kuoyang</div></div></div><div id="comment-tools-18665" class="comment-tools"></div><div class="clear"></div><div id="comment-18665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

