+++
type = "question"
title = "capture Q-in-Q VLAN IDs with tshark -T fields"
description = '''Hi all, Is there a way to display both the values of the inner and the outer VLAN IDs of a Q-in-Q packet using tshark -T fields? Wireshark display filters allow defining conditions on both values simultaneously: for instance &quot;vlan.id == 1 and vlan.id == 2&quot; matches Q-in-Q packets that have their oute...'''
date = "2015-07-28T08:10:00Z"
lastmod = "2015-07-28T10:29:00Z"
weight = 44566
keywords = [ "vlan", "tshark", "qinq" ]
aliases = [ "/questions/44566" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture Q-in-Q VLAN IDs with tshark -T fields](/questions/44566/capture-q-in-q-vlan-ids-with-tshark-t-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Is there a way to display both the values of the inner and the outer VLAN IDs of a Q-in-Q packet using <code>tshark -T fields</code>? Wireshark display filters allow defining conditions on both values simultaneously: for instance <code>"vlan.id == 1 and vlan.id == 2"</code> matches Q-in-Q packets that have their outer and inner VLAN IDs set to 1 and 2, respectively. However, the output of <code>tshark -i eth1 -Tfields -e vlan.id -e vlan.id</code> has its first column empty while the second column contains the value of the outer VLAN IDs.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">vlan tshark qinq</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '15, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/9a3172f727c17cc29eda4e1913e5ba87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvan&#39;s gravatar image" /><p>yvan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvan has no accepted answers">0%</span></p></div></div><div id="comments-container-44566" class="comments-container"><span id="44571"></span><div id="comment-44571" class="comment"><div id="post-44571-score" class="comment-score"></div><div class="comment-text"><p>have you looked here <a href="https://ask.wireshark.org/questions/15842/window7-automatically-remove-the-outer-vlan-tag">https://ask.wireshark.org/questions/15842/window7-automatically-remove-the-outer-vlan-tag</a> or here <a href="https://ask.wireshark.org/questions/41667/qinq-vlan-capture-filter">https://ask.wireshark.org/questions/41667/qinq-vlan-capture-filter</a> ?</p></div><div id="comment-44571-info" class="comment-info"><span class="comment-age">(28 Jul '15, 10:25)</span> Christian_R</div></div></div><div id="comment-tools-44566" class="comment-tools"></div><div class="clear"></div><div id="comment-44566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44572"></span>

<div id="answer-container-44572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44572-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the tshark usage output (1.12.6):</p><pre><code>-E&lt;fieldsoption&gt;=&lt;value&gt; set options for output when -Tfields selected:
     header=y|n            switch headers on and off
     separator=/t|/s|&lt;char&gt; select tab, space, printable character as separator
     occurrence=f|l|a      print first, last or all occurrences of each field
     aggregator=,|/s|&lt;char&gt; select comma, space, printable character as
                           aggregator</code></pre><p>Using the <code>occurence=a</code> option you'll get all vlan tags, not sure how they come out though, all in the first column, or over multiple columns.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '15, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44572" class="comments-container"><span id="44589"></span><div id="comment-44589" class="comment"><div id="post-44589-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-44589-info" class="comment-info"><span class="comment-age">(29 Jul '15, 04:58)</span> grahamb ♦</div></div></div><div id="comment-tools-44572" class="comment-tools"></div><div class="clear"></div><div id="comment-44572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

