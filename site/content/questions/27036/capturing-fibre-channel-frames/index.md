+++
type = "question"
title = "capturing Fibre Channel frames"
description = '''Any rumors around supporting capture on Fibre Channel HBAs? --sk'''
date = "2013-11-15T08:33:00Z"
lastmod = "2013-11-15T13:12:00Z"
weight = 27036
keywords = [ "fibre", "channel", "capture" ]
aliases = [ "/questions/27036" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capturing Fibre Channel frames](/questions/27036/capturing-fibre-channel-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27036-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Any rumors around supporting capture on Fibre Channel HBAs?</p><p>--sk</p></div><div id="question-tags" class="tags-container tags">fibre channel capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '13, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/18ae5b8bfddad49931ec557b9342075a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skendric&#39;s gravatar image" /><p>skendric<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skendric has no accepted answers">0%</span></p></div></div><div id="comments-container-27036" class="comments-container"></div><div id="comment-tools-27036" class="comment-tools"></div><div class="clear"></div><div id="comment-27036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27042"></span>

<div id="answer-container-27042" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27042-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No rumors I've heard of lately.</p><p>So, the answer of @Guy Harris in the following question is still valid.</p><blockquote><p><a href="http://ask.wireshark.org/questions/9687/about-capturing-of-fibre-channel-packets">http://ask.wireshark.org/questions/9687/about-capturing-of-fibre-channel-packets</a><br />
</p></blockquote><p>A possible way was discussed here</p><blockquote><p><a href="http://www.wireshark.org/lists/wireshark-users/201109/msg00099.html">http://www.wireshark.org/lists/wireshark-users/201109/msg00099.html</a><br />
</p></blockquote><p>By using a Cisco MDS Port Analyzer Adapter (not sure if that thing is still available - maybe eBay), you can encapsulate Fibre Channel traffic into an ethernet frame which can then be analyzed with Wireshark.</p><p>I have no idea if that really works, but the screenshot in the following paper shows the GUI of Ethereal (former name of Wireshark) with such a frame.</p><blockquote><p><a href="https://learningnetwork.cisco.com/servlet/JiveServlet/download/3740-2-3383/FCAnalyzer%2022Dec09%209%20d-3740.pdf">https://learningnetwork.cisco.com/servlet/JiveServlet/download/3740-2-3383/FCAnalyzer%2022Dec09%209%20d-3740.pdf</a><br />
</p><p><a href="http://www.cisco.com/en/US/docs/storage/san_switches/mds9000/hw/paa/installation/note/FPAA2.html">http://www.cisco.com/en/US/docs/storage/san_switches/mds9000/hw/paa/installation/note/FPAA2.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '13, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Nov '13, 13:18</p></div></div><div id="comments-container-27042" class="comments-container"><span id="27157"></span><div id="comment-27157" class="comment"><div id="post-27157-score" class="comment-score"></div><div class="comment-text"><p>Assuming I had money (which I don't at the moment, but let's ignore this for the moment) -- where might I advertise to find someone with the skills it would take to extend libpcap/Winpcap support to a Fibre Channel HBA?</p><p>--sk</p></div><div id="comment-27157-info" class="comment-info"><span class="comment-age">(20 Nov '13, 05:54)</span> skendric</div></div><span id="27159"></span><div id="comment-27159" class="comment"><div id="post-27159-score" class="comment-score"></div><div class="comment-text"><p>In think it's cheaper to buy a fibre channel analyzer than to 'sponsor' that kind of libpcap extension ;-))</p><p>However, I might be wrong: Please post your message to the libpcap developer list.</p><blockquote><p><a href="http://www.tcpdump.org/#mailing-lists">http://www.tcpdump.org/#mailing-lists</a></p></blockquote></div><div id="comment-27159-info" class="comment-info"><span class="comment-age">(20 Nov '13, 06:49)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27042" class="comment-tools"></div><div class="clear"></div><div id="comment-27042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

