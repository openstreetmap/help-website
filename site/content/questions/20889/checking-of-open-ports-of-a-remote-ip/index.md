+++
type = "question"
title = "Checking of open ports of a remote IP ."
description = '''For instance, my current ip address is 192.168.2.33 , but I want to check for open ports of the ip address 191.168.1.44 .  If I enter netstat -an on my machine, it checks for open ports on my machine and not the remote machine right ?  How do I use netstat to probe the remote ip at 191.168.1.44 inst...'''
date = "2013-05-01T22:26:00Z"
lastmod = "2013-05-02T04:09:00Z"
weight = 20889
keywords = [ "ip", "netstat", "remote" ]
aliases = [ "/questions/20889" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Checking of open ports of a remote IP .](/questions/20889/checking-of-open-ports-of-a-remote-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20889-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For instance, my current ip address is 192.168.2.33 , but I want to check for open ports of the ip address 191.168.1.44 .</p><p>If I enter <code>netstat -an</code> on my machine, it checks for open ports on my machine and not the remote machine right ?</p><p>How do I use netstat to probe the remote ip at 191.168.1.44 instead ?</p><p>Also, for example is I want to check if FTP is open. If telnet <code>191.168.1.44 20</code> is successful, does it mean that the FTP port is open ?</p><p>Thanks in advance for any replies :)</p></div><div id="question-tags" class="tags-container tags">ip netstat remote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '13, 22:26</strong></p><img src="https://secure.gravatar.com/avatar/9b52984d9786885d47fe81e43d8591ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinged&#39;s gravatar image" /><p>Dinged<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinged has no accepted answers">0%</span></p></div></div><div id="comments-container-20889" class="comments-container"></div><div id="comment-tools-20889" class="comment-tools"></div><div class="clear"></div><div id="comment-20889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20900"></span>

<div id="answer-container-20900" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20900-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How do I use netstat to probe the remote ip at 191.168.1.44 instead ?</p></blockquote><p>You can't as netstat will only show LISTENing connections on the local machine and ESTABLISHed connections to a remote system, <strong>if</strong> there is an open session.</p><blockquote><p>If telnet 191.168.1.44 20 is successful, does it mean that the FTP port is open ?</p></blockquote><p>Please connect to port 21, as that's the FTP control connection. If you see the banner message of the FTP server, it means that there is a FTP server running. If you don't get any response, it means there is either no service running (look for TCP RESETs in Wireshark) or there is a firewall that blocks the connection.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '13, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20900" class="comments-container"><span id="20907"></span><div id="comment-20907" class="comment"><div id="post-20907-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply, it clarified my doubts. This may be off-topic, but is there any common software being used to probe for remote ip ? The software on my mind is Nmap.</p></div><div id="comment-20907-info" class="comment-info"><span class="comment-age">(02 May '13, 06:08)</span> Dinged</div></div><span id="20908"></span><div id="comment-20908" class="comment"><div id="post-20908-score" class="comment-score">1</div><div class="comment-text"><p>namp is the 'standard' tool for port scanning. There is also a free Windows tool, called 'SoftPerfect Network Scanner' and numerous other tools. Just google for: port scanner</p></div><div id="comment-20908-info" class="comment-info"><span class="comment-age">(02 May '13, 06:43)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20900" class="comment-tools"></div><div class="clear"></div><div id="comment-20900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20891"></span>

<div id="answer-container-20891" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20891-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, you can always use nmap or any other port scanning web site to try check the remote port? but if i remember correct, you cant use telnet to check udp port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '13, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/ba7415b503be15241d880cab78574700?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="splibytes&#39;s gravatar image" /><p>splibytes<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="splibytes has no accepted answers">0%</span></p></div></div><div id="comments-container-20891" class="comments-container"></div><div id="comment-tools-20891" class="comment-tools"></div><div class="clear"></div><div id="comment-20891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

