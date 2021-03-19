+++
type = "question"
title = "Trying to find which workstation has trojan zbot on it"
description = '''My home ip address is blacklisted on http://cbl.abuseat.org/lookup.cgi?ip=63.142.130.18&amp;amp;.pubmit=Lookup and they state that a workstation in my home is infected with the ZeuS trojan, also known as &quot;Zbot&quot; and &quot;WSNPoem&quot; I delisted my ip address but am back on the list, which affects my email delive...'''
date = "2013-09-26T09:46:00Z"
lastmod = "2013-09-26T11:18:00Z"
weight = 25283
keywords = [ "zbot", "trojan", "zeus", "wsnpoem", "wireshark" ]
aliases = [ "/questions/25283" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to find which workstation has trojan zbot on it](/questions/25283/trying-to-find-which-workstation-has-trojan-zbot-on-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25283-score" class="post-score" title="current number of votes">0</div><span id="post-25283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My home ip address is blacklisted on <a href="http://cbl.abuseat.org/lookup.cgi?ip=63.142.130.18&amp;.pubmit=Lookup">http://cbl.abuseat.org/lookup.cgi?ip=63.142.130.18&amp;.pubmit=Lookup</a> and they state that a workstation in my home is infected with the ZeuS trojan, also known as "Zbot" and "WSNPoem"</p><p>I delisted my ip address but am back on the list, which affects my email deliverability.</p><p>I have spent all morning trying to use Wireshark to sniff the traffic on my entire network looking for the workstation that is communicating with the external ip address that they have identified the information is being sent to, although in this case it is a sinkhole.</p><p>I have tried multiple filters and command strings but nothing seems to be working the way I envisioned it would.</p><p>Does anyone know where there might be a step-by-step guide for what I am attempting to do?</p><p>I am in school for IT and have years of experience on computers. The common homeowner would be bald by now.</p><p>Thanks</p><p>PS - I am using a Mac and wonder if this program would work better on a PC?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zbot" rel="tag" title="see questions tagged &#39;zbot&#39;">zbot</span> <span class="post-tag tag-link-trojan" rel="tag" title="see questions tagged &#39;trojan&#39;">trojan</span> <span class="post-tag tag-link-zeus" rel="tag" title="see questions tagged &#39;zeus&#39;">zeus</span> <span class="post-tag tag-link-wsnpoem" rel="tag" title="see questions tagged &#39;wsnpoem&#39;">wsnpoem</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '13, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/ea0104282ec06baedd71fc9187f2a81b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="billwynne&#39;s gravatar image" /><p><span>billwynne</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="billwynne has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '13, 09:48</strong> </span></p></div></div><div id="comments-container-25283" class="comments-container"></div><div id="comment-tools-25283" class="comment-tools"></div><div class="clear"></div><div id="comment-25283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25285"></span>

<div id="answer-container-25285" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25285-score" class="post-score" title="current number of votes">1</div><span id="post-25285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My home ip address is blacklisted on <a href="http://cbl.abuseat.org/lookup.cgi?ip=63.142.130.18&amp;.pubmit=Lookup">http://cbl.abuseat.org/lookup.cgi?ip=63.142.130.18&amp;.pubmit=Lookup</a></p></blockquote><p>hm.. they tell you pretty clearly what to look for.</p><p>Cite:</p><pre><code>Behind a NAT, you should be able to find the infected machine by looking for attempted connections to IP address 87.255.51.229 or host name benznflvsgttdydqdguwcem.info on any port with a network sniffer such as wireshark. Equivalently, you can examine your DNS server or proxy server logs to references to 87.255.51.229 or benznflvsgttdydqdguwcem.info. See Advanced Techniques for more detail on how to use wireshark - ignore the references to port 25/SMTP traffic - the identifying activity is NOT on port 25. </code></pre><p>That's not a guarantee to find the machine, as it may have switched to a different C&amp;C server, but did you try all that?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '13, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '13, 10:37</strong> </span></p></div></div><div id="comments-container-25285" class="comments-container"><span id="25286"></span><div id="comment-25286" class="comment"><div id="post-25286-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Thanks for taking the time to share. I have run Wireshark to view all the network traffic and then looked for that ip address and port but it did not show up at all. I have all the workstations running so I could bust the culprit. I am not sure that I am using WireShark the right way to do this.</p><p>It is a technical piece of software and I was hoping for a step-by-step guide on how to perform a task like what I am trying to do.</p><p>Thanks</p></div><div id="comment-25286-info" class="comment-info"><span class="comment-age">(26 Sep '13, 10:49)</span> <span class="comment-user userinfo">billwynne</span></div></div><span id="25291"></span><div id="comment-25291" class="comment"><div id="post-25291-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am not sure that I am using WireShark the right way to do this.</p></blockquote><p>O.K. where did you run Wireshark? On your local PC? If so, you will <strong>not</strong> see the whole network traffic unless you've taken the appropriate steps.</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></blockquote><p>Please check that.</p><blockquote><p>I have run Wireshark to view all the network traffic and then looked for that ip address and port but it did not show up at all.</p></blockquote><p>O.K. if your capture setup is done right (see above) and you still don't find that IP address, you could look for 'strange' DNS names. Trojans often use random domain names for their C&amp;C servers (like the one mentioned: benznflvsgttdydqdguwcem.info). So, please capture the whole DNS traffic and then filter for DNS requests.</p><p>Display filter:</p><blockquote><p>dns.qry.name</p></blockquote><p>Try to find strange looking names like the one above.</p></div><div id="comment-25291-info" class="comment-info"><span class="comment-age">(26 Sep '13, 11:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-25285" class="comment-tools"></div><div class="clear"></div><div id="comment-25285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25287"></span>

<div id="answer-container-25287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25287-score" class="post-score" title="current number of votes">0</div><span id="post-25287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To filter on traffic to and from the sink hole, enter the following display filter: <em>ip.addr==87.255.51.229</em></p><p>Assuming, as is likely, that you're on a switched network, the problem may be that you're not seeing the traffic from the infected machine. See <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">this page</a> of the Wireshark Wiki for a discussion of how to capture traffic on a switched Ethernet network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '13, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-25287" class="comments-container"></div><div id="comment-tools-25287" class="comment-tools"></div><div class="clear"></div><div id="comment-25287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

