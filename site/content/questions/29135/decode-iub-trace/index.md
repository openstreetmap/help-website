+++
type = "question"
title = "Decode IuB Trace"
description = '''Hi, In the given trace present at pcapr, I was able to decode nbap, but most of the FP/MAC/RLC packets are throwing exceptions. Is it possible to see the RRC packets with any particular settings?? http://www.pcapr.net/view/nos/2011/3/1/13/iub_over_udp_nbap_and_rrc.html Regards, Vineeth'''
date = "2014-01-24T03:09:00Z"
lastmod = "2015-01-14T01:09:00Z"
weight = 29135
keywords = [ "mac", "iub", "rrc", "rlc" ]
aliases = [ "/questions/29135" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decode IuB Trace](/questions/29135/decode-iub-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29135-score" class="post-score" title="current number of votes">0</div><span id="post-29135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In the given trace present at pcapr, I was able to decode nbap, but most of the FP/MAC/RLC packets are throwing exceptions. Is it possible to see the RRC packets with any particular settings??</p><p><a href="http://www.pcapr.net/view/nos/2011/3/1/13/iub_over_udp_nbap_and_rrc.html">http://www.pcapr.net/view/nos/2011/3/1/13/iub_over_udp_nbap_and_rrc.html</a></p><p>Regards, Vineeth</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-iub" rel="tag" title="see questions tagged &#39;iub&#39;">iub</span> <span class="post-tag tag-link-rrc" rel="tag" title="see questions tagged &#39;rrc&#39;">rrc</span> <span class="post-tag tag-link-rlc" rel="tag" title="see questions tagged &#39;rlc&#39;">rlc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '14, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/6b9ae8a749ec26d7d2cbb3507068861f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vineeth&#39;s gravatar image" /><p><span>Vineeth</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vineeth has no accepted answers">0%</span></p></div></div><div id="comments-container-29135" class="comments-container"></div><div id="comment-tools-29135" class="comment-tools"></div><div class="clear"></div><div id="comment-29135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39120"></span>

<div id="answer-container-39120" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39120-score" class="post-score" title="current number of votes">0</div><span id="post-39120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>FP/MAC/RLC are automatically dissected. But beware that UMTS security design is not allowing to see Iub messages after cyphering (i.e. authentication and security procedure right after RRC Connection Setup Complete and Direct Transfer messages to Core Network) if encryption algorithm is activated in Core Network. Check that first, and then verify that EA1 is not used, then you should be able to see RRC protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '15, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/16b27fade385db77779abdca9686591e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fedemone&#39;s gravatar image" /><p><span>Fedemone</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fedemone has no accepted answers">0%</span></p></div></div><div id="comments-container-39120" class="comments-container"></div><div id="comment-tools-39120" class="comment-tools"></div><div class="clear"></div><div id="comment-39120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

