+++
type = "question"
title = "Wireshark causing network problems"
description = '''I am trying to use Wireshark to monitor our internet usage. We have been maxing out on our bandwidth and I want to work out who is using it and why. If it&#x27;s valid we need to upgrade our internet pipe if not I need to stop the problem. So I setup Wireshark on a spare Windows 7 machine that has two ne...'''
date = "2012-02-08T02:44:00Z"
lastmod = "2013-09-12T03:50:00Z"
weight = 8892
keywords = [ "problem", "network", "wireshark" ]
aliases = [ "/questions/8892" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark causing network problems](/questions/8892/wireshark-causing-network-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8892-score" class="post-score" title="current number of votes">0</div><span id="post-8892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use Wireshark to monitor our internet usage. We have been maxing out on our bandwidth and I want to work out who is using it and why. If it's valid we need to upgrade our internet pipe if not I need to stop the problem.</p><p>So I setup Wireshark on a spare Windows 7 machine that has two network cards. And setup Port mirroring (RA and TX) on my Switch (Netgear GS748T). This mirrors the port connected to the Internet router to the port connected to the Wireshark PC.</p><p>But after a few minutes of running Wireshark all users on the switch loose internet connectivity. I can no longer ping my internet router. I have to stop and exit Wireshark to get internet connectivity back.</p><p>I have set Wireshark to use Promisculous mode.</p><p>What am I doing wrong?</p><p>BTW. I have setup Microsoft Network Monitor 3.4 on the same machine using the same Port Mirroring and works without any problems. But I don't like using it. Its too difficult to get the info I need. Wireshark is much nicer to use. I don't run Wireshark and Network Monitor 3.4 at the same time.</p><p>Thanks,</p><p>Mark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '12, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/f03cb7d1ee96a65c79ab03396a3d4be4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marky&#39;s gravatar image" /><p><span>marky</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marky has one accepted answer">50%</span></p></div></div><div id="comments-container-8892" class="comments-container"><span id="8895"></span><div id="comment-8895" class="comment"><div id="post-8895-score" class="comment-score"></div><div class="comment-text"><p>have you unhooked all the protocols like TCP/IP, File sharing etc. in the capturing NICs preferences?</p></div><div id="comment-8895-info" class="comment-info"><span class="comment-age">(08 Feb '12, 04:58)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="8900"></span><div id="comment-8900" class="comment"><div id="post-8900-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply.</p><p>Do you mean unticked them from the properties of the network adapter within Windows 7?</p></div><div id="comment-8900-info" class="comment-info"><span class="comment-age">(08 Feb '12, 05:32)</span> <span class="comment-user userinfo">marky</span></div></div><span id="8901"></span><div id="comment-8901" class="comment"><div id="post-8901-score" class="comment-score"></div><div class="comment-text"><p>I have not unticked any of the protocols from the properties of the network adapter.</p><p>BTW. It is not just the Wireshark PC that looses contact with our internet router but all users on the network.</p></div><div id="comment-8901-info" class="comment-info"><span class="comment-age">(08 Feb '12, 07:14)</span> <span class="comment-user userinfo">marky</span></div></div><span id="8902"></span><div id="comment-8902" class="comment"><div id="post-8902-score" class="comment-score"></div><div class="comment-text"><p>Yap, i understood you perfectly but please untick every single protocol from that NIC with which you capture the data from the span port and see if the issue still exists. Please remember to unplug the card before you do so and then attach it to the switch again</p></div><div id="comment-8902-info" class="comment-info"><span class="comment-age">(08 Feb '12, 07:18)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="8903"></span><div id="comment-8903" class="comment"><div id="post-8903-score" class="comment-score"></div><div class="comment-text"><p>OK, Thanks. I will try that in the morning when I only have a few users online.</p></div><div id="comment-8903-info" class="comment-info"><span class="comment-age">(08 Feb '12, 07:44)</span> <span class="comment-user userinfo">marky</span></div></div></div><div id="comment-tools-8892" class="comment-tools"></div><div class="clear"></div><div id="comment-8892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8930"></span>

<div id="answer-container-8930" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8930-score" class="post-score" title="current number of votes">1</div><span id="post-8930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="marky has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well I removed all the protocols from the network adapter and I didn't have any problems this morning.</p><p>I will switch off DNS lookups also as it's not essential. Just makes it easier to read.</p><p>Thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '12, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/f03cb7d1ee96a65c79ab03396a3d4be4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marky&#39;s gravatar image" /><p><span>marky</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marky has one accepted answer">50%</span></p></div></div><div id="comments-container-8930" class="comments-container"><span id="8933"></span><div id="comment-8933" class="comment"><div id="post-8933-score" class="comment-score"></div><div class="comment-text"><p>Glad to hear it worked</p></div><div id="comment-8933-info" class="comment-info"><span class="comment-age">(09 Feb '12, 07:53)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-8930" class="comment-tools"></div><div class="clear"></div><div id="comment-8930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8906"></span>

<div id="answer-container-8906" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8906-score" class="post-score" title="current number of votes">1</div><span id="post-8906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I doubt if the network settings are causing the problem as you say you can use the same machine with Netmon without a problem and you also say that when you stop Wireshark, but leave the Wireshark PC connected, the problem goes away.</p><p>This means Wireshark itself seems to do something that is frustrating all other traffic. Wireshark is capturing passively, so it should not be a problem. The only thing Wireshark will do on the network is perform (a lot of) reverse DNS lookups. Maybe that is causing your issue. You can disable name resolution (for the network layer) and see if that helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '12, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-8906" class="comments-container"><span id="24601"></span><div id="comment-24601" class="comment"><div id="post-24601-score" class="comment-score"></div><div class="comment-text"><p>hi can you please tell me how to disable the name resolution</p></div><div id="comment-24601-info" class="comment-info"><span class="comment-age">(12 Sep '13, 03:17)</span> <span class="comment-user userinfo">Paras Watts</span></div></div><span id="24603"></span><div id="comment-24603" class="comment"><div id="post-24603-score" class="comment-score"></div><div class="comment-text"><p>Edit -&gt; Preferences -&gt; Name Resolution -&gt; uncheck the top three items</p></div><div id="comment-24603-info" class="comment-info"><span class="comment-age">(12 Sep '13, 03:50)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-8906" class="comment-tools"></div><div class="clear"></div><div id="comment-8906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

