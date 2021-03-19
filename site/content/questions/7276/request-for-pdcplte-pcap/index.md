+++
type = "question"
title = "Request for PDCP(LTE) pcap"
description = '''Hi Sir/Madam, I am looking for PDCP pcap (for using LTE protocol stack). Please help me in providing the same. PDCP should include ROHC and encryption (either AES or SNOW3G). Regards, Sreekanth'''
date = "2011-11-08T03:52:00Z"
lastmod = "2011-11-11T07:28:00Z"
weight = 7276
keywords = [ "pdcp", "lte" ]
aliases = [ "/questions/7276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Request for PDCP(LTE) pcap](/questions/7276/request-for-pdcplte-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7276-score" class="post-score" title="current number of votes">0</div><span id="post-7276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Sir/Madam,</p><p>I am looking for PDCP pcap (for using LTE protocol stack). Please help me in providing the same. PDCP should include ROHC and encryption (either AES or SNOW3G).</p><p>Regards, Sreekanth</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pdcp" rel="tag" title="see questions tagged &#39;pdcp&#39;">pdcp</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '11, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/d9288d489c9ff9a3208243967ebab9bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="v_sreekanth&#39;s gravatar image" /><p><span>v_sreekanth</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="v_sreekanth has no accepted answers">0%</span></p></div></div><div id="comments-container-7276" class="comments-container"></div><div id="comment-tools-7276" class="comment-tools"></div><div class="clear"></div><div id="comment-7276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7286"></span>

<div id="answer-container-7286" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7286-score" class="post-score" title="current number of votes">0</div><span id="post-7286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If by "pcap" you mean "link-layer header type value for pcap and pcap-ng file formats", the Wireshark developers don't assign them, the libpcap/tcpdump developers do; please send a mail message to <a href="http://www.tcpdump.org/#patches">the tcpdump-workers mailing list</a> asking for a new link-layer header type value. Indicate what format the packets have, including any metadata preceding the PDCP header.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '11, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7286" class="comments-container"><span id="7382"></span><div id="comment-7382" class="comment"><div id="post-7382-score" class="comment-score"></div><div class="comment-text"><p>The other possibility would be normal ethernet pcap that captured the UDP framing method described in http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-pdcp-lte.h that can be generated in the same way that the example program referenced by http://wiki.wireshark.org/PDCP-LTE does (see http://www.wireshark.org/~martinm/pdcp_lte_logger.c).</p><p>I don't have any such captures. The dissector currently has limited support for ROHC and no support for ciphering.</p></div><div id="comment-7382-info" class="comment-info"><span class="comment-age">(11 Nov '11, 07:28)</span> <span class="comment-user userinfo">MartinM</span></div></div></div><div id="comment-tools-7286" class="comment-tools"></div><div class="clear"></div><div id="comment-7286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

