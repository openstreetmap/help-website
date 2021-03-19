+++
type = "question"
title = "what is the reason for Bad checksum [should be 0x55718ef8]"
description = '''Hi, im getting some errors while running wireshark. im getting all these errors from my network printer what could be the reason for that? [Expert Info (Error/Checksum): Bad checksum [should be 0x1c224e67]'''
date = "2017-05-25T09:08:00Z"
lastmod = "2017-05-28T09:24:00Z"
weight = 61627
keywords = [ "checksum", "bad" ]
aliases = [ "/questions/61627" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [what is the reason for Bad checksum \[should be 0x55718ef8\]](/questions/61627/what-is-the-reason-for-bad-checksum-should-be-0x55718ef8)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61627-score" class="post-score" title="current number of votes">0</div><span id="post-61627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>im getting some errors while running wireshark. im getting all these errors from my network printer what could be the reason for that?</p><p>[Expert Info (Error/Checksum): Bad checksum [should be 0x1c224e67]</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-bad" rel="tag" title="see questions tagged &#39;bad&#39;">bad</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '17, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/b5f9e52e6130ce40edaac22f2101403a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vasim&#39;s gravatar image" /><p><span>vasim</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vasim has no accepted answers">0%</span></p></div></div><div id="comments-container-61627" class="comments-container"><span id="61628"></span><div id="comment-61628" class="comment"><div id="post-61628-score" class="comment-score"></div><div class="comment-text"><p>In what context is the checksum? From the size it would seem to be an application protocol?</p></div><div id="comment-61628-info" class="comment-info"><span class="comment-age">(25 May '17, 09:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="61650"></span><div id="comment-61650" class="comment"><div id="post-61650-score" class="comment-score"></div><div class="comment-text"><p>getting this error at broadcast ARP Frame check sequence: 0x00000000 [incorrect, should be 0xa5a56305] im getting this for my 2 network printers.</p></div><div id="comment-61650-info" class="comment-info"><span class="comment-age">(26 May '17, 23:29)</span> <span class="comment-user userinfo">vasim</span></div></div></div><div id="comment-tools-61627" class="comment-tools"></div><div class="clear"></div><div id="comment-61627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61660"></span>

<div id="answer-container-61660" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61660-score" class="post-score" title="current number of votes">1</div><span id="post-61660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>getting this error at broadcast ARP Frame check sequence: 0x00000000 [incorrect, should be 0xa5a56305] im getting this for my 2 network printers.</p></blockquote><p>It probably means that Wireshark thinks the packet, as captured, has a CRC at the end when, in fact, it doesn't. (All Ethernet packets have a CRC at the end - but not all capture devices and mechanisms include the CRC in the packet data.)</p><p>We'd have to see one of the packets (preferably in the form of a capture file, rather than a screenshot) to see whether this is a problem in Wireshark or just some case where there's not enough information for Wireshark to determine whether there's a CRC or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '17, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61660" class="comments-container"><span id="61668"></span><div id="comment-61668" class="comment"><div id="post-61668-score" class="comment-score"></div><div class="comment-text"><p><code> Frame 36594: 64 bytes on wire (512 bits), 64 bytes captured (512 bits) on interface 0     Interface id: 0 (\Device\NPF_{0A822D34-D117-4A97-9600-B75053AE0252})     Encapsulation type: Ethernet (1)     Arrival Time: May 25, 2017 20:12:20.225033000 Arabian Standard Time     [Time shift for this packet: 0.000000000 seconds]     Epoch Time: 1495728740.225033000 seconds     [Time delta from previous captured frame: 0.005614000 seconds]     [Time delta from previous displayed frame: 0.005614000 seconds]     [Time since reference or first frame: 2067.779529000 seconds]     Frame Number: 36594     Frame Length: 64 bytes (512 bits)     Capture Length: 64 bytes (512 bits)     [Frame is marked: False]     [Frame is ignored: False]     [Protocols in frame: eth:ethertype:arp]     [Coloring Rule Name: ARP]     [Coloring Rule String: arp] Ethernet II, Src: Sharp_51:df:3b (34:f6:2d:51:df:3b), Dst: Broadcast (ff:ff:ff:ff:ff:ff)     Destination: Broadcast (ff:ff:ff:ff:ff:ff)         Address: Broadcast (ff:ff:ff:ff:ff:ff)         .... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the factory default)         .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)     Source: Sharp_51:df:3b (34:f6:2d:51:df:3b)         Address: Sharp_51:df:3b (34:f6:2d:51:df:3b)         .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)         .... ...0 .... .... .... .... = IG bit: Individual address (unicast)     Type: ARP (0x0806)     Padding: 000000000000000000000000000000000000     Frame check sequence: 0x00000000 [incorrect, should be 0x1c224e67]         [Expert Info (Error/Checksum): Bad checksum [should be 0x1c224e67]]             [Bad checksum [should be 0x1c224e67]]             [Severity level: Error]             [Group: Checksum]     [FCS Status: Bad] Address Resolution Protocol (request)     Hardware type: Ethernet (1)     Protocol type: IPv4 (0x0800)     Hardware size: 6     Protocol size: 4     Opcode: request (1)     Sender MAC address: Sharp_51:df:3b (34:f6:2d:51:df:3b)     Sender IP address: 192.168.0.225     Target MAC address: 00:00:00_00:00:00 (00:00:00:00:00:00)     Target IP address: 192.168.0.205</code></p></div><div id="comment-61668-info" class="comment-info"><span class="comment-age">(28 May '17, 04:05)</span> <span class="comment-user userinfo">vasim</span></div></div><span id="61675"></span><div id="comment-61675" class="comment"><div id="post-61675-score" class="comment-score"></div><div class="comment-text"><p>OK, this is on Windows (on UN*X, interfaces don't have names like <code>\Device\NPF_{0A822D34-D117-4A97-9600-B75053AE0252}</code>), and the frame is claimed to be 64 bytes long, but it's an ARP packet, which means that it's short enough that the payload is less than 64-(14+4) = 46 bytes long.</p><p>That means that, if the host that transmitted it padded the payload sufficiently to make it a minimum-length Ethernet frame, if it were 64 bytes long the last 4 bytes would be the FCS.</p><p>So, given that the last 4 bytes are zero, either 1) the machine that sent it added an extra 4 bytes of padding - which is legal, although wasteful - or 2) those 4 bytes of zero were added by something else.</p><p>Perhaps Wireshark's heuristic to guess whether there's an FCS or not should assume that if the last 4 bytes of the frame are zero, it's not an FCS. For now, just ignore those errors if the FCS is reported as zero.</p></div><div id="comment-61675-info" class="comment-info"><span class="comment-age">(28 May '17, 09:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-61660" class="comment-tools"></div><div class="clear"></div><div id="comment-61660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

