+++
type = "question"
title = "30 seconds delays in server response"
description = '''After examining the Wireshark flow graph. The clients connects to the the server then after the PSH, ACK it takes the server 30 seconds to respond. This happens 6 times in the total conversation, making data transfer take forever. Win7 PC connecting to a VM CentOS 5.7. VMWare are tools installed. Do...'''
date = "2012-02-14T11:26:00Z"
lastmod = "2012-02-15T03:14:00Z"
weight = 9000
keywords = [ "tcppackets", "delayed" ]
aliases = [ "/questions/9000" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [30 seconds delays in server response](/questions/9000/30-seconds-delays-in-server-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9000-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After examining the Wireshark flow graph. The clients connects to the the server then after the PSH, ACK it takes the server 30 seconds to respond. This happens 6 times in the total conversation, making data transfer take forever. Win7 PC connecting to a VM CentOS 5.7. VMWare are tools installed. Does any one have any ideas what might cause this 30 second delay in server response? Any help appreciated.</p><pre><code>4   0.001504000 192.168.1.114   192.168.10.89   TCP 51416 &gt; netview-aix-6 [PSH, ACK] Seq=1 Ack=1 Win=65536 Len=344
5   0.001825000 192.168.10.89   192.168.1.114   TCP netview-aix-6 &gt; 51416 [ACK] Seq=1 Ack=345 Win=6912 Len=0
6   30.017798000 192.168.10.89  192.168.1.114   TCP netview-aix-6 &gt; 51416 [PSH, ACK] Seq=1 Ack=345 Win=6912 Len=722
7   30.019302000 192.168.1.114  192.168.10.89   TCP 51416 &gt; netview-aix-6 [PSH, ACK] Seq=345 Ack=723 Win=64814 Len=242</code></pre></div><div id="question-tags" class="tags-container tags">tcppackets delayed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '12, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/98d7a6e2fb22dc6dc4c76b2a93e48fc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bryanice&#39;s gravatar image" /><p>bryanice<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bryanice has no accepted answers">0%</span></p></div></div><div id="comments-container-9000" class="comments-container"></div><div id="comment-tools-9000" class="comment-tools"></div><div class="clear"></div><div id="comment-9000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9014"></span>

<div id="answer-container-9014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9014-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you are not mentioning what kind of protocol is used, it's hard to tell from just the packet capture.</p><p>What you do know is that it is a delay in the server (assuming the trace was made on the server side to exclude any intermediate devices). So the 30 sec delay is something on the server side. If it is (close to) 30 sec all the time, then it does not sound like processing time, but more like a timeout being hit.</p><p>You would need to know more about the application on the server to determine the exact cause.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '12, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Feb '12, 03:19</p></div></div><div id="comments-container-9014" class="comments-container"></div><div id="comment-tools-9014" class="comment-tools"></div><div class="clear"></div><div id="comment-9014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9015"></span>

<div id="answer-container-9015" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9015-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Lets take a look:</p><p>In packet 4, 334 bytes are sent from IP 192.168.1.114 to 192.168.10.89 (the latter of which I guess is your server), and the server acks it right away (well, about 0.3ms later) in packet 5 with a payload of 0 bytes. So far so good - all data sent and acknowledged for. Both systems are happy and have nothing else to say apparently.</p><p>In packet 6, the server sends 722 bytes to the client, which are acknowledged in packet 7 with a delay of about 2ms. Also not too bad. Since there had been no client data that the server had to react to you can ignore the delta time here. Servers <strong>only</strong> need to send packets fast if they have been asked for data, which is not the case here.</p><p>I think the 30s delta between packet 5 and 6 tells the story - if you ever encounter a number that "nicely" aligned to a timeout value a human programmer would select (typically numbers close to 10, 15, 20, 30, 45, 60, 90, 120 seconds) it is an application issue. Maybe both client and servers had nothing to say to each other, so they waited - very often you'll see packets like yours when two nodes are doing TCP keep alives to keep the session from timing out.</p><p>So unless you <strong>know</strong> that the application is slow you can disregard the pattern you found. But <strong>if</strong> the application is slow you'll need to ask the application guys what they're doing in the 30 seconds time window, and why they do not process data faster.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '12, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9015" class="comments-container"></div><div id="comment-tools-9015" class="comment-tools"></div><div class="clear"></div><div id="comment-9015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

