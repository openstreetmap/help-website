+++
type = "question"
title = "Filtering in wireshark is extremely slow compared to tshark"
description = '''I have a capture file with Modbus/RTU traffic. I&#x27;m using user DLT to set it as mbrtu protocol. The file contains about 450000 packets. I would like to apply this filter in wireshark !(mbrtu.unit_id==50 || mbrtu.unit_id==49) || mbrtu.crc16.incorrect  but it tooks about 15 minutes to perform filtering...'''
date = "2017-03-23T13:21:00Z"
lastmod = "2017-04-04T04:13:00Z"
weight = 60294
keywords = [ "filter", "display-filter" ]
aliases = [ "/questions/60294" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering in wireshark is extremely slow compared to tshark](/questions/60294/filtering-in-wireshark-is-extremely-slow-compared-to-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60294-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture file with Modbus/RTU traffic. I'm using user DLT to set it as mbrtu protocol. The file contains about 450000 packets. I would like to apply this filter in wireshark</p><pre><code>!(mbrtu.unit_id==50 || mbrtu.unit_id==49) || mbrtu.crc16.incorrect</code></pre><p>but it tooks about 15 minutes to perform filtering. In tshark using following command, it tooks just 7 seconds with the same result.</p><pre><code>tshark -2 -R &quot;!(mbrtu.unit_id==50 || mbrtu.unit_id==49) || mbrtu.crc16.incorrect&quot; -r rs485.pcap -w errors.pcap</code></pre><p>When i split input file using <code>editpcap</code> command to chunks with just 50000 packets, it tooks 3 seconds in wireshark to perform filtering for that file. Simple linear approximation told me, that it should took 9*3=27 seconds to process original file and not 900 seconds.</p><p>I'm using Wireshark 2.2.5 on Linux. I have Intel [email protected] and 8GB of RAM. Wireshark takes just 300 MB of RAM and utilizes one core at 100%.</p><p>Am I doing something wrong? Is there some way to speed up the wireshark gui?</p></div><div id="question-tags" class="tags-container tags">filter display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '17, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/09eeee14385ba75f18adb473ccffe208?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j123b567&#39;s gravatar image" /><p>j123b567<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j123b567 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Mar '17, 13:26</p></div></div><div id="comments-container-60294" class="comments-container"></div><div id="comment-tools-60294" class="comment-tools"></div><div class="clear"></div><div id="comment-60294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60302"></span>

<div id="answer-container-60302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60302-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Without having done any investigation note that your tshark command line is just read filtering and then writing to the output whereas Wireshark is filtering and displaying. Not sure if that accounts for all the difference though, you would need to profile the runs to see what's going on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '17, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60302" class="comments-container"><span id="60304"></span><div id="comment-60304" class="comment"><div id="post-60304-score" class="comment-score"></div><div class="comment-text"><p>Loading and displaying the file without filter tooks 0.7 seconds. Loading the file in Wireshark with read filter tooks 7 seconds (same as tshark), but filter can't be undone - I must reload the file with different filter. I will try the same on Windows machine. I don't have time to profile the Wireshark now, but will try it in the future.</p></div><div id="comment-60304-info" class="comment-info"><span class="comment-age">(24 Mar '17, 03:00)</span> j123b567</div></div><span id="60309"></span><div id="comment-60309" class="comment"><div id="post-60309-score" class="comment-score"></div><div class="comment-text"><p>Same on windows, linux wireshark (qt5) and linux wireshark-gtk. Maybe, there are some GUI updates during display filtering that drastically decrease performance.</p></div><div id="comment-60309-info" class="comment-info"><span class="comment-age">(24 Mar '17, 04:02)</span> j123b567</div></div><span id="60311"></span><div id="comment-60311" class="comment"><div id="post-60311-score" class="comment-score"></div><div class="comment-text"><blockquote><p>mbrtu.crc16.incorrect do you get a lot of incorrect checksums? if so perhaps expert items are produced and cause poor performance? If you are able to share the file you could open a bug report so someone could take a look.</p></blockquote></div><div id="comment-60311-info" class="comment-info"><span class="comment-age">(24 Mar '17, 05:10)</span> Anders ♦</div></div><span id="60312"></span><div id="comment-60312" class="comment"><div id="post-60312-score" class="comment-score"></div><div class="comment-text"><p>After filtering, there is about 132 incorrect packets in ~450k captured. Ok, I can open bug report for this. Until then, here is the file to play with <a href="https://jaybee.cz/files/rs485.pcap.gz">https://jaybee.cz/files/rs485.pcap.gz</a></p></div><div id="comment-60312-info" class="comment-info"><span class="comment-age">(24 Mar '17, 05:41)</span> j123b567</div></div><span id="60347"></span><div id="comment-60347" class="comment"><div id="post-60347-score" class="comment-score"></div><div class="comment-text"><p>To what protocol should the DLT be connected?</p></div><div id="comment-60347-info" class="comment-info"><span class="comment-age">(27 Mar '17, 03:42)</span> Anders ♦</div></div><span id="60399"></span><div id="comment-60399" class="comment not_top_scorer"><div id="post-60399-score" class="comment-score"></div><div class="comment-text"><p>@Anders mbrtu</p></div><div id="comment-60399-info" class="comment-info"><span class="comment-age">(29 Mar '17, 03:33)</span> j123b567</div></div></div><div id="comment-tools-60302" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-60302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60563"></span>

<div id="answer-container-60563" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60563-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I think the problem is with the code in packet-mbtcp.c function dissect_modbus_response() on the second pass when it tries to find the corresponding request it goes through all packets from the end. The code should be changed to separate conversation and per packet data and store the per packet data only on the first pass for retrieval on the second pass.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '17, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-60563" class="comments-container"><span id="60564"></span><div id="comment-60564" class="comment"><div id="post-60564-score" class="comment-score"></div><div class="comment-text"><p>This sounds good. I just don't understand, why tshark works, because it should also perform two-pass dissection. (I have used parameter <code>-2</code>). It is also completely wrong to search corresponding response in mbrtu, because it will always be the next message or nothing.</p></div><div id="comment-60564-info" class="comment-info"><span class="comment-age">(04 Apr '17, 04:26)</span> j123b567</div></div><span id="60567"></span><div id="comment-60567" class="comment"><div id="post-60567-score" class="comment-score"></div><div class="comment-text"><p>Although possibly not related to the issue, Modbus TCP allows multiple requests to be "in flight" so it's not guaranteed that the response will be in the next "message".</p></div><div id="comment-60567-info" class="comment-info"><span class="comment-age">(04 Apr '17, 07:37)</span> grahamb ♦</div></div><span id="60585"></span><div id="comment-60585" class="comment"><div id="post-60585-score" class="comment-score"></div><div class="comment-text"><p>If you can please test or deskcheck <a href="https://code.wireshark.org/review/#/c/20927/1">https://code.wireshark.org/review/#/c/20927/1</a></p></div><div id="comment-60585-info" class="comment-info"><span class="comment-age">(05 Apr '17, 04:33)</span> Anders ♦</div></div></div><div id="comment-tools-60563" class="comment-tools"></div><div class="clear"></div><div id="comment-60563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

