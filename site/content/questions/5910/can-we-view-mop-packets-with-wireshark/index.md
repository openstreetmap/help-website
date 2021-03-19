+++
type = "question"
title = "can we view MOP packets with wireshark"
description = '''I&#x27;m trying to capture some Maintenance Operation Protocol (MOP) related packets from a router. but when i go to the filter section in wireshark, it does not have MOP listed under the protocols list. Is there any specific wireshark version where i can get MOP as filter option. or is there any other w...'''
date = "2011-08-29T00:18:00Z"
lastmod = "2011-08-29T16:35:00Z"
weight = 5910
keywords = [ "mop", "filters" ]
aliases = [ "/questions/5910" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can we view MOP packets with wireshark](/questions/5910/can-we-view-mop-packets-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5910-score" class="post-score" title="current number of votes">0</div><span id="post-5910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture some Maintenance Operation Protocol (MOP) related packets from a router. but when i go to the filter section in wireshark, it does not have MOP listed under the protocols list. Is there any specific wireshark version where i can get MOP as filter option. or is there any other work around?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mop" rel="tag" title="see questions tagged &#39;mop&#39;">mop</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '11, 00:18</strong></p><img src="https://secure.gravatar.com/avatar/31da490116683ddda60643c483f481d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="realm_wrecker&#39;s gravatar image" /><p><span>realm_wrecker</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="realm_wrecker has no accepted answers">0%</span></p></div></div><div id="comments-container-5910" class="comments-container"><span id="5914"></span><div id="comment-5914" class="comment"><div id="post-5914-score" class="comment-score"></div><div class="comment-text"><p>What kind of router ?</p><p>MOP is the name of an old Digital Network Architecture proprietary protocol; I wouldn't really have expected to see much of this protocol any more...</p><p>http://en.wikipedia.org/wiki/Maintenance_Operations_Protocol</p><p>http://www.cisco.com/en/US/tech/tk870/tk136/tk885/technologies_tech_note09186a0080093cd1.shtml</p></div><div id="comment-5914-info" class="comment-info"><span class="comment-age">(29 Aug '11, 06:48)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="5917"></span><div id="comment-5917" class="comment"><div id="post-5917-score" class="comment-score"></div><div class="comment-text"><p>Hi Bill, It's an edge router i'm using. Yes, MOP is quite old, you're right about that. that isn't my question. My question is whether there's any way we can filter (from a capture file of several packets), and look at mop packets only. when i tried doing this is when i realised, wireshark doesn't have MOP in it's list of protocol filters. is there any extended filter set/ patch i can add to wiresark, so the intent is achieved?</p><p>one idea that just dawned on me now, is to use the reserved mcast addresses as a filter criterion. let me try that.</p></div><div id="comment-5917-info" class="comment-info"><span class="comment-age">(29 Aug '11, 08:02)</span> <span class="comment-user userinfo">realm_wrecker</span></div></div><span id="5920"></span><div id="comment-5920" class="comment"><div id="post-5920-score" class="comment-score"></div><div class="comment-text"><p>or: use tshark -R "eth.type == 0x6001" ...</p></div><div id="comment-5920-info" class="comment-info"><span class="comment-age">(29 Aug '11, 09:44)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-5910" class="comment-tools"></div><div class="clear"></div><div id="comment-5910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5912"></span>

<div id="answer-container-5912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5912-score" class="post-score" title="current number of votes">0</div><span id="post-5912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK, Wireshark recognizes ethertype 0x6001 as "DEC DNA Dump/Load", but there's no dissector for it. You can file an enhancement bug report at <a href="https://bugs.wireshark.org">bugzilla</a>, attaching a sample capture file and reference to the specification, in order to invite someone to write a dissector for it. Or you may want to try yourself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '11, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5912" class="comments-container"><span id="5918"></span><div id="comment-5918" class="comment"><div id="post-5918-score" class="comment-score"></div><div class="comment-text"><p>THanks jap, i'll try that</p></div><div id="comment-5918-info" class="comment-info"><span class="comment-age">(29 Aug '11, 08:03)</span> <span class="comment-user userinfo">realm_wrecker</span></div></div><span id="5934"></span><div id="comment-5934" class="comment"><div id="post-5934-score" class="comment-score"></div><div class="comment-text"><p>The specification is <a href="http://h71000.www7.hp.com/wizard/decnet/maintop30.txt">here</a>.</p></div><div id="comment-5934-info" class="comment-info"><span class="comment-age">(29 Aug '11, 16:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-5912" class="comment-tools"></div><div class="clear"></div><div id="comment-5912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

