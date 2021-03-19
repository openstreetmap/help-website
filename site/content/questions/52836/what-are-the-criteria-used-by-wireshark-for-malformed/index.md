+++
type = "question"
title = "What are the criteria used by Wireshark for &quot;Malformed&quot; ?"
description = '''Hi, I&#x27;ve searched around the internet but I could not find an answer matching exactly what I&#x27;m looking for. I&#x27;m currently working on fuzzing network protocols, with different softwares. Some are fully automated (but are not free), some are open-source but it requires I write my own scripts. Since I ...'''
date = "2016-05-23T09:19:00Z"
lastmod = "2016-05-24T04:22:00Z"
weight = 52836
keywords = [ "arp", "malformed", "fuzzing" ]
aliases = [ "/questions/52836" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What are the criteria used by Wireshark for "Malformed" ?](/questions/52836/what-are-the-criteria-used-by-wireshark-for-malformed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52836-score" class="post-score" title="current number of votes">0</div><span id="post-52836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've searched around the internet but I could not find an answer matching exactly what I'm looking for. I'm currently working on fuzzing network protocols, with different softwares. Some are fully automated (but are not free), some are open-source but it requires I write my own scripts. Since I want to create errors with the open sources ones, I'm trying to create "Malformed packets" so the devices I'm testing have to deal with malformed data.</p><p>For my tests, I'm fuzzing ARP protocol. When I'm observing "Malformed packets" with fully automated, test version of a fuzzer, I only have full well-formed packets with my self-writted fuzzing scripts. I observed differences beetween the two kinds of packets, but I couldn't find out what is the difference that let Wireshark say it's "Malformed" or it's not.</p><p>Here is an example of two similar packets which I cannot understand why there is a malformed one and a "clean" one. <img src="http://i.imgur.com/hxay52n.png" alt="http://i.imgur.com/hxay52n.png" /></p><p>What is the real difference beetween those two packets ? I can see the payload is starting 4 bytes earlier on the malformed one, but why isn't Wireshark saying that the "opcode" is unknown ? When I generate a packet with my open source software, I can put any byte I want anywhere so the packet is the most malformed ARP packet you've ever seen, Wireshark will still say the code is unknown, not that the packet is malformed.</p><p>Has anyone an answer ? Thank you for your attention</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-malformed" rel="tag" title="see questions tagged &#39;malformed&#39;">malformed</span> <span class="post-tag tag-link-fuzzing" rel="tag" title="see questions tagged &#39;fuzzing&#39;">fuzzing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '16, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/33d9e24b85ffa13bcab07d031ea11f48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pygmay&#39;s gravatar image" /><p><span>Pygmay</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pygmay has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52836" class="comments-container"></div><div id="comment-tools-52836" class="comment-tools"></div><div class="clear"></div><div id="comment-52836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52839"></span>

<div id="answer-container-52839" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52839-score" class="post-score" title="current number of votes">1</div><span id="post-52839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pygmay has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look at <a href="https://ask.wireshark.org/questions/52190/what-is-the-reason-for-malformed-packet-error/52193">this answer</a> of <span>@Guy Harris</span> to almost the same question asked a few weeks ago.</p><p>In your particular case, the deviation from a valid packet you have caused may be so small that it can be pinpointed rather than causing one of the dissectors participating in the dissection to get out of sync and thus report a malformed packet. Unknown opcode is an example of such an error, and moreover, the dissector may still be fine if the other shifted data can be interpreted as <strong>formally</strong> valid ones.</p><p>In real life, a packet corrupt that way in transmission is highly unlikely to make it to the destination application because the receiving network card would drop it due to incorrect CRC; if you forge a packet using your software, the CRC is correct (because it is calculated <strong>after</strong> you've damaged the data) so the receiving network card delivers the packet to the application (and also Wireshark, which also cannot see packets received with incorrect CRC). I.e. this way, you can test the robustness of the protocol itself and its receiver-side implementation against errors of sender-side implementation.</p><p>NB: if you want us to look at the difference between two packets in detail, post them as capture files (or, in case of one or two packets, at least as hex dumps which can be imported), never as screenshots.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '16, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52839" class="comments-container"><span id="52854"></span><div id="comment-52854" class="comment"><div id="post-52854-score" class="comment-score"></div><div class="comment-text"><p>Hello, Thank you for your fast answer, that I find clearer that the one given to Guy Harris ^^'</p><p>I understand quite well this on a high level. Is it possible to read somewhere how the dissector is working on a lower level ? For example, can I find details of the behaviour of the ARP dissector in a very low level ?</p><p>NB : Got it, thanks :)</p></div><div id="comment-52854-info" class="comment-info"><span class="comment-age">(24 May '16, 02:03)</span> <span class="comment-user userinfo">Pygmay</span></div></div><span id="52857"></span><div id="comment-52857" class="comment"><div id="post-52857-score" class="comment-score"></div><div class="comment-text"><p>I guess <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-arp.c;hb=refs/heads/master-2.0#l1365">this is as low as you can go</a>. Start at <code>dissect_arp()</code> and work your way from there.</p></div><div id="comment-52857-info" class="comment-info"><span class="comment-age">(24 May '16, 03:00)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="52862"></span><div id="comment-52862" class="comment"><div id="post-52862-score" class="comment-score"></div><div class="comment-text"><p>Thanks !!!</p></div><div id="comment-52862-info" class="comment-info"><span class="comment-age">(24 May '16, 04:22)</span> <span class="comment-user userinfo">Pygmay</span></div></div></div><div id="comment-tools-52839" class="comment-tools"></div><div class="clear"></div><div id="comment-52839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

