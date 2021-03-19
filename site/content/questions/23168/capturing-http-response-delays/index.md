+++
type = "question"
title = "Capturing http response delays"
description = '''Can someone tell me how I set this up for capture? I&#x27;m trying to discover delayed http responses to http requests from a particular PC on our LAN. It&#x27;s IP address is 192.168.1.73. I don&#x27;t know the web server&#x27;s address yet but I will in a minute so we can just make one up for now for this discussion....'''
date = "2013-07-19T11:33:00Z"
lastmod = "2013-07-22T06:33:00Z"
weight = 23168
keywords = [ "delay", "http", "response" ]
aliases = [ "/questions/23168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing http response delays](/questions/23168/capturing-http-response-delays)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone tell me how I set this up for capture? I'm trying to discover delayed http responses to http requests from a particular PC on our LAN. It's IP address is 192.168.1.73. I don't know the web server's address yet but I will in a minute so we can just make one up for now for this discussion.</p></div><div id="question-tags" class="tags-container tags">delay http response</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '13, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/20f542ee7a1e0c461a355c8371fceda2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WineGeek&#39;s gravatar image" /><p>WineGeek<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WineGeek has no accepted answers">0%</span></p></div></div><div id="comments-container-23168" class="comments-container"></div><div id="comment-tools-23168" class="comment-tools"></div><div class="clear"></div><div id="comment-23168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23230"></span>

<div id="answer-container-23230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23230-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would do it this way.</p><p>Display filter: <code>ip.addr eq 192.168.1.73 and (http.request or http.response)</code><br />
</p><p>Then set the <strong>Time</strong> column to the following format</p><blockquote><p><code>View -&gt; Time Display Format -&gt; Seconds Since Beginning of Capture</code><br />
</p></blockquote><p>As the client is also able to send several requests at the same time (in different TCP connections) you need to check the TCP Stream number as well. For this purpose, please add a new column in the GUI for the tcp.stream value. Here is how to do this</p><blockquote><p><code>Edit -&gt; Preferences -&gt; User Interface -&gt; Columns</code><br />
</p></blockquote><p>Add a column called "TCP Stream". Then choose <strong>Custom</strong> as type and <strong>tcp.stream</strong> as value.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/preferences.png" alt="GUI column preferences" /></p><p>Then sort the GUI by the "TCP Stream" column.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/gui_1.png" alt="GUI" /></p><p>Then use a <strong>Time Reference</strong> (CTRL-T in the GUI) for easy delta time calculation between request and response. As you can see the 'delay' (delta) between request and response is 2.144 seconds for the first request and 0.2605 for the second request.</p><p>You can also use tshark with some scripting:</p><blockquote><p><code>tshark -nr input.pcap -R "ip.addr eq 192.168.1.73 and (http.request or http.response)" -T fields -e frame.number -e frame.time_relative  -e ip.src -e ip.dst -e tcp.stream -e http.request.full_uri -e http.response.code -e http.response.phrase</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div></div><div id="comments-container-23230" class="comments-container"></div><div id="comment-tools-23230" class="comment-tools"></div><div class="clear"></div><div id="comment-23230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

