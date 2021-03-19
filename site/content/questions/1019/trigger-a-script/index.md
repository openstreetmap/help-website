+++
type = "question"
title = "trigger a script"
description = '''Dear all, Is it possible to use a packet filter to trigger a shell script? For example: I have a continuous incoming UDP stream with &quot;0&quot; as data. When it becomes &quot;1&quot; I want to run a shell command. I want to run this as a service. Best regards, Koen'''
date = "2010-11-19T02:38:00Z"
lastmod = "2010-11-20T03:18:00Z"
weight = 1019
keywords = [ "filter", "shell", "trigger", "script" ]
aliases = [ "/questions/1019" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [trigger a script](/questions/1019/trigger-a-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1019-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all,</p><p>Is it possible to use a packet filter to trigger a shell script?</p><p>For example: I have a continuous incoming UDP stream with "0" as data. When it becomes "1" I want to run a shell command.</p><p>I want to run this as a service.</p><p>Best regards, Koen</p></div><div id="question-tags" class="tags-container tags">filter shell trigger script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '10, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/6ab7ae3ff82d3131e1ce8f86dc079c45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoenJ&#39;s gravatar image" /><p>KoenJ<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoenJ has no accepted answers">0%</span></p></div></div><div id="comments-container-1019" class="comments-container"></div><div id="comment-tools-1019" class="comment-tools"></div><div class="clear"></div><div id="comment-1019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1032"></span>

<div id="answer-container-1032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1032-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark and tshark don't do well as a service when you want to monitor traffic. This is because their memory footprint will increase over time to keep state information that is needed to dissect all the packets.</p><p>You might want to write a script that uses libpcap/winpcap, it's not really that difficult to parse UDP that way.</p><p>You could also use tcpdump, although I'm not sure if it won't slowly eat up memory too. Here is a startingpoint:</p><pre><code>tcpdump -nli en1 &quot;udp[10]=1 and host 192.168.1.20&quot;</code></pre><p>This will only output packets where the third byte in the UDP payload (the 8 byte UDP header starts at 0, so 10 is the third payload byte) equals to 1 for a particular host (192.168.1.20). You can then pipe the output to a script that will fire off something else when it does see a line of output on it's stdin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '10, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Nov '10, 03:18</p></div></div><div id="comments-container-1032" class="comments-container"><span id="6658"></span><div id="comment-6658" class="comment"><div id="post-6658-score" class="comment-score"></div><div class="comment-text"><p>may i know what exactly the service mean here?</p></div><div id="comment-6658-info" class="comment-info"><span class="comment-age">(01 Oct '11, 00:21)</span> Terrestrial ...</div></div><span id="6662"></span><div id="comment-6662" class="comment"><div id="post-6662-score" class="comment-score"></div><div class="comment-text"><p>In this context "service" means a process that starts automatically and runs forever. "Service" is a term from the windows world where in the *nix world it would be called a daemon.</p></div><div id="comment-6662-info" class="comment-info"><span class="comment-age">(01 Oct '11, 01:57)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1032" class="comment-tools"></div><div class="clear"></div><div id="comment-1032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

