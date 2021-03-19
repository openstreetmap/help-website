+++
type = "question"
title = "psprserver protocol with tcp 2354"
description = '''hi,  i sniff on my external router and found alot duplicate ack and Ignored Unknown Record in the secure socket layer. The Destination port is to : psprserver (2354). ? i have try google to find out that protocol but no info is found.'''
date = "2013-04-15T04:26:00Z"
lastmod = "2013-04-15T06:10:00Z"
weight = 20412
keywords = [ "protocol" ]
aliases = [ "/questions/20412" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [psprserver protocol with tcp 2354](/questions/20412/psprserver-protocol-with-tcp-2354)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20412-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, i sniff on my external router and found alot duplicate ack and Ignored Unknown Record in the secure socket layer. The Destination port is to : psprserver (2354). ? i have try google to find out that protocol but no info is found.</p></div><div id="question-tags" class="tags-container tags">protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '13, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/ba7415b503be15241d880cab78574700?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="splibytes&#39;s gravatar image" /><p>splibytes<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="splibytes has no accepted answers">0%</span></p></div></div><div id="comments-container-20412" class="comments-container"></div><div id="comment-tools-20412" class="comment-tools"></div><div class="clear"></div><div id="comment-20412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20417"></span>

<div id="answer-container-20417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20417-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is probably just the ephemeral port your client uses, and which is only used temporarily. Don't get distracted by the protocol name "psprserver" since it is simply not relevant for ephemeral ports.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '13, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20417" class="comments-container"><span id="20433"></span><div id="comment-20433" class="comment"><div id="post-20433-score" class="comment-score"></div><div class="comment-text"><p>you could try to identify the process on your PC that is doing the transmission and then google for that executable.</p><p>I usually do it like this: use a command line to call <em>netstat -ano</em>, which will list all TCP/UDP conversations your computer has at the moment. Find the one with the port you're investigating and write down the process ID (PID). Run taskmanager, select the "Processes" tab and add the PID column if it isn't already in there (Menu -&gt; Options -&gt; Select Columns -&gt; checkmark at "PID"). Then find the process with the PID you wrote down.</p><p>Note: this only works while the connection is still active; you can't do that when it is already finished. And, if you know how to start an elevated command prompt you can use <em>netstat -anb</em> instead, which will list the process name right away.</p></div><div id="comment-20433-info" class="comment-info"><span class="comment-age">(15 Apr '13, 10:57)</span> Jasper ♦♦</div></div><span id="20434"></span><div id="comment-20434" class="comment"><div id="post-20434-score" class="comment-score"></div><div class="comment-text"><p>Hi, after check the sniff data i found connect to akamai technologies(Destination: 23.59.165.186) and after Google around some report is a spyware and some say is normal. how can do i classify it as spyware or no base on the capturing? Also this capturing are found from the load balancer to the external router so it will need times to trace client which setting out the packet</p></div><div id="comment-20434-info" class="comment-info"><span class="comment-age">(15 Apr '13, 11:01)</span> splibytes</div></div><span id="20435"></span><div id="comment-20435" class="comment"><div id="post-20435-score" class="comment-score"></div><div class="comment-text"><p>on base of the capture you could try to identify what data was exchanged, but other than that it's pretty hard to do. In most cases I had, the communication to Akamai was harmless; mostly some update process, certificate revocation checks or other software update stuff.</p></div><div id="comment-20435-info" class="comment-info"><span class="comment-age">(15 Apr '13, 11:07)</span> Jasper ♦♦</div></div><span id="20436"></span><div id="comment-20436" class="comment"><div id="post-20436-score" class="comment-score"></div><div class="comment-text"><blockquote><p>. how can do i classify it as spyware or no base on the capturing?</p></blockquote><p>you can't, as the communication is encrypted and you don't know what kind of information is sent/received. The only chance is to identify the client (use the connection table of your loadbalancer) and then investigate the issue on the client machine itself.</p></div><div id="comment-20436-info" class="comment-info"><span class="comment-age">(15 Apr '13, 11:20)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20417" class="comment-tools"></div><div class="clear"></div><div id="comment-20417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

