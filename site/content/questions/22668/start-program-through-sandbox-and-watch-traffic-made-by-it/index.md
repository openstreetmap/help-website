+++
type = "question"
title = "Start program through Sandbox and watch traffic made by it"
description = '''Hi, I would like to check which connections and where to a program did, but I have problems setting Wireshark up. HTTP only connections aren&#x27;t enough, I want to see if it does more than it. I don&#x27;t even know where to see which program did specific traffic in Wireshark so I would really appreciate he...'''
date = "2013-07-04T13:23:00Z"
lastmod = "2013-07-04T13:35:00Z"
weight = 22668
keywords = [ "sandbox", "get", "traffic", "all", "wireshark" ]
aliases = [ "/questions/22668" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Start program through Sandbox and watch traffic made by it](/questions/22668/start-program-through-sandbox-and-watch-traffic-made-by-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22668-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to check which connections and where to a program did, but I have problems setting Wireshark up. HTTP only connections aren't enough, I want to see if it does more than it.</p><p>I don't even know where to see which program did specific traffic in Wireshark so I would really appreciate help. Although I know about Wireshark since months and use it a few times I'm not pro in it.</p><p>Greetings</p></div><div id="question-tags" class="tags-container tags">sandbox get traffic all wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '13, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/a2478c74af8f65b4a2b7bb41a9f325c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Metro2033&#39;s gravatar image" /><p>Metro2033<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Metro2033 has no accepted answers">0%</span></p></div></div><div id="comments-container-22668" class="comments-container"><span id="22676"></span><div id="comment-22676" class="comment"><div id="post-22676-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Start program through Sandbox and watch traffic made by it</p></blockquote><p>if you start the program in a sandbox, why do you need Wireshark? The sandbox tool should tell you all connections opened by the program.</p></div><div id="comment-22676-info" class="comment-info"><span class="comment-age">(04 Jul '13, 14:55)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22668" class="comment-tools"></div><div class="clear"></div><div id="comment-22668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22669"></span>

<div id="answer-container-22669" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22669-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does not have the capability to show which process generated traffic, it can only capture the traffic.</p><p>If you're running on Windows, Network Monitor from MS can show the process involved with the traffic.</p><p>The command line program netstat and the appropriate options for your OS can show which process is using current socket connections.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '13, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22669" class="comments-container"><span id="22670"></span><div id="comment-22670" class="comment"><div id="post-22670-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your fast reply... Well, alright. Can Network Monitor also show the capture traffic of an program "before it even start"? Since the program is genereating the most traffic while starting I'm not fast enough to catch it and then show the traffic.</p></div><div id="comment-22670-info" class="comment-info"><span class="comment-age">(04 Jul '13, 13:40)</span> Metro2033</div></div><span id="22672"></span><div id="comment-22672" class="comment"><div id="post-22672-score" class="comment-score"></div><div class="comment-text"><p>What do you mean "before it even start". Network Monitor (and Wireshark) will capture traffic from the point at which you ask it to start capturing. If this is after a program has started sending traffic, then that traffic won't be captured, only traffic after the start of capture.</p><p>If the program runs at system start-up then you will have to look at capturing off the local machine, e.g. by using the port-mirroring or span option of a switch connected to the target host and another machine running the capture. See the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capturing Setup</a> page on the Wiki for more info.</p></div><div id="comment-22672-info" class="comment-info"><span class="comment-age">(04 Jul '13, 13:46)</span> grahamb ♦</div></div><span id="22673"></span><div id="comment-22673" class="comment"><div id="post-22673-score" class="comment-score"></div><div class="comment-text"><p>Well, since the program connects to whatever it does very fast and right when it start it's hard to make Network Monitor only show traffic made by this programm. Can Network Monitor monitor the network all the time (before the program has been start) and when the program is started capture it, and then I can take a look. Hopefully you understand it now a little bit more hehe. Thanks</p></div><div id="comment-22673-info" class="comment-info"><span class="comment-age">(04 Jul '13, 13:50)</span> Metro2033</div></div><span id="22674"></span><div id="comment-22674" class="comment"><div id="post-22674-score" class="comment-score"></div><div class="comment-text"><p>Not that I know of. You'll have to move to capturing off the target machine as I suggested above. When doing this you won't be able to get process info though.</p></div><div id="comment-22674-info" class="comment-info"><span class="comment-age">(04 Jul '13, 14:08)</span> grahamb ♦</div></div><span id="22675"></span><div id="comment-22675" class="comment"><div id="post-22675-score" class="comment-score"></div><div class="comment-text"><p>Oh, I haven't seen that second part of your message, sorry... Anyway, the program is not running from auto start, but I will read into Ethernet Capturing tomorrow. Do you have any other suggestions I could try tomorrow then? In case this will cause problems / don't work</p></div><div id="comment-22675-info" class="comment-info"><span class="comment-age">(04 Jul '13, 14:16)</span> Metro2033</div></div><span id="22685"></span><div id="comment-22685" class="comment not_top_scorer"><div id="post-22685-score" class="comment-score"></div><div class="comment-text"><p>If the program doesn't auto-start then it sounds as though you should be able to control the start-up to wait for you to get a capturing program running.</p><p>If you still can't achieve that then you'll have to capture off machine using another solution such as I've suggested.</p></div><div id="comment-22685-info" class="comment-info"><span class="comment-age">(05 Jul '13, 01:41)</span> grahamb ♦</div></div></div><div id="comment-tools-22669" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-22669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

