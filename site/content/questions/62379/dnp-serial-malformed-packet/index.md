+++
type = "question"
title = "DNP Serial Malformed Packet."
description = '''Wireshark gives me a &quot;malformed packet&quot; message every time my DNP 3 responses are larger that a single frame. I am analyzing DNP over serial. I am trying to determine the setting that will allow decoding of greater that 255 byte packets, but am not having any luck. Any ideas?'''
date = "2017-06-28T15:59:00Z"
lastmod = "2017-07-11T12:51:00Z"
weight = 62379
keywords = [ "malformedpacket" ]
aliases = [ "/questions/62379" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DNP Serial Malformed Packet.](/questions/62379/dnp-serial-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62379-score" class="post-score" title="current number of votes">0</div><span id="post-62379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark gives me a "malformed packet" message every time my DNP 3 responses are larger that a single frame. I am analyzing DNP over serial. I am trying to determine the setting that will allow decoding of greater that 255 byte packets, but am not having any luck. Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malformedpacket" rel="tag" title="see questions tagged &#39;malformedpacket&#39;">malformedpacket</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '17, 15:59</strong></p><img src="https://secure.gravatar.com/avatar/1ded6651d0130b9462f2d7f31c931715?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt&#39;s gravatar image" /><p><span>Kurt</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt has no accepted answers">0%</span></p></div></div><div id="comments-container-62379" class="comments-container"><span id="62384"></span><div id="comment-62384" class="comment"><div id="post-62384-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc?</p></div><div id="comment-62384-info" class="comment-info"><span class="comment-age">(28 Jun '17, 21:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="62596"></span><div id="comment-62596" class="comment"><div id="post-62596-score" class="comment-score"></div><div class="comment-text"><p>That's not really necessary. I simply need to know how to set Wireshark to decide more than one frame of serial data. I figured it out with ASE2000, I just need help with Wireshark.</p></div><div id="comment-62596-info" class="comment-info"><span class="comment-age">(06 Jul '17, 21:10)</span> <span class="comment-user userinfo">Kurt</span></div></div><span id="62601"></span><div id="comment-62601" class="comment"><div id="post-62601-score" class="comment-score"></div><div class="comment-text"><p>As the DNP3 dissector successfully reassembles DNP3 traffic over both TCP and UDP, I suspect that the fact that your capture is "serial" may be the issue, hence the need to see the capture.</p><p>How exactly did you make the capture file?</p></div><div id="comment-62601-info" class="comment-info"><span class="comment-age">(07 Jul '17, 02:58)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-62379" class="comment-tools"></div><div class="clear"></div><div id="comment-62379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62598"></span>

<div id="answer-container-62598" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62598-score" class="post-score" title="current number of votes">0</div><span id="post-62598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go <code>Edit -&gt; Preferences -&gt; Protocols -&gt; DNP 3.0</code> or right-click the DNP layer in the packet dissection pane. There is a single preference - <code>Reassemble DNP3 messages spanning multiple TCP segments</code> which is, however, on by default. If it is on and the problem persists, something is wrong with the trace contents or with the dissector, that's why <a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> asked you to share the trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '17, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62598" class="comments-container"><span id="62679"></span><div id="comment-62679" class="comment"><div id="post-62679-score" class="comment-score"></div><div class="comment-text"><p>I haven't used this service before. I posted a capture on Cloudshark as requested</p></div><div id="comment-62679-info" class="comment-info"><span class="comment-age">(11 Jul '17, 12:50)</span> <span class="comment-user userinfo">Kurt</span></div></div><span id="62680"></span><div id="comment-62680" class="comment"><div id="post-62680-score" class="comment-score"></div><div class="comment-text"><p>Can you provide a link to it?</p></div><div id="comment-62680-info" class="comment-info"><span class="comment-age">(11 Jul '17, 12:51)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62598" class="comment-tools"></div><div class="clear"></div><div id="comment-62598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

