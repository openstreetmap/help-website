+++
type = "question"
title = "Wi-Fi direct"
description = '''Hi, We have encountered a problem using Wireshark to capture traffic between two nodes communicating with the Wi-Fi direct protocol. Encryption seems to be mandatory. Is there a way to decrypt tne packets and show them in Wireshark? --Thomas'''
date = "2015-05-13T08:49:00Z"
lastmod = "2017-03-01T09:52:00Z"
weight = 42370
keywords = [ "wi-fi", "direct" ]
aliases = [ "/questions/42370" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wi-Fi direct](/questions/42370/wi-fi-direct)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42370-score" class="post-score" title="current number of votes">0</div><span id="post-42370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, We have encountered a problem using Wireshark to capture traffic between two nodes communicating with the Wi-Fi direct protocol. Encryption seems to be mandatory. Is there a way to decrypt tne packets and show them in Wireshark?</p><p>--Thomas</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wi-fi" rel="tag" title="see questions tagged &#39;wi-fi&#39;">wi-fi</span> <span class="post-tag tag-link-direct" rel="tag" title="see questions tagged &#39;direct&#39;">direct</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '15, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/13d40a0697fea6c1b20509108be2fc2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomaslindh&#39;s gravatar image" /><p><span>Thomaslindh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomaslindh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '15, 09:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-42370" class="comments-container"></div><div id="comment-tools-42370" class="comment-tools"></div><div class="clear"></div><div id="comment-42370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42371"></span>

<div id="answer-container-42371" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42371-score" class="post-score" title="current number of votes">2</div><span id="post-42371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In all WiFi Direct connections, there is a Group Owner (GO) that has the authority to issue and revoke credentials. Also, the WiFi Direct Specification uses WiFi Protected Setup (WPS) or sometimes referred to as WiFi Simple Configuration (WSC) to exchange credentials. So the GO becomes the WSC Registrar and the other devices become Enrollees.</p><p>The WSC Registrar (GO) generates and issues the network credentials (security keys) to the Enrollee (Client). In a WSC connection, all credential exchanges between enrollee and registrar are encrypted. If you perform a WiFi capture of the WSC exchange, the user will not be able to determine the PSK passphrase. The only way to determine the passphrase is to query the registrar (GO).</p><p>So you need a way to get the credential from the GO. This requires the GO to be rooted - in Android vocabulary. Then you need to know how to extract the WiFi credentials.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '15, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-42371" class="comments-container"><span id="42396"></span><div id="comment-42396" class="comment"><div id="post-42396-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the check mark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-42396-info" class="comment-info"><span class="comment-age">(14 May '15, 08:24)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-42371" class="comment-tools"></div><div class="clear"></div><div id="comment-42371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59764"></span>

<div id="answer-container-59764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59764-score" class="post-score" title="current number of votes">1</div><span id="post-59764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this blog <a href="https://androcraftsite.wordpress.com/2017/03/01/decrypting-wifi-direct-packets-in-wireshark/">https://androcraftsite.wordpress.com/2017/03/01/decrypting-wifi-direct-packets-in-wireshark/</a> it explains how to get PSK for android phones and you can use those PSK to decrypt your packets</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '17, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/eecc9aba66aa565df87dd6a72b26092f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rajat27&#39;s gravatar image" /><p><span>rajat27</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rajat27 has no accepted answers">0%</span></p></div></div><div id="comments-container-59764" class="comments-container"><span id="59768"></span><div id="comment-59768" class="comment"><div id="post-59768-score" class="comment-score">1</div><div class="comment-text"><p>Thanks for providing the location of where to find the credentials within Android!</p></div><div id="comment-59768-info" class="comment-info"><span class="comment-age">(01 Mar '17, 09:52)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-59764" class="comment-tools"></div><div class="clear"></div><div id="comment-59764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

