+++
type = "question"
title = "Wireshark AMQP Plugin"
description = '''Hi How do you install and make use of the AMQP plugin (or dissector) for Linux? I am running a Redhat 5.5 system, have Wireshark v1.0.8 installed but do not know how to get the AMQP plugin online? Can you help please? I have searched for hours for online docs etc. but have come up with nothing :( Ma...'''
date = "2012-07-04T05:34:00Z"
lastmod = "2012-07-05T07:50:00Z"
weight = 12438
keywords = [ "wireshark" ]
aliases = [ "/questions/12438" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark AMQP Plugin](/questions/12438/wireshark-amqp-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12438-score" class="post-score" title="current number of votes">0</div><span id="post-12438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi How do you install and make use of the AMQP plugin (or dissector) for Linux? I am running a Redhat 5.5 system, have Wireshark v1.0.8 installed but do not know how to get the AMQP plugin online?</p><p>Can you help please? I have searched for hours for online docs etc. but have come up with nothing :(</p><p>Many thanks, any help is appreciated.</p><p>Brgds, David</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '12, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/0b06a598c8685216821920bf5d7ea551?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Thompson&#39;s gravatar image" /><p><span>David Thompson</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Thompson has no accepted answers">0%</span></p></div></div><div id="comments-container-12438" class="comments-container"></div><div id="comment-tools-12438" class="comment-tools"></div><div class="clear"></div><div id="comment-12438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12439"></span>

<div id="answer-container-12439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12439-score" class="post-score" title="current number of votes">0</div><span id="post-12439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The amqp dissector is part of Wireshark proper (even though it says <code>AMQP v0-9, 0-10 Wireshark dissector plug-in</code> at the beginning of the source file.</p><p>(I've fixed the comment in the development version source file to remove the word 'plugin').</p><p>The amqp dissector was added to Wireshark in a version prior to 1.0.8.</p><p>So: the dissector is <em>not</em> a plugin and should be called if a capture file contains packets on tcp port 5672. (You can use <code>Analyze ! Decode As</code> if a different TCP port is being used).</p><p>Are you having a problem wherein the amqp dissector isn't being called to dissect amqp packets in a capture file ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '12, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jul '12, 06:06</strong> </span></p></div></div><div id="comments-container-12439" class="comments-container"><span id="12440"></span><div id="comment-12440" class="comment"><div id="post-12440-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Thanks for getting back. Ok, so the AMQP dissector plug-in is included in my build, great.</p><p>Yes, I think I may have a problem in that case. When I run 'wireshark' the GUI (Gnome) opens fine. But when I close the GUI I see "Warn Dissector bug, protocol AMQP, in packet 58772: packet-amqp.c:2091: failed assertion "(0)"". This is repeated hundreds of times in the terminal I started 'wireshark' in.</p><p>Any clues?</p><p>/David</p></div><div id="comment-12440-info" class="comment-info"><span class="comment-age">(04 Jul '12, 07:03)</span> <span class="comment-user userinfo">David Thompson</span></div></div><span id="12441"></span><div id="comment-12441" class="comment"><div id="post-12441-score" class="comment-score"></div><div class="comment-text"><p>This is the result of the dissectors not understanding the AMQP type. Not really a bug, just that it only understands AMQP_FRAME_TYPE_METHOD(1), AMQP_FRAME_TYPE_CONTENT_HEADER(2) and AMQP_FRAME_TYPE_CONTENT_BODY(3).</p></div><div id="comment-12441-info" class="comment-info"><span class="comment-age">(04 Jul '12, 07:40)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="12464"></span><div id="comment-12464" class="comment"><div id="post-12464-score" class="comment-score"></div><div class="comment-text"><p>A little further research indicates that reporting unknown message types as "dissector bugs" was fixed a while back (Jan 2011).</p><p>Unknown message types are now reported with an explicit "Unknown Frame Type" message in the packet details dissection.</p><p>See: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4048">Bug 4048</a></p><p>This fix was included in Wireshark1.2.14 and Wireshark 1.4.3 which were both released in January 2011.</p><p>So: It seems you are using an older version of Wireshark.</p><p>If possible you may want to consider upgrading to the latest stable version of Wireshark (1.8.0).</p></div><div id="comment-12464-info" class="comment-info"><span class="comment-age">(05 Jul '12, 07:50)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-12439" class="comment-tools"></div><div class="clear"></div><div id="comment-12439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

