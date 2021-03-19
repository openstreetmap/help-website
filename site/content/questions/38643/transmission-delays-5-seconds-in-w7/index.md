+++
type = "question"
title = "Transmission delays 5 seconds in W7"
description = '''Dear All, we are using a 64 bit W7, PC. It communicates with a PLC in a production plant.  Sometimes our outgoing message is delayed 5 seconds, causing alarms and production comes to stop.  How do we change the setting so that our PC re-transmitts not after waiting 5,000 ms but 500 ms? Please advice...'''
date = "2014-12-20T10:02:00Z"
lastmod = "2015-01-08T09:17:00Z"
weight = 38643
keywords = [ "delay", "retransmitting", "5", "seconds" ]
aliases = [ "/questions/38643" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Transmission delays 5 seconds in W7](/questions/38643/transmission-delays-5-seconds-in-w7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38643-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All,</p><p>we are using a 64 bit W7, PC. It communicates with a PLC in a production plant. Sometimes our outgoing message is delayed 5 seconds, causing alarms and production comes to stop. How do we change the setting so that our PC re-transmitts not after waiting 5,000 ms but 500 ms?</p><p>Please advice, Knocking</p></div><div id="question-tags" class="tags-container tags">delay retransmitting 5 seconds</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '14, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/eb0281207fb96b2b78668f8efe316a38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Knocking&#39;s gravatar image" /><p>Knocking<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Knocking has no accepted answers">0%</span></p></div></div><div id="comments-container-38643" class="comments-container"><span id="38645"></span><div id="comment-38645" class="comment"><div id="post-38645-score" class="comment-score"></div><div class="comment-text"><p>This is difficult to answer, because the reason for the delay for the outgoing message is unclear. Do you have a capture of this happening that you could share?</p></div><div id="comment-38645-info" class="comment-info"><span class="comment-age">(20 Dec '14, 10:17)</span> Jasper ♦♦</div></div><span id="38646"></span><div id="comment-38646" class="comment"><div id="post-38646-score" class="comment-score"></div><div class="comment-text"><p><a href="http://support.microsoft.com/kb/2861819">KB2861819</a> adresses the 5 second TCP delay in Windows 7. It's not 100% guaranteed, but it fixed 4 differnt delay problems for me.</p></div><div id="comment-38646-info" class="comment-info"><span class="comment-age">(20 Dec '14, 14:27)</span> DarrenWright</div></div><span id="38650"></span><div id="comment-38650" class="comment"><div id="post-38650-score" class="comment-score"></div><div class="comment-text"><p>Hello again, and thank you for showing interest in this problem.</p><p>I have studied the WS logging and can send it to you along with the PC log showing what and when entries are made in our C# code.</p><p>I think one can conclude that it is the C# code which does not read the incoming message immediately but waits. When it is read the answer is immediate which can be confirmed also in WS logging - outgoing message.</p><p>I guess the question has come to why our C# code do not read what is available?</p><p>I am happy to send log files (approx 550 kb), if you only can tell me how or where?</p><p>Best regards Knocking</p></div><div id="comment-38650-info" class="comment-info"><span class="comment-age">(21 Dec '14, 03:49)</span> Knocking</div></div><span id="38651"></span><div id="comment-38651" class="comment"><div id="post-38651-score" class="comment-score"></div><div class="comment-text"><p>Also, it seems as if the problems are less when we run the software as Administrator. (the windows firewall is turned off.)</p><p>Best regards Knocking</p></div><div id="comment-38651-info" class="comment-info"><span class="comment-age">(21 Dec '14, 03:52)</span> Knocking</div></div><span id="38738"></span><div id="comment-38738" class="comment"><div id="post-38738-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am happy to send log files (approx 550 kb), if you only can tell me how or where?</p></blockquote><p>upload them on google drive, dropbox or cloudshark.org and then post the link here.</p></div><div id="comment-38738-info" class="comment-info"><span class="comment-age">(27 Dec '14, 08:57)</span> Kurt Knochner ♦</div></div><span id="38941"></span><div id="comment-38941" class="comment not_top_scorer"><div id="post-38941-score" class="comment-score"></div><div class="comment-text"><p>Dear All,</p><p>there are 3 files:</p><ol><li>Shark file.</li><li>Log file from our software</li><li>Excel document to assist in comparing.</li></ol><p>Thank you for all help!</p><p><a href="https://drive.google.com/folderview?id=0B-2RoGZWzudQRGlLSmlTU0pNb2s&amp;usp=sharing">https://drive.google.com/folderview?id=0B-2RoGZWzudQRGlLSmlTU0pNb2s&amp;usp=sharing</a></p></div><div id="comment-38941-info" class="comment-info"><span class="comment-age">(08 Jan '15, 03:17)</span> Knocking</div></div><span id="38944"></span><div id="comment-38944" class="comment not_top_scorer"><div id="post-38944-score" class="comment-score"></div><div class="comment-text"><p>Please add more details where in the capture file (frame number!) you see the 5 second delay.</p></div><div id="comment-38944-info" class="comment-info"><span class="comment-age">(08 Jan '15, 04:40)</span> Kurt Knochner ♦</div></div><span id="38964"></span><div id="comment-38964" class="comment not_top_scorer"><div id="post-38964-score" class="comment-score"></div><div class="comment-text"><p>Dear All,</p><p>please see the following description/comments:</p><p>On row no 2188 a query was received on board 7087. On the next no (2189) the data had been processed by our software and response was sent. Total processing time was approximately 10 ms.</p><p>For the next board (7088) the situation is different. On row no 2192 the query was received by WS but the response was sent approximately 5032 ms later, on row 2205. In the log for the software we can see that the data was received and response sent within a few ms. Also, this timestamp correlates to the response in WS. However, our software did not start the processing after a delay of approx 5010 ms. So, the query was detected by WS and detected by our software 5010 ms later. (Immediately the software processed and sent the response, which also is confirmed in WS.)</p><p>Of course this pattern occurs regularly (see row no 2501, 2502, 2503, 2524) . The delay in our logging is always 5000 ms (+5 to +15 ms).</p><p>We find it very strange that when there is a delay, it is always 5000 ms. Of course, there could be a capacity problem on our CPU but the delay should differ, which it doesn´t.</p><p>Anybody who can advise? Any help appreciated.</p><p>Knocking</p></div><div id="comment-38964-info" class="comment-info"><span class="comment-age">(08 Jan '15, 08:49)</span> Knocking</div></div></div><div id="comment-tools-38643" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-38643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38968"></span>

