+++
type = "question"
title = "How to filter packets while capturing them using tcpdump on linux based on a diameter AVP value"
description = '''Hello, we have a server that is acting as a diameter server. We would like to capture traffic between the diameter client and our daimeter server and have only those records that have a specific AVP values say...only those packets with a particular IMSI in the corresponding pcap. Is it possible to d...'''
date = "2013-08-16T10:26:00Z"
lastmod = "2013-08-21T22:38:00Z"
weight = 23824
keywords = [ "diameter", "tcpdump" ]
aliases = [ "/questions/23824" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter packets while capturing them using tcpdump on linux based on a diameter AVP value](/questions/23824/how-to-filter-packets-while-capturing-them-using-tcpdump-on-linux-based-on-a-diameter-avp-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23824-score" class="post-score" title="current number of votes">1</div><span id="post-23824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, we have a server that is acting as a diameter server. We would like to capture traffic between the diameter client and our daimeter server and have only those records that have a specific AVP values say...only those packets with a particular IMSI in the corresponding pcap. Is it possible to define such kind of filter when we initiate tcpdump on linux and if so could you provide the sysntax associated with such filters between a souce &amp; destination? Thanks Raj</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '13, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/9d890b455dafb1b9d40efc81dcc6328e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raj&#39;s gravatar image" /><p><span>raj</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raj has no accepted answers">0%</span></p></div></div><div id="comments-container-23824" class="comments-container"></div><div id="comment-tools-23824" class="comment-tools"></div><div class="clear"></div><div id="comment-23824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="23842"></span>

<div id="answer-container-23842" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23842-score" class="post-score" title="current number of votes">2</div><span id="post-23842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>only those packets with a particular IMSI in the corresponding pcap. Is it possible to define such kind of filter when we initiate tcpdump on linux and if so could you provide the sysntax associated with such filters between a souce &amp; destination?</p></blockquote><p>it is not possible to <strong>capture</strong> only those packets with a certain AVP (see the answer of <span><span>@Guy Harris</span></span>).</p><p>However, on Linux you can use <a href="http://ngrep.sourceforge.net/">ngrep</a>, if the Diameter communication is <strong>not encrypted</strong> and if you <strong>have a defined search string</strong> (in your case an IMSI).</p><blockquote><p>ngrep -d eth0 -O /var/tmp/imsi.pcap '262 01 9876543210' 'host 1.2.3.4 and host 2.3.4.5 and port 3868'</p></blockquote><p>This will look for the string '262 01 9876543210' (your IMSI) in the communication of host 1.2.3.4 and host 2.3.4.5 on port 3868. Packets that match the string will be written to /var/tmp/imsi.pcap. That file can then be further analyzed with wireshark/tshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '13, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Aug '13, 15:03</strong> </span></p></div></div><div id="comments-container-23842" class="comments-container"></div><div id="comment-tools-23842" class="comment-tools"></div><div class="clear"></div><div id="comment-23842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23939"></span>

<div id="answer-container-23939" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23939-score" class="post-score" title="current number of votes">1</div><span id="post-23939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the easiest method would be to do a tcpdump at a tcp/sctp port level, save it as a .pcap, then read it into tshark (on the server if it has wireshark installed, or on your laptop after transferring the file since as you're tracing a particular IMSI I'm assuming this is an ad-hoc troubleshooting effort and not a scripted process you're building).</p><p>Now, in the tshark CLI or wireshark with a <em>display</em> filter, what you're asking for is easy. Most Diameter applications would store the IMSI as the value of diameter.Session-Id-Data (in the case of credit control, policy control, etc.) or for some applications as diameter.User-Name. To give the exact filter (or to even attempt to give the exact filter for tcpdump) we'd need to know which Diameter application you're using though.</p><p>Since many Diameter servers (all that I have seen, and that includes one of the largest vendors in this space) will send multiple Diameter commands in a single IP packet, even if the AVP sequence and length is fixed a reliable tcpdump solution could be really tricky depending on the setup.</p><p>Are you deploying a Diameter router in this setup? If so it is usually the best place you can trace from since it can gice you both client and server legs and not all Diameter routers can be trusted not to tinker with the AVPs.</p><p>Edit: Kurt's solution with ngrep is probably the simplest, and definitely easier than tcpdump but if you have the ability to just save the trace and call on wireshark dissectors with tshark I still think that has the lowest margin for error here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 22:38</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Aug '13, 22:42</strong> </span></p></div></div><div id="comments-container-23939" class="comments-container"></div><div id="comment-tools-23939" class="comment-tools"></div><div class="clear"></div><div id="comment-23939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23835"></span>

<div id="answer-container-23835" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23835-score" class="post-score" title="current number of votes">0</div><span id="post-23835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to define such kind of filter when we initiate tcpdump on linux</p></blockquote><p>It would, at best, be extremely difficult, and would probably be impossible, given that parsing AVP values probably requires a loop and BPF filters (which is what Wireshark uses for capture filters and tcpdump uses for all its filters) are explicitly disallowed from looping (they're handed to the kernel to execute interpretively, and only forward branches are allowed, to prevent the kernel being made to loop infinitely).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '13, 18:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23835" class="comments-container"></div><div id="comment-tools-23835" class="comment-tools"></div><div class="clear"></div><div id="comment-23835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23919"></span>

<div id="answer-container-23919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23919-score" class="post-score" title="current number of votes">0</div><span id="post-23919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the AVP you are trying to filter on is always the n-th AVP in the diameter packet or if it is within the first n AVP's, you can build a filter for it.</p><p>Are you able to share a couple of packets that contain the AVP you want to filter on? You could upload it to www.cloudshark.org (if it contains no sensitive information of course). I could give it a shot to build a capture filter for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23919" class="comments-container"></div><div id="comment-tools-23919" class="comment-tools"></div><div class="clear"></div><div id="comment-23919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

