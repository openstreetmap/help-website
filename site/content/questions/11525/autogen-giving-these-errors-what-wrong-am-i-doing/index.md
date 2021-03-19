+++
type = "question"
title = "./autogen giving these errors, what wrong am i doing ?"
description = '''[root@localhost wireshark-1.7.1]# ./autogen.sh ./autogen.sh: line 101: ./aclocal-flags: Permission denied configure.in:208: warning: macro `AM_PATH_LIBGCRYPT&#x27; not found in library configure.in:833: warning: macro `AM_PATH_GTK_3_0&#x27; not found in library configure.in:39: warning: AC_CACHE_VAL(lt_prog_c...'''
date = "2012-06-01T04:36:00Z"
lastmod = "2012-06-04T02:59:00Z"
weight = 11525
keywords = [ "installation", "wireshark1.7" ]
aliases = [ "/questions/11525" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [./autogen giving these errors, what wrong am i doing ?](/questions/11525/autogen-giving-these-errors-what-wrong-am-i-doing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11525-score" class="post-score" title="current number of votes">0</div><span id="post-11525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>[<span class="__cf_email__" data-cfemail="20524f4f54604c4f43414c484f5354">[email protected]</span> wireshark-1.7.1]# ./autogen.sh</p><p>./autogen.sh: line 101: ./aclocal-flags: Permission denied</p><p><a href="http://configure.in:208">configure.in:208</a>: warning: macro `AM_PATH_LIBGCRYPT' not found in library</p><p><a href="http://configure.in:833">configure.in:833</a>: warning: macro `AM_PATH_GTK_3_0' not found in library</p><p><a href="http://configure.in:39">configure.in:39</a>: warning: AC_CACHE_VAL(lt_prog_compiler_pic_works, ...): suspicious cache-id, must contain <em>cv</em> to be cached ../../lib/autoconf/general.m4:1974: AC_CACHE_VAL is expanded from... ../../lib/autoconf/general.m4:1994: AC_CACHE_CHECK is expanded from...</p><p>.</p><p>. . . .</p><p>aclocal.m4:4534: _LT_AC_LANG_GCJ_CONFIG is expanded from...</p><p>aclocal.m4:4533: AC_LIBTOOL_LANG_GCJ_CONFIG is expanded from...</p><p><a href="http://configure.in:39">configure.in:39</a>: warning: AC_CACHE_VAL(lt_prog_compiler_static_works_GCJ, ...): suspicious cache-id, must contain <em>cv</em> to be cached</p><p>automake: cannot open &lt; epan/dfilter/../../Makefile.am.inc: No such file or directory</p><p>[<span class="__cf_email__" data-cfemail="c3b1acacb783afaca0a2afabacb0b7">[email protected]</span> wireshark-1.7.1]#</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-wireshark1.7" rel="tag" title="see questions tagged &#39;wireshark1.7&#39;">wireshark1.7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '12, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p><span>yogeshg</span><br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11525" class="comments-container"><span id="11526"></span><div id="comment-11526" class="comment"><div id="post-11526-score" class="comment-score"></div><div class="comment-text"><p>Similarly configure script is also giving few errors , i suspect those to be caused by above autogen errors.Please help.</p></div><div id="comment-11526-info" class="comment-info"><span class="comment-age">(01 Jun '12, 04:37)</span> <span class="comment-user userinfo">yogeshg</span></div></div></div><div id="comment-tools-11525" class="comment-tools"></div><div class="clear"></div><div id="comment-11525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11527"></span>

<div id="answer-container-11527" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11527-score" class="post-score" title="current number of votes">1</div><span id="post-11527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yogeshg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>What is your system (<strong>lsb_release -a</strong>)?</li><li>Did you install all required tools/libs (Ubuntu: <strong>apt-get build-dep wireshark</strong>)</li><li>What is the output of <strong>ls -al aclocal-flags</strong> in the wireshark directory</li><li>Did you expand the sources on a NFS share? If so, local root might not have enough access rights! In that case, please try again from a local file system.</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '12, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '12, 04:53</strong> </span></p></div></div><div id="comments-container-11527" class="comments-container"><span id="11528"></span><div id="comment-11528" class="comment"><div id="post-11528-score" class="comment-score"></div><div class="comment-text"><p>[<span class="__cf_email__" data-cfemail="6614090912260a0905070a0e091512">[email protected]</span> ~]# lsb_release -a LSB Version: :core-3.1-ia32:core-3.1-noarch:graphics-3.1-ia32:graphics-3.1-noarch Distributor ID: Fedora Description: Fedora release 9 (Sulphur) Release: 9 Codename: Sulphur</p><p>[<span class="__cf_email__" data-cfemail="0a7865657e4a6665696b666265797e">[email protected]</span> wireshark-1.7.1]# ls -al aclocal-flags -rw-r--r-- 1 root root 4608 2012-04-07 00:12 aclocal-flags</p><p>I intend to write plugin for wireshark so i took development release source from <a href="http://wireshark.org">wireshark.org</a> itself and I didn't do any expansion</p></div><div id="comment-11528-info" class="comment-info"><span class="comment-age">(01 Jun '12, 04:54)</span> <span class="comment-user userinfo">yogeshg</span></div></div><span id="11529"></span><div id="comment-11529" class="comment"><div id="post-11529-score" class="comment-score"></div><div class="comment-text"><p>there are no exec rights for aclocal-flags and autogen.sh tries to execute that file (./aclocal-flags). Where did you get the source from and how did you expand it?</p><p>Can you please try this:</p><blockquote><p><code>svn checkout http://anonsvn.wireshark.org/wireshark/trunk wireshark</code><br />
</p></blockquote><p>and then run ./autogen.sh again.</p><p>If svn is not available on your system, install it:</p><blockquote><p><code>yum install subversion</code></p></blockquote><p>If you get different errors, your Fedora system (V9) might be to old to build the current version (GTK dev libs, etc.).</p></div><div id="comment-11529-info" class="comment-info"><span class="comment-age">(01 Jun '12, 04:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11606"></span><div id="comment-11606" class="comment"><div id="post-11606-score" class="comment-score"></div><div class="comment-text"><p>Thanks a ton Kurt for your valuable time. Actually source file was folder was not copied properly and now that i have copied it again its working!thanks again</p></div><div id="comment-11606-info" class="comment-info"><span class="comment-age">(04 Jun '12, 02:52)</span> <span class="comment-user userinfo">yogeshg</span></div></div><span id="11609"></span><div id="comment-11609" class="comment"><div id="post-11609-score" class="comment-score"></div><div class="comment-text"><p>good to hear.</p><p>If you like, you can mark my answer as the correct one (checkmark - see FAQ). It will help others to find anwers to their problems.</p></div><div id="comment-11609-info" class="comment-info"><span class="comment-age">(04 Jun '12, 02:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11527" class="comment-tools"></div><div class="clear"></div><div id="comment-11527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

