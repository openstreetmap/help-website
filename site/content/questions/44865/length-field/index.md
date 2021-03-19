+++
type = "question"
title = "length field"
description = '''hi guys, I captured a ping to my default gateway with Wireshark. I&#x27;m now wondering about the &quot;Length&quot; field. From what I already know, the Preamble and FCS fields are not shown by Wireshark.  So is this the REAL Frame length? I mean it includes all fields from Preamble to FCS included ?   thank you ...'''
date = "2015-08-05T06:25:00Z"
lastmod = "2015-08-07T02:14:00Z"
weight = 44865
keywords = [ "framelength" ]
aliases = [ "/questions/44865" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [length field](/questions/44865/length-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44865-score" class="post-score" title="current number of votes">0</div><span id="post-44865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>I captured a ping to my default gateway with Wireshark. I'm now wondering about the "Length" field. From what I already know, the Preamble and FCS fields are not shown by Wireshark. So is this the REAL Frame length? I mean it includes all fields from Preamble to FCS included ?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/lenght.jpg" alt="alt text" /></p><p>thank you for clarification !</p><p>Best Regards</p><p>Adam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-framelength" rel="tag" title="see questions tagged &#39;framelength&#39;">framelength</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '15, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></img></div></div><div id="comments-container-44865" class="comments-container"></div><div id="comment-tools-44865" class="comment-tools"></div><div class="clear"></div><div id="comment-44865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44866"></span>

<div id="answer-container-44866" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44866-score" class="post-score" title="current number of votes">1</div><span id="post-44866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, the length field is displayed by Wireshark. As you stated, the Ethernet preamble is not displayed by Wireshark. Therefore, the length does not include the preamble.</p><p>To confirm this, observe the Packet Details and Packet Bytes section in Wireshark. There are no Ethernet preamble bits shown in either. If you count the bits in the Packet Bytes section it will match the length field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '15, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44866" class="comments-container"><span id="44867"></span><div id="comment-44867" class="comment"><div id="post-44867-score" class="comment-score"></div><div class="comment-text"><p>Thank you! and what about the FCS field? Is it included ? Or is the Wireshark "Length" filed total length of the Ethernet Frame minus Preamble (8 bytes) and FCS (4 bytes )?</p></div><div id="comment-44867-info" class="comment-info"><span class="comment-age">(05 Aug '15, 06:47)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="44868"></span><div id="comment-44868" class="comment"><div id="post-44868-score" class="comment-score"></div><div class="comment-text"><p>Neither the Preamble or FCS is included.</p></div><div id="comment-44868-info" class="comment-info"><span class="comment-age">(05 Aug '15, 06:58)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-44866" class="comment-tools"></div><div class="clear"></div><div id="comment-44866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44871"></span>

<div id="answer-container-44871" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44871-score" class="post-score" title="current number of votes">1</div><span id="post-44871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is showing you the length of the Ethernet frame that is handed to it, which may or may not include the FCS. No capture hardware that I'm aware of saves the preamble or SFD bytes (if it did, it would probably require a new DLT), and most common capture hardware strips away the FCS so that Wireshark (or any packet analysis tool) never sees it. Some capture hardware does retain the FCS though, in which case it could be present in the capture file, and if it is, the Ethernet frame length will reflect those bytes as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '15, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-44871" class="comments-container"><span id="44872"></span><div id="comment-44872" class="comment"><div id="post-44872-score" class="comment-score"></div><div class="comment-text"><p>Actually, there are DLT's such as <code>LINKTYPE_NETANALYZER_TRANSPARENT</code> that do seem to include the preamble, SFD and FCS. See <a href="http://www.tcpdump.org/linktypes.html">http://www.tcpdump.org/linktypes.html</a>. But I'm guessing you're asking about <code>LINKTYPE_ETHERNET</code>.</p></div><div id="comment-44872-info" class="comment-info"><span class="comment-age">(05 Aug '15, 08:20)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="44902"></span><div id="comment-44902" class="comment"><div id="post-44902-score" class="comment-score"></div><div class="comment-text"><p>ok, so i cannot understand one thing. when i run ping it sends 32 bytes "The default is 32. The maximum size is 65,527." So Wireshark is showing the length as 74 bytes. So if I add the Preamble 8 bytes / FCS 4 bytes it makes = 86 bytes. So even if the smallest Ethernet II Frame is 64 bytes (86-64 equals to 22 bytes). So what about the 32 bytes that the ping is sending or am I looking at it in a wrong way ?</p></div><div id="comment-44902-info" class="comment-info"><span class="comment-age">(06 Aug '15, 01:48)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="44907"></span><div id="comment-44907" class="comment"><div id="post-44907-score" class="comment-score">1</div><div class="comment-text"><p><em>or am I looking at it in a wrong way ?</em></p><p>Yes. The 74 bytes is comprised of the following:</p><pre><code>Ethernet header: 14 bytes
IP header (standard): 20 bytes
ICMP header: 8 bytes
ICMP payload: 32 bytes</code></pre></div><div id="comment-44907-info" class="comment-info"><span class="comment-age">(06 Aug '15, 07:49)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="44916"></span><div id="comment-44916" class="comment"><div id="post-44916-score" class="comment-score"></div><div class="comment-text"><p>ok now i see. So 14 bytes for the Ethernet Header (Destination + Source + Type Filed) and 60 bytes which is the actual Layer 3 PDU encapsulated in the Ethernet Frame, correct ?</p><p>Is it technically correct to say that the ICMP message / request is ENCAPSULATED within the IPv4 packet ?</p></div><div id="comment-44916-info" class="comment-info"><span class="comment-age">(07 Aug '15, 02:14)</span> <span class="comment-user userinfo">adasko</span></div></div></div><div id="comment-tools-44871" class="comment-tools"></div><div class="clear"></div><div id="comment-44871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

