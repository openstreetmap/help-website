+++
type = "question"
title = "Multiple .c files"
description = '''Hi, I&#x27;m having trouble compiling multiple source files. Following the README.plugins, I added the DISSECTOR_INCLUDES and DISSECTOR_SUPPORT_SRC variables to Makefile.common. Additionally, according to this correspondence, I added the DISSECTOR_SUPPORT_SRC variable under my dissector_la_SOURCES variab...'''
date = "2014-06-05T11:10:00Z"
lastmod = "2014-06-06T14:04:00Z"
weight = 33457
keywords = [ "plugin", "dissectors", "dissector", "plugins" ]
aliases = [ "/questions/33457" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple .c files](/questions/33457/multiple-c-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33457-score" class="post-score" title="current number of votes">0</div><span id="post-33457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm having trouble compiling multiple source files. Following the README.plugins, I added the DISSECTOR_INCLUDES and DISSECTOR_SUPPORT_SRC variables to Makefile.common. Additionally, according to <a href="http://t72538.network-wireshark-development.networkbuzz.info/using-dissector-support-src-t72538.html">this correspondence</a>, I added the DISSECTOR_SUPPORT_SRC variable under my dissector_la_SOURCES variable. However, when I make, it says that there is nothing to be done. I've also tried copying other what plugins have (opcua, to be precise), which also includes adding the DISSECTOR_* variables to Makefile, Makefile.in, Makefile.am, etc. I'm developing on Wireshark 1.0.15 (for reasons).</p><p>EDIT: Here is what my Makefile.common looks like</p><pre><code>...
PLUGIN_NAME = xxx
DISSECTOR_SRC = \
   packet-xxx.c
DISSECTOR_INCLUDES = \
   xxxhelper.h
DISSECTOR_SUPPORT_SRC = \
   xxxhelper.c
...</code></pre><p>EDIT2: Here is my Makefile</p><pre><code>...
xxx_la_SOURCES = \
    plugin.c \
    moduleinfo.h \
    $(DISSECTOR_SRC) \
    $(DISSECTOR_INCLUDES) \
    $(DISSECTOR_SUPPORT_SRC)
...</code></pre><p>EDIT3: Here's the make -d output: <a href="https://www.dropbox.com/s/gwtybcv73cyfh24/output.txt">https://www.dropbox.com/s/gwtybcv73cyfh24/output.txt</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-dissectors" rel="tag" title="see questions tagged &#39;dissectors&#39;">dissectors</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '14, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/7781069f122c3b3eef20438565e7e36f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barney&#39;s gravatar image" /><p><span>barney</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barney has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jun '14, 11:27</strong> </span></p></div></div><div id="comments-container-33457" class="comments-container"><span id="33466"></span><div id="comment-33466" class="comment"><div id="post-33466-score" class="comment-score">1</div><div class="comment-text"><p>Is that really with a colon at the end of xxxhelper.c:</p><p>Did you go trough the autogen.sh &amp;&amp; ./configure &amp;&amp; make dance or just make?</p></div><div id="comment-33466-info" class="comment-info"><span class="comment-age">(05 Jun '14, 12:55)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="33468"></span><div id="comment-33468" class="comment"><div id="post-33468-score" class="comment-score"></div><div class="comment-text"><p>No, my bad, that was a typo. Also, yes, I tried to autogen/configure/make and still no luck.</p></div><div id="comment-33468-info" class="comment-info"><span class="comment-age">(05 Jun '14, 13:19)</span> <span class="comment-user userinfo">barney</span></div></div><span id="33476"></span><div id="comment-33476" class="comment"><div id="post-33476-score" class="comment-score"></div><div class="comment-text"><p>what is the output of the following command?</p><blockquote><p>make -d</p></blockquote></div><div id="comment-33476-info" class="comment-info"><span class="comment-age">(05 Jun '14, 13:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33477"></span><div id="comment-33477" class="comment"><div id="post-33477-score" class="comment-score"></div><div class="comment-text"><p>I'm a little clueless about make, should I post the entire output (~22k lines)? The tail of it is:</p><pre><code>...
       Prerequisite `/usr/local/include/protobuf-c/protobuf-c.h&#39; is older than target `packet-xxx.lo&#39;.
      No need to remake target `packet-xxx.lo&#39;.
     Finished prerequisites of target file `xxx.la&#39;.
     Prerequisite `plugin.lo&#39; is older than target `xxx.la&#39;.
     Prerequisite `packet-xxx.lo&#39; is older than target `xxx.la&#39;.
    No need to remake target `xxx.la&#39;.
   Finished prerequisites of target file `all-am&#39;.
  Must remake target `all-am&#39;.
  Successfully remade target file `all-am&#39;.
 Finished prerequisites of target file `all&#39;.
Must remake target `all&#39;.
Successfully remade target file `all&#39;.
make: Nothing to be done for `all&#39;.</code></pre><p>The .c file I'm trying to include is a Google Protocol Buffer model (compiled using protobuf-c), if that makes a difference.</p></div><div id="comment-33477-info" class="comment-info"><span class="comment-age">(05 Jun '14, 14:24)</span> <span class="comment-user userinfo">barney</span></div></div><span id="33480"></span><div id="comment-33480" class="comment"><div id="post-33480-score" class="comment-score"></div><div class="comment-text"><p>can you post the whole file on google drive or dropbox and post the link here?</p></div><div id="comment-33480-info" class="comment-info"><span class="comment-age">(05 Jun '14, 14:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33483"></span><div id="comment-33483" class="comment not_top_scorer"><div id="post-33483-score" class="comment-score"></div><div class="comment-text"><p>Here's the make -d output: <a href="https://www.dropbox.com/s/gwtybcv73cyfh24/output.txt">https://www.dropbox.com/s/gwtybcv73cyfh24/output.txt</a></p></div><div id="comment-33483-info" class="comment-info"><span class="comment-age">(05 Jun '14, 15:33)</span> <span class="comment-user userinfo">barney</span></div></div></div><div id="comment-tools-33457" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-33457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33531"></span>

<div id="answer-container-33531" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33531-score" class="post-score" title="current number of votes">0</div><span id="post-33531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="barney has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I figured it out by stepping through a diff. You also need to add to the Makefile at least two more lines, one for the .Plo (e.g. include ./$(DEPDIR)/xxxhelper.c.Plo) and the other for the .lo file (add the line to xxx_la_OBJECTS).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '14, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/7781069f122c3b3eef20438565e7e36f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barney&#39;s gravatar image" /><p><span>barney</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barney has one accepted answer">100%</span></p></div></div><div id="comments-container-33531" class="comments-container"></div><div id="comment-tools-33531" class="comment-tools"></div><div class="clear"></div><div id="comment-33531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

