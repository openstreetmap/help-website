+++
type = "question"
title = "Duplicate IP address detected but mac doesn&#x27;t exist"
description = '''I am getting IP address conflicts all over network for months. Trying to locate but not making progress. Wireshark packets indicate duplicate Ip address in use. For example: duplicate ip address detectect for 192.168.1.1 (cc:52:af:0d:5f:d6) also in use by 02:cb:13:0d:5f:d6) frame (1102). I look at f...'''
date = "2013-10-02T13:35:00Z"
lastmod = "2015-10-31T12:51:00Z"
weight = 25554
keywords = [ "ip", "duplicate", "aruba" ]
aliases = [ "/questions/25554" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate IP address detected but mac doesn't exist](/questions/25554/duplicate-ip-address-detected-but-mac-doesnt-exist)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25554-score" class="post-score" title="current number of votes">0</div><span id="post-25554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting IP address conflicts all over network for months. Trying to locate but not making progress. Wireshark packets indicate duplicate Ip address in use. For example:</p><p>duplicate ip address detectect for 192.168.1.1 (cc:52:af:0d:5f:d6) also in use by 02:cb:13:0d:5f:d6) frame (1102).</p><p>I look at frame 1102 and sure enough it has an ARP asking who has IP address 192.168.1.254 (happens to be gateway) to please tell 192.168.1.1 but of course the Mac address is not correct.</p><p>I check the DHCP server, 192.168.1.1 has not been assigned. The station that should get it doesn't get anything except a windows error telling it there is a conflict.</p><p>When I telnet to each switch in the path and check mac address for 02:cb:13:0d:5f:d6 sometimes it actually exists and always it traces back to one of many ARUBA wireless 135 devices we have deployed (not always same aruba, many times not). Sometimes though the mac address doesn't even exist. When it does tie back to aruba, in every single case that mac address is not connected to any aruba devices, I can see from our console that it is not there.</p><p>I know addresses that start with 02 are locallly administered addresses. I'm assuming we have an infested machine somewhere but how to locate when the mac address no where to be found?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-aruba" rel="tag" title="see questions tagged &#39;aruba&#39;">aruba</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '13, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/f39f51e3705e49c3a49595a2b9cc9084?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jim%20fixit&#39;s gravatar image" /><p><span>jim fixit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jim fixit has no accepted answers">0%</span></p></div></div><div id="comments-container-25554" class="comments-container"></div><div id="comment-tools-25554" class="comment-tools"></div><div class="clear"></div><div id="comment-25554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25734"></span>

<div id="answer-container-25734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25734-score" class="post-score" title="current number of votes">1</div><span id="post-25734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is another guy with the same problem. Aruba APs, duplicate IPs with MAC addresses starting with 02:</p><blockquote><p><a href="http://community.arubanetworks.com/t5/Aruba-Instant-Cloud-Wi-Fi/Duplicate-DHCP-addresses-when-connecting-two-AP105-s/m-p/55984">http://community.arubanetworks.com/t5/Aruba-Instant-Cloud-Wi-Fi/Duplicate-DHCP-addresses-when-connecting-two-AP105-s/m-p/55984</a></p></blockquote><p>Cite: <code>One MAC address is the original MAC address of the laptop and the other MAC address is a phantom address starting with 02:....</code><br />
</p><p>So, this seems to be an internal (maybe documented or not) feature of the Aruba APs.</p><blockquote><p><strong>I'm assuming we have an infested machine somewhere</strong> but how to locate when the mac address no where to be found?</p></blockquote><p>I don't think so.</p><p>You should contact the Aruba support and ask them about that behavior.</p><p>Please update here as well. Might be interesting for others sometime ;-)</p><p><strong>++ UPDATE ++</strong></p><p>Wait a moment. MAC address starting with 02:... That reminds me on something. Microsoft NLB.</p><blockquote><p><a href="http://technet.microsoft.com/de-de/library/ff849728.aspx">http://technet.microsoft.com/de-de/library/ff849728.aspx</a></p></blockquote><p>Cite:</p><pre><code>To identify NLB-enabled hosts when using switch or network tracing software look for MAC addresses that start with 02. The masked MAC address is similar to the original MAC address, but with the first two fields replaced as follows: 02-[Host ID including zero]-[Original MAC address values]. </code></pre><p>Hm... do you have any NLB enabled systems on that network?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Oct '13, 16:25</strong> </span></p></div></div><div id="comments-container-25734" class="comments-container"><span id="47117"></span><div id="comment-47117" class="comment"><div id="post-47117-score" class="comment-score"></div><div class="comment-text"><p>Not NLB, but I have been dealing with similar issues related to this:</p><p><a href="http://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/8021x/116529-problemsolution-product-00.html">http://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/8021x/116529-problemsolution-product-00.html</a></p></div><div id="comment-47117-info" class="comment-info"><span class="comment-age">(31 Oct '15, 12:51)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-25734" class="comment-tools"></div><div class="clear"></div><div id="comment-25734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25626"></span>

<div id="answer-container-25626" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25626-score" class="post-score" title="current number of votes">0</div><span id="post-25626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you have many "Duplicate IP address detected" messages, I would start by collecting these over a period of time and try to find a pattern. Which IP addresses are involved and which are not. Which mac-addresses are involved and how do they relate to the each other. If there is a pattern in the mac-addresses, you might be able to create a capture filter for it. Or better, you might be able to create an ACL on your network devices to log packets that match. Did you obfuscate the mac-addresses or are they literally the ones you did see on the network. Assuming they were not obfuscated, I find the fact that the last 3 octets of the mac-address are the same noteworthy.</p><p>Since ARP requests are broadcast, you will see them everywhere. You might want to isolate by making traces on a span port only spanning the incoming packets. That way you can at least isolate where the packets are actually coming from. But you might already have done that as you say it always comes from one of the Aruba AP's.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25626" class="comments-container"></div><div id="comment-tools-25626" class="comment-tools"></div><div class="clear"></div><div id="comment-25626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

