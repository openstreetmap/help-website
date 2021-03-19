+++
type = "question"
title = "Can wireshark open TRC. files?"
description = '''Does anyone know if wireshark can be used to open TRC. file? I am trying to open some OTDR files and someone told me that wireshark does this. Is this true? If so, how? Thank you'''
date = "2016-01-22T13:13:00Z"
lastmod = "2016-01-22T13:29:00Z"
weight = 49468
keywords = [ "trc" ]
aliases = [ "/questions/49468" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can wireshark open TRC. files?](/questions/49468/can-wireshark-open-trc-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49468-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone know if wireshark can be used to open TRC. file? I am trying to open some OTDR files and someone told me that wireshark does this. Is this true? If so, how? Thank you</p></div><div id="question-tags" class="tags-container tags">trc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '16, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/6e659c331dcb3933ae6e3955f67165d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smarminess&#39;s gravatar image" /><p>Smarminess<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smarminess has no accepted answers">0%</span></p></div></div><div id="comments-container-49468" class="comments-container"></div><div id="comment-tools-49468" class="comment-tools"></div><div class="clear"></div><div id="comment-49468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49469"></span>

<div id="answer-container-49469" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49469-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I have to guess what some of the initialisms mean - it's probably best to assume that not everybody is familiar with the terminology of your particular technology domain when you ask a question - but if OTDR means <a href="https://en.wikipedia.org/wiki/Optical_time-domain_reflectometer">Optical Time-Domain Reflectometer</a>, then, no, Wireshark doesn't read log files of any sort from OTDRs.</p><p>Perhaps those log files have come to be known as "trc. files", perhaps because the file names often begin or end with "trc.", but, in general, it's not always a good idea to refer to file types by commonly-used prefixes or suffixes - for one thing, again, somebody not familiar with a particular technology domain might not be familiar with them, and, for another thing, some suffixes are used by several <em>different</em> file formats, for example there are several different packet capture file formats for which the suffix ".cap" is used.</p><p>And perhaps the fact that Wireshark does handle some files for which the suffix ".trc" is used, such as classic DOS Sniffer Token Ring captures, gave somebody the incorrect impression that Wireshark could read some other unrelated type of file where the name also included "trc".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '16, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49469" class="comments-container"></div><div id="comment-tools-49469" class="comment-tools"></div><div class="clear"></div><div id="comment-49469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

