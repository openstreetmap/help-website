+++
type = "question"
title = "Sharktools: Build Matshark...Please help!!!"
description = '''Hello All, In order to build Matshark, I followed the instructions on http://cpansearch.perl.org/src/NANIS/Net-Sharktools-0.009/README.sharktools-0.1.5.txt I am using a 32 bit, ubuntu 10.04 machine with gcc-4.3.4  I configured as follows: ./configure --disable-pyshark --with-mex=/[path/to/mex] --wit...'''
date = "2012-06-11T14:17:00Z"
lastmod = "2012-06-14T10:42:00Z"
weight = 11839
keywords = [ "gcc", "wireshark", "mex", "sharktools", "matshark" ]
aliases = [ "/questions/11839" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Sharktools: Build Matshark...Please help!!!](/questions/11839/sharktools-build-matsharkplease-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11839-score" class="post-score" title="current number of votes">0</div><span id="post-11839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>In order to build Matshark, I followed the instructions on <a href="http://cpansearch.perl.org/src/NANIS/Net-Sharktools-0.009/README.sharktools-0.1.5.txt">http://cpansearch.perl.org/src/NANIS/Net-Sharktools-0.009/README.sharktools-0.1.5.txt</a></p><p>I am using a 32 bit, ubuntu 10.04 machine with gcc-4.3.4</p><p>I configured as follows: ./configure --disable-pyshark --with-mex=/[path/to/mex] --with-wireshark-src=[/path/to/wireshark]</p><p>The process completes successfully and makefile is generated. When I issue the "make" command, I get:</p><p>sharktools_cfile.c: In function 'cap_file_init':</p><p>sharktools_cfile.c:47: error:'capture_file' has no member named 'plist_start'</p><p>sharktools_cfile.c:51: error:'capture_file' has no member named 'plist_end'</p><p>sharktools_cfile.c:57: error:'capture_file' has no member named 'user_saved'</p><p>make[1]:*** [all-recursive] Error 1</p><p>Can someone help with this?</p><p>Regards, Ramya</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gcc" rel="tag" title="see questions tagged &#39;gcc&#39;">gcc</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-mex" rel="tag" title="see questions tagged &#39;mex&#39;">mex</span> <span class="post-tag tag-link-sharktools" rel="tag" title="see questions tagged &#39;sharktools&#39;">sharktools</span> <span class="post-tag tag-link-matshark" rel="tag" title="see questions tagged &#39;matshark&#39;">matshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '12, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/43e3e902abae6fe307a1f695cdcd9af6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ramya&#39;s gravatar image" /><p><span>ramya</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ramya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '12, 16:27</strong> </span></p></div></div><div id="comments-container-11839" class="comments-container"></div><div id="comment-tools-11839" class="comment-tools"></div><div class="clear"></div><div id="comment-11839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11844"></span>

<div id="answer-container-11844" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11844-score" class="post-score" title="current number of votes">2</div><span id="post-11844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>user_saved</code></pre><p>The <code>sharktools_cfile.c</code> you have, wherever it comes from, probably expects an older version of the header files (and code!) for Wireshark, and you probably don't have it, given that the <code>capture_file</code> structure used to have a <code>user_saved</code> member but no longer does (it has a <code>unsaved_changes</code> member; the code for "Save" and "Save As" was changed for 1.8 to reflect the fact that Wireshark is now an "editor", in that you can read in a capture file with Wireshark, add comments to the file or to packets in the file/edit existing comments/delete existing comments, and then save the modified file).</p><p>There's probably a bug, or at least an invalid assumption, somewhere in Matshark, that's causing it not to work with whatever version of Wireshark you're using. You probably want to ask the Matshark people about this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '12, 20:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-11844" class="comments-container"><span id="11850"></span><div id="comment-11850" class="comment"><div id="post-11850-score" class="comment-score">1</div><div class="comment-text"><p>Indeed. From <a href="http://cpansearch.perl.org/src/NANIS/Net-Sharktools-0.009/README.sharktools-0.1.5.txt">README.sharktools-0.1.5.txt</a>:</p><pre><code>&quot;Be sure that you download the version of Wireshark that is roughly(\*) the same as the version of Wireshark installed by your package management system.  The source to Wireshark is needed because your distribution&#39;s wireshark-dev package is generally not sufficient(**) to build sharktools.&quot;</code></pre><p>In your case that would be something like: <code> Ubuntu 10.04.1 LTS + Python 2.6.5 + Wireshark 1.2.7</code></p></div><div id="comment-11850-info" class="comment-info"><span class="comment-age">(12 Jun '12, 05:36)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="11898"></span><div id="comment-11898" class="comment"><div id="post-11898-score" class="comment-score"></div><div class="comment-text"><p>Hello Guy, Thank you for your answer! So I went ahead and downgraded the wireshark version to 1.2.7. The errors above go away. But now when I try to make the file, I get another set of errors. All these errors are coming from sharktools_core.c :</p><hr /><pre><code>sharktools_core.c : undefined reference to epan_dissect_init
sharktools_core.c : undefined reference to frame_data_init
sharktools_core.c : undefined reference to frame_data_set_before_dissect
sharktools_core.c : undefined reference to frame_data_cleanup
sharktools_core.c : undefined reference to frame_data_set_after_dissect</code></pre><hr /><p>These functions are defined in Wireshark's epan.h and frame_data.h. I made sure that sharktools_core.c includes these headers from Wireshark's epan directory. Yet I get the erros above.</p><p>I have been struggling with this for the past week now. Any pointers on how to proceed further will be very helpful!</p><p>Best regards, Ramya</p></div><div id="comment-11898-info" class="comment-info"><span class="comment-age">(14 Jun '12, 07:28)</span> <span class="comment-user userinfo">ramya</span></div></div><span id="11899"></span><div id="comment-11899" class="comment"><div id="post-11899-score" class="comment-score"></div><div class="comment-text"><p>1.Hello Guy, Thank you for your answer! PLease see my answer below where I decribe a new set of errors I get once i downgrade teh wireshark version. Thank you, Ramya</p><p>Edit (<span>@grahamb</span>): I converted your "answer" to a comment as that is how this site works.</p></div><div id="comment-11899-info" class="comment-info"><span class="comment-age">(14 Jun '12, 07:44)</span> <span class="comment-user userinfo">ramya</span></div></div><span id="11903"></span><div id="comment-11903" class="comment"><div id="post-11903-score" class="comment-score"></div><div class="comment-text"><p>It appears that Sharktools does not support Wireshark 1.6.0 or later at all; <a href="http://www.wireshark.org/lists/wireshark-users/201011/msg00028.html">the announcement sent to the Wireshark mailing lists</a> only says it works with "Most - if not all - versions of Wireshark from 0.99.5 to 1.4.0".</p><p>There <em>does</em> appear to be an attempt in the configuration file to detect whether Wireshark is 1.0.x, 1.2.x, or 1.4.x, but that might not be working. Try doing <code>make distclean</code> and re-running the configure script in the Sharktools source directory.</p></div><div id="comment-11903-info" class="comment-info"><span class="comment-age">(14 Jun '12, 10:42)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-11844" class="comment-tools"></div><div class="clear"></div><div id="comment-11844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

