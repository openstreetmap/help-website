+++
type = "question"
title = "Internet header + 64 bits o datagram"
description = '''Hello,  I have a little question about the field &quot;Internet Header + 64 bits of Data Datagram&quot; when I trying to calculate checksum icmp type 11. How can i check it on wireshark? Thanks '''
date = "2012-05-17T12:29:00Z"
lastmod = "2012-05-18T17:42:00Z"
weight = 11114
keywords = [ "checksum" ]
aliases = [ "/questions/11114" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Internet header + 64 bits o datagram](/questions/11114/internet-header-64-bits-o-datagram)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11114-score" class="post-score" title="current number of votes">0</div><span id="post-11114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a little question about the field "Internet Header + 64 bits of Data Datagram" when I trying to calculate checksum icmp type 11. How can i check it on wireshark?</p><p>Thanks <img src="https://osqa-ask.wireshark.org/upfiles/icmp_type11.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '12, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/917f6c4ca3412b5be65c51e4b90a2be5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blackfredy&#39;s gravatar image" /><p><span>blackfredy</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blackfredy has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '12, 12:31</strong> </span></p></div></div><div id="comments-container-11114" class="comments-container"></div><div id="comment-tools-11114" class="comment-tools"></div><div class="clear"></div><div id="comment-11114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11122"></span>

<div id="answer-container-11122" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11122-score" class="post-score" title="current number of votes">1</div><span id="post-11122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="blackfredy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The checksum calculation works exactly the same as for ICMP ECHO/ECHO-REPLY packets. Instead of some user data, the payload of the ICMP packet is now a portion of the packet that triggered the TTL-exceeded ICMP message. As the RFC says, it is the complete IP header plus 64 bits (8 octets) of said packet (these are used to be able to identify which packets caused the TTL-exceeded message).</p><p>In your example, the 64 bits are the ICMP header of the ping from 172.22.51.119 to 172.22.2.38.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11122" class="comments-container"><span id="11123"></span><div id="comment-11123" class="comment"><div id="post-11123-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>However thanks, well I'm doing this:</p><p>type+code = 0x0b00</p><p>Complete ip_header = 0x4500; 0x005c; 0xc0dd; 0x0000; 0x0001; 0xac16; 0x3377; 0xac16; 0x0226;</p><p>And plus</p><p>0xac16; 0x3377; 0xac16; 0x0226;</p><p>Adding the carry and doing the complement the result would be 0xf4ff? I think I am in a mistake. could help me?</p><p>Thanks!</p></div><div id="comment-11123-info" class="comment-info"><span class="comment-age">(17 May '12, 17:53)</span> <span class="comment-user userinfo">blackfredy</span></div></div><span id="11131"></span><div id="comment-11131" class="comment"><div id="post-11131-score" class="comment-score"></div><div class="comment-text"><p>You should use:</p><pre><code>ICMP header:
  type+code = 0x0b00
  checksum  = 0x0000 (ok, academically speaking ;-))

ICMP payload (IP header + 64 bits of payload, which is ICMP in this case:
  ip_header = 0x4500; 0x005c; 0xc0dd; 0x0000; 0x0001; 0xac16; 0x3377; 0xac16; 0x0226;
  icmp_header = 0x0800; 0x9bff; 0x0200; 0x5a00</code></pre></div><div id="comment-11131-info" class="comment-info"><span class="comment-age">(18 May '12, 02:56)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="11141"></span><div id="comment-11141" class="comment"><div id="post-11141-score" class="comment-score"></div><div class="comment-text"><p>I read rfc 792, and I couldn't understand, "64 bits of Original Data Datagram", but with your explanation now I got it. I follow your advice and additional I add ip_header checksum to reach 0xf4ff.</p><p>I really feel so grateful with your help,</p><p>Thanks!</p></div><div id="comment-11141-info" class="comment-info"><span class="comment-age">(18 May '12, 17:42)</span> <span class="comment-user userinfo">blackfredy</span></div></div></div><div id="comment-tools-11122" class="comment-tools"></div><div class="clear"></div><div id="comment-11122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

