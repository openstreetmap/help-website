+++
type = "question"
title = "Question re Capture files"
description = '''Hi, Hopefully not to dumb a question. But really want to get into Wireshark and therefore I am going through various capture files I have been able to find on Wireshark.org and via Google searches, and I find these very good as part of the learning process, BUT, I don&#x27;t seem to be able to find what ...'''
date = "2016-06-03T08:28:00Z"
lastmod = "2016-06-03T09:25:00Z"
weight = 53180
keywords = [ "ds95gas" ]
aliases = [ "/questions/53180" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Question re Capture files](/questions/53180/question-re-capture-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53180-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Hopefully not to dumb a question. But really want to get into Wireshark and therefore I am going through various capture files I have been able to find on Wireshark.org and via Google searches, and I find these very good as part of the learning process, BUT, I don't seem to be able to find what capture filter the originator has used on the file.</p><p>Looking in the properties doesn't really help, and a good deal of the time, the title used to save the file is not giving much away.</p><p>I just want to be able to load up the capture files, see the traffic and find out what filter was used to capture those particular traffic elements in the first place.</p><p>Could anyone advise please ..... Sorry if its a stupid question.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ds95gas</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '16, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/9c57c5eea9c6a4ad0f6eeabe99d5516d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d95gas&#39;s gravatar image" /><p>d95gas<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="d95gas has no accepted answers">0%</span></p></div></div><div id="comments-container-53180" class="comments-container"></div><div id="comment-tools-53180" class="comment-tools"></div><div class="clear"></div><div id="comment-53180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53182"></span>

<div id="answer-container-53182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53182-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The capture filter used (if any) during collection of frames in the capture files is a local matter, that is, it is not stored or recorded in the capture file itself.</p><p>Only the newly developed <a href="https://github.com/pcapng/pcapng">pcap-ng capture file format</a> allows storing of the applied capture filter, in the <a href="http://xml2rfc.tools.ietf.org/cgi-bin/xml2rfc.cgi?url=https://raw.githubusercontent.com/pcapng/pcapng/master/draft-tuexen-opsawg-pcapng.xml&amp;modeAsFormat=html/ascii&amp;type=ascii#section_idb">Interface Description Block</a>, so this type of capture files could contain this information. Currently it is not so usual to find them. I'm not even aware if Wireshark sets this.</p><p>Actually a good question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '16, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53182" class="comments-container"><span id="53183"></span><div id="comment-53183" class="comment"><div id="post-53183-score" class="comment-score"></div><div class="comment-text"><p>Many thanks Jaap ..... So glad it wasn't such a dumb question :-)</p><p>Just means learning is a little harder, but not the end of the world....... Just make me work harder for my money so to speak.</p><p>Thanks again</p></div><div id="comment-53183-info" class="comment-info"><span class="comment-age">(03 Jun '16, 09:35)</span> d95gas</div></div><span id="53185"></span><div id="comment-53185" class="comment"><div id="post-53185-score" class="comment-score"></div><div class="comment-text"><p>To help others spot usefully answered Questions, please Accept an Answer which you find useful by clicking the checkmark icon next to it. No one else can do it on your behalf - anyone else can vote but not Accept.</p><p>And your post has been converted to a comment, as it wasn't an Answer to your Question. See site FAQ for details.</p></div><div id="comment-53185-info" class="comment-info"><span class="comment-age">(03 Jun '16, 11:17)</span> sindy</div></div></div><div id="comment-tools-53182" class="comment-tools"></div><div class="clear"></div><div id="comment-53182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

