+++
type = "question"
title = "Bandwidth Throttling, Emulating"
description = '''Hi, I know this question is not wireshark related, but i am looking for a piece of software to dynamically simulate bandwidth speeds.  Thanks in advanced.'''
date = "2014-04-08T04:01:00Z"
lastmod = "2014-04-09T13:50:00Z"
weight = 31621
keywords = [ "bandwidth", "emulation", "throttling" ]
aliases = [ "/questions/31621" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Bandwidth Throttling, Emulating](/questions/31621/bandwidth-throttling-emulating)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31621-score" class="post-score" title="current number of votes">0</div><span id="post-31621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I know this question is not wireshark related, but i am looking for a piece of software to dynamically simulate bandwidth speeds.</p><p>Thanks in advanced.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-emulation" rel="tag" title="see questions tagged &#39;emulation&#39;">emulation</span> <span class="post-tag tag-link-throttling" rel="tag" title="see questions tagged &#39;throttling&#39;">throttling</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '14, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/140fe8da9d189e180c3927c9a61dc09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimmy967&#39;s gravatar image" /><p><span>jimmy967</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimmy967 has no accepted answers">0%</span></p></div></div><div id="comments-container-31621" class="comments-container"></div><div id="comment-tools-31621" class="comment-tools"></div><div class="clear"></div><div id="comment-31621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="31622"></span>

<div id="answer-container-31622" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31622-score" class="post-score" title="current number of votes">1</div><span id="post-31622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Easiest way to do this is to use NetEm, which is included in most Linux kernels already.</p><p>See <a href="http://www.linuxfoundation.org/collaborate/workgroups/networking/netem">http://www.linuxfoundation.org/collaborate/workgroups/networking/netem</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '14, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31622" class="comments-container"><span id="31624"></span><div id="comment-31624" class="comment"><div id="post-31624-score" class="comment-score"></div><div class="comment-text"><p>im running the client on a windows 8.0 os</p></div><div id="comment-31624-info" class="comment-info"><span class="comment-age">(08 Apr '14, 04:07)</span> <span class="comment-user userinfo">jimmy967</span></div></div><span id="31625"></span><div id="comment-31625" class="comment"><div id="post-31625-score" class="comment-score"></div><div class="comment-text"><p>You'll most likely have to use a proxy service that can throttle the connection. I'd go for a VM running Linux with NetEm and route the traffic through it. I guess there are also a couple of Windows tools that do this, but I haven't checked.</p></div><div id="comment-31625-info" class="comment-info"><span class="comment-age">(08 Apr '14, 04:11)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="31630"></span><div id="comment-31630" class="comment"><div id="post-31630-score" class="comment-score"></div><div class="comment-text"><p>okay, thanks alot</p></div><div id="comment-31630-info" class="comment-info"><span class="comment-age">(08 Apr '14, 05:02)</span> <span class="comment-user userinfo">jimmy967</span></div></div></div><div id="comment-tools-31622" class="comment-tools"></div><div class="clear"></div><div id="comment-31622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31672"></span>

<div id="answer-container-31672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31672-score" class="post-score" title="current number of votes">0</div><span id="post-31672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another very good traffic shaping tool is FreeBSD's <a href="http://www.freebsd.org/cgi/man.cgi?query=dummynet&amp;sektion=4">dummynet</a> (part of their ipfw firewall stuff). I used it for years and it was <em>rock solid</em> (as FreeBSD typically is).</p><p>Of course it doesn't directly help you on Windows, but there's probably no free software to do this on Windows. (I'm pretty sure there are commercial vendors which run on Windows; I think Shunra at least used to make an "IP cloud" product.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '14, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-31672" class="comments-container"></div><div id="comment-tools-31672" class="comment-tools"></div><div class="clear"></div><div id="comment-31672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31687"></span>

<div id="answer-container-31687" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31687-score" class="post-score" title="current number of votes">0</div><span id="post-31687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Other tools are:</p><p>eEx Netlab - Windows: <a href="http://www.eex-dev.net/index.php?id=38&amp;L=1">http://www.eex-dev.net/index.php?id=38&amp;L=1</a><br />
WANem - Ready-to-go Linux appliance: <a href="http://wanem.sourceforge.net/">http://wanem.sourceforge.net/</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '14, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-31687" class="comments-container"></div><div id="comment-tools-31687" class="comment-tools"></div><div class="clear"></div><div id="comment-31687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

