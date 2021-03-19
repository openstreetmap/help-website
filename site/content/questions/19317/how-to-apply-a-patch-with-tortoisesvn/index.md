+++
type = "question"
title = "How to apply a Patch with TortoiseSVN"
description = '''Hi How can I apply a Patch to Wireshark using TortoiseSVN application?'''
date = "2013-03-08T14:39:00Z"
lastmod = "2013-03-09T00:17:00Z"
weight = 19317
keywords = [ "patch" ]
aliases = [ "/questions/19317" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to apply a Patch with TortoiseSVN](/questions/19317/how-to-apply-a-patch-with-tortoisesvn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19317-score" class="post-score" title="current number of votes">0</div><span id="post-19317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>How can I apply a Patch to Wireshark using TortoiseSVN application?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-patch" rel="tag" title="see questions tagged &#39;patch&#39;">patch</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '13, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/5318038b31cc44ad026905167c9b1824?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve21&#39;s gravatar image" /><p><span>steve21</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve21 has no accepted answers">0%</span></p></div></div><div id="comments-container-19317" class="comments-container"></div><div id="comment-tools-19317" class="comment-tools"></div><div class="clear"></div><div id="comment-19317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19318"></span>

<div id="answer-container-19318" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19318-score" class="post-score" title="current number of votes">0</div><span id="post-19318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not really a Wireshark question.</p><p>Anyway a patch file modifies the source code of an application not the binary. You'll need to get a Wireshark development environment setup first, check you can build an unmodified version, then apply the patch and rebuild.</p><p>To apply the patch with Tortoise, right click on the top level directory and from the Tortoise menu select "Apply patch", then select the patch file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '13, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19318" class="comments-container"><span id="19319"></span><div id="comment-19319" class="comment"><div id="post-19319-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Thanks for your answer. Still I could not apply it. Do you know any other method to apply it?</p><p>1) I have Download the wireshark source code and compile with Microsoft Visual Studio nmake -f Makefile.nmake setup nmake -f Makefile.nmake all 2) Checkout the following patch file from our SVN repositoy and try to apply the Patch using Tortoise SVN. 3) Finally I compile the wireshark source code using the command 'nmake -f Makefile.nmake all' 4) Run wireshark from the directory wireshark/wireshark-gtk2 using the command 'wireshark.exe'</p></div><div id="comment-19319-info" class="comment-info"><span class="comment-age">(08 Mar '13, 15:21)</span> <span class="comment-user userinfo">steve21</span></div></div><span id="19320"></span><div id="comment-19320" class="comment"><div id="post-19320-score" class="comment-score"></div><div class="comment-text"><p>So presumably</p><blockquote><p>2) Checkout the following patch file from our SVN repositoy and try to apply the Patch using Tortoise SVN.</p></blockquote><p>failed, if you "could not apply [the patch]". What happened when you tried it? Did Tortoise report an error? If so, what was the error?</p></div><div id="comment-19320-info" class="comment-info"><span class="comment-age">(08 Mar '13, 15:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="19321"></span><div id="comment-19321" class="comment"><div id="post-19321-score" class="comment-score"></div><div class="comment-text"><p>I am not so sure but when I apply it, I see 3 TortoiseUdiff windows with message 'Rejected patch hunks for 'packet-gprscdr.c'</p><p>(Converted to a comment in keeping with the convention for using ask.wireshark.org. Please see the FAQ).</p></div><div id="comment-19321-info" class="comment-info"><span class="comment-age">(08 Mar '13, 15:38)</span> <span class="comment-user userinfo">steve21</span></div></div><span id="19325"></span><div id="comment-19325" class="comment"><div id="post-19325-score" class="comment-score"></div><div class="comment-text"><p>"rejected patch hunks..." means just that. At least some parts (hunks) of the patch didn't apply cleanly to the source file.</p><p>This usually happens because the source file has changed somehow (in the lines affected by the patch) since the patch was made.</p><p>Patch matches lines around the patch before applying the patch.</p><p>So: If you want to fix things manually, you'll need to use an editor to examine the patch file and the source file, determine which patches (if any) did get applied, see why the others didn't get applied, and then update the source file as needed with the un-applied patch hunks.</p></div><div id="comment-19325-info" class="comment-info"><span class="comment-age">(08 Mar '13, 18:11)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="19329"></span><div id="comment-19329" class="comment"><div id="post-19329-score" class="comment-score"></div><div class="comment-text"><p>packet-gprscdr.c is a generated dissector perhaps you should patch or add the asn1 files you presumably changed and regenerate the dissector with asn2wrs or if possibly offer the changes to GPL Wireshark to have them included.</p></div><div id="comment-19329-info" class="comment-info"><span class="comment-age">(09 Mar '13, 00:17)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-19318" class="comment-tools"></div><div class="clear"></div><div id="comment-19318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

