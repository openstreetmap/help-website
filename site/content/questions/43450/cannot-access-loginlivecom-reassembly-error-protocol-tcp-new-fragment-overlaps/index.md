+++
type = "question"
title = "Cannot access login.live.com - &quot;Reassembly error, protocol TCP: New fragment overlaps...&quot;"
description = '''Hi, I have an issue with a client who has a server hosted with a third party provider. They have recently have their server moved (still within the same company) as they needed the server to be under their own account and not their old IT providers&#x27; account. Ever since the migration, the customer ca...'''
date = "2015-06-22T10:22:00Z"
lastmod = "2015-06-24T03:57:00Z"
weight = 43450
keywords = [ "443", "reassembly", "tcp", "https", "error" ]
aliases = [ "/questions/43450" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot access login.live.com - "Reassembly error, protocol TCP: New fragment overlaps..."](/questions/43450/cannot-access-loginlivecom-reassembly-error-protocol-tcp-new-fragment-overlaps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43450-score" class="post-score" title="current number of votes">0</div><span id="post-43450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have an issue with a client who has a server hosted with a third party provider. They have recently have their server moved (still within the same company) as they needed the server to be under their own account and not their old IT providers' account. Ever since the migration, the customer cannot access Hotmail. I have tried Gmail and AOL and a bunch of other HTTPS sites but for some reason I can only find an issue with them accessing Hotmail. What is happening is when they go to Hotmail, they are redirected to login.live.com (as you'd expect) but accessing the page is intermittent and so far I have not been able to log in successfully once. I have ran Wireshark and followed the TCP stream for this particular conversation but I am unsure what the output actually means. I see we get a packet that says [TCP Retransmission] and then after that the connection is reset.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Untitled2_DNy2khp.png" alt="alt text" /></p><p>Any help on this would be fantastic please.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-443" rel="tag" title="see questions tagged &#39;443&#39;">443</span> <span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '15, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/8ac8aaabcf360cef154c972fb2a2292a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonathanbaird&#39;s gravatar image" /><p><span>jonathanbaird</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonathanbaird has one accepted answer">50%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jun '15, 12:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-43450" class="comments-container"><span id="43457"></span><div id="comment-43457" class="comment"><div id="post-43457-score" class="comment-score"></div><div class="comment-text"><p>Do I understand right, that you are connected to a totally wrong destination?</p></div><div id="comment-43457-info" class="comment-info"><span class="comment-age">(22 Jun '15, 12:13)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-43450" class="comment-tools"></div><div class="clear"></div><div id="comment-43450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43497"></span>

<div id="answer-container-43497" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43497-score" class="post-score" title="current number of votes">0</div><span id="post-43497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jonathanbaird has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Kurt,</p><p>Thanks for your response. It turns out that the server NIC had TCP offloading enabled which was causing the issues. Disabling this resolved the issue immediately. Very odd! Thanks for your help anyway.</p><p>Jonathan.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '15, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/8ac8aaabcf360cef154c972fb2a2292a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonathanbaird&#39;s gravatar image" /><p><span>jonathanbaird</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonathanbaird has one accepted answer">50%</span></p></div></div><div id="comments-container-43497" class="comments-container"></div><div id="comment-tools-43497" class="comment-tools"></div><div class="clear"></div><div id="comment-43497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43468"></span>

<div id="answer-container-43468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43468-score" class="post-score" title="current number of votes">1</div><span id="post-43468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your screenshot shows a HTTPS session to the IP 131.253.61.82, which is one of the IPs of login.live.com, so at least you are talking to the right server. However, the problem with your capture file is, that there is (most certainly) TCP segment offloading enabled on the server (frames &gt; 1500 bytes), which makes it hard to do any TCP sequence analysis, especially based on a screenshot.</p><blockquote><p>but accessing the page is intermittent and so far I have not been able to log in successfully once.</p></blockquote><p>What do you mean by that? You enter the user credentials, and then page loading stalls, or do you get an error message?</p><p>If it's an error message: What's the message?</p><p>If that page stalls, my best <strong>guess</strong> would be that there is some kind of security software on that system (AV, Endpoint Security, etc.) that hooks itself into the data stream to scan internet downloads and something goes wrong. Please check that and disable any security software for another test with Hotmail.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '15, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43468" class="comments-container"><span id="43473"></span><div id="comment-43473" class="comment"><div id="post-43473-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>Thanks for your reply. Yes indeed I do get to the correct server, the issue is that when I type ANY login details to log in I just get a "no response from server" in Chrome and similar messages in Firefox and IE. Sophos was installed on this PC but this has been completely uninstalled and there is no other AV running on here.</p><p>I'll check if there is any other security related software running and see if I can disable this. It is just very odd that it only happens with login.live.com.</p><p>P.S. Where did you see the destination IP!? I though I'd removed everything - purely for confidentiality that's all! :)</p></div><div id="comment-43473-info" class="comment-info"><span class="comment-age">(23 Jun '15, 01:17)</span> <span class="comment-user userinfo">jonathanbaird</span></div></div><span id="43474"></span><div id="comment-43474" class="comment"><div id="post-43474-score" class="comment-score"></div><div class="comment-text"><p>he got the ip from the hex view</p></div><div id="comment-43474-info" class="comment-info"><span class="comment-age">(23 Jun '15, 01:29)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="43480"></span><div id="comment-43480" class="comment"><div id="post-43480-score" class="comment-score"></div><div class="comment-text"><p>Well, if it's not a security software on your system, it could be a security device (firewall) in the network. Did you check that as well?</p></div><div id="comment-43480-info" class="comment-info"><span class="comment-age">(23 Jun '15, 11:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-43468" class="comment-tools"></div><div class="clear"></div><div id="comment-43468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

