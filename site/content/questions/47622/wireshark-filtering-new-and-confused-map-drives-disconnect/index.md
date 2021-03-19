+++
type = "question"
title = "Wireshark Filtering, new and confused, map drives disconnect"
description = '''Hi all i am very new to WireShark (first time i have run and produced a packet capture)so any help would be much appreciated. I have a client on windows 7 pc, who is getting disconnected from the shared drive windows server 2008. I ran a WireShark capture for a few hours on the users machine to capt...'''
date = "2015-11-15T21:27:00Z"
lastmod = "2015-11-16T03:01:00Z"
weight = 47622
keywords = [ "filter", "server2008", "windows7", "disconnect", "smb" ]
aliases = [ "/questions/47622" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Filtering, new and confused, map drives disconnect](/questions/47622/wireshark-filtering-new-and-confused-map-drives-disconnect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47622-score" class="post-score" title="current number of votes">0</div><span id="post-47622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all i am very new to WireShark (first time i have run and produced a packet capture)so any help would be much appreciated.</p><p>I have a client on windows 7 pc, who is getting disconnected from the shared drive windows server 2008.</p><p>I ran a WireShark capture for a few hours on the users machine to capture the disconnects.</p><p>I have a time window between 1550 and 1559, when the user had a clear disconnect, how do i filter the log to see the disconnects and the cause of the disconnects.</p><p>currently i have filtered with the following:</p><p>(frame.time &gt;= "Nov 03, 2015 15:50:00")&amp;&amp;(frame.time &lt;= "Nov 03, 2015 15:59:00")&amp;&amp;(tcp.flags.reset == 1)</p><p>This has still given me over 102 records so am finding it very difficult to see what i am looking for.</p><p>Can someone help me filter and read the log to give a more black and white cause (if possible)</p><p>Thank you advance Diviesh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-server2008" rel="tag" title="see questions tagged &#39;server2008&#39;">server2008</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-disconnect" rel="tag" title="see questions tagged &#39;disconnect&#39;">disconnect</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '15, 21:27</strong></p><img src="https://secure.gravatar.com/avatar/0587a3186e2097d04b2fd13ec20f29b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="diviesh&#39;s gravatar image" /><p><span>diviesh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="diviesh has no accepted answers">0%</span></p></div></div><div id="comments-container-47622" class="comments-container"></div><div id="comment-tools-47622" class="comment-tools"></div><div class="clear"></div><div id="comment-47622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47629"></span>

<div id="answer-container-47629" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47629-score" class="post-score" title="current number of votes">0</div><span id="post-47629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would recommend to:<br />
1. click, in the packet list pane, at the second of those packets shown while using your filter<br />
2. clear the filter (the packet you've clicked at remains focused at)<br />
3. click at "Analyze -&gt; Follow TCP stream", a window with the conversation contents will open, but also a new display filter will be prepared and applied, so you'll (hopefully, if the capture was long enough) see the whole tcp session which has ended by RST. In the packet list pane, the highest level protocol found in each packet is displayed, so don't worry that some of them are marked as "tcp" and some as "smb" or something else<br />
4. now try to find out whether there was some reason for the RST at the protocol level.</p><p>But the rule No.1 is - Wireshark (or any other capture tool) can answer you WHAT has happened, not WHY it has happened. So if your W7 client and W2008 server are not in the same IP subnet, it may make sense to capture at both of them to see the differences; if they exist, the intermediate equipment may have affected the connection. Otherwise, only heavy packet loss (which can also be spotted by capturing at both ends) or application behaviour (fault) or hardware failure (the latter two cannot be displayed using Wireshark) can be the root causes of the disconnection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '15, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Nov '15, 03:02</strong> </span></p></div></div><div id="comments-container-47629" class="comments-container"></div><div id="comment-tools-47629" class="comment-tools"></div><div class="clear"></div><div id="comment-47629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

