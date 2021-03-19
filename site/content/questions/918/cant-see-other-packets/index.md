+++
type = "question"
title = "Can&#x27;t see other packets"
description = '''Hi All! I have problems with wireshark I can&#x27;t see packets from other users, I see only packets from myself. I searched the help file and found a &quot;solution&quot; it&#x27;s explained in question 7.1, my problem is I don&#x27;t understand that answer. Can someone else explain it in a different way for me? I am using...'''
date = "2010-11-11T13:12:00Z"
lastmod = "2010-11-11T16:50:00Z"
weight = 918
keywords = [ "not", "from", "packets", "others" ]
aliases = [ "/questions/918" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't see other packets](/questions/918/cant-see-other-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-918-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All!</p><p>I have problems with wireshark I can't see packets from other users, I see only packets from myself.</p><p>I searched the help file and found a "solution" it's explained in question 7.1, my problem is I don't understand that answer.</p><p>Can someone else explain it in a different way for me?</p><p>I am using a wireless adapter on a router.</p><p>Thanks in advance,</p><p>Greetings,</p><p>Marco</p></div><div id="question-tags" class="tags-container tags">not from packets others</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '10, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/92a530c5dfdaefb015d0e3d31de1e8b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolfshape&#39;s gravatar image" /><p>wolfshape<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolfshape has no accepted answers">0%</span></p></div></div><div id="comments-container-918" class="comments-container"></div><div id="comment-tools-918" class="comment-tools"></div><div class="clear"></div><div id="comment-918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="920"></span>

<div id="answer-container-920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-920-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Marco...</p><p>Ok... assuming you are doing a WLAN capture, you need to run Wireshark (or Tshark if desired) on a host that has an adapter that will go into promiscuous mode and monitor mode (so you can see traffic on other WLANs). We have a video on testing your adapter over at www.wiresharkbook.com/coffee. Notice that one WLAN adapter cannot run in promiscuous mode (hence I won't see any traffic but my own).</p><p>Can you provide a bit more detail on your capture setup? "using a wireless adapter on a router?"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '10, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-920" class="comments-container"><span id="934"></span><div id="comment-934" class="comment"><div id="post-934-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer, your assumings are right. I am connected via a WLAN on a router I am trying to monitor another PC on my network which is connected to the same router via a cable.</p><p>I started my adapter in promiscuous mode and wireshark didn't complained (as explained in your video).</p><p>Still I can't see other traffic except for my own.</p><p>I hope you can give me some hints!</p><p>Greetings and thanks in advance,</p><p>Marco</p></div><div id="comment-934-info" class="comment-info"><span class="comment-age">(12 Nov '10, 13:53)</span> wolfshape</div></div><span id="935"></span><div id="comment-935" class="comment"><div id="post-935-score" class="comment-score"></div><div class="comment-text"><p>Sounds like you are capturing on a WLAN interface, but the other host is connected via cable to the router (directly - not through a switch?). You'll need to tap in somewhere on the wired network to capture their traffic on that wired network. If, however, their traffic eventually crosses the WLAN environment, you may need to get another adapter to allow you to see their traffic - on a Windows host I use an AirPcap adapter.</p><p>See http://wiki.wireshark.org/CaptureSetup/WLAN for more information on WLAN capture.</p></div><div id="comment-935-info" class="comment-info"><span class="comment-age">(12 Nov '10, 14:35)</span> lchappell ♦</div></div></div><div id="comment-tools-920" class="comment-tools"></div><div class="clear"></div><div id="comment-920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

