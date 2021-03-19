+++
type = "question"
title = "Wireshark only works one time"
description = '''Hello,  Let me explain what&#x27;s going on with my wireshark installation. I am using wireshark to sniff EtherCAT packets, and everything works perfectly the first time I run wireshark. After I press the stop button and try to restart the sniffing process, wireshark simpy freezes and I am forced to clos...'''
date = "2014-09-19T08:03:00Z"
lastmod = "2014-09-30T09:41:00Z"
weight = 36455
keywords = [ "wireshark" ]
aliases = [ "/questions/36455" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark only works one time](/questions/36455/wireshark-only-works-one-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36455-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Let me explain what's going on with my wireshark installation. I am using wireshark to sniff EtherCAT packets, and everything works perfectly the first time I run wireshark. After I press the stop button and try to restart the sniffing process, wireshark simpy freezes and I am forced to close it and restart it to get it to work again.</p><p>It works, as you can see, but it's really anoying to restart it after every sniff.</p><p>Has anyone else ever had to deal with this problem?</p><p><strong>EDIT:</strong> OS: Windows 7 Wireshark v1.12.1</p><p><strong>EDIT2:</strong> <del>@grahamb Yes it stops. For some reason I can't write comments now, it sends me this message: "Sorry, but akismet thinks your comment is spam"</del></p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '14, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/363b1bb1c9cd90a0ae14ace401289dbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morcillo&#39;s gravatar image" /><p>morcillo<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morcillo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Sep '14, 09:41</p></div></div><div id="comments-container-36455" class="comments-container"><span id="36457"></span><div id="comment-36457" class="comment"><div id="post-36457-score" class="comment-score"></div><div class="comment-text"><p>Wireshark and OS versions?</p></div><div id="comment-36457-info" class="comment-info"><span class="comment-age">(19 Sep '14, 08:11)</span> grahamb ♦</div></div><span id="36459"></span><div id="comment-36459" class="comment"><div id="post-36459-score" class="comment-score"></div><div class="comment-text"><p>Can you check, using task manager, that when you stop the capture, the capture process dumpcap.exe stops?</p></div><div id="comment-36459-info" class="comment-info"><span class="comment-age">(19 Sep '14, 08:30)</span> grahamb ♦</div></div><span id="36480"></span><div id="comment-36480" class="comment"><div id="post-36480-score" class="comment-score"></div><div class="comment-text"><p>@grahamb Yes, it stops</p></div><div id="comment-36480-info" class="comment-info"><span class="comment-age">(20 Sep '14, 09:35)</span> morcillo</div></div><span id="36481"></span><div id="comment-36481" class="comment"><div id="post-36481-score" class="comment-score"></div><div class="comment-text"><p>@grahamb Sorry it took such a long time to answer in the comments, but yesterday it said that I was not allowed to post comments. Something about my comment being spam</p></div><div id="comment-36481-info" class="comment-info"><span class="comment-age">(20 Sep '14, 09:38)</span> morcillo</div></div><span id="36715"></span><div id="comment-36715" class="comment"><div id="post-36715-score" class="comment-score"></div><div class="comment-text"><p>@grahamb Hello? Sorry to call you this way, but it's getting really hard to use wireshark as it is now</p></div><div id="comment-36715-info" class="comment-info"><span class="comment-age">(29 Sep '14, 17:29)</span> morcillo</div></div><span id="36720"></span><div id="comment-36720" class="comment not_top_scorer"><div id="post-36720-score" class="comment-score"></div><div class="comment-text"><p>Do you have any AV or endpoint protection, or VPN software installed on the machine? These have been known to interfere with Wireshark operation, but usually by just hiding some traffic.</p></div><div id="comment-36720-info" class="comment-info"><span class="comment-age">(30 Sep '14, 02:12)</span> grahamb ♦</div></div><span id="36723"></span><div id="comment-36723" class="comment not_top_scorer"><div id="post-36723-score" class="comment-score"></div><div class="comment-text"><p>@grahamb No. Nothing like that. But I am using a ethernet to usb converter in order to sniff the packets. That's the only possible interface tha I have at the time. Could that be the problem?</p></div><div id="comment-36723-info" class="comment-info"><span class="comment-age">(30 Sep '14, 07:26)</span> morcillo</div></div><span id="36725"></span><div id="comment-36725" class="comment not_top_scorer"><div id="post-36725-score" class="comment-score"></div><div class="comment-text"><p>@morcillo,</p><p>Just to confirm, the first run works, and allows you to stop the capture, but starting another capture (with which button or command?) causes Wireshark to hang?</p></div><div id="comment-36725-info" class="comment-info"><span class="comment-age">(30 Sep '14, 08:03)</span> grahamb ♦</div></div><span id="36726"></span><div id="comment-36726" class="comment not_top_scorer"><div id="post-36726-score" class="comment-score"></div><div class="comment-text"><p>@grahamb Exactly. I run it the first time, the I press the stop button (big red square button). After that I can analyze all the packets. Everything is perfect until I try to restart wireshark. When I do that it hangs.</p></div><div id="comment-36726-info" class="comment-info"><span class="comment-age">(30 Sep '14, 08:12)</span> morcillo</div></div></div><div id="comment-tools-36455" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-36455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36730"></span>

<div id="answer-container-36730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36730-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have looked into a very similar issue (on Win 8 tho) before as the OP was able to provide me with process dumps, but all I could determine was that Wireshark was stuck in a call into WinPCap which is another project entirely.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '14, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36730" class="comments-container"><span id="36735"></span><div id="comment-36735" class="comment"><div id="post-36735-score" class="comment-score"></div><div class="comment-text"><p>@grahamb Thank you for that tip. I had already tried installing and uninstalling wireshark, but without uninstalling WinPCap. Thanks to this comment I removed it completely and installed everything again. Now it works. Would you like to post it as an answer? That wai I'll be able to thank you properly.</p></div><div id="comment-36735-info" class="comment-info"><span class="comment-age">(30 Sep '14, 14:26)</span> morcillo</div></div></div><div id="comment-tools-36730" class="comment-tools"></div><div class="clear"></div><div id="comment-36730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

