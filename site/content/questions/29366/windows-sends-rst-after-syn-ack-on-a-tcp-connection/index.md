+++
type = "question"
title = "Windows sends RST after SYN-ACK on a TCP connection"
description = '''I&#x27;m developing an Windows application that performs NAT between a virtual TAP interface and a physical Ethernet interface (with the purpose of achieving load balancing), using WinPcap. The test setup looks something like this:  I ran the test on two machines with Windows 7 64-bit, and on one of them...'''
date = "2014-02-01T07:40:00Z"
lastmod = "2014-02-01T08:01:00Z"
weight = 29366
keywords = [ "rst", "winpcap", "nat", "tcp", "syn" ]
aliases = [ "/questions/29366" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Windows sends RST after SYN-ACK on a TCP connection](/questions/29366/windows-sends-rst-after-syn-ack-on-a-tcp-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29366-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm developing an Windows application that performs NAT between a virtual TAP interface and a physical Ethernet interface (with the purpose of achieving load balancing), using WinPcap. The test setup looks something like this:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/NAT.png" alt="alt text" /></p><p>I ran the test on two machines with Windows 7 64-bit, and on one of them everything works as expected, but on the other one, after SYN-ACK is received Windows sends a RST, and I don't understand why.</p><p><a href="http://www.cloudshark.org/captures/2c6784d4371c">Here</a> is a Wireshark capture file recorded on the physical interface. The test consist in running a web browser and try access a website. Because the default gateway is set on the TAP interface, all traffic goes through it. So this is what happens:</p><ul><li>SYN is received on TAP interface</li><li>my NAT application performs NAT on the packet and sends it on physical interface</li><li>a SYN-ACK reply is received on the physical if</li><li>for some reason Windows replies with a RST on the physical if</li><li>in the meanwhile my app performs NAT no the SYN-ACK packet and sends it on TAP</li><li>unaware that a RST was sent on physical if, Windows sends an ACK on TAP</li><li>and from here on the website replies with a RST because physical if broke the TCP connection</li></ul><p>Initially I thought that the Windows firewall might be the one breaking the connection, but the problem doesn't go away even if I disable the firewall. Besides, I installed the same firewall on the machine that didn't have problems before and it stayed that way, everything worked as expected.</p><p>Who is sending that RST on the physical interface? How could I find out?</p></div><div id="question-tags" class="tags-container tags">rst winpcap nat tcp syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '14, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/f8e012725d982ab24841ba6445fb0503?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20DB&#39;s gravatar image" /><p>Chris DB<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris DB has no accepted answers">0%</span></p></img></div></div><div id="comments-container-29366" class="comments-container"></div><div id="comment-tools-29366" class="comment-tools"></div><div class="clear"></div><div id="comment-29366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29367"></span>

<div id="answer-container-29367" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29367-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The usual reason for a Reset being sent is either that the incoming packets were in some way catastrophically bad/damaged (which doesn't seem to be the case here), or that the application holding the port has released it in the meantime. That results in the stack receiving a packet for a closed port and answering with a reset.</p><p>You could monitor your port state table (via netstat or Sysinternals tools like TCPView and Process Viewer) to check if your application is closing the port. Microsoft NetMon can also help with that I guess, but I don't have much experience with it.</p><p>If this would be my application I'd try to add debug messages for the component that opens and closes the ports to see when that happens, and add additional exception handlers to see if errors are thrown that could explain the socket closing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '14, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29367" class="comments-container"><span id="29368"></span><div id="comment-29368" class="comment"><div id="post-29368-score" class="comment-score"></div><div class="comment-text"><p>The port is not closed. The port is held by the web browser (Chrome), and you can see that after the RST, Chrome still sends an ACK and a HTTP-GET. I had no idea that the stack is supposed to respond with a RST if it receives a packet for a closed port. Are sockets tied to an interface or do they listen on all interfaces ?</p></div><div id="comment-29368-info" class="comment-info"><span class="comment-age">(01 Feb '14, 08:17)</span> Chris DB</div></div><span id="29369"></span><div id="comment-29369" class="comment"><div id="post-29369-score" class="comment-score"></div><div class="comment-text"><p>Yes, there is an ACK and a HTTP-GET but I guessed that this is from a different process using the same port. It's a little hard to say why that happens, because when a stack sends a Reset it should not reuse to port for anything else for a while. So how come that Chrome is on that port? I thought that trace contains what your NAT application is doing? Or is you application running inside Chrome?</p><p>Sockets can be tied to one or multiple interfaces. You can see how it is bound by using "netstat -an" - if the listening IP is 0.0.0.0 the port is open on all interfaces; if there is a specific IP it is only open for that IP.</p></div><div id="comment-29369-info" class="comment-info"><span class="comment-age">(01 Feb '14, 08:26)</span> Jasper ♦♦</div></div><span id="29370"></span><div id="comment-29370" class="comment"><div id="post-29370-score" class="comment-score"></div><div class="comment-text"><p>BTW, I wrote a program once that showed the exact same pattern: SYN - SYN/ACK - RST. The reason was that I had misinterpreted the socket timeout settings - I thought the value I put in that parameter is seconds, so I used "10", but it was "microseconds". Which meant that when the SYN/ACK came back from the server my client had already torn down the socket again, because it took the server longer than 10 microseconds to respond.</p></div><div id="comment-29370-info" class="comment-info"><span class="comment-age">(01 Feb '14, 08:31)</span> Jasper ♦♦</div></div><span id="29371"></span><div id="comment-29371" class="comment"><div id="post-29371-score" class="comment-score"></div><div class="comment-text"><p>The NAT app is using WinPcap, so it's capturing the packets from one interfaces, modifies the MAC/IP addresses accordingly and sends it on another interface, without port translation. My app doesn't work with sockets, they are handled by the requesting app (i.e. Chrome). Packets are captured by the WinPcap NPF driver at a very low level (before tcpip.sys) and ideally, the stack on the physical interface should ignore the packets and not respond. But it looks like that doesn't happened. I guess there is no escape, I have to do port translation ...</p></div><div id="comment-29371-info" class="comment-info"><span class="comment-age">(01 Feb '14, 08:45)</span> Chris DB</div></div><span id="29374"></span><div id="comment-29374" class="comment"><div id="post-29374-score" class="comment-score"></div><div class="comment-text"><p>Okay, that is your problem then - you're basically listening passively for packets that the host does not have a socket for and so it refuses the connection. You have to do port translation, yes.</p></div><div id="comment-29374-info" class="comment-info"><span class="comment-age">(01 Feb '14, 09:09)</span> Jasper ♦♦</div></div></div><div id="comment-tools-29367" class="comment-tools"></div><div class="clear"></div><div id="comment-29367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

