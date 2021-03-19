+++
type = "question"
title = "No SYN/ACK for the SYN packet"
description = '''Hi Friends, This is my first post and will try to make it as informative as I can. The issue is related to remote desktop connection on one of the windows 2008 R2 server. Some users are facing issue while connecting to remote desktop session of a server in VLAN A. For the same server remote desktop ...'''
date = "2015-06-17T04:39:00Z"
lastmod = "2015-06-24T04:42:00Z"
weight = 43240
keywords = [ "rdp", "wireshark" ]
aliases = [ "/questions/43240" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [No SYN/ACK for the SYN packet](/questions/43240/no-synack-for-the-syn-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43240-score" class="post-score" title="current number of votes">0</div><span id="post-43240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Friends,</p><p>This is my first post and will try to make it as informative as I can. The issue is related to remote desktop connection on one of the windows 2008 R2 server. Some users are facing issue while connecting to remote desktop session of a server in VLAN A. For the same server remote desktop for other users are working fine. While troubleshooting Network team was able to see traffic flowing through the firewall and reaching to the server but never responded back. I did setup wireshark packet capture on the server side to analyse the traffic. I do see packets reaching to the server but are not being responded back. There is packet retransmission happening from client side due to no ACK. Can any one suggest what could be wrong here?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/1_Ires8Oy.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '15, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/83e95ff1ecf36ca47241a9c4160d118e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vjay&#39;s gravatar image" /><p><span>vjay</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vjay has no accepted answers">0%</span></p></img></div></div><div id="comments-container-43240" class="comments-container"></div><div id="comment-tools-43240" class="comment-tools"></div><div class="clear"></div><div id="comment-43240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43242"></span>

<div id="answer-container-43242" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43242-score" class="post-score" title="current number of votes">2</div><span id="post-43242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vjay has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I see three possible reasons:</p><ul><li>you don't see the server response (SYN-ACK( due to a known "problem" of your capture setup (see here: <a href="https://ask.wireshark.org/tags/outgoing/)">https://ask.wireshark.org/tags/outgoing/)</a></li><li>there is a SYN-ACK, but the server is dual homed (multiple interfaces in the same subnet) and it sends the response out a different interface.</li><li>there is no SYN-ACK, which means the RDP server did not answer the SYN. That's something you can only diagnose with the help of microsoft.</li></ul><p>Personally I believe it's option #2, although this is just a wild guess: I've seen that happen from time to time, because people give their servers several interfaces for "redundancy" reasons and then they simply assign an IP address from the same subnet (Windows does not prevent that)! This usually works on a local network without security devices (firewall, loadbalancers, etc.), but it can cause problems if those devices are in place.</p><p>In your case, the firewall might well block the SYN-ACK, if it's coming from a different MAC address than the SYN was sent to (windows sends the SYN-ACK out the other interface). This depends on the firewall type and on the firewall configuration.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43242" class="comments-container"><span id="43244"></span><div id="comment-43244" class="comment"><div id="post-43244-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for your time. You are spot on. We do have two interfaces on that server over different VLAN but I couldn't capture syn/ack on other interface. I applied same filter as first interface which receives SYN packets. Is there anyway I can capture those SYN/ACK packets on second interface?</p></div><div id="comment-43244-info" class="comment-info"><span class="comment-age">(17 Jun '15, 05:18)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43246"></span><div id="comment-43246" class="comment"><div id="post-43246-score" class="comment-score"></div><div class="comment-text"><p>Set Wireshark to capture from all relevant interfaces. Simply check all the interfaces you wish to capture from in the Capture Options dialog.</p></div><div id="comment-43246-info" class="comment-info"><span class="comment-age">(17 Jun '15, 05:27)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43248"></span><div id="comment-43248" class="comment"><div id="post-43248-score" class="comment-score"></div><div class="comment-text"><p>to rule out problem #1 you should capture on a switch mirror/monitor/span port, which mirrors the traffic of both server interfaces.</p></div><div id="comment-43248-info" class="comment-info"><span class="comment-age">(17 Jun '15, 06:19)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43253"></span><div id="comment-43253" class="comment"><div id="post-43253-score" class="comment-score"></div><div class="comment-text"><p>Well, I am getting all the hand shakes and frames for other communication only for this particular communication I am seeing this behaviour. RDP connections are working for internal traffic but the issue is for external traffic where we are only getting SYN packets in capture. For internal traffic we are getting ACK packets from same interface. Do you think problem#1 and problem#3 can still be an issue?</p></div><div id="comment-43253-info" class="comment-info"><span class="comment-age">(17 Jun '15, 06:50)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43255"></span><div id="comment-43255" class="comment"><div id="post-43255-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but the issue is for external traffic where we are only getting SYN packets in capture.</p></blockquote><p>O.K. can you please provide a capture file for the case where it does not work? I want to check if there is something wrong in the frame with the SYN flag.</p><blockquote><p>Do you think problem#1 and problem#3 can still be an issue?</p></blockquote><p>Maybe. Can you asure that the frames in <strong>both cases</strong> (internal and 'external') are taking the same path/route?</p></div><div id="comment-43255-info" class="comment-info"><span class="comment-age">(17 Jun '15, 07:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43256"></span><div id="comment-43256" class="comment not_top_scorer"><div id="post-43256-score" class="comment-score"></div><div class="comment-text"><p>Pardon me for ignorance, How can i upload a file here?</p></div><div id="comment-43256-info" class="comment-info"><span class="comment-age">(17 Jun '15, 07:29)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43258"></span><div id="comment-43258" class="comment not_top_scorer"><div id="post-43258-score" class="comment-score"></div><div class="comment-text"><p>You can't. Please upload it to dropbox, google drive or cloudshark.org and then post the link here.</p></div><div id="comment-43258-info" class="comment-info"><span class="comment-age">(17 Jun '15, 07:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43259"></span><div id="comment-43259" class="comment not_top_scorer"><div id="post-43259-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt.</p><p>External Traffic : <a href="https://www.cloudshark.org/captures/7e47bcb89d32">https://www.cloudshark.org/captures/7e47bcb89d32</a></p><p>Internal Traffic : <a href="https://www.cloudshark.org/captures/9d169624703d">https://www.cloudshark.org/captures/9d169624703d</a></p></div><div id="comment-43259-info" class="comment-info"><span class="comment-age">(17 Jun '15, 07:47)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43260"></span><div id="comment-43260" class="comment not_top_scorer"><div id="post-43260-score" class="comment-score"></div><div class="comment-text"><p>The SYN frame looks good, but as you can see there is also no answer to the ping requests.</p><p>So, this leads me to further assumptions</p><ul><li>Do you have the windows firewall enabled on that windows system or any other seecurity software (Endpoint security) that might block those frames?</li><li>Do you have a default route pointing back to the firewall or at least a route for the remote network?</li></ul><p>Can you please post the output of the following command on the Windows server?</p><blockquote><p>route print</p></blockquote></div><div id="comment-43260-info" class="comment-info"><span class="comment-age">(17 Jun '15, 07:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43261"></span><div id="comment-43261" class="comment not_top_scorer"><div id="post-43261-score" class="comment-score"></div><div class="comment-text"><p>Pasting it in two parts.</p><pre><code>C:\Users&gt;route print
===========================================================================
Interface List
 12...00 0c 29 0c 88 7b ......Intel(R) PRO/1000 MT Network Connection #2
 11...00 0c 29 0c 88 71 ......Intel(R) PRO/1000 MT Network Connection
  1...........................Software Loopback Interface 1
 13...00 00 00 00 00 00 00 e0 Microsoft ISATAP Adapter
 14...00 00 00 00 00 00 00 e0 Microsoft ISATAP Adapter #2
 15...00 00 00 00 00 00 00 e0 Teredo Tunneling Pseudo-Interface
===========================================================================

IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0      172.16.87.5    172.16.87.123    266
      62.116.24.9  255.255.255.255      172.16.84.1    172.16.84.121     11
       80.90.2.33  255.255.255.255      172.16.84.1    172.16.84.121     11
     88.81.157.71  255.255.255.255      172.16.84.1    172.16.84.121     11
    91.220.189.12  255.255.255.255      172.16.84.1    172.16.84.121     11
        127.0.0.0        255.0.0.0         On-link         127.0.0.1    306
        127.0.0.1  255.255.255.255         On-link         127.0.0.1    306
  127.255.255.255  255.255.255.255         On-link         127.0.0.1    306
        172.0.0.0        255.0.0.0      172.16.84.1    172.16.84.121     11
      172.16.84.0    255.255.255.0         On-link     172.16.84.121    266
    172.16.84.121  255.255.255.255         On-link     172.16.84.121    266
    172.16.84.255  255.255.255.255         On-link     172.16.84.121    266
      172.16.87.0    255.255.255.0         On-link     172.16.87.123    266
    172.16.87.123  255.255.255.255         On-link     172.16.87.123    266
    172.16.87.255  255.255.255.255         On-link     172.16.87.123    266
        224.0.0.0        240.0.0.0         On-link         127.0.0.1    306
        224.0.0.0        240.0.0.0         On-link     172.16.87.123    266
        224.0.0.0        240.0.0.0         On-link     172.16.84.121    266
  255.255.255.255  255.255.255.255         On-link         127.0.0.1    306
  255.255.255.255  255.255.255.255         On-link     172.16.87.123    266
  255.255.255.255  255.255.255.255         On-link     172.16.84.121    266
===========================================================================</code></pre></div><div id="comment-43261-info" class="comment-info"><span class="comment-age">(17 Jun '15, 08:12)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43262"></span><div id="comment-43262" class="comment not_top_scorer"><div id="post-43262-score" class="comment-score"></div><div class="comment-text"><pre><code>Persistent Routes:
  Network Address          Netmask  Gateway Address  Metric
        172.0.0.0        255.0.0.0      172.16.84.1       1
     88.81.157.71  255.255.255.255      172.16.84.1       1
       80.90.2.33  255.255.255.255      172.16.84.1       1
      62.116.24.9  255.255.255.255      172.16.84.1       1
    91.220.189.12  255.255.255.255      172.16.84.1       1
          0.0.0.0          0.0.0.0      172.16.87.5  Default
===========================================================================

IPv6 Route Table
===========================================================================
Active Routes:
 If Metric Network Destination      Gateway
  1    306 ::1/128                  On-link
  1    306 ff00::/8                 On-link
===========================================================================
Persistent Routes:
  None
</code></pre></div><div id="comment-43262-info" class="comment-info"><span class="comment-age">(17 Jun '15, 08:13)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43263"></span><div id="comment-43263" class="comment not_top_scorer"><div id="post-43263-score" class="comment-score"></div><div class="comment-text"><p>Opps. Let me see any other way I can upload.</p></div><div id="comment-43263-info" class="comment-info"><span class="comment-age">(17 Jun '15, 08:20)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43264"></span><div id="comment-43264" class="comment not_top_scorer"><div id="post-43264-score" class="comment-score"></div><div class="comment-text"><p>You have two gateways. One for 172.0.0.0/8 and one default route.</p><pre><code>          0.0.0.0          0.0.0.0      172.16.87.5    172.16.87.123    266
        172.0.0.0        255.0.0.0      172.16.84.1    172.16.84.121     11</code></pre><p>Now, what's the IP address of the firewall and what's the "other" gateway then?</p><p>The reply packets for the "external client" (10.6.4.125) should be coming in through gateway 172.16.87.5, as that's the way back for your them (default GW). If that's not the case, you have some form of asymmetric routing, which is a bad idea with statefull firewalls. But then you should at least be able to see the answer of your server on its other interface!</p></div><div id="comment-43264-info" class="comment-info"><span class="comment-age">(17 Jun '15, 08:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43267"></span><div id="comment-43267" class="comment not_top_scorer"><div id="post-43267-score" class="comment-score"></div><div class="comment-text"><p>Do you mean to say the other interface 172.16.87.123 will send reply to 10.6.4.125? My filter was for both interfaces and via filtering 10.6.4.125 I could get only the response which I uploaded.</p></div><div id="comment-43267-info" class="comment-info"><span class="comment-age">(17 Jun '15, 08:47)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43269"></span><div id="comment-43269" class="comment not_top_scorer"><div id="post-43269-score" class="comment-score"></div><div class="comment-text"><p>I can't tell you, because I don't know where the traffic came in. Can you please post the output of the following command on the server?</p><blockquote><p>dumpcap -D -M</p></blockquote></div><div id="comment-43269-info" class="comment-info"><span class="comment-age">(17 Jun '15, 08:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43271"></span><div id="comment-43271" class="comment not_top_scorer"><div id="post-43271-score" class="comment-score"></div><div class="comment-text"><ol><li>\Device\NPF_{01FCA39F-F324-4E69-8846-98BC42FD040A} Intel(R) PRO/1000 MT Net work Connection Web Front 0 172.16.87.123 network</li><li>\Device\NPF_{8BEF7088-B506-40A4-A1A2-D6D46A4BF9CE} Intel(R) PRO/1000 MT Net work Connection Web Backend 0 172.16.84.121 network</li></ol><p>In network capture for both interfaces I only see traffic coming for 3389 from 10.6.4.125 IP but don't see any traffic going out from 3389 port to that IP Address.</p></div><div id="comment-43271-info" class="comment-info"><span class="comment-age">(17 Jun '15, 09:04)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43282"></span><div id="comment-43282" class="comment not_top_scorer"><div id="post-43282-score" class="comment-score"></div><div class="comment-text"><p>as I suspected, the traffic in your capture file was captured on the interface with IP address 172.16.84.121, (see Statistics -&gt; Summary. You'll find the ID of the interface there). Now, the default route will send out the answer through the other interface to gateway 172.16.87.5. This will result in a firewall seeing only parts of the traffic, or it will see the same session on different interfaces. In both cases a stateful firewall will deny to process the session.</p><p>Why you don't see the SYN-ACK in Wireshark, I can't tell you. Maybe there is something wrong with your capture setup. You should see the SYN-ACK and the ping response on the other interface (172.16.87.123).</p><p>There are two obvious solutions:</p><ul><li>Add a route for 10.x.x.x/8 (or whatever subnet you need) to 172.16.84.1</li><li>Perform SNAT on the Firewall, and translate the address 10.6.4.125 to an address in the range of 172.x.x.x/8. Please ask your firewall admins, they should know what to do.</li></ul><p>BTW: There is still a chance, that a filter on the Windows system blocks your frames, like the windows firewall or any other form of security software. Did you check that?</p></div><div id="comment-43282-info" class="comment-info"><span class="comment-age">(17 Jun '15, 13:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43306"></span><div id="comment-43306" class="comment not_top_scorer"><div id="post-43306-score" class="comment-score"></div><div class="comment-text"><p>Yes, local firewall has been turned off and there is no antivirus software running on the server.</p><p>Unfortunately, Network Admin is stuck on the point that firewall is passing traffic but server is not responding, I will need some proof to get him make change on gateway or firewall. Is there a way I can capture response from other interface to 10.6.4.125? I do have whole capture without any filter available for both the interfaces but I don't see any response for 10.6.4.125.</p></div><div id="comment-43306-info" class="comment-info"><span class="comment-age">(18 Jun '15, 00:12)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43310"></span><div id="comment-43310" class="comment not_top_scorer"><div id="post-43310-score" class="comment-score"></div><div class="comment-text"><p>To make sure you are <strong>really</strong> capturing on both ports, please start Wireshark with the following command:</p><blockquote><p>wireshark -ni 1 -ni 2 -k -f "host 10.6.4.125"</p></blockquote><p>Then start the ping and connect to the RDP server. Wait 10-20 seconds. Then look at the data. You should see the ping response now and the SYN-ACK.</p><p>If you <strong>don't</strong> see the answer packets, there is indeed a problem on your server and then you need to double check that nothing <strong>on the server</strong> blocks the frames (AV, IPS, Endpoint security, etc.).</p></div><div id="comment-43310-info" class="comment-info"><span class="comment-age">(18 Jun '15, 01:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43313"></span><div id="comment-43313" class="comment not_top_scorer"><div id="post-43313-score" class="comment-score"></div><div class="comment-text"><p>Still getting same results. On Windows server also firewall has been turned off.</p><pre><code>C:\Program Files\Wireshark&gt;netsh advfirewall show currentprofile

Domain Profile Settings:
----------------------------------------------------------------------
State                                 OFF
Firewall Policy                       BlockInbound,AllowOutbound
LocalFirewallRules                    N/A (GPO-store only)
LocalConSecRules                      N/A (GPO-store only)
InboundUserNotification               Disable
RemoteManagement                      Disable
UnicastResponseToMulticast            Enable

Logging:
LogAllowedConnections                 Disable
LogDroppedConnections                 Disable
FileName                              %systemroot%\system32\LogFiles\Firewall\pf
irewall.log
MaxFileSize                           4096

Public Profile Settings:
----------------------------------------------------------------------
State                                 OFF
Firewall Policy                       BlockInbound,AllowOutbound
LocalFirewallRules                    N/A (GPO-store only)
LocalConSecRules                      N/A (GPO-store only)
InboundUserNotification               Disable
RemoteManagement                      Disable
UnicastResponseToMulticast            Enable

Logging:
LogAllowedConnections                 Disable
LogDroppedConnections                 Disable
FileName                              %systemroot%\system32\LogFiles\Firewall\pf
irewall.log
MaxFileSize                           4096

Ok.
C:\Program Files\Wireshark&gt;</code></pre><p>Don't know what could be the issue.</p></div><div id="comment-43313-info" class="comment-info"><span class="comment-age">(18 Jun '15, 02:03)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43314"></span><div id="comment-43314" class="comment not_top_scorer"><div id="post-43314-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Still getting same results. On Windows server also firewall has been turned off.<br />
Don't know what could be the issue.</p></blockquote><p>I don't know it either, but if you still don't see the reply packets in the capture file (with the command I posted above), then I conclude that:</p><ul><li>something on the Windows system blocks the incoming frames. I can't help you with that. Please ask your local Windows hero!</li><li><strong>OR the server does not get an ARP reply for the Default Gateway</strong>. Do you see ARP requests in the capture file? What is the output of the following command?</li></ul><blockquote><p>arp -a | find "172.16.87.5"</p></blockquote></div><div id="comment-43314-info" class="comment-info"><span class="comment-age">(18 Jun '15, 02:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43315"></span><div id="comment-43315" class="comment not_top_scorer"><div id="post-43315-score" class="comment-score"></div><div class="comment-text"><p>C:\Program Files\Wireshark&gt;arp -a | find "172.16.87.5" 172.16.87.5 00-23-e9-6e-09-87 dynamic</p><p>How can I check ARP requests in capture file?</p></div><div id="comment-43315-info" class="comment-info"><span class="comment-age">(18 Jun '15, 02:28)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43316"></span><div id="comment-43316" class="comment not_top_scorer"><div id="post-43316-score" class="comment-score"></div><div class="comment-text"><p>Use a display filter of "arp".</p></div><div id="comment-43316-info" class="comment-info"><span class="comment-age">(18 Jun '15, 02:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43317"></span><div id="comment-43317" class="comment not_top_scorer"><div id="post-43317-score" class="comment-score"></div><div class="comment-text"><p>You don't have to look for ARP requests, as the server knows the MAC address of the gateway!</p><p>So, my conclusion is: <strong>something</strong> on the server blocks the incoming requests from 10.6.4.125. You say, that there is no security software enabled, so I can't tell you what it might be. Please ask your local windows hero/guru to have a look at it.</p></div><div id="comment-43317-info" class="comment-info"><span class="comment-age">(18 Jun '15, 02:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43318"></span><div id="comment-43318" class="comment not_top_scorer"><div id="post-43318-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for your extensive support. Really appreciated. I will check with Windows team.</p></div><div id="comment-43318-info" class="comment-info"><span class="comment-age">(18 Jun '15, 03:04)</span> <span class="comment-user userinfo">vjay</span></div></div><span id="43319"></span><div id="comment-43319" class="comment not_top_scorer"><div id="post-43319-score" class="comment-score"></div><div class="comment-text"><p>You're welcome!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-43319-info" class="comment-info"><span class="comment-age">(18 Jun '15, 03:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43498"></span><div id="comment-43498" class="comment not_top_scorer"><div id="post-43498-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt Knochner</span>, I have added persistent route for the destination and it is working fine now. I thought to put an update so it may help someone in future.</p></div><div id="comment-43498-info" class="comment-info"><span class="comment-age">(24 Jun '15, 04:42)</span> <span class="comment-user userinfo">vjay</span></div></div></div><div id="comment-tools-43242" class="comment-tools"><span class="comments-showing"> showing 5 of 27 </span> <a href="#" class="show-all-comments-link">show 22 more comments</a></div><div class="clear"></div><div id="comment-43242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

