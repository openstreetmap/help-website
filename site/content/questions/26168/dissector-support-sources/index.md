+++
type = "question"
title = "dissector support sources"
description = '''Hi all. I&#x27;ve finished my dissector plugin. Now I want to &quot;beautify&quot; it. Currently my plugin uses some helper files e.g. &quot;verifier.h&quot;. These helper files don&#x27;t point to a .c file at the moment, though. Both declerations and definitions are located in the .h files. That&#x27;s because I couldn&#x27;t manage to ...'''
date = "2013-10-18T07:58:00Z"
lastmod = "2013-10-18T07:58:00Z"
weight = 26168
keywords = [ "source", "support", "dissector" ]
aliases = [ "/questions/26168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dissector support sources](/questions/26168/dissector-support-sources)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all. I've finished my dissector plugin. Now I want to "beautify" it. Currently my plugin uses some helper files e.g. "verifier.h". These helper files don't point to a .c file at the moment, though. Both declerations and definitions are located in the .h files. That's because I couldn't manage to seperate declerations and definitions when developing my plugin. When I add the include/verifier.c to the DISSECTOR_SUPPORT_SRC variable in my plugin's Makefile, I get an error when starting wireshark: "Couldn't load module /usr/lib/wireshark/libwireshark1/plugins/myplugin.so: /usr/lib/wireshark/libwireshark1/plugins/myplugin.so: undefined symbol: find_certificate". This function is defined in verifier.c, so obviously my verifier.c is ignored by make command... So my question is: How can I seperate my includes into .h and .c files? The developer readme doesn't provide me this kind of information and now I don't have any idea how to solve my problem. I'm developing on Ubuntu Linux.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">source support dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/4d0f1f7eeb5c80f659413b34da3dd344?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arthur%20Giss&#39;s gravatar image" /><p>Arthur Giss<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arthur Giss has no accepted answers">0%</span></p></div></div><div id="comments-container-26168" class="comments-container"></div><div id="comment-tools-26168" class="comment-tools"></div><div class="clear"></div><div id="comment-26168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

