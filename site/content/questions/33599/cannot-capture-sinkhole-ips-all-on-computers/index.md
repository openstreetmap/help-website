+++
type = "question"
title = "Cannot capture sinkhole IP&#x27;s all on computers"
description = '''I have been struggling with getting listed on the CBL for weeks. I finally found this program and received 2 different IPS that I should be looking out for in my capture. They are 38.102.150.27 and 216.66.15.109. I have wireshark running on all the PC in my network and I have the capture filter set ...'''
date = "2014-06-09T18:43:00Z"
lastmod = "2014-06-11T14:09:00Z"
weight = 33599
keywords = [ "ip", "sinkhole" ]
aliases = [ "/questions/33599" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture sinkhole IP's all on computers](/questions/33599/cannot-capture-sinkhole-ips-all-on-computers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33599-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been struggling with getting listed on the CBL for weeks. I finally found this program and received 2 different IPS that I should be looking out for in my capture. They are 38.102.150.27 and 216.66.15.109. I have wireshark running on all the PC in my network and I have the capture filter set up ip.addr==38.102.150.27 and ip.addr==216.66.15.103. I am convinced that something is wrong because I have never seen them come up. The CBL told me to enter one of those IP's into my browser and see if they come up in the capture. They only came up on one of the computers. I would really like to see it on the others even if I try to type into the browser. Please help...</p><p>I have to find the infected computer!!!! Tell me if I am doing something right or wrong.</p><p>Oh I am running Windows 7 Pro.</p></div><div id="question-tags" class="tags-container tags">ip sinkhole</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '14, 18:43</strong></p><img src="https://secure.gravatar.com/avatar/4eefc5bff7e4a86eced83ab729149dd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="astark&#39;s gravatar image" /><p>astark<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="astark has no accepted answers">0%</span></p></div></div><div id="comments-container-33599" class="comments-container"><span id="33673"></span><div id="comment-33673" class="comment"><div id="post-33673-score" class="comment-score"></div><div class="comment-text"><p>Hey I have the same problem. Every morning at 04.00 GMT my server is listed on CBL. The problem in those 2 ip : 38.102.150.27 and 216.66.15.109. but i don't find anything on my system. Did you find a solution?</p></div><div id="comment-33673-info" class="comment-info"><span class="comment-age">(11 Jun '14, 13:30)</span> sanx</div></div><span id="33674"></span><div id="comment-33674" class="comment"><div id="post-33674-score" class="comment-score"></div><div class="comment-text"><p>@sanx: <strong>please don't add an answer</strong> if you have only a comment or a question yourself!</p><p>I converted your answer to a comment of the question.</p><p>Please read the FAQ of this site.</p></div><div id="comment-33674-info" class="comment-info"><span class="comment-age">(11 Jun '14, 13:32)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33599" class="comment-tools"></div><div class="clear"></div><div id="comment-33599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33607"></span>

<div id="answer-container-33607" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33607-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You won't see traffic of other machines, if you run Wireshark on your system, <strong>without</strong> preparing the environment in a special way (hub, TAP, mirror port on the switch, etc.). Please read the Wiki:</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '14, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33607" class="comments-container"></div><div id="comment-tools-33607" class="comment-tools"></div><div class="clear"></div><div id="comment-33607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33676"></span>

<div id="answer-container-33676" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33676-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I did....Wireshark turned up nothing because it was on the computer that hosts my security cameras that I never thought to monitor. Last night I gave it one more shot to watch the log on my router and low and behold I saw the sinkhole IP show up.<br />
</p><p>Other than seeing the sink hole IP there were other symptoms once I logged onto the computer. I try to go to the Malwarebytes site and TDSkiller site and it wouldnt let me. I tried other basic website and I was fine but any security site I went to it wouldnt allow me on. I ended up downloading Malwarebytes from CNET and it found Conficker plus 6 other trojans.<br />
</p><p>LOOK AT EVERY SINGLE COMPUTER ON YOUR NETWORK EVEN THE ONES YOU DONT SUSPECT!!!<br />
</p><p>It was a struggle. Good Luck.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '14, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/4eefc5bff7e4a86eced83ab729149dd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="astark&#39;s gravatar image" /><p>astark<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="astark has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-33676" class="comments-container"></div><div id="comment-tools-33676" class="comment-tools"></div><div class="clear"></div><div id="comment-33676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

