+++
type = "question"
title = "Merge error - Wireshark can&#x27;t save this capture in that format."
description = '''I am trying to merge two capture files i downloaded from the sample captures from wireshark site. zigbee-join-authenticate.pcap Teredo.pcap Every time i select a file to merge with currently opened cature file i get the following dialogue box &quot;Wireshark can&#x27;t save this capture in that format.&quot; Could...'''
date = "2012-01-19T07:36:00Z"
lastmod = "2012-01-29T16:21:00Z"
weight = 8469
keywords = [ "merge", "capture-file-merge" ]
aliases = [ "/questions/8469" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Merge error - Wireshark can't save this capture in that format.](/questions/8469/merge-error-wireshark-cant-save-this-capture-in-that-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8469-score" class="post-score" title="current number of votes">0</div><span id="post-8469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to merge two capture files i downloaded from the sample captures from wireshark site. zigbee-join-authenticate.pcap Teredo.pcap</p><p>Every time i select a file to merge with currently opened cature file i get the following dialogue box</p><p>"Wireshark can't save this capture in that format."</p><p>Could some one tell me what the issue is?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-capture-file-merge" rel="tag" title="see questions tagged &#39;capture-file-merge&#39;">capture-file-merge</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '12, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/83e04f89cabcf71f8efd2238a88905ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="v%20j&#39;s gravatar image" /><p><span>v j</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="v j has no accepted answers">0%</span></p></div></div><div id="comments-container-8469" class="comments-container"><span id="8487"></span><div id="comment-8487" class="comment"><div id="post-8487-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark (or mergecap) are you using?</p></div><div id="comment-8487-info" class="comment-info"><span class="comment-age">(19 Jan '12, 17:55)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="8488"></span><div id="comment-8488" class="comment"><div id="post-8488-score" class="comment-score"></div><div class="comment-text"><p>I am using Wireshark version 1.6.5 on windows, but I got the same issue with 1.7.0 also</p></div><div id="comment-8488-info" class="comment-info"><span class="comment-age">(19 Jan '12, 19:21)</span> <span class="comment-user userinfo">v j</span></div></div></div><div id="comment-tools-8469" class="comment-tools"></div><div class="clear"></div><div id="comment-8469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8495"></span>

<div id="answer-container-8495" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8495-score" class="post-score" title="current number of votes">1</div><span id="post-8495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="v j has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The issue is that:</p><ol><li>those two capture files have different link-layer header types;</li><li>they are both pcap files, so the default file type for the merged file is pcap;</li><li>pcap files do not support multiple link-layer header types in a single file.</li></ol><p>Try selecting pcap-ng format instead; that supports multiple link-layer header types in a single file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8495" class="comments-container"><span id="8512"></span><div id="comment-8512" class="comment"><div id="post-8512-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tip. It worked. But i had an issue with pcapng format.</p><p>I did 2 fresh captures myself and saved them in pcap format and the merged them into one, it succeeded.</p><p>But when i save the captures in pcapng format and merge them i get the same old error.</p></div><div id="comment-8512-info" class="comment-info"><span class="comment-age">(20 Jan '12, 06:19)</span> <span class="comment-user userinfo">v j</span></div></div><span id="8683"></span><div id="comment-8683" class="comment"><div id="post-8683-score" class="comment-score"></div><div class="comment-text"><p>bounce ...</p></div><div id="comment-8683-info" class="comment-info"><span class="comment-age">(29 Jan '12, 16:21)</span> <span class="comment-user userinfo">v j</span></div></div></div><div id="comment-tools-8495" class="comment-tools"></div><div class="clear"></div><div id="comment-8495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

