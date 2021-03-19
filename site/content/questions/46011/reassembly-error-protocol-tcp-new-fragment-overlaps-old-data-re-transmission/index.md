+++
type = "question"
title = "Reassembly error, protocol TCP: New fragment overlaps old data (re transmission?)"
description = '''Client IP - 172.17.6.20 Server IP - 10.1.1.45 Server Port - 5555 ( web service )  Client is accessing this server and after sometimes the browser gets stuck and there is no data. After doing packet captures on both ends we have seen some errors ( last section of server file ) . There is a firewall i...'''
date = "2015-09-21T05:44:00Z"
lastmod = "2015-09-28T12:56:00Z"
weight = 46011
keywords = [ "fragment", "reassembly", "error", "overlaps" ]
aliases = [ "/questions/46011" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Reassembly error, protocol TCP: New fragment overlaps old data (re transmission?)](/questions/46011/reassembly-error-protocol-tcp-new-fragment-overlaps-old-data-re-transmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46011-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Client IP - 172.17.6.20 Server IP - 10.1.1.45 Server Port - 5555 ( web service )</p><p>Client is accessing this server and after sometimes the browser gets stuck and there is no data. After doing packet captures on both ends we have seen some errors ( last section of server file ) . There is a firewall in between but I have been told that there is nothing there blocking any such thing and since the TCP session is already established I believe it isnt a firewall issue .</p><p>Tcp Stream of Client is 152 I believe and Tcp stream of server file is 4 for this data flow.</p><p><a href="https://www.cloudshark.org/captures/c361eb9e22cf">https://www.cloudshark.org/captures/c361eb9e22cf</a> ( Server-Specified-Anon) <a href="https://www.cloudshark.org/captures/7c991ea9f83d">https://www.cloudshark.org/captures/7c991ea9f83d</a> ( Client-Anon-Specified )</p><p>I have made modifications to the packet captures using Tracewrangler . The strange thing is that this issue is random , sometimes it works fine and sometimes client is unable to browse properly and upon doing captures I got this.<br />
</p><p>The errors can be seen in the last 4-5 packets in Server capture file</p></div><div id="question-tags" class="tags-container tags">fragment reassembly error overlaps</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '15, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/2e473f2fd0144f4df712c5b477167fdb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abdur%20Rehman&#39;s gravatar image" /><p>Abdur Rehman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abdur Rehman has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Sep '15, 05:46</p></div></div><div id="comments-container-46011" class="comments-container"><span id="46019"></span><div id="comment-46019" class="comment"><div id="post-46019-score" class="comment-score"></div><div class="comment-text"><p>Note: I don't see any "Reassembly error ..." when looking at either of the captures with the latest development Wireshark.</p><p>(update) or: Are those errors showing for the original capture file (before the use of Tracewrangler ?)</p><p>What version of Wireshark are you using ?</p></div><div id="comment-46019-info" class="comment-info"><span class="comment-age">(21 Sep '15, 07:38)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-46011" class="comment-tools"></div><div class="clear"></div><div id="comment-46011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46014"></span>

<div id="answer-container-46014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46014-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the connection for port 50973 &lt;---&gt; 5555 (which is the connection for the last packets in the "server" capture:</p><p>It appears that everything is OK until the server sends a packet of 2 bytes which never shows up in the client capture.</p><p>After some number of retries(and 20 secs), the server gives up.</p><p>I would have to suspect the firewall somehow.</p><p>[Update] AFAIKT most/all of the retransmissions from the client to the server shown in the captures are due to lost ACKs from the server to the client.</p><p>The other issues also seem to involve lost packets from the server to the client.</p><p>(There is also one instance in the server capture wherein some packets sent from the server were not captured).</p><p>So: there appears to be an occasional specific problem (or problems) sending (small ?) packets from the server to the client. You would need to capture directly at the input/output of the firewall to see if there's a firewall problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '15, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Sep '15, 11:31</p></div></div><div id="comments-container-46014" class="comments-container"><span id="46047"></span><div id="comment-46047" class="comment"><div id="post-46047-score" class="comment-score"></div><div class="comment-text"><p>Yes I understand that some packets which server sents to client are not being received and this might be because of some network device making issues.</p><p>Here is a image of my wireshark which shows reassembly error , when i used tool to anonymous it, it changed this message .</p><p><a href="http://oi62.tinypic.com/2s9oqz9.jpg">http://oi62.tinypic.com/2s9oqz9.jpg</a></p><p>In the firewall we can see that ipid being forwarded but the client doesnt gets it , I guess we need to do captures on devices after firewall to see where exactly this small packet is getting dropped.</p></div><div id="comment-46047-info" class="comment-info"><span class="comment-age">(22 Sep '15, 01:51)</span> Abdur Rehman</div></div></div><div id="comment-tools-46014" class="comment-tools"></div><div class="clear"></div><div id="comment-46014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46227"></span>

<div id="answer-container-46227" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46227-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Reassembly error, protocol TCP: New fragment overlaps old data (re transmission?)</p><p>This error does not show an error at the IP layer. It is a follow up of a retransmitted segment, if you have "Allow subdissectors to reassemble TCP streams" enabled.<br />
</p><p><strong>With TCP reassembly disabled:</strong> <img src="https://osqa-ask.wireshark.org/upfiles/Retr1_Xkk3VD4.JPG" alt="alt text" /></p><p><strong>With TCP reassembly enabled:</strong> <img src="https://osqa-ask.wireshark.org/upfiles/Retr1.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '15, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 28 Sep '15, 13:02</p></div></div><div id="comments-container-46227" class="comments-container"></div><div id="comment-tools-46227" class="comment-tools"></div><div class="clear"></div><div id="comment-46227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

