+++
type = "question"
title = "Auto-save by using consol"
description = '''Hi, I&#x27;m Seok-jae Yun from Korea. I have a question about using command line(in DOS) I want to sort data filtering with 40000 UDP port. So, I input &quot;wireshark.exe A201205130000.dat -R udp.port==40000 -w please.snoop&quot; but, the Wireshark only filter data, but didn&#x27;t save as &quot;please.snooop&quot; how can I fi...'''
date = "2012-10-25T05:54:00Z"
lastmod = "2012-10-25T05:59:00Z"
weight = 15247
keywords = [ "console", "line", "command" ]
aliases = [ "/questions/15247" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Auto-save by using consol](/questions/15247/auto-save-by-using-consol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15247-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm Seok-jae Yun from Korea.</p><p>I have a question about using command line(in DOS)</p><p>I want to sort data filtering with 40000 UDP port.</p><p>So, I input "wireshark.exe A201205130000.dat -R udp.port==40000 -w please.snoop"</p><p>but, the Wireshark only filter data, but didn't save as "please.snooop"</p><p>how can I filter data and save it?</p><p>Thank you. Seok-jae, Yun</p></div><div id="question-tags" class="tags-container tags">console line command</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '12, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/97271419c2b14e11dc090d63405636ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Seok-Jae&#39;s gravatar image" /><p>Seok-Jae<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Seok-Jae has no accepted answers">0%</span></p></div></div><div id="comments-container-15247" class="comments-container"></div><div id="comment-tools-15247" class="comment-tools"></div><div class="clear"></div><div id="comment-15247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15248"></span>

<div id="answer-container-15248" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15248-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you should use tshark.exe instead of wireshark.exe, and then you can use the parameter "-F &lt;fileformat&gt;" to make it saving the file in a format it supports. If you call "tshark.exe -F" it will give you a list of supported output file formats.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '12, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15248" class="comments-container"><span id="15279"></span><div id="comment-15279" class="comment"><div id="post-15279-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much The solution is "tshark.exe -r A201205130000.dat -R udp.port==40000 -F snoop -w please.snoop"</p><p>Thank you again</p></div><div id="comment-15279-info" class="comment-info"><span class="comment-age">(25 Oct '12, 06:43)</span> Seok-Jae</div></div></div><div id="comment-tools-15248" class="comment-tools"></div><div class="clear"></div><div id="comment-15248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

