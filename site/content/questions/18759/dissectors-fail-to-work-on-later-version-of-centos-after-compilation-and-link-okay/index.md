+++
type = "question"
title = "dissectors fail to work on later version of centos after compilation and link okay"
description = '''for historical reasons we used version 1.0.8 wireshark ( I think it was the officially delivered one with a specific version of redhat we were using) I created a set of dissectors specific to ATC interfaces. (AFTN,FMTP etc) These were compiled under centos and windows and worked well with both under...'''
date = "2013-02-20T01:02:00Z"
lastmod = "2013-02-26T06:29:00Z"
weight = 18759
keywords = [ "dissector", "registering" ]
aliases = [ "/questions/18759" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dissectors fail to work on later version of centos after compilation and link okay](/questions/18759/dissectors-fail-to-work-on-later-version-of-centos-after-compilation-and-link-okay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18759-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>for historical reasons we used version 1.0.8 wireshark ( I think it was the officially delivered one with a specific version of redhat we were using) I created a set of dissectors specific to ATC interfaces. (AFTN,FMTP etc) These were compiled under centos and windows and worked well with both under wireshark 1.0.8.</p><p>We have now upgraded(!) to redhat 6.3 which comes with wireshark 1.2.15. I have now rebuilt under windows(win7 64bit) the dissectors with 1.2.15 src and they work well. However having rebuilt the dissectors under centos 6.3 (64bit) they compile and link fine but coredump when the capture files are read in under the same centos 6.3(under vmplayer). It is specific to a dissector which calls other registered dissectors and looking at the decode_as option it seems that some of the called dissectors do not appear to have registered correctly. I know I am way behind the curve but I was hoping someone might know if 1.2.15 had any quirks WRT called dissectors or the way they are registered.</p><p>okay rather than keep replying to myself i shall add comments to original.</p><p>The fix i mentioned below does not work on the delivered version of wireshark 1.2.15 as installed by yum. I even uninstalled both wireshark and the gnome addon to see if that had any effect. I have removed the offending .so file from /usr/local/lib/wireshark/plugins/1.2.15 and it runs up and loads the file in okay. Back to the original problem.</p></div><div id="question-tags" class="tags-container tags">dissector registering</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '13, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/d64d9a4ffe16338d4c65598b82424d6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spotthemaniac&#39;s gravatar image" /><p>spotthemaniac<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spotthemaniac has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Feb '13, 04:16</p></div></div><div id="comments-container-18759" class="comments-container"><span id="18760"></span><div id="comment-18760" class="comment"><div id="post-18760-score" class="comment-score"></div><div class="comment-text"><p>This looks bad I have found out why! The find_dissector() call was implemented in the proto_reg_handoff_&lt;plugin_name&gt; routine and it appears this does not work in this version on centos. maybe the order that the libraries are loaded? I have changed to find_dissector call to be in the actual dissector code and it now calls the other dissectors correctly. Is this now a correct implementation or a fudge? ! a fudge that does not work so it seems!</p></div><div id="comment-18760-info" class="comment-info"><span class="comment-age">(20 Feb '13, 01:56)</span> spotthemaniac</div></div><span id="18767"></span><div id="comment-18767" class="comment"><div id="post-18767-score" class="comment-score"></div><div class="comment-text"><p>Have you compared your makefiles with the ones of plugins in 1.2 and the register and register_handoff routines? also check that the genarted plugin.c looks ok.</p></div><div id="comment-18767-info" class="comment-info"><span class="comment-age">(20 Feb '13, 04:02)</span> Anders ♦</div></div><span id="18772"></span><div id="comment-18772" class="comment"><div id="post-18772-score" class="comment-score"></div><div class="comment-text"><p>thanks i will do that as soon as i can. I did do an autogen.sh, ./configure, make, after i had copied over the offending dissector directories but you may have a point. will copy over some makefiles from example in 1.2 and remake.</p></div><div id="comment-18772-info" class="comment-info"><span class="comment-age">(20 Feb '13, 08:02)</span> spotthemaniac</div></div></div><div id="comment-tools-18759" class="comment-tools"></div><div class="clear"></div><div id="comment-18759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18880"></span>

<div id="answer-container-18880" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18880-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>turns out that the guy that wrote the asterix dissectors had used the same name in the proto_reg_handoff routines which bizarrely did not affect the windows version but failed with the redhat/centos version. All now have unique names and there are no problems!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '13, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/d64d9a4ffe16338d4c65598b82424d6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spotthemaniac&#39;s gravatar image" /><p>spotthemaniac<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spotthemaniac has no accepted answers">0%</span></p></div></div><div id="comments-container-18880" class="comments-container"><span id="18881"></span><div id="comment-18881" class="comment"><div id="post-18881-score" class="comment-score"></div><div class="comment-text"><p>and yes i did use the new makefile templates which had very little changes to them thanks.</p></div><div id="comment-18881-info" class="comment-info"><span class="comment-age">(26 Feb '13, 06:30)</span> spotthemaniac</div></div></div><div id="comment-tools-18880" class="comment-tools"></div><div class="clear"></div><div id="comment-18880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

