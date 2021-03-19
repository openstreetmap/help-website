+++
type = "question"
title = "Facebook chat messages and other messengers"
description = '''Does anyone know how to capture facebook chat or where / how to look at messages sent and received, along with other messenger messages and email. I am using ARP poisoning to capture traffic to a machine from the suspect device and router, and then wireshark to capture all the traffic which appears ...'''
date = "2015-02-28T14:18:00Z"
lastmod = "2015-02-28T14:30:00Z"
weight = 40153
keywords = [ "messenger", "facebook" ]
aliases = [ "/questions/40153" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Facebook chat messages and other messengers](/questions/40153/facebook-chat-messages-and-other-messengers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40153-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone know how to capture facebook chat or where / how to look at messages sent and received, along with other messenger messages and email.</p><p>I am using ARP poisoning to capture traffic to a machine from the suspect device and router, and then wireshark to capture all the traffic which appears to be working. just now need to know which packets to look at and how to read the messages.</p></div><div id="question-tags" class="tags-container tags">messenger facebook</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '15, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/77bfc991bcd6da6286a697fc122ba2cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="new2geeky&#39;s gravatar image" /><p>new2geeky<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="new2geeky has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '15, 14:39</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-40153" class="comments-container"></div><div id="comment-tools-40153" class="comment-tools"></div><div class="clear"></div><div id="comment-40153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40154"></span>

<div id="answer-container-40154" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40154-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all I hope you're not doing anything illegal here - ARP cache poisoning is a network attack unless you use it for your own traffic, or in a network where you're allowed to do it (test/lab environments).</p><p>Second, you're not going to be able to read the packets, because Facebook and all other messengers use SSL layer encryption by default. So without the private encryption keys (either Facebooks, which you're not going to get, or the one on the local machine, which you may have access to) you're not going to see clear text, no matter what you do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '15, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40154" class="comments-container"><span id="40155"></span><div id="comment-40155" class="comment"><div id="post-40155-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper and thanks for the reply. Not doing anything illegal as it is traffic on my private LAN (house) which i pay for the internet connection to!</p><p>The problem i have is that i think one of my children is getting themselves into something they really should not be. So that i know one way or the other i need to stealthily look at what is going on and if my fears are correct i can deal with that as stealthily!</p><p>They are using an android phone which i have no access to, any help greatly appreciated.</p></div><div id="comment-40155-info" class="comment-info"><span class="comment-age">(28 Feb '15, 15:57)</span> new2geeky</div></div><span id="40157"></span><div id="comment-40157" class="comment"><div id="post-40157-score" class="comment-score"></div><div class="comment-text"><p>Okay, in that case you're out of luck. You might be able to force them through a proxy like Fiddler, but they WILL notice (if you do man-in-the-middle via Fiddler the SSL certificate will show a big red warning to them).</p><p>Also, you'd have to force their phones to go through the proxy, which is hard to do without their help. So I'm sorry to say that there is no stealthy way of doing this.</p></div><div id="comment-40157-info" class="comment-info"><span class="comment-age">(28 Feb '15, 16:29)</span> Jasper ♦♦</div></div><span id="40224"></span><div id="comment-40224" class="comment"><div id="post-40224-score" class="comment-score"></div><div class="comment-text"><blockquote><p>They are using an android phone which <strong>i have no access to</strong>, any help greatly appreciated.</p></blockquote><p>wait a moment. You are willing and able to do ARP spoofing and capturing traffic of the device!</p><p>So, what stops you from rooting the mobile phone and installing some <del>spy software</del> parental control tools?</p></div><div id="comment-40224-info" class="comment-info"><span class="comment-age">(03 Mar '15, 10:15)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-40154" class="comment-tools"></div><div class="clear"></div><div id="comment-40154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

