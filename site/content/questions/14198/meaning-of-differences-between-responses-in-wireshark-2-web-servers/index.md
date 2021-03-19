+++
type = "question"
title = "Meaning of differences between responses in WireShark - 2 web servers"
description = '''This question relates more to HTTP and web server responses than to WireShark, yet I am hoping that someone with intimate knowledge of comms and HTTP in particular, could take a look at the following and possibly offer insights. I have a device which issues GET and POST requests to a web endpoint. W...'''
date = "2012-09-12T01:26:00Z"
lastmod = "2012-09-12T06:30:00Z"
weight = 14198
keywords = [ "http-ok_non-response" ]
aliases = [ "/questions/14198" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Meaning of differences between responses in WireShark - 2 web servers](/questions/14198/meaning-of-differences-between-responses-in-wireshark-2-web-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14198-score" class="post-score" title="current number of votes">0</div><span id="post-14198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This question relates more to HTTP and web server responses than to WireShark, yet I am hoping that someone with intimate knowledge of comms and HTTP in particular, could take a look at the following and possibly offer insights.</p><p>I have a device which issues GET and POST requests to a web endpoint.</p><p>When the device issues these requests to an Apache web server, it responds properly to the Apache web server HTTP/1.1 200 OK responses.</p><p>The WireShark capture appears as follows:</p><pre><code>Frame 28: 96 bytes on wire (768 bits), 96 bytes captured (768 bits)
Ethernet II, Src: ...
Internet Protocol Version 4, Src: ...
Transmission Control Protocol, Src Port: http (80), Dst Port: nsstp (1036), Seq: 144, Ack: 257, Len: 30
[2 Reassembled TCP Segments (173 bytes): #27(143), #28(30)]
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        [Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]
            [Message: HTTP/1.1 200 OK\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Request Version: HTTP/1.1
        Status Code: 200
        Response Phrase: OK
    Content-Length: 30\r\n
        [Content length: 30]
    Content-Type: text/plain\r\n
    Date: Mon, 10 Sep 2012 13:15:16 GMT\r\n
    Server: CherryPy/3.1.0beta3 WSGI Server\r\n
    \r\n
Line-based text data: text/plain</code></pre><p>When the device issues these requests to an Microsoft-HTTPAPI/2.0 endpoint, it does not respond to the HTTP/1.1 200 OK responses.</p><p>The WireShark capture appears as follows:</p><pre><code>Frame 49: 240 bytes on wire (1920 bits), 240 bytes captured (1920 bits)
Ethernet II, Src: ...
Internet Protocol Version 4, Src: ...
Transmission Control Protocol, Src Port: http (80), Dst Port: kyoceranetdev (1063), Seq: 1, Ack: 257, Len: 174
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        [Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]
            [Message: HTTP/1.1 200 OK\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Request Version: HTTP/1.1
        Status Code: 200
        Response Phrase: OK
    Keep-Alive: true\r\n
    Content-Length: 0\r\n
        [Content length: 0]
    Content-Type: text/plain\r\n
    Server: Microsoft-HTTPAPI/2.0\r\n
    Date: Mon, 10 Sep 2012 13:29:20 GMT\r\n
    Connection: keep-alive\r\n
    \r\n</code></pre><p>I will really appreciate any assistance which may shed light on the possible cause.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http-ok_non-response" rel="tag" title="see questions tagged &#39;http-ok_non-response&#39;">http-ok_non-response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '12, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/2ed47cee87b4c41b4bf97720b4d58821?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oldevel&#39;s gravatar image" /><p><span>oldevel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oldevel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Sep '12, 03:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-14198" class="comments-container"></div><div id="comment-tools-14198" class="comment-tools"></div><div class="clear"></div><div id="comment-14198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14200"></span>

<div id="answer-container-14200" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14200-score" class="post-score" title="current number of votes">0</div><span id="post-14200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, this is not only not so much an HTTP question as it is a Wireshark question, it is more of an application specific question. Both responses are valid HTTP, but they do have different behavior. The biggest differences that stands out and can be a source of your device not responding properly is:</p><ul><li>The second response does not have content (it does not present any data back to your device), as can be seen in the "Content-Length: 0" header compared to the "Content-Length: 30" header in the apache response.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '12, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14200" class="comments-container"><span id="14203"></span><div id="comment-14203" class="comment"><div id="post-14203-score" class="comment-score"></div><div class="comment-text"><p>There is indeed data, click on the "Line-based text data" line and watch the corresponding hex data being highlighted. Or do a "Follow TCP stream" on the response packet.</p><p>Then from the increasing port numbers it looks like there is a new TCP connection for every object being transferred, even though the default in HTTP/1.1 is to keep the connection open. Does the client or the server close the connection?</p><p>Can you post a capture file to <a href="http://www.cloudshark.org">www.cloudshark.org</a> and paste the link to it here?</p><p>(You may want to use <a href="http://bittwist.sourceforge.net/">bittwiste</a> to remove the IP adresses)</p></div><div id="comment-14203-info" class="comment-info"><span class="comment-age">(12 Sep '12, 04:35)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="14204"></span><div id="comment-14204" class="comment"><div id="post-14204-score" class="comment-score"></div><div class="comment-text"><p>I am new to WireShark, and used "Export Packet Dissections as Plain Text File" to save the Capture for inspection in an editor. It appears that this Export option did not save the additional data which I now see is available. Your post has most certainly helped. Thank you.</p></div><div id="comment-14204-info" class="comment-info"><span class="comment-age">(12 Sep '12, 05:36)</span> <span class="comment-user userinfo">oldevel</span></div></div><span id="14205"></span><div id="comment-14205" class="comment"><div id="post-14205-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a "comment" as that's how this site works best, please see the FAQ for details.</p><p>Also, if you feel your question is answered, it is customary to accept the answer that answered your question by clicking on the check-mark next to it. This also removes the question from the "Ananswered Questions" list and helps other people to find the answers to their similar questions.</p></div><div id="comment-14205-info" class="comment-info"><span class="comment-age">(12 Sep '12, 05:44)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="14206"></span><div id="comment-14206" class="comment"><div id="post-14206-score" class="comment-score"></div><div class="comment-text"><p>I converted your second comment to an answer (I hope all is correct now). Once again thank you for your comments and advice.</p></div><div id="comment-14206-info" class="comment-info"><span class="comment-age">(12 Sep '12, 06:13)</span> <span class="comment-user userinfo">oldevel</span></div></div><span id="14208"></span><div id="comment-14208" class="comment"><div id="post-14208-score" class="comment-score"></div><div class="comment-text"><p>Actually, these were all comments to the same "answer" to keep the flow clear for others, it would have been better to leave that as a comment. But no worries... I don't think there will be more answers posted to this question (which will disrupt the flow, especially when people start liking answers which will change the order of answers).</p></div><div id="comment-14208-info" class="comment-info"><span class="comment-age">(12 Sep '12, 06:30)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-14200" class="comment-tools"></div><div class="clear"></div><div id="comment-14200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14202"></span>

<div id="answer-container-14202" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14202-score" class="post-score" title="current number of votes">0</div><span id="post-14202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you for your response. I have copied a few more responses below. From these responses, which also correspond to some information on how the device communication should work, it appears that no data is sent back from the web endpoint (web server) to the device, only OK. One thing that is somewhat contradictory here is that the Len: and Content length: fields in these responses appear to indicate otherwise, yet no corresponding data is visible in either the Info fields.<br />
</p><pre><code>No.     Time        Source                Destination           Protocol Length Info
      6 0.268032                                                HTTP     316    HTTP/1.1 200 OK  (text/plain)

Frame 6: 316 bytes on wire (2528 bits), 316 bytes captured (2528 bits)
Ethernet II, Src: ...
Internet Protocol Version 4, Src: ...
Transmission Control Protocol, Src Port: http (80), Dst Port: activesync (1034), Seq: 145, Ack: 180, Len: 250
[2 Reassembled TCP Segments (394 bytes): #5(144), #6(250)]
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        [Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]
            [Message: HTTP/1.1 200 OK\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Request Version: HTTP/1.1
        Status Code: 200
        Response Phrase: OK
    Content-Length: 250\r\n
        [Content length: 250]
    Content-Type: text/plain\r\n
    Date: Mon, 10 Sep 2012 13:15:07 GMT\r\n
    Server: CherryPy/3.1.0beta3 WSGI Server\r\n
    \r\n
Line-based text data: text/plain

No.     Time        Source                Destination           Protocol Length Info
     16 6.532646                                                HTTP     68     HTTP/1.1 200 OK  (text/plain)

Frame 16: 68 bytes on wire (544 bits), 68 bytes captured (544 bits)
Ethernet II, Src: ...
Internet Protocol Version 4, Src: ...
Transmission Control Protocol, Src Port: http (80), Dst Port: mxxrlogin (1035), Seq: 143, Ack: 231, Len: 2
[2 Reassembled TCP Segments (144 bytes): #15(142), #16(2)]
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        [Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]
            [Message: HTTP/1.1 200 OK\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Request Version: HTTP/1.1
        Status Code: 200
        Response Phrase: OK
    Content-Length: 2\r\n
        [Content length: 2]
    Content-Type: text/plain\r\n
    Date: Mon, 10 Sep 2012 13:15:13 GMT\r\n
    Server: CherryPy/3.1.0beta3 WSGI Server\r\n
    \r\n
Line-based text data: text/plain

No.     Time        Source                Destination           Protocol Length Info
     28 9.592467                                                HTTP     96     HTTP/1.1 200 OK  (text/plain)

Frame 28: 96 bytes on wire (768 bits), 96 bytes captured (768 bits)
Ethernet II, Src: ...
Internet Protocol Version 4, Src: ...
Transmission Control Protocol, Src Port: http (80), Dst Port: nsstp (1036), Seq: 144, Ack: 257, Len: 30
[2 Reassembled TCP Segments (173 bytes): #27(143), #28(30)]
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        [Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]
            [Message: HTTP/1.1 200 OK\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Request Version: HTTP/1.1
        Status Code: 200
        Response Phrase: OK
    Content-Length: 30\r\n
        [Content length: 30]
    Content-Type: text/plain\r\n
    Date: Mon, 10 Sep 2012 13:15:16 GMT\r\n
    Server: CherryPy/3.1.0beta3 WSGI Server\r\n
    \r\n
Line-based text data: text/plain

No.     Time        Source                Destination           Protocol Length Info
     38 33.427907                                               HTTP     68     HTTP/1.1 200 OK  (text/plain)

Frame 38: 68 bytes on wire (544 bits), 68 bytes captured (544 bits)
Ethernet II, Src: ...
Internet Protocol Version 4, Src: ...
Transmission Control Protocol, Src Port: http (80), Dst Port: ams (1037), Seq: 143, Ack: 231, Len: 2
[2 Reassembled TCP Segments (144 bytes): #37(142), #38(2)]
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        [Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]
            [Message: HTTP/1.1 200 OK\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Request Version: HTTP/1.1
        Status Code: 200
        Response Phrase: OK
    Content-Length: 2\r\n
        [Content length: 2]
    Content-Type: text/plain\r\n
    Date: Mon, 10 Sep 2012 13:15:40 GMT\r\n
    Server: CherryPy/3.1.0beta3 WSGI Server\r\n
    \r\n
Line-based text data: text/plain</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '12, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/2ed47cee87b4c41b4bf97720b4d58821?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oldevel&#39;s gravatar image" /><p><span>oldevel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oldevel has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-14202" class="comments-container"></div><div id="comment-tools-14202" class="comment-tools"></div><div class="clear"></div><div id="comment-14202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

