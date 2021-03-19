+++
type = "question"
title = "Remote capture with rpcapd on a CentOS server."
description = '''I have two computers in my office on a local network so both using 192.168.x.x IPs. One is my work PC that has Wireshark installed and running fine (when I capture from the NICs in this machine) running Windows 7. The other is a headless CentOS machine, set up as a proxy, that I use for capturing da...'''
date = "2014-10-16T07:18:00Z"
lastmod = "2014-10-17T01:58:00Z"
weight = 37111
keywords = [ "rpcapd", "centos" ]
aliases = [ "/questions/37111" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote capture with rpcapd on a CentOS server.](/questions/37111/remote-capture-with-rpcapd-on-a-centos-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37111-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two computers in my office on a local network so both using 192.168.x.x IPs. One is my work PC that has Wireshark installed and running fine (when I capture from the NICs in this machine) running Windows 7. The other is a headless CentOS machine, set up as a proxy, that I use for capturing data through a specific local network. I usually run tshark via PuTTY for what I need to do but my colleagues (on the same local network) would like the ability to add a remote interface to their local copy of Wireshark and capture the traffic going through this proxy.</p><p>So far I have rpcapd running on the CentOS box and it appears to be set up properly. It doesn't give any errors on running, it just prints "Press CTRL + C to stop the server..."</p><p>On my Windows 7 machine I am trying to add a remote interface. When I put in the address to the CentOS box and a un/pw combo Wireshark responds with:</p><blockquote><code>Can't get list of interfaces: Authentication failed: no such user</code></blockquote><p>And in the PuTTY Window rpcapd responds with:</p><blockquote><code>I'm exiting from the child loop The other host terminated the connection. Child terminated</code></blockquote><p>I don't know what to try to get it to accept the user, or if the issue really is to do with the user.</p><p>The un/pw combo I'm using works when I use it to connect over SSH so they are accepted by the CentOS machine.</p><p>I tried to add the remote interface using the root/pw combo to see if there was any permissions I might have missed off the user I've been trying but got the same result.</p><p>The port is open on iptables and I have tried disabling iptables to be sure it wasn't interfering.</p><p>The machines can ping each other and they are communicating as rpcapd responds to the attempt to connect, so it would appear that everything is getting through fine.</p><p>Does anyone have any suggestions of what I could try next?</p></div><div id="question-tags" class="tags-container tags">rpcapd centos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '14, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/b6eca2aedd2b00d7209007a124f40f93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fooboo&#39;s gravatar image" /><p>fooboo<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fooboo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '14, 07:22</p></div></div><div id="comments-container-37111" class="comments-container"></div><div id="comment-tools-37111" class="comment-tools"></div><div class="clear"></div><div id="comment-37111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37125"></span>

<div id="answer-container-37125" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37125-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can have a look at the communication between wireshark and rpcap with another wireshark. There you can see what the username is that is communicated to rpcap. Might help figure things out.</p><p>Have a look at the sourcecode as well, via the <a href="http://www.winpcap.org/devel.htm">WinPcap site</a>. You'll find the user check in winpcap/wpcap/libpcap/rpcapd/daemon.c. It's failing in a call to getpwnam().</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '14, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-37125" class="comments-container"><span id="37130"></span><div id="comment-37130" class="comment"><div id="post-37130-score" class="comment-score"></div><div class="comment-text"><p>It's definitely sending the right un/pw (I did check with a 2nd wireshark instance), and that user definitely exists (I can SSH with that same un/pw pair) but the response is that it doesn't exist so I need to find out why a user that exists and can log in to the server is considered not to exist when I try to use remote capture. Is there a permission or group I need to add it to? Do I need to tell something somewhere that it's allowed so that it responds with does exist instead?</p></div><div id="comment-37130-info" class="comment-info"><span class="comment-age">(17 Oct '14, 04:00)</span> fooboo</div></div></div><div id="comment-tools-37125" class="comment-tools"></div><div class="clear"></div><div id="comment-37125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

