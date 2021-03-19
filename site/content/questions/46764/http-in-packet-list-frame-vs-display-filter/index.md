+++
type = "question"
title = "&quot;HTTP&quot; in packet list frame vs. display filter"
description = '''I start Wireshark, then browse to a couple of websites, and voila, HTTP packets start showing up in the packet list frame. Then I stop the capture (or not), and type &quot;http&quot; in the display filter, and nothing passes the filter. However, &quot;tcp port 80&quot; does give me the packets labeled HTTP (along with ...'''
date = "2015-10-20T09:41:00Z"
lastmod = "2015-10-20T11:47:00Z"
weight = 46764
keywords = [ "novice", "newbie", "filters", "beginner" ]
aliases = [ "/questions/46764" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# ["HTTP" in packet list frame vs. display filter](/questions/46764/http-in-packet-list-frame-vs-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46764-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I start Wireshark, then browse to a couple of websites, and voila, HTTP packets start showing up in the packet list frame. Then I stop the capture (or not), and type "http" in the display filter, and nothing passes the filter. However, "tcp port 80" does give me the packets labeled HTTP (along with a bunch of other stuff). 1. What am I misunderstanding about how display filters work? 2. How can I filter to get just HTTP packets, and not other packets involving "tcp port 80"?</p></div><div id="question-tags" class="tags-container tags">novice newbie filters beginner</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '15, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/198f589fcb8e7cac734f9ea48a074977?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vparunak&#39;s gravatar image" /><p>vparunak<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vparunak has no accepted answers">0%</span></p></div></div><div id="comments-container-46764" class="comments-container"><span id="46767"></span><div id="comment-46767" class="comment"><div id="post-46767-score" class="comment-score">1</div><div class="comment-text"><p>It works on my system, so:</p><ul><li>what is your OS and OS version</li><li>what is your Wireshark version</li><li>What's the color of the display filter field after you type <strong>http</strong></li></ul></div><div id="comment-46767-info" class="comment-info"><span class="comment-age">(20 Oct '15, 10:15)</span> Kurt Knochner ♦</div></div><span id="46768"></span><div id="comment-46768" class="comment"><div id="post-46768-score" class="comment-score"></div><div class="comment-text"><p>OS: Mac OSX Yosemite 10.10.5 WS: 2.0.0rc1 (I know it's development, but Yosemite doesn't have Quartz to run 1.12.x) Color: green</p><p>Thanks for your help!</p></div><div id="comment-46768-info" class="comment-info"><span class="comment-age">(20 Oct '15, 10:18)</span> vparunak</div></div><span id="46773"></span><div id="comment-46773" class="comment"><div id="post-46773-score" class="comment-score"></div><div class="comment-text"><p>I can try it this evening. 2.0.0rc1 on Mac, if you want.</p></div><div id="comment-46773-info" class="comment-info"><span class="comment-age">(20 Oct '15, 10:45)</span> Christian_R</div></div></div><div id="comment-tools-46764" class="comment-tools"></div><div class="clear"></div><div id="comment-46764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46770"></span>

<div id="answer-container-46770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46770-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Same here on Windows 7 with 2.0.0rc1. I'd say it's a bug.</p><p>Please try one of the lastest automatic builds</p><blockquote><p><a href="https://www.wireshark.org/download/automated/">https://www.wireshark.org/download/automated/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '15, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Oct '15, 10:28</p></div></div><div id="comments-container-46770" class="comments-container"><span id="46771"></span><div id="comment-46771" class="comment"><div id="post-46771-score" class="comment-score"></div><div class="comment-text"><p>So: if I do the dance needed to install 1.12, it should work OK?</p></div><div id="comment-46771-info" class="comment-info"><span class="comment-age">(20 Oct '15, 10:35)</span> vparunak</div></div><span id="46772"></span><div id="comment-46772" class="comment"><div id="post-46772-score" class="comment-score">1</div><div class="comment-text"><p>It works on my system, and I've never heard of such problems with the current stable releae. That's all I can say. So, in general this would translate to: yes.</p></div><div id="comment-46772-info" class="comment-info"><span class="comment-age">(20 Oct '15, 10:38)</span> Kurt Knochner ♦</div></div><span id="46777"></span><div id="comment-46777" class="comment"><div id="post-46777-score" class="comment-score"></div><div class="comment-text"><p>I tried 2.1, and that seems to work fine. Thanks for the excellent help.</p></div><div id="comment-46777-info" class="comment-info"><span class="comment-age">(20 Oct '15, 12:25)</span> vparunak</div></div><span id="46778"></span><div id="comment-46778" class="comment"><div id="post-46778-score" class="comment-score"></div><div class="comment-text"><p>good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-46778-info" class="comment-info"><span class="comment-age">(20 Oct '15, 12:26)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46770" class="comment-tools"></div><div class="clear"></div><div id="comment-46770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46775"></span>

<div id="answer-container-46775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46775-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The display filter "http" will only match packets that have data in them. Wireshark treats all higher-level (above TCP) protocols this way. If it runs over port 80 and has data in it, it's an HTTP packet. If the packet does not have any data in it, then it doesn't matter that it runs over port 80. Wireshark identifies it as simply TCP. So the display filter "http" will not show empty packets: TCP connection establishment, acknowledgments, connection termination. If you want to see all packets in a web browsing session, then "tcp.port==80" (or whatever port was used) is a better display filter.</p><p>But besides that, beginning with version 1.12.0, Wireshark does not always correctly identify HTTP packets. This is a known bug: See the answer to <a href="https://ask.wireshark.org/questions/35767/packets-marked-as-http-on-1109-are-marked-as-tcp-on-1120">this question</a>.</p><p>Edit: Having now tried this in 2.0.0rc1, I see that this is new behavior which seems to be a different bug from the one I described.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '15, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Mar '16, 22:00</p></div></div><div id="comments-container-46775" class="comments-container"><span id="46776"></span><div id="comment-46776" class="comment"><div id="post-46776-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that gives me some context.</p></div><div id="comment-46776-info" class="comment-info"><span class="comment-age">(20 Oct '15, 12:23)</span> vparunak</div></div><span id="46779"></span><div id="comment-46779" class="comment"><div id="post-46779-score" class="comment-score"></div><div class="comment-text"><p>Well my try has looked like the described bug. But I am not 100% sure, because I can´t reproduce it.</p></div><div id="comment-46779-info" class="comment-info"><span class="comment-age">(20 Oct '15, 12:32)</span> Christian_R</div></div></div><div id="comment-tools-46775" class="comment-tools"></div><div class="clear"></div><div id="comment-46775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

