+++
type = "question"
title = "tshark: how to decode and display individual packets"
description = '''Hi All, I want to use tshark to display the raw packets.  By using the command and options: tshark -x -r file.pcap the tshark displays all the packets. I want to view the packets one by one, but can not find the option to display say the 1st packet. Thanks in advance. /Dan'''
date = "2010-11-09T03:05:00Z"
lastmod = "2010-11-09T03:11:00Z"
weight = 869
keywords = [ "tshark" ]
aliases = [ "/questions/869" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: how to decode and display individual packets](/questions/869/tshark-how-to-decode-and-display-individual-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-869-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I want to use tshark to display the raw packets. By using the command and options: tshark -x -r file.pcap the tshark displays all the packets. I want to view the packets one by one, but can not find the option to display say the 1st packet.</p><p>Thanks in advance.</p><p>/Dan</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '10, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/25968304357a2cbc5832a6b03745a548?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danyigez&#39;s gravatar image" /><p>danyigez<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danyigez has no accepted answers">0%</span></p></div></div><div id="comments-container-869" class="comments-container"></div><div id="comment-tools-869" class="comment-tools"></div><div class="clear"></div><div id="comment-869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="871"></span>

<div id="answer-container-871" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-871-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use a display filter to only select a particular frame.number:</p><pre><code>tshark -r &lt;file&gt; -x -R frame.number==1</code></pre><p>If you want to display more than one packet, you can combine it with the -c option:</p><pre><code>tshark -r &lt;file&gt; -x -c 10 -R frame.number&gt;=100</code></pre><p>This would show you 10 packets starting at packet 100.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '10, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-871" class="comments-container"></div><div id="comment-tools-871" class="comment-tools"></div><div class="clear"></div><div id="comment-871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

