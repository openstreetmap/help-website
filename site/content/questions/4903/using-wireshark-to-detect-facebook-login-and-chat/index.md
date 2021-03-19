+++
type = "question"
title = "Using wireshark to detect facebook login and chat?"
description = '''Hi there. Im having a bit of difficulty trying to decipher all the packet info on my machine and was looking for a way to detect the information easier. Im looking to detect a facebook successful login via wireshark as well as detecting if a user uses the chat feature. But i have no idea what all th...'''
date = "2011-07-05T04:01:00Z"
lastmod = "2012-01-22T01:30:00Z"
weight = 4903
keywords = [ "login", "facebook", "chat", "wireshark" ]
aliases = [ "/questions/4903" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Using wireshark to detect facebook login and chat?](/questions/4903/using-wireshark-to-detect-facebook-login-and-chat)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4903-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there. Im having a bit of difficulty trying to decipher all the packet info on my machine and was looking for a way to detect the information easier.</p><p>Im looking to detect a facebook successful login via wireshark as well as detecting if a user uses the chat feature. But i have no idea what all these packets are that are showing up. Is there a filtering option that can be setup just to detect facebook information?</p><p>cheers</p></div><div id="question-tags" class="tags-container tags">login facebook chat wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '11, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/2e3c6047dedb36a286421c0f2bb38e01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jgraham95&#39;s gravatar image" /><p>jgraham95<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jgraham95 has no accepted answers">0%</span></p></div></div><div id="comments-container-4903" class="comments-container"></div><div id="comment-tools-4903" class="comment-tools"></div><div class="clear"></div><div id="comment-4903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4920"></span>

<div id="answer-container-4920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4920-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming the monitored Facebook chat users are not using IM-encryption clients, you can watch Facebook chat messages by applying this display filter: <code>json contains message</code></p><p>Login is encrypted over SSL, so it would be difficult (if not impossible) for a display filter to detect whether a login is <em>successful</em>. You can, however, detect SSL Facebook traffic (which might be for login) using this display filter: <code>tcp contains facebook and ssl</code></p><p><strong>EDIT:</strong> Facebook supports <em>Secure Browsing</em>, which encrypts all Facebook traffic, including chat messages. They've also updated their chat protocol. See recent <a href="http://ask.wireshark.org/questions/7287/facebook-send-message">post</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '11, 22:43</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jan '12, 08:31</p></div></div><div id="comments-container-4920" class="comments-container"><span id="4926"></span><div id="comment-4926" class="comment"><div id="post-4926-score" class="comment-score"></div><div class="comment-text"><p>thanks again. :)</p></div><div id="comment-4926-info" class="comment-info"><span class="comment-age">(06 Jul '11, 07:44)</span> jgraham95</div></div></div><div id="comment-tools-4920" class="comment-tools"></div><div class="clear"></div><div id="comment-4920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8537"></span>

<div id="answer-container-8537" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8537-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The easiest way to follow facebook chats is to use the search function. Use the searchstring 'subject":"","body":"' and search for the string in the packet bytes. As result you see only the text which is displayed on the users screen, no matter whether the transmission is encrypted or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '12, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/82430c9aeb3635c636e17c88c535774a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anon&#39;s gravatar image" /><p>Anon<br />
<span class="score" title="84 reputation points">84</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anon has one accepted answer">16%</span></p></div></div><div id="comments-container-8537" class="comments-container"><span id="8543"></span><div id="comment-8543" class="comment"><div id="post-8543-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>As result you see only the text which is displayed on the users screen, no matter whether the transmission is encrypted or not.</p></blockquote><p>That's <strong>incorrect</strong>. If one were <em>easily</em> able to read encrypted traffic simply by using search functions in Wireshark (or any other packet sniffer), that would defeat the purpose of encryption.</p><p>You can prove this to yourself by enabling "Secure Browsing" in Facebook (<code>Account Settings &gt; Security &gt; Secure Browsing</code>) and then trying your Wireshark filter on live chat traffic.</p></div><div id="comment-8543-info" class="comment-info"><span class="comment-age">(22 Jan '12, 08:23)</span> helloworld</div></div><span id="8605"></span><div id="comment-8605" class="comment"><div id="post-8605-score" class="comment-score"></div><div class="comment-text"><p>The above described search shows the html-packages, which are displayed on the receivers screen and not the encrypted message package. I for myself use facebook with secure browsing and can read my own messages in the captured traffic easily, even so there are encrypted in the relevant packages. Don't ask me why, but I tested it this way, and was astonished that i could read it anyway....</p></div><div id="comment-8605-info" class="comment-info"><span class="comment-age">(25 Jan '12, 08:22)</span> Anon</div></div><span id="8613"></span><div id="comment-8613" class="comment"><div id="post-8613-score" class="comment-score"></div><div class="comment-text"><p>It should be obvious that your chat message(s) are not actually encrypted (in your particular case). To say that Facebook chats are readable in Wireshark despite it being encrypted is <strong>overgeneralizing</strong>.</p><p>I've confirmed that <em>Secure Browsing</em> still (as of today) encrypts my chat messages as well as other Facebook traffic. However, I did notice a small hiccup immediately after setting <em>Secure Browsing</em> from <em>off</em> to <em>on</em>: one of my chat messages came through in cleartext, but encryption took effect thereafter.</p><p>Rest assured, your chat messages <em>are</em> secure (except the first one sometimes ;).</p></div><div id="comment-8613-info" class="comment-info"><span class="comment-age">(25 Jan '12, 17:05)</span> helloworld</div></div></div><div id="comment-tools-8537" class="comment-tools"></div><div class="clear"></div><div id="comment-8537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6912"></span>

<div id="answer-container-6912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6912-score" class="post-score" title="current number of votes">-3</div></div></td><td><div class="item-right"><div class="answer-body"><p>i don't know</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '11, 18:59</strong></p><img src="https://secure.gravatar.com/avatar/3fe0e3cf7732359fb01ac8402ea23db6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dyess002&#39;s gravatar image" /><p>dyess002<br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dyess002 has no accepted answers">0%</span></p></div></div><div id="comments-container-6912" class="comments-container"><span id="46626"></span><div id="comment-46626" class="comment"><div id="post-46626-score" class="comment-score"></div><div class="comment-text"><p>ok, so what would a facebook packet look like?</p></div><div id="comment-46626-info" class="comment-info"><span class="comment-age">(16 Oct '15, 11:31)</span> Steve328</div></div></div><div id="comment-tools-6912" class="comment-tools"></div><div class="clear"></div><div id="comment-6912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

