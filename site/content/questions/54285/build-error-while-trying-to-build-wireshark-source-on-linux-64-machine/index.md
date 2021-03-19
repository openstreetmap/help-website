+++
type = "question"
title = "Build error while trying to build wireshark source on linux 64 machine"
description = '''Hello, I&#x27;m new to linux and wireshark development and awfully clueless here. My task is to build wireshark source wireshark-1.8.7. I&#x27;m getting the below error when I try configure make uninstall also gives the same error. ./configure: line 24671: syntax error near unexpected token `3.0.0,&#x27; ./configu...'''
date = "2016-07-25T04:48:00Z"
lastmod = "2016-07-26T05:04:00Z"
weight = 54285
keywords = [ "build_error", "linux" ]
aliases = [ "/questions/54285" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Build error while trying to build wireshark source on linux 64 machine](/questions/54285/build-error-while-trying-to-build-wireshark-source-on-linux-64-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54285-score" class="post-score" title="current number of votes">0</div><span id="post-54285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm new to linux and wireshark development and awfully clueless here. My task is to build wireshark source wireshark-1.8.7. I'm getting the below error when I try configure make uninstall also gives the same error.</p><pre><code>./configure: line 24671: syntax error near unexpected token `3.0.0,&#39;
./configure: line 24671: `                      AM_PATH_GTK_3_0(3.0.0,&#39;</code></pre><p>config.log has below error but I'm not sure if this has related</p><pre><code>configure:23853: gcc -c -g -O2 -Wall -W -Wextra -Wdeclaration-after-statement -Wendif-labels -Wpointer-arith -Wno-pointer-sign -Warray-bounds -Wcast-align -Wformat-security -Wold-style-definition -Wno-error=unused-but-set-variable -fexcess-precision=fast  conftest.c &gt;&amp;5
cc1: error: unrecognized command line option &quot;-fexcess-precision=fast&quot;</code></pre><p>linux machine info: 2.6.32-358.el6.x86_64</p><pre><code>[[email protected] Wireshark]# lsb_release -a
LSB Version:    :base-4.0-amd64:base-4.0-noarch:core-4.0-amd64:core-4.0-noarch:graphics-4.0-amd64:graphics-4.0-noarch:printing-4.0-amd64:printing-4.0-noarch
Distributor ID: RedHatEnterpriseServer
Description:    Red Hat Enterprise Linux Server release 6.4 (Santiago)
Release:        6.4
Codename:       Santiago</code></pre><p>Request for pointers what I might be missing.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '16, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/8f33b41ef74fe88317bf5384fc63d4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="satishp&#39;s gravatar image" /><p><span>satishp</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="satishp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jul '16, 04:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54285" class="comments-container"></div><div id="comment-tools-54285" class="comment-tools"></div><div class="clear"></div><div id="comment-54285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54313"></span>

<div id="answer-container-54313" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54313-score" class="post-score" title="current number of votes">1</div><span id="post-54313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="satishp has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That error suggests that <code>AM_PATH_GTK_3_0</code> wasn't replaced with the contents of that function. That's odd. Where did you get the source from. The 1.8.7 source tarball from wireshark.org don't have that problem.</p><p>I'd suggest running ./autogen.sh to re-generate <code>./configure</code>.</p><p>If that doesn't fix it then you're probably working from a modified version of Wireshark. If that's the case then you're going to have to try to figure out which of the changes that have been applied locally are causing the breakage.</p><p>Of course I'd <em>really</em> suggest using a (much) more recent version. But I'm guessing from your question that there's a particular reason you have to use exactly that version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '16, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-54313" class="comments-container"><span id="54331"></span><div id="comment-54331" class="comment"><div id="post-54331-score" class="comment-score"></div><div class="comment-text"><p>Hello JeffMorriss,</p><p>Thanks a lot for your response. executing ./autogen.sh to re-generate ./configure fixed the issue.</p></div><div id="comment-54331-info" class="comment-info"><span class="comment-age">(26 Jul '16, 02:55)</span> <span class="comment-user userinfo">satishp</span></div></div><span id="54335"></span><div id="comment-54335" class="comment"><div id="post-54335-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. Since this is a Q&amp;A site (not a forum) please be sure to "accept" the answer that answers your question (by clicking the checkmark next to the answer). That way the question won't show up in the list of unanswered questions (among other things--see the FAQ).</p></div><div id="comment-54335-info" class="comment-info"><span class="comment-age">(26 Jul '16, 05:04)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-54313" class="comment-tools"></div><div class="clear"></div><div id="comment-54313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

