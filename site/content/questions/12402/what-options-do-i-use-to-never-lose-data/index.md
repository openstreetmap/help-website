+++
type = "question"
title = "What options do I use to never lose data?"
description = '''What options do I use to never lose data? I do not want capture files to ever be overwritten or discarded. I do not want capturing to ever stop.'''
date = "2012-07-03T09:02:00Z"
lastmod = "2012-07-03T09:42:00Z"
weight = 12402
keywords = [ "great", "ghestsur" ]
aliases = [ "/questions/12402" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What options do I use to never lose data?](/questions/12402/what-options-do-i-use-to-never-lose-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12402-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What options do I use to never lose data?</p><p>I do not want capture files to ever be overwritten or discarded.</p><p>I do not want capturing to ever stop.</p></div><div id="question-tags" class="tags-container tags">great ghestsur</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '12, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/3d201a7d1c2936e720692022fd6bfe70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tompdiaz&#39;s gravatar image" /><p>tompdiaz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tompdiaz has no accepted answers">0%</span></p></div></div><div id="comments-container-12402" class="comments-container"></div><div id="comment-tools-12402" class="comment-tools"></div><div class="clear"></div><div id="comment-12402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12407"></span>

<div id="answer-container-12407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12407-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use dumpcap with a very large number of ring buffer files.</p><p>Windows:</p><blockquote><p><code>dumpcap.exe -i 1 -b filesize:100000</code> <del><code>files:100000</code></del> <code>-w output.cap</code><br />
</p></blockquote><p>Linux:<br />
</p><blockquote><p><code>dumpcap -i eth0 -b filesize:100000</code> <del><code>files:100000</code></del> <code>-w output.cap</code><br />
</p></blockquote><p>This will capture <del>100.000</del> files with 100 MByte each and thus it will virtually run "forever", or until your disk is full, whatever happens first. If that is not sufficient, just raise the values.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '12, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jul '12, 01:20</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></br></p></div></div><div id="comments-container-12407" class="comments-container"><span id="12409"></span><div id="comment-12409" class="comment"><div id="post-12409-score" class="comment-score">1</div><div class="comment-text"><p>Kurt, you can omit the "-b files:100000" option to make dumpcap <strong>not</strong> overwrite old files.</p><p>(Which will make the capture run "forever" if you bought the new "infinite" drive from <a href="http://www.nowthatswhaticallabigharddisk.com">www.nowthatswhaticallabigharddisk.com</a>)</p></div><div id="comment-12409-info" class="comment-info"><span class="comment-age">(03 Jul '12, 09:51)</span> SYN-bit ♦♦</div></div><span id="12411"></span><div id="comment-12411" class="comment"><div id="post-12411-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I never tried that!</p><p>BTW: Should that link actually work?</p></div><div id="comment-12411-info" class="comment-info"><span class="comment-age">(03 Jul '12, 09:57)</span> Kurt Knochner ♦</div></div><span id="12415"></span><div id="comment-12415" class="comment"><div id="post-12415-score" class="comment-score"></div><div class="comment-text"><p>Oops... I forgot to add the ";-)"</p></div><div id="comment-12415-info" class="comment-info"><span class="comment-age">(03 Jul '12, 10:43)</span> SYN-bit ♦♦</div></div><span id="12417"></span><div id="comment-12417" class="comment"><div id="post-12417-score" class="comment-score"></div><div class="comment-text"><p>damn, and I was already about to lauch <a href="http://amazon.com">amazon.com</a> ..... ;-)</p></div><div id="comment-12417-info" class="comment-info"><span class="comment-age">(03 Jul '12, 11:00)</span> Kurt Knochner ♦</div></div><span id="12433"></span><div id="comment-12433" class="comment"><div id="post-12433-score" class="comment-score"></div><div class="comment-text"><p>Also the 100MB might be a bit large for Wireshark to grok when you want to look into them.</p></div><div id="comment-12433-info" class="comment-info"><span class="comment-age">(04 Jul '12, 01:20)</span> Jaap ♦</div></div><span id="12434"></span><div id="comment-12434" class="comment not_top_scorer"><div id="post-12434-score" class="comment-score"></div><div class="comment-text"><p>really? Usually I split them in chunks of 250-400 MB with no (technical) problem at all. It's for sure a challenge to find THAT one packet, but that's a layer 8 problem.</p></div><div id="comment-12434-info" class="comment-info"><span class="comment-age">(04 Jul '12, 01:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12407" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-12407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

