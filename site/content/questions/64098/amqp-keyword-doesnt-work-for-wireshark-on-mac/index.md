+++
type = "question"
title = "&quot;amqp&quot; keyword doesn&#x27;t work for Wireshark on Mac"
description = '''I enter &quot;amqp&quot; keyword to filter the request/response in Wireshark on mac, my mac version is macOS version Sierra 10.12.6, while this keyword doesn&#x27;t work at all after I click &quot;Start capturing packets&quot;. while the rabbitmq client does receive the message sent. could someone help to resolve this issue...'''
date = "2017-10-23T02:22:00Z"
lastmod = "2017-10-26T23:50:00Z"
weight = 64098
keywords = [ "rabbitmq" ]
aliases = [ "/questions/64098" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# ["amqp" keyword doesn't work for Wireshark on Mac](/questions/64098/amqp-keyword-doesnt-work-for-wireshark-on-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64098-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I enter "amqp" keyword to filter the request/response in Wireshark on mac, my mac version is macOS version Sierra 10.12.6, while this keyword doesn't work at all after I click "Start capturing packets". while the rabbitmq client does receive the message sent. could someone help to resolve this issue? thanks in advance.</p></div><div id="question-tags" class="tags-container tags">rabbitmq</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '17, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/872d8df493c944600eab2f7432fdba71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hailongshih&#39;s gravatar image" /><p>hailongshih<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hailongshih has no accepted answers">0%</span></p></div></div><div id="comments-container-64098" class="comments-container"></div><div id="comment-tools-64098" class="comment-tools"></div><div class="clear"></div><div id="comment-64098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="64101"></span>

<div id="answer-container-64101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64101-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you attempting to use it as a Capture Filter, i.e. in the filter field just above the interface list that is preceded by the text "Capture ...using this filter:"?</p><p>If so, then this won't work as amqp is not valid for a capture filter, but is valid for a display filter.</p><p>You can try using a capture filter of "port 5672" for regular unencrypted amqp traffic, but your environment may vary</p><p>If your amqp traffic is using TCP on the standard port (5672) then it should be automatically dissected, and if running on TLS using the standard port (5671) and if you have decryption correctly configured that should be automatically dissected as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '17, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-64101" class="comments-container"><span id="64162"></span><div id="comment-64162" class="comment"><div id="post-64162-score" class="comment-score"></div><div class="comment-text"><blockquote><p>amqp is not valid for a capture filter</p></blockquote><p>...on <em>any</em> platform, not just macOS.</p><p>You could, however, use <code>port amqp</code> on at least some platforms to capture on the standard port 5672.</p></div><div id="comment-64162-info" class="comment-info"><span class="comment-age">(24 Oct '17, 11:35)</span> Guy Harris ♦♦</div></div><span id="64210"></span><div id="comment-64210" class="comment"><div id="post-64210-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb. I did use keyword "amqp" in the display filter but still no results. "port 5672" in capture filter will be automatically transfered to "amqp" as well, all failed and no packets are captured.</p></div><div id="comment-64210-info" class="comment-info"><span class="comment-age">(25 Oct '17, 23:48)</span> hailongshih</div></div><span id="64211"></span><div id="comment-64211" class="comment"><div id="post-64211-score" class="comment-score"></div><div class="comment-text"><p>If you capture without a capture filter, and then apply the display filter <code>amqp</code>, what TCP ports are the packets going to and coming from? If neither of them is 5672, then your AMQP traffic is <em>not</em> using the standard port 5672, and you will have to find out what port it <em>is</em> using, and use <code>port XXXX</code>, where <code>XXXX</code> is the port it's using, as the capture filter.</p></div><div id="comment-64211-info" class="comment-info"><span class="comment-age">(25 Oct '17, 23:58)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-64101" class="comment-tools"></div><div class="clear"></div><div id="comment-64101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="64266"></span>

<div id="answer-container-64266" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64266-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Guy,</p><p>I'm sure that rabbitmq on my mac uses the default port 5672 and I find mongo in display filter doesn't work neither while using the default port 27017. do you use teamViewer so that we can have a screen sharing?</p><p>thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '17, 23:50</strong></p><img src="https://secure.gravatar.com/avatar/872d8df493c944600eab2f7432fdba71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hailongshih&#39;s gravatar image" /><p>hailongshih<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hailongshih has no accepted answers">0%</span></p></div></div><div id="comments-container-64266" class="comments-container"></div><div id="comment-tools-64266" class="comment-tools"></div><div class="clear"></div><div id="comment-64266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

