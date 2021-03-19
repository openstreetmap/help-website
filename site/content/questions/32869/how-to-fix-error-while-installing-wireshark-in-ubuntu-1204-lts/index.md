+++
type = "question"
title = "How to fix error while installing Wireshark in Ubuntu 12.04 LTS?"
description = '''As I try to install wireshark I get following error and unable to isntall OpenFlow extension? so unable to run OF filter in it.  8 files updated, 0 files merged, 0 files removed, 0 files unresolved  scons: Reading SConscript files ...  scons: done reading SConscript files.  scons: Building targets ....'''
date = "2014-05-18T08:22:00Z"
lastmod = "2014-05-18T13:10:00Z"
weight = 32869
keywords = [ "installation", "install", "wireshark" ]
aliases = [ "/questions/32869" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to fix error while installing Wireshark in Ubuntu 12.04 LTS?](/questions/32869/how-to-fix-error-while-installing-wireshark-in-ubuntu-1204-lts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32869-score" class="post-score" title="current number of votes">0</div><span id="post-32869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As I try to install wireshark I get following error and unable to isntall OpenFlow extension? so unable to run OF filter in it.</p><pre><code> 8 files updated, 0 files merged, 0 files removed, 0 files unresolved
    scons: Reading SConscript files ...
    scons: done reading SConscript files.
    scons: Building targets ...
    gcc -o packet-openflow.os -c -fPIC -I. -I/usr/include/wireshark -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include packet-openflow.c
    In file included from /usr/include/glib-2.0/glib/galloca.h:34:0,
                     from /usr/include/glib-2.0/glib.h:32,
                     from packet-openflow.c:15:
    /usr/include/glib-2.0/glib/gtypes.h:34:24: fatal error: glibconfig.h: No such file or directory
    compilation terminated.
    scons: *** [packet-openflow.os] Error 1
    scons: building terminated because of errors.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '14, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/f91693f0885c0afef57ec7acd595ae51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milstein&#39;s gravatar image" /><p><span>milstein</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milstein has no accepted answers">0%</span></p></div></div><div id="comments-container-32869" class="comments-container"></div><div id="comment-tools-32869" class="comment-tools"></div><div class="clear"></div><div id="comment-32869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32871"></span>

<div id="answer-container-32871" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32871-score" class="post-score" title="current number of votes">1</div><span id="post-32871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should probably ask here <a href="http://archive.openflow.org/wk/index.php/OpenFlow_Wireshark_Dissector">http://archive.openflow.org/wk/index.php/OpenFlow_Wireshark_Dissector</a> or build the trunk version of wireshark which have a built in openflow dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '14, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32871" class="comments-container"><span id="32872"></span><div id="comment-32872" class="comment"><div id="post-32872-score" class="comment-score"></div><div class="comment-text"><p>Thanks! <span>@Anders</span></p></div><div id="comment-32872-info" class="comment-info"><span class="comment-age">(18 May '14, 13:10)</span> <span class="comment-user userinfo">milstein</span></div></div></div><div id="comment-tools-32871" class="comment-tools"></div><div class="clear"></div><div id="comment-32871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

