+++
type = "question"
title = "How to search for a string with the format x.x-xxxxxxx?"
description = '''I am looking for a version string with the format of x.x-xxxxxxx in a pcap file I have. I am fairly new to wireshark and I would like some help figuring out how to search for this.'''
date = "2016-09-28T11:20:00Z"
lastmod = "2016-09-28T11:55:00Z"
weight = 55970
keywords = [ "filter", "nsa", "challenge" ]
aliases = [ "/questions/55970" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to search for a string with the format x.x-xxxxxxx?](/questions/55970/how-to-search-for-a-string-with-the-format-xx-xxxxxxx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55970-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for a version string with the format of x.x-xxxxxxx in a pcap file I have. I am fairly new to wireshark and I would like some help figuring out how to search for this.</p></div><div id="question-tags" class="tags-container tags">filter nsa challenge</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '16, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/23831c9a350e0c40b17ee94d09b3266e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patprime&#39;s gravatar image" /><p>patprime<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patprime has no accepted answers">0%</span></p></div></div><div id="comments-container-55970" class="comments-container"></div><div id="comment-tools-55970" class="comment-tools"></div><div class="clear"></div><div id="comment-55970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55971"></span>

<div id="answer-container-55971" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55971-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use <code>Edit -&gt; Find</code> (or just press <code>Ctrl-F</code>), a new toolbar will show up below the "display filter" one. At the right, choose <code>Packet bytes</code> and <code>Regular expression</code> from the respective drop-down lists, and fill the regular expression describing your version string as precisely as possible into the search term field. Then each press of the <code>Find</code> button next to it will take you to next packet matching the condition, or the status line below will flash yellow to indicate that no such packet could be found.</p><p>As you haven't been exact about the possible values of x, x and xxxxxxx, I cannot give you a matching regular expression. If you know the exact string, just write it to the field, except that you have to use <code>\.</code> instead of just <code>.</code> because in regexp syntax, the <code>.</code> alone means "any character". The <code>-</code> may remain as-is in this simple expression, although in more complex cases it sometimes needs a special treatment as well.</p><p><strong>EDIT:</strong><br />
Instead of the <code>Find</code> functionality, you can also use a display filter: <code>frame matches regexp</code> will display only frames whose contents interpreted as text matches the <code>regexp</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '16, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '16, 03:16</p></div></div><div id="comments-container-55971" class="comments-container"><span id="56972"></span><div id="comment-56972" class="comment"><div id="post-56972-score" class="comment-score"></div><div class="comment-text"><p>@sindy thanks for the answer! I did not specified the value because my goal is finding out every possible 11 char version string that looks x.x-xxxxxxx (thus x can be every number)</p></div><div id="comment-56972-info" class="comment-info"><span class="comment-age">(04 Nov '16, 02:57)</span> lcltornado</div></div><span id="56973"></span><div id="comment-56973" class="comment"><div id="post-56973-score" class="comment-score"></div><div class="comment-text"><p>well, "every possible 11 char" sounds as if any symbol (including letters and special symbols) would be valid as <code>x</code>, while "x can be every number" sounds like "x can be any <strong>digit</strong>". The point is that if you can restrict the regular expression to <strong>digits</strong> x, you'll have less false positives.</p></div><div id="comment-56973-info" class="comment-info"><span class="comment-age">(04 Nov '16, 03:02)</span> sindy</div></div></div><div id="comment-tools-55971" class="comment-tools"></div><div class="clear"></div><div id="comment-55971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

