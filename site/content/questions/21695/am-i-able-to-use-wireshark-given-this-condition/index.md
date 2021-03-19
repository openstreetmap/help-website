+++
type = "question"
title = "Am I able to use Wireshark given this condition?"
description = '''Hi guys, I am currently living in a hostel and connect to the internet via the hostel&#x27;s centralized router. I am trying out a software and wish to find out whether it calls home, that is, capture data packets from my OS and send them to the software vendor. Can I use Wireshark to see whether the sof...'''
date = "2013-06-02T18:32:00Z"
lastmod = "2013-06-02T19:25:00Z"
weight = 21695
keywords = [ "home", "call", "packet", "data" ]
aliases = [ "/questions/21695" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Am I able to use Wireshark given this condition?](/questions/21695/am-i-able-to-use-wireshark-given-this-condition)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21695-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I am currently living in a hostel and connect to the internet via the hostel's centralized router.</p><p>I am trying out a software and wish to find out whether it calls home, that is, capture data packets from my OS and send them to the software vendor.</p><p>Can I use Wireshark to see whether the software in question send data packets back to the software vendor?</p><p>Can Wireshark reveal the contents of the data packets?</p><p>My OS is Microsoft Windows 7, 64-bit.</p></div><div id="question-tags" class="tags-container tags">home call packet data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '13, 18:32</strong></p><img src="https://secure.gravatar.com/avatar/7fd27e9287d3f55f9e01c8f69f9024fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newuser&#39;s gravatar image" /><p>newuser<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newuser has no accepted answers">0%</span></p></div></div><div id="comments-container-21695" class="comments-container"></div><div id="comment-tools-21695" class="comment-tools"></div><div class="clear"></div><div id="comment-21695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21696"></span>

<div id="answer-container-21696" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21696-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can capture all the packets coming or going from your computer's interface toward the Internet, so the short answer is yes it can get the traffic.</p><p>However, if you don't know anything about the traffic that could be being used to 'phone home', you may find it difficult to tell the normal traffic in your packet captures from the traffic that is phoning home, if it exists at all.</p><p>Wireshark can reveal/decode the contents of data packets, yes. If the application can't be decoded for any reason you will at a minimum see the binary data being sent across the wire. Note that doesn't mean the traffic isn't encrypted, but you can for sure get visibility to the bits leaving the wire.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '13, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21696" class="comments-container"><span id="21697"></span><div id="comment-21697" class="comment"><div id="post-21697-score" class="comment-score"></div><div class="comment-text"><p>Thanks for taking the time to answer my question.</p><p>So how to I go about to using Wireshark?</p><p>Do I have to use a second computer to monitor the computer on which the software that I am analyzing? In other words, how do I set up Wireshark?</p></div><div id="comment-21697-info" class="comment-info"><span class="comment-age">(02 Jun '13, 19:42)</span> newuser</div></div><span id="21698"></span><div id="comment-21698" class="comment"><div id="post-21698-score" class="comment-score"></div><div class="comment-text"><p>You can download Wireshark's installer from the download page here for your OS. Also yes, you can install it directly on the system you're trying to capture traffic from and should not need a second computer: <a href="http://www.wireshark.org/download.html">http://www.wireshark.org/download.html</a></p><p>As for how to use Wireshark, that's a bit of a loaded question but I suggest starting with the manual. Since you're really just trying to do a straightforward capture of packets on an interface, I suggest starting with Chapter 4 (Capturing Live Network Data) and asking questions here that come up: <a href="http://www.wireshark.org/docs/wsug_html_chunked/">http://www.wireshark.org/docs/wsug_html_chunked/</a></p></div><div id="comment-21698-info" class="comment-info"><span class="comment-age">(02 Jun '13, 21:07)</span> Quadratic</div></div></div><div id="comment-tools-21696" class="comment-tools"></div><div class="clear"></div><div id="comment-21696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

