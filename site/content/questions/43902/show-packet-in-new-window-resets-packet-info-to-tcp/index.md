+++
type = "question"
title = "&quot;Show packet in new window&quot; resets packet info to TCP"
description = '''I am developing a dissector plugin to decode our company&#x27;s wire-format for development and debugging purposes. The dissector properly decodes and displays information for the ports that the plugin automatically decodes as our protocol, however when I use &quot;Show Packet In New Window&quot; it will reset the...'''
date = "2015-07-06T13:43:00Z"
lastmod = "2015-08-25T12:24:00Z"
weight = 43902
keywords = [ "decode_as", "dissector", "packet_info", "tcp", "plugin" ]
aliases = [ "/questions/43902" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["Show packet in new window" resets packet info to TCP](/questions/43902/show-packet-in-new-window-resets-packet-info-to-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43902-score" class="post-score" title="current number of votes">0</div><span id="post-43902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am developing a dissector plugin to decode our company's wire-format for development and debugging purposes. The dissector properly decodes and displays information for the ports that the plugin automatically decodes as our protocol, however when I use "Show Packet In New Window" it will reset the Protocol Name and Protocol Info back to TCP while still displaying our decoded information in the packet's payload as we click through the different packets that contain our data.</p><p>If I use "Decode As" at this point to attempt to set the port manually back to our protocol, the packet information will blink to our protocol for a second, then back to TCP with TCP information (Again, while still displaying our decoded protocol in the payload data).</p><p>I'm unsure of the proper way to debug this problem, and have not been able to find similar issues with others. Has this been run into before, and are there any tips I can get? Any information that I can give to help solve this issue?</p><p>Developing and building in 1.99.X, Windows 7, 64-bit, building with Visual Studio 2013.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode_as" rel="tag" title="see questions tagged &#39;decode_as&#39;">decode_as</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-packet_info" rel="tag" title="see questions tagged &#39;packet_info&#39;">packet_info</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '15, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/4fd5789fea23c666ea1fa6533ac4984b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ayurov&#39;s gravatar image" /><p><span>ayurov</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ayurov has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jul '15, 06:44</strong> </span></p></div></div><div id="comments-container-43902" class="comments-container"><span id="43906"></span><div id="comment-43906" class="comment"><div id="post-43906-score" class="comment-score"></div><div class="comment-text"><p>Is the plugin a C-code plugin, or Lua based?</p></div><div id="comment-43906-info" class="comment-info"><span class="comment-age">(06 Jul '15, 15:29)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="43933"></span><div id="comment-43933" class="comment"><div id="post-43933-score" class="comment-score"></div><div class="comment-text"><p>Plugin is written in C, yes.</p></div><div id="comment-43933-info" class="comment-info"><span class="comment-age">(07 Jul '15, 06:34)</span> <span class="comment-user userinfo">ayurov</span></div></div></div><div id="comment-tools-43902" class="comment-tools"></div><div class="clear"></div><div id="comment-43902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45347"></span>

<div id="answer-container-45347" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45347-score" class="post-score" title="current number of votes">0</div><span id="post-45347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ayurov has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Problem reported, and solved, in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11369">Bug 11369</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '15, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/4fd5789fea23c666ea1fa6533ac4984b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ayurov&#39;s gravatar image" /><p><span>ayurov</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ayurov has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '15, 15:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-45347" class="comments-container"></div><div id="comment-tools-45347" class="comment-tools"></div><div class="clear"></div><div id="comment-45347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

