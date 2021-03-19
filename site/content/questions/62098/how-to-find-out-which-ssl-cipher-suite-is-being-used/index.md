+++
type = "question"
title = "How to find out which SSL cipher suite is being used?"
description = '''I am using an app which says it uses ssl v3 to transporrt data. After running an ssl test I see that the server supports tls 1.1,1.2 and ssl v3 so I open Wirehsark and connect iphone with it by rvi setting. In that it says the protocol being used is tcp and then http. I&#x27;m confused. I basically want ...'''
date = "2017-06-18T04:03:00Z"
lastmod = "2017-06-23T10:48:00Z"
weight = 62098
keywords = [ "ciphersuite", "ssl" ]
aliases = [ "/questions/62098" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to find out which SSL cipher suite is being used?](/questions/62098/how-to-find-out-which-ssl-cipher-suite-is-being-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62098-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using an app which says it uses ssl v3 to transporrt data. After running an ssl test I see that the server supports tls 1.1,1.2 and ssl v3 so I open Wirehsark and connect iphone with it by rvi setting. In that it says the protocol being used is tcp and then http. I'm confused. I basically want to find which cipher suite is being used. Is it possible to find this out?</p></div><div id="question-tags" class="tags-container tags">ciphersuite ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '17, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/84d44d0e27315ce6cd8571c2a00d43c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bangbam&#39;s gravatar image" /><p>bangbam<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bangbam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jun '17, 13:52</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-62098" class="comments-container"><span id="62140"></span><div id="comment-62140" class="comment"><div id="post-62140-score" class="comment-score"></div><div class="comment-text"><p>I don't think you've actually captured the SSL traffic. Are you capturing on the right port? Maybe visit the <a href="https://wiki.wireshark.org/SSL">Wireshark SSL wiki page</a> for more information?</p></div><div id="comment-62140-info" class="comment-info"><span class="comment-age">(19 Jun '17, 13:54)</span> cmaynard ♦♦</div></div><span id="62261"></span><div id="comment-62261" class="comment"><div id="post-62261-score" class="comment-score"></div><div class="comment-text"><p>ok then how can i determine which protocol is being used</p></div><div id="comment-62261-info" class="comment-info"><span class="comment-age">(23 Jun '17, 07:47)</span> bangbam</div></div></div><div id="comment-tools-62098" class="comment-tools"></div><div class="clear"></div><div id="comment-62098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62265"></span>

<div id="answer-container-62265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62265-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may have already seen this resource, but others may find it useful: "Getting a Packet Trace" from Apple's Developer Technical Q&amp;A: <a href="https://developer.apple.com/library/content/qa/qa1176/_index.html#//apple_ref/doc/uid/DTS10001707-CH1-SECIOSPACKETTRACING">https://developer.apple.com/library/content/qa/qa1176/_index.html#//apple_ref/doc/uid/DTS10001707-CH1-SECIOSPACKETTRACING</a> (This covers both MacOS and iOS)</p><p>I don't have a Mac, but the linked document suggests that an rvi interface can be treated pretty much like any other...I don't know how well Wireshark supports capturing on rvi interfaces, so you can use tcpdump.</p><p>If your RVI is set up and started properly, you should be able to use tcpdump to capture only SSL/TLS traffic by specifying TCP port 443, like so (rviX is your RVI interface):</p><p>sudo tcpdump 'tcp port 443' -i rviX -w mytrace.pcap</p><p>[run your tests]</p><p>[end tcpdump]</p><p>If you want to capture both HTTP and HTTPS traffic, try:</p><p>sudo tcpdump 'tcp port 80 or tcp port 443' -i rviX -w mytrace.pcap</p><p>[run your tests]</p><p>[end tcpdump]</p><p>Once you have this pcap file, you can load it in Wireshark and identify cipher suites as follows:</p><p>1) Use Statistics-&gt;Conversations (in the main menu) to list conversations contained in the capture file, like so: <img src="https://osqa-ask.wireshark.org/upfiles/tls_find_conversation.jpg" alt="Statistics-&gt;Conversations display" /></p><p>2) Highlight the specific conversation in which you're interested, and use 'Follow Stream' in the Conversations dialog to display that conversation. Dismiss the 'raw data' display that pops up; we won't need that for what we're doing.</p><p>3) In the the main Wireshark display:</p><ul><li>Highlight the 'Client Hello' packet in the top pane of the display - you can drill down to the list of cipher suites offered by the client in the center pane, like so: <img src="https://osqa-ask.wireshark.org/upfiles/tls_client_hello.jpg" alt="TLS Client Hello" /></li><li>Highlight the 'Server Hello' packet - you can drill down to the cipher suite chosen by the server in the center pane, like so:</li></ul><p><img src="https://osqa-ask.wireshark.org/upfiles/tls_server_hello.jpg" alt="TLS Server Hello" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '17, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '17, 14:39</p></div></div><div id="comments-container-62265" class="comments-container"></div><div id="comment-tools-62265" class="comment-tools"></div><div class="clear"></div><div id="comment-62265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

