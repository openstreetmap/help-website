+++
type = "question"
title = "Other formats missing from the &quot;Save as&quot; dialog"
description = '''Wireshark 1.4 on Windows 7 is missing a several output file formats. According to the documentation there should be ten options but there are only seven - the various *.cap options. I am particularly interested in being able to save in the bfr (Network Observer) format. How can I get this back? Than...'''
date = "2010-12-23T22:44:00Z"
lastmod = "2010-12-24T02:24:00Z"
weight = 1475
keywords = [ "output", "bfr", "file", "format" ]
aliases = [ "/questions/1475" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Other formats missing from the "Save as" dialog](/questions/1475/other-formats-missing-from-the-save-as-dialog)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1475-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark 1.4 on Windows 7 is missing a several output file formats. According to the documentation there should be ten options but there are only seven - the various *.cap options. I am particularly interested in being able to save in the bfr (Network Observer) format. How can I get this back?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">output bfr file format</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '10, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/f2c9155855562507657b4f08185b4876?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GPT&#39;s gravatar image" /><p>GPT<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GPT has no accepted answers">0%</span></p></div></div><div id="comments-container-1475" class="comments-container"></div><div id="comment-tools-1475" class="comment-tools"></div><div class="clear"></div><div id="comment-1475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1476"></span>

<div id="answer-container-1476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1476-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How about this note in the User's Guide:</p><blockquote><p>The selection of capture formats may be reduced!</p><p>Some capture formats may not be available, depending on the packet types captured.</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '10, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1476" class="comments-container"><span id="1496"></span><div id="comment-1496" class="comment"><div id="post-1496-score" class="comment-score"></div><div class="comment-text"><p>That doesn't say a whole lot, does it? Any ideas on what packet types these are? I would like to try filtering them out to see if I still have the data in which I am interestesd.</p><p>Thanks</p></div><div id="comment-1496-info" class="comment-info"><span class="comment-age">(28 Dec '10, 03:18)</span> GPT</div></div><span id="1576"></span><div id="comment-1576" class="comment"><div id="post-1576-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, to give details, we'd have to say a <em>whole</em> lot - we support a number of capture file formats and link-layer types, and we'd probably have to give a table with one of those being the rows and another being the columns, or something such as that.</p><p>In the <em>particular</em> case of .bfr format, the only link-layer types we support are Ethernet and Token Ring. What link-layer type is the capture you're trying to save, and what file format is it? (If it's a capture you made with Wireshark, is it pcap or pcap-ng?)</p></div><div id="comment-1576-info" class="comment-info"><span class="comment-age">(01 Jan '11, 10:15)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-1476" class="comment-tools"></div><div class="clear"></div><div id="comment-1476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

