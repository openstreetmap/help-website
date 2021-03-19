+++
type = "question"
title = "Setting address information in packet info structure for conversations"
description = '''I have a dissector for a link-layer protocol for which I can dissect packets already. I need to implement conversations for my dissector for per-packet data, and would like to use find_or_create_conversation. I have already added my new address and port types to epan/address.h, epan/address_to_str.c...'''
date = "2011-08-30T07:22:00Z"
lastmod = "2011-08-30T07:22:00Z"
weight = 5956
keywords = [ "development", "pinfo", "dissector", "conversation", "address" ]
aliases = [ "/questions/5956" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Setting address information in packet info structure for conversations](/questions/5956/setting-address-information-in-packet-info-structure-for-conversations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5956-score" class="post-score" title="current number of votes">0</div><span id="post-5956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a dissector for a link-layer protocol for which I can dissect packets already. I need to implement conversations for my dissector for per-packet data, and would like to use <code>find_or_create_conversation</code>. I have already added my new address and port types to <code>epan/address.h</code>, <code>epan/address_to_str.c</code> and <code>column-utils.c</code>.</p><p>How do I set the source and destination information in the <code>pinfo</code> structure so that the correct conversation data is found?</p><p>Sometimes my protocol is simulated over UDP for testing, and I'd like to use the same dissection logic regardless if it's over the real hardware or UDP. How do I ensure that any other source/destination data is clobbered so that only my protocol's data is present?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-pinfo" rel="tag" title="see questions tagged &#39;pinfo&#39;">pinfo</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '11, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-5956" class="comments-container"></div><div id="comment-tools-5956" class="comment-tools"></div><div class="clear"></div><div id="comment-5956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

