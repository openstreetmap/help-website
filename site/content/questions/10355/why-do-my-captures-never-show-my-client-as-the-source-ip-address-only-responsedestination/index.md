+++
type = "question"
title = "Why do my captures NEVER show my client as the Source IP address?  (only response/destination)"
description = '''Whether it be wired or wireless, any captures I perform only show my client&#x27;s IP in the destination, and the return traffic. This is true for the exception of ICMP. If I capture a web browsing session to &quot;google.com&quot;, the very first package I see in my trace is the SYN ACK from the web server. I see...'''
date = "2012-04-20T11:46:00Z"
lastmod = "2015-07-22T03:04:00Z"
weight = 10355
keywords = [ "source", "address", "ip" ]
aliases = [ "/questions/10355" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why do my captures NEVER show my client as the Source IP address? (only response/destination)](/questions/10355/why-do-my-captures-never-show-my-client-as-the-source-ip-address-only-responsedestination)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10355-score" class="post-score" title="current number of votes">0</div><span id="post-10355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Whether it be wired or wireless, any captures I perform only show my client's IP in the destination, and the return traffic. This is true for the exception of ICMP. If I capture a web browsing session to "google.com", the very first package I see in my trace is the SYN ACK from the web server. I see no SYN or ACKs originating from my machine.</p><p>I've not run into this issue before. Client/NIC drivers?</p><p>Workstation: HP Laptop, Windows 7 32-bit. NICs: Intel(R) 82579LM Gigabit Network Connection Intel(R) Centrino(R) Ultimate-N 6300 AGN</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '12, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/4995095aa039a7a67fd837d6ddba5ae5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheWraith&#39;s gravatar image" /><p><span>TheWraith</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheWraith has no accepted answers">0%</span></p></div></div><div id="comments-container-10355" class="comments-container"><span id="10394"></span><div id="comment-10394" class="comment"><div id="post-10394-score" class="comment-score"></div><div class="comment-text"><p>do you have TCP chimney offloading enabled in your cards settings? stick to the wired card to eliminate basic antenna errors while capturing</p></div><div id="comment-10394-info" class="comment-info"><span class="comment-age">(23 Apr '12, 01:45)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="13199"></span><div id="comment-13199" class="comment"><div id="post-13199-score" class="comment-score"></div><div class="comment-text"><p>HI;</p><p>I feel your pain! I have an HP 6450b laptop with the Intel 82579V wired NIC. I ripped my hair out today. We were troubleshooting a DHCP problem, and I wanted to verify the entire DHCP handshake.</p><p>To my dismay, NOT ONE of the DHCP DISCOVER packets sent by my laptop showed up in the Wireshark 1.81 capture. This is the exact problem you are describing - the first packet of a conversation does not show up. We plugged a Dell Lattitude (has Intel Pro 100 nic) into the cable and all was normal.</p><p>I then setup a Cisco monitor session on the switch and sent all traffic to another port, where we captured all the traffic from my HP 6450b. The DHCP discovers were there.</p><p>This is a HORRIBLE problem. I tried every combination of Advanced Parameters in the NIC properties and nothing could fix it.</p><p>If I can't figure this out, I have to junk this otherwise nice little HP 6450b and get a laptop that uses the Intel Pro 1000 line of nics.</p><p>Steve</p></div><div id="comment-13199-info" class="comment-info"><span class="comment-age">(31 Jul '12, 14:15)</span> <span class="comment-user userinfo">stevecrye</span></div></div><span id="44320"></span><div id="comment-44320" class="comment"><div id="post-44320-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I have exactly the same problem. I made a capture between pc client and a https server on the net and the capture does not show the client as source, the client is only in the destination. So I have the SYN,ACK and the ACK from the server...I don't understand why ? Have you any ideas ?</p><p>Thank you. David</p></div><div id="comment-44320-info" class="comment-info"><span class="comment-age">(21 Jul '15, 02:18)</span> <span class="comment-user userinfo">wire500</span></div></div></div><div id="comment-tools-10355" class="comment-tools"></div><div class="clear"></div><div id="comment-10355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44366"></span>

<div id="answer-container-44366" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44366-score" class="post-score" title="current number of votes">0</div><span id="post-44366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's probably the nic card ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '15, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/785844f83decaa3833a40eb83d56fd94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wire500&#39;s gravatar image" /><p><span>wire500</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wire500 has no accepted answers">0%</span></p></div></div><div id="comments-container-44366" class="comments-container"></div><div id="comment-tools-44366" class="comment-tools"></div><div class="clear"></div><div id="comment-44366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

