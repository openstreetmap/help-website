+++
type = "question"
title = "Wireshark via Remote Desktop Protocol"
description = '''Hii, if i type on my keyboard &quot; X &quot; via on RDP , where can i see in Wireshark??? i didnt find anything on Frame , Ethernet, Internet Protocol and in Transmission Control Protocol! typing X is maybe represented in binary or hex in?? if yes, where?? Or is it encrypted and i can not see it?!?! i need u...'''
date = "2014-08-05T07:58:00Z"
lastmod = "2014-08-05T09:53:00Z"
weight = 35220
keywords = [ "rdp", "homework", "wireshark" ]
aliases = [ "/questions/35220" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark via Remote Desktop Protocol](/questions/35220/wireshark-via-remote-desktop-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35220-score" class="post-score" title="current number of votes">0</div><span id="post-35220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hii,</p><p>if i type on my keyboard " X " via on RDP , where can i see in Wireshark??? i didnt find anything on Frame , Ethernet, Internet Protocol and in Transmission Control Protocol! typing X is maybe represented in binary or hex in?? if yes, where?? Or is it encrypted and i can not see it?!?!</p><p>i need ur help for my thesis:(</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span> <span class="post-tag tag-link-homework" rel="tag" title="see questions tagged &#39;homework&#39;">homework</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '14, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/09e914d0757725b5059168c435ca07f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lackysnumber%20one&#39;s gravatar image" /><p><span>lackysnumber...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lackysnumber one has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '14, 08:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-35220" class="comments-container"></div><div id="comment-tools-35220" class="comment-tools"></div><div class="clear"></div><div id="comment-35220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35225"></span>

<div id="answer-container-35225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35225-score" class="post-score" title="current number of votes">2</div><span id="post-35225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at the following article:</p><blockquote><p><a href="https://labs.portcullis.co.uk/blog/retrospective-decryption-of-ssl-encrypted-rdp-sessions/">https://labs.portcullis.co.uk/blog/retrospective-decryption-of-ssl-encrypted-rdp-sessions/</a></p></blockquote><p>It describes how to decrypt (ssl encrypted) RDP traffic and how to identify keystrokes.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '14, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '14, 08:49</strong> </span></p></div></div><div id="comments-container-35225" class="comments-container"><span id="35228"></span><div id="comment-35228" class="comment"><div id="post-35228-score" class="comment-score"></div><div class="comment-text"><p>many thnks to Kurt and Jasper.....i will try with ssl encrypted</p></div><div id="comment-35228-info" class="comment-info"><span class="comment-age">(05 Aug '14, 09:53)</span> <span class="comment-user userinfo">lackysnumber...</span></div></div></div><div id="comment-tools-35225" class="comment-tools"></div><div class="clear"></div><div id="comment-35225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35221"></span>

<div id="answer-container-35221" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35221-score" class="post-score" title="current number of votes">0</div><span id="post-35221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's usually encrypted, but even if it weren't you'd not see and "X", because RDP is most likely transfering keycodes instead of characters. So I doubt you'll ever see it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '14, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35221" class="comments-container"><span id="35222"></span><div id="comment-35222" class="comment"><div id="post-35222-score" class="comment-score"></div><div class="comment-text"><p>Also have a look at the <a href="http://wiki.wireshark.org/RDP">RDP wiki page</a>.</p></div><div id="comment-35222-info" class="comment-info"><span class="comment-age">(05 Aug '14, 08:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-35221" class="comment-tools"></div><div class="clear"></div><div id="comment-35221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

