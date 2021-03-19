+++
type = "question"
title = "Device can retrieve file over active FTP from one server but not another"
description = '''I am trying to get my device to retrieve a firmware upgrade over FTP from two servers. I know that the device uses active FTP but I do not have access to the source running on it so I can&#x27;t get any more details about it&#x27;s configuration. I cannot understand what&#x27;s going on with Server A below. I&#x27;ve l...'''
date = "2016-11-01T02:16:00Z"
lastmod = "2016-11-01T10:14:00Z"
weight = 56889
keywords = [ "ftp", "iis" ]
aliases = [ "/questions/56889" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Device can retrieve file over active FTP from one server but not another](/questions/56889/device-can-retrieve-file-over-active-ftp-from-one-server-but-not-another)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56889-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to get my device to retrieve a firmware upgrade over FTP from two servers. I know that the device uses active FTP but I do not have access to the source running on it so I can't get any more details about it's configuration.</p><p>I cannot understand what's going on with <em>Server A</em> below. I've linked to an anonymized trace of the packets for each server. While the two servers are running different versions of Windows and IIS, the setup on <em>Server B</em> was configured to be as close as possible to that of <em>Server A</em>.</p><p>Both servers are running in the same physical environment so there are no external firewalls getting in the way. Each server was assigned the identical static IP address during the test, although this is not clear in the traces since the data has been anonymized.</p><p><strong><em>Server A</em></strong></p><p>Windows Server 2012 R2</p><p>IIS V8.5</p><p>FTP V8.5.9600.17086</p><p>Windows firewall turned off</p><p><a href="https://www.cloudshark.org/captures/b0dc6c1a0a69">Packets</a></p><p><strong><em>Server B</em></strong></p><p>Windows 10</p><p>IIS V10</p><p>FTP V10.0.10586.0</p><p>Windows firewall turned off</p></div><div id="question-tags" class="tags-container tags">ftp iis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '16, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/6a60a54b2c92030caba2107e9758cfe6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlasdairStark&#39;s gravatar image" /><p>AlasdairStark<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlasdairStark has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Nov '16, 04:41</p></div></div><div id="comments-container-56889" class="comments-container"><span id="56890"></span><div id="comment-56890" class="comment"><div id="post-56890-score" class="comment-score"></div><div class="comment-text"><p>As you have reduced the capture size to a minimum of 66 bytes, the contents of the ftp control session is missing i your capture file =&gt; no way to find out what happened. Please capture complete frames, at least in the failed case (better in the correct one as well while transferring a file which you don't mind to be seen by the public).</p></div><div id="comment-56890-info" class="comment-info"><span class="comment-age">(01 Nov '16, 02:23)</span> sindy</div></div><span id="56893"></span><div id="comment-56893" class="comment"><div id="post-56893-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.cloudshark.org/captures/b0dc6c1a0a69">https://www.cloudshark.org/captures/b0dc6c1a0a69</a></p></div><div id="comment-56893-info" class="comment-info"><span class="comment-age">(01 Nov '16, 04:00)</span> AlasdairStark</div></div><span id="56897"></span><div id="comment-56897" class="comment"><div id="post-56897-score" class="comment-score"></div><div class="comment-text"><p>For me it seems that the Win FW is still active, as the trace is at client side and the SYN for FTPDATA didn't get a RST or SYN,ACK.</p></div><div id="comment-56897-info" class="comment-info"><span class="comment-age">(01 Nov '16, 05:35)</span> Christian_R</div></div></div><div id="comment-tools-56889" class="comment-tools"></div><div class="clear"></div><div id="comment-56889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56905"></span>

