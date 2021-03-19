+++
type = "question"
title = "compile error with v. 1.10.5 on fedora 17"
description = '''I downloaded v. 1.10.5 and the build failed. I simply ran ./configure without any options. The error was:  CC wireshark-capture-pcap-util.o capture-pcap-util.c:569:1: error: static declaration of ‘pcap_datalink_name_to_val’ follows non-static declaration In file included from /usr/include/pcap.h:45:...'''
date = "2014-01-15T06:51:00Z"
lastmod = "2014-07-02T08:48:00Z"
weight = 28910
keywords = [ "build_error" ]
aliases = [ "/questions/28910" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [compile error with v. 1.10.5 on fedora 17](/questions/28910/compile-error-with-v-1105-on-fedora-17)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28910-score" class="post-score" title="current number of votes">0</div><span id="post-28910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded v. 1.10.5 and the build failed. I simply ran ./configure without any options. The error was:</p><pre><code>  CC     wireshark-capture-pcap-util.o
capture-pcap-util.c:569:1: error: static declaration of ‘pcap_datalink_name_to_val’ follows non-static declaration
In file included from /usr/include/pcap.h:45:0,
                 from capture-pcap-util.h:30,
                 from capture-pcap-util.c:48:
/usr/include/pcap/pcap.h:380:5: note: previous declaration of ‘pcap_datalink_name_to_val’ was here
capture-pcap-util.c:584:1: error: static declaration of ‘pcap_datalink_val_to_name’ follows non-static declaration
In file included from /usr/include/pcap.h:45:0,
                 from capture-pcap-util.h:30,
                 from capture-pcap-util.c:48:
/usr/include/pcap/pcap.h:381:13: note: previous declaration of ‘pcap_datalink_val_to_name’ was here</code></pre><p>Which definition should be removed or modified?</p><p>Thank you, Chuck Crisler</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '14, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/92841c0f34c63e535d2d6eb7a212c9e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChuckCrisler&#39;s gravatar image" /><p><span>ChuckCrisler</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChuckCrisler has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jan '14, 07:02</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-28910" class="comments-container"></div><div id="comment-tools-28910" class="comment-tools"></div><div class="clear"></div><div id="comment-28910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28938"></span>

<div id="answer-container-28938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28938-score" class="post-score" title="current number of votes">0</div><span id="post-28938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Which definition should be removed or modified?</p></blockquote><p>Neither.</p><p>Instead, you need to file a Wireshark bug at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach the <code>config.log</code> file in the build directory; apparently, the configure script thought your version of libpcap doesn't have <code>pcap_datalink_name_to_val()</code> or <code>pcap_datalink_val_to_name()</code>, but it does.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '14, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-28938" class="comments-container"><span id="28939"></span><div id="comment-28939" class="comment"><div id="post-28939-score" class="comment-score"></div><div class="comment-text"><p>OK, I will do that tomorrow. Thank you for the info. However, I do still need the build. How do I get it to work?</p><p>Thank you, Chuck</p></div><div id="comment-28939-info" class="comment-info"><span class="comment-age">(15 Jan '14, 17:00)</span> <span class="comment-user userinfo">ChuckCrisler</span></div></div><span id="28940"></span><div id="comment-28940" class="comment"><div id="post-28940-score" class="comment-score"></div><div class="comment-text"><p>Edit config.h and make sure it defines <code>HAVE_PCAP_DATALINK_NAME_TO_VAL</code>, <code>HAVE_PCAP_DATALINK_VAL_TO_NAME</code>, and <code>HAVE_PCAP_DATALINK_VAL_TO_DESCRIPTION</code>. This may, or may not, make the compile of that file succeed, and, if it does make the compile of that file succeed, there may be other problems, if the configure script made other errors.</p></div><div id="comment-28940-info" class="comment-info"><span class="comment-age">(15 Jan '14, 17:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="34353"></span><div id="comment-34353" class="comment"><div id="post-34353-score" class="comment-score"></div><div class="comment-text"><p>I have a similar issue with build 1.10.2, but it only happens when I use --enable-static in the configure.</p></div><div id="comment-34353-info" class="comment-info"><span class="comment-age">(02 Jul '14, 08:48)</span> <span class="comment-user userinfo">FlanOSU</span></div></div></div><div id="comment-tools-28938" class="comment-tools"></div><div class="clear"></div><div id="comment-28938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

