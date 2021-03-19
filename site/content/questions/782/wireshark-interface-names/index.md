+++
type = "question"
title = "Wireshark Interface names"
description = '''I&#x27;m running the latest version of Wireshark on Windows 7 Home Premium 64 bit and 3 of the 5 capture interfaces are called &quot;Microsoft&quot; Where are these names pulled from? Why do they not show the actual card name? Only the LAN port shows correctly as &quot;Realtek RTL8168D&quot; '''
date = "2010-11-02T13:49:00Z"
lastmod = "2011-09-04T18:44:00Z"
weight = 782
keywords = [ "interface", "name" ]
aliases = [ "/questions/782" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Interface names](/questions/782/wireshark-interface-names)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-782-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running the latest version of Wireshark on Windows 7 Home Premium 64 bit and 3 of the 5 capture interfaces are called "Microsoft" Where are these names pulled from? Why do they not show the actual card name? Only the LAN port shows correctly as "Realtek RTL8168D"</p></div><div id="question-tags" class="tags-container tags">interface name</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '10, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/e791c5d284422221797ff07ed3500e9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonh001&#39;s gravatar image" /><p>jonh001<br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonh001 has no accepted answers">0%</span></p></div></div><div id="comments-container-782" class="comments-container"></div><div id="comment-tools-782" class="comment-tools"></div><div class="clear"></div><div id="comment-782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="788"></span>

<div id="answer-container-788" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-788-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess Wireshark pulls the card names from the drivers by asking them what the name of their device is. Obviously the OS often reports "Microsoft" for some of them instead of the vendor designation (at least on Win7), in my case for the WiFi card (it's a Dell card actually) and for another virtual adapter. What I usually do is connect only with one of my cards, check the interface list to see where packets are counting up and then give the card a more specific name in Preferences/Capture/Interfaces/Edit to avoid confusion.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '10, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-788" class="comments-container"><span id="806"></span><div id="comment-806" class="comment"><div id="post-806-score" class="comment-score"></div><div class="comment-text"><p>Awesome. I didn't know you could edit the interface descriptions. I used "ipconfig" and the IPv6 addresses to correctly map and set the descriptions. You just saved me my hair. Thanks.</p></div><div id="comment-806-info" class="comment-info"><span class="comment-age">(03 Nov '10, 19:59)</span> jonh001</div></div><span id="6074"></span><div id="comment-6074" class="comment"><div id="post-6074-score" class="comment-score"></div><div class="comment-text"><p>how did you do that? i see 3 "microsoft" interfaces and a realtek... dont know which one is my wireless interface</p></div><div id="comment-6074-info" class="comment-info"><span class="comment-age">(04 Sep '11, 11:18)</span> Victor Cheng</div></div><span id="6088"></span><div id="comment-6088" class="comment"><div id="post-6088-score" class="comment-score"></div><div class="comment-text"><p>Connect to a Wireless network (which will usually set an IP address), and open the "Capture Interfaces" Dialog. It will tell you the IP next to the adapter. Click on Details to find the Interface ID which you then can use to determine which adapter you need to rename in the Preferences dialog. You can also work with "ipconfig /all" on the command line to find the name and IP/MAC of all cards you have, and match them to the Wireshark list.</p></div><div id="comment-6088-info" class="comment-info"><span class="comment-age">(05 Sep '11, 01:25)</span> Jasper ♦♦</div></div></div><div id="comment-tools-788" class="comment-tools"></div><div class="clear"></div><div id="comment-788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6081"></span>

<div id="answer-container-6081" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6081-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark Capture Interfaces window shows the IP addresses of the interfaces - that should tell you which interface is which when referenced against the output of an "ipconfig /all" or "ifconfig". Then you can change the Wireshark interface name in Preferences/Capture/Interfaces/Edit.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '11, 18:44</strong></p><img src="https://secure.gravatar.com/avatar/e791c5d284422221797ff07ed3500e9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonh001&#39;s gravatar image" /><p>jonh001<br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonh001 has no accepted answers">0%</span></p></div></div><div id="comments-container-6081" class="comments-container"></div><div id="comment-tools-6081" class="comment-tools"></div><div class="clear"></div><div id="comment-6081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

