+++
type = "question"
title = "What are the units of time used in Wireshark"
description = '''Qual é a unidade de tempo usada em wireshark? como é calculado, em ms,s...? obrigado. (Or, for those who can&#x27;t read Portuguese, a translation from Google Translate: What is the unit of time used in wireshark? how is it calculated in ms, s...? Thank you.)'''
date = "2011-04-29T13:15:00Z"
lastmod = "2011-04-29T18:07:00Z"
weight = 3821
keywords = [ "time" ]
aliases = [ "/questions/3821" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What are the units of time used in Wireshark](/questions/3821/what-are-the-units-of-time-used-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3821-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Qual é a unidade de tempo usada em wireshark? como é calculado, em ms,s...? obrigado.</p><p>(Or, for those who can't read Portuguese, a translation from Google Translate:</p><p>What is the unit of time used in wireshark? how is it calculated in ms, s...? Thank you.)</p></div><div id="question-tags" class="tags-container tags">time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '11, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/50cc5c1ffd91dcbcb5e9960b1d4745b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guilherme&#39;s gravatar image" /><p>Guilherme<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guilherme has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Apr '11, 18:05</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-3821" class="comments-container"></div><div id="comment-tools-3821" class="comment-tools"></div><div class="clear"></div><div id="comment-3821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3829"></span>

<div id="answer-container-3829" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3829-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Internally, Wireshark's units of time are nanoseconds. <em>However</em>, not all packet time stamps have nanosecond resolution; the time stamps in pcap files, for example, have microsecond resolution, and there's no guarantee that the time stamps are accurate to the microsecond.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '11, 18:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3829" class="comments-container"><span id="3848"></span><div id="comment-3848" class="comment"><div id="post-3848-score" class="comment-score"></div><div class="comment-text"><p>And how do you know the resolution?</p></div><div id="comment-3848-info" class="comment-info"><span class="comment-age">(30 Apr '11, 12:53)</span> Guilherme</div></div><span id="3850"></span><div id="comment-3850" class="comment"><div id="post-3850-score" class="comment-score"></div><div class="comment-text"><p>You have to know the capture file format. Wireshark should provide that in the summary information, but doesn't.</p></div><div id="comment-3850-info" class="comment-info"><span class="comment-age">(30 Apr '11, 13:00)</span> Guy Harris ♦♦</div></div><span id="3851"></span><div id="comment-3851" class="comment"><div id="post-3851-score" class="comment-score"></div><div class="comment-text"><p>Bem, não entendi muito. Os formatos são de arquivos html, mht, htm ... obrigado.</p><p>(In English: Well, I did not understand. The file formats are html, mht, htm ... Thank you.)</p></div><div id="comment-3851-info" class="comment-info"><span class="comment-age">(30 Apr '11, 13:10)</span> Guilherme</div></div><span id="3852"></span><div id="comment-3852" class="comment"><div id="post-3852-score" class="comment-score"></div><div class="comment-text"><p>By "capture file format" I mean the format of the file you opened with Wireshark, not the format of the data transferred over the network in the capture. If you captured the traffic with Wireshark, the file format would be pcap format; that's also the format used by tcpdump and TShark.</p></div><div id="comment-3852-info" class="comment-info"><span class="comment-age">(30 Apr '11, 13:18)</span> Guy Harris ♦♦</div></div><span id="3853"></span><div id="comment-3853" class="comment"><div id="post-3853-score" class="comment-score"></div><div class="comment-text"><p>Entendi. Então pelo formato pcap o tempo está em nanossegundo? Eu não tenho experiência nisso, estou aprendendo para um projeto de redes do curso técnico. obrigado.</p><p>(In English: Understood. So the time in pcap format is in nanoseconds? I have no experience with it, I'm learning to design a network of technical courses. Thank you.)</p></div><div id="comment-3853-info" class="comment-info"><span class="comment-age">(30 Apr '11, 14:41)</span> Guilherme</div></div><span id="3854"></span><div id="comment-3854" class="comment not_top_scorer"><div id="post-3854-score" class="comment-score"></div><div class="comment-text"><p>No, the time format in pcap files is in units of microseconds, except in captures from the tcpdump that is part of AIX. There is a modified pcap format that supports nanoseconds, but I don't know what uses it. (AIX doesn't use it, so Wireshark has to do some hacks to figure out whether the file is from AIX or not.)</p></div><div id="comment-3854-info" class="comment-info"><span class="comment-age">(30 Apr '11, 14:47)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-3829" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-3829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

