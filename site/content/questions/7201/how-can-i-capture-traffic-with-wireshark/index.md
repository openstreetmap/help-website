+++
type = "question"
title = "How can I capture traffic with Wireshark?"
description = '''Hi, I am being driven round the bend by my isp as they want some results from wire shark, I know there is a problem with my line but they will not do anymore without these results. I am unable to get my network card in the drop down menu to enable me to start the capture. Any help will be much neede...'''
date = "2011-11-02T10:31:00Z"
lastmod = "2011-11-02T10:45:00Z"
weight = 7201
keywords = [ "windows", "wireless", "interface", "capture" ]
aliases = [ "/questions/7201" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I capture traffic with Wireshark?](/questions/7201/how-can-i-capture-traffic-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7201-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am being driven round the bend by my isp as they want some results from wire shark, I know there is a problem with my line but they will not do anymore without these results. I am unable to get my network card in the drop down menu to enable me to start the capture. Any help will be much needed. Thankyou.</p></div><div id="question-tags" class="tags-container tags">windows wireless interface capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '11, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/862bb5c0af6995f0e5de5477776b1680?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JIO22&#39;s gravatar image" /><p>JIO22<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JIO22 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Nov '11, 14:11</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-7201" class="comments-container"><span id="7212"></span><div id="comment-7212" class="comment"><div id="post-7212-score" class="comment-score">1</div><div class="comment-text"><p>What OS are you running? If you're running Windows, do you have WinPcap installed? Which version of Wireshark are you using? Which drop-down menu are you referring to exactly? If you bring up the Capture -&gt; Interfaces dialog from the Wireshark toolbar, do you see a list of interfaces and do any of them have incrementing packet counts? What happens if you click, "Start" next to one with incrementing packet counts, assuming you have any?</p></div><div id="comment-7212-info" class="comment-info"><span class="comment-age">(02 Nov '11, 17:59)</span> cmaynard ♦♦</div></div><span id="7223"></span><div id="comment-7223" class="comment"><div id="post-7223-score" class="comment-score"></div><div class="comment-text"><p>os is windows vista,WinPcap installed,wireshark version is 1.6.3 (SVN Rev 39702 from /trunk-1.6),the drop down menu is after you have clicked on capture on the main page and then click on options,it is the drop down menu in the top right hand corner. Yes from the capture interfaces toolbar i do see 3 different interfaces and 1 of them had incremeting packet counts it is the one called "microsoft", when I click start it brings up another screen with lots of data/numbers and info in lots of lines and adding more and more the longer you leave it. Does this mean it is working? Excellent if so.</p></div><div id="comment-7223-info" class="comment-info"><span class="comment-age">(03 Nov '11, 15:15)</span> JIO22</div></div><span id="7224"></span><div id="comment-7224" class="comment"><div id="post-7224-score" class="comment-score">1</div><div class="comment-text"><p>Yes, that sounds good. You should now be able to save the data and send it to your ISP as per their instructions.</p></div><div id="comment-7224-info" class="comment-info"><span class="comment-age">(03 Nov '11, 15:30)</span> grahamb ♦</div></div><span id="7238"></span><div id="comment-7238" class="comment"><div id="post-7238-score" class="comment-score"></div><div class="comment-text"><p>Excellent, thankyou for the info, hope this will do them!</p></div><div id="comment-7238-info" class="comment-info"><span class="comment-age">(04 Nov '11, 08:26)</span> JIO22</div></div></div><div id="comment-tools-7201" class="comment-tools"></div><div class="clear"></div><div id="comment-7201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7203"></span>

<div id="answer-container-7203" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7203-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I suspect that your capture environment is not set up correctly. Look at the <a href="http://wiki.wireshark.org/CaptureSetup/NetworkInterfaces">Network Interfaces</a> article on the Wireshark Wiki. You should probably also look at the <a href="http://www.wireshark.org/docs/wsug_html_chunked/" title="User&#39;s Guide">Wireshark User's Guide</a> and read the <a href="http://wiki.wireshark.org/CaptureSetup" title="CaptureSetup">Capture Setup</a> article on the Wireshark Wiki.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '11, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-7203" class="comments-container"><span id="7204"></span><div id="comment-7204" class="comment"><div id="post-7204-score" class="comment-score"></div><div class="comment-text"><p>Thankyou for your quick reply. I have to admit I am not very savvy with computers and all the meanings/lingo, i have looked and read lots on these guides but it totally confuses me as I do not understand 90% of what I am meant to do. I am totally stuck as my isp just keep pushing it back to get these results of wireshark and that they cant do anything without them.</p><p>Is there anything obvious you can suggest for me to try first and then I can reply back with what happens?</p><p>The laptop is a sony vaio, with windows vista, with a wireless network card/interface.</p><p>Thankyou for you help.</p></div><div id="comment-7204-info" class="comment-info"><span class="comment-age">(02 Nov '11, 10:55)</span> JIO22</div></div><span id="7205"></span><div id="comment-7205" class="comment"><div id="post-7205-score" class="comment-score"></div><div class="comment-text"><p>See also the <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Windows">wireless capture</a> article on the Wiki</p></div><div id="comment-7205-info" class="comment-info"><span class="comment-age">(02 Nov '11, 11:37)</span> grahamb ♦</div></div><span id="7208"></span><div id="comment-7208" class="comment"><div id="post-7208-score" class="comment-score"></div><div class="comment-text"><p>Thankyou again. Can anyone help me with trying anything in particular, or point me in the right direction to anything inparticular as the more I look into any of the guides etc I just get lost with it!</p><p>Thankyou.</p></div><div id="comment-7208-info" class="comment-info"><span class="comment-age">(02 Nov '11, 13:46)</span> JIO22</div></div></div><div id="comment-tools-7203" class="comment-tools"></div><div class="clear"></div><div id="comment-7203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

