+++
type = "question"
title = "Email password recover"
description = '''Hi, I try to recover my email password. I use Thunderbird. ssl/tls security option but for authentication I use simple username/password. incoming : imap on 993.  outgoing : smtp 465 (ssl/tls and simple username/password)  With this kind of setup I thought that login/password where not encrypted on ...'''
date = "2016-08-17T02:45:00Z"
lastmod = "2016-09-10T00:40:00Z"
weight = 54900
keywords = [ "password", "email", "recovering" ]
aliases = [ "/questions/54900" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Email password recover](/questions/54900/email-password-recover)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54900-score" class="post-score" title="current number of votes">0</div><span id="post-54900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I try to recover my email password. I use Thunderbird. ssl/tls security option but for authentication I use simple username/password.</p><p>incoming : imap on 993. <img src="https://osqa-ask.wireshark.org/upfiles/incoming.email.setup.PNG" alt="alt text" /></p><p>outgoing : smtp 465 (ssl/tls and simple username/password) <img src="https://osqa-ask.wireshark.org/upfiles/outgoing.email.setup.PNG" alt="alt text" /></p><p>With this kind of setup I thought that login/password where not encrypted on the internet (between my email manager and my email provider [imap and smtp] )</p><p>So I start capturing, and try a few filter : - smtp - smtp.req.command == "AUTH" - imap.request contains "login" - smtp.req.parameter contains "FROM"</p><p>All these return nothing...</p><p>So I try : On a shell dig &lt;imap_adress_of_my_email_manager&gt; (recovering the ip adress) By the way, smtp is the same name and ip. (seems unusual ?) and put this filter : ip.dst == &lt;email_provider_ip_adress&gt;</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_L9vCrpt.PNG" alt="alt text" /></p><p>I see what seem to be an exchange of public certificate and private key at the very beginning.</p><p>My questions are : - With this kind of email setup I thought that login/password where not encrypted on the internet. So I miss the correct packet with a wrong filter ? - Did I missunderstood my email protocol and peraphs read more about smtp ?</p><p>With regards, Clement</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span> <span class="post-tag tag-link-email" rel="tag" title="see questions tagged &#39;email&#39;">email</span> <span class="post-tag tag-link-recovering" rel="tag" title="see questions tagged &#39;recovering&#39;">recovering</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '16, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/675599f487c9b85ea3a88414b0e3939c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Titi&#39;s gravatar image" /><p><span>Titi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Titi has no accepted answers">0%</span></p></img></div></div><div id="comments-container-54900" class="comments-container"></div><div id="comment-tools-54900" class="comment-tools"></div><div class="clear"></div><div id="comment-54900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54903"></span>

<div id="answer-container-54903" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54903-score" class="post-score" title="current number of votes">0</div><span id="post-54903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it is a misunderstanding. The plaintext vs. "encrypted" password and plaintext vs. encrypted connection are two independent things. User authentication using password is just one part of the application conversation, so as soon as you permit use of SSL/TLS for the conversation as a whole, the user authentication part of it is also encrypted using TLS, although its contents is plaintext. On the other hand, if you do not use TLS, everything (including the contents of the e-mail messages) passes through the network without encryption, so as a password leakage protection you may use application-level encryption for the password alone (actually, the password is not transmitted at all, even encrypted - instead, there is a cryptographic check whether both parties know the same password, but that's another story).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '16, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></img></div></div><div id="comments-container-54903" class="comments-container"><span id="54916"></span><div id="comment-54916" class="comment"><div id="post-54916-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thank you for your answer.</p></div><div id="comment-54916-info" class="comment-info"><span class="comment-age">(17 Aug '16, 05:38)</span> <span class="comment-user userinfo">Titi</span></div></div></div><div id="comment-tools-54903" class="comment-tools"></div><div class="clear"></div><div id="comment-54903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54922"></span>

<div id="answer-container-54922" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54922-score" class="post-score" title="current number of votes">0</div><span id="post-54922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried Thunderbird itself?</p><p>Go to: Tool menu -&gt; Options -&gt; Security -&gt; press "Saved Passwords" -&gt; press "Show Passwords"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '16, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-54922" class="comments-container"><span id="55458"></span><div id="comment-55458" class="comment"><div id="post-55458-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer. I know my password, I just want to see if the "normal password" configuration permit to see clear password on the internet or not.</p></div><div id="comment-55458-info" class="comment-info"><span class="comment-age">(10 Sep '16, 00:40)</span> <span class="comment-user userinfo">Titi</span></div></div></div><div id="comment-tools-54922" class="comment-tools"></div><div class="clear"></div><div id="comment-54922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

