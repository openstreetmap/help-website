+++
type = "question"
title = "Is tshark able to use plugin dissectors?"
description = '''I have a dissector to decode the payload for an RTPS payload and it works fine in wireshark, but tshark does not seem to recogize the hand-off from RTPS to my sub-dissection routine. Is there a way for tshark to be able use plugin dissectors. A command-line solution would be nice to use for automate...'''
date = "2014-07-30T13:17:00Z"
lastmod = "2014-07-30T14:42:00Z"
weight = 35010
keywords = [ "plugins", "tshark", "dissectors" ]
aliases = [ "/questions/35010" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is tshark able to use plugin dissectors?](/questions/35010/is-tshark-able-to-use-plugin-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35010-score" class="post-score" title="current number of votes">0</div><span id="post-35010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a dissector to decode the payload for an RTPS payload and it works fine in wireshark, but tshark does not seem to recogize the hand-off from RTPS to my sub-dissection routine.</p><p>Is there a way for tshark to be able use plugin dissectors. A command-line solution would be nice to use for automated checking of pcap files.</p><p>I have googled this as many ways as I can think of and can't seem to find an answer.</p><p>Thanks for any advice or suggestions.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dissectors" rel="tag" title="see questions tagged &#39;dissectors&#39;">dissectors</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '14, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/599a63f7e6a0cd7d68eac5cb4b296745?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FlanOSU&#39;s gravatar image" /><p><span>FlanOSU</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FlanOSU has no accepted answers">0%</span></p></div></div><div id="comments-container-35010" class="comments-container"><span id="35013"></span><div id="comment-35013" class="comment"><div id="post-35013-score" class="comment-score"></div><div class="comment-text"><p>Does your dissector require 2 pass dissection? Try passing command line option '-2' to tshark.</p></div><div id="comment-35013-info" class="comment-info"><span class="comment-age">(30 Jul '14, 13:24)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-35010" class="comment-tools"></div><div class="clear"></div><div id="comment-35010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35012"></span>

<div id="answer-container-35012" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35012-score" class="post-score" title="current number of votes">1</div><span id="post-35012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FlanOSU has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would expect it to "just work".</p><p>(IOW: if a plugin works OK with wireshark, it should also be OK with tshark)</p><p>A long shot: what happens if you use <code>tshark -2 ...</code> ?</p><p>In any case, what platform/OS/version are you using ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '14, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jul '14, 13:25</strong> </span></p></div></div><div id="comments-container-35012" class="comments-container"><span id="35016"></span><div id="comment-35016" class="comment"><div id="post-35016-score" class="comment-score"></div><div class="comment-text"><p>I am running on a vm of Linux (RHEL 5).</p><p>The two pass option got me going in the right direction. I have to process the DDS publications in order to get a list of "upcoming" messages by GUID. I then have to use the GUID to correctly decode my payloads, which don't have typical header information like message id, length, etc...</p><p>I had an older version of wireshark/tshark that doesn't seem to support the two pass feature, but the latest wireshark build I was working with handles it correctly. Thanks for the assistance.</p></div><div id="comment-35016-info" class="comment-info"><span class="comment-age">(30 Jul '14, 14:42)</span> <span class="comment-user userinfo">FlanOSU</span></div></div></div><div id="comment-tools-35012" class="comment-tools"></div><div class="clear"></div><div id="comment-35012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

