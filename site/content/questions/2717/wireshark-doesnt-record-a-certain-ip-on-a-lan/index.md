+++
type = "question"
title = "Wireshark doesnt record a certain IP on a lan."
description = '''Hello, I have a critical issue with wireshark. I need to record my traffic on a lan, of one of my machine&#x27;s ip. But when filtering on that IP and Port, i get nothing. (all the other traffic on lan i see perfect). This is critical for us to record this traffic,  We have tried many workarounds such as...'''
date = "2011-03-08T19:16:00Z"
lastmod = "2011-03-09T02:06:00Z"
weight = 2717
keywords = [ "wireshark" ]
aliases = [ "/questions/2717" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesnt record a certain IP on a lan.](/questions/2717/wireshark-doesnt-record-a-certain-ip-on-a-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a critical issue with wireshark. I need to record my traffic on a lan, of one of my machine's ip. But when filtering on that IP and Port, i get nothing. (all the other traffic on lan i see perfect).</p><p>This is critical for us to record this traffic, We have tried many workarounds such as switching between nic's and so on.</p><p>Can you please Help?</p><p>Thank you very much Lior.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '11, 19:16</strong></p><img src="https://secure.gravatar.com/avatar/d9f1b7d0186b6fdad348075c4acab143?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="liorbnz&#39;s gravatar image" /><p>liorbnz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="liorbnz has no accepted answers">0%</span></p></div></div><div id="comments-container-2717" class="comments-container"></div><div id="comment-tools-2717" class="comment-tools"></div><div class="clear"></div><div id="comment-2717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2720"></span>

<div id="answer-container-2720" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2720-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can distinguish between a faulty capture setup and a filtering problem by checking whether capturing without a filter is showing (unicast) packets for the IP you are trying to monitor. If it does, your capture setup is OK and you should focus on the filtering. If it does not, you need to focus on how to capture the packets.</p><p>How are the systems connected? In particular, how are the machine you are trying to monitor and the capturing PC connected? Are you using span ports? HUB's? TAP's? to get the traffic to your capturing PC? Please have a look at <a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a> to see whether the capture setup you are using could be faulty for this job?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '11, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2720" class="comments-container"></div><div id="comment-tools-2720" class="comment-tools"></div><div class="clear"></div><div id="comment-2720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

