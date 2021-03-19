+++
type = "question"
title = "Can&#x27;t get list of interfaces from remote machine"
description = '''I have Win8 (32 Bit) , I Installed WinPCap 4.1.2 I Started rpcapd in services (ERORR MASSAGE : Can&#x27;t get list of interfaces: Is the server properly installed on 192.168.1.7? connect() failed: A connection attempt failed because the connected party did not properly respond after a period of time, or ...'''
date = "2014-07-13T11:17:00Z"
lastmod = "2014-07-15T03:10:00Z"
weight = 34624
keywords = [ "interface", "remote-capture", "remote", "help", "capture" ]
aliases = [ "/questions/34624" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can't get list of interfaces from remote machine](/questions/34624/cant-get-list-of-interfaces-from-remote-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34624-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Win8 (32 Bit) , I Installed WinPCap 4.1.2 I Started rpcapd in services</p><p>(ERORR MASSAGE : Can't get list of interfaces: Is the server properly installed on 192.168.1.7? connect() failed: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host failed to respond. (col###))</p><pre><code>      ****OR****</code></pre><p>(ERORR MASSAGE #Some times# : Can't get list of interfaces: Is the server properly installed on 192.168.1.1? connect() failed: No connection could be made because the target machine actively refused it. (code 10061))</p><p><strong>I USED CAIN AND ABEL AND I CAPTURE EVERYTHING BUT I DON'T KNOW WHY DON'T WORK WITH WIRESHARK !</strong></p><p>What i do to use remote interface i really need this PLEASE HELP!!!!!</p></div><div id="question-tags" class="tags-container tags">interface remote-capture remote help capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '14, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/4da44d362012da112b7b72c2f5109a10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Al00X&#39;s gravatar image" /><p>Al00X<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Al00X has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '14, 13:14</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34624" class="comments-container"></div><div id="comment-tools-34624" class="comment-tools"></div><div class="clear"></div><div id="comment-34624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34650"></span>

<div id="answer-container-34650" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34650-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>No connection could be made because the target machine actively refused it. (<strong>code 10061</strong>))</p></blockquote><p>Error code <strong>10061</strong> means, there is either no service listening on the target port (TCP reset or ICMP port unreachable from the OS) or 'something' (firewall) blocks the connection request.</p><p>Please make sure, that the local firewall (Windows or third party) <strong>allows</strong> connection on the port that is being used by rpcapd and that rpcapd is started properly (check with netstat -na).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34650" class="comments-container"><span id="34777"></span><div id="comment-34777" class="comment"><div id="post-34777-score" class="comment-score"></div><div class="comment-text"><p>Than Q Very Much This Answer was really helpful (SOLVED)</p></div><div id="comment-34777-info" class="comment-info"><span class="comment-age">(19 Jul '14, 13:07)</span> Al00X</div></div></div><div id="comment-tools-34650" class="comment-tools"></div><div class="clear"></div><div id="comment-34650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34628"></span>

<div id="answer-container-34628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34628-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to the WinPCap site, you need version 4.1.3 for windows 8 compatibility. See <a href="http://www.winpcap.org/news.htm">http://www.winpcap.org/news.htm</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '14, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34628" class="comments-container"><span id="34778"></span><div id="comment-34778" class="comment"><div id="post-34778-score" class="comment-score"></div><div class="comment-text"><p>Oh yeah i see it thx</p></div><div id="comment-34778-info" class="comment-info"><span class="comment-age">(19 Jul '14, 13:09)</span> Al00X</div></div></div><div id="comment-tools-34628" class="comment-tools"></div><div class="clear"></div><div id="comment-34628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

