+++
type = "question"
title = "Anyone get Wireshark to work with USB modems with Windows 7?"
description = '''If not, how does one submit an enhancement request?'''
date = "2014-06-30T14:39:00Z"
lastmod = "2014-08-04T15:03:00Z"
weight = 34300
keywords = [ "windows", "usb", "7", "modems" ]
aliases = [ "/questions/34300" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Anyone get Wireshark to work with USB modems with Windows 7?](/questions/34300/anyone-get-wireshark-to-work-with-usb-modems-with-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34300-score" class="post-score" title="current number of votes">0</div><span id="post-34300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If not, how does one submit an enhancement request?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span> <span class="post-tag tag-link-7" rel="tag" title="see questions tagged &#39;7&#39;">7</span> <span class="post-tag tag-link-modems" rel="tag" title="see questions tagged &#39;modems&#39;">modems</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '14, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/e426dbf025ed801449749806146cf5aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steveje0711&#39;s gravatar image" /><p><span>steveje0711</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steveje0711 has no accepted answers">0%</span></p></div></div><div id="comments-container-34300" class="comments-container"></div><div id="comment-tools-34300" class="comment-tools"></div><div class="clear"></div><div id="comment-34300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34302"></span>

<div id="answer-container-34302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34302-score" class="post-score" title="current number of votes">1</div><span id="post-34302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's a WinPcap issue, not a Wireshark issue (Wireshark is at the mercy of WinPcap here), so you'd have to <a href="http://www.winpcap.org/bugs.htm">submit a WinPcap enhancement request</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '14, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34302" class="comments-container"><span id="34305"></span><div id="comment-34305" class="comment"><div id="post-34305-score" class="comment-score"></div><div class="comment-text"><p>Until WinPcap is updated, you can as a workaround capture USB traffic thanks to USBPcap (requires Wireshark 1.10.0 or later). It should allow you to see the data traffic encapsulated in USB packets.</p></div><div id="comment-34305-info" class="comment-info"><span class="comment-age">(30 Jun '14, 22:57)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="34307"></span><div id="comment-34307" class="comment"><div id="post-34307-score" class="comment-score"></div><div class="comment-text"><p>You might also try Network Monitor or its successor Message Analyzer from Microsoft. Wireshark can open their capture files.</p></div><div id="comment-34307-info" class="comment-info"><span class="comment-age">(01 Jul '14, 01:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="34709"></span><div id="comment-34709" class="comment"><div id="post-34709-score" class="comment-score"></div><div class="comment-text"><p>The USBPcap approach worked, thank you. How do I go about making a feature request to Wireshark developers?</p></div><div id="comment-34709-info" class="comment-info"><span class="comment-age">(16 Jul '14, 11:55)</span> <span class="comment-user userinfo">steveje0711</span></div></div><span id="34715"></span><div id="comment-34715" class="comment"><div id="post-34715-score" class="comment-score"></div><div class="comment-text"><p>This is a WinPcap limitation as Guy explained. If you want to fill an enhancement request please follow the link he provided. Or were you thinking about something else?</p></div><div id="comment-34715-info" class="comment-info"><span class="comment-age">(16 Jul '14, 15:10)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="35169"></span><div id="comment-35169" class="comment"><div id="post-35169-score" class="comment-score"></div><div class="comment-text"><p>Well, WinPcap was integrated into Wireshark, which was written to auto-sense available networkinterfaces and list them for choosing. I'd be requesting RiverBed enhance Wireshark developers to integrate USBPcap in the same way, providing a list of USB ports available for captures. The options would be seamless within Wireshark and you wouldn't need to run two separate operations to get a decode.</p></div><div id="comment-35169-info" class="comment-info"><span class="comment-age">(04 Aug '14, 14:15)</span> <span class="comment-user userinfo">steveje0711</span></div></div><span id="35170"></span><div id="comment-35170" class="comment not_top_scorer"><div id="post-35170-score" class="comment-score"></div><div class="comment-text"><p>Wireshark was written to use libpcap to detect interfaces; WinPcap is a port of libpcap to Windows, and, as Windows doesn't come with WinPcap, whereas many UN<em>Xes come with libpcap, and on those UN</em>Xes that don't come with it, the users are likely to know enough to install it themselves, the Wireshark installer for Windows was changed to install WinPcap (rather than requiring it to be installed separately).</p><p>USBPcap is a program, rather than a library, so Wireshark can't use it the same way it uses the libpcap/WinPcap library.</p><p>The <a href="http://desowin.org/usbpcap/todo.html">USBPcap todo list</a> suggests one way of plugging it into Wireshark more seamlessly, but that awaits Wireshark's extcap mechanism being finished - and it won't show up until the next release.</p><p>Another way to plug it into Wireshark <em>and into other programs using WinPcap</em> would be to make it a component of WinPcap, but that wouldn't happen until a newer WinPcap release, which awaits some libpcap work to allow WinPcap's remote capture mechanism to be available, and would also mean the USBPcap developer wouldn't be able to maintain their code separately.</p><p>If WinPcap had a plugin mechanism that would allow adding "third-party modules", USBPcap could be maintained separately, but that would require developing a plugin interface that doesn't freeze libpcap/WinPcap internals; some work has been done on that, but it's not done yet.</p><p>So the "best" you can hope for is to wait for the extcap mechanism to be finished and a future Wireshark release that includes it to come out, and for the USBPcap developers to make an extcap module. Neither Riverbed nor the Wireshark developers can directly do much about the second of those.</p></div><div id="comment-35170-info" class="comment-info"><span class="comment-age">(04 Aug '14, 14:44)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="35172"></span><div id="comment-35172" class="comment not_top_scorer"><div id="post-35172-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'd be requesting RiverBed enhance Wireshark developers to integrate USBPcap in the same way,</p></blockquote><p>I'm not sure what you are requesting, but Wireshark is an open source project. Riverbed has no influence at all on the Wireshark developers, maybe except for those who are employed at Riverbed, which are not that many.</p><p>So, besides what <span>@Guy Harris</span> said, if you need a certain feature in Wireshark you have the following options:</p><ul><li>implement it yourself and submit the patches for the benefit of all other Wireshark users (preferred option).</li><li>open an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and hope somebody is willing to implement that feature for you</li><li>pay somebody to implement it</li><li>forget about the whole thing and live without that feature ;-)</li></ul><p>Regards<br />
Kurt</p></div><div id="comment-35172-info" class="comment-info"><span class="comment-age">(04 Aug '14, 15:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-34302" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-34302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

