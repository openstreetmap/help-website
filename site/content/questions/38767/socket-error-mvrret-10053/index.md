+++
type = "question"
title = "Socket error mvrRet = 10053"
description = '''hi guys, i need some help. i have an issue to backup via a Checkpoint getting error in Backup Exec 0xe00084f8 - The network connection to the Backup Exec Remote Agent has been lost.  in the debug logs found this : Socket error mvrRet = 10053  http://www.symantec.com/business/support/index?page=conte...'''
date = "2014-12-29T06:20:00Z"
lastmod = "2014-12-30T03:59:00Z"
weight = 38767
keywords = [ "winsock" ]
aliases = [ "/questions/38767" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Socket error mvrRet = 10053](/questions/38767/socket-error-mvrret-10053)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38767-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>i need some help. i have an issue to backup via a Checkpoint getting error in Backup Exec 0xe00084f8 - The network connection to the Backup Exec Remote Agent has been lost.</p><p>in the debug logs found this : Socket error mvrRet = 10053</p><p><a href="http://www.symantec.com/business/support/index?page=content&amp;id=TECH148097">http://www.symantec.com/business/support/index?page=content&amp;id=TECH148097</a></p><p>what could be the reason ?</p><p>tried with any - any rule = same issue</p><p>how could i use wireshark to see what's going on ?</p><p>as per</p><p><a href="http://support.microsoft.com/kb/819124/en-us">http://support.microsoft.com/kb/819124/en-us</a></p><p>WSAECONNABORTED (10053)</p><p>Translation: Software caused connection abort. Description: An established connection was stopped by the software in your host computer, possibly because of a data transmission time-out or protocol error.</p><p>does that mean that this is not Backup Exec issue ?</p><p>any help please ! :)</p><p>thank you very much</p></div><div id="question-tags" class="tags-container tags">winsock</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '14, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-38767" class="comments-container"></div><div id="comment-tools-38767" class="comment-tools"></div><div class="clear"></div><div id="comment-38767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38784"></span>

<div id="answer-container-38784" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38784-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i have an issue to backup via a <strong>Checkpoint</strong> getting error in Backup Exec</p></blockquote><p>sounds like you are trying to do a network backup through a Check Point firewall, right?</p><blockquote><p>WSAECONNABORTED (10053)<br />
what could be the reason ?</p></blockquote><p>Either one end of the participating systems terminates the connection, OR the firewall between those systems!</p><blockquote><p>how could i use wireshark to see what's going on ?</p></blockquote><pre><code>Backup Server [1] --- [2] Firewall --- [3] --- Backup Agent</code></pre><p>Try to capture the traffic in front of the backup agent [3] and the backup server [1] in parallel. See the following Wiki entry how to do that:</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a><br />
</p></blockquote><p>If you see a connection abort (RESET or FIN) at the server side [1] (coming from the server), it's the server who is terminating the connection. Then you should ask Symantec support.</p><p>If you see a connection abort (RESET/FIN) at the agent [3], but NOT on the server side [1], then it's the firewall who is terminating the session. In that case, please contact your local firewall guru.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-38784" class="comments-container"><span id="38791"></span><div id="comment-38791" class="comment"><div id="post-38791-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>yes. a Check Point firewall is in-between. thank you so much for you answers - makes sense to me. can you please tell me if any specific filter should be enabled on both (Backup Exec and Backup Agent Server) or which one would you enable in this case ...</p><p>thank you in advance</p><p>Best Regards</p><p>adasko</p></div><div id="comment-38791-info" class="comment-info"><span class="comment-age">(30 Dec '14, 05:31)</span> adasko</div></div><span id="38792"></span><div id="comment-38792" class="comment"><div id="post-38792-score" class="comment-score">1</div><div class="comment-text"><p>I would use a <strong>capture filter</strong> with the ip address of the server and the agent</p><blockquote><p>host x.x.x.x and host y.y.y.y</p></blockquote></div><div id="comment-38792-info" class="comment-info"><span class="comment-age">(30 Dec '14, 05:33)</span> Kurt Knochner ♦</div></div><span id="38795"></span><div id="comment-38795" class="comment"><div id="post-38795-score" class="comment-score"></div><div class="comment-text"><p>great ! will give it a try !</p></div><div id="comment-38795-info" class="comment-info"><span class="comment-age">(30 Dec '14, 07:13)</span> adasko</div></div><span id="38810"></span><div id="comment-38810" class="comment"><div id="post-38810-score" class="comment-score"></div><div class="comment-text"><p>@adasko: You awarded 11 points to me. I'm not sure you really wanted to do that, as your karma went down to 0. I rewarded the 11 karma points back to you!</p><p>So, if a supplied answer resolves your question you can "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can also up vote the answer (thumb up).</p></div><div id="comment-38810-info" class="comment-info"><span class="comment-age">(30 Dec '14, 14:20)</span> Kurt Knochner ♦</div></div><span id="38819"></span><div id="comment-38819" class="comment not_top_scorer"><div id="post-38819-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>one more question. let's say host A has the IP 10.0.0.1 and Host B the IP 10.0.0.2. so i would create on host A the capture like this host 10.0.0.1 anf host 10.0.0.2 but how on host B ? the other way i mean host 10.0.0.2 and host 10.0.0.1 or it should be the same as on host A ?</p><p>thank you very much and a Very Happy New YEar for YOU !</p></div><div id="comment-38819-info" class="comment-info"><span class="comment-age">(31 Dec '14, 05:43)</span> adasko</div></div><span id="38828"></span><div id="comment-38828" class="comment"><div id="post-38828-score" class="comment-score">1</div><div class="comment-text"><p>The filter is the same on both hosts, as you want to see only traffic from/to 10.0.0.1 AND from/to 10.0.0.2 on both systems. The order of the host statements does not matter, so <code>host x.x.x.x and host y.y.y.y</code> is identical to <code>host y.y.y.y and  host x.x.x.x</code>.</p></div><div id="comment-38828-info" class="comment-info"><span class="comment-age">(31 Dec '14, 08:08)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-38784" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-38784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

