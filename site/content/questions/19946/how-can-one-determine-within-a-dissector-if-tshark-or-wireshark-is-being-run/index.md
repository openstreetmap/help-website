+++
type = "question"
title = "How can one determine within a dissector if tshark or Wireshark is being run?"
description = '''The load time for NFSv4 captures can be reduced by up to 2.5 times by skipping the &#x27;proto_&#x27; routines during the initial load (first pass) of the capture in Wireshark. However, if &#x27;!tree&#x27; is used to detect if this is the first pass, &#x27;Find&#x27;s for text in the Info column fails because during a Find, &#x27;tr...'''
date = "2013-03-29T16:02:00Z"
lastmod = "2013-04-10T09:15:00Z"
weight = 19946
keywords = [ "is_tshark", "is_wireshark", "is_tshark_2pass" ]
aliases = [ "/questions/19946" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can one determine within a dissector if tshark or Wireshark is being run?](/questions/19946/how-can-one-determine-within-a-dissector-if-tshark-or-wireshark-is-being-run)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19946-score" class="post-score" title="current number of votes">0</div><span id="post-19946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The load time for NFSv4 captures can be reduced by up to 2.5 times by skipping the 'proto_' routines during the initial load (first pass) of the capture in Wireshark. However, if '!tree' is used to detect if this is the first pass, 'Find's for text in the Info column fails because during a Find, 'tree' is temporarily set to NULL. If instead the !pinfo-&gt;fd-&gt;flags.visited' is used, Finds work well but tshark's io,stat fails to see the NFS-related field values unless the '-2' (two pass) option of tshark is specified.<br />
</p><p>Is there a way to detect in dissect-nfs.c, via a global variable or by calling a routine, if tshark or Wireshark is being run? If so, is it also possible to detect if tshark's '-2' option was specified?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-is_tshark" rel="tag" title="see questions tagged &#39;is_tshark&#39;">is_tshark</span> <span class="post-tag tag-link-is_wireshark" rel="tag" title="see questions tagged &#39;is_wireshark&#39;">is_wireshark</span> <span class="post-tag tag-link-is_tshark_2pass" rel="tag" title="see questions tagged &#39;is_tshark_2pass&#39;">is_tshark_2pass</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '13, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/fdeb7677d2d5f1503c28986808c87a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="commsguy&#39;s gravatar image" /><p><span>commsguy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="commsguy has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Mar '13, 16:04</strong> </span></p></div></div><div id="comments-container-19946" class="comments-container"></div><div id="comment-tools-19946" class="comment-tools"></div><div class="clear"></div><div id="comment-19946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19947"></span>

<div id="answer-container-19947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19947-score" class="post-score" title="current number of votes">3</div><span id="post-19947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to detect in dissect-nfs.c, via a global variable or by calling a routine, if tshark or Wireshark is being run?</p></blockquote><p>No.</p><blockquote><p>The load time for NFSv4 captures can be reduced by up to 2.5 times by skipping the 'proto_' routines during the initial load (first pass) of the capture in Wireshark.</p></blockquote><p>Which you don't want to do if:</p><ol><li>you have a read filter;</li><li>you're running Wireshark and have a color filter;</li><li>you're running TShark with the -V flag or with -T fields;</li></ol><p>etc..</p><p>The way you determine whether to construct a protocol tree is, err, umm, by looking at the <code>tree</code> parameter.</p><p><code>tree</code> is not necessarily null on the first pass in Wireshark or TShark, and it's not necessarily non-null on subsequent passes.</p><blockquote><p>However, if '!tree' is used to detect if this is the first pass, 'Find's for text in the Info column fails because during a Find, 'tree' is temporarily set to NULL.</p></blockquote><p>If <code>tree</code> is used to control whether any columns are set - i.e., if columns are set only within <code>if (tree)</code> - that's a <em>bug</em>. Columns should be set regardless of whether <code>tree</code> is null or not.</p><p>And <code>tree</code> should not be set to NULL if you're doing a Find looking in the detail pane. It may be set to NULL if you're doing a Find looking in the Info field of the packet list pane, but that's because the protocol tree is not needed to generate the Info column.</p><p>(Also, it's not a case of "temporarily" being set to NULL. It's set to a non-null value iff the protocol tree is needed; it's not as if "non-null" is the standard setting and "null" merely a temporary special setting.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '13, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Mar '13, 19:44</strong> </span></p></div></div><div id="comments-container-19947" class="comments-container"><span id="19964"></span><div id="comment-19964" class="comment"><div id="post-19964-score" class="comment-score"></div><div class="comment-text"><p>Guy, Thanks. That answers my question. It is my understanding that that an 'if' operation (e.g., "if (tree) proto_tree_add_item(tree, hfindex, tvb, offset, 8, ENC_BIG_ENDIAN);") is less costly to performance than making the call to the 'proto_tree_' routine and having it return if tree is NULL because when the routine is called, its arguments have to be pushed and popped off the stack or copied to and read from registers.</p><p>In your opinion is it worthwhile to add an 'if (tree)' check to each proto_tree call or a set of such calls, or does the ugliness they cause outweigh the gains in performance afforded by them?</p></div><div id="comment-19964-info" class="comment-info"><span class="comment-age">(30 Mar '13, 14:32)</span> <span class="comment-user userinfo">commsguy</span></div></div><span id="19966"></span><div id="comment-19966" class="comment"><div id="post-19966-score" class="comment-score"></div><div class="comment-text"><p>The <code>if (tree)</code> takes more code (as the test is done at the call site rather than in the called routine), and the test is done in the called routine anyway, but it avoids the procedure call, so the net result may be positive. If you can bundle multiple calls under one <code>if</code>, there's probably a greater performance improvement.</p><p>It's worth doing it if it makes a big difference (and a 2.5x difference is big); it'd be nice to be able to avoid it, but that goes down the path of dynamic code generation (whether by interpretation of, for example, specialized bytecode, or by using something such as LLVM), which is a bigger project (worthwhile considering, but bigger).</p></div><div id="comment-19966-info" class="comment-info"><span class="comment-age">(30 Mar '13, 20:45)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="20253"></span><div id="comment-20253" class="comment"><div id="post-20253-score" class="comment-score"></div><div class="comment-text"><p>Guy, I spent a great deal of time adding "if (tree)" clauses throughout the packet-nfs.c code and did as much bundling of proto_tree routines within those clauses as possible. To my surprise, there was only a 6% improvement in the load time. At least to me, it doesn't seem worth the time and effort.</p></div><div id="comment-20253-info" class="comment-info"><span class="comment-age">(09 Apr '13, 11:55)</span> <span class="comment-user userinfo">commsguy</span></div></div><span id="20293"></span><div id="comment-20293" class="comment"><div id="post-20293-score" class="comment-score"></div><div class="comment-text"><p>I went over the NFS dissector once again and found that I had only covered about half the code with "if (tree)" checks. I paid special attention to the high volume routines. I completed the work and now I'm seeing a 21% reduction in load time. For me that makes it worth the effort because with the advent of 10Gig networks, captures are becoming much larger (e.g., 2 to 4 million frames).</p></div><div id="comment-20293-info" class="comment-info"><span class="comment-age">(10 Apr '13, 09:15)</span> <span class="comment-user userinfo">commsguy</span></div></div></div><div id="comment-tools-19947" class="comment-tools"></div><div class="clear"></div><div id="comment-19947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

