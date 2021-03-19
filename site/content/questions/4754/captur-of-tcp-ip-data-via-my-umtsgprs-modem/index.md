+++
type = "question"
title = "Captur of tcp ip data via my UMTS/GPRS Modem"
description = '''Hello Experts, I use wireshark for the first time and see it as a geat powerfull tool. unfortunately i can not find any method to capeter my communication via my gprs modem. (Only the Ethernet adapters of my laptop are in the list of capter interfaces) Is there any method to capter GPRS traffic ? Sy...'''
date = "2011-06-25T14:43:00Z"
lastmod = "2011-06-25T20:55:00Z"
weight = 4754
keywords = [ "gprs", "huawei", "modem" ]
aliases = [ "/questions/4754" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Captur of tcp ip data via my UMTS/GPRS Modem](/questions/4754/captur-of-tcp-ip-data-via-my-umtsgprs-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4754-score" class="post-score" title="current number of votes">0</div><span id="post-4754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Experts, I use wireshark for the first time and see it as a geat powerfull tool. unfortunately i can not find any method to capeter my communication via my gprs modem. (Only the Ethernet adapters of my laptop are in the list of capter interfaces)</p><p>Is there any method to capter GPRS traffic ?</p><p>System Info: Laptop with win vista SP1, 32 bit GPRS Modem Huawei E160G via USB.</p><p>Thanks a lot for your help.</p><p>ps. the programm's name is wireshark, but maybe i can capture wireless data ???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gprs" rel="tag" title="see questions tagged &#39;gprs&#39;">gprs</span> <span class="post-tag tag-link-huawei" rel="tag" title="see questions tagged &#39;huawei&#39;">huawei</span> <span class="post-tag tag-link-modem" rel="tag" title="see questions tagged &#39;modem&#39;">modem</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '11, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/5da5adbceb6d6a1a73fe6db23db6af1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hape01&#39;s gravatar image" /><p><span>hape01</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hape01 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jun '11, 22:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-4754" class="comments-container"></div><div id="comment-tools-4754" class="comment-tools"></div><div class="clear"></div><div id="comment-4754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4755"></span>

<div id="answer-container-4755" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4755-score" class="post-score" title="current number of votes">1</div><span id="post-4755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As <a href="http://www.winpcap.org/misc/faq.htm#Q-5">question 5 in the WinPcap FAQ</a> indicates, PPP devices are not supported on Windows Vista and Windows 7. Mobile phone modems show up as PPP devices, so you cannot capture on them.</p><p>The "wire" in Wireshark nonwithstanding, Wireshark is, in principle, capable of capturing on wireless networks. However, it is dependent on the capabilities of the OS it's running on, and the capture mechanism it uses, so if, on some particular OS, those don't support capturing on, for example, mobile phone modems, or Wi-Fi adapters, you won't be able to capture on them on that OS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '11, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4755" class="comments-container"></div><div id="comment-tools-4755" class="comment-tools"></div><div class="clear"></div><div id="comment-4755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

