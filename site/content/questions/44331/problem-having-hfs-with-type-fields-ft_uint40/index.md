+++
type = "question"
title = "Problem having hf&#x27;s with type fields &gt; FT_UINT40"
description = '''Hi, I am having problems displaying hf&#x27;s whose type is greater than FT_UINT40 (ie FT_UINT48, 56, and most annoyingly 64).  Hf in question: { &amp;amp;hf_ieee802154g_aux_sec_key_source64,  { &quot;Key Source&quot;, &quot;wpantemp.aux_sec.key_source_64&quot;, FT_UINT64, BASE_HEX, NULL, 0x0,  &quot;Key Source for processing of the...'''
date = "2015-07-21T11:50:00Z"
lastmod = "2015-07-22T09:46:00Z"
weight = 44331
keywords = [ "ft_uint64190" ]
aliases = [ "/questions/44331" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem having hf's with type fields &gt; FT\_UINT40](/questions/44331/problem-having-hfs-with-type-fields-ft_uint40)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44331-score" class="post-score" title="current number of votes">0</div><span id="post-44331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am having problems displaying hf's whose type is greater than FT_UINT40 (ie FT_UINT48, 56, and most annoyingly 64).</p><p>Hf in question: { &amp;hf_ieee802154g_aux_sec_key_source64, { "Key Source", "wpantemp.aux_sec.key_source_64", FT_UINT64, BASE_HEX, NULL, 0x0, "Key Source for processing of the protected frame", HFILL } },</p><p>I originally developed my dissector with the GTK developer version and had no problem, but now when I copy the plugin into c:\"Program Files"\Wireshark\plugins\1.12.6, and run the executable I get the error (for FT_UINT64 in the "Key Source" hf)</p><p>11:31:29: Err Field 'Key Source' (wpantemp.aux_sec.key_source_64) is signed (FT_UINT24) but is being displayed as unsigned (BASE_HEX).</p><p>If I change the FT_UINT64 to 54, the error changes to FT_UINT16, and also for FT_UINT48 and FT_UINT8.</p><p>I have commented out the part in the code that adds an item with this header format, and I still get the error so I am very confused. Any thoughts?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ft_uint64190" rel="tag" title="see questions tagged &#39;ft_uint64190&#39;">ft_uint64190</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '15, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/8f99f97ead483c8f43cf63e9b3d17f7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j-demars&#39;s gravatar image" /><p><span>j-demars</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j-demars has no accepted answers">0%</span></p></div></div><div id="comments-container-44331" class="comments-container"></div><div id="comment-tools-44331" class="comment-tools"></div><div class="clear"></div><div id="comment-44331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44332"></span>

<div id="answer-container-44332" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44332-score" class="post-score" title="current number of votes">0</div><span id="post-44332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="j-demars has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are compiling your plugin with Wireshark master branch (aka Wireshark 1.99.x), and then trying to run the compiled plugin with master-1.12 branch (aka Wireshark 1.12.x). This cannot work as there is no stable API between major versions that would allow a single plugin to run on all releases. We do ensure compatibility between minor releases though (all 1.12.x versions for example).</p><p>What you need to do is compile your plugin against each Wireshark version you intend to use. Which means compiling it both with master and master-1.12 branch in your case. And at the same time adapt / modify your code so that it can compile with each branch (as APIs can change or some functionalities could be missing in older branch).</p><p>PS: for reference your issue comes from the fact that ftenum enum definition changed between both branches, with new values inserted between FT_UINT32 and FT_UINT64, and between FT_INT32 and FT_INT64. But many other changes were done in master branch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jul '15, 12:44</strong> </span></p></div></div><div id="comments-container-44332" class="comments-container"><span id="44345"></span><div id="comment-44345" class="comment"><div id="post-44345-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the answer! I am wondering how I can go about compiling it with a specific branch? Is there some variable I need to change in a makefile?</p></div><div id="comment-44345-info" class="comment-info"><span class="comment-age">(21 Jul '15, 13:31)</span> <span class="comment-user userinfo">j-demars</span></div></div><span id="44352"></span><div id="comment-44352" class="comment"><div id="post-44352-score" class="comment-score"></div><div class="comment-text"><p>You need to checkout the corresponding branch using 'git checkout master-1.12' command if you are a git clone, or download the corresponding tarball. Then add your plugin in the source code (as you did with master branch) and recompile it.</p></div><div id="comment-44352-info" class="comment-info"><span class="comment-age">(21 Jul '15, 13:52)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="44359"></span><div id="comment-44359" class="comment"><div id="post-44359-score" class="comment-score"></div><div class="comment-text"><p>When you say add the plugin to the source code what specifically do you mean? I think I may have done it wrong in the first place. Recompile wireshark or the plugin? And then what executable do I use?</p></div><div id="comment-44359-info" class="comment-info"><span class="comment-age">(21 Jul '15, 16:08)</span> <span class="comment-user userinfo">j-demars</span></div></div><span id="44361"></span><div id="comment-44361" class="comment"><div id="post-44361-score" class="comment-score"></div><div class="comment-text"><p>To compile your plugin the first time, you downloaded at least the Wireshark header files from master branch (or most probably the full source code). If you want to compile a plugin that runs on Wireshark 1.12.6, you need to recompile your plugin against the header files of master-1.12 branch. So execute the same steps as before, but with another Wireshark code base (I can hardly be more precise without knowing the procedure you used in the first place).</p></div><div id="comment-44361-info" class="comment-info"><span class="comment-age">(21 Jul '15, 23:48)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="44374"></span><div id="comment-44374" class="comment"><div id="post-44374-score" class="comment-score"></div><div class="comment-text"><p>I figured it out. Thank you so much!</p></div><div id="comment-44374-info" class="comment-info"><span class="comment-age">(22 Jul '15, 08:51)</span> <span class="comment-user userinfo">j-demars</span></div></div><span id="44376"></span><div id="comment-44376" class="comment not_top_scorer"><div id="post-44376-score" class="comment-score"></div><div class="comment-text"><p><span>@j-demars</span></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-44376-info" class="comment-info"><span class="comment-age">(22 Jul '15, 09:46)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-44332" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-44332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

