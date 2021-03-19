+++
type = "question"
title = "Where is pcapng development happening and what is the roadmap?"
description = '''Could someone clarify the development process going on for pcapng? It looks interesting, and if the recent blog post on Wireshark.org is an indication, something we need to keep track of. But where is it happening? Libpcap seems to be incorporating more functionality for reading it, but does not see...'''
date = "2012-05-09T10:29:00Z"
lastmod = "2012-05-09T14:37:00Z"
weight = 10845
keywords = [ "development", "pcapng", "libpcap" ]
aliases = [ "/questions/10845" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Where is pcapng development happening and what is the roadmap?](/questions/10845/where-is-pcapng-development-happening-and-what-is-the-roadmap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10845-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could someone clarify the development process going on for pcapng? It looks interesting, and if the recent blog post on <a href="http://Wireshark.org">Wireshark.org</a> is an indication, something we need to keep track of.</p><p>But where is it happening? Libpcap seems to be incorporating more functionality for reading it, but does not seem to support writing it. Winpcap development seems to have stopped, which bothers me a lot.</p><p>I can come up with tons of questions, but for a start it would be nice to know if pcapng is <a href="http://tcpdump.org">tcpdump.org</a> project or a Riverbed project.</p></div><div id="question-tags" class="tags-container tags">development pcapng libpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '12, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/e591bdeaa9a96a12d360d64833fc3122?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ted&#39;s gravatar image" /><p>Ted<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ted has no accepted answers">0%</span></p></div></div><div id="comments-container-10845" class="comments-container"></div><div id="comment-tools-10845" class="comment-tools"></div><div class="clear"></div><div id="comment-10845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10853"></span>

<div id="answer-container-10853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10853-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>pcapng, the file format, is a project of whoever takes an interest in it.</p><p>Support for pcapng in Wireshark is a Wireshark project. Support for pcapng in libpcap is a <a href="http://tcpdump.org">tcpdump.org</a> project. WinPcap is a project mainly by some people who work at Riverbed - but, as almost all of it except for the Win32-specific part comes from libpcap, the pcapng support would mirror that in libpcap as it's picked up.</p><p>There really isn't a roadmap. It's a question of who gets time to work on the implementations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10853" class="comments-container"><span id="10860"></span><div id="comment-10860" class="comment"><div id="post-10860-score" class="comment-score"></div><div class="comment-text"><p>Well, I am not a programmer, at least not good enough right now to help. I am just someone who helps run a system of capture boxes running linux which my colleagues use to download captures to Wireshark on Windows boxes. Yes, I know we should be using Cascade; management is cheap.</p><p>I am concerned that Winpcap isn't being maintained, and libpcap and Wireshark seem to be diverging. If the pcapng-writing capability isn't in libpcap, is it being written into some other library? Pcapng sounds good, but it looks like it won't be portable.</p></div><div id="comment-10860-info" class="comment-info"><span class="comment-age">(09 May '12, 20:11)</span> Ted</div></div><span id="10871"></span><div id="comment-10871" class="comment"><div id="post-10871-score" class="comment-score"></div><div class="comment-text"><p>By the way, there is a new pcap-ng specific mailing list that you can subscribe to at <a href="https://www.winpcap.org/mailman/listinfo/pcap-ng-format">https://www.winpcap.org/mailman/listinfo/pcap-ng-format</a></p></div><div id="comment-10871-info" class="comment-info"><span class="comment-age">(10 May '12, 00:17)</span> Jasper ♦♦</div></div><span id="10910"></span><div id="comment-10910" class="comment"><div id="post-10910-score" class="comment-score"></div><div class="comment-text"><p>You'd have to ask about WinPcap on the WinPcap mailing list; it's a free software project, developed and maintained primarily by people who have day jobs at Riverbed, and they might or might not always have time to produce a new release.</p><p>I'm not sure how libpcap and Wireshark are "diverging". They have separate implementations of code to read pcap-ng files, but they also have separate implementations of code to read pcap files, and have had it for over 10 years, so that's not significant. Currently, libpcap's support for reading is limited and it has no support for writing, but...</p></div><div id="comment-10910-info" class="comment-info"><span class="comment-age">(10 May '12, 19:39)</span> Guy Harris ♦♦</div></div><span id="10911"></span><div id="comment-10911" class="comment"><div id="post-10911-score" class="comment-score"></div><div class="comment-text"><p>...that's a consequence of libpcap's current API being insufficient for full support for reading pcap-ng files and for supporting an application being able to choose whether to write pcap or pcap-ng files; it is not a permanent decision on the part of the libpcap developers (the main developer of libpcap's pcap-ng support doesn't do it as a full-time job - he's also a core Wireshark developer and spends some time answering questions on <a href="http://ask.wireshark.org">ask.wireshark.org</a> :-)).</p></div><div id="comment-10911-info" class="comment-info"><span class="comment-age">(10 May '12, 19:42)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-10853" class="comment-tools"></div><div class="clear"></div><div id="comment-10853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

