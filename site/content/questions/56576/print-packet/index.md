+++
type = "question"
title = "Print Packet"
description = '''I am trying to print a packet and would like it to be presented as it is in the packet header details. But whether I print to a printer or a PDF file the packet information is presented in a narrow column on the left margin. Can anyone tell me how I can get a better print image. OS: Windows 10 64 bi...'''
date = "2016-10-22T04:40:00Z"
lastmod = "2016-10-24T09:14:00Z"
weight = 56576
keywords = [ "print", "packet" ]
aliases = [ "/questions/56576" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Print Packet](/questions/56576/print-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56576-score" class="post-score" title="current number of votes">0</div><span id="post-56576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to print a packet and would like it to be presented as it is in the packet header details. But whether I print to a printer or a PDF file the packet information is presented in a narrow column on the left margin. Can anyone tell me how I can get a better print image.</p><p>OS: Windows 10 64 bit Wireshark Legacy v2.2.1</p><ol><li>First I got to Wireshark print screen and click print</li></ol><p><img src="https://osqa-ask.wireshark.org/upfiles/Untitled1_VdrlFA2.jpg" alt="alt text" /></p><ol><li>That brings me to the print screen to print to my printer or a pdf file. I click Okay</li></ol><p><img src="https://osqa-ask.wireshark.org/upfiles/Untitled2_yAqOp2G.jpg" alt="alt text" /></p><p>Below is how it looks:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Untitled3.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-print" rel="tag" title="see questions tagged &#39;print&#39;">print</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '16, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/bf9277ce6187b3ff49cee23ff9d3beed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="desertfoxma&#39;s gravatar image" /><p><span>desertfoxma</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="desertfoxma has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '16, 13:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></img></div></div><div id="comments-container-56576" class="comments-container"><span id="56577"></span><div id="comment-56577" class="comment"><div id="post-56577-score" class="comment-score"></div><div class="comment-text"><p>My Wireshark 2.2.1 on Windows 10 prints the packets just fine, definitely not the way you describe. Can you state which operating system and Wireshark version you use, and add to your question screenshots of the individual windows you click through to get the packet printed (including the <code>Page Setup...</code> window which you may not have tried), a screenshot of <code>Edit-&gt;Preferences-&gt;Advanced</code> after writing <code>print</code> into the <code>Search:</code> field, and maybe also a screenshot of a <code>.pdf</code> result file open in a reader?</p></div><div id="comment-56577-info" class="comment-info"><span class="comment-age">(22 Oct '16, 05:21)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56579"></span><div id="comment-56579" class="comment"><div id="post-56579-score" class="comment-score"></div><div class="comment-text"><p>Sindy:</p><p>When I printed using the non-legacy version it printed fine. Just not sure why the legacy version printed as described above.</p></div><div id="comment-56579-info" class="comment-info"><span class="comment-age">(22 Oct '16, 13:35)</span> <span class="comment-user userinfo">desertfoxma</span></div></div><span id="56580"></span><div id="comment-56580" class="comment"><div id="post-56580-score" class="comment-score"></div><div class="comment-text"><p>Your images have been added to the question and your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-56580-info" class="comment-info"><span class="comment-age">(22 Oct '16, 13:53)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="56618"></span><div id="comment-56618" class="comment"><div id="post-56618-score" class="comment-score"></div><div class="comment-text"><p>Out of interest, why are you still using the legacy version as we plan to stop distributing it in the Windows installer?</p></div><div id="comment-56618-info" class="comment-info"><span class="comment-age">(24 Oct '16, 09:14)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56576" class="comment-tools"></div><div class="clear"></div><div id="comment-56576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56588"></span>

<div id="answer-container-56588" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56588-score" class="post-score" title="current number of votes">1</div><span id="post-56588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems to be a bug of the legacy version, as I haven't found any settings of symbol size or page margins which could eventually cause the behaviour. You may want to <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi?product=Wireshark">file the bug</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '16, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></img></div></div><div id="comments-container-56588" class="comments-container"><span id="56616"></span><div id="comment-56616" class="comment"><div id="post-56616-score" class="comment-score"></div><div class="comment-text"><p>For reference, a bug has been filed as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13040">Bug 13040</a>.</p></div><div id="comment-56616-info" class="comment-info"><span class="comment-age">(24 Oct '16, 08:50)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-56588" class="comment-tools"></div><div class="clear"></div><div id="comment-56588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

