+++
type = "question"
title = "tshark print dns query hostname and http hostnames"
description = '''Find a tshark command that can print the following: go through all packets,  if it dns request, print  pktNum DNS dns.qry.name  if it is HTTP request, print  pktNum HTTP http.host '''
date = "2015-12-20T07:56:00Z"
lastmod = "2015-12-21T23:55:00Z"
weight = 48648
keywords = [ "tshark" ]
aliases = [ "/questions/48648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark print dns query hostname and http hostnames](/questions/48648/tshark-print-dns-query-hostname-and-http-hostnames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48648-score" class="post-score" title="current number of votes">0</div><span id="post-48648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Find a tshark command that can print the following:</p><pre><code>go through all packets,
    if it dns request, print
       pktNum  DNS  dns.qry.name
    if it is HTTP request, print
       pktNum HTTP http.host</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '15, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-48648" class="comments-container"></div><div id="comment-tools-48648" class="comment-tools"></div><div class="clear"></div><div id="comment-48648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48649"></span>

<div id="answer-container-48649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48649-score" class="post-score" title="current number of votes">0</div><span id="post-48649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm afraid the <code>ТCP</code> and <code>HTTP</code> strings are only displayed as contents of "protocol" column in the packet list pane, and they always indicate the topmost client protocol in the frame, so eventual http packets carrying some payload object would not be displayed even if a corresponding field name would be available inside them.</p><p>So try <code>-T fields -e frame.number -e frame.protocols -e dns.qry.name -e http.host -Y "dns.qry.name or http.host"</code>, you'll get the full list of protocol layers identified in each packet, and you'll have to use some post-process if necessary.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '15, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48649" class="comments-container"><span id="48653"></span><div id="comment-48653" class="comment"><div id="post-48653-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@sindy</span> for the tip, it's almost there. The <code>-e dns.qry.name</code> will catch both the host name in request and reply. Is there a way to skip DNS responses?</p></div><div id="comment-48653-info" class="comment-info"><span class="comment-age">(20 Dec '15, 16:07)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="48654"></span><div id="comment-48654" class="comment"><div id="post-48654-score" class="comment-score"></div><div class="comment-text"><p>Sure there is.</p><p>As it seems you don't have a possibility to use GUI Wireshark, all the protocol fields that can be chosen for display using <code>-e</code> as well for filtering using <code>-Y</code> or <code>-R</code> in tshark (see the difference between <code>-Y</code> and -R <a href="https://www.wireshark.org/docs/man-pages/tshark.html">here</a>) are listed <a href="https://www.wireshark.org/docs/dfref/">here</a>.</p><p>If you can use a GUI Wireshark, it is much more straightforward (especially if you are not familiar with your protocol of interest) to choose a packet which contains what you need, go to the packet dissection pane, unfold the protocol which you are interested in, and select the lines representing field dissections which seem to you as perspective candidates for being printed using <code>-e</code> or becoming part of the <code>-Y</code> or <code>-R</code> filter conditions. When a line is selected, the field name in a display filter format is displayed in the bottom part of the window frame. On top of that, you can right-click the line and choose e.g. <code>Prepare as filter -&gt; ...or Selected</code> to extend the existing display filter in the required way, without applying the change immediately.</p><p>So in case of a DNS query, the packet dissection looks like follows:</p><p><code>Frame 947: 71 bytes on wire (568 bits), 71 bytes captured (568 bits) on interface 0 Ethernet II, Src: 1c:3a:51:4c:47:74, Dst: 00:1e:56:71:9a:d3 Internet Protocol Version 4, Src: 192.168.15.160, Dst: 192.168.15.1 User Datagram Protocol, Src Port: 50670 (50670), Dst Port: 53 (53) Domain Name System (query)     [Response In: 948]     Transaction ID: 0x5acf     Flags: 0x0100 Standard query         0... .... .... .... = Response: Message is a query         .000 0... .... .... = Opcode: Standard query (0)         .... ..0. .... .... = Truncated: Message is not truncated         .... ...1 .... .... = Recursion desired: Do query recursively         .... .... .0.. .... = Z: reserved (0)         .... .... ...0 .... = Non-authenticated data: Unacceptable     Questions: 1     Answer RRs: 0     Authority RRs: 0     Additional RRs: 0     ...</code></p><p>You select (i.e. left-click) the line <code>Questions: 1</code> and in the bottom of the window frame you'll see the field name: <code>dns.count.queries</code>. So you'll modify the <code>-Y</code> part of the tshark filter to <code>-Y "(dns.qry.name and dns.count.queries &gt; 0) or http.host"</code> and you are there. Or you can use <code>dns.flags.response == 0</code> instead, but purely theoretically there may be a query carrying no question.</p></div><div id="comment-48654-info" class="comment-info"><span class="comment-age">(21 Dec '15, 00:00)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48666"></span><div id="comment-48666" class="comment"><div id="post-48666-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@sindy</span>, I tried <code>tshark -r 2015-12-21-threatglass.pcap -T fields -e frame.number -e frame.protocols -e dns.qry.name -e http.host -Y "(dns.qry.name and dns.count.queries &gt; 0) or http.host"</code> but still see the output contains for both DNS request and DNS query.</p></div><div id="comment-48666-info" class="comment-info"><span class="comment-age">(21 Dec '15, 20:53)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="48667"></span><div id="comment-48667" class="comment"><div id="post-48667-score" class="comment-score"></div><div class="comment-text"><p>Okay, so replace the <code>dns.count.queries &gt; 0</code> with <code>dns.flags.response == 0</code> . The <code>dns.qry.name</code> in the <code>-Y</code> should be enough to eliminate packets without any queried name, even without <code>dns.count.queries &gt; 0</code>. Just check how a PTR query looks like (as I'm not sure whether the IP address you want to resolve into name will be displayed as <code>dns.qry.name</code>). You can generate one using <code>nslookup ip.add.re.ss</code> on Windows or <code>dig -x ip.add.re.ss</code> on Linux.</p></div><div id="comment-48667-info" class="comment-info"><span class="comment-age">(21 Dec '15, 23:55)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48649" class="comment-tools"></div><div class="clear"></div><div id="comment-48649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

