+++
type = "question"
title = "Display filter with IN {set} not working."
description = '''I am trying to do a display filter as shown in section 6.4.4, https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html, but it isn&#x27;t working.  udp.dstport in {1900 2869 5000} Wireshark Version 1.99.8 (v1.99.8-0-ga0c561a from master)'''
date = "2015-10-17T11:09:00Z"
lastmod = "2015-10-18T11:01:00Z"
weight = 46644
keywords = [ "display-filter" ]
aliases = [ "/questions/46644" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display filter with IN {set} not working.](/questions/46644/display-filter-with-in-set-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46644-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to do a display filter as shown in section 6.4.4, <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html</a>, but it isn't working.<br />
</p><p>udp.dstport in {1900 2869 5000}</p><p>Wireshark Version 1.99.8 (v1.99.8-0-ga0c561a from master)</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '15, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/0bd23158db1b097d3de8e82572e70fdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sir%20Launcelot&#39;s gravatar image" /><p>Sir Launcelot<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sir Launcelot has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '15, 12:10</p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span></p></div></div><div id="comments-container-46644" class="comments-container"></div><div id="comment-tools-46644" class="comment-tools"></div><div class="clear"></div><div id="comment-46644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46674"></span>

<div id="answer-container-46674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46674-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>it works with 2.0.0RC1 on Windows 7. So, can you please try the latest development build?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/46644_screen01.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '15, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '15, 11:05</p></div></div><div id="comments-container-46674" class="comments-container"><span id="46678"></span><div id="comment-46678" class="comment"><div id="post-46678-score" class="comment-score"></div><div class="comment-text"><p>I guess the automatic upgrades don't work, nor does the check for updates button in the help menu. I had tried, or so I thought, to make sure I was up to date. I will recheck after rebooting for the install.</p></div><div id="comment-46678-info" class="comment-info"><span class="comment-age">(18 Oct '15, 16:50)</span> Sir Launcelot</div></div><span id="46688"></span><div id="comment-46688" class="comment"><div id="post-46688-score" class="comment-score"></div><div class="comment-text"><blockquote><p>so I thought, to make sure I was up to date</p></blockquote><p>Wireshark will tell you within the Help menu item in the GUI or via CLI</p><blockquote><p>wireshark -v</p></blockquote><p>You can find the latest development build here:</p><blockquote><p><a href="https://www.wireshark.org/download.html">https://www.wireshark.org/download.html</a></p></blockquote></div><div id="comment-46688-info" class="comment-info"><span class="comment-age">(19 Oct '15, 02:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46674" class="comment-tools"></div><div class="clear"></div><div id="comment-46674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

