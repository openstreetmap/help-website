+++
type = "question"
title = "Drop packets"
description = '''Hello, I trying to figure out how to do this. If you look here in the FAQ at question 12 it talks about filtering traffic. Does filtering means the packet will get dropped if it meets the filter criteria? Basically what I need is a way to drop packets containing a certain string. Somebody is sending...'''
date = "2011-03-20T17:57:00Z"
lastmod = "2011-03-23T14:36:00Z"
weight = 2960
keywords = [ "filter", "dropping", "drop", "packets", "filtering" ]
aliases = [ "/questions/2960" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Drop packets](/questions/2960/drop-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2960-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I trying to figure out how to do this.</p><p>If you look <a href="http://www.wireshark.org/faq.html#q12.1">here</a> in the FAQ at question 12 it talks about filtering traffic. Does filtering means the packet will get dropped if it meets the filter criteria?</p><p>Basically what I need is a way to drop packets containing a certain string. Somebody is sending a specific packet that crashes my server.<br />
</p><p>On Linux, you can use iptables to inspect the packets and block this attack easily, but currently I'm using Windows.</p><p>Does Wireshark have the ability to drop packets? If not, is there an extension/addon that can do it? Or how do you all drop malicious packets?</p><p>Thank you all for your help.</p></div><div id="question-tags" class="tags-container tags">filter dropping drop packets filtering</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '11, 17:57</strong></p><img src="https://secure.gravatar.com/avatar/6c52d9cacf4ddf372464326e5b8a9557?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lake393&#39;s gravatar image" /><p>lake393<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lake393 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-2960" class="comments-container"></div><div id="comment-tools-2960" class="comment-tools"></div><div class="clear"></div><div id="comment-2960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2986"></span>

<div id="answer-container-2986" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2986-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Nope, Wireshark captures and analyzes network traffic; it doesn't act as a "front-end" to selectively deny/allow traffic. Anything Wireshark sees is handled by the network interface(s).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 15:46</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-2986" class="comments-container"></div><div id="comment-tools-2986" class="comment-tools"></div><div class="clear"></div><div id="comment-2986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3063"></span>

<div id="answer-container-3063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3063-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Filtering" in Wireshark either means "limiting which packets Wireshark captures" or "limiting which of the packets in the current capture that Wireshark displays"; it doesn't mean that it controls what packets the machine on which it's running accepts.</p><p>What you need is some form of firewall software that supports string matching. You'd have to look at the firewall software programs available for your version of Windows to see whether any of them support dropping packets that contain a given string.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3063" class="comments-container"></div><div id="comment-tools-3063" class="comment-tools"></div><div class="clear"></div><div id="comment-3063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2963"></span>

<div id="answer-container-2963" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2963-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you can use Snort's window's version to drop malicious packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/4137971bd3a388bd8060c1de3e817ad3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blueguy777&#39;s gravatar image" /><p>blueguy777<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blueguy777 has no accepted answers">0%</span></p></div></div><div id="comments-container-2963" class="comments-container"></div><div id="comment-tools-2963" class="comment-tools"></div><div class="clear"></div><div id="comment-2963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

