+++
type = "question"
title = "Password promiscuous mode"
description = '''HI everyone So I am trying some experimentation: I have disabled wifi security and i go on http website. If I capture from my PC I can see my trafic and can get my password and login send without security. If I ask some one to go on this website from an other pc I can see everything where is going b...'''
date = "2011-12-13T13:04:00Z"
lastmod = "2011-12-14T10:03:00Z"
weight = 7950
keywords = [ "promiscuous", "password", "http" ]
aliases = [ "/questions/7950" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Password promiscuous mode](/questions/7950/password-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7950-score" class="post-score" title="current number of votes">0</div><span id="post-7950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI everyone</p><p>So I am trying some experimentation: I have disabled wifi security and i go on http website. If I capture from my PC I can see my trafic and can get my password and login send without security. If I ask some one to go on this website from an other pc I can see everything where is going but I can't see his password.</p><p>How it's possible ??</p><p>NB:I am on ubuntu and he is on windows .</p><p>thank you for explanation</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '11, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/3ec3bfe5b5bdb3a24d893633da266451?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vring6&#39;s gravatar image" /><p><span>vring6</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vring6 has no accepted answers">0%</span></p></div></div><div id="comments-container-7950" class="comments-container"><span id="7951"></span><div id="comment-7951" class="comment"><div id="post-7951-score" class="comment-score"></div><div class="comment-text"><p>Have you checked that he is not connecting with <code>https</code>? Do you see any traffic from your friend's computer? There are a number of factors that might influence this; promiscuous mode isn't really one of them. Just because the interface is in promiscuous mode doesn't mean that it will change the upper-layer protocol behaviors.</p></div><div id="comment-7951-info" class="comment-info"><span class="comment-age">(13 Dec '11, 14:50)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="7968"></span><div id="comment-7968" class="comment"><div id="post-7968-score" class="comment-score"></div><div class="comment-text"><p>HI</p><p>yes I am on http website, I can see every page he goes, on the same page from my computer i see password and from his computer i am not sure but i seems to be a cookie.</p><p>I don't understand</p></div><div id="comment-7968-info" class="comment-info"><span class="comment-age">(14 Dec '11, 08:45)</span> <span class="comment-user userinfo">vring6</span></div></div></div><div id="comment-tools-7950" class="comment-tools"></div><div class="clear"></div><div id="comment-7950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7970"></span>

<div id="answer-container-7970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7970-score" class="post-score" title="current number of votes">0</div><span id="post-7970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From your comments, I infer that your friend has already logged in to the website before you attempt to capture traffic and that this information is stored in a cookie, resulting in no login credentials being transmitted. Have your friend log out from the website first, and then follow the exact same procedure as you did to log in. This should remove any differences from your setup an your friend's so that you can capture traffic as expected. Of course, this assumes that your friend is cooperative and that you have permission to do this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '11, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Dec '11, 09:25</strong> </span></p></div></div><div id="comments-container-7970" class="comments-container"><span id="7971"></span><div id="comment-7971" class="comment"><div id="post-7971-score" class="comment-score"></div><div class="comment-text"><p>Yes I have permission to do this my friend is with me and we try many(login and log out) times because firstly we think not every packet were captured I also try on many website with http and one of mine</p></div><div id="comment-7971-info" class="comment-info"><span class="comment-age">(14 Dec '11, 09:33)</span> <span class="comment-user userinfo">vring6</span></div></div><span id="7973"></span><div id="comment-7973" class="comment"><div id="post-7973-score" class="comment-score"></div><div class="comment-text"><p>Sniffing your own traffic for your password can be a security test (e.g., to see whether an application is sending your password securely). On the other hand, sniffing for other people's passwords is almost always malicious, and IMO, there is no good reason to do it.</p></div><div id="comment-7973-info" class="comment-info"><span class="comment-age">(14 Dec '11, 09:57)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="7974"></span><div id="comment-7974" class="comment"><div id="post-7974-score" class="comment-score"></div><div class="comment-text"><p>where do you see i am sniffing people's password i am on my own network and my friend is on his laptop with me. I just want to prove that I can see password on http website on unsecure wifi network and for now I can't and I want to understand why because there is no encryption system and i can see where does he goes</p></div><div id="comment-7974-info" class="comment-info"><span class="comment-age">(14 Dec '11, 10:03)</span> <span class="comment-user userinfo">vring6</span></div></div></div><div id="comment-tools-7970" class="comment-tools"></div><div class="clear"></div><div id="comment-7970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

