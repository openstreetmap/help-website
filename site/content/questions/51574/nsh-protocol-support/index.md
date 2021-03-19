+++
type = "question"
title = "NSH  protocol support"
description = '''Hi,  Is there any dissector for NSH (network service header) protocol? I can see some bug being raised but I could not find the desired files. Can anyone help me how do I see the NSH packets in wireshark. Thanks  Saurav'''
date = "2016-04-12T00:00:00Z"
lastmod = "2016-04-12T02:40:00Z"
weight = 51574
keywords = [ "nsh", "dissector", "wireshark", "sfc", "plugin" ]
aliases = [ "/questions/51574" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NSH protocol support](/questions/51574/nsh-protocol-support)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51574-score" class="post-score" title="current number of votes">0</div><span id="post-51574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is there any dissector for NSH (network service header) protocol? I can see some bug being raised but I could not find the desired files. Can anyone help me how do I see the NSH packets in wireshark.</p><p>Thanks Saurav</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nsh" rel="tag" title="see questions tagged &#39;nsh&#39;">nsh</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-sfc" rel="tag" title="see questions tagged &#39;sfc&#39;">sfc</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/80a485df3f553e50ac4c5c01c9923daa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saurabh%20Suman&#39;s gravatar image" /><p><span>Saurabh Suman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saurabh Suman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Apr '16, 00:03</strong> </span></p></div></div><div id="comments-container-51574" class="comments-container"></div><div id="comment-tools-51574" class="comment-tools"></div><div class="clear"></div><div id="comment-51574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51578"></span>

<div id="answer-container-51578" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51578-score" class="post-score" title="current number of votes">0</div><span id="post-51578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A dissector was added in Feb 16, see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11490">this</a> item in the bug tracker. Some test captures are available on that item.</p><p>This will currently be available in <a href="https://www.wireshark.org/download/automated/">automated builds</a>, or builds made from master. For regular releases, you'll have to wait for the release of 2.2.x.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '16, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Apr '16, 03:07</strong> </span></p></div></div><div id="comments-container-51578" class="comments-container"><span id="51585"></span><div id="comment-51585" class="comment"><div id="post-51585-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. :)</p></div><div id="comment-51585-info" class="comment-info"><span class="comment-age">(12 Apr '16, 02:40)</span> <span class="comment-user userinfo">Saurabh Suman</span></div></div></div><div id="comment-tools-51578" class="comment-tools"></div><div class="clear"></div><div id="comment-51578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

