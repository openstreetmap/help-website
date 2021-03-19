+++
type = "question"
title = "So many issues changing from MSVC 2013 compiler to MSVC 2012 Compiler"
description = '''I am trying to build a plugin using the 1.12.7 source code of wireshark. I began using MSVC 2013 to compile my code, but now I have switched to MSVC 2012. I have uninstalled MSVC 2013 and have changed all the variables to MSVC (the MSVC Variant, my command line call, my Qt version) but now whenever ...'''
date = "2015-08-24T15:48:00Z"
lastmod = "2015-08-26T14:20:00Z"
weight = 45329
keywords = [ "msvc", "2012" ]
aliases = [ "/questions/45329" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [So many issues changing from MSVC 2013 compiler to MSVC 2012 Compiler](/questions/45329/so-many-issues-changing-from-msvc-2013-compiler-to-msvc-2012-compiler)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45329-score" class="post-score" title="current number of votes">0</div><span id="post-45329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build a plugin using the 1.12.7 source code of wireshark. I began using MSVC 2013 to compile my code, but now I have switched to MSVC 2012. I have uninstalled MSVC 2013 and have changed all the variables to MSVC (the MSVC Variant, my command line call, my Qt version) but now whenever I compile my plugin it completely crashes. It gives me &gt;100 errors like " error c2275: 'dissector_handle_t' : illegal use of this type as an expression. c:\development\wireshark-1.12.7\epan/packet.h(88) : see declaration of 'dissector_handle_t" and similar ones about each guint__ variable proto_item and proto_tree, exc.</p><p>It recognizes the types but for some reason it can't resolve me using them.</p><p>I'm very confused and frustrated, can you think of any reason this might be happening?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-msvc" rel="tag" title="see questions tagged &#39;msvc&#39;">msvc</span> <span class="post-tag tag-link-2012" rel="tag" title="see questions tagged &#39;2012&#39;">2012</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '15, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/8f99f97ead483c8f43cf63e9b3d17f7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j-demars&#39;s gravatar image" /><p><span>j-demars</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j-demars has no accepted answers">0%</span></p></div></div><div id="comments-container-45329" class="comments-container"></div><div id="comment-tools-45329" class="comment-tools"></div><div class="clear"></div><div id="comment-45329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45340"></span>

<div id="answer-container-45340" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45340-score" class="post-score" title="current number of votes">0</div><span id="post-45340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="j-demars has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're planning to build a plug-in that works with the 1.12.x release versions of Wireshark then you should use VS2010 SP1, as that's the compiler used for those versions, as detailed in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChToolsMSChain.html#_toolchain_package_alternatives">Developers Guide</a>.</p><p>Also note that building the Qt version isn't recommended for 1.12.x, it's very much just an experiment, use the 1.99.x sources for Qt builds.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '15, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45340" class="comments-container"><span id="45351"></span><div id="comment-45351" class="comment"><div id="post-45351-score" class="comment-score"></div><div class="comment-text"><p>I have changed everything so that I am now using MSVC 2010 with SP1, but I am still getting the same errors.</p></div><div id="comment-45351-info" class="comment-info"><span class="comment-age">(25 Aug '15, 15:54)</span> <span class="comment-user userinfo">j-demars</span></div></div><span id="45362"></span><div id="comment-45362" class="comment"><div id="post-45362-score" class="comment-score"></div><div class="comment-text"><p>What's the output of <code>nmake -f Makefile.nmake verify_tools</code>?</p></div><div id="comment-45362-info" class="comment-info"><span class="comment-age">(26 Aug '15, 02:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="45371"></span><div id="comment-45371" class="comment"><div id="post-45371-score" class="comment-score"></div><div class="comment-text"><p>I figured out what the issue is: I was declaring guints in the middle of a method (ie: not immediately after a { - which is okay for cpp files) and since the 2013 is smart enough to see that that's what that is, it was letting it fly, but going back to the old version of MSVCs made it break. Declaring the variables right after the { in each section of the code solved all my issues! Thanks!</p></div><div id="comment-45371-info" class="comment-info"><span class="comment-age">(26 Aug '15, 14:20)</span> <span class="comment-user userinfo">j-demars</span></div></div></div><div id="comment-tools-45340" class="comment-tools"></div><div class="clear"></div><div id="comment-45340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

