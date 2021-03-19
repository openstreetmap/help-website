+++
type = "question"
title = "INAP-ETC on wireshark"
description = '''Hi, pls go through the below link,  https://www.cloudshark.org/captures/addc482b811d In the above tracer assistingSSPIPRoutingAddress field value as 1203198974795017. Wireshark tracer showing as single parameter where as in MSC tracer showing the first 5 digits as separated parameters like NAI,NPI ....'''
date = "2014-03-09T21:23:00Z"
lastmod = "2014-03-09T22:42:00Z"
weight = 30628
keywords = [ "camel" ]
aliases = [ "/questions/30628" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [INAP-ETC on wireshark](/questions/30628/inap-etc-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30628-score" class="post-score" title="current number of votes">0</div><span id="post-30628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>pls go through the below link, <a href="https://www.cloudshark.org/captures/addc482b811d">https://www.cloudshark.org/captures/addc482b811d</a></p><p>In the above tracer assistingSSPIPRoutingAddress field value as 1203198974795017. Wireshark tracer showing as single parameter where as in MSC tracer showing the first 5 digits as separated parameters like NAI,NPI ...etc.</p><p>Is it possible to read in wireshark that all the parameters shown same as MSC tracer ??</p><p>Hanosh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-camel" rel="tag" title="see questions tagged &#39;camel&#39;">camel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '14, 21:23</strong></p><img src="https://secure.gravatar.com/avatar/947b7a306a061178060e0e2a11b93d81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hanosh&#39;s gravatar image" /><p><span>Hanosh</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hanosh has no accepted answers">0%</span></p></div></div><div id="comments-container-30628" class="comments-container"></div><div id="comment-tools-30628" class="comment-tools"></div><div class="clear"></div><div id="comment-30628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30629"></span>

<div id="answer-container-30629" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30629-score" class="post-score" title="current number of votes">0</div><span id="post-30629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark uses the ASN.1 definition files provided by 3GPP for Camel (in particular, 3GPP 29.078 release 7.3.0). I thought maybe it just didn't parse the details of assistingSSPIPRoutingAddress because the 3GPP release it's using is so old, but nope - even release 11 doesn't specify the details of assistingSSPIPRoutingAddress as anything but raw digits. The <em>comments</em> in the ASN file specify it to be a Generic Number, which has NAI/NPI/etc., but the definition doesn't specify that. That makes it pretty annoying to fix. :(</p><p>I suggest you submit an enhancement request to <a href="https://bugs.wireshark.org/bugzilla/">bugs.wireshark.org</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '14, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30629" class="comments-container"></div><div id="comment-tools-30629" class="comment-tools"></div><div class="clear"></div><div id="comment-30629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

