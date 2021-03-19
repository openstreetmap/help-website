+++
type = "question"
title = "./configure gives error --&gt; GTK+ version issue Solaris"
description = '''*** Could not run GTK+ test program, checking why... *** The test program failed to compile or link. See the file config.log for the *** exact error that occured. This usually means GTK+ is incorrectly installed. configure: error: GTK+ 2.4 or later isn&#x27;t available, so Wireshark can&#x27;t be compiled  Pl...'''
date = "2011-08-03T03:49:00Z"
lastmod = "2011-08-03T07:34:00Z"
weight = 5426
keywords = [ "development", "solaris" ]
aliases = [ "/questions/5426" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [./configure gives error --&gt; GTK+ version issue Solaris](/questions/5426/configure-gives-error-gtk-version-issue-solaris)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5426-score" class="post-score" title="current number of votes">0</div><span id="post-5426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>*** Could not run GTK+ test program, checking why...
*** The test program failed to compile or link. See the file config.log for the
*** exact error that occured. This usually means GTK+ is incorrectly installed.
configure: error: GTK+ 2.4 or later isn&#39;t available, so Wireshark can&#39;t be compiled</code></pre><p>Please help guys......</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-solaris" rel="tag" title="see questions tagged &#39;solaris&#39;">solaris</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '11, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/46f1d92dbdd0596560b0f0534d1085b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harshpandya88&#39;s gravatar image" /><p><span>harshpandya88</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harshpandya88 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Aug '11, 23:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5426" class="comments-container"><span id="5429"></span><div id="comment-5429" class="comment"><div id="post-5429-score" class="comment-score"></div><div class="comment-text"><p>please help friends......</p></div><div id="comment-5429-info" class="comment-info"><span class="comment-age">(03 Aug '11, 05:24)</span> <span class="comment-user userinfo">harshpandya88</span></div></div></div><div id="comment-tools-5426" class="comment-tools"></div><div class="clear"></div><div id="comment-5426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5438"></span>

<div id="answer-container-5438" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5438-score" class="post-score" title="current number of votes">1</div><span id="post-5438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Somewhere in the config.log it will tell you why the program did not compile or link. You have to find that section of the file to know the problem.</p><p>Since you're Solaris and I'm guessing Solaris 10, you could be running into Sun bug 6213382. The fix for that is to edit the file /usr/lib/pkgconfig/gthread-2.0.pc and:</p><p>1) remove "-mt" from the 2 places it appears 2) add "-D_REENTRANT" to Cflags</p><p>It may also be that you need to set LD_LIBRARY_PATH (to point to the location of GTK) but since it appears you're using Sun's version of GTK, I'd guess that's not the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-5438" class="comments-container"><span id="5440"></span><div id="comment-5440" class="comment"><div id="post-5440-score" class="comment-score"></div><div class="comment-text"><p>thx 4 kind help That error has been solved now by above steps but still getting error below</p><p>configure:20200: checking pcap.h presence configure:20200: gcc -E -I/usr/local/include conftest.c conftest.c:28:18: pcap.h: No such file or directory configure:20200: $? = 1</p><p>configure:20200: checking for pcap.h configure:20200: result: no configure:20207: error: Header file pcap.h not found; if you installed libpcap from source, did you also do "make install-incl", and if you installed a binary package of libpcap, is there also a developer's package of libpcap, and did you also install that package?</p></div><div id="comment-5440-info" class="comment-info"><span class="comment-age">(03 Aug '11, 06:31)</span> <span class="comment-user userinfo">harshpandya88</span></div></div><span id="5441"></span><div id="comment-5441" class="comment"><div id="post-5441-score" class="comment-score"></div><div class="comment-text"><p>Well, where do you have the libpcap header files installed? configure is expecting them in /usr/local/include .</p><p>If you don't need to capture you can configure --without-libpcap . If the header file and library are installed somewhere else you can configure --with-pcap=/path/to/where/they/are</p></div><div id="comment-5441-info" class="comment-info"><span class="comment-age">(03 Aug '11, 06:40)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="5442"></span><div id="comment-5442" class="comment"><div id="post-5442-score" class="comment-score"></div><div class="comment-text"><p>My server doesn't have libpcap installed, i even tried with "--without" option, but still getting the same error again...</p><p>I think, i must have to install libcap now..</p><p>kindly suggest if any suitable way !!</p></div><div id="comment-5442-info" class="comment-info"><span class="comment-age">(03 Aug '11, 06:49)</span> <span class="comment-user userinfo">harshpandya88</span></div></div><span id="5444"></span><div id="comment-5444" class="comment"><div id="post-5444-score" class="comment-score"></div><div class="comment-text"><p>Doh! Typo: it should be "--without-pcap". Sorry, doing too many things at once.</p><p>If that doesn't work, you'll probably have to install libpcap.</p></div><div id="comment-5444-info" class="comment-info"><span class="comment-age">(03 Aug '11, 07:17)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="5445"></span><div id="comment-5445" class="comment"><div id="post-5445-score" class="comment-score"></div><div class="comment-text"><p>thnx JeffMoriss.. this option worked. and finaly ./configure has completed successfully..</p><p>Let me try running make now.. and hopefully it should work.. :)</p></div><div id="comment-5445-info" class="comment-info"><span class="comment-age">(03 Aug '11, 07:26)</span> <span class="comment-user userinfo">harshpandya88</span></div></div><span id="5446"></span><div id="comment-5446" class="comment not_top_scorer"><div id="post-5446-score" class="comment-score"></div><div class="comment-text"><p>make: Fatal error: Can't find `makefile': No such file or directory</p><p>:(</p></div><div id="comment-5446-info" class="comment-info"><span class="comment-age">(03 Aug '11, 07:34)</span> <span class="comment-user userinfo">harshpandya88</span></div></div></div><div id="comment-tools-5438" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-5438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5430"></span>

<div id="answer-container-5430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5430-score" class="post-score" title="current number of votes">0</div><span id="post-5430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the error indicates, GTK 2.4 is missing from your machine. You can <a href="http://www.eiffelroom.org/blog/larryliuming/how_to_install_gtk_from_source_code_on_solaris_10">build it</a> from source.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-5430" class="comments-container"><span id="5433"></span><div id="comment-5433" class="comment"><div id="post-5433-score" class="comment-score"></div><div class="comment-text"><p>What does <code>config.log</code> show as the error?</p></div><div id="comment-5433-info" class="comment-info"><span class="comment-age">(03 Aug '11, 05:59)</span> <span class="comment-user userinfo">bstn</span></div></div><span id="5439"></span><div id="comment-5439" class="comment"><div id="post-5439-score" class="comment-score"></div><div class="comment-text"><p>from the error it is found that PKG_CONFIG script is pointing to the old copy of GTK version, how i can set modify your LD_LIBRARY_PATH enviroment variable to point it to a newer version already installed in system.</p></div><div id="comment-5439-info" class="comment-info"><span class="comment-age">(03 Aug '11, 06:20)</span> <span class="comment-user userinfo">harshpandya88</span></div></div></div><div id="comment-tools-5430" class="comment-tools"></div><div class="clear"></div><div id="comment-5430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

