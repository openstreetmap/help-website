+++
type = "question"
title = "How can I use idl2wrs with a dissector?"
description = '''I have installed wireshark, and I wanted to use idl2wrs. I have done everything a specified in the user guide: idl2wrs echo.idl &amp;gt; packet-test-idl.c` cp packet-test-idl.c /dir/where/wireshark/lives/epan/dissectors/  ...changed Makefile.common, then ./configure and make wireshark again. Everything ...'''
date = "2012-02-07T04:23:00Z"
lastmod = "2012-02-09T06:17:00Z"
weight = 8873
keywords = [ "development", "dissector", "build", "idl2wrs" ]
aliases = [ "/questions/8873" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I use idl2wrs with a dissector?](/questions/8873/how-can-i-use-idl2wrs-with-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8873-score" class="post-score" title="current number of votes">1</div><span id="post-8873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed wireshark, and I wanted to use <code>idl2wrs</code>. I have done everything a specified in the user guide:</p><pre><code>idl2wrs echo.idl &gt; packet-test-idl.c`
cp packet-test-idl.c /dir/where/wireshark/lives/epan/dissectors/</code></pre><p>...changed <code>Makefile.common</code>, then <code>./configure</code> and <code>make wireshark</code> again. Everything seemed okay. However, when I start Wireshark, I do not see it in the <code>Edit-&gt;preferences</code> menu, in the protocol list. What can I do differently to fix this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-idl2wrs" rel="tag" title="see questions tagged &#39;idl2wrs&#39;">idl2wrs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '12, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/80fdcdd1446b1855ee2fda6e19cae371?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivana&#39;s gravatar image" /><p><span>ivana</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Feb '12, 07:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8873" class="comments-container"></div><div id="comment-tools-8873" class="comment-tools"></div><div class="clear"></div><div id="comment-8873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8875"></span>

<div id="answer-container-8875" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8875-score" class="post-score" title="current number of votes">2</div><span id="post-8875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You only see dissectors with registered preferences there. Since there aren't any it doesn't show up.</p><p>You could find it through Analyze|Enabled Protocols... and/or through Help|Supported Protocols</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '12, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8875" class="comments-container"><span id="8877"></span><div id="comment-8877" class="comment"><div id="post-8877-score" class="comment-score"></div><div class="comment-text"><p>It isn't there either :|</p></div><div id="comment-8877-info" class="comment-info"><span class="comment-age">(07 Feb '12, 07:59)</span> <span class="comment-user userinfo">ivana</span></div></div><span id="8885"></span><div id="comment-8885" class="comment"><div id="post-8885-score" class="comment-score"></div><div class="comment-text"><p>It's</p><pre><code>./autogen.sh &amp;&amp; ./configure &amp;&amp; make</code></pre><p>to process the changes in Makefile.common and make because a dissector is not part of Wireshark (gasp), it's part of EPAN, found in libwireshark.</p></div><div id="comment-8885-info" class="comment-info"><span class="comment-age">(07 Feb '12, 23:16)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-8875" class="comment-tools"></div><div class="clear"></div><div id="comment-8875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8928"></span>

<div id="answer-container-8928" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8928-score" class="post-score" title="current number of votes">1</div><span id="post-8928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found solution! Maybe someone will find it helpful:</p><ol><li>Converting a CORBA idl file into a Wireshark dissector <code>idl2wrs echo.idl &gt; packet-giop_echo.c</code> (it is important that name is in format: <code>packet-xxxx.c</code>, where <code>xxxx</code> is name of dissector and it should be same as in functions <code>proto_register_handoff_giop_echo</code> and <code>proto_register_giop_echo</code>)<br />
</li><li>Copy the resulting C code to subdirectory <code>epan/dissectors/</code> inside your Wireshark source directory.<br />
<code>cp packet-test-idl.c /dir/where/wireshark/lives/epan/dissectors/</code><br />
</li><li>Adding dissector in Makefile.common(epan/dissectors/)<br />
<code>DISSECTOR_SRC = \</code><br />
<code>packet-test-idl.c \</code><br />
<code>packet-2dparityfec.c \</code><br />
<code>packet-3com-njack.c \</code><br />
<code>...</code><br />
</li><li>Adding dissector in <code>Makefile.in</code> (<code>epan/dissectors/</code>)<ul><li><code>libdissectors_la-packet-giop_echo.lo \</code></li><li><code>packet-giop_echo.c</code></li><li><code>@[email protected]@[email protected] @[email protected]/$(DEPDIR)/libdissectors_la-packet-      [email protected][email protected]_la-packet-echo.lo: packet-echo.c</code></li><li><pre><code>@am[email protected]    if $(LIBTOOL) --tag=CC --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(libdissectors_la_CFLAGS) $(CFLAGS) -MT libdissectors_la-packet-echo.lo -MD -MP -MF &quot;$(DEPDIR)/libdissectors_la-packet-echo.Tpo&quot; -c -o libdissectors_la-packet-echo.lo test -f &#39;packet-echo.c&#39; || echo &#39;$(srcdir)/&#39;packet-echo.c; 
@am[email protected]    then mv -f &quot;$(DEPDIR)/libdissectors_la-packet-echo.Tpo&quot; &quot;$(DEPDIR)/libdissectors_la-packet-echo.Plo&quot;; else rm -f &quot;$(DEPDIR)/libdissectors_la-packet-echo.Tpo&quot;; exit 1; fi
@[email protected]@am[email protected]       source=&#39;packet-echo.c&#39; object=&#39;libdissectors_la-packet-echo.lo&#39; libtool=yes @[email protected]
@[email protected]@am[email protected]       DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) @[email protected]
@[email protected]   $(LIBTOOL) --tag=CC --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(libdissectors_la_CFLAGS) $(CFLAGS) -c -o libdissectors_la-packet-echo.lo test -f &#39;packet-echo.c&#39; || echo &#39;$(srcdir)/&#39;packet-echo.c</code></pre><p><br />
</p></li></ul></li><li>Adding dissector in <code>CmakeLists.txt</code> (<code>epan/</code>)<br />
<code>dissectors/packet-giop_echo.c</code><br />
</li><li><code>./configure</code><br />
</li><li><code>make</code><br />
</li><li><code>make install</code></li></ol></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '12, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/80fdcdd1446b1855ee2fda6e19cae371?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivana&#39;s gravatar image" /><p><span>ivana</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivana has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Feb '12, 07:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></br></p></div></div><div id="comments-container-8928" class="comments-container"></div><div id="comment-tools-8928" class="comment-tools"></div><div class="clear"></div><div id="comment-8928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

