+++
type = "question"
title = "Making Plugin.c (using python)  No Files Found"
description = '''I&#x27;m converting a plugin from an older style nmake version to the newer way of doing Make files. The plugin builds fine on 1.10.7 using the old style system. I have tried following the example at README.plugins with no success. But the new style outputs the below error.  The Makefile.nmake is exactly...'''
date = "2014-05-06T16:13:00Z"
lastmod = "2014-08-13T13:12:00Z"
weight = 32571
keywords = [ "windows", "nmake" ]
aliases = [ "/questions/32571" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Making Plugin.c (using python) No Files Found](/questions/32571/making-pluginc-using-python-no-files-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32571-score" class="post-score" title="current number of votes">1</div><span id="post-32571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm converting a plugin from an older style nmake version to the newer way of doing Make files. The plugin builds fine on 1.10.7 using the old style system. I have tried following the example at <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.plugins">README.plugins</a> with no success. But the new style outputs the below error.<br />
</p><p>The Makefile.nmake is exactly the same as the gryphon one. My Makefile.common is below Is there some other file that I should be editing to get this to work correctly? What else should I be looking at to troubleshoot this?</p><hr /><blockquote><p>PLUGIN_NAME = Fet</p><p>DISSECTOR_SRC = \ packet-fet.c</p><p>DISSECTOR_INCLUDES = \ omFileReader.h \ fet-helper.h \ fet-tap-stats_tree.h \ typeidHash.h \ fetGenOutput.h</p><p>DISSECTOR_SUPPORT_SRC = \ typeidHash.c \ fet-helper.c \ omFileReader.c \ fet-tap-stats_tree.c \ tpdGenOutput.c</p></blockquote><hr /><blockquote><p>Making plugin.c (using python)</p><p>No files found</p><p>NMAKE : fatal error U1077: 'C:\Python27\python.exe' : return code '0x1'</p><p>Stop.</p><p>NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 10. \VC\BIN\nmake.exe"' : return code '0x2'</p><p>Stop.</p></blockquote></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-nmake" rel="tag" title="see questions tagged &#39;nmake&#39;">nmake</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '14, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 May '14, 10:27</strong> </span></p></div></div><div id="comments-container-32571" class="comments-container"></div><div id="comment-tools-32571" class="comment-tools"></div><div class="clear"></div><div id="comment-32571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32802"></span>

<div id="answer-container-32802" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32802-score" class="post-score" title="current number of votes">1</div><span id="post-32802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tlann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The issue comes from not using NONGENERATED_REGISTER_C_FILES in the Makefile.common This tells the python scanner to look in this file for the proto_register function.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '14, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span></p></div></div><div id="comments-container-32802" class="comments-container"><span id="35461"></span><div id="comment-35461" class="comment"><div id="post-35461-score" class="comment-score">1</div><div class="comment-text"><p>Could you explain more how modifying your Makefile.common fixed the problem? I suspect many people who try to update their custom dissectors from an older version will run into this problem.</p></div><div id="comment-35461-info" class="comment-info"><span class="comment-age">(13 Aug '14, 09:49)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="35463"></span><div id="comment-35463" class="comment"><div id="post-35463-score" class="comment-score"></div><div class="comment-text"><p>In the Makefile.common There is a variable for source files called NONGENERATED_C_FILES. The files listed aren't actual dissectors themselves but they are supporting source files listed in here. In this list of files, there should be the MACRO/Variable Expansion thingy called $(NONGENERATED_REGISTER_C_FILES) listed with the source files.<br />
This is three months ago so my memory is a little dim on this but I've looked at the Make files to help figure this out. I believe looking at other plugin files helped me to troubleshoot this. The mate plugin looks like a decent example of this.<br />
So why doesn't anyone vote up answers and questions that are helpful? Shouldn't the correct behavior be promoted?</p></div><div id="comment-35463-info" class="comment-info"><span class="comment-age">(13 Aug '14, 10:03)</span> <span class="comment-user userinfo">tlann</span></div></div></div><div id="comment-tools-32802" class="comment-tools"></div><div class="clear"></div><div id="comment-32802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35466"></span>

<div id="answer-container-35466" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35466-score" class="post-score" title="current number of votes">1</div><span id="post-35466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When updating a plugin dissector to a newer<sup>1</sup> version of wireshark, you need to update all of the essential build files for your plugin to use the new style. There are additional changes to the API that will need adjustment in your code, but by making the below changes, you should be able to begin to build your dissectors and work through the changes.<br />
</p><p>CMakeLists.txt before</p><pre><code>set_target_properties(foo PROPERTIES SOVERSION ${CPACK_PACKAGE_VERSION})
set_target_properties(foo PROPERTIES LINK_FLAGS ${WS_LINK_FLAGS})</code></pre>CMakeLists.txt after<pre><code>set_target_properties(foo PROPERTIES LINK_FLAGS &quot;${WS_LINK_FLAGS}&quot;)
set_target_properties(foo PROPERTIES FOLDER &quot;Plugins&quot;)</code></pre><p>Makefile.am before</p><pre><code>INCLUDES = -I$(top_srcdir) -I(includedir)
# ...
foo_la_SOURCES = \
   plugin.c \
   moduleinfo.h \
   $(DISSECTOR_SRC) \
   $(DISSECTOR_SUPPORT_SRC) \
   $(DISSECTOR_INCLUDES)
# ...
plugin.c: $(DISSECTOR_SRC) $(top_srcdir)/tools/make-dissector-reg \
    $(top_srcdir)/tools/make-dissector-reg.py
   @if test -n &quot;$(PYTHON)&quot;; then \
     echo Making plugin.c with python ; \
     $(PYTHON) $(top_srcdir)/tools/make-dissector-reg.py $(srcdir) \
         plugin $(DISSECTOR_SRC) ; \
   else \
      echo Making plugin.c with shell script ; \
      $(top_srcdir)/tools/make-dissector-reg $(srcdir) \
          $(plugin_src) plugin $(DISSECTOR_SRC) ; \
   fi
# ...
checkapi:
   $(PERL) $(top_srcdir)/tools/checkAPIs.pl -g abort -g termoutput $(DISSECTOR_SRC) $(DISSECTOR_INCLUDES)</code></pre>Makefile.am after<pre><code>include $(top_srcdir/Makefile.am.inc
AM_CPPFLAGS = -I$(top_srcdir)
# ...
foo_la_SOURCES = \
   plugin.c \
   moduleinfo.h \
   $(SRC_FILES) \
   $(HEADER_FILES)
# ...
plugin.c: $(REGISTER_SRC_FILES) Makefile.common $(top_srcdir)/tools/make-dissector-reg \
    $(top_srcdir)/tools/make-dissector-reg.py
    @if test -n &quot;$(PYTHON)&quot;; then \
        echo Making plugin.c with python ; \
        $(PYTHON) $(top_srcdir)/tools/make-dissector-reg.py $(srcdir) \
            plugin $(REGISTER_SRC_FILES) ; \
    else \
        echo Making plugin.c with shell script ; \
        $(top_srcdir)/tools/make-dissector-reg $(srcdir) \
            $(plugin_src) plugin $(REGISTER_SRC_FILES) ; \
    fi
# ...
checkapi:
   $(PERL) $(top_srcdir)/tools/checkAPIs.pl -g abort -g termoutput -build \
   -sourcedir=$(srcdir) \
   $(CLEAN_SRC_FILES) $(CLEAN_HEADER_FILES)</code></pre><p>Makefile.nmake before</p><pre><code>CFLAGS=/D_NEED_VAR_IMPORT_ $(CFLAGS)
DISSECTOR_OBJECTS = $(DISSECTOR_SRC:.c=.obj)
DISSECTOR_SUPPORT_OBJECTS = $(DISSECTOR_SUPPORT_SRC:.c=.obj)
OBJECTS = $(DISSECTOR_OBJECTS) $(DISSECTOR_SUPPORT_OBJECTS) plugin.obj
# ...
!IFDEF PYTHON
plugin.c: $(DISSECTOR_SRC) moduleinfo.h ../../tools/make-dissector-reg.py
    @echo Making plugin.c (using python)
    @$(PYTHON) &quot;../../tools/make-dissector-reg.py&quot; . plugin $(DISSECTOR_SRC)
!ELSE
plugin.c: $(DISSECTOR_SRC) moduleinfo.h ../../tools/make-dissector-reg
    @echo Making plugin.c (using sh)
    @$(SH) ../../tools/make-dissector-reg . plugin $(DISSECTOR_SRC)
!ENDIF</code></pre>Makefile.nmake after<pre><code>CFLAGS=$(CFLAGS)
OBJECTS = $(C_FILES:.c=.obj) $(CPP_FILES:.cpp=.obj) plugin.obj
# ...
!IFDEF PYTHON
plugin.c: $(REGISTER_SRC_FILES) moduleinfo.h ../../tools/make-dissector-reg.py
    @echo Making plugin.c (using python)
    @$(PYTHON) &quot;../../tools/make-dissector-reg.py&quot; . plugin $(REGISTER_SRC_FILES)
!ELSE
plugin.c: $(REGISTER_SRC_FILES) moduleinfo.h ../../tools/make-dissector-reg
    @echo Making plugin.c (using sh)
    @$(SH) ../../tools/make-dissector-reg . plugin $(REGISTER_SRC_FILES)
!ENDIF</code></pre><p>Makefile.common before</p><pre><code>PLUGIN_NAME = foo
# the dissector sources (without any helpers)
DISSECTOR_SRC = \
   packet-foo.c
# corresponding headers
DISSECTOR_INCLUDES =    \
   packet-foo.h
# Dissector helpers. They&#39;re included in the source files in this
# directory, but they&#39;re not dissectors themselves, i.e. they&#39;re not
# used to generate &quot;plugin.c&quot;.
DISSECTOR_SUPPORT_SRC = \&lt;/code&gt;</code></pre><code></code><p>Makefile.common after</p><pre><code>PLUGIN_NAME = foo
# the dissector sources (without any helpers)
NONGENERATED_REGISTER_C_FILES = \
    packet-foo.c
NONGENERATED_C_FILES = \
   $(NONGENERATED_REGISTER_C_FILES)
# corresponding headers
CLEAN_HEADER_FILES =    \
    packet-foo.h
HEADER_FILES = \
   $(CLEAN_HEADER_FILES)
include ../Makefile.common.inc</code></pre><p><sup>1</sup>: I don't know at what point the change actually happened. In my case, I was updating from 1.8 to 1.99.</p></code></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '14, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Aug '14, 13:52</strong> </span></p></div></div><div id="comments-container-35466" class="comments-container"><span id="35467"></span><div id="comment-35467" class="comment"><div id="post-35467-score" class="comment-score"></div><div class="comment-text"><p>This is good information. I think it should go in the wiki.</p></div><div id="comment-35467-info" class="comment-info"><span class="comment-age">(13 Aug '14, 13:12)</span> <span class="comment-user userinfo">tlann</span></div></div></div><div id="comment-tools-35466" class="comment-tools"></div><div class="clear"></div><div id="comment-35466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

