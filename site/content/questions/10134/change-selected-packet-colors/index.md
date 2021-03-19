+++
type = "question"
title = "Change selected packet colors."
description = '''I see how to change the colors of foreground (characters) &amp;amp; background in a captured trace, but when I select a packet it&#x27;s white on light green and barely readable. It doesn&#x27;t matter which pre-selected packet coloring is applied. (I.E. Bad TCP is Red on Black but when selected it&#x27;s white on lig...'''
date = "2012-04-13T10:38:00Z"
lastmod = "2012-04-13T21:18:00Z"
weight = 10134
keywords = [ "color", "coloring", "colorization", "selection", "selected" ]
aliases = [ "/questions/10134" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Change selected packet colors.](/questions/10134/change-selected-packet-colors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10134-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see how to change the colors of foreground (characters) &amp; background in a captured trace, but when I select a packet it's white on light green and barely readable. It doesn't matter which pre-selected packet coloring is applied. (I.E. Bad TCP is Red on Black but when selected it's white on light green.)</p><p>How do I change the colors of a selected packet to something easier to see? (Such as black on light green?)</p></div><div id="question-tags" class="tags-container tags">color coloring colorization selection selected</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '12, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/c609362c709623fe3591a5da33a4937b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PReinie&#39;s gravatar image" /><p>PReinie<br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PReinie has no accepted answers">0%</span></p></div></div><div id="comments-container-10134" class="comments-container"></div><div id="comment-tools-10134" class="comment-tools"></div><div class="clear"></div><div id="comment-10134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10145"></span>

<div id="answer-container-10145" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10145-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>When I select a packet in Wireshark, on any computer that I have access to, the selected packet is always white on dark blue, regardless of what color filters are in place. I can't find anywhere--in Wireshark--to change the color of selected packets. The only way I was finally able to change the color of selected packets was to change the Windows color scheme.</p><p>So, is it possible that your selected packets are white on light green because you've changed the Windows system colors? If so, changing the Windows color scheme might be the only way to get a more readable display.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '12, 21:18</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-10145" class="comments-container"><span id="10147"></span><div id="comment-10147" class="comment"><div id="post-10147-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Jim, but I'm on a Mac.</p><p>For all the wonderful graphics things Macs can do, it simply amazes me that as near as I can tell you can't pick your own colors for such simple things as window borders, and with the latest Mac release, they even got rid of the scroll elevator arrows!</p><p>So, I have no color scheme to pick from. On other versions of Mac OS the colors were different. But maybe it was a different release of Wireshark. I don't have the resources (including time) to tell.</p><p>I too couldn't find anywhere to change the selected text colors, which is why I posted the question.</p><p>Phil</p></div><div id="comment-10147-info" class="comment-info"><span class="comment-age">(14 Apr '12, 13:52)</span> PReinie</div></div><span id="10149"></span><div id="comment-10149" class="comment"><div id="post-10149-score" class="comment-score"></div><div class="comment-text"><p>@PReinie, The selected-item color on my iMac is not the same as yours (it's a grayish blue BG with white FG). I could be wrong, but I think this color might actually be controlled by GTK color themes and not OSX. I'd look into <a href="http://orford.org/gtk/"><code>gtkrc</code></a>, and see a similar Ubuntu <a href="http://askubuntu.com/questions/63126/how-do-i-change-the-selected-items-color">question</a>.</p></div><div id="comment-10149-info" class="comment-info"><span class="comment-age">(14 Apr '12, 15:15)</span> helloworld</div></div><span id="10152"></span><div id="comment-10152" class="comment"><div id="post-10152-score" class="comment-score"></div><div class="comment-text"><p>Which file &amp; element do I change? I tried changing one but wireshark reloaded another version. Maybe I have to change permissions on the file (but which file)?</p><p>A work-around is to select a packet (get white characters on light green) then click once with the mouse in the lowest panel (the expanded content of the selected packet) the focus goes to that point, and the selected line (packet) remains selected but changes to white on a darker gray, which is easily visible. It's a work-around that works. (This doesn't count as answering my own question.)</p></div><div id="comment-10152-info" class="comment-info"><span class="comment-age">(14 Apr '12, 23:20)</span> PReinie</div></div><span id="10153"></span><div id="comment-10153" class="comment"><div id="post-10153-score" class="comment-score"></div><div class="comment-text"><p>BTW, what is this voting thing? Where do I do it?</p></div><div id="comment-10153-info" class="comment-info"><span class="comment-age">(14 Apr '12, 23:22)</span> PReinie</div></div><span id="10155"></span><div id="comment-10155" class="comment"><div id="post-10155-score" class="comment-score"></div><div class="comment-text"><p>The file is named "gtkrc". If you installed GTK through Macports, its location is in <code>/opt/local/share</code> somewhere. Use the <code>find</code> command to locate it. I think the property you need is named "selected_bg_color" (based on the question I had linked to in my last comment...take a look).</p></div><div id="comment-10155-info" class="comment-info"><span class="comment-age">(14 Apr '12, 23:38)</span> helloworld</div></div><span id="10157"></span><div id="comment-10157" class="comment not_top_scorer"><div id="post-10157-score" class="comment-score"></div><div class="comment-text"><p>You can vote by clicking the "thumbs up"/"thumbs down" icon in the top left corner of a question/answer. You can also upvote a comment by clicking the "thumbs up" in the bottom right corner of the comment. Click the vote button again to undo, but you're only allowed to "unvote" for a short period after the vote occurred (I think comments have 60 minutes).</p></div><div id="comment-10157-info" class="comment-info"><span class="comment-age">(14 Apr '12, 23:46)</span> helloworld</div></div><span id="10164"></span><div id="comment-10164" class="comment not_top_scorer"><div id="post-10164-score" class="comment-score"></div><div class="comment-text"><p>Actually, the unvote period applies only to votes on questions and answers (it's currently set to 1 day). You can unvote comments anytime.</p></div><div id="comment-10164-info" class="comment-info"><span class="comment-age">(15 Apr '12, 11:38)</span> helloworld</div></div></div><div id="comment-tools-10145" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-10145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

