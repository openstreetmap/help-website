+++
type = "question"
title = "How to capture PPP on wireshark"
description = '''Hi everyone, I am a new user to wireshark. I am having some problem getting wireshark to capture PPP can anyone tell me what I am doing wrong and what do I actually have to do to get the PPP because I have been searching google and youtube for this information and I still haven&#x27;t found anything that...'''
date = "2017-09-23T01:01:00Z"
lastmod = "2017-09-23T07:50:00Z"
weight = 63627
keywords = [ "ppp" ]
aliases = [ "/questions/63627" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture PPP on wireshark](/questions/63627/how-to-capture-ppp-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63627-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone, I am a new user to wireshark. I am having some problem getting wireshark to capture PPP can anyone tell me what I am doing wrong and what do I actually have to do to get the PPP because I have been searching google and youtube for this information and I still haven't found anything that shows me how to get PPP yet.</p></div><div id="question-tags" class="tags-container tags">ppp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '17, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/bd3c0bb25ee7905bb1ce0f6041d5ed98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tracer&#39;s gravatar image" /><p>Tracer<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tracer has no accepted answers">0%</span></p></div></div><div id="comments-container-63627" class="comments-container"><span id="63628"></span><div id="comment-63628" class="comment"><div id="post-63628-score" class="comment-score"></div><div class="comment-text"><p>What is the OS you're capturing on?</p></div><div id="comment-63628-info" class="comment-info"><span class="comment-age">(23 Sep '17, 03:02)</span> grahamb ♦</div></div><span id="63630"></span><div id="comment-63630" class="comment"><div id="post-63630-score" class="comment-score"></div><div class="comment-text"><p>I'm using windows</p></div><div id="comment-63630-info" class="comment-info"><span class="comment-age">(23 Sep '17, 05:46)</span> Tracer</div></div></div><div id="comment-tools-63627" class="comment-tools"></div><div class="clear"></div><div id="comment-63627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63632"></span>

<div id="answer-container-63632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63632-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>WinPcap, the standard capture driver used by Wireshark on Windows doesn't handle PPP.</p><p>Previously, I have used Microsoft's NetMon to make PPP captures and then export the capture to pcap and open it in Wireshark. I haven't done that for a while so I don't know if MessageAnalyzer (the replacement for NetMon) can capture PPP, but I think it should be able to do so.</p><p>Another option is to replace WinPcap with <a href="https://nmap.org/npcap/">Npcap</a>, which is a modern replacement for WinPcap, but again I haven't tried that for PPP captures. If you do try Npcap, I suggest manually uninstalling WinPcap first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '17, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63632" class="comments-container"></div><div id="comment-tools-63632" class="comment-tools"></div><div class="clear"></div><div id="comment-63632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

