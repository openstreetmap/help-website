+++
type = "question"
title = "Wireshark 2 new interface no longer seeing packet bytes in separate window"
description = '''Topic says it...per this link: separate window in the new Wireshark I don&#x27;t see any packet bytes at all...is there a way to configure this?'''
date = "2015-11-23T11:28:00Z"
lastmod = "2015-11-23T11:58:00Z"
weight = 47881
keywords = [ "bytes", "packet" ]
aliases = [ "/questions/47881" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2 new interface no longer seeing packet bytes in separate window](/questions/47881/wireshark-2-new-interface-no-longer-seeing-packet-bytes-in-separate-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47881-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Topic says it...per this link: <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChapterWork.html#ChWorkPacketSepView">separate window</a> in the new Wireshark I don't see any packet bytes at all...is there a way to configure this?</p></div><div id="question-tags" class="tags-container tags">bytes packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '15, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/feeceb13b3a434a147fa2c173ad18db8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigiAngelXX&#39;s gravatar image" /><p>DigiAngelXX<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigiAngelXX has no accepted answers">0%</span></p></div></div><div id="comments-container-47881" class="comments-container"></div><div id="comment-tools-47881" class="comment-tools"></div><div class="clear"></div><div id="comment-47881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47885"></span>

<div id="answer-container-47885" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47885-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This was not implemented and the issue is tracked at <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11760">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11760</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Nov '15, 09:48</p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-47885" class="comments-container"><span id="47900"></span><div id="comment-47900" class="comment"><div id="post-47900-score" class="comment-score"></div><div class="comment-text"><p>Actually, it <em>was</em> implemented, but it's not working. See ui/qt/packet_dialog.cpp, which does <code>byte_view_tab_ = new ByteViewTab(ui-&gt;packetSplitter);</code>, to no avail as no byte view tab shows up in the window.</p></div><div id="comment-47900-info" class="comment-info"><span class="comment-age">(23 Nov '15, 14:51)</span> Guy Harris ♦♦</div></div><span id="47919"></span><div id="comment-47919" class="comment"><div id="post-47919-score" class="comment-score"></div><div class="comment-text"><p>Ah....I did just that thank you.</p></div><div id="comment-47919-info" class="comment-info"><span class="comment-age">(24 Nov '15, 03:58)</span> DigiAngelXX</div></div></div><div id="comment-tools-47885" class="comment-tools"></div><div class="clear"></div><div id="comment-47885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

