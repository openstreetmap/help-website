+++
type = "question"
title = "TCP window size on Windows Server 2008 and FTP transfer"
description = '''Hello, I&#x27;m currently doing a performance analyis about FTP transfer to two Servers. PROD server : Win 2008  TEST server : Win 2008 R2 Latency between client and server : ~140ms (RTT ~280ms) Doing several transfer with the TEST server it appears something strange. The TCP Windows size is never the sa...'''
date = "2014-02-19T02:38:00Z"
lastmod = "2014-02-19T07:50:00Z"
weight = 29998
keywords = [ "server2008", "window", "size" ]
aliases = [ "/questions/29998" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP window size on Windows Server 2008 and FTP transfer](/questions/29998/tcp-window-size-on-windows-server-2008-and-ftp-transfer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29998-score" class="post-score" title="current number of votes">0</div><span id="post-29998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm currently doing a performance analyis about FTP transfer to two Servers. PROD server : Win 2008 TEST server : Win 2008 R2 Latency between client and server : ~140ms (RTT ~280ms)</p><p>Doing several transfer with the TEST server it appears something strange. The TCP Windows size is never the same. I discover the new automatic mechanism on Win 2008 to define the TCP window size by using a factor. But this factor is never the same eve using the same client and the same server.</p><p>During a first test where the client was on site A, the TCP window scaling was 256. Durind a second test where the client was on site B, the TCP window scaling was only 4 !!!!</p><p>I search on google informations about how Window 2008 server select the factor and the TCP window size but I didn't find any concrete explanation.</p><p>Do you have any detail about this behaviour ? Thanks for your help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-server2008" rel="tag" title="see questions tagged &#39;server2008&#39;">server2008</span> <span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '14, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/25fcd4b6692b20e9189d8f0b52f1663d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="any-one&#39;s gravatar image" /><p><span>any-one</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="any-one has no accepted answers">0%</span></p></div></div><div id="comments-container-29998" class="comments-container"></div><div id="comment-tools-29998" class="comment-tools"></div><div class="clear"></div><div id="comment-29998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30001"></span>

<div id="answer-container-30001" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30001-score" class="post-score" title="current number of votes">0</div><span id="post-30001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Window scaling on Windows is indeed very confusing, because there is no real pattern for how it behaves (unless you disable it, of course).</p><p>If you issue the command "<strong>netsh interface tcp show global</strong>" on a command line, you'll get something like this:</p><pre><code>Querying active state...
TCP Global Parameters
Receive-Side Scaling State          : enabled
Chimney Offload State               : automatic
NetDMA State                        : enabled
Direct Cache Acess (DCA)            : disabled
Receive Window Auto-Tuning Level    : normal
Add-On Congestion Control Provider  : none
ECN Capability                      : disabled
RFC 1323 Timestamps                 : disabled
** The above autotuninglevel setting is the result of Windows Scaling heuristics
overriding any local/policy configuration on at least one profile.</code></pre><p>If you take a look at the last two lines (about the autotunglevel) you can see why it does things differently sometimes: because "Windows Scaling heuristics" have kicked in and decided how to run things. So far nobody I've spoken to could tell me what it actually does - it's just doing <em>something</em> to the Window Scaling values when the PC has run for a while.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '14, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30001" class="comments-container"><span id="30006"></span><div id="comment-30006" class="comment"><div id="post-30006-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So far nobody I've spoken to could tell me what it actually does</p></blockquote><p>There is description (more or less detailed) in an article of 'The Cable Guy'.</p><blockquote><p><a href="http://technet.microsoft.com/en-us/magazine/2007.01.cableguy.aspx">http://technet.microsoft.com/en-us/magazine/2007.01.cableguy.aspx</a></p></blockquote><p>At the end: <strong>Receive Window Auto-Tuning in Windows Vista</strong>.</p><p>Apparently they calculate the BDP (bandwidth delay product) and then dynamically adjust the window size. As the value will be adjusted to the BDP (and other statistics), the window size is totally non-deterministic. The algorithms and parameters used for the adjustment are (obviously) not described.</p></div><div id="comment-30006-info" class="comment-info"><span class="comment-age">(19 Feb '14, 06:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="30008"></span><div id="comment-30008" class="comment"><div id="post-30008-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The algorithms and parameters used for the adjustment are (obviously) not described.</p></blockquote><p>That's what I meant. I (think) have seen all available documentation on that matter :-)</p></div><div id="comment-30008-info" class="comment-info"><span class="comment-age">(19 Feb '14, 06:40)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="30009"></span><div id="comment-30009" class="comment"><div id="post-30009-score" class="comment-score"></div><div class="comment-text"><p>thanks for your answer both of you.</p><p>I already seen this article. I tried to google it and seen lot ot article website but never find answer explaining how M. MICROSOFT calculate the factor and the window size to use.</p><p>maybe it's random :)</p></div><div id="comment-30009-info" class="comment-info"><span class="comment-age">(19 Feb '14, 06:42)</span> <span class="comment-user userinfo">any-one</span></div></div><span id="30010"></span><div id="comment-30010" class="comment"><div id="post-30010-score" class="comment-score"></div><div class="comment-text"><p>I know, but maybe the OP has not yet seen them ;-))</p><p>UPDATE: Apparently he has already seen that :-) See comment above....</p></div><div id="comment-30010-info" class="comment-info"><span class="comment-age">(19 Feb '14, 06:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="30011"></span><div id="comment-30011" class="comment"><div id="post-30011-score" class="comment-score"></div><div class="comment-text"><p>interesting articles I found:</p><ul><li><p><a href="http://books.google.fr/books?id=291YkeWyZP4C&amp;pg=PA172&amp;lpg=PA172&amp;dq=windows+2008+tcp+factor&amp;source=bl&amp;ots=deX3qn8G16&amp;sig=UY33bTtQ2rBTgzVCcthEQAOt5nY&amp;hl=fr&amp;sa=X&amp;ei=XbQEU5TRNqm57AbWgYHIBw&amp;ved=0CH8Q6AEwBw#v=onepage&amp;q=windows%202008%20tcp%20factor&amp;f=false">http://books.google.fr/books?id=291YkeWyZP4C&amp;pg=PA172&amp;lpg=PA172&amp;dq=windows+2008+tcp+factor&amp;source=bl&amp;ots=deX3qn8G16&amp;sig=UY33bTtQ2rBTgzVCcthEQAOt5nY&amp;hl=fr&amp;sa=X&amp;ei=XbQEU5TRNqm57AbWgYHIBw&amp;ved=0CH8Q6AEwBw#v=onepage&amp;q=windows%202008%20tcp%20factor&amp;f=false</a></p></li><li><p><a href="http://www.minasi.com/newsletters/nws0802.htm">http://www.minasi.com/newsletters/nws0802.htm</a></p></li></ul></div><div id="comment-30011-info" class="comment-info"><span class="comment-age">(19 Feb '14, 06:45)</span> <span class="comment-user userinfo">any-one</span></div></div><span id="30017"></span><div id="comment-30017" class="comment not_top_scorer"><div id="post-30017-score" class="comment-score"></div><div class="comment-text"><p>I verified the TCP setting on each server</p><p>PROD : Receive window auto-tuning level : normal window scaling heuristics : disabled</p><p>TEST : Receive window auto-tuning level : normal window scaling heuristics : disabled</p></div><div id="comment-30017-info" class="comment-info"><span class="comment-age">(19 Feb '14, 07:47)</span> <span class="comment-user userinfo">any-one</span></div></div><span id="30018"></span><div id="comment-30018" class="comment not_top_scorer"><div id="post-30018-score" class="comment-score"></div><div class="comment-text"><p>I have seen systems where the Window Scaling factor changed depending on software installed, e.g. an Avira virus scanner.</p></div><div id="comment-30018-info" class="comment-info"><span class="comment-age">(19 Feb '14, 07:50)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-30001" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-30001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

