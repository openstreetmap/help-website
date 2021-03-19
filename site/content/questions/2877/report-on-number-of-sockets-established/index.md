+++
type = "question"
title = "report on number of sockets established"
description = '''Hello: We have a capture we are using to troubleshoot an application issue. our application establishes TCP sockets between medical devices and a custom gateway applicaiton on a specific server-side TCP port and IP address. What i&#x27;m looking for help on is this: How can I use wireshark or additional ...'''
date = "2011-03-16T12:10:00Z"
lastmod = "2011-03-16T14:59:00Z"
weight = 2877
keywords = [ "count", "of", "number", "established", "sockets" ]
aliases = [ "/questions/2877" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [report on number of sockets established](/questions/2877/report-on-number-of-sockets-established)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2877-score" class="post-score" title="current number of votes">0</div><span id="post-2877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello:</p><p>We have a capture we are using to troubleshoot an application issue. our application establishes TCP sockets between medical devices and a custom gateway applicaiton on a specific server-side TCP port and IP address.</p><p>What i'm looking for help on is this:</p><p>How can I use wireshark or additional tool to build a query for the number of established socketed connections contained in the capture?</p><p>In other words, after the three way handshake completes, and a socket is established between device and gateway, i'd like to be able to tally them. Ideally, i'd like to be able to pull out the time stamp for each socketed connection that is successfully established.</p><p>So for example, if 1000 3-way handshakes complete and a socket is established between devices and Gateway, i'd like to be able to end up with a list of each successful connection and it's timestamp.</p><p>From there, I can use excel or Access to graph it out over time.</p><p>our custom server side application has no means of reporting on successfully established sockets over time. We are trying to evaluate how the application serves under different medical device loads in order to measure socket performance under different loads.</p><p>Being able to use a wireshark capture to break down the data would be very helpful to graph performance over time.</p><p>I'm also hoping what ever technique that is suggested here to obtain the data i'm looking for out of the wireshark capture for the number of successfully established socketed connections may also lead me to use a similar mechanism to track the # of forced resets, and maybe the number of normal socket closes.</p><p>but for now, i'd love to be able to pull the time stamp, ip address of the source medical device, per row, that represents a successful establishment of a socket from a wireshark capture.</p><p>thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-of" rel="tag" title="see questions tagged &#39;of&#39;">of</span> <span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span> <span class="post-tag tag-link-established" rel="tag" title="see questions tagged &#39;established&#39;">established</span> <span class="post-tag tag-link-sockets" rel="tag" title="see questions tagged &#39;sockets&#39;">sockets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '11, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/2ce55a604bc27b5e99159944c96d9046?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bubbawny69&#39;s gravatar image" /><p><span>bubbawny69</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bubbawny69 has no accepted answers">0%</span></p></div></div><div id="comments-container-2877" class="comments-container"></div><div id="comment-tools-2877" class="comment-tools"></div><div class="clear"></div><div id="comment-2877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2880"></span>

<div id="answer-container-2880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2880-score" class="post-score" title="current number of votes">2</div><span id="post-2880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <code>tshark</code> to achieve these kind of statistics:</p><pre><code>$tshark -r tmp.cap -R &quot;tcp.flags==16 &amp;&amp; tcp.seq==1 &amp;&amp; tcp.ack==1 &amp;&amp; tcp.len==0&quot; -T fields -e ip.src | sort -n | uniq -c
   1 192.168.1.20
  23 192.168.1.242
   1 192.168.1.4
   2 192.168.2.103
$</code></pre><p>The display filter I used filters packets that have only the ACK flag set and SEQ and ACK both 1 and a segment length of 0 (which will be true for the ACK in the 3-way-handshake). This only works when you are using relative sequence numbers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '11, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2880" class="comments-container"></div><div id="comment-tools-2880" class="comment-tools"></div><div class="clear"></div><div id="comment-2880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

