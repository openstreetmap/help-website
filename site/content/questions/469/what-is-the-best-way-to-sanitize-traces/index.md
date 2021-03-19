+++
type = "question"
title = "What is the best way to sanitize traces?"
description = '''I can use the “Limit each packet to N bytes” capture option to make sure that application data is not captured, or editcap -s to remove already captured application data. But how do I change the IP addresses. I would like to maintain the relationships between IP addresses, that is addresses in the s...'''
date = "2010-10-10T07:05:00Z"
lastmod = "2010-10-12T07:20:00Z"
weight = 469
keywords = [ "privatize", "anonymize", "sanitize" ]
aliases = [ "/questions/469" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is the best way to sanitize traces?](/questions/469/what-is-the-best-way-to-sanitize-traces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-469-score" class="post-score" title="current number of votes">0</div><span id="post-469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can use the “Limit each packet to N bytes” capture option to make sure that application data is not captured, or editcap -s to remove already captured application data. But how do I change the IP addresses. I would like to maintain the relationships between IP addresses, that is addresses in the same subnet/network remain in the same subnet/network. I don't require that the addresses be changed to the standard private address space, just that they no longer reflect my addresses.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-privatize" rel="tag" title="see questions tagged &#39;privatize&#39;">privatize</span> <span class="post-tag tag-link-anonymize" rel="tag" title="see questions tagged &#39;anonymize&#39;">anonymize</span> <span class="post-tag tag-link-sanitize" rel="tag" title="see questions tagged &#39;sanitize&#39;">sanitize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '10, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/69a9d59a9709d6c6ba0d47409e89c90f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="noah&#39;s gravatar image" /><p><span>noah</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="noah has no accepted answers">0%</span></p></div></div><div id="comments-container-469" class="comments-container"></div><div id="comment-tools-469" class="comment-tools"></div><div class="clear"></div><div id="comment-469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="470"></span>

<div id="answer-container-470" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-470-score" class="post-score" title="current number of votes">2</div><span id="post-470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="noah has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://bittwist.sourceforge.net/index.html">bittwiste.1</a> - <a href="http://bittwist.sourceforge.net/doc.html">pcap capture file editor</a><br />
You can find more information in the <a href="http://bittwist.sourceforge.net/doc/bittwiste.1.html">man-page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '10, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></p></div></div><div id="comments-container-470" class="comments-container"><span id="471"></span><div id="comment-471" class="comment"><div id="post-471-score" class="comment-score"></div><div class="comment-text"><p>Thanks that looks like it will do what I want.</p></div><div id="comment-471-info" class="comment-info"><span class="comment-age">(10 Oct '10, 11:19)</span> <span class="comment-user userinfo">noah</span></div></div><span id="486"></span><div id="comment-486" class="comment"><div id="post-486-score" class="comment-score"></div><div class="comment-text"><p>bit-twist is a great tool!</p></div><div id="comment-486-info" class="comment-info"><span class="comment-age">(12 Oct '10, 06:07)</span> <span class="comment-user userinfo">GeonJay</span></div></div></div><div id="comment-tools-470" class="comment-tools"></div><div class="clear"></div><div id="comment-470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="473"></span>

<div id="answer-container-473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-473-score" class="post-score" title="current number of votes">1</div><span id="post-473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just a note of caution here -</p><p>bittwiste's IP address replacement does not go further than the IP header to sanitize the IP addresses - so watch out for packets that may contain the original IP addresses embedded further along - for example - watch out for the 227 response to an FTP PASV command or the FTP PORT command packets. Typically - if I absolutely have to ensure the original IP address is not somewhere in the trace file, I open it with a hex editor and search/replace throughout. This won't recalculate the checksums for you and you might consider disabing the checksum coloring rule because of that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '10, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-473" class="comments-container"><span id="474"></span><div id="comment-474" class="comment"><div id="post-474-score" class="comment-score"></div><div class="comment-text"><p>Yes, HxD, freeware Hex Editor and Disk Editor, can do this job perfectly:<br />
http://mh-nexus.de/en/hxd/</p><p>But then you have to be aware of other sensitive information in the capture file.<br />
The OP has already truncated the packets.</p></div><div id="comment-474-info" class="comment-info"><span class="comment-age">(11 Oct '10, 00:52)</span> <span class="comment-user userinfo">joke</span></div></div><span id="488"></span><div id="comment-488" class="comment"><div id="post-488-score" class="comment-score"></div><div class="comment-text"><blockquote><p>This won't recalculate the checksums for you...</p></blockquote><p>But Wireshark can, so load your capture, see what it says it should be, hexedit, rinse and repeat.</p></div><div id="comment-488-info" class="comment-info"><span class="comment-age">(12 Oct '10, 07:20)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-473" class="comment-tools"></div><div class="clear"></div><div id="comment-473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

