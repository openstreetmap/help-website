+++
type = "question"
title = "Counting incoming TCP open &amp; http GET requests to a web server"
description = '''I want to use wireshark (preferably tshark) as a sniffer for web server performance symbiotic simulation analysis. The countables of interest are:  Incoming TCP open connections i.e.  &quot;tcp.flags.syn==1&quot; and  &quot;tcp.flags.ack==0&quot; Incoming GET http  requests.  For those I don&#x27;t need the details, only co...'''
date = "2011-12-17T13:52:00Z"
lastmod = "2011-12-22T12:43:00Z"
weight = 8029
keywords = [ "filter", "http", "file", "tcp", "counters" ]
aliases = [ "/questions/8029" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Counting incoming TCP open & http GET requests to a web server](/questions/8029/counting-incoming-tcp-open-http-get-requests-to-a-web-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8029-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to use wireshark (preferably tshark) as a sniffer for web server performance symbiotic simulation analysis. The countables of interest are:</p><ol><li>Incoming TCP open connections i.e. "tcp.flags.syn==1" and "tcp.flags.ack==0"</li><li>Incoming GET http requests.</li></ol><p>For those I don't need the details, only counters (quantities). These need to be stored in the same file, with some text readable format, because another application will be reading and producing output from them.</p><p>Does anyone know of a way to do that?</p></div><div id="question-tags" class="tags-container tags">filter http file tcp counters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '11, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/b6ab78997ac26efb7a11ea254f8bcc76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adonies&#39;s gravatar image" /><p>adonies<br />
<span class="score" title="12 reputation points">12</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adonies has no accepted answers">0%</span></p></div></div><div id="comments-container-8029" class="comments-container"></div><div id="comment-tools-8029" class="comment-tools"></div><div class="clear"></div><div id="comment-8029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="8030"></span>

<div id="answer-container-8030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8030-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here is a way to count the tcp flags and HTTP get requests:<br />
<a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a> statistics.</p><pre><code>$ tshark -r Clmt_04.pcap -qz &quot;io,stat,0,COUNT(tcp.flags)tcp.flags==0x12&quot; -z &quot;io,stat,0,COUNT(http.request.method)http.request.method==&quot;GET&quot;&quot;
===================================================================
IO Statistics
Column #0: COUNT(http.request.method)http.request.method==GET
                |   Column #0
Time            |          COUNT
000.000-                      115
===================================================================

===================================================================
IO Statistics
Column #0: COUNT(tcp.flags)tcp.flags==0x12
                |   Column #0
Time            |          COUNT
000.000-                       74
===================================================================</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '11, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></p></div></div><div id="comments-container-8030" class="comments-container"><span id="8043"></span><div id="comment-8043" class="comment"><div id="post-8043-score" class="comment-score"></div><div class="comment-text"><p>a.<br />
This was very helpful, thank you.<br />
I use a wireshark capture file that was filtered 'tcp dst port 8080'.<br />
The above code runs to completion, but although the http GET count turns up correct, the tcp.flags count turns up 0.<br />
Is the value <code>tcp.flags==0x12</code> correct for capturing tcp open requests?<br />
I'd thought that only the tcp-syn flag would be set in such packets, although I can't tell which value that corresponds to in the tcp.flags variable.<br />
<br />
b.<br />
Ideally I'd like to have a process that counts such packets in real time and produces a simple (capture?) file where it updates the two packet counts of interest in intervals.<br />
Is there any way to configure tshark to do that?</p></div><div id="comment-8043-info" class="comment-info"><span class="comment-age">(19 Dec '11, 10:52)</span> adonies</div></div><span id="8047"></span><div id="comment-8047" class="comment"><div id="post-8047-score" class="comment-score"></div><div class="comment-text"><p>a<br />
Sorry, my bad, should be&lt;br&lt; tcp.flags==0x02</p></div><div id="comment-8047-info" class="comment-info"><span class="comment-age">(19 Dec '11, 12:59)</span> joke</div></div><span id="8060"></span><div id="comment-8060" class="comment"><div id="post-8060-score" class="comment-score"></div><div class="comment-text"><p>With this value, I get a count of tcp.flags(0x02) 41.478 in my capture file, while the http.request.method(GET) is at 33.280.<br />
This result is strange because these counts should have been more or less the same.<br />
The web client requesting the data from the web server is custom-made and implements http/0.1 only: open TCP connection, request file, get data, close TCP.<br />
I know from the web server logs that about 33.280 were serviced 200 OK, and from the web client logs that about 33.528 requests were sent.<br />
I expected a count of about 33.528 tcp.flags(0x02) instead of 41.478.</p></div><div id="comment-8060-info" class="comment-info"><span class="comment-age">(20 Dec '11, 14:20)</span> adonies</div></div><span id="8088"></span><div id="comment-8088" class="comment"><div id="post-8088-score" class="comment-score"></div><div class="comment-text"><p>So I'm assuming the traffic you're capturing has only the test sequences, so there aren't other TCP connections being requested, possibly for protocols other than HTTP or for HTTP where the first request isn't a GET.</p><p>If so, what happens if you look instead for SYN+ACK from the server? If the initial SYN doesn't get responded to by the server, you'll get an initial SYN but you won't get a TCP connection and thus won't get a GET request.</p></div><div id="comment-8088-info" class="comment-info"><span class="comment-age">(22 Dec '11, 15:17)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8030" class="comment-tools"></div><div class="clear"></div><div id="comment-8030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8046"></span>

<div id="answer-container-8046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8046-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>io,stat</strong><br />
You can send the output only to a text file.<br />
</p><pre><code>$ tshark -i 3 -qz &quot;io,stat,120,COUNT(tcp.flags)tcp.flags==0x02&quot; -z &quot;io,stat,120,COUNT(http.request.method)http.request.method==&quot;GET&quot;&quot; &gt; io-stat.txt
===================================================================
io-stat.txt
===================================================================
IO Statistics
Interval: 120.000 secs
Column #0: COUNT(http.request.method)http.request.method==GET
                |   Column #0
Time            |          COUNT
000.000-120.000                 0
120.000-240.000               151
===================================================================
===================================================================
IO Statistics
Interval: 120.000 secs
Column #0: COUNT(tcp.flags)tcp.flags==0x02
                |   Column #0
Time            |          COUNT
000.000-120.000                 0
120.000-240.000                83
===================================================================</code></pre><p><br />
<br />
<strong>Output to capture file</strong><br />
You cannot use display filters, when capturing and saving the captured packets. So you have to use capture filters.<br />
<br />
Capture filters:<br />
Capture SYN packets:<br />
tcp[0xd]&amp;18=2<br />
<br />
Capture GET requests:<br />
tcp[20:4]=0x47455420<br />
<br />
$ tshark -i 3 -f "tcp[13]=0x02 or tcp[20:4]=0x47455420" -w syn-http.request.get.pcap<br />
<br />
Useful links:<br />
<a href="http://www.tcpdump.org/tcpdump_man.html">http://www.tcpdump.org/tcpdump_man.html</a><br />
<a href="http://www.packetlevel.ch/html/tcpdumpf.html">http://www.packetlevel.ch/html/tcpdumpf.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '11, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Dec '11, 12:58</p></div></div><div id="comments-container-8046" class="comments-container"><span id="8061"></span><div id="comment-8061" class="comment"><div id="post-8061-score" class="comment-score"></div><div class="comment-text"><p>io,stat<br />
a. The command line process does not end on its own, but keeps recording in 120 sec intervals, until killed (Ctrl-C) - and then only writes to the output file. Is there an option to have the process end on its own?<br />
b. Can I add the option -f "tcp dst port 8080" in the command line as well?<br />
<br />
output to capture file<br />
a. Can I add the "tcp dst port 8080" in capture filter?<br />
b. The "syn-http.request.get.pcap" file is written continually or at the end?<br />
c. Can I use the -r option with that file to count tcp &amp; http, as described in your previous post?</p></div><div id="comment-8061-info" class="comment-info"><span class="comment-age">(20 Dec '11, 14:36)</span> adonies</div></div><span id="8062"></span><div id="comment-8062" class="comment"><div id="post-8062-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>The command line process does not end on its own, but keeps recording in 120 sec intervals, until killed (Ctrl-C) - and then only writes to the output file. Is there an option to have the process end on its own?</p></blockquote><p>To stop the capture after a timeout, use tshark's <a href="http://www.wireshark.org/docs/man-pages/tshark.html#a_capture_autostop_condition">-a flag with duration</a>:</p><pre><code>$ tshark -a duration:120</code></pre></div><div id="comment-8062-info" class="comment-info"><span class="comment-age">(20 Dec '11, 15:15)</span> helloworld</div></div><span id="8063"></span><div id="comment-8063" class="comment"><div id="post-8063-score" class="comment-score"></div><div class="comment-text"><p>io,stat<br />
a. Thanks helloworld:)<br />
For Statistics you can also use 0 (=no interval)<br />
tshark -i 3 -qz "io,stat,0,COUNT(tcp.flags)tcp.flags==0x02"<br />
b. Yes: tshark -i 3 -f "tcp dst port 8080" -qz "io,stat,120,COUNT(tcp.flags)tcp.flags==0x02" -z "io,stat,120,COUNT(http.request.method)http.request.method=="GET"" &gt; io-stat-dstport8080.txt<br />
<br />
</p></div><div id="comment-8063-info" class="comment-info"><span class="comment-age">(20 Dec '11, 22:19)</span> joke</div></div><span id="8064"></span><div id="comment-8064" class="comment"><div id="post-8064-score" class="comment-score"></div><div class="comment-text"><p>output to capture file<br />
a. tshark -i 3 -f "(tcp dst port 8080) &amp;&amp; (tcp[13]=0x02 or tcp[20:4]=0x47455420)" -w syn-http.request.get.dstport8080.pcap<br />
b.<br />
c. You can run TShark twice (or even more):<br />
use one instance to capture the traffic and another instance for statistics<br />
</p></div><div id="comment-8064-info" class="comment-info"><span class="comment-age">(20 Dec '11, 22:21)</span> joke</div></div></div><div id="comment-tools-8046" class="comment-tools"></div><div class="clear"></div><div id="comment-8046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8071"></span>

<div id="answer-container-8071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8071-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your webserver tells you it served 33.280 objects and wireshark tells you it saw 33.280 http requests then all requests that were on the wire did get a response. Now your client tells you it requested 33.528 objects. So in 248 cases it was not able to get the request on the wire.</p><p>Combine that with the fact that you saw 41.478 TCP/SYN packets, then you can imagine that there was a problem opening TCP sessions to the server. This can be either because the server was too busy to handle all the incoming connections, but this seems illogical as all HTTP requests were properly answered. It could also be that the webserver has a configured limit on the amount of concurrent sessions it can handle and you hit that limit. This would explain the SYN retransmissions and when it fails to get a TCP connection at all, the missing requests.</p><p><em>BTW It's better to use the capture filter "tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420" to capture the GET requests, as this filter will work even when there are TCP options in the packet (it looks at the TCP header length and skips the proper amount of bytes to get to the TCP payload).</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '11, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-8071" class="comments-container"><span id="8080"></span><div id="comment-8080" class="comment"><div id="post-8080-score" class="comment-score"></div><div class="comment-text"><p>Capture filter "tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420"<br />
Visit the <a href="http://www.wireshark.org/lists/">Wireshark Mailing List</a> to read <a href="http://www.wireshark.org/lists/wireshark-users/201003/msg00024.html">Sake's explanation</a> of this capture filter.</p></div><div id="comment-8080-info" class="comment-info"><span class="comment-age">(22 Dec '11, 07:44)</span> joke</div></div><span id="8083"></span><div id="comment-8083" class="comment"><div id="post-8083-score" class="comment-score"></div><div class="comment-text"><p>Is there a procedure in the TCP protocol spec for TCP/SYN retransmission?<br />
Or is it implementation specific, configured to decide that the connection was refused after X retries?</p></div><div id="comment-8083-info" class="comment-info"><span class="comment-age">(22 Dec '11, 12:46)</span> adonies</div></div><span id="8089"></span><div id="comment-8089" class="comment"><div id="post-8089-score" class="comment-score"></div><div class="comment-text"><p>The <a href="http://tools.ietf.org/html/rfc793">TCP spec</a> doesn't give a detailed procedure for retransmission; different implementations can use different retransmission timers and different count values for when it's time to give up.</p></div><div id="comment-8089-info" class="comment-info"><span class="comment-age">(22 Dec '11, 15:20)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8071" class="comment-tools"></div><div class="clear"></div><div id="comment-8071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8082"></span>

<div id="answer-container-8082" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8082-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you joke, helloworld, SYNbit and Guy Harris for your answers. I think I got the problem under control now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '11, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/b6ab78997ac26efb7a11ea254f8bcc76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adonies&#39;s gravatar image" /><p>adonies<br />
<span class="score" title="12 reputation points">12</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adonies has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Dec '11, 10:53</p></div></div><div id="comments-container-8082" class="comments-container"></div><div id="comment-tools-8082" class="comment-tools"></div><div class="clear"></div><div id="comment-8082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

