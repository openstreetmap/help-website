+++
type = "question"
title = "How can I tell if my connection is encrypted?"
description = '''I setup a VPN using SoftEther VPN software, but I don&#x27;t know if my web communications are encrypted. In the software, I have L2TP/IPsec and AES-256-SHA checked off/enabled, but I want to be sure that I&#x27;m not transmitting data that isn&#x27;t unencrypted. Both of the computers are running Windows 7. I dow...'''
date = "2013-07-30T12:15:00Z"
lastmod = "2013-08-24T12:14:00Z"
weight = 23451
keywords = [ "encrypted", "windows7", "wireshark", "packets", "softether" ]
aliases = [ "/questions/23451" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How can I tell if my connection is encrypted?](/questions/23451/how-can-i-tell-if-my-connection-is-encrypted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23451-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I setup a VPN using SoftEther VPN software, but I don't know if my web communications are encrypted. In the software, I have L2TP/IPsec and AES-256-SHA checked off/enabled, but I want to be sure that I'm not transmitting data that isn't unencrypted. Both of the computers are running Windows 7. I downloaded Wireshark, but I don't know how I can tell if the packets I send out are secure/encrypted.</p><p>TL;DR</p><p>Connected to VPN in my house. Enabled encryption in software, want to see if the packets are encrypted. How do I find encrypted packets and be sure that the connection is encrypted?</p></div><div id="question-tags" class="tags-container tags">encrypted windows7 wireshark packets softether</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '13, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/5e201468fc6aef7f120b75ead1fbf697?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MastaChief11&#39;s gravatar image" /><p>MastaChief11<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MastaChief11 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Jul '13, 10:55</p></div></div><div id="comments-container-23451" class="comments-container"></div><div id="comment-tools-23451" class="comment-tools"></div><div class="clear"></div><div id="comment-23451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="23631"></span>

<div id="answer-container-23631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23631-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Connected to VPN in my house. Enabled encryption in software, want to see if the packets are encrypted. How do I find encrypted packets and be sure that the connection is encrypted?</p></blockquote><p>without a VPN tunnel you would not be able to connect to any of your internal 'home/house' IP addresses from any location in the internet. So just by applying logic thinking, you can conclude, that encryption (or at least some tunnel technology) is in place if you are able to connect to those IP addresses, right?</p><p>Using Wireshark, you should see the encryption protocols you described, <strong>if you capture</strong> the communication <strong>off-box</strong> (means in front on any of the involved systems). You will see those encrypted packets with this display filter</p><blockquote><p>lt2p or isakmp or esp</p></blockquote><p>as long as you really use those tunnel protocols!</p><p>If you capture the traffic <strong>on-box</strong> (means the VPN client), it depends on the internals of the VPN client if Wireshark sees the unencrypted or the encrypted traffic. I can't tell, as I don't know SoftEther VPN. Just try it and you'll see...</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23631" class="comments-container"><span id="23637"></span><div id="comment-23637" class="comment not_top_scorer"><div id="post-23637-score" class="comment-score"></div><div class="comment-text"><p>On the server, I sometimes see TLSv1 packets being sent from the server to the client, and the client to the server. Within these packets, I see that it says Secure Sockets Layer. However, I also see packets that are not encrypted, such as ones that are labeled TCP and UDP.</p></div><div id="comment-23637-info" class="comment-info"><span class="comment-age">(08 Aug '13, 06:03)</span> MastaChief11</div></div><span id="23660"></span><div id="comment-23660" class="comment not_top_scorer"><div id="post-23660-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I sometimes see TLSv1 packets being sent from the server to the client,</p></blockquote><p>that could be simply HTTPS or an SSL based VPN.</p></div><div id="comment-23660-info" class="comment-info"><span class="comment-age">(08 Aug '13, 14:20)</span> Kurt Knochner ♦</div></div><span id="23665"></span><div id="comment-23665" class="comment not_top_scorer"><div id="post-23665-score" class="comment-score"></div><div class="comment-text"><p>On the client, I have something similar to "Encrypt connection with Secure Sockets Layer" checked off. Are you saying that my connection is encrypted?</p></div><div id="comment-23665-info" class="comment-info"><span class="comment-age">(08 Aug '13, 17:03)</span> MastaChief11</div></div><span id="23674"></span><div id="comment-23674" class="comment"><div id="post-23674-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Are you saying that my connection is encrypted?</p></blockquote><p>No. I am saying, that there seems to be a TLS/SSL secured connection between your client and your VPN Server. That could be</p><ul><li>a TLS/SSL based VPN Tunnel, although you say you disabled that feature</li><li>the Admin GUI of the VPN Server, if you had that open from the client in parallel: <a href="https://vpnserver/admin/xzy.">https://vpnserver/admin/xzy.</a></li><li>Anything else that is hosted on the server that is your VPN server and your client was accessing that via HTTPS.</li></ul><p>So, to come back to your original question, how you can verify if the connection is encrypted or not?</p><p>As you did not give any details about your network setup, let's just assume a standard setup.</p><pre><code>VPN Client (10.1.1.x) --- Internet Router --- Internet -- VPN Server -- Internal/Home Server (192.168.1.x)</code></pre><p>Please replace my sample IPs with the ones in your environment!</p><p>If you establish a VPN Tunnel from your client and you do a ping from 10.1.1.x to 192.168.1.x (CLI: ping 192.168.1.x), do you see that ping in the capture file?</p><p>If you can't see the ping (Display Filter: icmp) in the capture file <strong>and</strong> you get a response on the CLI, then there is a pretty good chance, that the VPN tunnel is established and the communication is encrypted (see my argument about applying logical thinking in my answer ;-)).</p><p>If you do see the ping in the capture file, then we really need more detailed information about your network setup.</p></div><div id="comment-23674-info" class="comment-info"><span class="comment-age">(09 Aug '13, 05:08)</span> Kurt Knochner ♦</div></div><span id="23688"></span><div id="comment-23688" class="comment not_top_scorer"><div id="post-23688-score" class="comment-score"></div><div class="comment-text"><p>The VPN Server that I am using is within my house, and on the same network that my client is on. I have SSL enabled within the client, but I don't know if TLS is enabled.</p><p>This is my setup (this is the equipment that I have, I'm not sure if this is the correct order):</p><p>VPN Client - VPN Server - Router - Internet</p><p>Should I type this into my Wireshark console (without the things in parenthesis)?</p><p>(Client) 192.168.1.134 --- (Server) 192.168.1.132 --- (Router) 192.168.1.1 -- (Public IP) 50.censored</p><p>I apologize for my inexperience.</p></div><div id="comment-23688-info" class="comment-info"><span class="comment-age">(10 Aug '13, 06:00)</span> MastaChief11</div></div><span id="23689"></span><div id="comment-23689" class="comment"><div id="post-23689-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>(Client) 192.168.1.134</p></blockquote><p>is this your VPN client (the system that runs the VPN client software) or the system you connect to from the internet, using a VPN client on a laptop?</p><blockquote><p>I have SSL enabled within the client, but I don't know if TLS is enabled.</p></blockquote><p>SSL and TLS is almost the same (from a very high-level view - there are of course technical differences). Anyway, if you have enabled SSL, your VPN tunnel traffic (encrypted traffic) will appear as SSL (or TLS) protocol in Wireshark.</p></div><div id="comment-23689-info" class="comment-info"><span class="comment-age">(10 Aug '13, 06:11)</span> Kurt Knochner ♦</div></div><span id="23690"></span><div id="comment-23690" class="comment not_top_scorer"><div id="post-23690-score" class="comment-score"></div><div class="comment-text"><p>The IP that I listed as the client is running as the VPN client (it's running the VPN client software). This is a snapshot I took of Wireshark on my server last week.</p><p><a href="http://www.vpnusers.com/download/file.php?id=117&amp;mode=view">http://www.vpnusers.com/download/file.php?id=117&amp;mode=view</a></p><p>I noticed that not all of the packets are labeled TLSv1. The packet data on the lower half of the image is from the TLSv1 packet.</p></div><div id="comment-23690-info" class="comment-info"><span class="comment-age">(10 Aug '13, 07:13)</span> MastaChief11</div></div><span id="23692"></span><div id="comment-23692" class="comment"><div id="post-23692-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>The IP that I listed as <strong>the client is running as the VPN client</strong> (it's running the VPN client software).</p></blockquote><p>O.K. what are you trying to do? Having a VPN Tunnel in the local network (client <strong>and</strong> VPN server are <strong>in the same subnet</strong>), is only useful in certain environments. Is this just a test?</p><p>The UDP packets in the screenshot could be part of the VPN tunnel. As I don't know your VPN software, I can't tell you.</p><p>please run the following commands on <strong>both</strong> the client and the server.</p><blockquote><p>netstat -nab &gt; netstat_client.txt<br />
netstat -nab &gt; netstat_server.txt</p></blockquote><p>The command may take a few seconds, don't interrupt it! Please run the command as Administrator (e.g. in an elevated DOS box). Then post the content of text files here. I'm interested in the 'owner' of port 40000 (safetynetp).</p><p>The rest (SSL/TLS/https) is either part of the VPN tunnel or (as I already mentioned), the web admin GUI of the server, if that runs on port tcp/443 (https).</p></div><div id="comment-23692-info" class="comment-info"><span class="comment-age">(10 Aug '13, 10:48)</span> Kurt Knochner ♦</div></div><span id="23695"></span><div id="comment-23695" class="comment not_top_scorer"><div id="post-23695-score" class="comment-score"></div><div class="comment-text"><p>I wanted to get the VPN working at my house first (be sure I can connect to it, that it's encrypted, etc.), and then bring it to an office. The server does listen on port 443, and the client is configured to connect to the server via port 443.</p><p>I typed in "netstat -nab &gt; netstat_client.txt" (as an Administrator), but it just skipped to the next line. However, typing only "netstat" did work, and this is the result.</p><p>imgur.com/sOAR6vX</p><p>Where would the file generate if the command worked?</p><p>Both computers are running Windows 7 64 Bit.</p></div><div id="comment-23695-info" class="comment-info"><span class="comment-age">(11 Aug '13, 05:43)</span> MastaChief11</div></div><span id="23696"></span><div id="comment-23696" class="comment not_top_scorer"><div id="post-23696-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I wanted to get the VPN working at my house first (be sure I can connect to it, that it's encrypted, etc.), and then bring it to an office.</p></blockquote><p>well, then you will be able to establish a VPN tunnel, but you will not get any answer if you try to connect something through the tunnel, unless you simulated the office environment at your home.</p><blockquote><p>I typed in "netstat -nab &gt; netstat_client.txt" (as an Administrator), but it just skipped to the next line. However, typing only "netstat" did work, and this is the result.</p></blockquote><p>I need the output of the file netstat_client.txt (command run on the client) <strong>and</strong> netstat_sever.txt (command run on the client). Both files will be created in the same directory where you executed the netstat command.</p><blockquote><p>and this is the result. imgur.com/sOAR6vX</p></blockquote><p>Unfortunately that does not help for two reasons.</p><ol><li>You ran the command only on the client</li><li>You ran the command without option -b (actually -nab)!</li></ol><blockquote><p>The server does listen on port 443, and the client is configured to connect to the server via port 443.</p></blockquote><p>O.K. then there is no reason why the traffic should not be encrypted, however, as I said above, you will have a hard time to test the tunnel, as you won't get an answer from anything "after" the tunnel, unless you simulated parts of the office environment at your home. BTW: What is the IP subnet in the office? If it is also 192.168.1.0/24, then you won't be able to test anything at your home, because the client and the systems that are supposed to be located 'behind' the VPN tunnel are in the same subnet!</p></div><div id="comment-23696-info" class="comment-info"><span class="comment-age">(11 Aug '13, 11:30)</span> Kurt Knochner ♦</div></div><span id="23697"></span><div id="comment-23697" class="comment not_top_scorer"><div id="post-23697-score" class="comment-score"></div><div class="comment-text"><p>I had to post this as an answer because I can't post more than 2500 characters if I post a comment. I censored a couple lines just in case they had sensitive information in them, but not much. This is the client file. I will post the server file very soon (within 15 minutes). As of 5:17 P.M., I removed the information pertaining to my antivirus.</p><pre><code>Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING
  RpcSs
 [svchost.exe]
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING
 Can not obtain ownership information
  TCP    0.0.0.0:5357           0.0.0.0:0              LISTENING
 Can not obtain ownership information
  TCP    0.0.0.0:9930           0.0.0.0:0              LISTENING
 [vpnclient_x64.exe]
  TCP    0.0.0.0:9983           0.0.0.0:0              LISTENING
 [vpnclient_x64.exe]
  TCP    0.0.0.0:12025          0.0.0.0:0              LISTENING
 [nvstreamsvc.exe]
  TCP    0.0.0.0:49152          0.0.0.0:0              LISTENING

 [wininit.exe]
  TCP    0.0.0.0:49153          0.0.0.0:0              LISTENING

  eventlog
 [svchost.exe]
  TCP    0.0.0.0:49154          0.0.0.0:0              LISTENING

  Schedule
 [svchost.exe]
  TCP    0.0.0.0:49155          0.0.0.0:0              LISTENING

 [services.exe]
  TCP    0.0.0.0:49156          0.0.0.0:0              LISTENING

  PolicyAgent
 [svchost.exe]
  TCP    0.0.0.0:49158          0.0.0.0:0              LISTENING

 [lsass.exe]
  TCP    127.0.0.1:2559         0.0.0.0:0              LISTENING

 [daemonu.exe]
  TCP    127.0.0.1:2559         127.0.0.1:52380        TIME_WAIT

  TCP    127.0.0.1:5905         127.0.0.1:49179        ESTABLISHED

 [nvstreamsvc.exe]
  TCP    127.0.0.1:5905         127.0.0.1:49180        ESTABLISHED

 [nvstreamsvc.exe]
  TCP    127.0.0.1:5905         127.0.0.1:49181        ESTABLISHED

 [nvstreamsvc.exe]
  TCP    127.0.0.1:5905         127.0.0.1:49182        ESTABLISHED

 [nvstreamsvc.exe]
  TCP    127.0.0.1:5905         127.0.0.1:49183        ESTABLISHED

 [nvstreamsvc.exe]
  TCP    127.0.0.1:9930         127.0.0.1:49215        ESTABLISHED

 [vpnclient_x64.exe]
  TCP    127.0.0.1:9930         127.0.0.1:49217        ESTABLISHED

 [vpnclient_x64.exe]
  TCP    127.0.0.1:12025        0.0.0.0:0              LISTENING

 [AvastSvc.exe]
  TCP    127.0.0.1:12080        0.0.0.0:0              LISTENING

 [AvastSvc.exe]
  TCP    127.0.0.1:12110        0.0.0.0:0              LISTENING

 [AvastSvc.exe]
  TCP    127.0.0.1:12119        0.0.0.0:0              LISTENING

 [nvstreamsvc.exe]
  TCP    127.0.0.1:49180        127.0.0.1:5905         ESTABLISHED

 [nvstreamsvc.exe]
  TCP    127.0.0.1:49181        127.0.0.1:5905         ESTABLISHED

 [nvstreamsvc.exe]
  TCP    127.0.0.1:49182        127.0.0.1:5905         ESTABLISHED

 [nvstreamsvc.exe]
  TCP    127.0.0.1:49183        127.0.0.1:5905         ESTABLISHED

 [nvstreamsvc.exe]
  TCP    127.0.0.1:49215        127.0.0.1:9930         ESTABLISHED

 [vpncmgr_x64.exe]
  TCP    127.0.0.1:49217        127.0.0.1:9930         ESTABLISHED

 [vpncmgr_x64.exe]
  TCP    127.0.0.1:52441        127.0.0.1:47986        SYN_SENT

 [nvstreamsvc.exe]
  TCP    169.254.35.142:139     0.0.0.0:0              LISTENING
 Can not obtain ownership information
  TCP    192.168.1.134:139      0.0.0.0:0              LISTENING
 Can not obtain ownership information
  TCP    192.168.1.134:49306    173.194.43.6:80        CLOSE_WAIT

 [AvastUI.exe]
  TCP    192.168.1.134:49351    77.234.42.54:80        ESTABLISHED

 [AvastSvc.exe]
  TCP    192.168.1.134:52127    192.168.1.132:443      ESTABLISHED

 [vpnclient_x64.exe]
  TCP    192.168.1.134:52151    192.168.1.132:443      ESTABLISHED

 [vpnclient_x64.exe]
  TCP    192.168.1.134:52166    204.245.190.48:8*(Censored)      TIME_WAIT

  TCP    192.168.1.134:52288    72.233.69.4:443        TIME_WAIT

  TCP    192.168.1.134:52290    74.125.26.95:8*        TIME_WAIT

  TCP    192.168.1.134:52292    173.194.43.52:8*       TIME_WAIT

  TCP    192.168.1.134:52302    173.194.43.52:8*       TIME_WAIT

  TCP    192.168.1.134:52305    146.82.2.59:8*         TIME_WAIT

  TCP    192.168.1.134:52307    74.125.26.95:8*        TIME_WAIT

  TCP    192.168.1.134:52313    74.125.226.193:8*      TIME_WAIT

  TCP    192.168.1.134:52317    173.194.43.52:8*       TIME_WAIT

  TCP    192.168.1.134:52319    173.194.43.52:8*       TIME_WAIT

  TCP    192.168.1.134:52320    173.194.43.52:8*       TIME_WAIT

  TCP    192.168.1.134:52321    173.194.43.52:8*       TIME_WAIT

  TCP    192.168.1.134:52391    192.168.1.109:2869     TIME_WAIT

  TCP    192.168.1.134:52392    192.168.1.109:2869     ESTABLISHED

 [wmpnetwk.exe]
  TCP    [::]:135               [::]:0                 LISTENING
  RpcSs
 [svchost.exe]
  TCP    [::]:445               [::]:0                 LISTENING
 Can not obtain ownership information
  TCP    [::]:5357              [::]:0                 LISTENING
 Can not obtain ownership information
  TCP    [::]:9983              [::]:0                 LISTENING
 [vpnclient_x64.exe]
  TCP    [::]:49152             [::]:0                 LISTENING
 [wininit.exe]
  TCP    [::]:49153             [::]:0                 LISTENING
  eventlog
 [svchost.exe]
  TCP    [::]:49154             [::]:0                 LISTENING
  Schedule
 [svchost.exe]
  TCP    [::]:49155             [::]:0                 LISTENING
 [services.exe]
  TCP    [::]:49156             [::]:0                 LISTENING
  PolicyAgent
 [svchost.exe]
  TCP    [::]:49158             [::]:0                 LISTENING
 [lsass.exe]
  TCP    [::1]:12025            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12110            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12119            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12143            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12465            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12563            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12993            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12995            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:27275            [::]:0                 LISTENING
 [AvastSvc.exe]
  UDP    0.0.0.0:68             *:*                    
  Dhcp
 [svchost.exe]
  UDP    0.0.0.0:427            *:*                    
  HPSLPSVC
 [svchost.exe]
  UDP    0.0.0.0:500            *:*                    
  IKEEXT
 [svchost.exe]
  UDP    0.0.0.0:889            *:*                    
 [spd.exe]
  UDP    0.0.0.0:3702           *:*                    
  EventSystem
 [svchost.exe]
  UDP    0.0.0.0:3702           *:*                    
  FDResPub
 [svchost.exe]
  UDP    0.0.0.0:3702           *:*                    
  FDResPub
 [svchost.exe]
  UDP    0.0.0.0:3702           *:*                    
  EventSystem
 [svchost.exe]
  UDP    0.0.0.0:4500           *:*                    
  IKEEXT
 [svchost.exe]
  UDP    0.0.0.0:5355           *:*                    
  Dnscache
 [svchost.exe]
  UDP    0.0.0.0:49152          *:*                    
 [vpnclient_x64.exe]
  UDP    0.0.0.0:51818          *:*                    
  FDResPub
 [svchost.exe]
  UDP    0.0.0.0:52953          *:*                    
 [spd.exe]
  UDP    0.0.0.0:59670          *:*                    
 [vpnclient_x64.exe]
  UDP    0.0.0.0:59671          *:*                    
 [vpncmgr_x64.exe]
  UDP    0.0.0.0:63365          *:*                    
  EventSystem
 [svchost.exe]
  UDP    127.0.0.1:1900         *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    127.0.0.1:44301        *:*                    
 [PnkBstrA.exe]
  UDP    127.0.0.1:48000        *:*                    
 [daemonu.exe]
  UDP    127.0.0.1:48001        *:*                    
 [nvtray.exe]
  UDP    127.0.0.1:48002        *:*                    
 [nvstreamsvc.exe]
  UDP    127.0.0.1:48003        *:*                    
 [NvTmru.exe]
  UDP    127.0.0.1:49200        *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    169.254.35.142:137     *:*                    
 Can not obtain ownership information
  UDP    169.254.35.142:138     *:*                    
 Can not obtain ownership information
  UDP    169.254.35.142:427     *:*                    
  HPSLPSVC
 [svchost.exe]
  UDP    169.254.35.142:1900    *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    169.254.35.142:49198   *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    192.168.1.134:137      *:*                    
 Can not obtain ownership information
  UDP    192.168.1.134:138      *:*                    
 Can not obtain ownership information
  UDP    192.168.1.134:427      *:*                    
  HPSLPSVC
 [svchost.exe]
  UDP    192.168.1.134:1900     *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    192.168.1.134:49199    *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    192.168.1.134:49842    *:*                    
 [vpnclient_x64.exe]
  UDP    [::]:500               *:*                    
  IKEEXT
 [svchost.exe]
  UDP    [::]:3702              *:*                    
  FDResPub
 [svchost.exe]
  UDP    [::]:3702              *:*                    
  EventSystem
 [svchost.exe]
  UDP    [::]:3702              *:*                    
  FDResPub
 [svchost.exe]
  UDP    [::]:3702              *:*                    
  EventSystem
 [svchost.exe]
  UDP    [::]:4500              *:*                    
  IKEEXT
 [svchost.exe]
  UDP    [::]:5355              *:*                    
  Dnscache
 [svchost.exe]
  UDP    [::]:51819             *:*                    
  FDResPub
 [svchost.exe]
  UDP    [::]:63366             *:*                    
  EventSystem
 [svchost.exe]
  UDP    [::1]:1900             *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    [::1]:49197            *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    [fe80::60:631c:e3e4:238e%1044]:1900  *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    [fe80::60:631c:e3e4:238e%1044]:49195  *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    [fe80::a8a1:be59:9656:32b8%11]:546  *:*                    
  Dhcp
 [svchost.exe]
  UDP    [fe80::a8a1:be59:9656:32b8%11]:1900  *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    [fe80::a8a1:be59:9656:32b8%11]:49196  *:*                    
  SSDPSRV
 [svchost.exe]</code></pre></div><div id="comment-23697-info" class="comment-info"><span class="comment-age">(11 Aug '13, 14:05)</span> MastaChief11</div></div><span id="23698"></span><div id="comment-23698" class="comment not_top_scorer"><div id="post-23698-score" class="comment-score"></div><div class="comment-text"><p>this is the output of the client. Can you please add the output of the server as well? I'm still trying to find port 40000 to figure out if that belongs to the VPN.</p><p>BTW: What is the IP subnet in the office? If it is also 192.168.1.0/24, then you won't be able to test anything at your home, because the client and the systems that are supposed to be located 'behind' the VPN tunnel are in the same subnet!</p></div><div id="comment-23698-info" class="comment-info"><span class="comment-age">(11 Aug '13, 14:15)</span> Kurt Knochner ♦</div></div><span id="23699"></span><div id="comment-23699" class="comment not_top_scorer"><div id="post-23699-score" class="comment-score"></div><div class="comment-text"><p>This is the server netstat output. .132 is the server, and .134 is the client. I found port 40000, and I highlighted and italicized it to make it easier to find (it's 2/3 of the way down). I won't be able to get the subnet at this moment, but I will find out when I can get there.</p><pre><code>Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING
  RpcSs
 [svchost.exe]
  TCP    0.0.0.0:443            0.0.0.0:0              LISTENING
 [vpnserver_x64.exe]
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING
 Can not obtain ownership information
  TCP    0.0.0.0:992            0.0.0.0:0              LISTENING
 [vpnserver_x64.exe]
  TCP    0.0.0.0:1194           0.0.0.0:0              LISTENING
 [vpnserver_x64.exe]
  TCP    0.0.0.0:2869           0.0.0.0:0              LISTENING
 Can not obtain ownership information
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING
  CryptSvc
 [svchost.exe]
  TCP    0.0.0.0:5555           0.0.0.0:0              LISTENING
 [vpnserver_x64.exe]
  TCP    0.0.0.0:12025          0.0.0.0:0              LISTENING
 [wininit.exe]
  TCP    0.0.0.0:49153          0.0.0.0:0              LISTENING
  eventlog
 [svchost.exe]
  TCP    0.0.0.0:49154          0.0.0.0:0              LISTENING
  Schedule
 [svchost.exe]
  TCP    0.0.0.0:49155          0.0.0.0:0              LISTENING
 [services.exe]
  TCP    0.0.0.0:49156          0.0.0.0:0              LISTENING
  PolicyAgent
 [svchost.exe]
  TCP    0.0.0.0:49160          0.0.0.0:0              LISTENING
 [lsass.exe]
  TCP    0.0.0.0:65494          0.0.0.0:0              LISTENING
 [vpnserver_x64.exe]
  TCP    127.0.0.1:12025        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:12080        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:12080        127.0.0.1:51530        TIME_WAIT
  TCP    127.0.0.1:12080        127.0.0.1:51550        TIME_WAIT
  TCP    127.0.0.1:12080        127.0.0.1:51554        TIME_WAIT
  TCP    127.0.0.1:12110        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:12119        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:12143        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:12465        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:12563        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:12993        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:12995        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:27275        0.0.0.0:0              LISTENING
 [AvastSvc.exe]
  TCP    127.0.0.1:49158        0.0.0.0:0              LISTENING
 [THXAudNB.exe]
  TCP    127.0.0.1:51565        127.0.0.1:12080        TIME_WAIT
  TCP    192.168.1.132:139      0.0.0.0:0              LISTENING
 Can not obtain ownership information
  TCP    192.168.1.132:443      192.168.1.134:52127    ESTABLISHED
 [vpnserver_x64.exe]
  TCP    192.168.1.132:443      192.168.1.134:52151    ESTABLISHED
 [vpnserver_x64.exe]
  TCP    192.168.1.132:2869     192.168.1.1:55462      TIME_WAIT
  TCP    192.168.1.132:2869     192.168.1.1:55463      TIME_WAIT
  TCP    192.168.1.132:2869     192.168.1.1:55464      TIME_WAIT
  TCP    192.168.1.132:49219    168.62.204.227:443     ESTABLISHED
 [vpnserver_x64.exe]
  TCP    192.168.1.132:49308    173.194.43.8:80        CLOSE_WAIT
 [AvastUI.exe]
  TCP    192.168.1.132:49349    77.234.43.53:80        ESTABLISHED
 [AvastSvc.exe]
  TCP    192.168.1.132:51494    192.168.1.1:47010      TIME_WAIT
  TCP    192.168.1.132:51495    192.168.1.1:47010      TIME_WAIT
  TCP    192.168.1.132:51534    69.90.210.72:443       TIME_WAIT
  TCP    192.168.1.132:51536    69.90.210.72:443       TIME_WAIT
  TCP    192.168.1.132:51537    192.168.1.1:47010      TIME_WAIT
  TCP    192.168.1.132:51538    192.168.1.1:47010      TIME_WAIT
  TCP    192.168.1.132:51541    69.90.210.72:443       TIME_WAIT
  TCP    192.168.1.132:51543    69.90.210.72:443       TIME_WAIT
  TCP    192.168.1.132:51544    69.90.210.72:443       TIME_WAIT
  TCP    192.168.1.132:51546    69.90.210.72:443       TIME_WAIT
  TCP    192.168.1.132:51548    69.90.210.15:443       TIME_WAIT
  TCP    192.168.1.132:51553    64.71.175.126:443      TIME_WAIT
  TCP    192.168.1.132:51561    64.71.175.126:443      TIME_WAIT
  TCP    192.168.1.132:51562    64.71.175.126:443      TIME_WAIT
  TCP    192.168.1.132:51567    64.71.175.133:443      TIME_WAIT
  TCP    192.168.1.132:51568    64.71.175.133:443      TIME_WAIT
  TCP    192.168.1.132:51569    64.71.175.133:443      TIME_WAIT
  TCP    192.168.1.132:51570    130.158.6.77:80        TIME_WAIT
  TCP    192.168.1.132:51571    192.168.1.1:47010      TIME_WAIT
  TCP    192.168.1.132:51572    192.168.1.1:47010      TIME_WAIT
  TCP    [::]:135               [::]:0                 LISTENING
  RpcSs
 [svchost.exe]
  TCP    [::]:443               [::]:0                 LISTENING
 [vpnserver_x64.exe]
  TCP    [::]:445               [::]:0                 LISTENING
 Can not obtain ownership information
  TCP    [::]:992               [::]:0                 LISTENING
 [vpnserver_x64.exe]
  TCP    [::]:1194              [::]:0                 LISTENING
 [vpnserver_x64.exe]
  TCP    [::]:2869              [::]:0                 LISTENING
 Can not obtain ownership information
  TCP    [::]:3389              [::]:0                 LISTENING
  CryptSvc
 [svchost.exe]
  TCP    [::]:5555              [::]:0                 LISTENING
 [vpnserver_x64.exe]
  TCP    [::]:49152             [::]:0                 LISTENING
 [wininit.exe]
  TCP    [::]:49153             [::]:0                 LISTENING
  eventlog
 [svchost.exe]
  TCP    [::]:49154             [::]:0                 LISTENING
  Schedule
 [svchost.exe]
  TCP    [::]:49155             [::]:0                 LISTENING
 [services.exe]
  TCP    [::]:49156             [::]:0                 LISTENING
  PolicyAgent
 [svchost.exe]
  TCP    [::]:49160             [::]:0                 LISTENING
 [lsass.exe]
  TCP    [::]:65494             [::]:0                 LISTENING
 [vpnserver_x64.exe]
  TCP    [::1]:12025            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12110            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12119            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12143            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12465            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12563            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12993            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:12995            [::]:0                 LISTENING
 [AvastSvc.exe]
  TCP    [::1]:27275            [::]:0                 LISTENING
 [AvastSvc.exe]
  UDP    0.0.0.0:500            *:*                    
 [vpnserver_x64.exe]
  UDP    0.0.0.0:889            *:*                    
 [spd.exe]
  UDP    0.0.0.0:1194           *:*                    
 [vpnserver_x64.exe]
  UDP    0.0.0.0:3544           *:*                    
  iphlpsvc
 [svchost.exe]
  UDP    0.0.0.0:4500           *:*                    
 [vpnserver_x64.exe]
  UDP    0.0.0.0:5355           *:*                    
  Dnscache
 [svchost.exe]
  UDP    0.0.0.0:7221           *:*                    
 [vpnserver_x64.exe]
  UDP    0.0.0.0:49152          *:*                    
 [vpnserver_x64.exe]
  UDP    0.0.0.0:49153          *:*                    
 [vpnserver_x64.exe]
  UDP    0.0.0.0:49857          *:*                    
 [vpnserver_x64.exe]
  UDP    0.0.0.0:53080          *:*                    
 [spd.exe]
  UDP    0.0.0.0:64343          *:*                    
 [vpnsmgr_x64.exe]
  UDP    127.0.0.1:500          *:*                    
 [vpnserver_x64.exe]
  UDP    127.0.0.1:1194         *:*                    
 [vpnserver_x64.exe]
  UDP    127.0.0.1:1900         *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    127.0.0.1:4500         *:*                    
 [vpnserver_x64.exe]
  UDP    127.0.0.1:60885        *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    192.168.1.132:137      *:*                    
 Can not obtain ownership information
  UDP    192.168.1.132:138      *:*                    
 Can not obtain ownership information
  UDP    192.168.1.132:500      *:*                    
 [vpnserver_x64.exe]
  UDP    192.168.1.132:1194     *:*                    
 [vpnserver_x64.exe]
  UDP    192.168.1.132:1900     *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    192.168.1.132:4500     *:*                    
 ***[vpnserver_x64.exe]
  UDP    192.168.1.132:40000    *:****                    
 [vpnserver_x64.exe]
  UDP    192.168.1.132:60112    *:*                    
  iphlpsvc
 [svchost.exe]
  UDP    192.168.1.132:60884    *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    [::]:500               *:*                    
 [vpnserver_x64.exe]
  UDP    [::]:1194              *:*                    
 [vpnserver_x64.exe]
  UDP    [::]:4500              *:*                    
 [vpnserver_x64.exe]
  UDP    [::]:5355              *:*                    
  Dnscache
 [svchost.exe]
  UDP    [::1]:500              *:*                    
 [vpnserver_x64.exe]
  UDP    [::1]:1194             *:*                    
 [vpnserver_x64.exe]
  UDP    [::1]:1900             *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    [::1]:4500             *:*                    
 [vpnserver_x64.exe]
  UDP    [::1]:60883            *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    [2001:0:5ef5:79fd:15:152f:cd62:5475]:500  *:*                    
 [vpnserver_x64.exe]
  UDP    [2001:0:5ef5:79fd:15:152f:cd62:5475]:1194  *:*                    
 [vpnserver_x64.exe]
  UDP    [2001:0:5ef5:79fd:15:152f:cd62:5475]:4500  *:*                    
 [vpnserver_x64.exe]
  UDP    [fe80::15:152f:cd62:5475%13]:500  *:*                    
 [vpnserver_x64.exe]
  UDP    [fe80::15:152f:cd62:5475%13]:1194  *:*                    
 [vpnserver_x64.exe]
  UDP    [fe80::15:152f:cd62:5475%13]:4500  *:*                    
 [vpnserver_x64.exe]
  UDP    [fe80::a08b:eff1:2a94:661b%12]:500  *:*                    
 [vpnserver_x64.exe]
  UDP    [fe80::a08b:eff1:2a94:661b%12]:546  *:*                    
  Dhcp
 [svchost.exe]
  UDP    [fe80::a08b:eff1:2a94:661b%12]:1194  *:*                    
 [vpnserver_x64.exe]
  UDP    [fe80::a08b:eff1:2a94:661b%12]:1900  *:*                    
  SSDPSRV
 [svchost.exe]
  UDP    [fe80::a08b:eff1:2a94:661b%12]:4500  *:*                    
 [vpnserver_x64.exe]
  UDP    [fe80::a08b:eff1:2a94:661b%12]:60882  *:*                    
  SSDPSRV
 [svchost.exe]</code></pre></div><div id="comment-23699-info" class="comment-info"><span class="comment-age">(11 Aug '13, 14:28)</span> MastaChief11</div></div><span id="23700"></span><div id="comment-23700" class="comment"><div id="post-23700-score" class="comment-score">1</div><div class="comment-text"><p>As you can see, port udp/40000 also belongs to the VPN solution.</p><pre><code> UDP    192.168.1.132:40000    *:****                    
 [vpnserver_x64.exe]</code></pre><p>If that is however VPN traffic (encrypted payload) or some form of status/management protocol, I can't tell you.</p><p>To sum it up. It looks like your VPN solution works (kind of). If you move the solution to the office, you may have to open more that just port tcp/443 on your office firewall to make the VPN work (port udp/40000 seems to be involved as well). However, that is 'a bit' off topic for this site and you better ask that question in the forum of the vendor.</p></div><div id="comment-23700-info" class="comment-info"><span class="comment-age">(11 Aug '13, 14:42)</span> Kurt Knochner ♦</div></div><span id="23703"></span><div id="comment-23703" class="comment not_top_scorer"><div id="post-23703-score" class="comment-score"></div><div class="comment-text"><p>As long as it is at my home, the ports won't need to be opened in order for the VPN to work properly (although I do have two of the ports that the VPN listens on open), and connection to be encrypted, correct?</p></div><div id="comment-23703-info" class="comment-info"><span class="comment-age">(11 Aug '13, 18:35)</span> MastaChief11</div></div><span id="23705"></span><div id="comment-23705" class="comment"><div id="post-23705-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>As long as it is at my home, the ports won't need to be opened in order for the VPN to work properly</p></blockquote><p>Yes, as there is no firewall between the client and the server, except the Windows 7 firewall, which is (most certainly) automatically configured (during installation of the VPN software) to make the VPN work.</p></div><div id="comment-23705-info" class="comment-info"><span class="comment-age">(12 Aug '13, 05:46)</span> Kurt Knochner ♦</div></div><span id="23710"></span><div id="comment-23710" class="comment not_top_scorer"><div id="post-23710-score" class="comment-score"></div><div class="comment-text"><p>Would I be correct to say that the VPN works, but there is no way to be sure that the packets are encrypted, but it is very likely that they are encrypted?</p></div><div id="comment-23710-info" class="comment-info"><span class="comment-age">(12 Aug '13, 08:07)</span> MastaChief11</div></div><span id="23720"></span><div id="comment-23720" class="comment not_top_scorer"><div id="post-23720-score" class="comment-score"></div><div class="comment-text"><p>sounds reasonable.</p></div><div id="comment-23720-info" class="comment-info"><span class="comment-age">(12 Aug '13, 14:19)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-23631" class="comment-tools"><span class="comments-showing"> showing 5 of 18 </span> <a href="#" class="show-all-comments-link">show 13 more comments</a></div><div class="clear"></div><div id="comment-23631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24008"></span>

<div id="answer-container-24008" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24008-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Watch the stream and look for negotiation using defined encryption protocols. If you know the data is compressed with bzip2, look for the strings 0x314159265359 and 0x177245385090. Unless headers are totally stripped out, they'll appear once for every block. You can take a guess at whether data is encrypted by following the stream and checking for entropy. The more entropy per bit, the more likely you're seeing encryption. This unfortunately applies to compression as well.</p><p>I would say that you can discern known encrypted, or known unencrypted. Differentiating encryption or compression would take a while and involve more complex code without header information for magic strings (like above) to give it away.</p><p>Regards <a href="http://www.education4world.net/">http://www.education4world.net/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/a53fb462484f0b68b7db43d5a7cec873?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ali%20Hassan&#39;s gravatar image" /><p>Ali Hassan<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ali Hassan has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-24008" class="comments-container"></div><div id="comment-tools-24008" class="comment-tools"></div><div class="clear"></div><div id="comment-24008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24009"></span>

<div id="answer-container-24009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24009-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wirelessly posted (Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16)</p><p>Setup an access point on your mac, connect your phone. Ensure all your webpages on your phone are using HTTPS, and not HTTP.</p><p>Install a packet analyzer like Packet Peeper, Cocoa, Or Wireshark on your mac, and take samples while you transmit data with the Phone.</p><p>Take a look at the packets and their headers, all should be unreadable.</p><p>Regards <a href="http://www.virtualians.pk/">http://www.virtualians.pk/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/7aebe1734e86efdbc5c65cc0974e0954?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irfan%20Khan&#39;s gravatar image" /><p>Irfan Khan<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irfan Khan has no accepted answers">0%</span></p></div></div><div id="comments-container-24009" class="comments-container"><span id="24215"></span><div id="comment-24215" class="comment"><div id="post-24215-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help, Irfan, but I don't use Macs. Your suggestion is still appreciated though.</p></div><div id="comment-24215-info" class="comment-info"><span class="comment-age">(30 Aug '13, 15:44)</span> MastaChief11</div></div></div><div id="comment-tools-24009" class="comment-tools"></div><div class="clear"></div><div id="comment-24009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

