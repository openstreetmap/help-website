+++
type = "question"
title = "DIS Warfare"
description = '''Hi everybody, I&#x27;m just starting out with Wireshark and ran a test capture on one of our servers. The expert infos showed a lot of errors, mostly malformed packets. I filtered out some packets and was hoping someone can explain what&#x27;s actually going on here. The source addresses are NEC Dect AP&#x27;s on ...'''
date = "2015-12-11T15:09:00Z"
lastmod = "2015-12-11T17:16:00Z"
weight = 48463
keywords = [ "warfare", "malformed", "dis" ]
aliases = [ "/questions/48463" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DIS Warfare](/questions/48463/dis-warfare)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48463-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody,</p><p>I'm just starting out with Wireshark and ran a test capture on one of our servers. The expert infos showed a lot of errors, mostly malformed packets. I filtered out some packets and was hoping someone can explain what's actually going on here. The source addresses are NEC Dect AP's on our network.</p><p><a href="https://drive.google.com/file/d/0B5faGzOi4clgNGJtUXMzMEJ0RWM/view?usp=sharing">a screenshot</a></p><p><a href="https://drive.google.com/file/d/0B5faGzOi4clgREdiMlRKdWpYTms/view?usp=sharing">dis.pcapng</a></p><p>We're not experiencing noticable issues, but I would still like to know if this is normal behaviour (think not) or if I need to further investigate this. Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">warfare malformed dis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '15, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/6aa7c4075c3bc72c72fc6cfe28f8f9cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="schapie1978&#39;s gravatar image" /><p>schapie1978<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="schapie1978 has no accepted answers">0%</span></p></div></div><div id="comments-container-48463" class="comments-container"></div><div id="comment-tools-48463" class="comment-tools"></div><div class="clear"></div><div id="comment-48463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48465"></span>

<div id="answer-container-48465" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48465-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is just the DECT AP's communication with each other on the network. They use Multicast to discover each other, hence why you are seeing the traffic at your server. It seems that they use a proprietary protocol, and Wireshark makes a guess as to the protocol...in this instance DIS, since it uses UDP port 3000 which is IANA registered.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '15, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-48465" class="comments-container"></div><div id="comment-tools-48465" class="comment-tools"></div><div class="clear"></div><div id="comment-48465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

