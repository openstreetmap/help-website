+++
type = "question"
title = "Extract certain bytes from packets programatically"
description = '''Hi, I&#x27;ve been searching for a way to do the following with no avail. I was hoping someone here could point me in the right direction. The problem is this: I have a ton of wireshark traces containing varying amount of ISCSI packets. I need to parse out the command being sent by the initiator (in byte...'''
date = "2011-09-07T19:11:00Z"
lastmod = "2011-09-07T22:13:00Z"
weight = 6203
keywords = [ "pcap", "iscsi", "wireshark", "extract", "parsing" ]
aliases = [ "/questions/6203" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract certain bytes from packets programatically](/questions/6203/extract-certain-bytes-from-packets-programatically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6203-score" class="post-score" title="current number of votes">1</div><span id="post-6203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've been searching for a way to do the following with no avail. I was hoping someone here could point me in the right direction.</p><p>The problem is this: I have a ton of wireshark traces containing varying amount of ISCSI packets. I need to parse out the command being sent by the initiator (in bytes) and write it to a file for each packet. I was originally going to do this manually, as it is easily viewable inside the wireshark application (see SS below), but some of these traces are huge (1-2 Gb), and it would take forever to do by hand.</p><p>To further clarify, what I need is this:</p><p><img src="http://img690.imageshack.us/img690/6067/wiresharksample.png" alt="alt text" /></p><p>I've been looking into tshark and rawshark documentation, but I'm not sure either is able to get me what I need. A friend suggested using libpcap to parse the traces myself, but from what I can tell I'd need to find some way to identify the bytes I need to pull out of each packet. Ideally I'd like to use something that recognizes it for me (ie wireshark's ISCSI dissector).</p><p>Can anyone point me in the right direction? I need some way to parse out these commands from each ISCSI packet without looking through the raw packet data and trying to identify which bytes I need. As a note - It's not always the last 16 bytes in the packet as shown above, so I can't just go through and take the last 16 bytes.</p><p>Any insight would be much appreciated, thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-iscsi" rel="tag" title="see questions tagged &#39;iscsi&#39;">iscsi</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '11, 19:11</strong></p><img src="https://secure.gravatar.com/avatar/221d0a1996ec18c9f46364f3090c9c0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trousers&#39;s gravatar image" /><p><span>trousers</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trousers has no accepted answers">0%</span></p></img></div></div><div id="comments-container-6203" class="comments-container"></div><div id="comment-tools-6203" class="comment-tools"></div><div class="clear"></div><div id="comment-6203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6204"></span>

<div id="answer-container-6204" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6204-score" class="post-score" title="current number of votes">0</div><span id="post-6204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you're looking for requires some programming. It can be accomplished by creating a so called tap, see <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.tapping">doc/README.tapping</a>. It basically allows the iSCSI dissector to do it's thing, identify the relevant packets for you, and send certain data out to the tap. The tap listener can collect this data and save it to a file.</p><p>A similar thing is done when you go to the menu option File|Export, there you have implementations of this model for HTTP, SMB, DICOM, etc. Have a look at there source code.</p><p>Another path could be through the use of LUA, but I'm not familiar with that.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 22:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-6204" class="comments-container"></div><div id="comment-tools-6204" class="comment-tools"></div><div class="clear"></div><div id="comment-6204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

