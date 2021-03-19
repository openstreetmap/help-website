+++
type = "question"
title = "Why multiple capture filter options don&#x27;t work when used in startup with Wireshark arguments ?"
description = '''I have the wireshark Version 1.10.8 (v1.10.8-2-g52a5244 from master-1.10) running on a server.  I have set the following arguments in the Wireshark shortcut link &quot;C:&#92;Program Files&#92;Wireshark&#92;Wireshark.exe&quot; -i 6 -i 5 -f &quot;port 2152&quot; -k&quot; I have no problem with this. When opening the shortcut, Wireshark ...'''
date = "2014-07-10T12:19:00Z"
lastmod = "2014-07-10T14:54:00Z"
weight = 34575
keywords = [ "interfaces", "capture-filter", "startup", "arguments", "wireshark" ]
aliases = [ "/questions/34575" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why multiple capture filter options don't work when used in startup with Wireshark arguments ?](/questions/34575/why-multiple-capture-filter-options-dont-work-when-used-in-startup-with-wireshark-arguments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34575-score" class="post-score" title="current number of votes">0</div><span id="post-34575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the wireshark Version 1.10.8 (v1.10.8-2-g52a5244 from master-1.10) running on a server. I have set the following arguments in the Wireshark shortcut link</p><p>"C:\Program Files\Wireshark\Wireshark.exe" -i 6 -i 5 -f "port 2152" -k"</p><p>I have no problem with this. When opening the shortcut, Wireshark starts automatically and captures on interface # 5, 6 and only packets with port 2152.</p><p>But when I combine multiple ports in the capture filter arguments of Wireshark, this doesn't work.</p><p>"C:\Program Files\Wireshark\Wireshark.exe" -i 6 -i 5 -f "port 2152 or port 2153" -k"</p><p>When opening this shortcut, Wireshark starts automatically and captures ALL the packets on interface # 5, 6 and deosn't apply the capture filter. I stop the capture and go to the capture options and I see the capture options field with the filter I had in it. When I restart the capture now, the capture filter is applied. This behavior is the same with all possible combinations of filters. When having tow or more filters, I will always have to stop the capture and then go to the capture options just so that Wireshark will take the filter.</p><p>Anybody seen this behavior ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span> <span class="post-tag tag-link-arguments" rel="tag" title="see questions tagged &#39;arguments&#39;">arguments</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '14, 12:19</strong></p><img src="https://secure.gravatar.com/avatar/ea3b504ace9b7c68f7d5be5c12561866?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prask&#39;s gravatar image" /><p><span>Prask</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prask has no accepted answers">0%</span></p></div></div><div id="comments-container-34575" class="comments-container"><span id="34576"></span><div id="comment-34576" class="comment"><div id="post-34576-score" class="comment-score"></div><div class="comment-text"><p>Additional Notes:</p><hr /><p>I tested these combinations in the start-up arguments:</p><h2 id="interface-and-1-capture-filter-works">1 Interface and 1 Capture Filter = Works</h2><h2 id="interface-and-2-capture-filters-works">1 Interface and 2 Capture Filters = Works</h2><h2 id="interface-and-3-capture-filters-works">1 Interface and &gt;3 Capture Filters = Works</h2><h2 id="interfaces-and-1-capture-filter-works">2 Interfaces and 1 Capture Filter = Works</h2><h2 id="interfaces-and-2-capture-filters-fail">2 Interfaces and &gt;2 Capture Filters = FAIL</h2></div><div id="comment-34576-info" class="comment-info"><span class="comment-age">(10 Jul '14, 12:25)</span> <span class="comment-user userinfo">Prask</span></div></div></div><div id="comment-tools-34575" class="comment-tools"></div><div class="clear"></div><div id="comment-34575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34577"></span>

<div id="answer-container-34577" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34577-score" class="post-score" title="current number of votes">0</div><span id="post-34577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The order of the interfaces makes a difference on my system.</p><p>Does not work (meaning shows ALL traffic):<br />
</p><blockquote><p>"C:\Program Files\Wireshark\Wireshark.exe" -i 6 <strong>-i 5</strong> -f "port 2152 or port 2153" -k</p></blockquote><p>Does work (meaning shows ONLY traffic on those ports):<br />
</p><blockquote><p>"C:\Program Files\Wireshark\Wireshark.exe" <strong>-i 5</strong> -i 6 -f "port 2152 or port 2153" -k</p></blockquote><p>Looks like a bug to me. Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '14, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-34577" class="comments-container"><span id="34587"></span><div id="comment-34587" class="comment"><div id="post-34587-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, I tried your method..Still same result for me. Will report the bug.</p><p>Thanks,</p><p>Pras</p></div><div id="comment-34587-info" class="comment-info"><span class="comment-age">(10 Jul '14, 14:54)</span> <span class="comment-user userinfo">Prask</span></div></div></div><div id="comment-tools-34577" class="comment-tools"></div><div class="clear"></div><div id="comment-34577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

