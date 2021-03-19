+++
type = "question"
title = "Cannot scan with my Alfa AWUS036H"
description = '''Hi, I have been working on this problem for weeks. I can only get broadcast traffic over my alfa AWUS036H. I started on windows and tried everything. And then I went to backtrack 5r2 -- which supposed has the right driver already installed. I have followed the instructions on countless forums with n...'''
date = "2012-09-09T16:26:00Z"
lastmod = "2012-09-09T18:00:00Z"
weight = 14148
keywords = [ "monitoring", "awus036h" ]
aliases = [ "/questions/14148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot scan with my Alfa AWUS036H](/questions/14148/cannot-scan-with-my-alfa-awus036h)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have been working on this problem for weeks. I can only get broadcast traffic over my alfa AWUS036H. I started on windows and tried everything. And then I went to backtrack 5r2 -- which supposed has the right driver already installed. I have followed the instructions on countless forums with no luck: I only see broadcast traffic.</p><p>Is it possible that I have a bad alfa? Has that ever happened to anyone? Also, I have onboard wifi -- I have tried this on 3 machines all with onboard wifi. So I am using wlan1 as my interface. Of course, yes I have used airmon-ng to put the card -- actually a usb device -- in monitor mode and then the interface is mon0. And I have put wlan1 in monitor mode manually with iwconfig. I really have tried anything.</p><p>In addition to wireshark I have tried tshark, kismet, airodump-ng.</p><p>Should I trash this card? What should I get instead?</p><p>Thanks,</p><p>Chris</p></div><div id="question-tags" class="tags-container tags">monitoring awus036h</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '12, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/a0086fcbe94b91b73f390ed51984534f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrisexx&#39;s gravatar image" /><p>chrisexx<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrisexx has no accepted answers">0%</span></p></div></div><div id="comments-container-14148" class="comments-container"></div><div id="comment-tools-14148" class="comment-tools"></div><div class="clear"></div><div id="comment-14148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14149"></span>

<div id="answer-container-14149" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14149-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ul><li>You cannot use that adapter to capture WLAN traffic on Windows (monitor mode is not supported by WinPcap - <a href="http://wiki.wireshark.org/CaptureSetup/WLAN).">http://wiki.wireshark.org/CaptureSetup/WLAN).</a></li><li>On Linux you need to activate "monitor" mode for the WLAN adapter (search google for that)</li><li>There are differing reports about the AWUS036H with Backtrack 5R2. Some say it works, others report driver problems !??!. I suggest to search for help in the Back Track forum, as that's certainly a better place than the Wireshark forum.</li></ul><blockquote><p><code>http://www.backtrack-linux.org/forums/forumdisplay.php?f=143</code><br />
</p></blockquote><p>BTW: Did you try what's described in the following link (first post)?</p><blockquote><p><code>http://www.backtrack-linux.org/forums/showthread.php?t=45455</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '12, 18:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Sep '12, 18:07</p></div></div><div id="comments-container-14149" class="comments-container"></div><div id="comment-tools-14149" class="comment-tools"></div><div class="clear"></div><div id="comment-14149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

