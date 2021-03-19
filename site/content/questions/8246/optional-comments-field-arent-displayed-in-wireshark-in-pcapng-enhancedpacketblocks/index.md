+++
type = "question"
title = "optional comments field aren&#x27;t displayed in wireshark In pcapng EnhancedPacketBlocks"
description = '''Hi, I am trying to view optional comment field present in pcapng EnhancedPacketBlocks, but wireshark is not displaying that. I see a bug (https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6229) has been fixed related to this in wireshark 1.6.2 release and i am using 1.6.3.  Do i need to do somethi...'''
date = "2012-01-05T22:55:00Z"
lastmod = "2012-01-06T11:52:00Z"
weight = 8246
keywords = [ "pcapng", "epb" ]
aliases = [ "/questions/8246" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [optional comments field aren't displayed in wireshark In pcapng EnhancedPacketBlocks](/questions/8246/optional-comments-field-arent-displayed-in-wireshark-in-pcapng-enhancedpacketblocks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8246-score" class="post-score" title="current number of votes">0</div><span id="post-8246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to view optional comment field present in pcapng EnhancedPacketBlocks, but wireshark is not displaying that. I see a bug (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6229">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6229</a>) has been fixed related to this in wireshark 1.6.2 release and i am using 1.6.3.</p><p>Do i need to do something more. Plz help.</p><p>Thanks, Ambika</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-epb" rel="tag" title="see questions tagged &#39;epb&#39;">epb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '12, 22:55</strong></p><img src="https://secure.gravatar.com/avatar/55898068b61d3986b5fd5996d329c9fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ambika&#39;s gravatar image" /><p><span>ambika</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ambika has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '12, 02:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-8246" class="comments-container"></div><div id="comment-tools-8246" class="comment-tools"></div><div class="clear"></div><div id="comment-8246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8248"></span>

<div id="answer-container-8248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8248-score" class="post-score" title="current number of votes">1</div><span id="post-8248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes.</p><p>You need to modify the API that Wireshark's Wiretap library (the source to it is in the <code>wiretap</code> directory of the Wireshark source code) exports so that, when a program such as Wireshark or TShark reads a packet, it gets the comments attached to the packet. (Extra credit for implementing it so that it can support both pcap-NG comments <em>and</em> Network Monitor capture file comments - a <em>lot</em> of extra credit, as pcap-NG comments are plain UTF-8 text while NetMon comments have a UTF-16 title and a Rich Text Format body.)</p><p>Then you need to modify the Wiretap module for reading pcap-NG files (<code>wiretap/pcap-ng.c</code>) to support that API.</p><p>Then you need to modify Wireshark to do something useful with comment fields it reads (including figuring out what "something useful" would be, e.g. putting it into the "Frame" section of the packet details, or having them pop up as tooltips in the packet list; <a href="http://blogs.technet.com/b/netmon/archive/2009/03/20/frame-commenting-is-here.aspx">here's how Network Monitor handles frame comments</a>).</p><p>Or, alternatively, you have to wait for somebody else to get around to doing it.</p><p>I.e., that's a feature that hasn't been implemented in Wireshark. The bug in question wasn't that <em>comments</em> weren't displayed, the bug was that if a frame had a comment Wireshark didn't properly return the <em>packet data</em> in the frame, so that Wireshark couldn't even show the frame's <em>data</em> correctly. That means that all the fix does is allow you to read the packets in a pcap-NG file with fame comments; it doesn't mean that anything useful is done with the frame comments.</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3096">Bug 3096</a> is the enhancement request for adding that feature.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '12, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '12, 02:15</strong> </span></p></div></div><div id="comments-container-8248" class="comments-container"><span id="8250"></span><div id="comment-8250" class="comment"><div id="post-8250-score" class="comment-score">1</div><div class="comment-text"><p>I've been playing around with this lately. I do have something very rough (the GUI parts look horrible ;). Only for pcapng, not taking into account utf8,16, ...</p><p>I am planning to create a first patch before beginning of Feb (meeting at Fosdem) so that people can comment on it, especially on the way the data is handled internally. Basically, the idea is to add a comment field to struct wtap and to struct frame_data.</p></div><div id="comment-8250-info" class="comment-info"><span class="comment-age">(06 Jan '12, 03:33)</span> <span class="comment-user userinfo">MartinKaiser</span></div></div><span id="8261"></span><div id="comment-8261" class="comment"><div id="post-8261-score" class="comment-score"></div><div class="comment-text"><p>I'm inclined to <em>reduce</em> the number of fields in <code>struct frame_data</code> over time, as there's a <code>struct frame_data</code> for every packet, and that can add up to a lot of memory. Most frames probably won't have comments in a large capture file; perhaps a separate sparse data structure using the frame number as a key and the comment(s) as a value would be better.</p></div><div id="comment-8261-info" class="comment-info"><span class="comment-age">(06 Jan '12, 11:52)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-8248" class="comment-tools"></div><div class="clear"></div><div id="comment-8248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

