+++
type = "question"
title = "TCP (and others) response times"
description = '''Can anyone provide some tips on determining response time to certain protocols? For instance, I can think of several protocols where I want to detect a network request then find how long it takes to get a response. The main one is ModbusTCP, where there is a request then a response some time later. ...'''
date = "2010-09-21T03:52:00Z"
lastmod = "2010-09-21T06:52:00Z"
weight = 241
keywords = [ "response", "service", "time" ]
aliases = [ "/questions/241" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP (and others) response times](/questions/241/tcp-and-others-response-times)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-241-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone provide some tips on determining response time to certain protocols? For instance, I can think of several protocols where I want to detect a network request then find how long it takes to get a response. The main one is ModbusTCP, where there is a request then a response some time later. Another could be DNS response times, or ARP response times. I know there is an option for service response times, but as luck would have it the ones I want are not there.</p><p>My solution is to export the packet data and bring into Excel and manipulate there. Very time consuming. Any tips, tricks, or ideas would be helpful!</p><p>Let me clarify my question a little more with an example. I may have a trace with one tcp connection, but the request and response is continuous. Each individual request and response has a response time, so I may have 100K packets, so 50K response times. I want to end with a histogram of response time, based on arbitrary criteria - say this port, or this type of request, or this packet size. Currently what I do is:</p><ol><li>Add columns to display: Modbus TransactionID, function code, and number of registers</li><li>Filter out the TCP stream I need in the display filter</li><li>Sort the data by TransactionID, and then view time starting at beginning of capture assuming that the packet number is a sub sort, as in there should be two packets (sometimes more) with the same transactionID, and I want the request first, response second, and this should be the case with the packet number.</li></ol><p>But then I export into Excel, and have to do some tests - I need two transactionIDs in a row that are the same; if so, then I can do a time delta between them and then for that function code and transactionID, I then have a response time. I do this for all the data, ignoring the cases where I have no response, or multiple requests for a response, and I can then plot and get a histogram.</p><p>Is there a way to get this in the IOgraph as part of Wireshark? I will do without the histogram, but I can live without the histogram, but a realtime response graph on the IOgraph would be fantastic. I can then just watch to see how the devices perform over time, and instantly see where we may have an issue to address.</p><p>If I need to do some scripting, I can give it a try. Can anyone point me to a suggested scripting language? I took cursory look at Lua, so I assume that is what I should start with as it is integrated with Wireshark? I suppose if I want to get really fancy - LUA script -&gt; GNUPlot then I can get my data and a graph at the same time?<br />
</p></div><div id="question-tags" class="tags-container tags">response service time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '10, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Sep '10, 06:29</p></div></div><div id="comments-container-241" class="comments-container"><span id="16447"></span><div id="comment-16447" class="comment"><div id="post-16447-score" class="comment-score"></div><div class="comment-text"><p>hello I would like to ask how me messure the requestand responce time of SMB ? Please send me on [email protected]<a href="http://hotmail.com">hotmail.com</a>.</p></div><div id="comment-16447-info" class="comment-info"><span class="comment-age">(29 Nov '12, 19:47)</span> imran</div></div><span id="16448"></span><div id="comment-16448" class="comment"><div id="post-16448-score" class="comment-score"></div><div class="comment-text"><p>hello I would like to ask how we messure the Request and responce time of SMB?</p></div><div id="comment-16448-info" class="comment-info"><span class="comment-age">(29 Nov '12, 19:48)</span> imran</div></div></div><div id="comment-tools-241" class="comment-tools"></div><div class="clear"></div><div id="comment-241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="242"></span>

<div id="answer-container-242" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-242-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Be sure you have a column setup for interpacket deltas (Edit-&gt;Prefs-&gt;Columns - add a column for "Delta Time Displayed"). This will show you the time delta between packets. Now you have to filter out the conversations that you want to view response times for. There are, of course, a few caveats. For TCP conversations you'll need to watch for the original SYN packet (am I the only one that loves saying "Original SYN"??) then look at the delta between that packet and the returning SYN-ACK. This delta, for the most part, will represent network flight time - How long it took to get from tier A to tier B. NORMALLY the SYN/SYN-ACK process involves little to no system processing time and, so, is a fairly reliable gauge of end-to-end latency. Things get more difficult if you want to monitor an entire conversation and understand the variable response times from either tierA or tierB. The TCP Flow Graph (Stats-&gt;Flow Graph) will break down the response times over time but they can be misleading depending on the volatility of the network.</p><hr /><pre><code> For DNS response times you can filter out the conversation and just look at the deltas between the request going out and the response coming in.  There are a few different ways to handle this kind of thing en masse - either with Excel or the raw dump and a good scripting language.</code></pre><hr /><p>Those are my $.02, others may have better input.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '10, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-242" class="comments-container"><span id="280"></span><div id="comment-280" class="comment"><div id="post-280-score" class="comment-score"></div><div class="comment-text"><p>I think that looking at the delta times between packets of the tcp handshake does provide a good indicator for network response time but may not shed any light on application response time. Additionally, if the trace was taken on the server then looking at time delta between syn and syn ack would be a misleading indicator of network response time. Rather, looking at the syn ack and ack delta would be more accurate due to where the trace was taken.</p></div><div id="comment-280-info" class="comment-info"><span class="comment-age">(22 Sep '10, 18:19)</span> 9691ekiM</div></div></div><div id="comment-tools-242" class="comment-tools"></div><div class="clear"></div><div id="comment-242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="245"></span>

<div id="answer-container-245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-245-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wow...and I thought it was a simple response time question ;-)</p><p>This is a pretty good writeup, taken from a Sharkfest presentation, see if it puts you on the right path.</p><p><a href="http://www.cacetech.com/sharkfest.09/bu-9-tompkins-gearbit-wireshark_charts_&amp;_io_graphs-sharkfest09.pdf">Wireshark Charts &amp; IO Graphs</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '10, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-245" class="comments-container"><span id="36407"></span><div id="comment-36407" class="comment"><div id="post-36407-score" class="comment-score"></div><div class="comment-text"><p>Hi Geon You mean to say, Delta Time displays the difference between request and response times?</p><p>Regards. Sudin<br />
</p></div><div id="comment-36407-info" class="comment-info"><span class="comment-age">(17 Sep '14, 08:01)</span> Sud</div></div><span id="36408"></span><div id="comment-36408" class="comment"><div id="post-36408-score" class="comment-score"></div><div class="comment-text"><p>Delta Time displays the time difference between packets, regardless of whether they are requests or responses, but you could apply a display filter so that Wireshark is showing only the requests and responses that you're concerned with. Make sure you're using the delta time between displayed packets, not the delta time between captured packets.</p><p>For some protocols, Wireshark will calculate the time between the request and response for you. Wireshark has the dns.time field, the http.time field, the smb.time field, and the smb2.time field. These time fields are found in the response packet, assuming that both the request and the response are in the trace. I do not see a time field for Modbus.</p></div><div id="comment-36408-info" class="comment-info"><span class="comment-age">(17 Sep '14, 08:42)</span> Jim Aragon</div></div></div><div id="comment-tools-245" class="comment-tools"></div><div class="clear"></div><div id="comment-245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

