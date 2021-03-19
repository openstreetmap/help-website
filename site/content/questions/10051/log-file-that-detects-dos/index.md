+++
type = "question"
title = "Log File that detects DoS"
description = '''I would like to get a log file that contains Denial of Service (Dos) attack events from WireShark. May i know how i do i get it using Wireshark?'''
date = "2012-04-11T01:42:00Z"
lastmod = "2012-04-11T17:20:00Z"
weight = 10051
keywords = [ "dos", "log" ]
aliases = [ "/questions/10051" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Log File that detects DoS](/questions/10051/log-file-that-detects-dos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10051-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to get a log file that contains Denial of Service (Dos) attack events from WireShark. May i know how i do i get it using Wireshark?</p></div><div id="question-tags" class="tags-container tags">dos log</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '12, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div></div><div id="comments-container-10051" class="comments-container"><span id="10052"></span><div id="comment-10052" class="comment"><div id="post-10052-score" class="comment-score"></div><div class="comment-text"><p>You need the tshark option <code>--DOS</code>. Unfortunately that hasn't been implemented yet.</p><p>If you explain a bit more about your requirements, e.g. what you think a DOS attack event looks like, then we can tell you how to use Wireshark to show the information.</p></div><div id="comment-10052-info" class="comment-info"><span class="comment-age">(11 Apr '12, 02:50)</span> grahamb ♦</div></div><span id="10053"></span><div id="comment-10053" class="comment"><div id="post-10053-score" class="comment-score"></div><div class="comment-text"><p>I just want a sample log from wireshark that contain DoS events and use it for log analysis on "Splunk" software. and i would like to know how the DoS attack event message will look like in the log file i get from wireshark.</p></div><div id="comment-10053-info" class="comment-info"><span class="comment-age">(11 Apr '12, 02:55)</span> misteryuku</div></div><span id="10054"></span><div id="comment-10054" class="comment"><div id="post-10054-score" class="comment-score"></div><div class="comment-text"><p>As Wikipedia shows <a href="http://en.wikipedia.org/wiki/Denial_of_Service">HERE</a> a DOS attack may take many forms. Wireshark has no simple button to produce a DOS list, it instead displays all captured packets, filtered and coloured as required by the user.</p><p>So, if you can explain the sort of DOS you are looking for we may be able to supply a filter and/or colouring rules to help.</p></div><div id="comment-10054-info" class="comment-info"><span class="comment-age">(11 Apr '12, 03:41)</span> grahamb ♦</div></div><span id="10069"></span><div id="comment-10069" class="comment"><div id="post-10069-score" class="comment-score"></div><div class="comment-text"><p>I read that there are many forms of DoS. I am looking for those DoS listed in the Wikipedia DoS page. I would like to know a way to get every single DoS attack event in a log file that i can obtain from wireshark.</p></div><div id="comment-10069-info" class="comment-info"><span class="comment-age">(11 Apr '12, 17:08)</span> misteryuku</div></div></div><div id="comment-tools-10051" class="comment-tools"></div><div class="clear"></div><div id="comment-10051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10070"></span>

<div id="answer-container-10070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10070-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not the best tool for this purpose. First of all, it's memory footprint will increase over time, so for long term monitoring, you need something else. Second of all, Wireshark will fully dissect each packet, which is overkill for DoS detection. You need a fast pattern matching enginge for that.</p><p>Have a look at <a href="http://www.snort.org/">Snort</a> instead...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '12, 17:20</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10070" class="comments-container"><span id="10072"></span><div id="comment-10072" class="comment"><div id="post-10072-score" class="comment-score"></div><div class="comment-text"><p>I would like to ask you, Snort requires Winpcap when installed on Windows?</p></div><div id="comment-10072-info" class="comment-info"><span class="comment-age">(11 Apr '12, 18:57)</span> misteryuku</div></div><span id="10074"></span><div id="comment-10074" class="comment"><div id="post-10074-score" class="comment-score"></div><div class="comment-text"><p>Snort uses pcap for capturing traffic, which means it requires WinPcap when installed on WIndows.</p></div><div id="comment-10074-info" class="comment-info"><span class="comment-age">(11 Apr '12, 19:13)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-10070" class="comment-tools"></div><div class="clear"></div><div id="comment-10070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

