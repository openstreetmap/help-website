+++
type = "question"
title = "Wireshark capture file timestamp display"
description = '''Hi, When opening a capture file that contains timestamping done by third party via Wireshark, What will be the default behavior assuming packets written to the file out-of-order, display by order or be timestamp? Thanks'''
date = "2017-03-19T00:18:00Z"
lastmod = "2017-03-19T23:11:00Z"
weight = 60168
keywords = [ "timestamp" ]
aliases = [ "/questions/60168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture file timestamp display](/questions/60168/wireshark-capture-file-timestamp-display)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, When opening a capture file that contains timestamping done by third party via Wireshark, What will be the default behavior assuming packets written to the file out-of-order, display by order or be timestamp?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">timestamp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '17, 00:18</strong></p><img src="https://secure.gravatar.com/avatar/f0d049fff33eee7fbeff10d3c08275d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yakovd&#39;s gravatar image" /><p>yakovd<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yakovd has no accepted answers">0%</span></p></div></div><div id="comments-container-60168" class="comments-container"><span id="60185"></span><div id="comment-60185" class="comment"><div id="post-60185-score" class="comment-score"></div><div class="comment-text"><blockquote><p>When opening a capture file that contains timestamping done by third party via Wireshark</p></blockquote><p>So you mean that you have a capture file with time stamping done by a third party, and you open it in Wireshark?</p><p>If so, by "timestamping" do you mean the time stamps in the packet records or time stamps in the contents of the packets?</p></div><div id="comment-60185-info" class="comment-info"><span class="comment-age">(19 Mar '17, 22:03)</span> Guy Harris ♦♦</div></div><span id="60187"></span><div id="comment-60187" class="comment"><div id="post-60187-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I mean the time stamps in the packet records.</p></div><div id="comment-60187-info" class="comment-info"><span class="comment-age">(19 Mar '17, 22:45)</span> yakovd</div></div></div><div id="comment-tools-60168" class="comment-tools"></div><div class="clear"></div><div id="comment-60168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60189"></span>

<div id="answer-container-60189" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60189-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The default behavior is to display packets by the order in which they appear in the file. You can sort by the time stamp column, bu that's not the default.</p><p>The Wireshark package includes a command-line tool, <code>reordercap</code>, which will read a capture file and write the packets, sorted by their timestamps, to a new file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '17, 23:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-60189" class="comments-container"></div><div id="comment-tools-60189" class="comment-tools"></div><div class="clear"></div><div id="comment-60189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

