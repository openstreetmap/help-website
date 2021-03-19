+++
type = "question"
title = "ftp downloads failing"
description = ''' see attached screenshot my ftp downloads are failing randomly. the download starts fine and goes upto 99.9% after which it stalls for a few seconds and asks me to start the download again. I have an inline sourcefire device which is allowing traffic thru any ideas ?'''
date = "2016-09-29T07:20:00Z"
lastmod = "2016-09-30T08:12:00Z"
weight = 55986
keywords = [ "ftp" ]
aliases = [ "/questions/55986" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ftp downloads failing](/questions/55986/ftp-downloads-failing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55986-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/do.jpg" alt="alt text" /></p><p>see attached screenshot</p><p>my ftp downloads are failing randomly. the download starts fine and goes upto 99.9% after which it stalls for a few seconds and asks me to start the download again. I have an inline sourcefire device which is allowing traffic thru</p><p>any ideas ?</p></div><div id="question-tags" class="tags-container tags">ftp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '16, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/0b247a9c8e15d271b4d37cedc0876022?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tmkunte&#39;s gravatar image" /><p>tmkunte<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tmkunte has no accepted answers">0%</span></p></img></div></div><div id="comments-container-55986" class="comments-container"><span id="56003"></span><div id="comment-56003" class="comment"><div id="post-56003-score" class="comment-score"></div><div class="comment-text"><p>The sourcefire device fails?</p></div><div id="comment-56003-info" class="comment-info"><span class="comment-age">(30 Sep '16, 04:30)</span> Jaap ♦</div></div><span id="56010"></span><div id="comment-56010" class="comment"><div id="post-56010-score" class="comment-score"></div><div class="comment-text"><p>no it does not</p></div><div id="comment-56010-info" class="comment-info"><span class="comment-age">(30 Sep '16, 05:51)</span> tmkunte</div></div><span id="56012"></span><div id="comment-56012" class="comment"><div id="post-56012-score" class="comment-score"></div><div class="comment-text"><p>Well, I can't think of anything else based on the data provided.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>? Problem solving from a screenshot is a pain since all (possible relevant) details are missing.</p><p>What are the IP addresses of the nodes involved?</p></div><div id="comment-56012-info" class="comment-info"><span class="comment-age">(30 Sep '16, 06:13)</span> Jaap ♦</div></div><span id="56013"></span><div id="comment-56013" class="comment"><div id="post-56013-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.cloudshark.org/captures/00661524237a">https://www.cloudshark.org/captures/00661524237a</a></p><p>source IP is 10.100.26.16</p><p>destination ftp server is 216.75.205.235</p></div><div id="comment-56013-info" class="comment-info"><span class="comment-age">(30 Sep '16, 06:24)</span> tmkunte</div></div><span id="56014"></span><div id="comment-56014" class="comment"><div id="post-56014-score" class="comment-score"></div><div class="comment-text"><p>@tmkunte</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-56014-info" class="comment-info"><span class="comment-age">(30 Sep '16, 06:26)</span> grahamb ♦</div></div><span id="56019"></span><div id="comment-56019" class="comment not_top_scorer"><div id="post-56019-score" class="comment-score"></div><div class="comment-text"><p>At which point, 1 or 2, in the chain</p><pre><code>client --1-- sourcefire --2-- server</code></pre><p>has the capture been taken?</p><p>You should capture at both places <strong>simultaneously</strong> to find out whether the last data segment (429 bytes total frame size) has been corrupt already by the sender or by the sourcefire box.</p></div><div id="comment-56019-info" class="comment-info"><span class="comment-age">(30 Sep '16, 07:25)</span> sindy</div></div><span id="56022"></span><div id="comment-56022" class="comment not_top_scorer"><div id="post-56022-score" class="comment-score"></div><div class="comment-text"><p>Looking at that capture reviles a lot. These last frames are totally borked, since looking at the raw bytes shows that there's FTP data, but the packet headers say there's nothing, followed by an incorrect Ethernet checksum.</p><p>Would be interesting to see if sindy's #2 capture point shows that too.</p></div><div id="comment-56022-info" class="comment-info"><span class="comment-age">(30 Sep '16, 08:10)</span> Jaap ♦</div></div><span id="56025"></span><div id="comment-56025" class="comment not_top_scorer"><div id="post-56025-score" class="comment-score"></div><div class="comment-text"><p>The <code>ethernet FCS bad</code> seems to me to be a Wireshark "issue" rather than a sourcefire one - in particular, a consequence of the fact that the <code>tcp</code> dissector stops dealing with the payload at the point of finding the broken <code>tcp.ack</code> value and reports back the processed tvb size only spanning the header up to that value. So the <code>ip</code> dissector does the same, and the <code>ether</code> dissector, as no payload size field exists in the Ethernet frame header, thus handles the rest of the packet as just a stuffing until the minimum frame size, and as there are still more bytes available than the minimum size, it treats them as the FCS.</p></div><div id="comment-56025-info" class="comment-info"><span class="comment-age">(30 Sep '16, 08:29)</span> sindy</div></div><span id="56030"></span><div id="comment-56030" class="comment not_top_scorer"><div id="post-56030-score" class="comment-score"></div><div class="comment-text"><p>@sindy: I don't think so, since the IP Total Length field is already reduced to only the size of the IP and TCP header (20+20 octets). The remaining Total Length - Header Length (40 - 20) worth of data is passed on the the TCP dissector. As far as the TCP dissector is concerned there is no more data.</p></div><div id="comment-56030-info" class="comment-info"><span class="comment-age">(30 Sep '16, 10:37)</span> Jaap ♦</div></div></div><div id="comment-tools-55986" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-55986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56023"></span>

<div id="answer-container-56023" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56023-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>turns out it is sourcefire mangling the packets. had to tweak the policy to get it to work</p><p>thank you everyone for your input</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '16, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/0b247a9c8e15d271b4d37cedc0876022?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tmkunte&#39;s gravatar image" /><p>tmkunte<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tmkunte has no accepted answers">0%</span></p></div></div><div id="comments-container-56023" class="comments-container"><span id="56029"></span><div id="comment-56029" class="comment"><div id="post-56029-score" class="comment-score"></div><div class="comment-text"><p>I could say I told you so, but I won't.</p></div><div id="comment-56029-info" class="comment-info"><span class="comment-age">(30 Sep '16, 10:18)</span> Jaap ♦</div></div></div><div id="comment-tools-56023" class="comment-tools"></div><div class="clear"></div><div id="comment-56023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

