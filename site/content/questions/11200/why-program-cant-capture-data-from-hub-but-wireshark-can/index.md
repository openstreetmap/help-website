+++
type = "question"
title = "why program can&#x27;t capture  data from HUB but wireshark can?"
description = '''Recently, my job involved capturing data, which STB communicates with BOSS. I connected my computer with STB using a 10M HUB in sharing mode (not switching mode), then, using wireshark, I do capture the desired data, but using my program, I can not capture any more. My program is linked with libpcap...'''
date = "2012-05-22T01:03:00Z"
lastmod = "2012-05-25T09:41:00Z"
weight = 11200
keywords = [ "programming", "libpcap", "wireshark" ]
aliases = [ "/questions/11200" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [why program can't capture data from HUB but wireshark can?](/questions/11200/why-program-cant-capture-data-from-hub-but-wireshark-can)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11200-score" class="post-score" title="current number of votes">0</div><span id="post-11200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently, my job involved capturing data, which STB communicates with BOSS. I connected my computer with STB using a 10M HUB in sharing mode (not switching mode), then, using wireshark, I do capture the desired data, but using my program, I can not capture any more. My program is linked with libpcap library. What's more, I download several network analyzing tools, and none of them can work as I desired and capture the desired data. So, I need to understand how wireshark avoids the bug my program runs up against, and what's the flow in which wireshark captures data from network.</p><p>PS.I am from ShenZhen City,China,and glad to receive reply from foreign friends.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-programming" rel="tag" title="see questions tagged &#39;programming&#39;">programming</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '12, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/4b0fa4b574a337d0b956e1f6e72ab129?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coolio&#39;s gravatar image" /><p><span>coolio</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coolio has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 May '12, 17:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-11200" class="comments-container"></div><div id="comment-tools-11200" class="comment-tools"></div><div class="clear"></div><div id="comment-11200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="11202"></span>

<div id="answer-container-11202" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11202-score" class="post-score" title="current number of votes">0</div><span id="post-11202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="coolio has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you can download the source code of wireshark and learn how it works</p><blockquote><p><code>http://wiresharkdownloads.riverbed.com/wireshark/src/wireshark-1.6.7.tar.bz2</code></p></blockquote><p>It might help troubleshooting your own tool.</p><p>Furthermore I recommend these links:</p><blockquote><p><code>http://www.tcpdump.org/pcap.html</code><br />
<code>http://undergraduate.csse.uwa.edu.au/units/CITS3231/reading/libpcap-programming.pdf</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-11202" class="comments-container"><span id="11325"></span><div id="comment-11325" class="comment"><div id="post-11325-score" class="comment-score"></div><div class="comment-text"><p>Dear Kurt: First of all,thank very for you kindly and timely help,the suggestions and articles you advised are of high quality,from which I have learned much knowlege about libpcap.Keeping track of clues provided in <a href="http://libpcap-programming.pdf">libpcap-programming.pdf</a>,I have solved my programe's bug smoothly,which is about the data encapsulation method in network protocol.I checked the data byte-by-byte ,and found that between Ethernet head part and IP head part,there are 8 bytes organized in PPPoE <a href="http://protocol.So">protocol.So</a> in order to debug my programe,I should let filter expression is NULL,and pay attention to PPPoE bytes. Best wishes to your work and life. Regards Coolio<br />
Jetsen Co.Ltd,ShenZhen,China</p></div><div id="comment-11325-info" class="comment-info"><span class="comment-age">(25 May '12, 03:51)</span> <span class="comment-user userinfo">coolio</span></div></div><span id="11327"></span><div id="comment-11327" class="comment"><div id="post-11327-score" class="comment-score"></div><div class="comment-text"><p>Coolio,</p><p>I'm glad I was able to help.<br />
BTW: If you like my answer, you can mark it as the correct answer.</p><p>Thanks<br />
Kurt</p></div><div id="comment-11327-info" class="comment-info"><span class="comment-age">(25 May '12, 04:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11202" class="comment-tools"></div><div class="clear"></div><div id="comment-11202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11220"></span>

<div id="answer-container-11220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11220-score" class="post-score" title="current number of votes">0</div><span id="post-11220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you capturing in promiscuous mode?</p><p>What's the code in your program that opens the capture device (<code>pcap_open_live()</code>, or <code>pcap_create()</code>and other calls), sets the filter (if any) on the capture device, and reads the packets?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-11220" class="comments-container"></div><div id="comment-tools-11220" class="comment-tools"></div><div class="clear"></div><div id="comment-11220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11335"></span>

<div id="answer-container-11335" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11335-score" class="post-score" title="current number of votes">0</div><span id="post-11335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the traffic you're trying to capture is PPPoE traffic, and you're using a capture filter, and <code>pppoe and</code> in front of the filter, for example <code>pppoe and host 192.9.200.2</code> if you're trying to capture PPPoE traffic to or from 192.9.200.2. Some older versions of libpcap don't support that, but newer versions do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '12, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-11335" class="comments-container"></div><div id="comment-tools-11335" class="comment-tools"></div><div class="clear"></div><div id="comment-11335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

