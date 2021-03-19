+++
type = "question"
title = "don&#x27;t want to work in monitoring mode"
description = '''I have this problem. tried wiershark on two ubuntu OS and linux. And on both OS inactive monitoring what the problem is? WI-FI - ALFA AWUS036 Notebook Acer E1-351 Just saying, in monitoring mode, the map translated.'''
date = "2013-11-21T00:59:00Z"
lastmod = "2013-11-22T02:27:00Z"
weight = 27201
keywords = [ "monitor" ]
aliases = [ "/questions/27201" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [don't want to work in monitoring mode](/questions/27201/dont-want-to-work-in-monitoring-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27201-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have this problem. tried wiershark on two ubuntu OS and linux. And on both OS inactive monitoring what the problem is? WI-FI - ALFA AWUS036 Notebook Acer E1-351 Just saying, in monitoring mode, the map translated.</p></div><div id="question-tags" class="tags-container tags">monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '13, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/348b58b10734f511c32ddaa3f6c15488?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sokolov%20%20Andrey&#39;s gravatar image" /><p>Sokolov Andrey<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sokolov  Andrey has no accepted answers">0%</span></p></div></div><div id="comments-container-27201" class="comments-container"><span id="27234"></span><div id="comment-27234" class="comment"><div id="post-27234-score" class="comment-score"></div><div class="comment-text"><blockquote><p>And on both OS <strong>inactive monitoring</strong></p></blockquote><p>what does that mean??</p></div><div id="comment-27234-info" class="comment-info"><span class="comment-age">(21 Nov '13, 07:40)</span> Kurt Knochner ♦</div></div><span id="27245"></span><div id="comment-27245" class="comment"><div id="post-27245-score" class="comment-score"></div><div class="comment-text"><p>Do you mean that you want to capture in monitor mode on your laptop, but on both Ubuntu Linux and whatever other Linux you're using monitor mode doesn't work?</p></div><div id="comment-27245-info" class="comment-info"><span class="comment-age">(21 Nov '13, 16:59)</span> Guy Harris ♦♦</div></div><span id="27247"></span><div id="comment-27247" class="comment"><div id="post-27247-score" class="comment-score"></div><div class="comment-text"><p>yes, my actions airmon-ng start wlan0 run wireshark and then trying to put a tick in the monitoring, he told me in one OS writes that airmon-ng does not include, although configurations(iwconfig) there is such a network mon0. And the second OS, the second this checkbox is not active P.S. wireshark not run as root then had to make settings that would be run by a normal user. <a href="http://securityblog.gr/1195/run-wireshark-as-a-user-rather-than-root-ubuntu/">http://securityblog.gr/1195/run-wireshark-as-a-user-rather-than-root-ubuntu/</a></p></div><div id="comment-27247-info" class="comment-info"><span class="comment-age">(21 Nov '13, 19:51)</span> Sokolov Andrey</div></div></div><div id="comment-tools-27201" class="comment-tools"></div><div class="clear"></div><div id="comment-27201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27266"></span>

<div id="answer-container-27266" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27266-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please follow the instructions in my answer to a similar question and you should be able to capture traffic in monitor mode.</p><blockquote><p><a href="http://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version">http://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version</a></p></blockquote><p>IMPORTANT: Please capture on <strong>mon0</strong> instead of wlan0 !!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '13, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27266" class="comments-container"></div><div id="comment-tools-27266" class="comment-tools"></div><div class="clear"></div><div id="comment-27266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

