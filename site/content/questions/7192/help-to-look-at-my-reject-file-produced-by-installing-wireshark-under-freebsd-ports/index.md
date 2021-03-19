+++
type = "question"
title = "Help to look at my reject file produced by installing wireshark under FreeBSD ports!"
description = '''I tried to install the wireshark under my FreeBSD ports, it failed and get the reject file, I want to know what the reject file mean, Does anyone of you can tell me that? Thank you! [root@CandyFreeBSD /usr/ports/net/wireshark]# make install clean ===&amp;gt; Found saved configuration for wireshark-0.99....'''
date = "2011-11-02T00:39:00Z"
lastmod = "2011-11-03T18:25:00Z"
weight = 7192
keywords = [ "install", "freebsd", "wireshark" ]
aliases = [ "/questions/7192" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Help to look at my reject file produced by installing wireshark under FreeBSD ports!](/questions/7192/help-to-look-at-my-reject-file-produced-by-installing-wireshark-under-freebsd-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7192-score" class="post-score" title="current number of votes">0</div><span id="post-7192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to install the wireshark under my FreeBSD ports, it failed and get the reject file, I want to know what the reject file mean, Does anyone of you can tell me that? Thank you!</p><h1 id="email-protected-usrportsnetwireshark-make-install-clean">[<span class="__cf_email__" data-cfemail="275548485367644649435e61554242657463">[email protected]</span> /usr/ports/net/wireshark]# make install clean</h1><h1 id="found-saved-configuration-for-wireshark-0.99.7">===&gt; Found saved configuration for wireshark-0.99.7</h1><p>=&gt; MD5 Checksum OK for wireshark-0.99.7.tar.bz2. =&gt; SHA256 Checksum OK for wireshark-0.99.7.tar.bz2. ===&gt; wireshark-0.99.7 depends on file: /usr/local/bin/perl5.8.8 - found ===&gt; Patching for wireshark-0.99.7 ===&gt; wireshark-0.99.7 depends on file: /usr/local/bin/perl5.8.8 - found ===&gt; Applying FreeBSD patches for wireshark-0.99.7 1 out of 1 hunks failed--saving rejects to epan/dissectors/packet-diameter.c.rej =&gt; Patch patch-epan_dissectors_packet-diameter.c failed to apply cleanly. =&gt; Patch(es) patch-Makefile.in patch-configure patch-epan_Makefile.in applied cleanly. *** Error code 1</p><p>Stop in /usr/ports/net/wireshark. *** Error code 1</p><p>Stop in /usr/ports/net/wireshark. [<span class="__cf_email__" data-cfemail="05776a6a714546646b617c43776060475641">[email protected]</span> /usr/ports/net/wireshark]# cat work/wireshark-0.99.7/epan/dissectors/packet-diameter.c.rej <strong><em>2022,2034</em></strong> * { "Flags", "diameter.flags", FT_UINT8, BASE_HEX, NULL, 0x0, "", HFILL }}, { &amp;hf_diameter_flags_request, - { "Request", "diameter.flags.request", FT_BOOLEAN, 8, TFS(&amp;flags_set_truth), DIAM_FLAGS_R, "", HFILL }}, { &amp;hf_diameter_flags_proxyable, - { "Proxyable", "diameter.flags.proxyable", FT_BOOLEAN, 8, TFS(&amp;flags_set_truth), DIAM_FLAGS_P, "", HFILL }}, { &amp;hf_diameter_flags_error, - { "Error","diameter.flags.error", FT_BOOLEAN, 8, TFS(&amp;flags_set_truth), DIAM_FLAGS_E, "", HFILL }}, { &amp;hf_diameter_flags_T, { "T(Potentially re-transmitted message)","diameter.flags.T", FT_BOOLEAN, 8, TFS(&amp;flags_set_truth),DIAM_FLAGS_T, --- 2022,2034 ---- { "Flags", "diameter.flags", FT_UINT8, BASE_HEX, NULL, 0x0, "", HFILL }}, { &amp;hf_diameter_flags_request, + { "Request ", "diameter.flags.request", FT_BOOLEAN, 8, TFS(&amp;flags_set_truth), DIAM_FLAGS_R, "", HFILL }}, { &amp;hf_diameter_flags_proxyable, + { "Proxyable ", "diameter.flags.proxyable", FT_BOOLEAN, 8, TFS(&amp;flags_set_truth), DIAM_FLAGS_P, "", HFILL }}, { &amp;hf_diameter_flags_error, + { "Error ","diameter.flags.error", FT_BOOLEAN, 8, TFS(&amp;flags_set_truth), DIAM_FLAGS_E, "", HFILL }}, { &amp;hf_diameter_flags_T, { "T(Potentially re-transmitted message)","diameter.flags.T", FT_BOOLEAN, 8, TFS(&amp;flags_set_truth),DIAM_FLAGS_T, [<span class="__cf_email__" data-cfemail="87f5e8e8f3c7c4e6e9e3fec1f5e2e2c5d4c3">[email protected]</span> /usr/ports/net/wireshark]#</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-freebsd" rel="tag" title="see questions tagged &#39;freebsd&#39;">freebsd</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '11, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/f872fd3170b0c2a2ed18ca4e8ad88323?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="candyli&#39;s gravatar image" /><p><span>candyli</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="candyli has no accepted answers">0%</span></p></div></div><div id="comments-container-7192" class="comments-container"><span id="7214"></span><div id="comment-7214" class="comment"><div id="post-7214-score" class="comment-score"></div><div class="comment-text"><p>Version 0.99.7 is very old and no longer supported. I suggest trying to install a more modern version of Wireshark which you can find at the <a href="http://www.wireshark.org/download.html">download</a> page.</p></div><div id="comment-7214-info" class="comment-info"><span class="comment-age">(02 Nov '11, 18:07)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-7192" class="comment-tools"></div><div class="clear"></div><div id="comment-7192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7229"></span>

<div id="answer-container-7229" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7229-score" class="post-score" title="current number of votes">1</div><span id="post-7229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SYN-bit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is an issue of the FreeBSD port system, not Wireshark; the FreeBSD port maintainers maintain the ports.</p><p>As <a href="http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/ports-using.html">Using the Ports Collection</a> says, "Warning: Before installing any port, you should be sure to have an up-to-date Ports Collection and you should check <a href="http://vuxml.freebsd.org/">http://vuxml.freebsd.org/</a> for security issues related to your port." Make sure your Ports Collection is up to date - as Chris Maynard notes, Wireshark 0.99.7 is a very old release.</p><p>You might want to check out <a href="http://lists.FreeBSD.org/mailman/listinfo/freebsd-questions">the freebsd-questions mailing list</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '11, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7229" class="comments-container"></div><div id="comment-tools-7229" class="comment-tools"></div><div class="clear"></div><div id="comment-7229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

