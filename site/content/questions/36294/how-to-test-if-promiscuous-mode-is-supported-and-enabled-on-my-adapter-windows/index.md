+++
type = "question"
title = "How to test if promiscuous mode is supported and enabled on my adapter? (Windows)"
description = '''How can I test whether promiscuous mode is available and enabled on my adapter? Outside the obvious setting up a test setup and trying promiscuous capture. Is there a command line that can tell me whether promiscuous capture is working OK? I have plugged my laptop into the router, but I can&#x27;t seem t...'''
date = "2014-09-13T07:55:00Z"
lastmod = "2014-09-13T15:28:00Z"
weight = 36294
keywords = [ "windows", "ethernet", "promiscuous", "winpcap" ]
aliases = [ "/questions/36294" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to test if promiscuous mode is supported and enabled on my adapter? (Windows)](/questions/36294/how-to-test-if-promiscuous-mode-is-supported-and-enabled-on-my-adapter-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36294-score" class="post-score" title="current number of votes">0</div><span id="post-36294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I test whether promiscuous mode is available and enabled on my adapter? Outside the obvious setting up a test setup and trying promiscuous capture.</p><p>Is there a command line that can tell me whether promiscuous capture is working OK?</p><p>I have plugged my laptop into the router, but I can't seem to capture any traffic oustide my own computer. I am not sure whether there is any ethernet switching happening on the router, so I need to make sure that promiscuous mode is working on my laptop first, before concluding that the switching is happening on the router.</p><p>Nothing looks off in Wireshark, the "use promiscuous mode on all adapters" is available and checked.</p><p>I use Wireshark on Windows.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '14, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/0b25afdab68afedc1da6476a2e7f4a58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rolfen&#39;s gravatar image" /><p><span>Rolfen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rolfen has no accepted answers">0%</span></p></div></div><div id="comments-container-36294" class="comments-container"></div><div id="comment-tools-36294" class="comment-tools"></div><div class="clear"></div><div id="comment-36294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36298"></span>

<div id="answer-container-36298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36298-score" class="post-score" title="current number of votes">1</div><span id="post-36298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am not sure whether there is any ethernet switching happening on the router, so I need to make sure that promiscuous mode is working on my laptop first, before concluding that the switching is happening on the router.</p></blockquote><p>The only way to <em>experimentally</em> determine whether promiscuous mode is working is to plug your computer into a non-switching hub, plug two other machines into that hub, have the other two machines exchange non-broadcast, non-multicast traffic, and run a capture program such as Wireshark and see whether it captures the traffic in question.</p><p>Most Ethernet adapters should support promiscuous mode, and Microsoft <em>might</em> require that Windows drivers for Ethernet adapters support turning promiscuous mode on in order to receive a "works with Windows" label from them, and WinPcap (which Wireshark uses on Windows) uses the standard NDIS programming interfaces for turning promiscuous mode on, so the problem is probably with the router.</p><p>Furthermore, it's probably easier to find out whether the router is at fault; find the documentation and see whether the port into which you plugged the laptop can be configured to have <em>all</em> traffic going through the router sent to it (this may be called "port mirroring" or a "SPAN port" or various other vendor-specific terms). If not, you're out of luck, promiscuous mode or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '14, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-36298" class="comments-container"><span id="36300"></span><div id="comment-36300" class="comment"><div id="post-36300-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tips and information. Might be useful.</p></div><div id="comment-36300-info" class="comment-info"><span class="comment-age">(13 Sep '14, 15:28)</span> <span class="comment-user userinfo">Rolfen</span></div></div></div><div id="comment-tools-36298" class="comment-tools"></div><div class="clear"></div><div id="comment-36298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

