+++
type = "question"
title = "Receiving udp packets on blocked port"
description = '''Hello, I want to send data from Android device to a Windows PC. Therefore I create a hotspot on the Android device and connect the PC to it. I wrote a small app that sends UDP packets from the Android device. I can see the UDP packets when I use Wireshark on the PC but I&#x27;m not able to open/use the d...'''
date = "2015-05-20T01:15:00Z"
lastmod = "2015-05-27T07:50:00Z"
weight = 42569
keywords = [ "firewall", "udp", "android", "port", "wireshark" ]
aliases = [ "/questions/42569" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Receiving udp packets on blocked port](/questions/42569/receiving-udp-packets-on-blocked-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42569-score" class="post-score" title="current number of votes">0</div><span id="post-42569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I want to send data from Android device to a Windows PC. Therefore I create a hotspot on the Android device and connect the PC to it. I wrote a small app that sends UDP packets from the Android device. I can see the UDP packets when I use Wireshark on the PC but I'm not able to open/use the data in any other program including Simulink and a small Java application I wrote. Is it possible that the packets are blocked for example by a firewall but I can see them in Wireshark anyway? Or can I be sure that the packets make it through the firewall if I receive them in Wireshark?</p><p>Would be glad if someone could help me :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '15, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/be27a9ee1b4299b854b285e19ce2d540?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ph_il&#39;s gravatar image" /><p><span>Ph_il</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ph_il has no accepted answers">0%</span></p></div></div><div id="comments-container-42569" class="comments-container"></div><div id="comment-tools-42569" class="comment-tools"></div><div class="clear"></div><div id="comment-42569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42705"></span>

<div id="answer-container-42705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42705-score" class="post-score" title="current number of votes">1</div><span id="post-42705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have encountered the similar situation before on a program I wrote on windows. My experience is that these packets will show up in wireshark even though that are blocked by firewall. If there is no firewall and there is no application listening on the UDP port, windows will send ICMP port unreachable packets back.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '15, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-42705" class="comments-container"></div><div id="comment-tools-42705" class="comment-tools"></div><div class="clear"></div><div id="comment-42705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

