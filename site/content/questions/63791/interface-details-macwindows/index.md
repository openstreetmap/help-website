+++
type = "question"
title = "Interface details - Mac/Windows"
description = '''So I&#x27;m trying to know my permanent station address by going into interface details, but for some reason I can&#x27;t find it. I have tried both Windows and Mac, but no luck at all. Any suggestions? The picture down below is the thing I&#x27;m trying to find. '''
date = "2017-10-10T07:31:00Z"
lastmod = "2017-10-11T09:26:00Z"
weight = 63791
keywords = [ "interface" ]
aliases = [ "/questions/63791" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Interface details - Mac/Windows](/questions/63791/interface-details-macwindows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63791-score" class="post-score" title="current number of votes">0</div><span id="post-63791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I'm trying to know my permanent station address by going into interface details, but for some reason I can't find it. I have tried both Windows and Mac, but no luck at all. Any suggestions?</p><p>The picture down below is the thing I'm trying to find.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Picture1_Yz702TR.png" width="640" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '17, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/8abe64dac77628fb2dd3ef96e3822589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="captainpancake133&#39;s gravatar image" /><p><span>captainpanca...</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="captainpancake133 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Oct '17, 09:04</strong> </span></p></div></div><div id="comments-container-63791" class="comments-container"><span id="63794"></span><div id="comment-63794" class="comment"><div id="post-63794-score" class="comment-score">1</div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/43383/captainpancake133"></a><a href="https://ask.wireshark.org/users/43383/captainpancake133">@captainpancake133</a></p><p>I've moved the image from your "answer" to the question and then deleted the "answer". Hopefully someone will come along and give you an actual answer.</p></div><div id="comment-63794-info" class="comment-info"><span class="comment-age">(10 Oct '17, 08:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="63797"></span><div id="comment-63797" class="comment"><div id="post-63797-score" class="comment-score"></div><div class="comment-text"><p>So you're trying to find the MAC address of the Ethernet interface of the machine that's running Wireshark?</p></div><div id="comment-63797-info" class="comment-info"><span class="comment-age">(10 Oct '17, 19:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="63802"></span><div id="comment-63802" class="comment"><div id="post-63802-score" class="comment-score"></div><div class="comment-text"><p>If it brings me to that exact picture, then I guess so.</p></div><div id="comment-63802-info" class="comment-info"><span class="comment-age">(11 Oct '17, 03:33)</span> <span class="comment-user userinfo">captainpanca...</span></div></div></div><div id="comment-tools-63791" class="comment-tools"></div><div class="clear"></div><div id="comment-63791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63803"></span>

<div id="answer-container-63803" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63803-score" class="post-score" title="current number of votes">0</div><span id="post-63803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That dialog is only present in the old GTK version of Wireshark and isn't present in the Qt version which is used on Windows and macOS, the address is normally known as the "MAC Address" for each interface on the machine.</p><p>If you think it should be added to the Qt version please check first, and if no item for it currently exists, raise an enhancement request on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>.</p><p>The information you require can be obtained from the OS's themselves, e.g. see <a href="https://kb.netgear.com/1005/How-to-find-a-MAC-address">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '17, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63803" class="comments-container"><span id="63806"></span><div id="comment-63806" class="comment"><div id="post-63806-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/43383/captainpancake133">@captainpancake133</a></p><p>Please STOP posting comments as "answers", it confuses other users of the site.</p><p>Yes, the MAC address is exactly the same as the "Permanent station address".</p></div><div id="comment-63806-info" class="comment-info"><span class="comment-age">(11 Oct '17, 05:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="63811"></span><div id="comment-63811" class="comment"><div id="post-63811-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Please STOP posting comments as "answers",</p></blockquote><p>I.e., this isn't a forum, it's a Q&amp;A site. "Answers" are answers to the original question; further questions asked of the person who asked the original question, and answers to those questions, are just comments.</p></div><div id="comment-63811-info" class="comment-info"><span class="comment-age">(11 Oct '17, 09:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-63803" class="comment-tools"></div><div class="clear"></div><div id="comment-63803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

