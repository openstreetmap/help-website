+++
type = "question"
title = "How do you capture internet connects and disconnects?"
description = '''I am a subscriber to Frontier DSL Internet service (only because of rural location) My internet connection is not totally reliable. There are sporadic disconnections and then reconnections, all at various times of the day and evening.  Frontier claims that all their tests so far show the elements of...'''
date = "2015-04-22T18:05:00Z"
lastmod = "2015-04-22T23:20:00Z"
weight = 41710
keywords = [ "internet" ]
aliases = [ "/questions/41710" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do you capture internet connects and disconnects?](/questions/41710/how-do-you-capture-internet-connects-and-disconnects)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41710-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a subscriber to Frontier DSL Internet service (only because of rural location) My internet connection is not totally reliable. There are sporadic disconnections and then reconnections, all at various times of the day and evening. Frontier claims that all their tests so far show the elements of connections are nominal. I claim they're not.</p><p>A technician is coming tomorrow to do an inside-the-house service call. I would like to be able to demonstrate the disconnections.</p><p>I downloaded WireShark hoping that it could generate a simple report of the disconnections and reconnections. I don't need a lot of data and detail, but the connectivity issue is something we are going to have an argument or several about. Is that possible with WireShark?</p><p>It is a fantastic piece of software, and brilliantly conceived and executed, but way above my head. Would appreciate some thoughtful hand-holding. Thank you</p></div><div id="question-tags" class="tags-container tags">internet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '15, 18:05</strong></p><img src="https://secure.gravatar.com/avatar/1de3f6892886d2f904e958ca14ea7156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="garryuws&#39;s gravatar image" /><p>garryuws<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="garryuws has no accepted answers">0%</span></p></div></div><div id="comments-container-41710" class="comments-container"></div><div id="comment-tools-41710" class="comment-tools"></div><div class="clear"></div><div id="comment-41710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41715"></span>

<div id="answer-container-41715" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41715-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several remarks that can be made here.</p><p>1) Capture interface</p><p>Wireshark can capture from various types on interfaces (Ethernet, USB, BT), but (without special hardware) not from DSL. So any physical layer or data link layer problems on the DSL can't be captured directly.</p><p>2) Modem</p><p>Your modem may provide valuable sources of information (something the tech will look at I guess) in internal logs. Depending on the type and configuration of the modem this may be accessible. Also the modem may provide a DSL capture interface which can be used to create capture files, which you can read with Wireshark.</p><p>Note: this very much depends on the type of modem. Many do not provide these features.</p><p>3) Test</p><p>You can test your link by having a continues ping running to a known external host. If your link goes down your ping replies stop coming in. This you can capture with Wireshark as well (although it doesn't point to any cause).</p><p>4) Timing</p><p>With the tech coming in you are already late to show a pattern, which should be taken on longer interval (days/weeks). Depending on the frequency of the occurrences it may be enough.</p><p>Good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41715" class="comments-container"><span id="41748"></span><div id="comment-41748" class="comment"><div id="post-41748-score" class="comment-score"></div><div class="comment-text"><p>Japp Many thanks for taking the time to share your expertise, excellent information and very helpful responses.</p><p>Your #3 is the best and most practical in this situation, given my relative inexperience.</p><p>Soooooooo..... If I may knock on your door for a little bit additional help......... How do I get Wireshark to generate pings? How do I filter out everything except the PING data from the report? Would greatly appreciate your assistance. Many thanks</p><p>/gh</p></div><div id="comment-41748-info" class="comment-info"><span class="comment-age">(23 Apr '15, 14:08)</span> garryuws</div></div><span id="41749"></span><div id="comment-41749" class="comment"><div id="post-41749-score" class="comment-score"></div><div class="comment-text"><p>Jaap, I meant. sorry for the typo.</p></div><div id="comment-41749-info" class="comment-info"><span class="comment-age">(23 Apr '15, 14:09)</span> garryuws</div></div><span id="41751"></span><div id="comment-41751" class="comment"><div id="post-41751-score" class="comment-score">1</div><div class="comment-text"><p>Wireshark doesn't generate pings, or any other network test traffic, it's a packet analyzer.</p><p>You can ping from the command prompt, or there are any number of fancy GUI tools that can do the same. Google will help here.</p></div><div id="comment-41751-info" class="comment-info"><span class="comment-age">(23 Apr '15, 14:19)</span> grahamb ♦</div></div></div><div id="comment-tools-41715" class="comment-tools"></div><div class="clear"></div><div id="comment-41715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

