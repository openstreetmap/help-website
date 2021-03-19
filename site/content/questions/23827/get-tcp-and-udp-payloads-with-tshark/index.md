+++
type = "question"
title = "Get tcp and udp payloads with TSHARK"
description = '''Hi. I use tshark to export packet information from a pcap file and it works well. I now need to export the tcp&#92;udp payload as well. I have looked at several answers -  http://ask.wireshark.org/questions/3323/printing-tcp-payload-using-tshark-t-fields and http://ask.wireshark.org/questions/12431/how-...'''
date = "2013-08-16T11:02:00Z"
lastmod = "2013-09-22T18:45:00Z"
weight = 23827
keywords = [ "tshark" ]
aliases = [ "/questions/23827" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get tcp and udp payloads with TSHARK](/questions/23827/get-tcp-and-udp-payloads-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23827-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>I use tshark to export packet information from a pcap file and it works well. I now need to export the tcp\udp payload as well. I have looked at several answers - <a href="http://ask.wireshark.org/questions/3323/printing-tcp-payload-using-tshark-t-fields">http://ask.wireshark.org/questions/3323/printing-tcp-payload-using-tshark-t-fields</a> and <a href="http://ask.wireshark.org/questions/12431/how-to-add-data-length-column-in-wireshark-display-or-plot-payload-length-vs-packet-no">http://ask.wireshark.org/questions/12431/how-to-add-data-length-column-in-wireshark-display-or-plot-payload-length-vs-packet-no</a> and they both claim</p><p>-e tcp.data</p><p>should work. However, I only get an empty field.</p><p>I'm using Wireshark 1.10.1 on windows 7 64 bit.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '13, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/eb19c4016864033ca12788883d2c251e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vadgros&#39;s gravatar image" /><p>vadgros<br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vadgros has no accepted answers">0%</span></p></div></div><div id="comments-container-23827" class="comments-container"></div><div id="comment-tools-23827" class="comment-tools"></div><div class="clear"></div><div id="comment-23827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25086"></span>

<div id="answer-container-25086" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25086-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There may be another way to do this, but I think if you [<em>at least temporarily</em>] disable all relevant upper-layer protocols, then I believe you will be able to get what you need.</p><p>For example, suppose you want to export all TCP data, which happens to be http traffic. First, in Wireshark, disable the http protocol via: <code>Analyze -&gt; Enabled Protocols -&gt; HTTP -&gt; [deselect] -&gt; OK</code>, and then quit Wireshark. This could even be done <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCustConfigProfilesSection.html">in a new profile</a>, let's call that profile, "<em>Export</em>". You could then have <a href="http://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> use that profile whenever you need to perform this task.</p><p>After that, you would run something along the lines of:</p><pre><code>tshark -r infile.pcap -C Export -T fields -e data</code></pre><p>You may need/want to apply a filter via <code>-Y "filter"</code> or <code>-2R "filter"</code> to select only those packets of interest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '13, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25086" class="comments-container"></div><div id="comment-tools-25086" class="comment-tools"></div><div class="clear"></div><div id="comment-25086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

