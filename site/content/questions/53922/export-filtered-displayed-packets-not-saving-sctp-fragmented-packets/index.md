+++
type = "question"
title = "Export filtered displayed packets not saving SCTP fragmented packets"
description = '''Hi Experts, I was under the impression that wireshark incorporated feature that when we save filtered displayed trace, it also saves dependent fragments of packets. So that the newly saved file can be restored to show all packets that were displayed in the raw trace. Is this function works for SCTP....'''
date = "2016-07-07T20:18:00Z"
lastmod = "2016-07-09T05:12:00Z"
weight = 53922
keywords = [ "filter", "fragmented", "sctp", "reassembly", "wirsehark" ]
aliases = [ "/questions/53922" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export filtered displayed packets not saving SCTP fragmented packets](/questions/53922/export-filtered-displayed-packets-not-saving-sctp-fragmented-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53922-score" class="post-score" title="current number of votes">0</div><span id="post-53922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>I was under the impression that wireshark incorporated feature that when we save filtered displayed trace, it also saves dependent fragments of packets. So that the newly saved file can be restored to show all packets that were displayed in the raw trace.</p><p>Is this function works for SCTP. I am not seeing this for my traces. We are running MEGACO and DIAMETER over SCTP. I am using Version 2.0.2 (v2.0.2-0-ga16e22e from master-2.0)</p><p>//SShark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-fragmented" rel="tag" title="see questions tagged &#39;fragmented&#39;">fragmented</span> <span class="post-tag tag-link-sctp" rel="tag" title="see questions tagged &#39;sctp&#39;">sctp</span> <span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-wirsehark" rel="tag" title="see questions tagged &#39;wirsehark&#39;">wirsehark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 20:18</strong></p><img src="https://secure.gravatar.com/avatar/4a2a1ab8f8fa05aa1d21e5b43f767aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sshark&#39;s gravatar image" /><p><span>sshark</span><br />
<span class="score" title="6 reputation points">6</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sshark has no accepted answers">0%</span></p></div></div><div id="comments-container-53922" class="comments-container"><span id="53936"></span><div id="comment-53936" class="comment"><div id="post-53936-score" class="comment-score"></div><div class="comment-text"><p>Can you specify exactly what steps you're doing?</p><p>I just tried it with 2.0.4 and it worked. Basically I:</p><ol><li>Applied a display filter that matched only the (reassembled) frame I wanted</li><li>Did File-&gt;Export Specified Packets</li><li>Chose a file name and hit Save</li></ol><p>(The Displayed column showed that I was going to save 2 packets rather than the 1 displayed in the packet list--which is what I wanted.)</p><p>The notes from the commit that added this feature indicate that it only works when exporting/saving the All the Displayed packets--it doesn't work with the Selected Packet or Marked Packet cases.</p></div><div id="comment-53936-info" class="comment-info"><span class="comment-age">(08 Jul '16, 06:36)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="53939"></span><div id="comment-53939" class="comment"><div id="post-53939-score" class="comment-score"></div><div class="comment-text"><p>Yes, I did exactly as you described</p><ol><li>Applied a display filter - "megaco or diameter"</li><li>Did File - Export Specified Packets --&gt; Save all Displyed packets</li><li>Open the new file and applied filter "megaco or diameter"</li><li>Cannot see one of the diameter packets (request)</li></ol><p>Yes, understand that the feature works if I save all Displayed Packets</p><p>I have in Packet re-assemble enabled under Edit - Preference - Protocol, IPv4 &amp; SCTP</p><p>Can share sample traces via email</p></div><div id="comment-53939-info" class="comment-info"><span class="comment-age">(08 Jul '16, 07:44)</span> <span class="comment-user userinfo">sshark</span></div></div></div><div id="comment-tools-53922" class="comment-tools"></div><div class="clear"></div><div id="comment-53922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53941"></span>

<div id="answer-container-53941" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53941-score" class="post-score" title="current number of votes">0</div><span id="post-53941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So it works in general but not for one particular message?</p><p>In that case we'd need to see the capture. You could post it someplace public like <a href="http://cloudshark.org">cloudshark.org</a> or, since it sounds it may be a bug, <a href="https://bugs.wireshark.org">raise a bug</a> (you can mark the bug was private if the capture file is sensitive--one of the core developers can then mark the attachment as private and make the bug public; unfortunately mere mortals don't have the ability to mark attachments as private).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '16, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-53941" class="comments-container"><span id="53954"></span><div id="comment-53954" class="comment"><div id="post-53954-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12597">Bug 12597</a> reported</p></div><div id="comment-53954-info" class="comment-info"><span class="comment-age">(09 Jul '16, 05:12)</span> <span class="comment-user userinfo">sshark</span></div></div></div><div id="comment-tools-53941" class="comment-tools"></div><div class="clear"></div><div id="comment-53941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

