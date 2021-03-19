+++
type = "question"
title = "Printer intermittently &#x27;drops off&#x27;  network"
description = '''Hi all, I have a network packet capture of network environment with my copier. The copier seems like drops off from the network intermittently and unable to print the files. I have to restart the machine to get it work. the workstation is 10.0.5.160 and the copier is 10.1.5.81 the link for the packe...'''
date = "2014-06-25T02:17:00Z"
lastmod = "2014-07-15T09:12:00Z"
weight = 34153
keywords = [ "drops", "network", "intermittent" ]
aliases = [ "/questions/34153" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Printer intermittently 'drops off' network](/questions/34153/printer-intermittently-drops-off-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34153-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have a network packet capture of network environment with my copier.</p><p>The copier seems like drops off from the network intermittently and unable to print the files. I have to restart the machine to get it work. the workstation is 10.0.5.160 and the copier is 10.1.5.81 the link for the packet capture, <a href="https://drive.google.com/file/d/0B-n7X77Fqu_Rc0ZaNFhpZklfeGM/edit?usp=sharing">https://drive.google.com/file/d/0B-n7X77Fqu_Rc0ZaNFhpZklfeGM/edit?usp=sharing</a></p><p>here I attached the packet capture when the problem occurred and hopefully I can get a clue what to do next.</p></div><div id="question-tags" class="tags-container tags">drops network intermittent</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '14, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/dacf8f83a9c585ca2775f22992332737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="forest79&#39;s gravatar image" /><p>forest79<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="forest79 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '14, 02:29</p></div></div><div id="comments-container-34153" class="comments-container"><span id="34158"></span><div id="comment-34158" class="comment"><div id="post-34158-score" class="comment-score">1</div><div class="comment-text"><p>Copier is advertising a zero window packets and after few second client 10.0.5.160 gives up(sent RST).Zero windows means copier asking client to stop sending any more data.printer's remaining window size continuously decreasing as it receives data faster then it can process it. At some point, the printer's receive buffer will fill, it will send a zero window, and data transfer will stop. As the printer continues printing, it will keep pulling data from the receive buffer, and when there is room for more incoming data, it will send a window update and data transfer will resume but this is not happening in your case and later on client is forcefully closing the session.</p></div><div id="comment-34158-info" class="comment-info"><span class="comment-age">(25 Jun '14, 02:53)</span> kishan pandey</div></div><span id="34394"></span><div id="comment-34394" class="comment"><div id="post-34394-score" class="comment-score"></div><div class="comment-text"><p>Hi kishhan, when you said ' As the printer continues printing, it will keep pulling data from the receive buffer, and when there is room for more incoming data, it will send a window update and data transfer will resume but this is not happening in your case' is that imply that the copier didn't send (or failed to send) an update packets to client to get more incoming data? therefore the client is forcefully shutting.</p></div><div id="comment-34394-info" class="comment-info"><span class="comment-age">(03 Jul '14, 19:41)</span> forest79</div></div><span id="34395"></span><div id="comment-34395" class="comment"><div id="post-34395-score" class="comment-score">1</div><div class="comment-text"><p>Yes, the client is forcefully shutting (for example packet 2429 is an RST to terminate the TCP session from the client toward the printer).</p><p>To illustrate, enter the filter 'tcp.stream eq 30 &amp;&amp; ip.src==10.0.5.81', then right-click on "Windows size value:x" in the packet details pane and select "apply as column".</p><p>Look at how the window value is at 17490 in packet 3358, then it gradually goes to 0 and stays there. It stays there for more than a full minute, then the client gives up and sends an RST to terminate the session.</p></div><div id="comment-34395-info" class="comment-info"><span class="comment-age">(03 Jul '14, 20:18)</span> Quadratic</div></div></div><div id="comment-tools-34153" class="comment-tools"></div><div class="clear"></div><div id="comment-34153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34669"></span>

<div id="answer-container-34669" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34669-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is not with the client but with the printer. The printer is behaving in a bad way:</p><ul><li><p>At the beginning of connections to printer TCP port 9100, the canon printer announces a receiver window of only 30 bytes. This is very low value that, depending on the connection, is increased to 17490bytes after the first data packet is received from the client. Of course, this data packet is limited to 30 bytes in TCP size. For some connections the receiver window does not increase, and a zero window is kept until the client decides to reset the connection.</p></li><li><p>if the reciever window is increased, the printer receives the file to print in different packets and the printer acknowlodges those packets but reducing its receiver window, until reaching a zero announced window as stated before. There is some problem with the printer that is not procesing correctly the data received from the client at application layer.</p></li><li><p>The client generates then zero window probes to check if there is available window from the printer, but always it obtains a 0 value. More than a minute later, the client disconnects, and this is a normal behavior because the printer has not any capacity to receive more data.</p></li></ul><p>Therefore, it seems that there is a software (or hardware) problem with the printer. You could try to revise the configuration or reset it.</p><p>Another thing, all packets in the packet trace are duplicated. Did you use a port mirror/span to capture the traffic?</p><p><a href="http://expertnetworkanalysis.naudit.es">http://expertnetworkanalysis.naudit.es</a></p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/5286158fdb9be0bd97b194bc8093b713?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naudit&#39;s gravatar image" /><p>naudit<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naudit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '14, 09:14</p></div></div><div id="comments-container-34669" class="comments-container"><span id="34839"></span><div id="comment-34839" class="comment"><div id="post-34839-score" class="comment-score"></div><div class="comment-text"><p>Hi There,</p><p>Thank you for your answer and I have feed back the issue the printer supplier.</p><p>Yes we are using the switch with mirroring port and we can't get hub to do the capturing. Just wondering is that any better way to do the capturing beside using the mirroring port?</p><p>Thank you.</p></div><div id="comment-34839-info" class="comment-info"><span class="comment-age">(22 Jul '14, 18:51)</span> forest79</div></div><span id="34843"></span><div id="comment-34843" class="comment"><div id="post-34843-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Just wondering is that any better way to do the capturing beside using the mirroring port?</p></blockquote><p>No, you just need to do the port mirroring in the right way. If you mirrored the whole VLAN, then you could have mirrored the port of the client AND the port of the printer, which creates duplicate frames. In that case, please only mirror the port where the printer is connected to the switch.</p></div><div id="comment-34843-info" class="comment-info"><span class="comment-age">(23 Jul '14, 00:56)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34669" class="comment-tools"></div><div class="clear"></div><div id="comment-34669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

