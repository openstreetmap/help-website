+++
type = "question"
title = "Capture traffic from printer to smtp relay"
description = '''Hi all, I&#x27;ve been searching online for some help to this, but so far I haven&#x27;t found an answer (or at least I have not recognized the answer). I have a MFP (mock IP 192.168.0.20) and a SMTP relay which is setup on our DC/print server (mock IP 192.168.0.10). I&#x27;ve installed wireshark and winpcap on th...'''
date = "2013-09-13T06:53:00Z"
lastmod = "2013-09-14T04:27:00Z"
weight = 24645
keywords = [ "mfp", "printer", "smtp", "relay" ]
aliases = [ "/questions/24645" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capture traffic from printer to smtp relay](/questions/24645/capture-traffic-from-printer-to-smtp-relay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24645-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I've been searching online for some help to this, but so far I haven't found an answer (or at least I have not recognized the answer).</p><p>I have a MFP (mock IP 192.168.0.20) and a SMTP relay which is setup on our DC/print server (mock IP 192.168.0.10). I've installed wireshark and winpcap on the DC/print server.</p><p>I'm trying to configure the MFP for scan to email using the SMTP relay on the DC/print server which is pointing to a Office 365 SMTP server.</p><p>When a scan to email job is started from the printer, I get a connection error message (it is not descriptive at all. Just "error connecting".) I am not sure if the job is being rejected by the SMTP relay on the DC/print server or if it is being rejected by Office 365 SMTP.</p><p>I'd like to setup Wireshark to capture traffic from the MFP (192.168.0.20) to the DC/print server SMTP relay (IP 192.168.0.20). I'd consider myself a novice when it comes to Wireshark, though I'm understanding more and more as I use it.</p><p>I've googled for help as well, but I just might not have enough understanding of wireshark/packet capturing to utilize the advise/info I've found in my google searches.</p><p>Any help is greatly appreciated.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">mfp printer smtp relay</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '13, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/365ae88f9233f4317fd29928fc340cdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tkal&#39;s gravatar image" /><p>tkal<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tkal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Sep '13, 06:56</p></div></div><div id="comments-container-24645" class="comments-container"></div><div id="comment-tools-24645" class="comment-tools"></div><div class="clear"></div><div id="comment-24645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="24648"></span>

<div id="answer-container-24648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24648-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Alright, installing WinPCAP and Wireshark on a Domain Controller? I wouldn't dare to do that... :-)</p><p>Anyway, since you've already done it and it obviously didn't crash or otherwise have an impact on the server (you'd be asking other questions otherwise) you can proceed. I'd go with a capture on the network card where the MFP data is due to arrive at (the card with IP 192.168.0.10), and set a capture filter on the IP of the MFP to ignore everything that is not coming from the device. The filter would be set in the capture options of the NIC you capture on, and be something like "<code>host 192.168.0.20 and tcp port 25</code>" - without the quotation marks. That way you only get packets that arrive from your MFP and are coming in on port 25.</p><p>Two things might happen:</p><ol><li>you see no traffic at all. In that case you have set the wrong capture filter, or the traffic is never even arriving at the DC</li><li>you see SMTP packets and it is your task to interpret what is happening. If the communication to the printer looks fine you need to repeat the capture, but this time using the office 365 IP for your filter.</li></ol><p>Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Sep '13, 07:23</p></div></div><div id="comments-container-24648" class="comments-container"><span id="24656"></span><div id="comment-24656" class="comment"><div id="post-24656-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the info. Seeing the traffic come through. Now I need to wait for a user to run a scan to email test.</p><p>Much appreciated :)</p></div><div id="comment-24656-info" class="comment-info"><span class="comment-age">(13 Sep '13, 09:29)</span> tkal</div></div></div><div id="comment-tools-24648" class="comment-tools"></div><div class="clear"></div><div id="comment-24648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24651"></span>

<div id="answer-container-24651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24651-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably the MFP will be attempting to connect to the standard SMTP port which is TCP port 25, so setting a capture filter of "port 25" in Wireshark should get you the traffic, make sure you select the correct interface on the</p><p>Once you've captured the traffic, then you'll need to look at the actual SMTP conversation, however given your error message of "error connecting" it's likely that the MFP isn't able to make a connection at all. You should at least see the TCP "SYN" packets coming in from the MFP to open the connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24651" class="comments-container"></div><div id="comment-tools-24651" class="comment-tools"></div><div class="clear"></div><div id="comment-24651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24672"></span>

<div id="answer-container-24672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24672-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Just <strong>"error connecting"</strong>. I am not sure if the job is being rejected by the SMTP relay on the DC/print server or if it is being rejected by Office 365 SMTP.</p></blockquote><p>The connection error results from your local system, otherwise the error message would be different. Reason: Your mail <strong>relay</strong> works with the principle store and forward, that means it will receive the full mail from your local client and then forward it to the Office 365 server. So, if you get a "connection error" in your client log, the chances are pretty good, that it was not able to connect to port 25 on your DC/print server. As you did not explain how you setup a mail relay on that system I cannot give any advice, other than trying to telnet to port 25 on that machine and to check if it reacts at all.</p><blockquote><p>telnet 192.168.0.10 25</p></blockquote><p>If there is no telnet client on your Win 7, install it from an elevated DOS box with</p><blockquote><p>pkgmgr /iu:"TelnetClient"</p></blockquote><ol><li><p>If you don't get a connection to the SMTP server (timeout in the client), you have found the problem. Then you need to check the firewall on the DC, if it allows connections to port 25 (I doubt it).</p></li><li><p>If you do get a connection, the problem is either only related to your MFP, or somewhere else. Here only a cpature of the traffic would help.</p></li></ol><p>I tend to believe that 1.) is your problem.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '13, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24672" class="comments-container"></div><div id="comment-tools-24672" class="comment-tools"></div><div class="clear"></div><div id="comment-24672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