<div id="answer-container-56905" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56905-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem was that ECN is enabled by default on Windows Server 2012 and not Windows 10.</p><p>The device was not able to negotiate a data port with ECN enabled and therefore the transfer failed.</p><p>I turned ECN off with the following command:</p><pre><code>netsh interface tcp set global ecncapability=disabled</code></pre><p><a href="http://serverfault.com/questions/526377/is-ecn-explicit-congestion-notification-turned-on-by-default-on-windows-server">See this serverfault question for more info.</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/6a60a54b2c92030caba2107e9758cfe6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlasdairStark&#39;s gravatar image" /><p>AlasdairStark<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlasdairStark has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Nov '16, 02:01</p></div></div><div id="comments-container-56905" class="comments-container"><span id="56906"></span><div id="comment-56906" class="comment"><div id="post-56906-score" class="comment-score"></div><div class="comment-text"><p>Good to know that the ftp client does hold the data port only less than 15 seconds open.</p></div><div id="comment-56906-info" class="comment-info"><span class="comment-age">(01 Nov '16, 10:18)</span> Christian_R</div></div></div><div id="comment-tools-56905" class="comment-tools"></div><div class="clear"></div><div id="comment-56905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56892"></span>

<div id="answer-container-56892" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56892-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the control session, 217.196.35.149 is the TCP client, and the control session is established properly.</p><p>In the data session, the FTP server at 192.168.107.229 acts as a TCP client, but the SYN packets it sends to the FTP client are never responded.</p><p>But when you look into the parameters of the PORT command (frame 15), you'll see that the FTP client asks the FTP server to connect to a public IP address 93.186.33.66, while the FTP server sends the TCP SYN to what it can see as the remote party of the FTP control session, i.e. to 217.196.35.149.</p><p>As you say you have anonymized the original traces, you may have anonymized this one as well.</p><p>If not:</p><ul><li><p>the FTP server may ignore the IP address from the PORT command and attempt to establish the data TCP session to the remote party of the control session because it is configured to do so, or</p></li><li><p>the FTP client may have two interfaces with different addresses and send the other one by mistake or due to configuration.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56892" class="comments-container"><span id="56894"></span><div id="comment-56894" class="comment"><div id="post-56894-score" class="comment-score"></div><div class="comment-text"><p>Hey Sindy, 93.186.33.66 was the actual IP, I've updated the link on the original question to try and make that less confusing. Sorry, this is the first time I've used TraceWrangler and it's difficult to achieve the correct level of obfuscation.</p></div><div id="comment-56894-info" class="comment-info"><span class="comment-age">(01 Nov '16, 04:15)</span> AlasdairStark</div></div><span id="56896"></span><div id="comment-56896" class="comment"><div id="post-56896-score" class="comment-score"></div><div class="comment-text"><p>In that case, check the logs and settings of the firewall of the FTP client, as it probably doesn't permit incoming TCP connections on "high" ports. As you have removed the original captures, I cannot check whether the other FTP server uses a different local port as client one for the data TCP connection, which could explain why the FTP client's firewall treats the two cases differently.</p><p>As for TraceWrangler, I'm afraid it is not realistic to have all L4 and above protocols parsed for occurrence of L3 addresses and replace them in accord with those in L3 fields. FTP is "especially special" here as its PORT command transports the IP address as four ASCII-encoded decimal numbers.</p></div><div id="comment-56896-info" class="comment-info"><span class="comment-age">(01 Nov '16, 05:34)</span> sindy</div></div><span id="56909"></span><div id="comment-56909" class="comment"><div id="post-56909-score" class="comment-score"></div><div class="comment-text"><p>TraceWrangler can't parse protocols on top of TCP right now, which includes FTP, HTTP and others. So right now it will either cut everything away, or keep it intact.</p><p>Any IP address will not be modified in those protocols on top of TCP, especially (as @sindy already mentions) not ASCII representations like FTP uses, because that will mess up sequence numbers.</p></div><div id="comment-56909-info" class="comment-info"><span class="comment-age">(01 Nov '16, 10:51)</span> Jasper ♦♦</div></div></div><div id="comment-tools-56892" class="comment-tools"></div><div class="clear"></div><div id="comment-56892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

