+++
type = "question"
title = "Can rpmbuild be used to create a tshark package?"
description = '''I&#x27;ve been using rpmbuild to create a wireshark rpm that includes a plugin I&#x27;ve made. This works fine but I want to create a tshark only package that can run on a server.  I used this configure command in the spec file: ./configure --host=x86_64-unknown-linux-gnu --build=x86_64-unknown-linux-gnu --pr...'''
date = "2011-04-12T11:58:00Z"
lastmod = "2011-04-13T10:05:00Z"
weight = 3466
keywords = [ "rpm", "tshark" ]
aliases = [ "/questions/3466" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can rpmbuild be used to create a tshark package?](/questions/3466/can-rpmbuild-be-used-to-create-a-tshark-package)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3466-score" class="post-score" title="current number of votes">0</div><span id="post-3466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been using rpmbuild to create a wireshark rpm that includes a plugin I've made. This works fine but I want to create a tshark only package that can run on a server.</p><p>I used this configure command in the spec file:</p><pre><code>./configure --host=x86_64-unknown-linux-gnu --build=x86_64-unknown-linux-gnu --program-prefix= --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/lib --localstatedir=/var --sharedstatedir=/usr/com --mandir=/usr/share/man --infodir=/usr/share/info --disable-wireshark --disable-editcap --disable-capinfos --disable-mergecap --disable-text2pcap --disable-idl2wrs --disable-dftest --disable-randpkt --disable-rawshark</code></pre><p>But I get the following error once rpmbuild gets to the install part:</p><pre><code>RPM build errors:
File not found: /usr/src/packages/BUILDROOT/wireshark-1.4.4-38.1.x86_64/usr/bin/wireshark
File not found: /usr/src/packages/BUILDROOT/wireshark-1.4.4-38.1.x86_64/usr/bin/editcap
File not found: /usr/src/packages/BUILDROOT/wireshark-1.4.4-38.1.x86_64/usr/bin/mergecap
File not found: /usr/src/packages/BUILDROOT/wireshark-1.4.4-38.1.x86_64/usr/bin/text2pcap
File not found: /usr/src/packages/BUILDROOT/wireshark-1.4.4-38.1.x86_64/usr/bin/dftest
File not found: /usr/src/packages/BUILDROOT/wireshark-1.4.4-38.1.x86_64/usr/bin/capinfos
File not found: /usr/src/packages/BUILDROOT/wireshark-1.4.4-38.1.x86_64/usr/bin/randpkt
File not found: /usr/src/packages/BUILDROOT/wireshark-1.4.4-38.1.x86_64/usr/bin/rawshark</code></pre><p>Does anyone know what I'm doing wrong? Obviously it's trying to package up all those binaries but I indicated inside the configure command not to compile those ones..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpm" rel="tag" title="see questions tagged &#39;rpm&#39;">rpm</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '11, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/e38821ea7ed026bbdf8032a0fdc64d6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tokolosh&#39;s gravatar image" /><p><span>Tokolosh</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tokolosh has no accepted answers">0%</span></p></div></div><div id="comments-container-3466" class="comments-container"></div><div id="comment-tools-3466" class="comment-tools"></div><div class="clear"></div><div id="comment-3466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3473"></span>

<div id="answer-container-3473" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3473-score" class="post-score" title="current number of votes">2</div><span id="post-3473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tokolosh has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Certainly it should be possible--I'd be willing to bet that Redhat's RPMs are built with rpmbuild. You might want to start with their spec file, if you're doing it that way though...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '11, 17:44</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-3473" class="comments-container"><span id="3488"></span><div id="comment-3488" class="comment"><div id="post-3488-score" class="comment-score"></div><div class="comment-text"><p>Good suggestion. So good that I went ahead already and got a tshark spec file form a src rpm on opensuse.org. Seems to have done the job fairly well. Thank you =]</p></div><div id="comment-3488-info" class="comment-info"><span class="comment-age">(13 Apr '11, 10:05)</span> <span class="comment-user userinfo">Tokolosh</span></div></div></div><div id="comment-tools-3473" class="comment-tools"></div><div class="clear"></div><div id="comment-3473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3470"></span>

<div id="answer-container-3470" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3470-score" class="post-score" title="current number of votes">0</div><span id="post-3470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You will need to edit the <code>packaging/rpm/SPECS/wireshark.spec.in</code> file. Specifically, you will need to modify the <code>CFLAGS</code> line to match your desired configuration. See also <a href="http://ask.wireshark.org/questions/3237/how-would-one-generate-an-rpm-for-wireshark">this</a> related question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '11, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3470" class="comments-container"><span id="3472"></span><div id="comment-3472" class="comment"><div id="post-3472-score" class="comment-score"></div><div class="comment-text"><p>Yeh lol that was me.</p><p>I wanted to avoid using make to generate the rpm because in the past that resulted in buggy package.</p></div><div id="comment-3472-info" class="comment-info"><span class="comment-age">(12 Apr '11, 13:35)</span> <span class="comment-user userinfo">Tokolosh</span></div></div></div><div id="comment-tools-3470" class="comment-tools"></div><div class="clear"></div><div id="comment-3470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

