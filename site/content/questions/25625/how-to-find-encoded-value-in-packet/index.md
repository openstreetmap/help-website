+++
type = "question"
title = "How to find encoded value in packet?"
description = '''Hi, In following image, selected filed shows &#x27;(0)&#x27; in front of field name. I have tried hard to understand where it came from, but not able to get where this 0 is encoded. Is there any way to find it out. It&#x27;s gsm_map protocol. And its response of ATI message. Kindly note that image is tampered inte...'''
date = "2013-10-04T01:10:00Z"
lastmod = "2013-10-08T06:31:00Z"
weight = 25625
keywords = [ "dissector", "wireshark", "analysis", "display-filter" ]
aliases = [ "/questions/25625" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to find encoded value in packet?](/questions/25625/how-to-find-encoded-value-in-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25625-score" class="post-score" title="current number of votes">0</div><span id="post-25625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In following image, selected filed shows '(0)' in front of field name. I have tried hard to understand where it came from, but not able to get where this 0 is encoded. Is there any way to find it out. It's gsm_map protocol. And its response of ATI message.</p><p><em>Kindly note that image is tampered intentionally to hide information.</em></p><p><img src="https://osqa-ask.wireshark.org/upfiles/lcs_1.bmp" alt="alt text" /> In image,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '13, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/4d5a1d4ba48122bcddd239a84b8bf3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pranitkothari&#39;s gravatar image" /><p><span>pranitkothari</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pranitkothari has one accepted answer">100%</span></p></img></div></div><div id="comments-container-25625" class="comments-container"></div><div id="comment-tools-25625" class="comment-tools"></div><div class="clear"></div><div id="comment-25625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25629"></span>

<div id="answer-container-25629" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25629-score" class="post-score" title="current number of votes">2</div><span id="post-25629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pranitkothari has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>GSM MAP uses <a href="https://en.wikipedia.org/wiki/ASN.1">ASN.1</a>'s <a href="https://en.wikipedia.org/wiki/Basic_Encoding_Rules#BER_encoding">BER</a> encoding. Try turning on the "Show internal BER encapsulation tokens" option for the BER protocol (in Edit -&gt; Preferences; open up the Protocols list and select BER) and selecting the "subscriberState" field, and it'll show you where the value of 0 is encoded, using BER, for that field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-25629" class="comments-container"><span id="25636"></span><div id="comment-25636" class="comment"><div id="post-25636-score" class="comment-score"></div><div class="comment-text"><p>Your answer really helped me. Just wanted to understand what does it means 'GSM MAP uses ASN.1's BER encoding', secondly how to find protocol uses which encoding internally?</p></div><div id="comment-25636-info" class="comment-info"><span class="comment-age">(04 Oct '13, 04:11)</span> <span class="comment-user userinfo">pranitkothari</span></div></div><span id="25652"></span><div id="comment-25652" class="comment"><div id="post-25652-score" class="comment-score"></div><div class="comment-text"><p>See the two links for "ASN.1" and "BER" for a discussion of ASN.1 ("Abstract Syntax Notation 1") and BER (Basic Encoding Rules).</p><p>You'd have to find a description of a particular protocol to find what encoding it uses, although turning the "Show internal BER encapsulation tokens" will indicate whether a protocol uses ASN.1 BER (or DER, "Distinguished Encoding Rules", or CER, "Canonical Encoding Rules", which are subsets of BER).</p></div><div id="comment-25652-info" class="comment-info"><span class="comment-age">(04 Oct '13, 11:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="25742"></span><div id="comment-25742" class="comment"><div id="post-25742-score" class="comment-score"></div><div class="comment-text"><p><span>@Guy Harris</span>: Thank you very much. It really helped.</p></div><div id="comment-25742-info" class="comment-info"><span class="comment-age">(08 Oct '13, 06:31)</span> <span class="comment-user userinfo">pranitkothari</span></div></div></div><div id="comment-tools-25629" class="comment-tools"></div><div class="clear"></div><div id="comment-25629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

