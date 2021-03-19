+++
type = "question"
title = "Capture filter not capturing - same as display filter works"
description = '''Hello, I have the two TCP packets in my stream with the following payload: 00 00 00 0b 06 ff 82 00 00 00 01 00 00 00 00 00 00 00 0b 07 ff 82 00 00 00 01 78 bf 88 b0 I want to capture both of them with the following capture filter: tcp port 4500 and tcp[26:1]==0x82 and (tcp[24:1]==06 or tcp[24:1]==07...'''
date = "2015-11-05T21:57:00Z"
lastmod = "2015-11-10T03:51:00Z"
weight = 47323
keywords = [ "capture-filter", "display-filter" ]
aliases = [ "/questions/47323" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter not capturing - same as display filter works](/questions/47323/capture-filter-not-capturing-same-as-display-filter-works)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47323-score" class="post-score" title="current number of votes">0</div><span id="post-47323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have the two TCP packets in my stream with the following payload:</p><p>00 00 00 0b 06 ff 82 00 00 00 01 00 00 00 00</p><p>00 00 00 0b 07 ff 82 00 00 00 01 78 bf 88 b0</p><p>I want to capture both of them with the following capture filter: tcp port 4500 and tcp[26:1]==0x82 and (tcp[24:1]==06 or tcp[24:1]==07)</p><p>The problem is, the first packet with 06 is captured, the second is not.</p><p>If I capture everything and apply the following display filter it works: tcp.port==4500 &amp;&amp; tcp[26:1]==0x82 &amp;&amp; (tcp[24]==06 || tcp[24]==07)</p><p>I don't understand it. In my opinion the capture filter is correct. I'm running the current version of wireshark and winpcap</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '15, 21:57</strong></p><img src="https://secure.gravatar.com/avatar/1980571959547796b06e97e252056436?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sputnik24&#39;s gravatar image" /><p><span>Sputnik24</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sputnik24 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '15, 05:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-47323" class="comments-container"><span id="47324"></span><div id="comment-47324" class="comment"><div id="post-47324-score" class="comment-score"></div><div class="comment-text"><p>They look oke, but are there (varying) TCP options involved? The index into TCP doesn't necessarily land you on your payload bytes then.</p></div><div id="comment-47324-info" class="comment-info"><span class="comment-age">(06 Nov '15, 00:43)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="47325"></span><div id="comment-47325" class="comment"><div id="post-47325-score" class="comment-score"></div><div class="comment-text"><p>Length is always the same. Here are the full packets:</p><p>0010020e001fc22697fdbd8008004500003765c040008006f1cea9fe500aa9feff2ac0791194cfc8cac3ea530c4850183ff3df5700000000000b06ff820000000100000000</p><p>c22697fdbd800010020e001f080045000037d9ef40004006bd9fa9feff2aa9fe500a1194c079ea530c48cfc8cad250180b58a2e200000000000b07ff820000000178bf88b0</p></div><div id="comment-47325-info" class="comment-info"><span class="comment-age">(06 Nov '15, 00:47)</span> <span class="comment-user userinfo">Sputnik24</span></div></div><span id="47351"></span><div id="comment-47351" class="comment"><div id="post-47351-score" class="comment-score"></div><div class="comment-text"><p>Nope, no IP or TCP options.</p><p>If the capture filter in Wireshark has a "Compile selected BPFs" or "Compile BPFs" button next to it, if you click on that button when your capture filter is typed in, it should pop up a window with some cryptic text in it (well, cryptic unless you're a BPF geek). Please copy the text from that window and paste it in a comment. (Please don't post a screenshot, just copy and paste the text - that's all we want.)</p></div><div id="comment-47351-info" class="comment-info"><span class="comment-age">(06 Nov '15, 14:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="47361"></span><div id="comment-47361" class="comment"><div id="post-47361-score" class="comment-score"></div><div class="comment-text"><p>I've already looked at the compiled BPF code (assuming ethernet), and if you read assembly language it's not that hard to follow ;)</p><pre><code>(000) ldh      [12]
(001) jeq      #0x86dd          jt 18   jf 2
(002) jeq      #0x800           jt 3    jf 18
(003) ldb      [23]
(004) jeq      #0x6             jt 5    jf 18
(005) ldh      [20]
(006) jset     #0x1fff          jt 18   jf 7
(007) ldxb     4*([14]&amp;0xf)
(008) ldh      [x + 14]
(009) jeq      #0x1194          jt 12   jf 10
(010) ldh      [x + 16]
(011) jeq      #0x1194          jt 12   jf 18
(012) ldb      [x + 40]
(013) jeq      #0x82            jt 14   jf 18
(014) ldb      [x + 38]
(015) jeq      #0x6             jt 17   jf 16
(016) jeq      #0x7             jt 17   jf 18
(017) ret      #262144
(018) ret      #0</code></pre><p>It looks for IPv4, looks for TCP, gets the IPv4 header length, looks for source or destination port 4500, then looks for the respective databytes. Couldn't see a flaw in that, other than TCP options taking space.</p><p>Hope he can paste his.</p></div><div id="comment-47361-info" class="comment-info"><span class="comment-age">(07 Nov '15, 14:41)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="47362"></span><div id="comment-47362" class="comment"><div id="post-47362-score" class="comment-score"></div><div class="comment-text"><p>That's what libpcap generated on your machine; perhaps there's a code generator bug in the libpcap/WInPcap on the original poster's machine. (And, yes, both packets have what appear to be Ethernet headers.)</p></div><div id="comment-47362-info" class="comment-info"><span class="comment-age">(07 Nov '15, 17:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="47365"></span><div id="comment-47365" class="comment not_top_scorer"><div id="post-47365-score" class="comment-score"></div><div class="comment-text"><p>Indeed, so OP please post your compiled BPF.</p></div><div id="comment-47365-info" class="comment-info"><span class="comment-age">(08 Nov '15, 01:21)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="47449"></span><div id="comment-47449" class="comment not_top_scorer"><div id="post-47449-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>thanks a lot and sorry for the late response. Before I post the BPF code here some new infos:</p><p>We have a XenServer hosting 4 VMs with Windows 7. They are using virtual NICs linked to real NICs of the Server. The described error exists there. We have additionally single PCs running Windows 7 and a similiar hardware environment. Here, the capture filter works.</p><p>Filter: tcp port 4500 and tcp[20:4]==0x0000000B and (tcp[24:1]==06 or tcp[24:1]==07) and tcp[26:1]==0x82</p><p>BPF code, looks the same at VM and PC:</p><pre><code>(000) ldh      [12]
(001) jeq      #0x86dd          jt 20   jf 2
(002) jeq      #0x800           jt 3    jf 20
(003) ldb      [23]
(004) jeq      #0x6             jt 5    jf 20
(005) ldh      [20]
(006) jset     #0x1fff          jt 20   jf 7
(007) ldxb     4*([14]&amp;0xf)
(008) ldh      [x + 14]
(009) jeq      #0x1194          jt 12   jf 10
(010) ldh      [x + 16]
(011) jeq      #0x1194          jt 12   jf 20
(012) ld       [x + 34]
(013) jeq      #0xb             jt 14   jf 20
(014) ldb      [x + 38]
(015) jeq      #0x6             jt 17   jf 16
(016) jeq      #0x7             jt 17   jf 20
(017) ldb      [x + 40]
(018) jeq      #0x82            jt 19   jf 20
(019) ret      #65535
(020) ret      #0</code></pre><p>It looks like a problem of VM, but without filter I can see the frame. Why doesn't Wireshark capture it at the VM? Weird.</p></div><div id="comment-47449-info" class="comment-info"><span class="comment-age">(09 Nov '15, 23:27)</span> <span class="comment-user userinfo">Sputnik24</span></div></div><span id="47463"></span><div id="comment-47463" class="comment not_top_scorer"><div id="post-47463-score" class="comment-score"></div><div class="comment-text"><p>You're not very specific on where you capture the network traffic: In the Win7 guest, in the Xen host on the VIF, on the PIF, or on a bridge maybe?</p></div><div id="comment-47463-info" class="comment-info"><span class="comment-age">(10 Nov '15, 03:51)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-47323" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-47323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

