+++
type = "question"
title = "&quot;coap13&quot; isn&#x27;t a valid Capture filter (syntax error)"
description = '''I am working with wireshark(tshark). I want to capture specific protocol like ipv6, coap13 etc. i added coap13.lua file.  i tried to capture ipv6 with  &quot;tshark.exe&quot; -i 3 -f &quot;ip6&quot; -a duration:400 -a filesize:20480 -a files:512 -w &quot;C:&#92;Packet_Capture.pcap&quot; it runs well  but when i want to capture CoAP ...'''
date = "2014-03-04T02:54:00Z"
lastmod = "2014-03-04T03:14:00Z"
weight = 30387
keywords = [ "wireshark", "lua", "capture-filter", "coap", "packet-capture" ]
aliases = [ "/questions/30387" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ["coap13" isn't a valid Capture filter (syntax error)](/questions/30387/coap13-isnt-a-valid-capture-filter-syntax-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30387-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working with wireshark(tshark). I want to capture specific protocol like ipv6, coap13 etc. i added coap13.lua file.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/aaa.png" alt="alt text" /></p><p>i tried to capture ipv6 with "tshark.exe" -i 3 -f "ip6" -a duration:400 -a filesize:20480 -a files:512 -w "C:\Packet_Capture.pcap"</p><p>it runs well</p><p>but when i want to capture CoAP or CoAP13 with</p><p>"tshark.exe" -i 3 -f "coap13" -a duration:400 -a filesize:20480 -a files:512 -w "C:\Packet_Capture.pcap"</p><p>it didn't work.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/bbbb.png" alt="alt text" /></p><p>What is the syntax to capture CoAP protocol? Where can i find the list(syntax) for capture filter?</p></div><div id="question-tags" class="tags-container tags">wireshark lua capture-filter coap packet-capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '14, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/a717f574f006b4977952372192a67e7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amrit&#39;s gravatar image" /><p>Amrit<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amrit has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 04 Mar '14, 02:54</p></div></div><div id="comments-container-30387" class="comments-container"></div><div id="comment-tools-30387" class="comment-tools"></div><div class="clear"></div><div id="comment-30387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30388"></span>

<div id="answer-container-30388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30388-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As per the error message, display filters and capture filters are different. Also as per the error message, the <a href="http://www.wireshark.org/docs/wsug_html_chunked/">Users Guide</a> has informative sections on <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayFilterSection.html">display</a> and <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html">capture</a> filters with links to other topics of interest.</p><p>In your particular case there is no explicit capture filter syntax for the protocols CoAP or CoAP13, but you could use <code>udp port 5683</code> if the CoAP traffic is on the registered port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '14, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-30388" class="comments-container"></div><div id="comment-tools-30388" class="comment-tools"></div><div class="clear"></div><div id="comment-30388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

