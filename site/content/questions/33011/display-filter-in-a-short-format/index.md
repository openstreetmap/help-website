+++
type = "question"
title = "Display filter in a short format"
description = '''I use often the display filters with same name but different values. For example, &quot;sip.from.addr contains &quot;12345&quot; || sip.from.addr contains &quot;54321&quot; || sip.from.addr ...&quot;. Can I use the form of filter like &quot;sip.from.addr contains &quot;12345&quot; or &quot;54321&quot;&quot;? '''
date = "2014-05-22T19:24:00Z"
lastmod = "2015-10-17T11:07:00Z"
weight = 33011
keywords = [ "filter", "short", "display", "format" ]
aliases = [ "/questions/33011" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Display filter in a short format](/questions/33011/display-filter-in-a-short-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33011-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use often the display filters with same name but different values. For example, "sip.from.addr contains "12345" || sip.from.addr contains "54321" || sip.from.addr ...". Can I use the form of filter like "sip.from.addr contains "12345" or "54321""?</p></div><div id="question-tags" class="tags-container tags">filter short display format</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '14, 19:24</strong></p><img src="https://secure.gravatar.com/avatar/d7ebdfa64a88154cd163c7cc781e4315?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="factorial&#39;s gravatar image" /><p>factorial<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="factorial has no accepted answers">0%</span></p></div></div><div id="comments-container-33011" class="comments-container"></div><div id="comment-tools-33011" class="comment-tools"></div><div class="clear"></div><div id="comment-33011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="33013"></span>

<div id="answer-container-33013" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33013-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, I don't think so. That's not how the display filter expression syntax works, so if you want to have something like this you'd need to patch it into the Wireshark code yourself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '14, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33013" class="comments-container"></div><div id="comment-tools-33013" class="comment-tools"></div><div class="clear"></div><div id="comment-33013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33043"></span>

<div id="answer-container-33043" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33043-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe a <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChDisplayFilterMacrosSection.html">Display Filter Macro</a> will help?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '14, 18:22</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-33043" class="comments-container"></div><div id="comment-tools-33043" class="comment-tools"></div><div class="clear"></div><div id="comment-33043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46643"></span>

<div id="answer-container-46643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46643-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check out how to use the IN for a set of matching items.</p><p><a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '15, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/0bd23158db1b097d3de8e82572e70fdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sir%20Launcelot&#39;s gravatar image" /><p>Sir Launcelot<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sir Launcelot has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '15, 12:09</p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span></p></div></div><div id="comments-container-46643" class="comments-container"></div><div id="comment-tools-46643" class="comment-tools"></div><div class="clear"></div><div id="comment-46643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

