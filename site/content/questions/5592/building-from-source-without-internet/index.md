+++
type = "question"
title = "Building from source without internet"
description = '''I&#x27;m developing on a laptop without internet access. The problem arises when I enter nmake -f Makefile.nmake setup. I fail because it tries to use wget to get the library files from the internet. I have all the appropriate library files on the laptop without internet, but where do I put them so wires...'''
date = "2011-08-09T11:14:00Z"
lastmod = "2011-08-09T18:40:00Z"
weight = 5592
keywords = [ "source", "build", "internet" ]
aliases = [ "/questions/5592" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Building from source without internet](/questions/5592/building-from-source-without-internet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5592-score" class="post-score" title="current number of votes">0</div><span id="post-5592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm developing on a laptop without internet access. The problem arises when I enter <code>nmake -f Makefile.nmake setup</code>. I fail because it tries to use wget to get the library files from the internet.</p><p>I have all the appropriate library files on the laptop without internet, but where do I put them so wireshark can use them? Does anyone have a set of instructions to follow to build wireshark without internet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-internet" rel="tag" title="see questions tagged &#39;internet&#39;">internet</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '11, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/1c6ffc8d55b39ae552af734e35307f71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dean%20Wormer&#39;s gravatar image" /><p><span>Dean Wormer</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dean Wormer has no accepted answers">0%</span></p></div></div><div id="comments-container-5592" class="comments-container"></div><div id="comment-tools-5592" class="comment-tools"></div><div class="clear"></div><div id="comment-5592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5595"></span>

<div id="answer-container-5595" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5595-score" class="post-score" title="current number of votes">2</div><span id="post-5595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dean Wormer has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>During the build process, Wireshark downloads its dependencies to <code>C:\wireshark-win32-libs</code> (assuming you are following the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html" title="Developer&#39;s Guide">Win32 Step-By-Step</a> instructions). This is the folder in which you should place these files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '11, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-5595" class="comments-container"><span id="5596"></span><div id="comment-5596" class="comment"><div id="post-5596-score" class="comment-score"></div><div class="comment-text"><p>So I took the files from http://anonsvn.wireshark.org/wireshark-win32-libs/trunk/packages</p><p>In the directory you mention, do I put the .zip files and let <code>nmake -f Makefile.nmake setup</code> take care of it? Do I extract the folders, extract the dlls and just run <code>nmake -f Makefile.nmake all</code>?</p><p>Sorry for the noobish questions. I appreciate your help</p></div><div id="comment-5596-info" class="comment-info"><span class="comment-age">(09 Aug '11, 12:31)</span> <span class="comment-user userinfo">Dean Wormer</span></div></div><span id="5599"></span><div id="comment-5599" class="comment"><div id="post-5599-score" class="comment-score"></div><div class="comment-text"><p>placing the .zip archives in the folder and running <code>nmake -f Makefile.nmake</code> should be sufficient. YMMV since building on Windows without directly following the steps in the developer's guide is always a bit tricky.</p></div><div id="comment-5599-info" class="comment-info"><span class="comment-age">(09 Aug '11, 12:55)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="5604"></span><div id="comment-5604" class="comment"><div id="post-5604-score" class="comment-score">2</div><div class="comment-text"><p>Once you have all the dependency files, go ahead and run <code>nmake -f Makefile.nmake setup</code>, which will run the verify_tools, clean_setup and process_libs targets. When you get to the process_libs part, you'll see messages such as, <em>"File <code>blah.zip</code> already there; not retrieving"</em>. You only need to run setup once (unless you want to update any libraries). When the setup completes, you're ready to run <code>nmake -f Makefile.nmake all</code>. If you want to create an installer, you'll need to get other stuff though, such as the NSIS installer and vcredist_x86.exe. See the Win32 guide for more details.</p></div><div id="comment-5604-info" class="comment-info"><span class="comment-age">(09 Aug '11, 18:40)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-5595" class="comment-tools"></div><div class="clear"></div><div id="comment-5595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

