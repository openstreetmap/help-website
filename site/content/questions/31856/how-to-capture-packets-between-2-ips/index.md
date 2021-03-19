+++
type = "question"
title = "How to capture packets between 2 IP&#x27;s"
description = '''I have two IP address. 10.xx.xx.xx and 10.yy.yy.yy. I am running GDB Server on one and GDB client on the other. I want to capture the first 50 packets or so between them when they initially hand shake. I am having Wireshark 1.8.3. I am running it on a Windows system. I was hoping it would be as simp...'''
date = "2014-04-15T15:54:00Z"
lastmod = "2014-04-15T16:52:00Z"
weight = 31856
keywords = [ "network" ]
aliases = [ "/questions/31856" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture packets between 2 IP's](/questions/31856/how-to-capture-packets-between-2-ips)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31856-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two IP address. 10.xx.xx.xx and 10.yy.yy.yy. I am running GDB Server on one and GDB client on the other. I want to capture the first 50 packets or so between them when they initially hand shake. I am having Wireshark 1.8.3. I am running it on a Windows system. I was hoping it would be as simple as</p><p>From IP: 10.xx,xx,xx</p><p>To IP: 10.yy.yy.yy.</p><p>Capture: 50 packets.</p><p>Hit the Start button</p><p>and when I start my GDB the packets should turn up. I played with it, Goggled it but no one gave a simple Click this Click this kind of suggestion. Could you please? Thanks in advance</p></div><div id="question-tags" class="tags-container tags">network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '14, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/5e0009f71c27b493081e07b2dc32a672?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="agvardha&#39;s gravatar image" /><p>agvardha<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="agvardha has no accepted answers">0%</span></p></div></div><div id="comments-container-31856" class="comments-container"></div><div id="comment-tools-31856" class="comment-tools"></div><div class="clear"></div><div id="comment-31856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31858"></span>

<div id="answer-container-31858" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31858-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do this:</p><ul><li>When you first start Wireshark, click on the button in the far upper-left that says "List the available capture interfaces" when you scroll over it.</li><li>In the new "Capture Interfaces" window that opens, select the interface you want to capture packets (with the check box on the left-hand side) and click"Options".</li><li>In the Capture Options window, on the lower-left corner there should be a "Stop Capture Automatically After..." seciton. Check the "packets" option and put in a value of 50</li><li>In the same Capture Options window, in the text box to the right of "Capture Filter", type the statement (without quotes) "ip host 10.xx.xx.xx and ip host 10.yy.yy.yy".</li><li>Hit the Start button :)</li></ul><p>One small thing to note - if the interface you're capturing is doing vlan tagging, replace the capture filter statement to "vlan and ip host 10.xx.xx.xx and ip host 10.yy.yy.yy" without quotes.</p><p>Edit:</p><p>An even simpler solution is to just use one command line statement:</p><p>C:\Program Files\Wireshark\dumpcap.exe -c 50 -i {interface name or number} -w {wherever you want to save the packet capture file}</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Apr '14, 17:02</p></div></div><div id="comments-container-31858" class="comments-container"><span id="31860"></span><div id="comment-31860" class="comment"><div id="post-31860-score" class="comment-score"></div><div class="comment-text"><p>Worked like a charm!!!!!!!! Thanks a lot Quadratic!!</p></div><div id="comment-31860-info" class="comment-info"><span class="comment-age">(15 Apr '14, 17:54)</span> agvardha</div></div><span id="31861"></span><div id="comment-31861" class="comment"><div id="post-31861-score" class="comment-score"></div><div class="comment-text"><p>&amp; the command line option is even more awesome. Thank you again very much.</p></div><div id="comment-31861-info" class="comment-info"><span class="comment-age">(15 Apr '14, 18:40)</span> agvardha</div></div></div><div id="comment-tools-31858" class="comment-tools"></div><div class="clear"></div><div id="comment-31858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

