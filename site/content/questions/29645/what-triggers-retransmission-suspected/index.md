+++
type = "question"
title = "What triggers Retransmission (suspected)?"
description = '''PCAP link A newbie to Wireshark, I need a glimmer of understanding to debug a LAN. The PCAP was taken at firebox. (Please see config. at my initial question..) TIA, kirby'''
date = "2014-02-10T10:47:00Z"
lastmod = "2014-11-08T11:31:00Z"
weight = 29645
keywords = [ "suspect", "retransmission" ]
aliases = [ "/questions/29645" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What triggers Retransmission (suspected)?](/questions/29645/what-triggers-retransmission-suspected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29645-score" class="post-score" title="current number of votes">0</div><span id="post-29645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><h3 id="pcap-link"><a href="https://www.dropbox.com/s/xfiis5rb5n7eoho/shark-kd.pcapng.gz">PCAP link</a></h3><p>A newbie to Wireshark, I need a glimmer of understanding to debug a LAN.<br />
The PCAP was taken at <em>firebox.</em> (Please see config. at my <a href="http://ask.wireshark.org/questions/29582/do-browsers-treat-http-links-differently-from-manually-entered-urls">initial question.</a>.)<br />
TIA,<br />
kirby</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-suspect" rel="tag" title="see questions tagged &#39;suspect&#39;">suspect</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '14, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/d77229ae8593144da6d67d910697141b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kirby&#39;s gravatar image" /><p><span>kirby</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kirby has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-29645" class="comments-container"><span id="29648"></span><div id="comment-29648" class="comment"><div id="post-29648-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Please see config. at my initial question..</p></blockquote><p>you did not answer my comment, so we still don't know what your problem might be !??! Not a good position, if you want any further help ;-)</p></div><div id="comment-29648-info" class="comment-info"><span class="comment-age">(10 Feb '14, 11:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29708"></span><div id="comment-29708" class="comment"><div id="post-29708-score" class="comment-score"></div><div class="comment-text"><p>'Sorry Kurt. I did not see your comment.</p></div><div id="comment-29708-info" class="comment-info"><span class="comment-age">(11 Feb '14, 10:09)</span> <span class="comment-user userinfo">kirby</span></div></div></div><div id="comment-tools-29645" class="comment-tools"></div><div class="clear"></div><div id="comment-29645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29662"></span>

<div id="answer-container-29662" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29662-score" class="post-score" title="current number of votes">0</div><span id="post-29662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Retransmissions are triggered by duplicate acks or a retransmission timer expiring. In your case it's the client asking for the same segment over and over. The server's retransmitted segments never arrive at the client though - when they are a full MSS 1460 in size. See my answer to your original question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-29662" class="comments-container"><span id="37701"></span><div id="comment-37701" class="comment"><div id="post-37701-score" class="comment-score"></div><div class="comment-text"><p>how do you stop this im getting a lot of that</p></div><div id="comment-37701-info" class="comment-info"><span class="comment-age">(08 Nov '14, 11:31)</span> <span class="comment-user userinfo">MostUnlikedO...</span></div></div></div><div id="comment-tools-29662" class="comment-tools"></div><div class="clear"></div><div id="comment-29662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

