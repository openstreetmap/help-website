+++
type = "question"
title = "Capture email packets"
description = '''Hi,  I am trying to capture email packets on my wired network but i dont get any. But alot of other network traffic is captured. The email client is hotmail. What might be the problem? :('''
date = "2013-04-11T02:36:00Z"
lastmod = "2013-04-11T05:41:00Z"
weight = 20312
keywords = [ "packets", "email" ]
aliases = [ "/questions/20312" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture email packets](/questions/20312/capture-email-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20312-score" class="post-score" title="current number of votes">0</div><span id="post-20312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to capture email packets on my wired network but i dont get any. But alot of other network traffic is captured. The email client is hotmail. What might be the problem? :(</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-email" rel="tag" title="see questions tagged &#39;email&#39;">email</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '13, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/5fea58481cbc3b8c4d30db7c29230b22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Metall&#39;s gravatar image" /><p><span>Metall</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Metall has no accepted answers">0%</span></p></div></div><div id="comments-container-20312" class="comments-container"></div><div id="comment-tools-20312" class="comment-tools"></div><div class="clear"></div><div id="comment-20312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20313"></span>

<div id="answer-container-20313" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20313-score" class="post-score" title="current number of votes">1</div><span id="post-20313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hotmail would mean that you access your email by web browser, which would mean that the data is transported via HTTP, not POP/IMAP, in case you're expecting these two protocols. Most likely Hotmail pages are also HTTPS, which means they're encrypted and non-readable unless you try to decrypt them.</p><p>What kind of traffic DO you see?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '13, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20313" class="comments-container"><span id="20317"></span><div id="comment-20317" class="comment"><div id="post-20317-score" class="comment-score"></div><div class="comment-text"><p>Because I saw a tutorial where this guy could see a packet called "POST" but when I do the same thing by sending an email to my self i don't see it. And I try to see this POST packet.</p><p>I can see HTTP, TCP, ARP, TLS, NBNS, SSDP AND IGMP packets</p></div><div id="comment-20317-info" class="comment-info"><span class="comment-age">(11 Apr '13, 03:00)</span> <span class="comment-user userinfo">Metall</span></div></div><span id="20320"></span><div id="comment-20320" class="comment"><div id="post-20320-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>TLS</p></blockquote><p>Do you connect to <strong>https</strong>://www.hotmail.com or to <strong>https</strong>://outlook.com (the successor of hotmail)? If so, think about the consequences for packet capturing ;-)</p></div><div id="comment-20320-info" class="comment-info"><span class="comment-age">(11 Apr '13, 03:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20324"></span><div id="comment-20324" class="comment"><div id="post-20324-score" class="comment-score"></div><div class="comment-text"><p>I connected to <a href="https://www.hotmail.com">https://www.hotmail.com</a>. But do this mean that I am not able to see the packets that runs over SSL?</p></div><div id="comment-20324-info" class="comment-info"><span class="comment-age">(11 Apr '13, 03:55)</span> <span class="comment-user userinfo">Metall</span></div></div><span id="20329"></span><div id="comment-20329" class="comment"><div id="post-20329-score" class="comment-score">1</div><div class="comment-text"><p>Correct, SSL traffic is (usually) encrypted. So, unless you can persuade the folks at Hotmail to hand over the private key they use for their SSL connections you won't be able to decrypt the data.</p></div><div id="comment-20329-info" class="comment-info"><span class="comment-age">(11 Apr '13, 05:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="20330"></span><div id="comment-20330" class="comment not_top_scorer"><div id="post-20330-score" class="comment-score"></div><div class="comment-text"><p>But shouldn't I be able just to see the packet? Even though they are encrypted?</p></div><div id="comment-20330-info" class="comment-info"><span class="comment-age">(11 Apr '13, 05:37)</span> <span class="comment-user userinfo">Metall</span></div></div><span id="20331"></span><div id="comment-20331" class="comment"><div id="post-20331-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I am not able to see the packets that runs over SSL?</p></blockquote><p>No, you will see the packet, but you can't decipher the payload as it is encrypted. As you mentioned TLS, I guess those are the Hotmail packets (TLS is the successor of SSL).</p></div><div id="comment-20331-info" class="comment-info"><span class="comment-age">(11 Apr '13, 05:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20313" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-20313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

