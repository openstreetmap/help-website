+++
type = "question"
title = "Decoding PCOIP"
description = '''Does wireshark support PCOIP? If so which option do I use to decode it since it is not listed under current protocols'''
date = "2016-12-13T20:38:00Z"
lastmod = "2016-12-14T00:03:00Z"
weight = 58061
keywords = [ "pcoip", "4172" ]
aliases = [ "/questions/58061" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding PCOIP](/questions/58061/decoding-pcoip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58061-score" class="post-score" title="current number of votes">0</div><span id="post-58061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does wireshark support PCOIP? If so which option do I use to decode it since it is not listed under current protocols</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcoip" rel="tag" title="see questions tagged &#39;pcoip&#39;">pcoip</span> <span class="post-tag tag-link-4172" rel="tag" title="see questions tagged &#39;4172&#39;">4172</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '16, 20:38</strong></p><img src="https://secure.gravatar.com/avatar/ad068929eae0968646f30eea858bfe49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kab13&#39;s gravatar image" /><p><span>kab13</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kab13 has no accepted answers">0%</span></p></div></div><div id="comments-container-58061" class="comments-container"></div><div id="comment-tools-58061" class="comment-tools"></div><div class="clear"></div><div id="comment-58061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58067"></span>

<div id="answer-container-58067" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58067-score" class="post-score" title="current number of votes">1</div><span id="post-58067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is simple PCOIP Lua dissector written by Paul Offord and his team. It will decode PCoIP Sequence Numbers and find if there any gaps in those. But of course it won't do any decryption.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/pcoip_summary.png" alt="alt text" /></p><p>You can download it on Tribelab site (free registration required, but they won't send any spam to you for sure):</p><p><a href="https://community.tribelab.com/course/view.php?id=17">https://community.tribelab.com/course/view.php?id=17</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '16, 00:03</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p><span>Packet_vlad</span><br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Dec '16, 00:05</strong> </span></p></div></div><div id="comments-container-58067" class="comments-container"></div><div id="comment-tools-58067" class="comment-tools"></div><div class="clear"></div><div id="comment-58067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58062"></span>

<div id="answer-container-58062" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58062-score" class="post-score" title="current number of votes">0</div><span id="post-58062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Does wireshark support PCOIP?</p></blockquote><p>No. It's apparently a <a href="https://www.petri.com/what-is-pc-over-ip#">proprietary protocol</a>, so unless Teradici documents it or somebody reverse-engineers it, Wireshark won't be able to dissect it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '16, 21:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-58062" class="comments-container"></div><div id="comment-tools-58062" class="comment-tools"></div><div class="clear"></div><div id="comment-58062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

