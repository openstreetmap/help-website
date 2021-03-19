+++
type = "question"
title = "Need help decoding network traffic."
description = '''Due to not expose my question here, and the fact that google has snapped up this, I&#x27;m removing what was written here just in case my research would be snapped up and used by my classmates. I don&#x27;t know how to delete an entire question, so I&#x27;m doing it this way. If this is not allowed, I could post m...'''
date = "2012-11-21T09:25:00Z"
lastmod = "2012-11-21T14:45:00Z"
weight = 16169
keywords = [ "traffic", "tcpdump", "network" ]
aliases = [ "/questions/16169" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need help decoding network traffic.](/questions/16169/need-help-decoding-network-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16169-score" class="post-score" title="current number of votes">-1</div><span id="post-16169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Due to not expose my question here, and the fact that google has snapped up this, I'm removing what was written here just in case my research would be snapped up and used by my classmates.</p><p>I don't know how to delete an entire question, so I'm doing it this way.</p><p>If this is not allowed, I could post my original question here again.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '12, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/f43a1284c6784bcfcc178e6100f9b919?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tcphelp&#39;s gravatar image" /><p><span>tcphelp</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tcphelp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '12, 14:07</strong> </span></p></div></div><div id="comments-container-16169" class="comments-container"><span id="16181"></span><div id="comment-16181" class="comment"><div id="post-16181-score" class="comment-score"></div><div class="comment-text"><p>What happened? Why do you want to delete the question now? Did you try to cheat? I don't think so, as you solved most of the assignment yourself.</p></div><div id="comment-16181-info" class="comment-info"><span class="comment-age">(21 Nov '12, 14:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16182"></span><div id="comment-16182" class="comment"><div id="post-16182-score" class="comment-score"></div><div class="comment-text"><p>No cheating here, but I've spent loads of hours figuring this out, and you only have to search for one of the strings on google to get to this post and therefore you have all my work displayed for everyone to see ;) I'd just like to keep my work to myself as it's an individual assignment.</p></div><div id="comment-16182-info" class="comment-info"><span class="comment-age">(21 Nov '12, 14:45)</span> <span class="comment-user userinfo">tcphelp</span></div></div></div><div id="comment-tools-16169" class="comment-tools"></div><div class="clear"></div><div id="comment-16169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16175"></span>

<div id="answer-container-16175" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16175-score" class="post-score" title="current number of votes">0</div><span id="post-16175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your analysis is pretty good and almost complete.</p><blockquote><p>The machine with 192.168.264.128 is a (most likely) a Windows box</p></blockquote><p>hard to say, as there are no real signs for that. If it is a windows box, it must be something &gt;= Windows Vista, as it uses the source port 54955 for the HTTP connection (Frame: #11). The ephemeral port range was changed in Windows Vista:</p><blockquote><p><code>http://support.microsoft.com/kb/929851</code><br />
</p></blockquote><p>However, it could be any OS with a modified ephemeral port range.</p><p>So, what other sings are there? It denies packets on port UDP/137. As you already mentioned, that could be the Windows firewall or it's a system that has no service on UDP/137 (Windows with some disabled Netbios features or Linux/Unix).</p><p>Anything else? Well: The initial TCP window size in frame #11 could be interesting. Observe some TCP connections from a windows and a Linux box with Wireshark and compare what you see with the content of frame #11.</p><blockquote><p>To me it looks like the 128 machine is trying to access the Web Server at 13,</p></blockquote><p>Right. Frame #11.</p><blockquote><p>Furthermore I believe that the strings between 3-8 consists of the Web Server trying to access the 128 machine and resolve it's name via NetBIOS name service.</p></blockquote><p>Looks like that's happening. Which could be, because 192.168.246.13 <strong>thinks</strong> 192.168.246.128 is a Windows box !?!</p><blockquote><p>The operation fails 3 times, most likely because the 128 machine has got an internal Firewall that blocks the attempt,</p></blockquote><p>maybe</p><blockquote><p>or it's a Linux box,</p></blockquote><p>maybe</p><blockquote><p>or the last case might be that the machine is routed through an external Firewall box with NAT.</p></blockquote><p>Take a look at Frame #1 and #2 and rethink your last assumption.</p><blockquote><p>So, string 9-10 is somewhat blurry to me, as I don't know really what's going on here, besides it looks like the end of a handshake, only it seems to have failed.</p></blockquote><p>Look at the source port and compare it with the other TCP connection in the capture output.</p><blockquote><p>String 11-14 is ok, as it's a completion of a tree way handshake between the 128 and 13 machine.</p></blockquote><p>correct.</p><blockquote><p>Another thing that's confusing, is the timespan between 8-9 and 10-14. To me it seems like something's missing here, but we've not quite figured it out yet.</p></blockquote><p>Look at the source ports and you will understand.</p><blockquote><p>Another part of the assignment is to determine what kind of security level is at the machine at 192.168.246.13.</p></blockquote><p>If you ever get the solution for this assignment, please post the answer to this question. I'm eager to see how your teacher is able to deduce the 'security level' (how is that defined) of that machine from the given capture output :-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '12, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '12, 12:11</strong> </span></p></div></div><div id="comments-container-16175" class="comments-container"></div><div id="comment-tools-16175" class="comment-tools"></div><div class="clear"></div><div id="comment-16175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

