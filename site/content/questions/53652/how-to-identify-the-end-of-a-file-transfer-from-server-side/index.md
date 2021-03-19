+++
type = "question"
title = "How to identify the end of a file transfer from server side?"
description = '''The scenario is quite straight forward - a client is downloading a file from a server using HTTP GET.  I can use wireshark at server end, but not at client end.  What I want to do is to calculate the download throughput. I&#x27;m trying to use wireshark to see the beginning and end timestamp of the file ...'''
date = "2016-06-26T03:25:00Z"
lastmod = "2016-06-26T04:23:00Z"
weight = 53652
keywords = [ "download", "http", "tcp", "sequence" ]
aliases = [ "/questions/53652" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to identify the end of a file transfer from server side?](/questions/53652/how-to-identify-the-end-of-a-file-transfer-from-server-side)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53652-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The scenario is quite straight forward - a client is downloading a file from a server using HTTP GET.</p><p>I can use wireshark at server end, but not at client end.</p><p>What I want to do is to calculate the download throughput. I'm trying to use wireshark to see the beginning and end timestamp of the file download, but I'm having trouble identifying the latter. (The beginning time is when server receives the HTTP GET packet)</p><p>As far as I can see, there are lots of TCP ACK coming into the server after the HTTP 200 OK packet was sent from server to the client, which makes sense as the client is ack'ing the data segments.</p><p>My questions are:</p><ul><li>How to identify the end of a file transfer? Is it the last ACK received from client?</li><li>If I want to do this in real time (using tcpdump, for example), I won't be able to know which ACK is the last one. So is there any way I can "track" the packets and know it's the last one, e.g., through seq/ack numbers?</li></ul></div><div id="question-tags" class="tags-container tags">download http tcp sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '16, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/5b505a91634dbad2eb6c081340c7197f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chang&#39;s gravatar image" /><p>Chang<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chang has no accepted answers">0%</span></p></div></div><div id="comments-container-53652" class="comments-container"></div><div id="comment-tools-53652" class="comment-tools"></div><div class="clear"></div><div id="comment-53652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53653"></span>

<div id="answer-container-53653" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53653-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, if we talk about network throughput, the beginning of transfer is not when the server receives the "HTTP GET packet", and even not when the server receives the last packet of the HTTP GET (which may occupy more than a single packet in some cases). The beginning of the transfer is when the server sends the first packet with non-zero payload size.</p><p>The end of the transfer is when all parts of the file have reached the client. If there is no packet loss, it is the moment when the last packet with non-zero payload size has arrived to the client. And "last" is the one which is followed by at least one packet from the server which has zero payload length, which may be a FIN, a RST, or simply an ACK to the first packet of a subsequent GET sent using the same TCP session.</p><p>The trouble (from the perspective of your task) is that a typical browser does not close a TCP session immediately after finishing transfer of a single file but keeps it open for a while and eventually reuses it if it needs to transfer another file from the same server. So if you open a web page which e.g. contains several pictures stored at the same server like the base html file, you'll see several GETs and responses to them in a single TCP session.</p><p>What might help you is that Wireshark, and therefore also tshark, normally reassembles the payload, so the last packet of a file is the one which is marked as HTTP, while all the previous ones are only marked as TCP. This won't work with tcpdump which does not reassemble the application protocols. But using this feature for your online throughput analysis requires that you take the HTTP GET as the beginning of the file transfer which induces some error into your bandwidth calculation (the request processing time at the server.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '16, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '16, 04:27</p></div></div><div id="comments-container-53653" class="comments-container"><span id="53657"></span><div id="comment-53657" class="comment"><div id="post-53657-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your comment!</p><p>Can you please elaborate a bit more on (last paragraph) "Wireshark ... the last packet of a file is the one which is marked as HTTP"?</p><p>When I look at the wireshark trace, I can see that there is always a "HTTP 200 OK" near the end of a download - is this the one you are referring to?</p></div><div id="comment-53657-info" class="comment-info"><span class="comment-age">(26 Jun '16, 12:19)</span> Chang</div></div><span id="53658"></span><div id="comment-53658" class="comment"><div id="post-53658-score" class="comment-score"></div><div class="comment-text"><p>Btw I forgot to mention that I'm looking to estimate the throughput by best effort, so the error caused by using HTTP GET as the beginning of a transfer is acceptable in this case.</p></div><div id="comment-53658-info" class="comment-info"><span class="comment-age">(26 Jun '16, 12:21)</span> Chang</div></div><span id="53659"></span><div id="comment-53659" class="comment"><div id="post-53659-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I can see that there is always a "HTTP 200 OK" near the end of a download - is this the one you are referring to?</p></blockquote><p>Yes, exactly. An HTTP PDU, especially one carrying a file as a payload, often spans over several packets (sometimes thousands of packets), and thus Wireshark (as well as the actual recipient) can only properly process it after it gets received completely. So although the string "200 OK" is physically present in the first packet of the response, tshark shows it in the "reassembled data" of the last one, and therefore also marks only the last packet of the response as a HTTP one.</p><p>The file you transfer is actually a payload of the HTTP 200 OK message, i.e. there is some overhead added to the file size.</p><p>There are also several methods of encoding the file contents for transfer, so the number of bytes needed to transfer the file may differ significantly from its actual size. It may be bigger but also smaller as some methods encode binary data using only byte values which represent printable characters (so the result occupies more bytes), some methods compress the data and use all 8 bits to transport the result.</p><p>So your throughput measurement will give you the raw figures, i.e. actually transferred bytes per second including all overheads (HTTP, TCP, IP, Ethernet) plus the size after encoding of the transferred file.</p><p>Off topic: on this site, the purpose of the "thumbs up" icon next to an Answer is to allow other users than the author of the Question to vote for those Answers which they consider more useful than other ones. To mark an Answer as useful, the author of the Question should use the checkmark icon. Doing so changes the appearance of the Question in the list in order to indicate to others coming to ask a similar Question that the existing one has been answered usefully.</p></div><div id="comment-53659-info" class="comment-info"><span class="comment-age">(26 Jun '16, 14:07)</span> sindy</div></div><span id="53660"></span><div id="comment-53660" class="comment"><div id="post-53660-score" class="comment-score"></div><div class="comment-text"><p>This has been super helpful, thanks again!</p></div><div id="comment-53660-info" class="comment-info"><span class="comment-age">(26 Jun '16, 15:18)</span> Chang</div></div></div><div id="comment-tools-53653" class="comment-tools"></div><div class="clear"></div><div id="comment-53653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

