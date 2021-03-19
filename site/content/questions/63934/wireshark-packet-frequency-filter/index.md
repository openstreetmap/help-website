+++
type = "question"
title = "Wireshark packet frequency filter"
description = '''Hello, Is there any filter in Wireshark which can calculate a cummulative of the packets received and sent over a given period of time. For example, the filter flags a host and destination if more than 150 packets are received in a second. This can be used to track possible denial of service attacks...'''
date = "2017-10-16T10:33:00Z"
lastmod = "2017-10-16T12:36:00Z"
weight = 63934
keywords = [ "filter", "capture-filter", "capure", "wireshark" ]
aliases = [ "/questions/63934" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark packet frequency filter](/questions/63934/wireshark-packet-frequency-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63934-score" class="post-score" title="current number of votes">0</div><span id="post-63934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is there any filter in Wireshark which can calculate a cummulative of the packets received and sent over a given period of time. For example, the filter flags a host and destination if more than 150 packets are received in a second. This can be used to track possible denial of service attacks and so may prove to be very useful for me</p><p>Thanks :))</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-capure" rel="tag" title="see questions tagged &#39;capure&#39;">capure</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '17, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/a6df0b722ff3a42b2627e2c1c723be24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smurpani&#39;s gravatar image" /><p><span>smurpani</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smurpani has no accepted answers">0%</span></p></div></div><div id="comments-container-63934" class="comments-container"><span id="63940"></span><div id="comment-63940" class="comment"><div id="post-63940-score" class="comment-score">1</div><div class="comment-text"><p>Omnipeek, a commercial alternative to wireshark, contains some defined error conditions related to such metrics as packets per second of a particular condition. However, I am not sure it is extensible, i.e. where you get to define your own conditions.</p></div><div id="comment-63940-info" class="comment-info"><span class="comment-age">(16 Oct '17, 11:05)</span> <span class="comment-user userinfo">Bob Jones</span></div></div></div><div id="comment-tools-63934" class="comment-tools"></div><div class="clear"></div><div id="comment-63934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63938"></span>

<div id="answer-container-63938" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63938-score" class="post-score" title="current number of votes">0</div><span id="post-63938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="smurpani has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nope. Filters can only decide if any individual packet should be captured\displayed, they don't provide aggregation facilities over multiple packets.</p><p>The area you're looking at sounds more like network security tools rather than packet analysis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '17, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63938" class="comments-container"><span id="63939"></span><div id="comment-63939" class="comment"><div id="post-63939-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer... I'm actually doing a project which explores how packet analysis can prevent malware from spreading and so your assumption about the network security aspect is accurate ;)</p></div><div id="comment-63939-info" class="comment-info"><span class="comment-age">(16 Oct '17, 11:04)</span> <span class="comment-user userinfo">smurpani</span></div></div><span id="63942"></span><div id="comment-63942" class="comment"><div id="post-63942-score" class="comment-score"></div><div class="comment-text"><p>This looks like something for Snort or Suricata</p></div><div id="comment-63942-info" class="comment-info"><span class="comment-age">(16 Oct '17, 12:36)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-63938" class="comment-tools"></div><div class="clear"></div><div id="comment-63938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

