+++
type = "question"
title = "Computer sending emails via phishing program."
description = '''Hi. So Im currently trying to dig into wireshark, and im now testing if its possible to get email content out of a phishing program (e.g message sent, stored passwords inside program, reciver). Ive found the stream and confirmed that It&#x27;s sending the mails to an unknown gmail address. When I try to ...'''
date = "2013-08-19T17:12:00Z"
lastmod = "2013-08-20T01:31:00Z"
weight = 23854
keywords = [ "phishing", "smtp", "email", "tcp", "wireshark" ]
aliases = [ "/questions/23854" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Computer sending emails via phishing program.](/questions/23854/computer-sending-emails-via-phishing-program)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23854-score" class="post-score" title="current number of votes">0</div><span id="post-23854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>So Im currently trying to dig into wireshark, and im now testing if its possible to get email content out of a phishing program (e.g message sent, stored passwords inside program, reciver). Ive found the stream and confirmed that It's sending the mails to an unknown gmail address. When I try to "follow tcp stream" I just get a bunch of, what seems to be, encoded characters. So no real content. Im wondering if the email is automatically encrypted and that the information is impossible to read from it.</p><p>However I got a feeling it should be possible somehow, since its doing everything from my machine.</p><p>Any idea and/or tips on how to proceed?</p><p>Best regards,</p><p>Wireshark newbie</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-phishing" rel="tag" title="see questions tagged &#39;phishing&#39;">phishing</span> <span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span> <span class="post-tag tag-link-email" rel="tag" title="see questions tagged &#39;email&#39;">email</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '13, 17:12</strong></p><img src="https://secure.gravatar.com/avatar/92218142d86812f36078d5eb4c0ae50a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Whaleshark&#39;s gravatar image" /><p><span>Whaleshark</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Whaleshark has no accepted answers">0%</span></p></div></div><div id="comments-container-23854" class="comments-container"></div><div id="comment-tools-23854" class="comment-tools"></div><div class="clear"></div><div id="comment-23854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23855"></span>

<div id="answer-container-23855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23855-score" class="post-score" title="current number of votes">0</div><span id="post-23855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not knowing the details of what you have found out so far, I'm just guessing. If your "bot" is proabbly sending to an address using public key encryption you won't be able to decode the traffic on the wire, short of dumping the bot's memory and looking for keys. (All of the network traffic will be encrypted by the server's public key, and the subsequent session keys - so unless you have the server's private key, you can't decode traffic just from the wire).</p><p>Your only other hope is if your bot hunts out and would trust a SSL proxy (if that is what it uses for it's encrypted traffic). If so you could deploy a proxy that you have the private key for, and if the bot connects through that, you could decode the traffic.</p><p>There are a lot of ifs there, and probably a lot of work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '13, 21:51</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-23855" class="comments-container"></div><div id="comment-tools-23855" class="comment-tools"></div><div class="clear"></div><div id="comment-23855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23858"></span>

<div id="answer-container-23858" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23858-score" class="post-score" title="current number of votes">0</div><span id="post-23858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>When I try to "follow tcp stream" I just get a bunch of, what seems to be, encoded characters. So no real content.</p></blockquote><p>If the tcp connection was a SMTP connection (port 25 or 465) it could have been encrypted with transport layer encryption (SSL/TLS).</p><p>So, was that a SMTP connection over port 25 or 465? If port 25, did you see the string STARTTLS at the beginning of the TCP connection?</p><blockquote><p>Im wondering if the email is <strong>automatically encrypted</strong> and that the information is impossible to read from it.</p></blockquote><p>It won't be <strong>automatically</strong> encrypted, but if this is a trojan, chances are good, that they use their own encryption scheme to hide their tracks.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '13, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23858" class="comments-container"></div><div id="comment-tools-23858" class="comment-tools"></div><div class="clear"></div><div id="comment-23858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

