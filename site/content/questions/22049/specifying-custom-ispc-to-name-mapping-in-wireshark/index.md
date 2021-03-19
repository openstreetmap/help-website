+++
type = "question"
title = "Specifying custom ISPC to name mapping in Wireshark"
description = '''Hello, Would it be possible to use a specific mapping of ISPC to name of the signalling point operator in Wireshark by specifying it in the configuration or somehow, without needing to specify it in packet-q708.c and recompiling it? Cheers, zvmduka'''
date = "2013-06-14T03:11:00Z"
lastmod = "2013-06-15T05:28:00Z"
weight = 22049
keywords = [ "q708", "ispc" ]
aliases = [ "/questions/22049" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Specifying custom ISPC to name mapping in Wireshark](/questions/22049/specifying-custom-ispc-to-name-mapping-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22049-score" class="post-score" title="current number of votes">0</div><span id="post-22049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Would it be possible to use a specific mapping of ISPC to name of the signalling point operator in Wireshark by specifying it in the configuration or somehow, without needing to specify it in packet-q708.c and recompiling it?</p><p>Cheers, zvmduka</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-q708" rel="tag" title="see questions tagged &#39;q708&#39;">q708</span> <span class="post-tag tag-link-ispc" rel="tag" title="see questions tagged &#39;ispc&#39;">ispc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '13, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/3abd13efb468bd08f0f3ad8c5c12df58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zvmduka&#39;s gravatar image" /><p><span>zvmduka</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zvmduka has no accepted answers">0%</span></p></div></div><div id="comments-container-22049" class="comments-container"></div><div id="comment-tools-22049" class="comment-tools"></div><div class="clear"></div><div id="comment-22049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22060"></span>

<div id="answer-container-22060" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22060-score" class="post-score" title="current number of votes">0</div><span id="post-22060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zvmduka has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, you can't do that now. But there's an <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7592">enhancement request</a> out there which requests the functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '13, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-22060" class="comments-container"><span id="22087"></span><div id="comment-22087" class="comment"><div id="post-22087-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info Jeff, I haven't seen this request before.</p></div><div id="comment-22087-info" class="comment-info"><span class="comment-age">(15 Jun '13, 05:28)</span> <span class="comment-user userinfo">zvmduka</span></div></div></div><div id="comment-tools-22060" class="comment-tools"></div><div class="clear"></div><div id="comment-22060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22059"></span>

<div id="answer-container-22059" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22059-score" class="post-score" title="current number of votes">1</div><span id="post-22059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>use a specific mapping of ISPC to name of the signalling point ... without needing to specify it in packet-q708.c</p></blockquote><p>Unfortunately that is not implemented in that code (no user definable options). So, if you need to change a mapping, you'll have to change the code and then recompile it.</p><p>BTW #1: If a 'mapping bug' is the reason for the change, please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>BTW #2: Why do you need a different mapping? Maybe there is another solution for your problem.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '13, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '13, 06:26</strong> </span></p></div></div><div id="comments-container-22059" class="comments-container"><span id="22061"></span><div id="comment-22061" class="comment"><div id="post-22061-score" class="comment-score"></div><div class="comment-text"><p>For #2: think of it as IP&lt;-&gt;hostname mapping except for SS7 point codes.</p></div><div id="comment-22061-info" class="comment-info"><span class="comment-age">(14 Jun '13, 06:58)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="22062"></span><div id="comment-22062" class="comment"><div id="post-22062-score" class="comment-score"></div><div class="comment-text"><p>maybe he needs the mapping just for some kind of quick analysis,which could also be done with a script !?!</p></div><div id="comment-22062-info" class="comment-info"><span class="comment-age">(14 Jun '13, 07:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22086"></span><div id="comment-22086" class="comment"><div id="post-22086-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info Kurt!</p><p>1: there's no bug in ISPC-&gt;operator mapping, that's all good.</p><p>2: to have a human-readable format of the point codes used in the internal communication between the nodes and as well with international ones.</p><p>In the telco network you have a big bunch of nodes communicating with paired routers and it would be easier to see through the Wireshark communication between "London-SMSC-4; London-HLR-1" rather than OPC/DPC == 1234/5678.</p><p>Anyways, thanks for the info. For the time being I'll keep the list of PCs in packet-q708.c and recompile when necessary.</p><p>Cheers!</p></div><div id="comment-22086-info" class="comment-info"><span class="comment-age">(15 Jun '13, 05:19)</span> <span class="comment-user userinfo">zvmduka</span></div></div></div><div id="comment-tools-22059" class="comment-tools"></div><div class="clear"></div><div id="comment-22059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

