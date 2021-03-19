+++
type = "question"
title = "CDP question"
description = '''The only thing that is not clear for me is the fact that for example I connect a cisco access point to a cisco swith with cdp enable both running same version and if then I SPAN the port connecting the access point I can clear see that the cdp packet reaching the port on the switch and then I should...'''
date = "2012-01-16T09:24:00Z"
lastmod = "2012-01-16T10:30:00Z"
weight = 8410
keywords = [ "cdp" ]
aliases = [ "/questions/8410" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [CDP question](/questions/8410/cdp-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8410-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The only thing that is not clear for me is the fact that for example I connect a cisco access point to a cisco swith with cdp enable both running same version and if then I SPAN the port connecting the access point I can clear see that the cdp packet reaching the port on the switch and then I should display at the other end with show cdp nei to say something.</p><p>but what happens when I have to switches involved</p><p>SW-1----SW-2</p><p>Should I see the info of cdp in SW1 of switch 2 and the other way around? applying a double session one span in switch 1 and another session in switch 2.</p></div><div id="question-tags" class="tags-container tags">cdp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '12, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/0d552ea2856847502a1c37614082f447?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnRodriguez&#39;s gravatar image" /><p>JohnRodriguez<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnRodriguez has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '12, 13:22</p></div></div><div id="comments-container-8410" class="comments-container"><span id="8421"></span><div id="comment-8421" class="comment"><div id="post-8421-score" class="comment-score"></div><div class="comment-text"><p>@JohnRodriguez; Please use "add a comment" to follow up, instead of editing the original question. Otherwise, it is very difficult for others to see what was asked and to follow the flow of the conversation.</p></div><div id="comment-8421-info" class="comment-info"><span class="comment-age">(16 Jan '12, 16:37)</span> Jim Aragon</div></div></div><div id="comment-tools-8410" class="comment-tools"></div><div class="clear"></div><div id="comment-8410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8413"></span>

<div id="answer-container-8413" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8413-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no acknowledgement from the other device. CDP packets are sent to the multicast address 01-00-0c-cc-cc-cc out each connected interface. Because the CDP packet is sent out a directly-connected interface, you can be pretty confident that it will reach the interface of the other system, as long as the interface is up, functioning, and connected. Of course, the other system might not listen for CDP packets. No, there is no way to tell <em>in Wireshark</em> that the other device has received CDP packets. You would have to log in to the other device and display its CDP information.</p><p>The devices do not send CDP packets to <em>get</em> information from each other; they send CDP packets to <em>send</em> information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '12, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '12, 15:50</p></div></div><div id="comments-container-8413" class="comments-container"></div><div id="comment-tools-8413" class="comment-tools"></div><div class="clear"></div><div id="comment-8413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

