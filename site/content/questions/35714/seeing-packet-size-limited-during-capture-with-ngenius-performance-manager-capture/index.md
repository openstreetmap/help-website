+++
type = "question"
title = "Seeing &quot;Packet size limited during capture&quot; with nGenius Performance Manager capture"
description = '''I&#x27;m getting the message [Packet size limited during capture] and than on the tcp stream content i can see this[xxx bytes missing in capture file]. does anyone solved this issue or have an suggestion. thanks 2x2i'''
date = "2014-08-25T11:40:00Z"
lastmod = "2014-08-25T14:09:00Z"
weight = 35714
keywords = [ "snapshot", "ngenius" ]
aliases = [ "/questions/35714" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Seeing "Packet size limited during capture" with nGenius Performance Manager capture](/questions/35714/seeing-packet-size-limited-during-capture-with-ngenius-performance-manager-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35714-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting the message [Packet size limited during capture] and than on the tcp stream content i can see this[xxx bytes missing in capture file]. does anyone solved this issue or have an suggestion.</p><p>thanks 2x2i</p></div><div id="question-tags" class="tags-container tags">snapshot ngenius</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '14, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/c9eb9c012e62cd9862a31a1406202fe1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="2x2i&#39;s gravatar image" /><p>2x2i<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="2x2i has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Aug '14, 13:28</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-35714" class="comments-container"><span id="35717"></span><div id="comment-35717" class="comment"><div id="post-35717-score" class="comment-score"></div><div class="comment-text"><p>Did you capture this traffic with Wireshark or with some other program?</p><p>On what OS did you capture it, and on what network device did you capture it?</p><p>If you captured it with Wireshark, did you specify the "Limit each packet to ... bytes" option?</p><p>If you captured it with some other program, what program was that, and what options did you use with that program?</p></div><div id="comment-35717-info" class="comment-info"><span class="comment-age">(25 Aug '14, 11:52)</span> Guy Harris ♦♦</div></div><span id="35719"></span><div id="comment-35719" class="comment"><div id="post-35719-score" class="comment-score"></div><div class="comment-text"><p>I have used net scout to capture traffic.</p></div><div id="comment-35719-info" class="comment-info"><span class="comment-age">(25 Aug '14, 12:16)</span> 2x2i</div></div><span id="35720"></span><div id="comment-35720" class="comment"><div id="post-35720-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.netscout.com/products/Pages/default.aspx">NetScout</a> have a lot of products; which particular one did you use?</p></div><div id="comment-35720-info" class="comment-info"><span class="comment-age">(25 Aug '14, 12:37)</span> Guy Harris ♦♦</div></div><span id="35721"></span><div id="comment-35721" class="comment"><div id="post-35721-score" class="comment-score"></div><div class="comment-text"><p>nGenius Performance Manager, my bed i was in the hurry...</p></div><div id="comment-35721-info" class="comment-info"><span class="comment-age">(25 Aug '14, 12:45)</span> 2x2i</div></div><span id="35724"></span><div id="comment-35724" class="comment"><div id="post-35724-score" class="comment-score"></div><div class="comment-text"><p><a href="https://h21007.www2.hp.com/portal/download/product/17377/PM4-5_DS081908_1224512481222.pdf">This document from HP</a> says that nGenius Performance Manager can "Save, share, import and export capture files in standard formats (dat, cap, dmp, pcap)". What format did you save it in in order to read it into Wireshark?</p><p>When you read it into Wireshark, the packet detail display should show "''N'' bytes on wire" and "''M'' bytes captured", where ''M'' could be less than ''N''. Are there any packets in which ''M'' is less than ''N'', such as "1514 bytes on wire, 128 bytes captured" - or "1514 bytes on wire (12112 bits), 128 bytes captured (1024 bits)" ?</p></div><div id="comment-35724-info" class="comment-info"><span class="comment-age">(25 Aug '14, 13:27)</span> Guy Harris ♦♦</div></div><span id="35726"></span><div id="comment-35726" class="comment not_top_scorer"><div id="post-35726-score" class="comment-score"></div><div class="comment-text"><p>i have save it as Tcpdump.pcap buffer size is 64 MB Slice size is 64 Bytes ( i cant change this one) <img src="https://osqa-ask.wireshark.org/upfiles/ask_wireshark_Capture.PNG" alt="alt text" /></p></div><div id="comment-35726-info" class="comment-info"><span class="comment-age">(25 Aug '14, 13:43)</span> 2x2i</div></div></div><div id="comment-tools-35714" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-35714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35728"></span>

<div id="answer-container-35728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35728-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you can't change the slice size, this is an unfixable problem; "Slice Size: 64 Bytes" is nGenius Performance Manager's way of saying what, in the Wireshark GUI, is said as "Limit each packet to 64 bytes" - or it's way of saying "the slice size that was specified at capture time is 64 bytes and can't be changed when you save it, because it's too late".</p><p>I.e., it's saying "Packet size limited during capture" because the packet size <em>was</em> limited, to at most 64 bytes per packet, during the capture.</p><p>If there's some way for you, or somebody else, to change the slice size - or completely disable packet slicing - that would be the only way <em>not</em> to get "Packet size limited during capture" and "[xxx bytes missing in capture file]".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '14, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-35728" class="comments-container"><span id="35750"></span><div id="comment-35750" class="comment"><div id="post-35750-score" class="comment-score"></div><div class="comment-text"><p>Thank you Guy for all your help, I'm going to see with netscout admin if we can change packet slicing or if its safe we may disable completely. thanks 2x2i</p></div><div id="comment-35750-info" class="comment-info"><span class="comment-age">(26 Aug '14, 05:31)</span> 2x2i</div></div></div><div id="comment-tools-35728" class="comment-tools"></div><div class="clear"></div><div id="comment-35728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

