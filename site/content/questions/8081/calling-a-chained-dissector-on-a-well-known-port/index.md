+++
type = "question"
title = "Calling a chained dissector on a well-known port"
description = '''I am currently trying to write a Lua chained dissector that would take place on a well-known port. I first wrote it as a post-dissector, and everything was working, but for some reason, the dissector function is never called for a chained dissector. For test purposes, the code is as simple as this :...'''
date = "2011-12-22T12:26:00Z"
lastmod = "2011-12-23T13:19:00Z"
weight = 8081
keywords = [ "chained-dissector", "lua", "dissector", "http" ]
aliases = [ "/questions/8081" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Calling a chained dissector on a well-known port](/questions/8081/calling-a-chained-dissector-on-a-well-known-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8081-score" class="post-score" title="current number of votes">1</div><span id="post-8081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am currently trying to write a Lua <a href="http://wiki.wireshark.org/Lua/Dissectors#chained_dissectors">chained dissector</a> that would take place on a well-known port. I first wrote it as a <a href="http://wiki.wireshark.org/Lua/Dissectors#postdissectors">post-dissector</a>, and everything was working, but for some reason, the dissector function is never called for a chained dissector.</p><p>For test purposes, the code is as simple as this :</p><pre><code>-- declare our protocol
httpProto        = Proto(&quot;http&quot;,&quot;http&quot;)

print(&quot;out of  the dissector&quot;)
--======================-- create a functions to dissect it --======================--

function httpProto.dissector( buffer, pinfo, tree )
   print(&quot;In the dissector&quot;)  

end
-- load the tcp.port table

tcp_table = DissectorTable.get( &quot;tcp.port&quot; )

-- register our protocol to handle the chosen port

tcp_table:add( 80, httpProto )</code></pre><p>I ran it using <code>tshark</code> with a sample HTTP capture from the Wireshark site (<a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=http.cap">http.cap</a>), but the message "In the dissector" is never displayed:</p><pre><code>C:\Program Files (x86)\Wireshark&gt;tshark.exe -r http.cap  
__out of  the dissector__  
  1   0.000000 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [SYN] Seq=0 Win=8760 Len=0 MSS=1460 SACK_PERM=1 80 0  
  2   0.911310 65.208.228.223 -&gt; 145.254.160.237 TCP http &gt; tip2 [SYN, ACK] Seq=0 Ack=1 Win=5840 Len=0 MSS=1380 SACK_PERM=1 3372 0  
  3   0.911310 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=1 Ack=1 Win=9660 Len=0 80 0  
  4   0.911310 145.254.160.237 -&gt; 65.208.228.223 HTTP GET /download.html HTTP/1.1  80 0  
  5   1.472116 65.208.228.223 -&gt; 145.254.160.237 TCP http &gt; tip2 [ACK] Seq=1 Ack=480 Win=6432 Len=0 3372 0  
  6   1.682419 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
  7   1.812606 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=480 Ack=1381 Win=9660 Len=0 80 0  
  8   1.812606 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
  9   2.012894 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=480 Ack=2761 Win=9660 Len=0 80 0  
 10   2.443513 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
 11   2.553672 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
 12   2.553672 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=480 Ack=5521 Win=9660 Len=0 80 0  
 13   2.553672 145.254.160.237 -&gt; 145.253.2.203 DNS Standard query A pagead2.googlesyndication.com 53  
 14   2.633787 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
 15   2.814046 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=480 Ack=6901 Win=9660 Len=0 80 0  
 16   2.894161 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
 17   2.914190 145.253.2.203 -&gt; 145.254.160.237 DNS Standard query response CNAME pagead2.google.com CNAME pagead.google.akadns.net A 216.239.59.104 A
 216.239.59.99 3009  
 18   2.984291 145.254.160.237 -&gt; 216.239.59.99 HTTP GET /pagead/ads?client=ca-pub-2309191948673629&amp;random=1084443430285&amp;lmt=1082467020&amp;format=468x60_
as&amp;output=html&amp;url=http%3A%2F%2Fwww.ethereal.com%2Fdownload.html&amp;color_bg=FFFFFF&amp;color_text=333333&amp;color_link=000000&amp;color_url=666633&amp;color_border=666
633 HTTP/1.1  80 2  
[...]</code></pre><p>However, if I change the code in order to bind it to an "empty" port (as follows):</p><pre><code>[...]
-- load the tcp.port table  
tcp_table = DissectorTable.get( &quot;tcp.port&quot; )  
-- register our protocol to handle the chosen port  
tcp_table:add( 1756, httpProto )</code></pre><p>...and then I feed <code>tshark</code> with a trace that contains a packet from this port, I can see my "In the dissector":</p><pre><code>C:\Program Files (x86)\Wireshark&gt;tshark.exe -r test1756Packets.pcap  
__out of  the dissector__  
__In the dissector__  
  1   0.000000   10.1.0.122 -&gt; 10.2.17.199  TCP 63545 &gt; capfast-lmd [PSH, ACK] Seq=1 Ack=1 Win=64164 Len=20 1756 0  
__In the dissector__  
  2   0.006478  10.2.17.199 -&gt; 10.1.0.122   TCP capfast-lmd &gt; 63545 [PSH, ACK] Seq=1 Ack=21 Win=1664 Len=64 63545 0  </code></pre><p>I am running Wireshark 1.6.4 (32- and 64-bit, I tried both) on Windows 7 (64-bit). Can you help me find what am I doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-chained-dissector" rel="tag" title="see questions tagged &#39;chained-dissector&#39;">chained-dissector</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '11, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/1be8dea3a0a7084944950af15337facb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mathieu&#39;s gravatar image" /><p><span>Mathieu</span><br />
<span class="score" title="14 reputation points">14</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mathieu has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Dec '11, 16:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></br></p></div></div><div id="comments-container-8081" class="comments-container"></div><div id="comment-tools-8081" class="comment-tools"></div><div class="clear"></div><div id="comment-8081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8093"></span>

<div id="answer-container-8093" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8093-score" class="post-score" title="current number of votes">2</div><span id="post-8093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that you're trying to declare a dissector with an existing name; there's already a dissector named "http". You should see the error when you try to load the script:</p><pre><code>$ tshark -Xlua_script:test.lua -i en0 -R &quot;http&quot;
tshark: Lua: Error during loading:
 [string &quot;test.lua&quot;]:2: bad argument #1 to &#39;Proto&#39; (Proto_new: there cannot be two protocols with the same name)</code></pre><p>Also, as is, the code shown in your question isn't actually a chained dissector because it doesn't call the original dissector. I'm guessing that was just a copy-and-paste mistake.</p><p>With the appropriate changes (bold) in <code>test.lua</code>:</p><pre><code>-- declare our protocol
httpProto        = Proto(&quot;httpwrap&quot;, &quot;HTTP wrapper&quot;)
print(&quot;out of  the dissector&quot;)

--======================-- create a functions to dissect it --======================--
function httpProto.dissector( buffer, pinfo, tree )
   print(&quot;In the dissector&quot;)
   orig_http_dis:call( buffer, pinfo, tree ) 
end

-- load the tcp.port table
tcp_table = DissectorTable.get( &quot;tcp.port&quot; )

orig_http_dis = tcp_table:get_dissector( 80 )

-- register our protocol to handle the chosen port
tcp_table:add( 80, httpProto )</code></pre><p><br />
...you should see the expected output from your chained dissector:</p><pre><code>$ tshark -Xlua_script:test.lua -R &quot;http&quot; -r http.cap
out of  the dissector
In the dissector
  0.911310 145.254.160.237 -&gt; 65.208.228.223 HTTP 533 GET /download.html HTTP/1.1 
In the dissector
  1.682419 65.208.228.223 -&gt; 145.254.160.237 HTTP/XML 1434 HTTP/1.1 200 OK 
In the dissector
[...]</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '11, 17:36</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-8093" class="comments-container"><span id="8110"></span><div id="comment-8110" class="comment"><div id="post-8110-score" class="comment-score"></div><div class="comment-text"><p>I am sorry you are right, I changed the Proto field to make it more verbose and I didn't try to rerun the script. I removed the call to the original dissector to make it as simple as possible.</p><p>I copy/pasted your exact script that you gave me, but I get the same output:</p><pre><code>C:\Program Files (x86)\Wireshark&gt;tshark.exe -r http.cap  
__out of  the dissector__  
  1   0.000000 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [SYN] Seq=0 Win=8760 Len=0 MSS=1460 SACK_PERM=1 80 0  
  2   0.911310 65.208.228.223 -&gt; 145.254.160.237 TCP http &gt; tip2 [SYN, ACK] Seq=0 Ack=1 Win=5840 Len=0 MSS=1380 SACK_PERM=1 3372 0  
  3   0.911310 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=1 Ack=1 Win=9660 Len=0 80 0  
  4   0.911310 145.254.160.237 -&gt; 65.208.228.223 HTTP GET /download.html HTTP/1.1  80 0  
  5   1.472116 65.208.228.223 -&gt; 145.254.160.237 TCP http &gt; tip2 [ACK] Seq=1 Ack=480 Win=6432 Len=0 3372 0  
  6   1.682419 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
  7   1.812606 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=480 Ack=1381 Win=9660 Len=0 80 0  
  8   1.812606 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
  9   2.012894 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=480 Ack=2761 Win=9660 Len=0 80 0  
 10   2.443513 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
 11   2.553672 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
 12   2.553672 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=480 Ack=5521 Win=9660 Len=0 80 0  
 13   2.553672 145.254.160.237 -&gt; 145.253.2.203 DNS Standard query A pagead2.googlesyndication.com 53  
 14   2.633787 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
 15   2.814046 145.254.160.237 -&gt; 65.208.228.223 TCP tip2 &gt; http [ACK] Seq=480 Ack=6901 Win=9660 Len=0 80 0  
 16   2.894161 65.208.228.223 -&gt; 145.254.160.237 TCP [TCP segment of a reassembled PDU] 3372 0  
 17   2.914190 145.253.2.203 -&gt; 145.254.160.237 DNS Standard query response CNAME pagead2.google.com CNAME pagead.google.akadns.net A 216.239.59.104 A
 216.239.59.99 3009  
 18   2.984291 145.254.160.237 -&gt; 216.239.59.99 HTTP GET /pagead/ads?client=ca-pub-2309191948673629&amp;random=1084443430285&amp;lmt=1082467020&amp;format=468x60_
as&amp;output=html&amp;url=http%3A%2F%2Fwww.ethereal.com%2Fdownload.html&amp;color_bg=FFFFFF&amp;color_text=333333&amp;color_link=000000&amp;color_url=666633&amp;color_border=666
633 HTTP/1.1  80 2  
[...]</code></pre><p>The function <code>httpProto.dissector(...)</code> really seems to never be called. It is always the default http dissector that is called as if taking its place in the <code>DissectorTable</code> doesn't work.</p></div><div id="comment-8110-info" class="comment-info"><span class="comment-age">(23 Dec '11, 07:56)</span> <span class="comment-user userinfo">Mathieu</span></div></div><span id="8118"></span><div id="comment-8118" class="comment"><div id="post-8118-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark/TShark are you running? I just tried my script successfully from Windows 7 with TShark 1.7.0 (SVN 39768). I even used the <code>plugins</code> directory to avoid explicitly specifying the script (as you are doing).</p><pre><code>C:\temp&gt;tshark -R &quot;http&quot; -r http.cap
out of  the dissector
In the dissector
  4   0.911310 145.254.160.237 -&gt; 65.208.228.223 HTTP 533 GET /download.html HTTP/1.1
In the dissector
  6   1.682419 65.208.228.223 -&gt; 145.254.160.237 HTTP/XML 1434 HTTP/1.1 200 OK
In the dissector
  8   1.812606 65.208.228.223 -&gt; 145.254.160.237 HTTP 1434 Continuation or non-HTTP traffic</code></pre></div><div id="comment-8118-info" class="comment-info"><span class="comment-age">(23 Dec '11, 13:19)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-8093" class="comment-tools"></div><div class="clear"></div><div id="comment-8093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

