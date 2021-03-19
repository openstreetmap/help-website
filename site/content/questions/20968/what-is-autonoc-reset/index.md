+++
type = "question"
title = "What is autonoc reset?"
description = '''Hi, Wireshark is outputing a black background with pink(?) letters with this: [TCP Dup ACK] http -&amp;gt; autonoc [ACK] seq=597 ack=672 win=67000 And just bellow, follow a red background with yellow letters with this:  autonoc -&amp;gt; http [RST] seq=672 win=0 len=0 What could be this?'''
date = "2013-05-05T14:14:00Z"
lastmod = "2013-05-05T14:33:00Z"
weight = 20968
keywords = [ "autonoc", "reset" ]
aliases = [ "/questions/20968" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is autonoc reset?](/questions/20968/what-is-autonoc-reset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20968-score" class="post-score" title="current number of votes">0</div><span id="post-20968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Wireshark is outputing a black background with pink(?) letters with this:</p><p>[TCP Dup ACK] http -&gt; autonoc [ACK] seq=597 ack=672 win=67000</p><p>And just bellow, follow a red background with yellow letters with this:</p><p>autonoc -&gt; http [RST] seq=672 win=0 len=0</p><p>What could be this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-autonoc" rel="tag" title="see questions tagged &#39;autonoc&#39;">autonoc</span> <span class="post-tag tag-link-reset" rel="tag" title="see questions tagged &#39;reset&#39;">reset</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '13, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/91c9e20ad21c3397d085a7f2a8b4bac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skd&#39;s gravatar image" /><p><span>skd</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skd has no accepted answers">0%</span></p></div></div><div id="comments-container-20968" class="comments-container"></div><div id="comment-tools-20968" class="comment-tools"></div><div class="clear"></div><div id="comment-20968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20970"></span>

<div id="answer-container-20970" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20970-score" class="post-score" title="current number of votes">1</div><span id="post-20970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="skd has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jasper there is nothing particularly unusual or sinister here. There are a couple of things that probably threw you though:-</p><ol><li>Wireshark tries to convert TCP and UDP ports to the names that were registered for these numbers with the IANA registry. So TCP port 80 became http and TCP port 1140 became autonoc.</li><li>While http is useful in this case (helping us know the server was probably a web server), autonoc is probably not. When a client establishes a connection to a server it usually chooses a "random" port with a high number (above 1024), called an ephemeral port, for the connection. In this case your client chose 1140. So converting it to autonoc really is incorrect, as it would only make sense if this TCP port was on the server side.</li><li>The "Dup ACK" is probably just the server wanting to see some more action from the client. The followup action from the client though is the RST (reset), which means it is done with that conversation. So all good and normal TCP.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '13, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-20970" class="comments-container"></div><div id="comment-tools-20970" class="comment-tools"></div><div class="clear"></div><div id="comment-20970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20969"></span>

<div id="answer-container-20969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20969-score" class="post-score" title="current number of votes">1</div><span id="post-20969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nothing special, just color markers for a duplicate ACK and a TCP reset packet. Which is all basic TCP stuff, so if you want to know more about that you need to study how TCP works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '13, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20969" class="comments-container"></div><div id="comment-tools-20969" class="comment-tools"></div><div class="clear"></div><div id="comment-20969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

