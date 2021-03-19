+++
type = "question"
title = "Export Packet Range"
description = '''When I open a capture and filter it with a complex filter, the status bar of Wireshark displays: &quot;Packets: 973007 . Displayed: 15339 (1,6%)&quot; When I try to export only the filtered packets, the export packet range (where I can select either &#x27;all packets&#x27;, &#x27;selected packets&#x27;, &#x27;marked packets&#x27; and so o...'''
date = "2013-06-13T02:11:00Z"
lastmod = "2013-06-13T06:23:00Z"
weight = 21993
keywords = [ "displayed", "all", "export", "packets" ]
aliases = [ "/questions/21993" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Export Packet Range](/questions/21993/export-packet-range)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21993-score" class="post-score" title="current number of votes">0</div><span id="post-21993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I open a capture and filter it with a complex filter, the status bar of Wireshark displays:</p><p>"Packets: 973007 . Displayed: 15339 (1,6%)"</p><p>When I try to export only the filtered packets, the export packet range (where I can select either 'all packets', 'selected packets', 'marked packets' and so on) the column titled Displayed counts 39032 packets ... which in my opinion should be 15339.</p><p>When I mark all my displayed packets and then try to export, the number of Displayed (and Captured) packets correctly states 15339. But the 'All Packets' - 'Displayed' still counts 39032 for some reason.</p><p>Where does this number come from? Why does the statusbar say something different.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-displayed" rel="tag" title="see questions tagged &#39;displayed&#39;">displayed</span> <span class="post-tag tag-link-all" rel="tag" title="see questions tagged &#39;all&#39;">all</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '13, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/25daf811ebe1190b06093b3676a2533f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoepMeloen86&#39;s gravatar image" /><p><span>JoepMeloen86</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoepMeloen86 has one accepted answer">50%</span></p></div></div><div id="comments-container-21993" class="comments-container"><span id="21996"></span><div id="comment-21996" class="comment"><div id="post-21996-score" class="comment-score"></div><div class="comment-text"><p>what is your Wireshark version and OS?</p></div><div id="comment-21996-info" class="comment-info"><span class="comment-age">(13 Jun '13, 03:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22000"></span><div id="comment-22000" class="comment"><div id="post-22000-score" class="comment-score"></div><div class="comment-text"><p>Version 1.10.0 with Windows 8</p></div><div id="comment-22000-info" class="comment-info"><span class="comment-age">(13 Jun '13, 03:44)</span> <span class="comment-user userinfo">JoepMeloen86</span></div></div></div><div id="comment-tools-21993" class="comment-tools"></div><div class="clear"></div><div id="comment-21993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22009"></span>

<div id="answer-container-22009" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22009-score" class="post-score" title="current number of votes">2</div><span id="post-22009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JoepMeloen86 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you export the specified packets, Wireshark also exports any frames that your displayed frames depend on. For example: if you're looking at one 3000 byte HTTP message which was reassembled from 3 TCP segments the Displayed count on the bottom of the main window will say 1 but the Export Specified Packets UI will say 3.</p><p>The intention of this feature is that when you open the file that you saved that one HTTP packet to, you will actually be able to see the HTTP packet (rather than just the last TCP segment as you would have before the feature was introduced).</p><p>Yes, the UI could probably use some work. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7667">bug 7667</a>, especially comment 4.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-22009" class="comments-container"></div><div id="comment-tools-22009" class="comment-tools"></div><div class="clear"></div><div id="comment-22009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

