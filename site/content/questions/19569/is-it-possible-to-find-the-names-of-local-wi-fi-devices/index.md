+++
type = "question"
title = "Is it possible to find the names of local Wi-Fi devices?"
description = '''Hi  I want to know if it possible to find wireless devices like cellphones which are not connected or connected to an access point(it means i want name of devices which are On but not connected) and also distinguish between them by ssid or name of device or etc. Can i do this and what is requirement...'''
date = "2013-03-16T12:59:00Z"
lastmod = "2014-04-15T09:30:00Z"
weight = 19569
keywords = [ "wireless", "device", "name" ]
aliases = [ "/questions/19569" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to find the names of local Wi-Fi devices?](/questions/19569/is-it-possible-to-find-the-names-of-local-wi-fi-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19569-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I want to know if it possible to find wireless devices like cellphones which are not connected or connected to an access point(it means i want name of devices which are On but not connected) and also distinguish between them by ssid or name of device or etc. Can i do this and what is requirements for this if answer is yes?</p></div><div id="question-tags" class="tags-container tags">wireless device name</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '13, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/2897b94c86f4fd9645169552255fcef9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="behnam&#39;s gravatar image" /><p>behnam<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="behnam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Mar '13, 14:19</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-19569" class="comments-container"><span id="19579"></span><div id="comment-19579" class="comment"><div id="post-19579-score" class="comment-score"></div><div class="comment-text"><p>Well, first of all, not all cellphones support Wi-Fi, so the access point, in the sense of a Wi-Fi access point, might be irrelevant.</p><p>In addition, there are several billion cellphones on the planet, so finding all the ones that aren't connected to your access point could be a bit difficult. :-)</p><p>Which <em>particular</em> cellphones are you trying to find? The ones that support Wi-Fi and that are close enough to some Wi-Fi-capable device that their Wi-Fi transmissions can be seen by that device?</p></div><div id="comment-19579-info" class="comment-info"><span class="comment-age">(16 Mar '13, 16:48)</span> Guy Harris ♦♦</div></div><span id="19594"></span><div id="comment-19594" class="comment"><div id="post-19594-score" class="comment-score"></div><div class="comment-text"><p>Yeah I mean Wi-Fi-capable devices that their Wi-Fi transmissions can be seen by my device. So i want to find devices not access points and also these devices are not connected to any access point but they are turned on by these devices.(turned on= for example laptops can be on by a mechanical key)</p></div><div id="comment-19594-info" class="comment-info"><span class="comment-age">(17 Mar '13, 13:25)</span> behnam</div></div></div><div id="comment-tools-19569" class="comment-tools"></div><div class="clear"></div><div id="comment-19569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19595"></span>

<div id="answer-container-19595" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19595-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have a radiotap you can get the wireless information from signals in your area and some other device information.<br />
</p><p>Without a radiotap you could use a set of filters to isolate that type of traffic. Here's a few examples that I've found work successfully:</p><p>http.user_agent contains "iPhone" || http.user_agent contains "Blackberry" || http.user_agent contains "Android" || http.user_agent contains "iPad"</p><p>Now this assumes the person is connected to the network and you have visibility at the WAN.<br />
</p><p>Hope this is helpful,</p><p>John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '13, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-19595" class="comments-container"><span id="19598"></span><div id="comment-19598" class="comment"><div id="post-19598-score" class="comment-score"></div><div class="comment-text"><p>I should google it because i don't know much about this radiotap. and tnx for the clues</p></div><div id="comment-19598-info" class="comment-info"><span class="comment-age">(17 Mar '13, 15:03)</span> behnam</div></div></div><div id="comment-tools-19595" class="comment-tools"></div><div class="clear"></div><div id="comment-19595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31844"></span>

<div id="answer-container-31844" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31844-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should search on Google which is very helpful and also get more knowledge about other wi-fi devices.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/356bef7b97a5375c99695c2493131fa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnrooney&#39;s gravatar image" /><p>johnrooney<br />
(suspended)<br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnrooney has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Apr '14, 10:44</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-31844" class="comments-container"><span id="31845"></span><div id="comment-31845" class="comment"><div id="post-31845-score" class="comment-score"></div><div class="comment-text"><p>This is really not an answer at all. Consider adding more information about <em>how</em> to solve the problem presented in the question. Otherwise, (especially with your extraneous link) you look like a spambot.</p></div><div id="comment-31845-info" class="comment-info"><span class="comment-age">(15 Apr '14, 10:45)</span> multipleinte...</div></div></div><div id="comment-tools-31844" class="comment-tools"></div><div class="clear"></div><div id="comment-31844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

