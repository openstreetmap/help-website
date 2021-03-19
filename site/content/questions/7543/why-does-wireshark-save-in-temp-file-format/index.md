+++
type = "question"
title = "Why does Wireshark save in temp file format?"
description = '''I use Wireshark to take rolling captures on my machine overnight. I set it (in Capture Options) to take 200MB captures and stop after 30 captures. Everything works fine, but in the morning when I check the captures they are all stored in a temp format. I have to doubleclick on each one, load it up i...'''
date = "2011-11-21T13:10:00Z"
lastmod = "2011-11-21T14:12:00Z"
weight = 7543
keywords = [ "save", "pcap", "temp" ]
aliases = [ "/questions/7543" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why does Wireshark save in temp file format?](/questions/7543/why-does-wireshark-save-in-temp-file-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7543-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use Wireshark to take rolling captures on my machine overnight. I set it (in Capture Options) to take 200MB captures and stop after 30 captures. Everything works fine, but in the morning when I check the captures they are all stored in a temp format. I have to doubleclick on each one, load it up in Wireshark, and then save it back to the same folder in pcap format. It's a huge pain in the butt to open every file and save it. Is there any way to make Wireshark auto-save in pcap format?</p><p>TIA</p></div><div id="question-tags" class="tags-container tags">save pcap temp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '11, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/8737006597ff2c68f1cf7e4fb97e9f83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NarfBang&#39;s gravatar image" /><p>NarfBang<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NarfBang has no accepted answers">0%</span></p></div></div><div id="comments-container-7543" class="comments-container"></div><div id="comment-tools-7543" class="comment-tools"></div><div class="clear"></div><div id="comment-7543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7545"></span>

<div id="answer-container-7545" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7545-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, did you enter the capture file name in the capture options dialog <em>including</em> the <strong>.pcap</strong> extension?</p><p>I bet they're not actually in "temp" format, but just pcap files without a proper extension. You could try renaming them to include the .pcap extension, or (next time) just set the filename right with the .pcap extension in the capture options dialog. Wireshark will then automatically insert the running number and date/time, pushing the extension to the end.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '11, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7545" class="comments-container"><span id="7547"></span><div id="comment-7547" class="comment"><div id="post-7547-score" class="comment-score">1</div><div class="comment-text"><p>They are <em>certainly</em> not in "temp file format"; the formats in which Wireshark can save packets when capturing are pcap and pcap-NG formats, with pcap being the default format in all current versions (versions from the SVN trunk, such as the development builds, default to pcap-NG).</p><p>They don't have ".pcap" as a suffix of the file name, but the expectation is that they will be opened <em>only</em> by the version of Wireshark that wrote them and then saved or discarded. When saving to multiple files, give an explicit file name with .pcap as Jasper suggests, so you can open them by double-clicking.</p></div><div id="comment-7547-info" class="comment-info"><span class="comment-age">(21 Nov '11, 17:35)</span> Guy Harris ♦♦</div></div><span id="7556"></span><div id="comment-7556" class="comment"><div id="post-7556-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guys!!!! That helps a ton.</p></div><div id="comment-7556-info" class="comment-info"><span class="comment-age">(22 Nov '11, 07:04)</span> NarfBang</div></div></div><div id="comment-tools-7545" class="comment-tools"></div><div class="clear"></div><div id="comment-7545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

