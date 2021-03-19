+++
type = "question"
title = "Capture Filter for EAPOL packets does not show anything"
description = '''I am trying to capture only the EAPOL packets from my WLAN. I have read on the CaptureFilters wiki page that this should work with: ether proto 0x888e  But when i put that into wireshark it does not capture anything. So i played with the display filters, i think the equivalet there is: eth.type == 0...'''
date = "2016-01-03T13:59:00Z"
lastmod = "2016-01-05T13:37:00Z"
weight = 48811
keywords = [ "0x888e", "ethertype", "eapol", "capture-filter" ]
aliases = [ "/questions/48811" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filter for EAPOL packets does not show anything](/questions/48811/capture-filter-for-eapol-packets-does-not-show-anything)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48811-score" class="post-score" title="current number of votes">0</div><span id="post-48811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture only the EAPOL packets from my WLAN. I have read on the CaptureFilters wiki page that this should work with:</p><pre><code>ether proto 0x888e</code></pre><p>But when i put that into wireshark it does not capture anything.</p><p>So i played with the display filters, i think the equivalet there is:</p><pre><code>eth.type == 0x888e</code></pre><p>which also shows nothing on a data set that definitely contains EAPOL packets. Instead i could just set:</p><pre><code>eapol</code></pre><p>as the display filter and it works perfectly, the right packets show up.</p><p>Is it possible to set that somehow as capture filter? Bug in Wireshark or wrong filter?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-0x888e" rel="tag" title="see questions tagged &#39;0x888e&#39;">0x888e</span> <span class="post-tag tag-link-ethertype" rel="tag" title="see questions tagged &#39;ethertype&#39;">ethertype</span> <span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '16, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/8f75ba0079df65511021b81cef8fd4a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jake&#39;s gravatar image" /><p><span>Jake</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jake has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jan '16, 14:02</strong> </span></p></div></div><div id="comments-container-48811" class="comments-container"><span id="48815"></span><div id="comment-48815" class="comment"><div id="post-48815-score" class="comment-score"></div><div class="comment-text"><p>Do the packets you're capturing display in Wireshark/TShark with Ethernet headers or 802.11 headers? If they show 802.11 headers (from what is probably a monitor mode capture), <code>eth.type</code> won't be a valid field - you'll need to use <code>llc.type</code>, as Bob Jones indicated.</p><p>If you use a display filter of <code>eapol</code>:</p><ul><li>if the packets have an Ethernet header, what value do the EAPOL packets have in the Ethernet type field?</li><li>if the packets have an LLC and SNAP header, what are the OUI and PID values in the SNAP header for the EAPOL packets?</li></ul></div><div id="comment-48815-info" class="comment-info"><span class="comment-age">(03 Jan '16, 15:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="48818"></span><div id="comment-48818" class="comment"><div id="post-48818-score" class="comment-score"></div><div class="comment-text"><p>Yes, it is a wpa handshake with 802.11 headers from my card in monitor mode.</p></div><div id="comment-48818-info" class="comment-info"><span class="comment-age">(03 Jan '16, 16:43)</span> <span class="comment-user userinfo">Jake</span></div></div><span id="48820"></span><div id="comment-48820" class="comment"><div id="post-48820-score" class="comment-score"></div><div class="comment-text"><p>OK, so what are the OUI and PID values in the SNAP header for the EAPOL packets?</p></div><div id="comment-48820-info" class="comment-info"><span class="comment-age">(03 Jan '16, 16:49)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="48822"></span><div id="comment-48822" class="comment"><div id="post-48822-score" class="comment-score"></div><div class="comment-text"><p>I am not sure what OUI/PID are, so here is the whole LLC header:</p><pre><code>Logical-Link Control
    DSAP: SNAP (0xaa)
        1010 101. = SAP: SNAP
        .... ...0 = IG Bit: Individual
    SSAP: SNAP (0xaa)
        1010 101. = SAP: SNAP
        .... ...0 = CR Bit: Command
    Control field: U, func=UI (0x03)
        000. 00.. = Command: Unnumbered Information (0x00)
        .... ..11 = Frame type: Unnumbered frame (0x03)
    Organization Code: Encapsulated Ethernet (0x000000)
    Type: 802.1X Authentication (0x888e)</code></pre></div><div id="comment-48822-info" class="comment-info"><span class="comment-age">(04 Jan '16, 01:23)</span> <span class="comment-user userinfo">Jake</span></div></div><span id="48824"></span><div id="comment-48824" class="comment"><div id="post-48824-score" class="comment-score"></div><div class="comment-text"><p>If you select the <code>Type: 802.1X Authentication (0x888e)</code> item in the packet details pane, then, in the hex/ASCII dump pane, does it show data in the "Frame" tab or the "Decrypted WEP data"/"Decrypted CCIP data"/"Decrypted TKMP data" tab of that pane?</p></div><div id="comment-48824-info" class="comment-info"><span class="comment-age">(04 Jan '16, 02:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="48829"></span><div id="comment-48829" class="comment not_top_scorer"><div id="post-48829-score" class="comment-score"></div><div class="comment-text"><p>What tabs? I see only these 2 bytes highlighted in the hex pane after selecting that.</p></div><div id="comment-48829-info" class="comment-info"><span class="comment-age">(04 Jan '16, 03:23)</span> <span class="comment-user userinfo">Jake</span></div></div><span id="48851"></span><div id="comment-48851" class="comment not_top_scorer"><div id="post-48851-score" class="comment-score"></div><div class="comment-text"><p>The hex pane doesn't have two named tabs?</p></div><div id="comment-48851-info" class="comment-info"><span class="comment-age">(04 Jan '16, 12:02)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="48865"></span><div id="comment-48865" class="comment not_top_scorer"><div id="post-48865-score" class="comment-score"></div><div class="comment-text"><p>No. I dont have added any WPA decryption keys to the config so far, thats probably the reason.</p><p>Have you read the comments under Bob Jones Answer? An idea why is that?</p></div><div id="comment-48865-info" class="comment-info"><span class="comment-age">(05 Jan '16, 05:39)</span> <span class="comment-user userinfo">Jake</span></div></div><span id="48876"></span><div id="comment-48876" class="comment not_top_scorer"><div id="post-48876-score" class="comment-score"></div><div class="comment-text"><p>So the frame you're showing <em>hasn't</em> been decrypted? And you're capturing in monitor mode? But when you capture with <code>ether photo 0x888e</code>, packets like that one aren't captured?</p></div><div id="comment-48876-info" class="comment-info"><span class="comment-age">(05 Jan '16, 12:06)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="48877"></span><div id="comment-48877" class="comment not_top_scorer"><div id="post-48877-score" class="comment-score"></div><div class="comment-text"><p>Yes, yes and yes. (*proto not photo)</p></div><div id="comment-48877-info" class="comment-info"><span class="comment-age">(05 Jan '16, 12:25)</span> <span class="comment-user userinfo">Jake</span></div></div><span id="48878"></span><div id="comment-48878" class="comment not_top_scorer"><div id="post-48878-score" class="comment-score"></div><div class="comment-text"><blockquote><p>(*proto not photo)</p></blockquote><p>(Damn you autocorrect!)</p><p>So, in the capture options dialog, is there a "Compile BPFs" or "Compile selected BPFs" button? If so, what gets shown if, before starting a capture with the filter <code>ether proto 0x888e</code>, you push that button? It should pop up a window with text; what's the text?</p></div><div id="comment-48878-info" class="comment-info"><span class="comment-age">(05 Jan '16, 12:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="48879"></span><div id="comment-48879" class="comment not_top_scorer"><div id="post-48879-score" class="comment-score"></div><div class="comment-text"><p>(Why won't OSQA allow a comment to begin with fixed-width text?)</p><pre><code>(000) ldb      [3]
(001) lsh      #8
(002) tax      
(003) ldb      [2]
(004) or       x
(005) st       M[0]
(006) tax      
(007) txa      
(008) add      #24
(009) st       M[1]
(010) ldb      [x + 0]
(011) jset     #0x8             jt 12   jf 28
(012) jset     #0x4             jt 28   jf 13
(013) jset     #0x80            jt 14   jf 17
(014) ld       M[1]
(015) add      #2
(016) st       M[1]
(017) ld       [4]
(018) jset     #0x2000000       jt 19   jf 28
(019) jset     #0x1000000       jt 20   jf 22
(020) ldb      [16]
(021) jset     #0x20            jt 24   jf 28
(022) ldb      [8]
(023) jset     #0x20            jt 24   jf 28
(024) ld       M[1]
(025) add      #3
(026) and      #0xfffffffc
(027) st       M[1]
(028) ldx      M[0]
(029) ldb      [x + 0]
(030) jset     #0x4             jt 38   jf 31
(031) ldx      M[0]
(032) ldb      [x + 0]
(033) jset     #0x8             jt 34   jf 38
(034) ldx      M[1]
(035) ldh      [x + 6]
(036) jeq      #0x888e          jt 37   jf 38
(037) ret      #262144
(038) ret      #0</code></pre><p>(Why does it always change the layout after posting?)</p></div><div id="comment-48879-info" class="comment-info"><span class="comment-age">(05 Jan '16, 13:04)</span> <span class="comment-user userinfo">Jake</span></div></div><span id="48884"></span><div id="comment-48884" class="comment not_top_scorer"><div id="post-48884-score" class="comment-score"></div><div class="comment-text"><blockquote><p>(Why does it always change the layout after posting?)</p></blockquote><p>Because it assumes most of what you're typing is free-form text, which it wraps. If you want fixed-formatted text, you either need to put it in backquotes or begin each line with 4 spaces. (And you can't <em>begin</em> a comment with a 4-space indent, which is why I added the parenthesized note to your comment.)</p></div><div id="comment-48884-info" class="comment-info"><span class="comment-age">(05 Jan '16, 13:37)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-48811" class="comment-tools"><span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a></div><div class="clear"></div><div id="comment-48811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48813"></span>

<div id="answer-container-48813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48813-score" class="post-score" title="current number of votes">0</div><span id="post-48813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I use ether proto 0x888e as a capture filter in Windump or tcpdump, such as:</p><pre><code>C:\traces&gt;windump -i 1 -s 1600 -w EAPOL -W 200 -C 200 ether proto 0x888e</code></pre><p>but it's really only good for the 4-way WPA handshake. Group rekeys are encrypted, so tougher to get. Share your trace and we can have a look. Exactly where do you put this filter when configuring?</p><blockquote><blockquote><p>eth.type == 0x888e</p></blockquote></blockquote><p>If it is a trace with 802.11 headers, this will likely not work. Try:</p><pre><code>llc.type == 0x888e</code></pre><p>Without capture filter: <img src="https://osqa-ask.wireshark.org/upfiles/Without_eapol_filter.png" alt="alt text" /></p><p>With Capture filter in place: <img src="https://osqa-ask.wireshark.org/upfiles/With_eapol_filter.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '16, 15:10</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jan '16, 05:13</strong> </span></p></div></div><div id="comments-container-48813" class="comments-container"><span id="48819"></span><div id="comment-48819" class="comment"><div id="post-48819-score" class="comment-score"></div><div class="comment-text"><p>I put that into the display filter field (in the Wireshark gui), but eth.type was just a guess, i understand now that this is a other header and it works fine with llc.type. My question ist still how to set that as capture filter?</p></div><div id="comment-48819-info" class="comment-info"><span class="comment-age">(03 Jan '16, 16:45)</span> <span class="comment-user userinfo">Jake</span></div></div><span id="48835"></span><div id="comment-48835" class="comment"><div id="post-48835-score" class="comment-score"></div><div class="comment-text"><p>I just did a test on Windows with Wireshark - with a capture filter of</p><p>ether proto 0x888e</p><p>At the same time, I ran another Wireshark process but this time with no capture filter, with only a display filter of eapol and confirm both show the same exact packets. Note that the open capture had 40K+ total packets, displaying only 15, while the capture filter Wireshark only captured and display 15. If I can get a screenshot posted, I will do so.</p><p>This is on a Windows7 system with AirPcapNx.</p></div><div id="comment-48835-info" class="comment-info"><span class="comment-age">(04 Jan '16, 05:07)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="48839"></span><div id="comment-48839" class="comment"><div id="post-48839-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your effort! But i did the same test, my capture options are exactly the same as on the screenshoot and i get nothing. I tried some of the other capture filter presets and they all worked, even "ether proto" with other numbers (for example 0x0800 - IPv4). So is it a bug?</p><p>Wireshark 2.0.0 (from the offical repo) on Manjaro Linux.</p></div><div id="comment-48839-info" class="comment-info"><span class="comment-age">(04 Jan '16, 08:11)</span> <span class="comment-user userinfo">Jake</span></div></div><span id="48842"></span><div id="comment-48842" class="comment"><div id="post-48842-score" class="comment-score"></div><div class="comment-text"><p>Tested on Kali2 w/ Wireshark 1.12.6 (whatever is in the repository) and it works as expected, just like my Windows screenshots. Maybe you found something with Wireshark2/Linux?</p></div><div id="comment-48842-info" class="comment-info"><span class="comment-age">(04 Jan '16, 08:57)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="48848"></span><div id="comment-48848" class="comment"><div id="post-48848-score" class="comment-score"></div><div class="comment-text"><p>Okay, so i tested it with Kali 2 and got nothing again...</p><p>Then i found out that the wlan adapter has something to do with it: All the tests were on my Intel 3160, if i use a USB TL-WN722N instead i get at least some packets, but only 1-2 from a 4 way handshake (totally random which one), while the 2.Wireshark without filter captures all.</p></div><div id="comment-48848-info" class="comment-info"><span class="comment-age">(04 Jan '16, 10:37)</span> <span class="comment-user userinfo">Jake</span></div></div></div><div id="comment-tools-48813" class="comment-tools"></div><div class="clear"></div><div id="comment-48813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

