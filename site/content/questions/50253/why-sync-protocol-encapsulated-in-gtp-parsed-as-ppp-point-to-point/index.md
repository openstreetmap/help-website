+++
type = "question"
title = "Why Sync protocol encapsulated in GTP parsed as PPP (point to point)?"
description = '''I have a tcpdump (.pcap) and I wonder why sync (MBMS synchronization protocol) encapsulated inside GTP is parsed by Wireshark as PPP? link to image If image is not loading, please see this link instead: https://drive.google.com/open?id=0ByOndV1AGUP1SXB5ck8taE4yZGc'''
date = "2016-02-17T00:00:00Z"
lastmod = "2016-02-17T17:51:00Z"
weight = 50253
keywords = [ "gtp", "ppp", "tcpdump", "sync" ]
aliases = [ "/questions/50253" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why Sync protocol encapsulated in GTP parsed as PPP (point to point)?](/questions/50253/why-sync-protocol-encapsulated-in-gtp-parsed-as-ppp-point-to-point)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50253-score" class="post-score" title="current number of votes">0</div><span id="post-50253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a tcpdump (.pcap) and I wonder why sync (MBMS synchronization protocol) encapsulated inside GTP is parsed by Wireshark as PPP?</p><p><a href="https://drive.google.com/open?id=0ByOndV1AGUP1SXB5ck8taE4yZGc">link to image</a></p><p>If image is not loading, please see this link instead: <a href="https://drive.google.com/open?id=0ByOndV1AGUP1SXB5ck8taE4yZGc">https://drive.google.com/open?id=0ByOndV1AGUP1SXB5ck8taE4yZGc</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gtp" rel="tag" title="see questions tagged &#39;gtp&#39;">gtp</span> <span class="post-tag tag-link-ppp" rel="tag" title="see questions tagged &#39;ppp&#39;">ppp</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-sync" rel="tag" title="see questions tagged &#39;sync&#39;">sync</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '16, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/ca02d0b4dedd058552f233c010585a1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fearfox&#39;s gravatar image" /><p><span>fearfox</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fearfox has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '16, 00:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-50253" class="comments-container"><span id="50255"></span><div id="comment-50255" class="comment"><div id="post-50255-score" class="comment-score"></div><div class="comment-text"><p>Post a link to a pcap file with the packet instead so we can find out what's wrong.</p></div><div id="comment-50255-info" class="comment-info"><span class="comment-age">(17 Feb '16, 00:55)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="50261"></span><div id="comment-50261" class="comment"><div id="post-50261-score" class="comment-score"></div><div class="comment-text"><p>here is a link yo pcap file: <a href="https://drive.google.com/file/d/0ByOndV1AGUP1ajlEZjRab3FvQTg/view?usp=sharing">https://drive.google.com/file/d/0ByOndV1AGUP1ajlEZjRab3FvQTg/view?usp=sharing</a></p></div><div id="comment-50261-info" class="comment-info"><span class="comment-age">(17 Feb '16, 03:20)</span> <span class="comment-user userinfo">fearfox</span></div></div></div><div id="comment-tools-50253" class="comment-tools"></div><div class="clear"></div><div id="comment-50253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50263"></span>

<div id="answer-container-50263" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50263-score" class="post-score" title="current number of votes">1</div><span id="post-50263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fearfox has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to GTP protocol preferences (<code>Edit -&gt; Preferences -&gt; Protocols -&gt; GTP</code>) and change the <code>Dissect T-PDU as</code> setting from the default value <code>TPDU</code> to <code>SYNC</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '16, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '16, 04:42</strong> </span></p></div></div><div id="comments-container-50263" class="comments-container"><span id="50287"></span><div id="comment-50287" class="comment"><div id="post-50287-score" class="comment-score"></div><div class="comment-text"><p>wonderful! it worked! Thank you :)</p></div><div id="comment-50287-info" class="comment-info"><span class="comment-age">(17 Feb '16, 17:51)</span> <span class="comment-user userinfo">fearfox</span></div></div></div><div id="comment-tools-50263" class="comment-tools"></div><div class="clear"></div><div id="comment-50263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