<div id="answer-container-38968" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38968-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>For the next board (7088) the situation is different.</p></blockquote><p>If you set a filter for that TCP stream, you will see the following.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Q38643_screenshot.png" alt="alt text" /></p><p><strong>Frame 2192</strong>: Client (.6) sends request.<br />
<strong>Frame 2194</strong>: ACK for that frame was received, meaning the server (.71) TCP/IP stack has seen the request and confirmed it with an ACK.<br />
<strong>Frame 2201</strong>: The <strong>client</strong> closes the connection after 5 seconds, maybe due to a timeout.<br />
<strong>Frame 2202</strong>: The <strong>FIN</strong> was ACKed<br />
<strong>Frame 2205</strong>: The <strong>server</strong> sends it's response. It's unclear why this happens!!</p><p>So,</p><ul><li>either frame 2192 did not really reach the server. In that case some kind of TCP proxy must be between the client/server - which is rather unlikely in this case</li><li>or there is a bug in the TCP/IP stack of the server</li><li>or there is a bug in the server <strong>software</strong> (which is what I believe).</li></ul><p>You won't be able to figure this out with the help of Wireshark. What you probably can do:</p><p>Capture in front of the client AND server (switch mirror port) to verify what we are seeing on one capture file, currently taken at the client. If you see the same behaviour, the next step would be debugging of the server application and/or the TCP/IP stack of the server.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '15, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '15, 09:23</p></div></div><div id="comments-container-38968" class="comments-container"><span id="38969"></span><div id="comment-38969" class="comment"><div id="post-38969-score" class="comment-score"></div><div class="comment-text"><p>It's not a server, rather it's a PLC. Good luck trying to debug that. Some PLC's have a separate comms processor to handle things such as Modbus so there shouldn't be any delays caused by the real-time process loop in the PLC, but others do rely on the main process loop to handle comms.</p><p>It may be that the PLC does just take 5 seconds to respond sometimes (which is very slow), so increasing the client timeout would help. I would try increasing the timeout in the client software say to 7 seconds.</p><p>It's also possible that the client FIN wakes the PLC up and causes it to send the response, in which case increasing the client timeout won't help.</p><p>What make is the PLC?</p></div><div id="comment-38969-info" class="comment-info"><span class="comment-age">(08 Jan '15, 09:38)</span> grahamb ♦</div></div></div><div id="comment-tools-38968" class="comment-tools"></div><div class="clear"></div><div id="comment-38968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

