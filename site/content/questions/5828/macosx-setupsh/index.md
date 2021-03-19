+++
type = "question"
title = "macosx-setup.sh"
description = '''When running the macosx-setup.sh command I get an error. Any ideas what is going on here? I am running Mac OS 10.6.8 and have XCode 3.6.2 installed. In file included from pangocairo-fontmap.c:30: pangocairo-coretext.h:28:26: error: cairo-quartz.h: No such file or directory make[4]: *** [libpangocair...'''
date = "2011-08-23T16:36:00Z"
lastmod = "2011-08-24T03:29:00Z"
weight = 5828
keywords = [ "osx", "build", "header" ]
aliases = [ "/questions/5828" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [macosx-setup.sh](/questions/5828/macosx-setupsh)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5828-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When running the macosx-setup.sh command I get an error. Any ideas what is going on here? I am running Mac OS 10.6.8 and have XCode 3.6.2 installed.</p><p>In file included from pangocairo-fontmap.c:30: pangocairo-coretext.h:28:26: error: cairo-quartz.h: No such file or directory make[4]: *** [libpangocairo_1_0_la-pangocairo-fontmap.lo] Error 1</p></div><div id="question-tags" class="tags-container tags">osx build header</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '11, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/d7d5b1b472290be80f288300c46d8ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nate&#39;s gravatar image" /><p>Nate<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nate has no accepted answers">0%</span></p></div></div><div id="comments-container-5828" class="comments-container"></div><div id="comment-tools-5828" class="comment-tools"></div><div class="clear"></div><div id="comment-5828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5830"></span>

<div id="answer-container-5830" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5830-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The setup script <a href="http://anonsvn.wireshark.org/viewvc/trunk/macosx-setup.sh?revision=38104&amp;view=markup#l153">commented out Cairo</a>. Perhaps you need it. Try running the script with those lines uncommented.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '11, 17:52</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-5830" class="comments-container"><span id="5832"></span><div id="comment-5832" class="comment"><div id="post-5832-score" class="comment-score"></div><div class="comment-text"><p>You should not need Cairo <em>IF</em> you have X11 installed, complete with the X11 SDK (I don't remember whether you need to separately install the X11 SDK or not). As macosx-setup.sh currently builds GTK+ and its support libraries with X11, you need the X11 SDK to build the libraries.</p></div><div id="comment-5832-info" class="comment-info"><span class="comment-age">(23 Aug '11, 17:55)</span> Guy Harris ♦♦</div></div><span id="5848"></span><div id="comment-5848" class="comment"><div id="post-5848-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the hint. As far as I can tell I have X11 and X11 SDK installed.</p></div><div id="comment-5848-info" class="comment-info"><span class="comment-age">(24 Aug '11, 11:53)</span> Nate</div></div></div><div id="comment-tools-5830" class="comment-tools"></div><div class="clear"></div><div id="comment-5830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5835"></span>

<div id="answer-container-5835" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5835-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try updating to the latest SVN version (if you're running macosx-setup.sh, you're building from SVN or from a source tarball built from SVN); if macosx-setup.sh says "Please install X11 and the X11 SDK first.", you need to install X11 and, possibly, the X11 SDK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '11, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-5835" class="comments-container"><span id="5849"></span><div id="comment-5849" class="comment"><div id="post-5849-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I checked out a clean copy of wireshark SVN, uninstalled XCode 3.2.6 and reinstalled with all options selected. I also completely removed my MacPorts install and Mono (it had a few duplicate libraries and an executable, aclocal). After running macosx-setup.sh I get the following:</p><p>You are now prepared to build Wireshark. To do so do:</p><p>autogen.sh appears to have worked as well:</p><p>Now type "./configure [options]" and "make" to compile Wireshark.</p><p>configure failes with:</p><p>checking for GTK+ - version &gt;= 2.12.0... Package cairo was not found in the pkg-config search path.</p><p>Thanks.</p></div><div id="comment-5849-info" class="comment-info"><span class="comment-age">(24 Aug '11, 12:11)</span> Nate</div></div><span id="5850"></span><div id="comment-5850" class="comment"><div id="post-5850-score" class="comment-score"></div><div class="comment-text"><p>Try setting the <code>PKG_CONFIG_PATH</code> environment variable to</p><pre><code>/usr/X11/lib/pkgconfig:/usr/local/lib/pkgconfig</code></pre></div><div id="comment-5850-info" class="comment-info"><span class="comment-age">(24 Aug '11, 12:13)</span> Guy Harris ♦♦</div></div><span id="5851"></span><div id="comment-5851" class="comment"><div id="post-5851-score" class="comment-score"></div><div class="comment-text"><p>Thanks again. We're getting closer. I got through configure after setting the env var. Now I'm getting an error when I call make -j 3 (as instructed by macosx-setup.sh):</p><p>I'll post the error in another comment since it won't fit in this window.</p></div><div id="comment-5851-info" class="comment-info"><span class="comment-age">(24 Aug '11, 12:36)</span> Nate</div></div><span id="5852"></span><div id="comment-5852" class="comment"><div id="post-5852-score" class="comment-score"></div><div class="comment-text"><p>cc1: warnings being treated as errors tcp_graph.c: In function 'expose_event': tcp_graph.c:3231: warning: unused parameter 'widget' tcp_graph.c: In function 'button_press_event': tcp_graph.c:3495: warning: unused parameter 'widget' tcp_graph.c: In function 'motion_notify_event': tcp_graph.c:3532: warning: unused parameter 'widget'</p></div><div id="comment-5852-info" class="comment-info"><span class="comment-age">(24 Aug '11, 12:37)</span> Nate</div></div><span id="5853"></span><div id="comment-5853" class="comment not_top_scorer"><div id="post-5853-score" class="comment-score"></div><div class="comment-text"><p>tcp_graph.c: In function 'button_release_event': tcp_graph.c:3589: warning: unused parameter 'widget' tcp_graph.c: In function 'leave_notify_event': tcp_graph.c:3696: warning: unused parameter 'widget' tcp_graph.c: In function 'enter_notify_event': tcp_graph.c:3706: warning: unused parameter 'widget' make[2]: *** [libui_a-tcp_graph.o] Error 1</p></div><div id="comment-5853-info" class="comment-info"><span class="comment-age">(24 Aug '11, 12:37)</span> Nate</div></div><span id="5854"></span><div id="comment-5854" class="comment not_top_scorer"><div id="post-5854-score" class="comment-score"></div><div class="comment-text"><p>OK, so that means your question is now answered - you cleaned your machine up and set <code>PKG_CONFIG_PATH</code> so it picks up the system version of Cairo.</p><p>The problems you're seeing now are the result of building from top-of-tree SVN; we're in the middle of doing a whole bunch of stuff to support GTK+ 3.x, and sometimes that breaks things. Keep updating your SVN tree, and eventually you'll get something buildable.</p></div><div id="comment-5854-info" class="comment-info"><span class="comment-age">(24 Aug '11, 12:40)</span> Guy Harris ♦♦</div></div><span id="5856"></span><div id="comment-5856" class="comment"><div id="post-5856-score" class="comment-score">1</div><div class="comment-text"><p>After updating from SVN and noticing a new tcp_graph.c downloaded, I rebuilt. It compiled and successfully ran under X11. Thanks for your help.</p></div><div id="comment-5856-info" class="comment-info"><span class="comment-age">(24 Aug '11, 14:35)</span> Nate</div></div></div><div id="comment-tools-5835" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-5835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

