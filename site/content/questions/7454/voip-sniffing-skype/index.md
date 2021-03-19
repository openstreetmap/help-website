+++
type = "question"
title = "VOIP sniffing (Skype)"
description = '''When i sniff for skype calls all i get is UDP packets. how can i get it so wireshark captures RTP packets so i can use wireshark player to hear the voice clips. Thanks. even if it means using a different voip client, i just need to get a example voip call recording. Thanks'''
date = "2011-11-15T16:42:00Z"
lastmod = "2011-11-15T22:51:00Z"
weight = 7454
keywords = [ "sniffing", "voip" ]
aliases = [ "/questions/7454" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [VOIP sniffing (Skype)](/questions/7454/voip-sniffing-skype)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7454-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When i sniff for skype calls all i get is UDP packets. how can i get it so wireshark captures RTP packets so i can use wireshark player to hear the voice clips. Thanks. even if it means using a different voip client, i just need to get a example voip call recording. Thanks</p></div><div id="question-tags" class="tags-container tags">sniffing voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '11, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/4da038ce3cdd0709b1f313e66c227fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stampy29&#39;s gravatar image" /><p>Stampy29<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stampy29 has no accepted answers">0%</span></p></div></div><div id="comments-container-7454" class="comments-container"></div><div id="comment-tools-7454" class="comment-tools"></div><div class="clear"></div><div id="comment-7454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7461"></span>

<div id="answer-container-7461" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7461-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If Skype is using RTP you could select the UDP packet and do "decode as" and selct RTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '11, 22:05</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-7461" class="comments-container"></div><div id="comment-tools-7461" class="comment-tools"></div><div class="clear"></div><div id="comment-7461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7462"></span>

<div id="answer-container-7462" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7462-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Skype stuff in encrypted. Have a look at the Wiki <a href="http://wiki.wireshark.org/SampleCaptures">SampleCaptures</a> page, the section SIP and RTP likely contains what you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '11, 22:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7462" class="comments-container"></div><div id="comment-tools-7462" class="comment-tools"></div><div class="clear"></div><div id="comment-7462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

