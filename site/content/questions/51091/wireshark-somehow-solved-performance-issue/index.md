+++
type = "question"
title = "WireShark somehow solved performance issue"
description = '''Hi there, our sotfware product installed on Windows Server 2012R2, running on hypervisor esxi v6, was showing very long responses and delays on application requests.  After investigation that we performed on application level and which showed no problems, we focused on network level. We installed Wi...'''
date = "2016-03-22T07:49:00Z"
lastmod = "2016-03-22T09:03:00Z"
weight = 51091
keywords = [ "performance" ]
aliases = [ "/questions/51091" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [WireShark somehow solved performance issue](/questions/51091/wireshark-somehow-solved-performance-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51091-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, our sotfware product installed on Windows Server 2012R2, running on hypervisor esxi v6, was showing very long responses and delays on application requests. After investigation that we performed on application level and which showed no problems, we focused on network level. We installed Wireshark-win64-1.12.7 and WinPcap 4.1.3 in order to trace down network communication and to find out where is the problem. Surprisingly we immediately noticed significant improvement of speed and general stability of system. From that moment application is working as expected, but we are not able to discover why. We have been trying to isolate the problem on production environment, but without any success. We are quite limited in investigation because production environment is running, it cannot be turned off even for a short time and we can not perform risky operations on it. Could anyone provide us with little help and give us some hints where could be the issue and what parameters which are relevant in our case did WireShark change? It seems that this basically solved our performance issues, but from various reasons we have to fix it properly. :-) Many thanks!</p></div><div id="question-tags" class="tags-container tags">performance</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '16, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/94b7386055596209b51d347fd7bdc93d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dominika&#39;s gravatar image" /><p>Dominika<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dominika has no accepted answers">0%</span></p></div></div><div id="comments-container-51091" class="comments-container"><span id="51121"></span><div id="comment-51121" class="comment"><div id="post-51121-score" class="comment-score"></div><div class="comment-text"><p>Does it be better from the moment of installation or do you need to start a trace for better performance. And have you installed the latest network card drivers?</p></div><div id="comment-51121-info" class="comment-info"><span class="comment-age">(23 Mar '16, 05:22)</span> Christian_R</div></div></div><div id="comment-tools-51091" class="comment-tools"></div><div class="clear"></div><div id="comment-51091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51097"></span>

<div id="answer-container-51097" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51097-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the older answer you are even more interested in (because it matches your case quite closely) is <a href="https://ask.wireshark.org/questions/50123/win-2012-r2-vm-network-much-faster-after-wireshark-was-started/50178">this one</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '16, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-51097" class="comments-container"><span id="51120"></span><div id="comment-51120" class="comment"><div id="post-51120-score" class="comment-score"></div><div class="comment-text"><p>Thank you, we already tried something similar, but will do it again. I will get back to this aftewards.</p></div><div id="comment-51120-info" class="comment-info"><span class="comment-age">(23 Mar '16, 04:58)</span> Dominika</div></div><span id="51334"></span><div id="comment-51334" class="comment"><div id="post-51334-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, it helped us! It took time to test it and to perform what was needed because as I already mentioned, we are running on production env. with limited access. It seems that the problem is really in vmware, I hope we could upgrade to newer version where it is fixed very soon..</p><p>Once again - many thanks, we really appreciate your help!</p></div><div id="comment-51334-info" class="comment-info"><span class="comment-age">(01 Apr '16, 01:13)</span> Dominika</div></div><span id="51342"></span><div id="comment-51342" class="comment"><div id="post-51342-score" class="comment-score"></div><div class="comment-text"><p>Thank you too, but all the tributes belong to the authors of the older Answer I've referred to. I was just a postman in this case.</p></div><div id="comment-51342-info" class="comment-info"><span class="comment-age">(01 Apr '16, 05:53)</span> sindy</div></div></div><div id="comment-tools-51097" class="comment-tools"></div><div class="clear"></div><div id="comment-51097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51093"></span>

<div id="answer-container-51093" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51093-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This subject was already discussed in the following thread:</p><p><a href="https://ask.wireshark.org/questions/11733/wireshark-install-seems-to-improve-performance">https://ask.wireshark.org/questions/11733/wireshark-install-seems-to-improve-performance</a></p><p>Hope that helps!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '16, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-51093" class="comments-container"><span id="51119"></span><div id="comment-51119" class="comment"><div id="post-51119-score" class="comment-score"></div><div class="comment-text"><p>Thank you, but this will not help in our case.</p></div><div id="comment-51119-info" class="comment-info"><span class="comment-age">(23 Mar '16, 04:56)</span> Dominika</div></div></div><div id="comment-tools-51093" class="comment-tools"></div><div class="clear"></div><div id="comment-51093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

