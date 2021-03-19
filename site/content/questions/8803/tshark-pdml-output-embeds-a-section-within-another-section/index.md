+++
type = "question"
title = "tshark pdml output embeds a  section within another  section"
description = '''Hi Guys, I have a pdml output file which is OK for all the IP, TCP, UDP etc but there is one protocol which does not get writen correctly. tshark puts a &amp;lt;proto&amp;gt;&amp;lt;/proto&amp;gt; section within another &amp;lt;proto&amp;gt;&amp;lt;/proto&amp;gt; section which makes it non XML compliant. Has anyone had this happen...'''
date = "2012-02-03T02:45:00Z"
lastmod = "2014-10-19T02:42:00Z"
weight = 8803
keywords = [ "section", "pdml", "tshark" ]
aliases = [ "/questions/8803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark pdml output embeds a section within another section](/questions/8803/tshark-pdml-output-embeds-a-section-within-another-section)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8803-score" class="post-score" title="current number of votes">0</div><span id="post-8803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I have a pdml output file which is OK for all the IP, TCP, UDP etc but there is one protocol which does not get writen correctly. tshark puts a &lt;proto&gt;&lt;/proto&gt; section within another &lt;proto&gt;&lt;/proto&gt; section which makes it non XML compliant. Has anyone had this happen before? Any ideas how I can correct it?</p><p>regards,</p><p>Degsy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-section" rel="tag" title="see questions tagged &#39;section&#39;">section</span> <span class="post-tag tag-link-pdml" rel="tag" title="see questions tagged &#39;pdml&#39;">pdml</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '12, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/9ccdf645a58ff89056dec0273965243f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Degsy&#39;s gravatar image" /><p><span>Degsy</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Degsy has no accepted answers">0%</span></p></div></div><div id="comments-container-8803" class="comments-container"><span id="8807"></span><div id="comment-8807" class="comment"><div id="post-8807-score" class="comment-score"></div><div class="comment-text"><p>I haven't seen that happen myself. Are you able to share a file that exhibits this behavior? You could post it to <a href="http://www.cloudshark.org">CloudShark</a> for people to look at.</p><p>Are you using any custom dissectors? What version of TShark is producing the PDML?</p></div><div id="comment-8807-info" class="comment-info"><span class="comment-age">(03 Feb '12, 07:59)</span> <span class="comment-user userinfo">zachad</span></div></div><span id="37157"></span><div id="comment-37157" class="comment"><div id="post-37157-score" class="comment-score"></div><div class="comment-text"><p>I can replicate described behavior with current wireshark git (54dfe3b9b68) without any custom dissectors. It doesn't break XML in my case, but differs from "fake protocol wrapper" fields that seem to be used in similar cases elsewhere.</p><p>As README.xml-output doesn't mention that it's possible for fields to contain "proto" elements, is it safe to assume it's a bug and that it should be reported as such?</p></div><div id="comment-37157-info" class="comment-info"><span class="comment-age">(19 Oct '14, 00:47)</span> <span class="comment-user userinfo">mk-fg</span></div></div><span id="37158"></span><div id="comment-37158" class="comment"><div id="post-37158-score" class="comment-score"></div><div class="comment-text"><p>If you have a capture file that exhibits the issue, go ahead and file a report at the Wireshark <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a> and attach the capture to the bug report.</p></div><div id="comment-37158-info" class="comment-info"><span class="comment-age">(19 Oct '14, 01:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37159"></span><div id="comment-37159" class="comment"><div id="post-37159-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Filed it under <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10588">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10588</a></p></div><div id="comment-37159-info" class="comment-info"><span class="comment-age">(19 Oct '14, 02:42)</span> <span class="comment-user userinfo">mk-fg</span></div></div></div><div id="comment-tools-8803" class="comment-tools"></div><div class="clear"></div><div id="comment-8803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

