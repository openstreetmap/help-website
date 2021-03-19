+++
type = "question"
title = "Why are the bytes &#x27;00 00&#x27; but Wireshark shows an ip total length of 2016?"
description = '''The ip total length field gives the value in bytes of the ip header along with the data it contains. However, in the below image the byes are 00 00 but Wireshark has a total length 0f 2016. Can someone clue me in on how that is calculated? '''
date = "2012-11-25T12:13:00Z"
lastmod = "2012-11-25T16:37:00Z"
weight = 16279
keywords = [ "ip" ]
aliases = [ "/questions/16279" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why are the bytes '00 00' but Wireshark shows an ip total length of 2016?](/questions/16279/why-are-the-bytes-00-00-but-wireshark-shows-an-ip-total-length-of-2016)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16279-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The ip total length field gives the value in bytes of the ip header along with the data it contains. However, in the below image the byes are 00 00 but Wireshark has a total length 0f 2016. Can someone clue me in on how that is calculated?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2012-11-25_at_2.09.18_PM.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '12, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/fa3819a16ed8b0da298be03bfeed1897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Binyan&#39;s gravatar image" /><p>Binyan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Binyan has no accepted answers">0%</span></p></img></div></div><div id="comments-container-16279" class="comments-container"><span id="16280"></span><div id="comment-16280" class="comment"><div id="post-16280-score" class="comment-score"></div><div class="comment-text"><p>looks strange. Your screenshot shows 0x0000 where it should be 0x07E0.</p><p>Can you post that single packet as pcap file on <a href="http://cloudshark.org">cloudshark.org</a>?</p></div><div id="comment-16280-info" class="comment-info"><span class="comment-age">(25 Nov '12, 12:49)</span> Kurt Knochner ♦</div></div><span id="16281"></span><div id="comment-16281" class="comment"><div id="post-16281-score" class="comment-score"></div><div class="comment-text"><p>I've save the single packet as a pcap file but <a href="http://loudshark.org">loudshark.org</a>, doesn't resolve for me. Is that the correct address?</p></div><div id="comment-16281-info" class="comment-info"><span class="comment-age">(25 Nov '12, 13:32)</span> Binyan</div></div><span id="16282"></span><div id="comment-16282" class="comment"><div id="post-16282-score" class="comment-score"></div><div class="comment-text"><p>sorry, should have been <a href="http://cloudshark.org">cloudshark.org</a>.</p></div><div id="comment-16282-info" class="comment-info"><span class="comment-age">(25 Nov '12, 13:40)</span> Kurt Knochner ♦</div></div><span id="16283"></span><div id="comment-16283" class="comment"><div id="post-16283-score" class="comment-score"></div><div class="comment-text"><p>OK, here it is <a href="http://cloudshark.org/captures/25e40f73bc1c">http://cloudshark.org/captures/25e40f73bc1c</a></p></div><div id="comment-16283-info" class="comment-info"><span class="comment-age">(25 Nov '12, 13:43)</span> Binyan</div></div></div><div id="comment-tools-16279" class="comment-tools"></div><div class="clear"></div><div id="comment-16279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16287"></span>

