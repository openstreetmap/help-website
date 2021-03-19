+++
type = "question"
title = "Coap 7-Coap 8 Disector problems"
description = '''Hello everyone,  I recently upgraded to version Version 1.10.3 (SVN Rev 53022 from /trunk-1.10) from version 1.7.1 and have noticed that the when dissecting coap7-coap8 messages are not being decoded correctly. Specifically I am referring to the first option of all COAP messages [coap-problem.pcapng...'''
date = "2013-11-12T19:06:00Z"
lastmod = "2013-11-19T10:40:00Z"
weight = 26917
keywords = [ "dissector", "coap" ]
aliases = [ "/questions/26917" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Coap 7-Coap 8 Disector problems](/questions/26917/coap-7-coap-8-disector-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26917-score" class="post-score" title="current number of votes">0</div><span id="post-26917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I recently upgraded to version Version 1.10.3 (SVN Rev 53022 from /trunk-1.10) from version 1.7.1 and have noticed that the when dissecting coap7-coap8 messages are not being decoded correctly. Specifically I am referring to the first option of all COAP messages [<a href="https://www.dropbox.com/s/dtjspjjzod443kc/coap-problem.pcapng">coap-problem.pcapng</a>].</p><p>Is there a way to "downgrade" the dissector?</p><p>I imagine the right way to go about it is to update/fix the dissector. However I am a complete beginner when it comes to how to do this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-coap" rel="tag" title="see questions tagged &#39;coap&#39;">coap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '13, 19:06</strong></p><img src="https://secure.gravatar.com/avatar/84d0d36fb6753c5a4269bec6d5ec494b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maguirre&#39;s gravatar image" /><p><span>maguirre</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maguirre has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Nov '13, 19:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-26917" class="comments-container"></div><div id="comment-tools-26917" class="comment-tools"></div><div class="clear"></div><div id="comment-26917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26918"></span>

<div id="answer-container-26918" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26918-score" class="post-score" title="current number of votes">1</div><span id="post-26918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maguirre has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are running on Windows, you can just re-install an earlier version of Wireshark. (The existing version will be removed). (or: do an uninstall first before installing the new version). (See the download section of wireshark.org for older Windows versions).</p><p>If you are running on a different platform, I would expect that you should be able to uninstall Wireshark and then install a previous version using tools/repositories available on that platform. (I'm assuming that the Wireshark 1.7 being used was not built manually [which may be an incorrect assumption]).</p><p>In any case, version 1.7.1 was a development Wireshark version; I suggest you try the latest "old stable release": v 1.8.11</p><p>Also: if you feel that there's been a regression, please file a bug report at bugs.wireshark.org with the details and attach the capture file.</p><p>That way the issue can be tracked and addressed as needed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '13, 19:24</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Nov '13, 19:36</strong> </span></p></div></div><div id="comments-container-26918" class="comments-container"><span id="26923"></span><div id="comment-26923" class="comment"><div id="post-26923-score" class="comment-score"></div><div class="comment-text"><p>It appears that there have been a number of updates to the COAP dissector (some of which which appeared in Wireshark 1.10) to reflect changes in the spec.</p><p>(See some of the "commit log" entries below.</p><p>Are there different implementations of COAP "in the wild" such that the dissector needs to be able to handle different versions ??</p><p>Based upon the comments in the Wireshark COAP dissector source, it appears that the COAP versions supported by Wireshark are as follows:</p><pre><code>Wireshark 1.8:       draft-ietf-core-coap-07.txt
Wireshark 1.10:      draft-ietf-core-coap-14.txt
Wiresharl 1.11(dev): draft-ietf-core-coap-17.txt</code></pre><p>=============</p><p>(Some commit log entries for the COAP dissector).</p><hr /><p>r49882 | 2013-06-11 01:31:10 -0400</p><p>There were some changes in how to specify the length or give a bigger option delta. This is now implemented how it is specified in CoAP draft 17. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8780">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8780</a></p><hr /><p>r49881 | 2013-06-11 01:27:47 -0400</p><p>There is no option length attribute any more there is just the end of options marker. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8780">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8780</a></p><hr /><p>r49880 | 2013-06-11 01:23:52 -0400</p><p>The field named Transaction ID is named Message ID in the RFC draft version 17 <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8780">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8780</a></p><hr /><p>r49879 | 2013-06-11 01:20:33 -0400</p><p>The token is not an option any more, but it is now in the main header. This was done between CoAP draft 12 and 13 and still exists in CoAP draft 17.</p><h2 id="httpsbugs.wireshark.orgbugzillashow_bug.cgiid8780"><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8780">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8780</a></h2><p>r48471 | 2013-03-21 20:12:44 -0400</p><p>via <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8070">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8070</a></p><p>Update CoAP dissector to the latest spec from the IETF, and make several more fields filterable.</p></div><div id="comment-26923-info" class="comment-info"><span class="comment-age">(12 Nov '13, 20:15)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="27108"></span><div id="comment-27108" class="comment"><div id="post-27108-score" class="comment-score"></div><div class="comment-text"><p>CoAP has been an approved standard since 2013-07-11 (draft-ietf-core-coap-18), and there is little point in keeping support for pre-13 versions of the protocol around. Note that -13 to -18 are essentially the same except for the Accept option, and with a little tweak to the Accept option you might even support both the option number 16 used in -13 to -17 and the option number 17 that is the approved standard.</p><p>If you really need any pre-13 versions, it is probably best to use the Lua dissector to continue support for old versions of CoAP.</p></div><div id="comment-27108-info" class="comment-info"><span class="comment-age">(19 Nov '13, 10:21)</span> <span class="comment-user userinfo">cabo</span></div></div><span id="27109"></span><div id="comment-27109" class="comment"><div id="post-27109-score" class="comment-score"></div><div class="comment-text"><p>Thanks Bill, It appears the standard changed so much that now the dissector doesn't quite understand COAP-7-8. While I think it makes sense to stay using older versions until my devices implement the latest Coap Standard. However given that the work was already done wouldn't it make sense to support several versions of the standard by using different dissectors?</p></div><div id="comment-27109-info" class="comment-info"><span class="comment-age">(19 Nov '13, 10:40)</span> <span class="comment-user userinfo">maguirre</span></div></div></div><div id="comment-tools-26918" class="comment-tools"></div><div class="clear"></div><div id="comment-26918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

