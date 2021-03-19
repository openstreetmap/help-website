+++
type = "question"
title = "newbie question, need to run as a commald line"
description = '''Hi need to run Wireshark from a command line as follows if possible capture all packets with following options  1. IP name resolution  2. file capture directory c:capture  3. file size 100mb  4. 5 rolling files so when 5th one full goes back to number 1 thanks Steve'''
date = "2010-12-06T04:39:00Z"
lastmod = "2010-12-10T04:12:00Z"
weight = 1254
keywords = [ "line", "command" ]
aliases = [ "/questions/1254" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [newbie question, need to run as a commald line](/questions/1254/newbie-question-need-to-run-as-a-commald-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1254-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>need to run Wireshark from a command line as follows if possible capture all packets with following options 1. IP name resolution 2. file capture directory c:capture 3. file size 100mb 4. 5 rolling files so when 5th one full goes back to number 1</p><p>thanks Steve</p></div><div id="question-tags" class="tags-container tags">line command</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '10, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/0d66264723d1bb11ef950dd1fc0935b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve_1&#39;s gravatar image" /><p>steve_1<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve_1 has no accepted answers">0%</span></p></div></div><div id="comments-container-1254" class="comments-container"></div><div id="comment-tools-1254" class="comment-tools"></div><div class="clear"></div><div id="comment-1254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1257"></span>

<div id="answer-container-1257" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1257-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Steve</p><p>tshark is installed as part of wirehark and should perform what is needed.</p><p>tshark -h prints the help</p><p>I think this is pretty close to what you need.. (you need to check the available interfaces via the tshark -D command)</p><p>tshark -f "port 53" -i 2 -b filesize:100 -b files:5 -w "c:capturedns-capture"</p><p>Eric</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '10, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/d5aa09edfeeb0600f74a72e63806f227?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erics&#39;s gravatar image" /><p>erics<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erics has no accepted answers">0%</span></p></div></div><div id="comments-container-1257" class="comments-container"></div><div id="comment-tools-1257" class="comment-tools"></div><div class="clear"></div><div id="comment-1257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1308"></span>

<div id="answer-container-1308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1308-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to run Wireshark with certain options see <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCustCommandLine.html">this part of the Users's Guide</a>. If you just want to capture (not dissect straight away) then go for <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolsdumpcap.html">dumpcap</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '10, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1308" class="comments-container"></div><div id="comment-tools-1308" class="comment-tools"></div><div class="clear"></div><div id="comment-1308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

