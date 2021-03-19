+++
type = "question"
title = "SYN is answered by a strange ACK, RST is ignored. Windows"
description = '''This is from a customer, cannot send the whole log. One side is our communications device, another is Windows Server 2008. http://imgur.com/gxpolJ3 This happens very rarely, but we see it. Windows replies with &#x27;2470&#x27;, seq is 1 instead of 0, and it is ACK instead of SYN-ACK, and it acks a packet that...'''
date = "2013-02-22T09:54:00Z"
lastmod = "2013-02-22T23:30:00Z"
weight = 18817
keywords = [ "ack", "handshake", "syn", "tcp" ]
aliases = [ "/questions/18817" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [SYN is answered by a strange ACK, RST is ignored. Windows](/questions/18817/syn-is-answered-by-a-strange-ack-rst-is-ignored-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18817-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is from a customer, cannot send the whole log. One side is our communications device, another is Windows Server 2008.</p><p><a href="http://imgur.com/gxpolJ3">http://imgur.com/gxpolJ3</a></p><p>This happens very rarely, but we see it.</p><p>Windows replies with '2470', seq is 1 instead of 0, and it is ACK instead of SYN-ACK, and it acks a packet that is never seen (not in all the previous communication either). This packet is repeated as if Windows sees duplicates. RST is ignored. The device retries and finally succeeds. Any idea what is wrong?</p></div><div id="question-tags" class="tags-container tags">ack handshake syn tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '13, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/669dc3a462125228156d0c8aa71d09e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IoT&#39;s gravatar image" /><p>IoT<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IoT has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Feb '13, 10:00</p></div></div><div id="comments-container-18817" class="comments-container"><span id="18822"></span><div id="comment-18822" class="comment"><div id="post-18822-score" class="comment-score"></div><div class="comment-text"><p>Thank you! Lets see, here is what happens:</p><pre><code>1. Device&gt;  SYN // device starts a handshake
2. Windows&lt; ACK // ?? Should be SYN-ACK. Also, ack seq is a bad number
3. Device&gt;  RST // Device did not understands and it resets
4. Device&gt;  SYN // device retries an attempt
5. Windows&lt; ACK // ?? Sees it again, but it is even a duplicate of 2. 
                //     as if there was a duplicate packet from device 
6. Device&gt;  RST // Device did not understands and it resets</code></pre><p>I would assume Windows would reset if it could not service the connection, instead the device resets - because it gets ACK instead of SYN-ACK.....</p><p>By the way the wireshark is taken at Windows side. Any further comments?</p></div><div id="comment-18822-info" class="comment-info"><span class="comment-age">(22 Feb '13, 11:58)</span> IoT</div></div></div><div id="comment-tools-18817" class="comment-tools"></div><div class="clear"></div><div id="comment-18817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18827"></span>

<div id="answer-container-18827" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18827-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at your image, all sessions that fail are from port 1598 (I looked up picknfs in the services file). Then the session that does succeed is from port 1601 (again from the services file). So it looks like a device between you and the server was having a problem with traffic from port 1598 at the time.</p><p>I have seen this behavior with a Cisco ASA firewall running old software. But it could be a problem on any device that keeps track of sessions (Firewall, Loadbalancer, Proxy, etc.). What kind of devices are in the path?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '13, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18827" class="comments-container"><span id="18832"></span><div id="comment-18832" class="comment"><div id="post-18832-score" class="comment-score"></div><div class="comment-text"><p>I got the answer from the customer representative: the Windows server (that gives bad replies) has Windows Firewall and it also has Symantec Endpoint Protection. He will attempt to try disabling these. And here is the [whole chunk in cloudshark][1] <a href="http://www.cloudshark.org/captures/6be79d094391">http://www.cloudshark.org/captures/6be79d094391</a></p></div><div id="comment-18832-info" class="comment-info"><span class="comment-age">(23 Feb '13, 10:02)</span> IoT</div></div><span id="18835"></span><div id="comment-18835" class="comment"><div id="post-18835-score" class="comment-score">1</div><div class="comment-text"><p>I'm confused. Would anyone care to speculate why, in frames 3, 6, 9, 12, and 15, the RST packet claims to be both FROM and TO IP address 72.237.119.107, whereas the MAC addresses correspond to packets that are FROM 192.168.1.2 and TO 72.237.119.107, as does the IP TTL? Is this just an intermediate device that's completely mangling the packets?</p></div><div id="comment-18835-info" class="comment-info"><span class="comment-age">(23 Feb '13, 17:23)</span> Jim Aragon</div></div><span id="18836"></span><div id="comment-18836" class="comment"><div id="post-18836-score" class="comment-score"></div><div class="comment-text"><p>Wow, this is big, and I did not notice this. Thank you!</p></div><div id="comment-18836-info" class="comment-info"><span class="comment-age">(23 Feb '13, 22:55)</span> IoT</div></div><span id="18837"></span><div id="comment-18837" class="comment"><div id="post-18837-score" class="comment-score">1</div><div class="comment-text"><p>How are these networks connected? I notice that the round trip time is very high--well over 700 ms--even for the successful connection, and we seem to be going through some sort of DigiBoard device.</p></div><div id="comment-18837-info" class="comment-info"><span class="comment-age">(24 Feb '13, 09:36)</span> Jim Aragon</div></div><span id="18855"></span><div id="comment-18855" class="comment"><div id="post-18855-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much Jim - I just learned that our engineers identified a firmware bug that led to this behavior. Fyi, this is an over-the-air mesh network in the area of smart metering. Devices from different vendors are involved.</p></div><div id="comment-18855-info" class="comment-info"><span class="comment-age">(25 Feb '13, 11:25)</span> IoT</div></div></div><div id="comment-tools-18827" class="comment-tools"></div><div class="clear"></div><div id="comment-18827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18820"></span>

<div id="answer-container-18820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18820-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like a typical case of where the application decides to refuse a session based on some setting it has. This is usually something like "only allow clients from a subnet like w.x.y.z" - the SYN comes in, and the TCP stack tells the application about it while it already acknowledges the SYN on it's own. The application realizes that it doesn't like the connection from that source IP and shuts it down by closing the socket - which results in a reset.</p><p>In your case the connection works after a while, so the criteria can't be the source IP. But maybe there is some "maximum concurrent sessions" setting in the application, and it will only allow the new connection after an older one has finished and/or has timed out. Sometimes FTP server do something like this to avoid having too many connections, but they ususaly do it within the application flow, not on kinda rude socket behavior.</p><p>Check if there is a limitation of any kind on the device that sends the reset. If there isn't any (meaning: someone other than you tells your there isn't any ;-)) you should try to verify this. I would capture the connections after a restart of the server and start counting concurrent sessions, which you can do with Wireshark conversation stastistics by looking at start and duration times.</p><p>Oh, and by the way, the RST is not "ignored". The client just tries a new connection attempt by sending another SYN.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '13, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-18820" class="comments-container"><span id="18829"></span><div id="comment-18829" class="comment"><div id="post-18829-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much! I will have to wait until Monday. I will also ask if it is possible to post the whole shark.</p></div><div id="comment-18829-info" class="comment-info"><span class="comment-age">(23 Feb '13, 01:57)</span> IoT</div></div></div><div id="comment-tools-18820" class="comment-tools"></div><div class="clear"></div><div id="comment-18820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

