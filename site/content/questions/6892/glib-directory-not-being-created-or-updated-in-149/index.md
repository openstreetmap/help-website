+++
type = "question"
title = "glib directory not being created or updated in 1.4.9"
description = '''I am trying to update a custom plugin from Ethereal 0.10.14 to Wireshark 1.4.9. I am following the README.plugins file to do the update. This is for a Win32 application, and I am using MSVC2008 as recommended. I get the following error when compiling my plugin source: c:&#92;wireshark&#92;wireshark-1.4.9&#92;pl...'''
date = "2011-10-14T08:52:00Z"
lastmod = "2011-10-15T02:35:00Z"
weight = 6892
keywords = [ "development", "windows" ]
aliases = [ "/questions/6892" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [glib directory not being created or updated in 1.4.9](/questions/6892/glib-directory-not-being-created-or-updated-in-149)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6892-score" class="post-score" title="current number of votes">0</div><span id="post-6892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to update a custom plugin from Ethereal 0.10.14 to Wireshark 1.4.9. I am following the README.plugins file to do the update. This is for a Win32 application, and I am using MSVC2008 as recommended.</p><p>I get the following error when compiling my plugin source:</p><pre><code>c:\wireshark\wireshark-1.4.9\plugins\fatv\Rccu.h(12) : fatal error C1083: Cannot open include file: &#39;glib.h&#39;: No such file or directory</code></pre><p>I had used the following command sequences:</p><pre><code>nmake -f Makefile.nmake clean_setup
    # (Here I see that the glib directory is deleted)
nmake -f Makefile.nmake 
    # (I cannot find a glib directory getting created after this nor can I find anything in the make files to create this directory)
nmake -f Makefile.nmake 
    # (The above error occurs during this make)</code></pre><p>Is glib obselete? If not, why is it not found or created? How do I resolve this issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '11, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/15553454dfe2d95883f27714ebc070a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lanb&#39;s gravatar image" /><p><span>lanb</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lanb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Oct '11, 13:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6892" class="comments-container"></div><div id="comment-tools-6892" class="comment-tools"></div><div class="clear"></div><div id="comment-6892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6902"></span>

<div id="answer-container-6902" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6902-score" class="post-score" title="current number of votes">1</div><span id="post-6902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check your Makefile.nmake for your plugin.</p><pre><code>CFLAGS=/WX /DHAVE_CONFIG_H /I../.. $(GLIB_CFLAGS) 
    /I$(PCAP_DIR)include -D_U_=&quot;&quot; $(LOCAL_CFLAGS)</code></pre>Sets up the search path for the glib include file, through <code>GLIB_FLAGS</code> imported from <code>config.nmake</code></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '11, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6902" class="comments-container"></div><div id="comment-tools-6902" class="comment-tools"></div><div class="clear"></div><div id="comment-6902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6895"></span>

<div id="answer-container-6895" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6895-score" class="post-score" title="current number of votes">0</div><span id="post-6895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Does a "nmake -f Makefile.nmake setup" do the trick? ("clean_setup" deletes the old setup, but you need to explicitly recreate the setup stuff.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '11, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-6895" class="comments-container"><span id="6899"></span><div id="comment-6899" class="comment"><div id="post-6899-score" class="comment-score"></div><div class="comment-text"><p>It did not format well and I see I forgot the setup on the post, but I did the following:</p><p>nmake -f Makefile.nmake clean_setup</p><p>nmake -f Makefile.nmake setup</p><p>nmake -f Makefile.nmake all</p><p>So yes I did to an nmake ... setup after the clean_setup but do not see the glib directory being created in the libs directory.</p></div><div id="comment-6899-info" class="comment-info"><span class="comment-age">(14 Oct '11, 12:52)</span> <span class="comment-user userinfo">lanb</span></div></div><span id="6900"></span><div id="comment-6900" class="comment"><div id="post-6900-score" class="comment-score"></div><div class="comment-text"><p>For current Wireshark gtk/glib Win2 libraries, glib.h is in the following directory</p><p><code>[...]\win32-libs\gtk2\include\glib-2.0</code></p><p>There will not be a glib directory directly in the libs directory. (ISTR that the whole gtk2/glib directory structure changed at some point).</p><p>When you do the 'nmake all' do the Wireshark source files compile OK ? If yes then the library setup is not the problem.</p><p>Perhaps we might be able to help if you post the make output of the compile command for your plugin</p><p>E.G., <code>cl /D_NEED_VAR_IMPORT_ -WX -DHAVE_CONFIG_H -D_U_="" /Zi /W3 /MD ....</code></p></div><div id="comment-6900-info" class="comment-info"><span class="comment-age">(14 Oct '11, 16:50)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-6895" class="comment-tools"></div><div class="clear"></div><div id="comment-6895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

