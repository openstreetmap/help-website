+++
type = "question"
title = "home router repetitive ARP request"
description = '''hi, I am wondering why my router (also DHCP server) keeps ARP requesting non-stop to my home PC my rounter is D-Link N600:  http://www.dlink.com/ca/en/home-solutions/connect/routers/dir-826l-cloud-gigabit-router-n600 here&#x27;s a picture of the traffic:  http://i.imgur.com/4zTiu6V.jpg'''
date = "2013-12-17T00:08:00Z"
lastmod = "2013-12-17T13:49:00Z"
weight = 28192
keywords = [ "arp", "router", "request" ]
aliases = [ "/questions/28192" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [home router repetitive ARP request](/questions/28192/home-router-repetitive-arp-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28192-score" class="post-score" title="current number of votes">0</div><span id="post-28192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, I am wondering why my router (also DHCP server) keeps ARP requesting non-stop to my home PC</p><p>my rounter is D-Link N600: <a href="http://www.dlink.com/ca/en/home-solutions/connect/routers/dir-826l-cloud-gigabit-router-n600">http://www.dlink.com/ca/en/home-solutions/connect/routers/dir-826l-cloud-gigabit-router-n600</a></p><p>here's a picture of the traffic: <a href="http://i.imgur.com/4zTiu6V.jpg">http://i.imgur.com/4zTiu6V.jpg</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '13, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/f4d8306d9b943c98744de49602bf6678?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thisistherun&#39;s gravatar image" /><p><span>thisistherun</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thisistherun has no accepted answers">0%</span></p></div></div><div id="comments-container-28192" class="comments-container"></div><div id="comment-tools-28192" class="comment-tools"></div><div class="clear"></div><div id="comment-28192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28208"></span>

<div id="answer-container-28208" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28208-score" class="post-score" title="current number of votes">2</div><span id="post-28208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>why</strong> my router (also DHCP server) keeps ARP requesting non-stop to my home PC</p></blockquote><p>well, a network analysis tool (Wireshark) can never answer <strong>why</strong> a system is behaving as observed. That question can only be answered by the developer of that device, by looking at the code.</p><p>I can imagine some reasons like</p><ul><li>the DHCP server on the box tries to figure out if the MAC address is still in use (online), to decide if it can reuse the IP address.</li><li>the box tries to check if the MAC address is still in use (online) to show the device in the 'connected device/client list'</li><li>etc.</li></ul><p>but that would be only speculation and would not help you to understand the real reason for the ARP requests.</p><p>So, to <strong>answer your question</strong>: Nobody here will be able to tell you for sure <strong>why</strong> the box sends ARP requests to your client, as nobody has access to the firmware code. So, it's better to ask these kind of questions in a D-Link forum or google for similar reports of other users.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '13, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Dec '13, 08:14</strong> </span></p></div></div><div id="comments-container-28208" class="comments-container"><span id="28213"></span><div id="comment-28213" class="comment"><div id="post-28213-score" class="comment-score"></div><div class="comment-text"><p>I contacted hardware vendor, but no response yet</p><p>ok, thanks Kurt</p></div><div id="comment-28213-info" class="comment-info"><span class="comment-age">(17 Dec '13, 07:24)</span> <span class="comment-user userinfo">thisistherun</span></div></div><span id="28215"></span><div id="comment-28215" class="comment"><div id="post-28215-score" class="comment-score">1</div><div class="comment-text"><p>BTW: Are you sure your <strong>router</strong> is sending the ARP requests? In the 'Description' field of Netmon, it's said: <strong>192.168.0.77 asks</strong> for 192.168.0.1. What IP address is configured on your router? The default IP is 192.168.0.1.</p></div><div id="comment-28215-info" class="comment-info"><span class="comment-age">(17 Dec '13, 08:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28222"></span><div id="comment-28222" class="comment"><div id="post-28222-score" class="comment-score"></div><div class="comment-text"><p>oh 192.168.0.77 is the client 192.168.0.1 is the router</p><p>i am taking another picture <a href="http://i.imgur.com/d5lDNnc.jpg">http://i.imgur.com/d5lDNnc.jpg</a> 192.168.0.7 = client 192.168.0.1 = router</p><p>I am just setting up random static IP, even if it's a lease from DHCP server, it still does the ARP request consistently</p></div><div id="comment-28222-info" class="comment-info"><span class="comment-age">(17 Dec '13, 13:18)</span> <span class="comment-user userinfo">thisistherun</span></div></div><span id="28223"></span><div id="comment-28223" class="comment"><div id="post-28223-score" class="comment-score"></div><div class="comment-text"><p>Well, then see my explanation in the answer ;-)</p></div><div id="comment-28223-info" class="comment-info"><span class="comment-age">(17 Dec '13, 13:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28208" class="comment-tools"></div><div class="clear"></div><div id="comment-28208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

