+++
type = "question"
title = "Any way to run wireshark standalone (not installing it)"
description = '''We have some XP machines that have an app that periodically stop communicating with the network. Problem is we have 2500 machines and it&#x27;s random that they stop. We can&#x27;t put Wireshark on every machine so I&#x27;m wondering if there&#x27;s a way that when I see one with this app not talking, i can remote in a...'''
date = "2011-12-14T14:38:00Z"
lastmod = "2011-12-14T16:00:00Z"
weight = 7983
keywords = [ "wireshark" ]
aliases = [ "/questions/7983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Any way to run wireshark standalone (not installing it)](/questions/7983/any-way-to-run-wireshark-standalone-not-installing-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7983-score" class="post-score" title="current number of votes">0</div><span id="post-7983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have some XP machines that have an app that periodically stop communicating with the network. Problem is we have 2500 machines and it's random that they stop. We can't put Wireshark on every machine so I'm wondering if there's a way that when I see one with this app not talking, i can remote in and plop down an executable and run it that way without having to actually install the program. I don't think I can but figured I'd ask.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '11, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/caa2ffd31240cafdaba6bbab216c96b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kelemvor&#39;s gravatar image" /><p><span>kelemvor</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kelemvor has no accepted answers">0%</span></p></div></div><div id="comments-container-7983" class="comments-container"></div><div id="comment-tools-7983" class="comment-tools"></div><div class="clear"></div><div id="comment-7983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7984"></span>

<div id="answer-container-7984" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7984-score" class="post-score" title="current number of votes">1</div><span id="post-7984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You've got several options. Here are the ones I can think of off the top of my head:</p><ol><li>Run the PortableApps version (http://portableapps.com) of Wireshark. When a machine stops communicating, plug your USB flash drive in to that machine, and launch Wireshark Portable. Wireshark itself will run without being installed on the PC. Wireshark requires Winpcap in order to capture traffic, so it will install Winpcap if Winpcap is not already installed on the PC, but it will offer to remove it and clean up when you exit Wireshark.</li><li>Download the Windows port of tcpdump found at http://www.microolap.com. You can use this to capture the traffic and save it to disk, then move the file to another machine that has Wireshark installed for the actual analysis. Tcpdump requires no installation. You can simply copy it to the hard drive and execute it. Or not copy it to the hard drive, and execute it from a network share or from a flash drive.</li><li>Install Wireshark on a laptop. When a machine stops communicating with the app, assuming you can break the link momentarily, throw a hub inline between the PC and the switch and connect Wireshark to the hub to capture traffic.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '11, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-7984" class="comments-container"></div><div id="comment-tools-7984" class="comment-tools"></div><div class="clear"></div><div id="comment-7984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

