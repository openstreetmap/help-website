+++
type = "question"
title = "What should I see in capture when there is TCP error: Could not connect to the server?"
description = '''I&#x27;m investigating some strange error on OS X. When I&#x27;m sending multiple HTTP request to one host. One of the HTTP request sent in the middle receives an error &quot;Error Domain=NSURLErrorDomain Code=-1004 &quot;Could not connect to the server.&quot;&quot;. I&#x27;ve limited connection per host to 1. I&#x27;ve noticed that this ...'''
date = "2016-08-13T00:57:00Z"
lastmod = "2016-08-13T06:00:00Z"
weight = 54778
keywords = [ "filter", "connection", "tcp", "error" ]
aliases = [ "/questions/54778" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What should I see in capture when there is TCP error: Could not connect to the server?](/questions/54778/what-should-i-see-in-capture-when-there-is-tcp-error-could-not-connect-to-the-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54778-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm investigating some strange error on OS X. When I'm sending multiple HTTP request to one host. One of the HTTP request sent in the middle receives an error "Error Domain=NSURLErrorDomain Code=-1004 "Could not connect to the server."". I've limited connection per host to 1. I've noticed that this error appears when number of connection per host is lower than number of HTTP requests sent in single time. I can see this issue only with some servers.</p><p>Now I need verify that this issue is caused by Apple library not by actual error in network traffic. When I'm looking on thing which Wireshark captured everything looks fine to me. I'm not very good with TCP protocol so my question is what shall I see in Wireshark when I have this kind of errors.</p><p>I used filter: <code>ip.addr == &lt;server ip&gt;</code> and all entries are "green".</p><p>So what kind of TCP packet should I see if connection to server can't be established?</p></div><div id="question-tags" class="tags-container tags">filter connection tcp error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '16, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/afdd5d793e560990654ac95622b3ef42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marek%20R&#39;s gravatar image" /><p>Marek R<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marek R has no accepted answers">0%</span></p></div></div><div id="comments-container-54778" class="comments-container"></div><div id="comment-tools-54778" class="comment-tools"></div><div class="clear"></div><div id="comment-54778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54779"></span>

<div id="answer-container-54779" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54779-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should see connections with just a SYN packet, or a SYN packet with an Reset packet coming back in as a response. Easiest way to find those is by using the Statistics menu, and choosing "Conversations". Select the TCP tab, and check if you see any connection to the server IP that has less than 4 packets (SYN packets are often resend to retry). If you find one, use the popup menu to filter on it "A&lt;-&gt;B", meaning both directions.</p><p>My guess is that your problem is not an error at all - if you limit connections per host to 1 (or, as you say, less than HTTP requests) there's going to be a problem. I don't know OS X, so I guess this is some kind of firewall setting. If a web page needs n requests to pull all page content, and you set the limit to n-1, the kernel will stop at n-1 and not make the final connection at all. If you set the limit to 1, only one connection will be made. At least that's what I experience on my firewall.</p><p>Keep in mind that, depending on the target server, HTTP may be forced to open <strong>multiple</strong> TCP connections to pull all content. This happens when the HTTP server is either using HTTP/1.0 or if it refuses the "connection: keep alive" option and tears down the connection. If you limit your TCP connections per host to 1 (or anything less than the number of required connections), you're in trouble. It will only work for hosts that can keep a TCP connection open to pull the remaining content.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '16, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54779" class="comments-container"><span id="54792"></span><div id="comment-54792" class="comment"><div id="post-54792-score" class="comment-score"></div><div class="comment-text"><p>so if I use filer: <code>ip.addr == &lt;server ip&gt; &amp;&amp; tcp.flags.reset == 1</code> I should be able localize all occurrences of this error? If this filter is Ok than this must be a bug in <code>NSURLSession</code>. Conversation view doesn't show any errors, every entry for each "Port A" has at least 4 packets.</p></div><div id="comment-54792-info" class="comment-info"><span class="comment-age">(14 Aug '16, 05:52)</span> Marek R</div></div><span id="54794"></span><div id="comment-54794" class="comment"><div id="post-54794-score" class="comment-score"></div><div class="comment-text"><p>The conversations view will show you the individual sessions as individual lines at the TCP tab, as each of the TCP sessions from the same client to the same server uses a different ephemeral port (the dynamically assigned one at client side). Use a display filter <code>ip.addr == &lt;server ip&gt;</code> in the main window and tick the "limit to display filter" in the conversations window.</p><p>The way how the session is rejected outside your machine (if it is) may vary:</p><ul><li><p>if the error is reported immediately, you should see packets with <code>tcp.flags.reset == 1 or tcp.flags.fin == 1</code> if it is rejected by something outside your machine.</p></li><li><p>if it takes many tens of seconds, you should see several repetitions of a SYN packet (<code>tcp.flags.syn == 1</code>) from the same ephemeral port, but no response to any of them. But as you say everything is "green", I do not expect any SYN retransmissions.</p></li></ul></div><div id="comment-54794-info" class="comment-info"><span class="comment-age">(14 Aug '16, 06:12)</span> sindy</div></div></div><div id="comment-tools-54779" class="comment-tools"></div><div class="clear"></div><div id="comment-54779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

