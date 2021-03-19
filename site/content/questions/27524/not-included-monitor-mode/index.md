+++
type = "question"
title = "not included monitor mode"
description = '''now, here by-step instruction on how I do it wi-fi:alfa awus036h step 1: catch the traffic going through wlan1 -iwconfig -airmon-ng start wlan1 http://savepic.net/3980106.htm step 2: due to the fact that under the root wireshark wrote a mistake made the following http://securityblog.gr/1195/run-wire...'''
date = "2013-11-28T02:06:00Z"
lastmod = "2013-11-28T07:26:00Z"
weight = 27524
keywords = [ "monitor" ]
aliases = [ "/questions/27524" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [not included monitor mode](/questions/27524/not-included-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27524-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>now, here by-step instruction on how I do it</p><p>wi-fi:alfa awus036h</p><p>step 1: catch the traffic going through wlan1</p><p>-iwconfig</p><p>-airmon-ng start wlan1</p><p><a href="http://savepic.net/3980106.htm">http://savepic.net/3980106.htm</a></p><p>step 2: due to the fact that under the root wireshark wrote a mistake made the following</p><p><a href="http://securityblog.gr/1195/run-wireshark-as-a-user-rather-than-root-ubuntu/">http://securityblog.gr/1195/run-wireshark-as-a-user-rather-than-root-ubuntu/</a></p><p>step 3: -wiershark (run from normal user)</p><p>when I choose the mon0 or wlan1 generates an error:</p><p><a href="http://savepic.net/3950410.htm">http://savepic.net/3950410.htm</a> <a href="http://savepic.net/3970890.htm">http://savepic.net/3970890.htm</a></p><p>then try to turn on the monitor mode it gives me an error(see screenshot 2)</p><p>what will be your advice?</p><p>on OS back-track the error persists</p></div><div id="question-tags" class="tags-container tags">monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '13, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/348b58b10734f511c32ddaa3f6c15488?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sokolov%20%20Andrey&#39;s gravatar image" /><p>Sokolov Andrey<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sokolov  Andrey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '13, 03:30</p></div></div><div id="comments-container-27524" class="comments-container"></div><div id="comment-tools-27524" class="comment-tools"></div><div class="clear"></div><div id="comment-27524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27534"></span>

<div id="answer-container-27534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27534-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>what will be your advice?</p></blockquote><p><strong>First advice</strong>: Please <strong>stop creating</strong> new questions <strong>for the same problem</strong>, again and again!</p><ul><li><a href="http://ask.wireshark.org/questions/26919/how-to-fix-the-error-the-capabilities-of-the-capture-device-wlan0-could-not-be-obtained-that-device-doesnt-support-monitor-mode">Question #1</a><br />
</li><li><a href="http://ask.wireshark.org/questions/26925/how-else-can-i-fix-this-error">Question #2</a><br />
</li><li><a href="http://ask.wireshark.org/questions/27201/dont-want-to-work-in-monitoring-mode">Question #3</a><br />
</li><li><a href="http://ask.wireshark.org/questions/27524/not-included-monitor-mode">Question #4</a><br />
</li></ul><p>It's easier to follow a problem in a <strong>single question</strong>, than in four different questions for the <strong>same</strong> problem.</p><p><strong>Second advice</strong>: reply to those people who have answered you in other identical questions. Maybe that leads to something.</p><p><strong>Third advice</strong>: Please try to capture on mon0 with <strong>dumpcap</strong> or <strong>tcpdump</strong> (as already mentioned in one of the solutions linked in your other questions!). What is the output of that command?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '13, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '13, 07:27</p></div></div><div id="comments-container-27534" class="comments-container"></div><div id="comment-tools-27534" class="comment-tools"></div><div class="clear"></div><div id="comment-27534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

