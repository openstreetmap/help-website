+++
type = "question"
title = "SCTP Association Algorithm"
description = '''I&#x27;m trying to write a python module for determining SCTP associations from captured traffic. It works fine when I read a pcap that has SACK chunks (since my heuristic uses TSNs), but I have a couple of files that don&#x27;t have these chunks (either because they have been removed, or because they mostly ...'''
date = "2015-08-06T06:06:00Z"
lastmod = "2015-08-06T06:06:00Z"
weight = 44906
keywords = [ "sctp", "association", "wireshark" ]
aliases = [ "/questions/44906" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SCTP Association Algorithm](/questions/44906/sctp-association-algorithm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44906-score" class="post-score" title="current number of votes">0</div><span id="post-44906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to write a python module for determining SCTP associations from captured traffic. It works fine when I read a pcap that has SACK chunks (since my heuristic uses TSNs), but I have a couple of files that don't have these chunks (either because they have been removed, or because they mostly contain retransmissions)</p><p>When I try to run the script on these files, I get different results to Wireshark's Telephony&gt;SCTP&gt;Show All Associations utility.</p><p>At the moment I'm using a combination of comparing TSNs and comparing Transport Addresses. For the latter, arrays of unique src and dst transport addresses are kept for each endpoint. When a src TA for one endpoint is found in the dst array of another, they are made more likely to be put into an association together.</p><p>For example with <a href="https://www.cloudshark.org/captures/e6909dc0862f?filter=frame%20and%20eth%20and%20ip%20and%20sctp%20and%20m3ua%20and%20sccp%20and%20ranap%20and%20sctp%20and%20m3ua">this</a> file, my script gets all associations right, except the ones with VTags: 838939786, 4139831617 and 3653663047.</p><p>Wireshark pairs up the first 2, and the 365[...] with a 0 VTag.</p><p>My script puts 838[...] and 365[...] together, and 413[...] with a 0 VTag.</p><p>Is there something else Wireshark does that I've not considered?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sctp" rel="tag" title="see questions tagged &#39;sctp&#39;">sctp</span> <span class="post-tag tag-link-association" rel="tag" title="see questions tagged &#39;association&#39;">association</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '15, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/d0ac0a1b1a2bd52ccfc6f6f3c17aaafb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex%20Hunter&#39;s gravatar image" /><p><span>Alex Hunter</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex Hunter has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Aug '15, 07:56</strong> </span></p></div></div><div id="comments-container-44906" class="comments-container"></div><div id="comment-tools-44906" class="comment-tools"></div><div class="clear"></div><div id="comment-44906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

