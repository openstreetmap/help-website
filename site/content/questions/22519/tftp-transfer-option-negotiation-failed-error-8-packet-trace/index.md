+++
type = "question"
title = "TFTP Transfer option negotiation failed error 8 packet trace"
description = '''Hey guys, I have been trying to figure out why my netboot TFTP transfers are failing when the client is asking for option negotiation from the TFTP server. Basically wireshark has helped me determine that the communication goes like this. Client (port 10545)-&amp;gt; Server (port 69) Read request for fi...'''
date = "2013-07-01T13:14:00Z"
lastmod = "2013-07-01T13:43:00Z"
weight = 22519
keywords = [ "osx", "tftp", "macosx", "netboot" ]
aliases = [ "/questions/22519" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TFTP Transfer option negotiation failed error 8 packet trace](/questions/22519/tftp-transfer-option-negotiation-failed-error-8-packet-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22519-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys,</p><p>I have been trying to figure out why my netboot TFTP transfers are failing when the client is asking for option negotiation from the TFTP server.</p><p>Basically wireshark has helped me determine that the communication goes like this.</p><pre><code>Client (port 10545)-&gt; Server (port 69) Read request for file.exe - Transfer type: octet, blksize\000=512\000, tsize\000=0\000

Server (port 52104) -&gt; Client (port 10545) option acknowledgement, blksize\000=512\000, tsize\000=994464\000

Client (port 10545) -&gt; Server (port 52104 Error Code, Code: Option Negotiation failed: Message error code 8 client or user aborted transfer</code></pre><p>A 2nd attempt is immediately tried again but this time with out the tsize option.</p><pre><code>Client -&gt; Server Read request for file.exe - Transfer type: octet, blksize\000=8192\000
Server -&gt; Client option acknowledgement, blksize\000=8192\000
Client -&gt; Server acknowledgement, Block:0</code></pre><p>It is then fine.</p><p>So either the client cant get its OACK or options acknowledgement back to the server or the client is just outright refusing the servers option acknowledgement and then cancels the transfer.</p><p>I cant do a shark on the client because it is in firmware booting mode, and I dont have a switch that can do port mirroring.</p><p>I have scoured the inter webs for some kind of a solution to whats going on. Maybe the experts here can give a helping hand.</p><p>Thanks in advance!!!</p></div><div id="question-tags" class="tags-container tags">osx tftp macosx netboot</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '13, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/4ae3163f348b4298baab0e79cfb3a3cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ClassicII&#39;s gravatar image" /><p>ClassicII<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ClassicII has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jul '13, 14:20</p></div></div><div id="comments-container-22519" class="comments-container"></div><div id="comment-tools-22519" class="comment-tools"></div><div class="clear"></div><div id="comment-22519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22522"></span>

<div id="answer-container-22522" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22522-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks to me that the client first tries to negotiate a blocksize of 512 and requests the filesize. Then when it does receive the filesize, it decides to use a blocksize of 8192 instead of 512. No need to use the tsize option again, as the filesize is already known.</p><p>According to the <a href="http://tools.ietf.org/html/rfc2347">RFC</a>, the tftp server should not return a tsize option in the response to the second request. Did you really see that in the option acknowledgement?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22522" class="comments-container"><span id="22524"></span><div id="comment-22524" class="comment"><div id="post-22524-score" class="comment-score"></div><div class="comment-text"><p>Yes good call and sorry for the typo! You are right the 2nd request looks like this.</p><p>Client -&gt; Server Read request for file.exe - Transfer type: octet, blksize\000=8192\000 Server -&gt; Client option acknowledgement, blksize\000=8192\000 Client -&gt; Server acknowledgement, Block:0</p><p>What is interesting is that when I fire up my client and ask the server for the same thing.</p><p>tftp mode octet tsize on blksize 8192 get file.exe</p><p>Client -&gt; Server : Read request for file.exe - Transfer type: octet, tsize\000=0\000, blksize\000=8192\000 Server -&gt; Client : option acknowledgement, tsize\000=994464\000, blksize\000=8192\000 Client -&gt; Server : acknowledgement, Block:0</p><p>What i did notice about this one is that the server port is always port 69.</p><p>Also according to that link.</p><p>If the client rejects the OACK, then it sends an ERROR packet, with error code 8, to the server and the transfer is terminated.</p><p>Once a client acknowledges an OACK, with an appropriate non-error response, that client has agreed to use only the options and values returned by the server. Remember that the server cannot request an option; it can only respond to them. If the client receives an OACK containing an unrequested option, it should respond with an ERROR packet, with error code 8, and terminate the transfer.</p><p>So according to this its like the server is sending back an OACK with options that the client did not ask for in the first place even though the options look proper in the trace ?</p></div><div id="comment-22524-info" class="comment-info"><span class="comment-age">(01 Jul '13, 14:19)</span> ClassicII</div></div><span id="22526"></span><div id="comment-22526" class="comment"><div id="post-22526-score" class="comment-score"></div><div class="comment-text"><p>Well, there are options for which the value may change between the request and the acknowledgement. tsize is one of them, see <a href="http://tools.ietf.org/html/rfc2349">RFC 2349</a></p></div><div id="comment-22526-info" class="comment-info"><span class="comment-age">(01 Jul '13, 14:27)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-22522" class="comment-tools"></div><div class="clear"></div><div id="comment-22522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

