+++
type = "question"
title = "how to write a wireshark dissector for amf packet sent over tcp"
description = '''I want to write a wireshark dissector for amf packet sent over tcp. In wireshark capture window amf packet which is inside a tcp is dissected as tcp . I want to dissect the amf packet that is encapsulated inside tcp. '''
date = "2012-10-18T01:28:00Z"
lastmod = "2012-11-16T14:35:00Z"
weight = 15072
keywords = [ "dissector" ]
aliases = [ "/questions/15072" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to write a wireshark dissector for amf packet sent over tcp](/questions/15072/how-to-write-a-wireshark-dissector-for-amf-packet-sent-over-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15072-score" class="post-score" title="current number of votes">0</div><span id="post-15072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to write a wireshark dissector for amf packet sent over tcp. In wireshark capture window amf packet which is inside a tcp is dissected as tcp . I want to dissect the amf packet that is encapsulated inside tcp.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '12, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/b0ed262c234b0aa9fae2e5b2d51b14c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akhil&#39;s gravatar image" /><p><span>Akhil</span><br />
<span class="score" title="53 reputation points">53</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akhil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Oct '12, 02:04</strong> </span></p></div></div><div id="comments-container-15072" class="comments-container"><span id="15073"></span><div id="comment-15073" class="comment"><div id="post-15073-score" class="comment-score"></div><div class="comment-text"><p>Okay. So what is your question? You should be way more specific, or this (non-) question will not survive in the shark pond very long...</p></div><div id="comment-15073-info" class="comment-info"><span class="comment-age">(18 Oct '12, 01:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="15076"></span><div id="comment-15076" class="comment"><div id="post-15076-score" class="comment-score"></div><div class="comment-text"><p>In wireshark capture window amf packet which is inside a tcp is dissected as tcp . I want to dissect the amf packet that is encapsulated inside tcp.</p></div><div id="comment-15076-info" class="comment-info"><span class="comment-age">(18 Oct '12, 02:04)</span> <span class="comment-user userinfo">Akhil</span></div></div><span id="15081"></span><div id="comment-15081" class="comment"><div id="post-15081-score" class="comment-score"></div><div class="comment-text"><p>this still isn't a question, it's a statement. If you need a starting point on how to develop something for Wireshark, start here: <a href="http://wiki.wireshark.org/Development,">http://wiki.wireshark.org/Development,</a> or look at the documentation which comes with the sources.</p><p>If you have something specific to ask (which would include a question mark somewhere in your sentences, at least once) you can do that here.</p></div><div id="comment-15081-info" class="comment-info"><span class="comment-age">(18 Oct '12, 04:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-15072" class="comment-tools"></div><div class="clear"></div><div id="comment-15072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15088"></span>

<div id="answer-container-15088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15088-score" class="post-score" title="current number of votes">0</div><span id="post-15088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is your traffic going to or from TCP port 1935?</p><p>Wireshark only recognizes TCP traffic to or from port 1935 as RTMPT traffic. If your RTMPT traffic isn't to or from port 1935, Wireshark won't recognize it as RTMPT traffic; Wireshark would have to be changed to allow other ports to be specified.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '12, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15088" class="comments-container"></div><div id="comment-tools-15088" class="comment-tools"></div><div class="clear"></div><div id="comment-15088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15994"></span>

<div id="answer-container-15994" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15994-score" class="post-score" title="current number of votes">0</div><span id="post-15994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>And if it's going to and from port 80 or port 443 - or, rather, if it's being transported over HTTP or "HTTPS" (HTTP-over-SSL/TLS) with a media type of application/x-amf, as <a href="http://ask.wireshark.org/questions/15078/how-to-decrypt-https-packet-in-wireshark">one of your other questions</a> suggests it is - see <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=46047">how we now do it in the trunk of the Wireshark source repository</a>, as of my checkin of an AMF message dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '12, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Nov '12, 14:36</strong> </span></p></div></div><div id="comments-container-15994" class="comments-container"></div><div id="comment-tools-15994" class="comment-tools"></div><div class="clear"></div><div id="comment-15994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

