+++
type = "question"
title = "Extra fields displayed in ICMP capture"
description = '''In trying to manually determine the maximum transmission unit (MTU) of a triple IPsec encrypted link, I am using ICMP to form the basis. The MTU is not adding up correctly based on Wireshark output. The number of bytes adds up correctly but the displayed ICMP fields seem to be incorrect. And Wiresha...'''
date = "2011-03-15T07:12:00Z"
lastmod = "2011-03-23T16:45:00Z"
weight = 2827
keywords = [ "icmp" ]
aliases = [ "/questions/2827" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extra fields displayed in ICMP capture](/questions/2827/extra-fields-displayed-in-icmp-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2827-score" class="post-score" title="current number of votes">0</div><span id="post-2827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In trying to manually determine the maximum transmission unit (MTU) of a triple IPsec encrypted link, I am using ICMP to form the basis. The MTU is not adding up correctly based on Wireshark output. The number of bytes adds up correctly but the displayed ICMP fields seem to be incorrect. And Wireshark includes two sequence number fields in the ICMP request and ICMP reply which does not folow the documented ICMP packet structure - OR did things change again and I'm still asleep :) ?</p><p>The Ping request total bytes is 1314 bytes, correct</p><p>The Ping reply total bytes is 1318 bytes, correct</p><p>The extra fields displayed within each captured packet seems to be incorrect.</p><p>:::::::::::::::::::::::</p><p>Win XP Pro with Service pack 2:</p><p>C:&gt;ping –n 1 –l 1272 –f –i 2 192.168.1.1</p><p>:::::::::::::::::::::::::</p><p>When I capture (Wireshark 1.4.4) the ICMP request and reply, I expect Wireshark to display:</p><p>• Ethernet header</p><p>• IP header</p><p>• ICMP header and ICMP data</p><p>When I expand the ICMP request header, I expect Wireshark to display:</p><p>• Type field</p><p>• Code</p><p>• Checksum</p><p>When I expand the ICMP reply header, I expect Wireshark to display:</p><p>• Type field</p><p>• Code</p><p>• Checksum</p><p>• Identifier</p><p>• Sequence number</p><p>BUT, instead I see the following:</p><p>ICMP Type: 8 (Echo (ping) request)</p><p>Code: 0</p><p>Checksum: 0x92c2 [correct]</p><p>Identified: 0x200</p><p>Sequence number: 7680 (0xle00)</p><p>Sequence number (LE): 30 (ox00le)</p><p>Data (1272 bytes)</p><p>::::::::::::::::::</p><p>ICMP Type: 0 (Echo (ping) reply)</p><p>Code: 0</p><p>Checksum: 0x9ac2 [correct]</p><p>Identified: 0x200</p><p>Sequence number: 7680 (0xle00)</p><p>Sequence number (LE): 30 (ox00le)</p><p>Data (1272 bytes)</p><p>:::::::::::::::::::</p><p>This is the expected view of the ICMP packet as explained in TCP/IP Illistrated Vol. 1 as well as most web searches.</p><p>Ping request:</p><p>Ethernet header = 18 bytes</p><p>IP header = 20 bytes</p><p>ICMP header = 4 bytes</p><p>The ICMP portion is expanded to reveal these fields:</p><pre><code>    Type code   = 1 byte

    Code        = 1 byte

    Checksum    = 2 bytes</code></pre><p>Data = 1272 bytes</p><p>TOTAL of PING REQUEST = 1314 bytes</p><p>:::::::::::::::::::::::</p><p>Ping reply:</p><p>Ethernet header = 18 bytes</p><p>IP header = 20 bytes</p><p>ICMP header = 8 bytes</p><p>The ICMP portion is expanded to reveal these fields:</p><pre><code>    Type code   = 1 byte

    Code        = 1 byte

    Checksum    = 2 bytes

    Identifier  = 2 bytes

    Sequence #  = 2 bytes</code></pre><p>Data = 1272 bytes</p><p>TOTAL of PING REPLY = 1318 bytes</p><p>::::::::::::::::</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '11, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/e0d8e2d933cdb529440838255909920b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fsebera&#39;s gravatar image" /><p><span>fsebera</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fsebera has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Mar '11, 04:53</strong> </span></p></div></div><div id="comments-container-2827" class="comments-container"><span id="2835"></span><div id="comment-2835" class="comment"><div id="post-2835-score" class="comment-score"></div><div class="comment-text"><p>So what are the "extra fields" in question?</p></div><div id="comment-2835-info" class="comment-info"><span class="comment-age">(15 Mar '11, 10:09)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-2827" class="comment-tools"></div><div class="clear"></div><div id="comment-2827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2875"></span>

<div id="answer-container-2875" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2875-score" class="post-score" title="current number of votes">1</div><span id="post-2875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are no extra fields. The sequence number field is simply being displayed in both big and little endian format to make it easier to follow when those sequence numbers are incrementing from one ICMP echo request/reply to the next. The reason both formats are shown is because the fields are populated in either big or little endian format, depending upon the OS and there is no definitive way to tell which format it's in from the contents of the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '11, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-2875" class="comments-container"><span id="3030"></span><div id="comment-3030" class="comment"><div id="post-3030-score" class="comment-score"></div><div class="comment-text"><p>Ok Great, thanks for explaining what's happening here. : BUT, is there a way [in Wireshark] to disable all of the Wireshark generated extra fields so it would be easier to determine what is on the wire verses what Wireshark adds. : Thanks again n best regards Frank</p></div><div id="comment-3030-info" class="comment-info"><span class="comment-age">(22 Mar '11, 11:22)</span> <span class="comment-user userinfo">fsebera</span></div></div><span id="3031"></span><div id="comment-3031" class="comment"><div id="post-3031-score" class="comment-score"></div><div class="comment-text"><p>Not to my knowledge, there isn't.</p></div><div id="comment-3031-info" class="comment-info"><span class="comment-age">(22 Mar '11, 11:26)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-2875" class="comment-tools"></div><div class="clear"></div><div id="comment-2875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3072"></span>

<div id="answer-container-3072" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3072-score" class="post-score" title="current number of votes">0</div><span id="post-3072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Don't forget, Windows adds 8 bytes for the ICMP header. So if you send 1460 byte ICMP (-l 1460), you still have to account for 20 bytes of IP header and 8 bytes of ICMP header. So the IP packet will be 1488 bytes (1460 ICMP + 8 ICMP header + 20 IP header).<br />
</p><p>Also, if you want to see the ICMP packet size, open up the ICMP header and add the ICMP data size as a column.<br />
</p><p>One more thing, not everyone will send you an ICMP 3/4 message. So you <em>may</em> never be able to determine the MTU via Path-MTU Discovery. So your method of sending pings of varying size manually may be the only option. This is why Cisco routers offer you the hack option of munging the MSS field on the router (via tcp intercept)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Mar '11, 16:47</strong> </span></p></div></div><div id="comments-container-3072" class="comments-container"></div><div id="comment-tools-3072" class="comment-tools"></div><div class="clear"></div><div id="comment-3072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

