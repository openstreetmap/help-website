+++
type = "question"
title = "Username / password not available"
description = '''Hi there, I am using Pirni Pro, a network sniffer, and I did a test on my own network. I have went to mail.yahoo.com, signed up with my username and password, then stoped the sniffer. It gave me a log.pcap file, I have downloaded it to my computer, opened it with WireShark and used the search tool. ...'''
date = "2011-06-05T15:18:00Z"
lastmod = "2011-06-05T17:35:00Z"
weight = 4388
keywords = [ "pirni" ]
aliases = [ "/questions/4388" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Username / password not available](/questions/4388/username-password-not-available)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4388-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, I am using Pirni Pro, a network sniffer, and I did a test on my own network. I have went to mail.yahoo.com, signed up with my username and password, then stoped the sniffer. It gave me a log.pcap file, I have downloaded it to my computer, opened it with WireShark and used the search tool. While searching for "mail.yahoo.com" or "yahoo.com", it gaved me results, but when searching after my username and / or password it gaved me back no results.</p><p>Any tips please on how to see the username and / or password ?</p><p>Thanks !</p></div><div id="question-tags" class="tags-container tags">pirni</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '11, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/49a53864b39c4f913795c6b023be6f55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nlkoo&#39;s gravatar image" /><p>nlkoo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nlkoo has no accepted answers">0%</span></p></div></div><div id="comments-container-4388" class="comments-container"></div><div id="comment-tools-4388" class="comment-tools"></div><div class="clear"></div><div id="comment-4388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4390"></span>

<div id="answer-container-4390" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4390-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't see it. Yahoo automatically redirects you to an SSL encrypted page, meaning that you used HTTPS to login. Due to the encryption you won't be able to see the password (which is the reason why it was encrypted in the first place ;-))</p><p>If you look at your capture you'll see that mail.yahoo.com replies with a return code 302 in the inital conversation to port 80, redirecting you to https://login.yahoo.com.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '11, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4390" class="comments-container"><span id="4401"></span><div id="comment-4401" class="comment"><div id="post-4401-score" class="comment-score"></div><div class="comment-text"><p>Oh, so I can gather all usernames and passwords on websites that have "http://site.com" and not "http<strong>s</strong>:// ?</p><p>Thanks for the reply Jasper</p><p><em>converted to comment due to the Q&amp;A nature of this website</em></p></div><div id="comment-4401-info" class="comment-info"><span class="comment-age">(06 Jun '11, 07:28)</span> nlkoo</div></div><span id="4404"></span><div id="comment-4404" class="comment"><div id="post-4404-score" class="comment-score"></div><div class="comment-text"><p>Yes, you should, as long as the communication is unencrypted and you are able to capture the packets containing the credentials.</p></div><div id="comment-4404-info" class="comment-info"><span class="comment-age">(06 Jun '11, 07:38)</span> Jasper ♦♦</div></div></div><div id="comment-tools-4390" class="comment-tools"></div><div class="clear"></div><div id="comment-4390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

