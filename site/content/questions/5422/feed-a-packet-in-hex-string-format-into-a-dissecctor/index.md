+++
type = "question"
title = "feed a packet in hex string format into a dissecctor"
description = '''Hi all,  I have a packet in hex string format, how do i create the three data format required (tvb, pinfo and tree) in order to pass it to a dissector? I have come across this mail and thought of using the function tvb_new_real_data but i have no idea how to use it. Any help and guidance is apprecia...'''
date = "2011-08-03T03:12:00Z"
lastmod = "2011-08-04T09:42:00Z"
weight = 5422
keywords = [ "development" ]
aliases = [ "/questions/5422" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [feed a packet in hex string format into a dissecctor](/questions/5422/feed-a-packet-in-hex-string-format-into-a-dissecctor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5422-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I have a packet in hex string format, how do i create the three data format required (tvb, pinfo and tree) in order to pass it to a dissector? I have come across <a href="http://ethereal.archive.sunet.se/lists/ethereal-dev/200103/msg00306.html">this mail</a> and thought of using the function <code>tvb_new_real_data</code> but i have no idea how to use it.</p><p>Any help and guidance is appreciated.</p><p>Thank you</p><p>Regards, Eddie Choo</p></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '11, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/c1dac05d0e75992546b5da006c6b718e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eddie%20choo&#39;s gravatar image" /><p>eddie choo<br />
<span class="score" title="66 reputation points">66</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eddie choo has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Aug '11, 16:15</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5422" class="comments-container"><span id="5460"></span><div id="comment-5460" class="comment"><div id="post-5460-score" class="comment-score">1</div><div class="comment-text"><p>Can you clarify? What do you mean by "you have a packet in hex string format? Can you supply an example packet/file/whatever?</p></div><div id="comment-5460-info" class="comment-info"><span class="comment-age">(03 Aug '11, 17:02)</span> cmaynard ♦♦</div></div><span id="5474"></span><div id="comment-5474" class="comment"><div id="post-5474-score" class="comment-score"></div><div class="comment-text"><p><code>03b1682daa0980030e160b129500120426180610030208120600120456497341623f4 804ba1411b66b1e281c060700118605010101a011600f80020780a1090607040000010 002036c17a115020100020103a30d040825054373236300f50a0100</code> Here you go</p></div><div id="comment-5474-info" class="comment-info"><span class="comment-age">(03 Aug '11, 19:07)</span> eddie choo</div></div><span id="5475"></span><div id="comment-5475" class="comment"><div id="post-5475-score" class="comment-score">1</div><div class="comment-text"><p>Where does this data come from - a .pcap file, a text file, or somewhere else?</p></div><div id="comment-5475-info" class="comment-info"><span class="comment-age">(03 Aug '11, 19:26)</span> cmaynard ♦♦</div></div><span id="5477"></span><div id="comment-5477" class="comment"><div id="post-5477-score" class="comment-score"></div><div class="comment-text"><p>I got this raw hex string from other sources, and i need to feed it directly into the dissector.</p></div><div id="comment-5477-info" class="comment-info"><span class="comment-age">(03 Aug '11, 19:49)</span> eddie choo</div></div></div><div id="comment-tools-5422" class="comment-tools"></div><div class="clear"></div><div id="comment-5422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5504"></span>

<div id="answer-container-5504" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5504-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>How is your dissector called? I.e., is it called from TCP, UDP, its own data link type, or some other method? If you can convert the hex string to a format <code>text2pcap</code> understands you could use it to create a libpcap capture file which could then be used by your dissector. For example, if you then use <code>text2pcap -l user0</code> to convert the hex data to a pcap file, you can use <em>Edit→Preferences→Protocols→DLT_USER</em> to associate DLT 147 (user0) with your dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '11, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-5504" class="comments-container"><span id="5517"></span><div id="comment-5517" class="comment"><div id="post-5517-score" class="comment-score"></div><div class="comment-text"><p>Hi Gerald, basically my task is to design a program which filters massive real time packets with high speed. So i thought of minimizing the dissectors, by modifying them to suit my needs. My input will be hex string and i dont need the whole dissector to dissect my packet as the criteria of my filters are only limited to 1 information field. My temporary solution is to modify the <code>tvb_get_uintX()</code> function to suit my needs. Thanks for your reply</p><p>Eddie Choo</p></div><div id="comment-5517-info" class="comment-info"><span class="comment-age">(04 Aug '11, 19:25)</span> eddie choo</div></div></div><div id="comment-tools-5504" class="comment-tools"></div><div class="clear"></div><div id="comment-5504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

