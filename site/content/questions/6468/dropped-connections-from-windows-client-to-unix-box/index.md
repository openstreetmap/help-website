+++
type = "question"
title = "Dropped connections from Windows Client to Unix box"
description = '''Hi, I am completely new to WireShark and have been struggling to find out why random telnet sessions (Windows XP clients to an older SCO Unix) have been getting dropped lately. We have been working fine since 2000, but over the last couple of years the dropped sessions started, but lately have gotte...'''
date = "2011-09-20T12:58:00Z"
lastmod = "2011-09-21T07:39:00Z"
weight = 6468
keywords = [ "connection", "dropped", "telnet" ]
aliases = [ "/questions/6468" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dropped connections from Windows Client to Unix box](/questions/6468/dropped-connections-from-windows-client-to-unix-box)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6468-score" class="post-score" title="current number of votes">0</div><span id="post-6468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am completely new to WireShark and have been struggling to find out why random telnet sessions (Windows XP clients to an older SCO Unix) have been getting dropped lately. We have been working fine since 2000, but over the last couple of years the dropped sessions started, but lately have gotten worse. I was able to download and run WireShark on one of the PC's that experienced a dropped connection today. It's a 15 or 20mg pcap file. I don't know what I am looking for and/or how to interpret the output. Can someone point me in the right direction? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-dropped" rel="tag" title="see questions tagged &#39;dropped&#39;">dropped</span> <span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '11, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/31d7b1e817c10266c09162af1de85902?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markc&#39;s gravatar image" /><p><span>markc</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markc has no accepted answers">0%</span></p></div></div><div id="comments-container-6468" class="comments-container"></div><div id="comment-tools-6468" class="comment-tools"></div><div class="clear"></div><div id="comment-6468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6469"></span>

<div id="answer-container-6469" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6469-score" class="post-score" title="current number of votes">2</div><span id="post-6469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First, I would filter on telnet sessions since that seems to be the problematic application. To do this you could put a filter into the filter bar saying <code>tcp.port==23</code> (unless your telnet sessions runs on a different TCP port; in that case substitute the port number 23 with whatever you're using). Take a look at the packets and see if there is anything unusual; since Telnet is ASCII based you could use the "Follow TCP stream" filter on session to see what is going on</p><p>Next, check if you can find TCP reset packets (filter for that would be <code>tcp.flags.reset==1</code>). TCP sessions that get terminated often have reset packets at the end, but if you don't you still might see Telnet sessions suddenly stopping to work. In that case it might help to do captures both at the telnet client and the telnet server at the same time to compare what is going back and forth. Maybe something in the middle is doing mayhem to the connection for whatever reason.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '11, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6469" class="comments-container"><span id="6477"></span><div id="comment-6477" class="comment"><div id="post-6477-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper. It helps to have a pro like yourself, providing some guidance....I really appreciate it. The Unix box is very old (scheduled to be replaced in a couple of months) and right now, some telnet sessions are better than none, so rather than screw something up trying to install WireShark on a system that I am not comfortable working on, AND is on its last leg...is probably not going to happen. However; I am certainly going to review what I have per your suggestions and will report back. If you or anyone else has any other thoughts, I would be eternally grateful to help me get our telnet sessions to a semi-reliable state.</p><p>I could be persuaded to try it on the Unix box if someone has had a similar situation and can help guide me through it.</p><p>Another thing that seems to exacerbate the telnet dropped connections is when I RDP from my Mac to a Windows server on the LAN, and/or if there seems to be a lot of network traffic. I had the Unix box on the same switch as the other users and tried moving it to its own switch with an uplink to the original switch but eventually the dropped connections come back.</p></div><div id="comment-6477-info" class="comment-info"><span class="comment-age">(21 Sep '11, 07:26)</span> <span class="comment-user userinfo">markc</span></div></div><span id="6478"></span><div id="comment-6478" class="comment"><div id="post-6478-score" class="comment-score"></div><div class="comment-text"><p>Sorry if I left a few things out, but I never recommend installing Wireshark on a box that is having trouble. Captures should always be done on a 3rd, passive box, that listens to a SPAN/Monitor/Mirror port on the switch the box to be captured is connected to. If you don't have manageable switches (thus: no SPAN) you might try using a MiniSwitch or Hub to help you to get to the data.</p><p>Regarding RDP - as far as I see it RDP will try to reestablish dropped connections, but that doesn't change the fact that the old connection was broken. Looks like there is some real trouble in your network.</p></div><div id="comment-6478-info" class="comment-info"><span class="comment-age">(21 Sep '11, 07:39)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-6469" class="comment-tools"></div><div class="clear"></div><div id="comment-6469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

