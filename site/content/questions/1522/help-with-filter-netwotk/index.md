+++
type = "question"
title = "help with filter netwotk!!!"
description = '''I&#x27;m just see this app from today i&#x27;m like its i&#x27;m test to capture,its ok but i can&#x27;t fill IP target (like my PC IP 192.168.1.1)and target IP is 192.168.1.2 so i&#x27;m want capture on IP 192.168.1.2 how to do? i can&#x27;t see about do on its!!! help pls'''
date = "2010-12-29T23:53:00Z"
lastmod = "2010-12-30T00:23:00Z"
weight = 1522
keywords = [ "com", "for", "here", "learn" ]
aliases = [ "/questions/1522" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [help with filter netwotk!!!](/questions/1522/help-with-filter-netwotk)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1522-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm just see this app from today i'm like its i'm test to capture,its ok but i can't fill IP target (like my PC IP 192.168.1.1)and target IP is 192.168.1.2 so i'm want capture on IP 192.168.1.2 how to do? i can't see about do on its!!! help pls</p></div><div id="question-tags" class="tags-container tags">com for here learn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '10, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/94ec80f83d68112295a513ba0c8db187?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morokat&#39;s gravatar image" /><p>morokat<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morokat has no accepted answers">0%</span></p></div></div><div id="comments-container-1522" class="comments-container"><span id="1538"></span><div id="comment-1538" class="comment"><div id="post-1538-score" class="comment-score"></div><div class="comment-text"><p>Morokat, Please answer the following questions so people can help you. 1) Are you using a switch? 2) What is the name/model of the switch? 3) Which PC (192.168.1.1 or 1.2) has Wireshark installed?</p><p>In general, on a switch, you have to redirect the packets of 1.2 host to your PC running wireshark (1.1). The way to do it depends on the model/brand of your switch.</p></div><div id="comment-1538-info" class="comment-info"><span class="comment-age">(30 Dec '10, 07:23)</span> hansangb</div></div></div><div id="comment-tools-1522" class="comment-tools"></div><div class="clear"></div><div id="comment-1522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="1523"></span>

<div id="answer-container-1523" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1523-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't use Wireshark to capture <em>on</em> another target PC. However if the capture interface you are using can see traffic heading to and from that target PC then you can a. capture that traffic and b. filter it.</p><p>In the capture filter, you need a filter "host 192.168.1.2"</p><p>In the display filter (which filters traffic after it has been captured) you can just set "ip.addr eq 192.168.1.2"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '10, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1523" class="comments-container"></div><div id="comment-tools-1523" class="comment-tools"></div><div class="clear"></div><div id="comment-1523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1524"></span>

<div id="answer-container-1524" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1524-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><img src="http://img607.imageshack.us/img607/2006/erere.jpg" alt="alt text" /></p><p>yes like this , when i'm fill its error like in pictuer</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '10, 00:14</strong></p><img src="https://secure.gravatar.com/avatar/94ec80f83d68112295a513ba0c8db187?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morokat&#39;s gravatar image" /><p>morokat<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morokat has no accepted answers">0%</span></p></img></div></div><div id="comments-container-1524" class="comments-container"><span id="1526"></span><div id="comment-1526" class="comment"><div id="post-1526-score" class="comment-score"></div><div class="comment-text"><p>The filter will need to be "host x.x.x.x" instead of just "x.x.x.x"</p></div><div id="comment-1526-info" class="comment-info"><span class="comment-age">(30 Dec '10, 00:18)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1524" class="comment-tools"></div><div class="clear"></div><div id="comment-1524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1525"></span>

<div id="answer-container-1525" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1525-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can have a look at the <a href="http://wiki.wireshark.org/CaptureSetup">CaptureSetup</a> page on the Wireshark wiki to learn how to capture traffic from other systems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '10, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1525" class="comments-container"></div><div id="comment-tools-1525" class="comment-tools"></div><div class="clear"></div><div id="comment-1525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1527"></span>

<div id="answer-container-1527" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1527-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>i'm still not see the way for fill its!!!!!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '10, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/94ec80f83d68112295a513ba0c8db187?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morokat&#39;s gravatar image" /><p>morokat<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morokat has no accepted answers">0%</span></p></div></div><div id="comments-container-1527" class="comments-container"><span id="1528"></span><div id="comment-1528" class="comment"><div id="post-1528-score" class="comment-score"></div><div class="comment-text"><p>To which answer or comment is this a reply? Please use "add new comment" to respond to earlier given answers instead of posting a new answer (this is not a forum, this is a Q&amp;A site, which works slightly different :-)).</p><p>Have you checked the link I sent you in an earlier answer? Please do...</p></div><div id="comment-1528-info" class="comment-info"><span class="comment-age">(30 Dec '10, 00:41)</span> SYN-bit ♦♦</div></div><span id="1529"></span><div id="comment-1529" class="comment"><div id="post-1529-score" class="comment-score"></div><div class="comment-text"><p>sorry and thanks you</p></div><div id="comment-1529-info" class="comment-info"><span class="comment-age">(30 Dec '10, 00:46)</span> morokat</div></div><span id="1530"></span><div id="comment-1530" class="comment"><div id="post-1530-score" class="comment-score"></div><div class="comment-text"><p>i'm still can't use !!!! i want capture 192.168.1.192 that is from swict</p></div><div id="comment-1530-info" class="comment-info"><span class="comment-age">(30 Dec '10, 01:10)</span> morokat</div></div><span id="1531"></span><div id="comment-1531" class="comment"><div id="post-1531-score" class="comment-score"></div><div class="comment-text"><p>Have you read the "CaptureSetup" page I mentioned earlier?</p></div><div id="comment-1531-info" class="comment-info"><span class="comment-age">(30 Dec '10, 01:23)</span> SYN-bit ♦♦</div></div><span id="1532"></span><div id="comment-1532" class="comment"><div id="post-1532-score" class="comment-score"></div><div class="comment-text"><p>yes i read here http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_on_the_machine_you.27re_interested_in http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_MITM_.28Man-In-The-Middle.29_software and here http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_an_Ethernet_hub but all talk and talk not see tutorial about how to use sorry i'm very newbie about this app</p></div><div id="comment-1532-info" class="comment-info"><span class="comment-age">(30 Dec '10, 01:28)</span> morokat</div></div><span id="1533"></span><div id="comment-1533" class="comment not_top_scorer"><div id="post-1533-score" class="comment-score"></div><div class="comment-text"><p>Analyzing network traffic is not straightforward with a one-solution-fits-all scenario. It is therefor not easy to provide a tutorial, as each setup can be different. It also depends on the knowledge level of the person wanting to do the analysis.</p><p>You might want to read the book "Wireshark Network Analysis" by Laura Chappell (http://www.wiresharkbook.com/), which is an excellent introduction to Network Analysis.</p></div><div id="comment-1533-info" class="comment-info"><span class="comment-age">(30 Dec '10, 01:50)</span> SYN-bit ♦♦</div></div><span id="1541"></span><div id="comment-1541" class="comment not_top_scorer"><div id="post-1541-score" class="comment-score"></div><div class="comment-text"><p>Morokat, Please answer the following questions so people can help you. 1) Are you using a switch? 2) What is the name/model of the switch? 3) Which PC (192.168.1.1 or 1.2) has Wireshark installed? thanks you my following here 1. yes i'm using switch 2. switch name TENDA 16 switch 3. 192.168.1.1 install Wireshark waiting for ur kind</p></div><div id="comment-1541-info" class="comment-info"><span class="comment-age">(30 Dec '10, 18:43)</span> morokat</div></div><span id="1542"></span><div id="comment-1542" class="comment not_top_scorer"><div id="post-1542-score" class="comment-score"></div><div class="comment-text"><p>Morokat,</p><p>It is important to be precise when providing information for us. Tenda has multiple switch models. Tenda has two 16 port switches. One supports port-mirroring, the other doesn't. Only with port-mirroring will you be able to usefully see traffic to and from another computer. What is the <em>exact</em> model you have?</p></div><div id="comment-1542-info" class="comment-info"><span class="comment-age">(30 Dec '10, 19:29)</span> martyvis</div></div></div><div id="comment-tools-1527" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-1527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

