+++
type = "question"
title = "Reading tcpdump capture: Complex interface configuration"
description = '''I&#x27;m trying to read a tcpdump capture with Wireshark, but getting pcap: network type 1146433328 unknown or unsupported This box is using 803.1Q vlan tagging over 803.3ad link aggravation and I have not had a problem with that in the past. However, this one also has an alias defined and that seems to ...'''
date = "2014-01-04T09:59:00Z"
lastmod = "2014-01-04T12:45:00Z"
weight = 28569
keywords = [ "tcpdump", "pcap", "network-type-error", "interface-alias" ]
aliases = [ "/questions/28569" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reading tcpdump capture: Complex interface configuration](/questions/28569/reading-tcpdump-capture-complex-interface-configuration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28569-score" class="post-score" title="current number of votes">0</div><span id="post-28569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to read a tcpdump capture with Wireshark, but getting <strong>pcap: network type 1146433328 unknown or unsupported</strong></p><p>This box is using 803.1Q vlan tagging over 803.3ad link aggravation and I have not had a problem with that in the past. However, this one also has an alias defined and that seems to be what's causing the problem. So the interfaces look like:</p><pre><code>eth0--+         +--vlan20   =&gt; 192.168.20.1
      |         |
      +--Bond0--+
      |         |
eth1--+         +--vlan20:1 =&gt; 192.168.20.2</code></pre><p>When I try to replay the capture in Wireshark I get the pcap error. The capture does replay fine with tcpdump. For what its worth, I typically ftp the capture and replay with an MS Windows instance of Wireshark. Again, this appears to be the result of the alias since I don't have problems replaying captures where there isn't one (but there is 803.1Q and 803.3ad). I assume it's due to how tcpdump writes the link layer header. Is there a simple switch, or other way, to read these, or write them in a readable way?</p><p>TIA.</p><p>EDIT:</p><p>I can add a little more to this. Wireshark is getting the network type from offset 0x8b-0x8e in the capture file. In this file the payload of the first packet actually begins at offset 0x52. When you replay the capture in tcpdump the payload begins at offset 0x2a. So, the .cap file has a 40 byte header. I'm guessing there is something in the header that causes Wireshark to misinterpret the file structure.</p><p>EDIT:</p><p>I've decoded the per file header and the first per packet header and I don't see anything obvious. The link layer type is LINKTYPE_ETHERNET just as it should be. Below is the .cap file content, with first packet payload beginning at 52h.</p><pre><code>00000000h: D4 C3 B2 A1 02 00 04 00 00 00 00 00 00 00 00 00 ; ÔÃ²¡............
00000010h: FF FF 00 00 01 00 00 00 DA 67 C8 52 DF 6A 0C 00 ; ÿÿ......ÚgÈRßj..
00000020h: 4C 02 00 00 4C 02 00 00 00 25 90 6C A9 82 00 25 ; L...L....%l©‚.%
00000030h: 90 6A F3 3A 08 00 45 00 02 3E D8 31 00 00 40 11 ; jó:..E..&gt;Ø[email protected]
00000040h: 04 AD C0 A8 14 01 C0 A8 06 7F 13 C4 13 C4 02 2A ; .­À¨..À¨..Ä.Ä.*
00000050h: 0A 6E 4F 50 54 49 4F 4E 53 20 73 69 70 3A 31 30 ; .nOPTIONS sip:10</code></pre><p>BTW, 1146433328d = 44h 55h 2Fh 30h = SIP/2.<strong>0/UD</strong>P</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-network-type-error" rel="tag" title="see questions tagged &#39;network-type-error&#39;">network-type-error</span> <span class="post-tag tag-link-interface-alias" rel="tag" title="see questions tagged &#39;interface-alias&#39;">interface-alias</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '14, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/8d6999530cfff600ff9ba352d2ae675f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlum&#39;s gravatar image" /><p><span>tlum</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlum has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jan '14, 12:18</strong> </span></p></div></div><div id="comments-container-28569" class="comments-container"><span id="28572"></span><div id="comment-28572" class="comment"><div id="post-28572-score" class="comment-score"></div><div class="comment-text"><p>Can you share the pcap file? If not, can you share the first 40-100 bytes as a snippet?</p></div><div id="comment-28572-info" class="comment-info"><span class="comment-age">(04 Jan '14, 11:49)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="28573"></span><div id="comment-28573" class="comment"><div id="post-28573-score" class="comment-score"></div><div class="comment-text"><p>also, can you try to compress the file and then FTP it? Maybe the transfer messes with the file contents.</p></div><div id="comment-28573-info" class="comment-info"><span class="comment-age">(04 Jan '14, 11:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="28574"></span><div id="comment-28574" class="comment"><div id="post-28574-score" class="comment-score"></div><div class="comment-text"><p>For me this snippet opens in Wireshark and says "packet seems to have been cut short", which comes as no surprise. Also, in my hex editor the file looks fine to me, including file and packet header. What Wireshark version are you using, and which OS is this? Can you try a newer version perhaps?</p></div><div id="comment-28574-info" class="comment-info"><span class="comment-age">(04 Jan '14, 12:38)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-28569" class="comment-tools"></div><div class="clear"></div><div id="comment-28569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28575"></span>

<div id="answer-container-28575" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28575-score" class="post-score" title="current number of votes">0</div><span id="post-28575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Tremendously sorry, but the UltraEdit ftp is brain damaged. It appears to have ignored the binary setting and I don't know why. What is even stranger is that if I ftp open the file its binary and its just fine, but if I do a transfer of the file it seems to come over as ascii. But that's not a Wireshark problem, its an UltraEdit problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '14, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/8d6999530cfff600ff9ba352d2ae675f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlum&#39;s gravatar image" /><p><span>tlum</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlum has no accepted answers">0%</span></p></div></div><div id="comments-container-28575" class="comments-container"><span id="28576"></span><div id="comment-28576" class="comment"><div id="post-28576-score" class="comment-score"></div><div class="comment-text"><p>No problem, as long as it works now ;-)</p></div><div id="comment-28576-info" class="comment-info"><span class="comment-age">(04 Jan '14, 12:45)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-28575" class="comment-tools"></div><div class="clear"></div><div id="comment-28575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

