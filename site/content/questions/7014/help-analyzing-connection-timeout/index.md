+++
type = "question"
title = "Help analyzing connection timeout"
description = '''Hello, I have been having issues with long-running ssh connections dropping. I want to blame our firewall, but I see no evidence of it timing out states (normally I&#x27;d see packets associated with a session that timed out being blocked). To help figure this out, I started an session from one host to a...'''
date = "2011-10-20T16:31:00Z"
lastmod = "2011-10-21T00:21:00Z"
weight = 7014
keywords = [ "analyze", "tcp", "timeout", "keepalive" ]
aliases = [ "/questions/7014" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help analyzing connection timeout](/questions/7014/help-analyzing-connection-timeout)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7014-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have been having issues with long-running ssh connections dropping. I want to blame our firewall, but I see no evidence of it timing out states (normally I'd see packets associated with a session that timed out being blocked). To help figure this out, I started an session from one host to another after starting a tcpdump trace on both hosts.</p><p>Looking at the captures side-by-side in wireshark, I'm a bit perplexed. Can anyone explain further what I'm seeing? Below is the text output of the "flow graph" from both ends. The first output is from the host that initiated the ssh session (sanitized to 10.1.1.1) the second output is from the ssh session's destination host (sanitized to 10.2.2.2). 10.1.1.1 has a firewall between it and the internet (no NAT though), 10.2.2.2 has a host-based firewall, but tcpdump sees the packets before any filtering.</p><p>I couldn't get the code formatting here to actually work, so I've put it here instead:</p><p>1 - <a href="http://pastebin.ca/2092041">http://pastebin.ca/2092041</a></p><p>2 - <a href="http://pastebin.ca/2092042">http://pastebin.ca/2092042</a></p></div><div id="question-tags" class="tags-container tags">analyze tcp timeout keepalive</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '11, 16:31</strong></p><img src="https://secure.gravatar.com/avatar/ca19cdf35f8edceb6aec6d7c8ddaecca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sporkman&#39;s gravatar image" /><p>sporkman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sporkman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Oct '11, 16:32</p></div></div><div id="comments-container-7014" class="comments-container"></div><div id="comment-tools-7014" class="comment-tools"></div><div class="clear"></div><div id="comment-7014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7017"></span>

<div id="answer-container-7017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7017-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like both sides are sending keep-alive packets after 2 hours, but they never reach each other. Most probably because the firewall in between has timed out the session. You can change the keep-alive interval on your ssh session to prevent the session from being dropped. Here is some info from the ssh_config manpage of ssh on my mac:</p><pre><code> ServerAliveCountMax
         Sets the number of server alive messages (see below) which may be sent without ssh(1) receiving any mes-
         sages back from the server.  If this threshold is reached while server alive messages are being sent, ssh
         will disconnect from the server, terminating the session.  It is important to note that the use of server
         alive messages is very different from TCPKeepAlive (below).  The server alive messages are sent through the
         encrypted channel and therefore will not be spoofable.  The TCP keepalive option enabled by TCPKeepAlive is
         spoofable.  The server alive mechanism is valuable when the client or server depend on knowing when a con-
         nection has become inactive.

         The default value is 3.  If, for example, ServerAliveInterval (see below) is set to 15 and
         ServerAliveCountMax is left at the default, if the server becomes unresponsive, ssh will disconnect after
         approximately 45 seconds.  This option applies to protocol version 2 only.

 ServerAliveInterval
         Sets a timeout interval in seconds after which if no data has been received from the server, ssh(1) will
         send a message through the encrypted channel to request a response from the server.  The default is 0,
         indicating that these messages will not be sent to the server.  This option applies to protocol version 2
         only.

 TCPKeepAlive
         Specifies whether the system should send TCP keepalive messages to the other side.  If they are sent, death
         of the connection or crash of one of the machines will be properly noticed.  However, this means that con-
         nections will die if the route is down temporarily, and some people find it annoying.

         The default is ``yes&#39;&#39; (to send TCP keepalive messages), and the client will notice if the network goes
         down or the remote host dies.  This is important in scripts, and many users want it too.

         To disable TCP keepalive messages, the value should be set to ``no&#39;&#39;.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '11, 00:21</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7017" class="comments-container"></div><div id="comment-tools-7017" class="comment-tools"></div><div class="clear"></div><div id="comment-7017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

