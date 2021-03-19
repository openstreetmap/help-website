+++
type = "question"
title = "exporting payload data in binary file"
description = '''Hi, I have successfully created a filter and captured the packets I need. I have looked at the various save and export options in Wireshark, and fail to find an option to save only the payload data in a binary file without any file headers or formatting. Is this possible in Wireshark, or do I need t...'''
date = "2014-08-10T01:36:00Z"
lastmod = "2014-08-10T06:24:00Z"
weight = 35353
keywords = [ "binary", "export", "payload" ]
aliases = [ "/questions/35353" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [exporting payload data in binary file](/questions/35353/exporting-payload-data-in-binary-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35353-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have successfully created a filter and captured the packets I need. I have looked at the various save and export options in Wireshark, and fail to find an option to save only the payload data in a binary file without any file headers or formatting.</p><p>Is this possible in Wireshark, or do I need to create some sort of script to do this?</p><p>Thanks in advance for any replies.</p></div><div id="question-tags" class="tags-container tags">binary export payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '14, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/e3caffe7a16a0a1ee8e85f945a47d568?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yulquen&#39;s gravatar image" /><p>yulquen<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yulquen has no accepted answers">0%</span></p></div></div><div id="comments-container-35353" class="comments-container"></div><div id="comment-tools-35353" class="comment-tools"></div><div class="clear"></div><div id="comment-35353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35364"></span>

<div id="answer-container-35364" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35364-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is this possible in Wireshark, or do I need to create some sort of script to do this?</p></blockquote><p>Wireshark</p><ul><li>right click on one of the frames and select "Follow TCP Stream" (or "Follow UDP Stream"). In the pop-up windows select the bytes you are interested in and save them in <strong>raw</strong> format.</li><li>or use the Wireshark Export options: <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html">http://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html</a></li></ul><p>Scripting:</p><ul><li>You could use tshark</li><li>or write a <a href="http://www.wireshark.org/docs/wsug_html_chunked/wslua_tap_example.html">TAP/Listener with Lua</a></li></ul><p>tshark examples:</p><blockquote><p><a href="http://ask.wireshark.org/questions/23827/get-tcp-and-udp-payloads-with-tshark">http://ask.wireshark.org/questions/23827/get-tcp-and-udp-payloads-with-tshark</a><br />
<a href="http://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only">http://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only</a><br />
run <strong><code>tshark -nr input.pcap -Vx</code></strong> and then parse the output</p></blockquote><p>Lua Examples:</p><blockquote><p><a href="http://wiki.wireshark.org/Lua/Examples">http://wiki.wireshark.org/Lua/Examples</a><br />
<a href="http://wiki.wireshark.org/Lua/Taps">http://wiki.wireshark.org/Lua/Taps</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Aug '14, 06:25</p></div></div><div id="comments-container-35364" class="comments-container"><span id="35386"></span><div id="comment-35386" class="comment"><div id="post-35386-score" class="comment-score"></div><div class="comment-text"><p>Follow TCP stream seems to be the easiest solution, but there seems to be a limitation.</p><p>When I select the first packet and Follow TCP stream, only a small part of the data is available (about 204KB of 16MB's of data capture). Saving as raw gives me the payload data I wanted, but only a small fraction of the whole data set.</p></div><div id="comment-35386-info" class="comment-info"><span class="comment-age">(10 Aug '14, 13:14)</span> yulquen</div></div><span id="35387"></span><div id="comment-35387" class="comment"><div id="post-35387-score" class="comment-score"></div><div class="comment-text"><p>did you limit the frame size during the capture phase?</p><p>Please check if <strong>bytes on wire</strong> and <strong>bytes captured</strong> (Frame layer) are identical.</p></div><div id="comment-35387-info" class="comment-info"><span class="comment-age">(10 Aug '14, 14:09)</span> Kurt Knochner ♦</div></div><span id="35388"></span><div id="comment-35388" class="comment"><div id="post-35388-score" class="comment-score"></div><div class="comment-text"><p>They are the same (1514 bytes).</p><p>My capture have 10881 packets. If I select a "Follow TCP stream" the dropdown says "Entire conversation (204400 bytes)" and when I do a raw save, thats how big my file gets.</p><p>TCP segment length is 1460 so it amounts to payload from exactly 140 packets instead of 10881.</p></div><div id="comment-35388-info" class="comment-info"><span class="comment-age">(10 Aug '14, 14:32)</span> yulquen</div></div><span id="35389"></span><div id="comment-35389" class="comment"><div id="post-35389-score" class="comment-score"></div><div class="comment-text"><p>hm.. could be a bug. What is your</p><ul><li>OS and OS version</li><li>Wireshark version</li></ul></div><div id="comment-35389-info" class="comment-info"><span class="comment-age">(10 Aug '14, 14:53)</span> Kurt Knochner ♦</div></div><span id="35391"></span><div id="comment-35391" class="comment"><div id="post-35391-score" class="comment-score"></div><div class="comment-text"><ul><li>win7 pro 64bit sp1</li><li>wireshark Version 1.12.0 (v1.12.0-0-g4fab41a from master-1.12)</li></ul></div><div id="comment-35391-info" class="comment-info"><span class="comment-age">(11 Aug '14, 00:39)</span> yulquen</div></div><span id="35394"></span><div id="comment-35394" class="comment not_top_scorer"><div id="post-35394-score" class="comment-score"></div><div class="comment-text"><p>can you please try version 1.10.9?</p></div><div id="comment-35394-info" class="comment-info"><span class="comment-age">(11 Aug '14, 02:44)</span> Kurt Knochner ♦</div></div><span id="35395"></span><div id="comment-35395" class="comment not_top_scorer"><div id="post-35395-score" class="comment-score"></div><div class="comment-text"><p>done, same result.</p></div><div id="comment-35395-info" class="comment-info"><span class="comment-age">(11 Aug '14, 03:18)</span> yulquen</div></div><span id="35398"></span><div id="comment-35398" class="comment not_top_scorer"><div id="post-35398-score" class="comment-score"></div><div class="comment-text"><p>well, then it's probably related to your capture file. Is there any special protocol on top of TCP that Wireshark 'detetcs', like SMTP, HTTP, etc.?</p></div><div id="comment-35398-info" class="comment-info"><span class="comment-age">(11 Aug '14, 04:11)</span> Kurt Knochner ♦</div></div><span id="35400"></span><div id="comment-35400" class="comment not_top_scorer"><div id="post-35400-score" class="comment-score"></div><div class="comment-text"><p>The packet details only lists Ethernet II, IP V4 and TCP for all packets.</p><p>If I disable all other protocols, theres an additional listing for data (1460 bytes). But even so, selecting "Follow TCP stream", it still says 204400 bytes in total. Looking av the raw export file in a hex-viewer, it is clear that Wireshark just exports the payload from the 140 first frames, and leaves the rest of them out .</p></div><div id="comment-35400-info" class="comment-info"><span class="comment-age">(11 Aug '14, 04:43)</span> yulquen</div></div><span id="35403"></span><div id="comment-35403" class="comment not_top_scorer"><div id="post-35403-score" class="comment-score"></div><div class="comment-text"><blockquote><p>it is clear that Wireshark just exports the payload from the 140 first frames, and leaves the rest of them out .</p></blockquote><p>hm... sounds like a bug. Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and add a reference to this question. Please add as much information as possible, e.g. a smaller capture file that helps to reproduce the problem.</p></div><div id="comment-35403-info" class="comment-info"><span class="comment-age">(11 Aug '14, 05:34)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-35364" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-35364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