<div id="answer-container-16287" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16287-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sometimes <a href="http://blogs.technet.com/b/nettracer/archive/2010/10/05/bogus-ip-packets-and-wireshark.aspx">valid IP packets from interfaces doing TCP segmentation offloading will have an IP length of 0</a>, and Wireshark has a preference to handle that. The preference is probably set for you; note that if you turn it off, things will not work very well.</p><p>For some reason, at least with Safari, Cloudshark isn't letting me download the packet; Chrome on OS X, and Internet Explorer 9 on a Windows 7 virtual machine, isn't doing so either. Perhaps Cloudshark is just completely broken.</p><p>The Git-trunk version of tcpdump has code, compiled in if <code>GUESS_TSO</code> is #defined, to do the same thing Wireshark does; that's not enabled by default. The blog post I cited above says</p><blockquote><p>Note: Network Monitor already takes that into account and hence you don’t need to take any corrective action if you’re checking the trace with it.</p></blockquote><p>and I think it's a Microsoft blog, so, while NetMon may show the field as having the value 0 (because its dissection is done based on protocol format descriptions, which might make it harder to show the inferred value of the field), it might still handle the packet correctly.</p><p>Wireshark should probably note that this is a <em>calculated</em> value and that this is the result of TCP segmentation offloading; I've modified the code on the SVN trunk to do so.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '12, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '12, 19:16</p></div></div><div id="comments-container-16287" class="comments-container"><span id="16305"></span><div id="comment-16305" class="comment"><div id="post-16305-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Cloudshark isn't letting me download the packet;</p></blockquote><p>just remove <code>/export</code> from the URL and then use the regular download function of cloudshark. The /export links don't seem to work very well.</p></div><div id="comment-16305-info" class="comment-info"><span class="comment-age">(26 Nov '12, 03:14)</span> Kurt Knochner ♦</div></div><span id="16335"></span><div id="comment-16335" class="comment"><div id="post-16335-score" class="comment-score"></div><div class="comment-text"><p>That worked - I guess the <code>/export</code> URL is a URL for the export pop-up window, and, if accessed out of context, doesn't work. I edited the comment containing the URL to remove the <code>/export</code>.</p></div><div id="comment-16335-info" class="comment-info"><span class="comment-age">(26 Nov '12, 12:05)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-16287" class="comment-tools"></div><div class="clear"></div><div id="comment-16287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16284"></span>

<div id="answer-container-16284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16284-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. it's really 0x0000 and Wireshark (1.9.0 SVN-46157) shows the length as 2016. As this is clearly wrong, I double checked with tcpdump and MS Netmon.</p><p>tcpdump:</p><blockquote><p><code>20:50:14.587897 IP bad-len 0</code><br />
</p></blockquote><p>MS Netmon:</p><blockquote><p><code>shows IP TotalLength as 0</code></p></blockquote><p>I would say, this is probably a bug in Wireshark. If Wireshark deduces the length from the rest of the frame, it should at least output some warning about the zero IP length (Expert Info and/or coloring of IP Length field).</p><p>Please file a bug report at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a> with a link to this question. Please provide the capture file in the bug report.</p><p>Please also post the link to the bug here.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '12, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '12, 14:02</p></div></div><div id="comments-container-16284" class="comments-container"><span id="16285"></span><div id="comment-16285" class="comment"><div id="post-16285-score" class="comment-score"></div><div class="comment-text"><p>Well I would think it is an error if it wasn't for the fact that the # is correct. There really is 2016 bytes of data in the packet (20 bytes for ip header + 20 bytes for tcp header + 1976 bytes for HTTP post). I have a total of 6 post in ths file and 4 have this issue where there is a total length of 00 00 but the byte count is really right.</p></div><div id="comment-16285-info" class="comment-info"><span class="comment-age">(25 Nov '12, 14:07)</span> Binyan</div></div><span id="16286"></span><div id="comment-16286" class="comment"><div id="post-16286-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Well I would think it is an error if it wasn't for the fact that the # is correct.</p></blockquote><p>if it's a bug or not is up to the core developers to decide. However, there is no (full) plausibility check of the IP length in the code, so either this is by design or a bug ;-)</p></div><div id="comment-16286-info" class="comment-info"><span class="comment-age">(25 Nov '12, 14:42)</span> Kurt Knochner ♦</div></div><span id="16300"></span><div id="comment-16300" class="comment"><div id="post-16300-score" class="comment-score"></div><div class="comment-text"><p>there you have it. It's by design :-))</p></div><div id="comment-16300-info" class="comment-info"><span class="comment-age">(26 Nov '12, 02:19)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16284" class="comment-tools"></div><div class="clear"></div><div id="comment-16284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

