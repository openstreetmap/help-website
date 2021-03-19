+++
type = "question"
title = "Is it possible to see what on my computer is requesting a webpage to be opened?"
description = '''http://websearch.linksys.com/?eg=-1367549799&amp;amp;job=blank ...is the site my computer keeps opening. If its already opened, Chrome will open up a new tab and will continue to do so. If I leave my computer sitting idle for a while, I can come back and find 5+ tabs opened up in Google Chrome to the ad...'''
date = "2011-09-09T09:22:00Z"
lastmod = "2011-09-11T13:32:00Z"
weight = 6232
keywords = [ "malware", "troubleshooting" ]
aliases = [ "/questions/6232" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to see what on my computer is requesting a webpage to be opened?](/questions/6232/is-it-possible-to-see-what-on-my-computer-is-requesting-a-webpage-to-be-opened)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6232-score" class="post-score" title="current number of votes">0</div><span id="post-6232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>http://websearch.linksys.com/?eg=-1367549799&amp;job=blank</p><p>...is the site my computer keeps opening. If its already opened, Chrome will open up a new tab and will continue to do so.</p><p>If I leave my computer sitting idle for a while, I can come back and find 5+ tabs opened up in Google Chrome to the address, even if Chrome wasn't opened when I left my computer. Changing the default browser also does nothing. It'll just continue to open the same page in, say, Firefox or whatever I change the browser to.</p><p>I've blocked the IP to the site in Windows Firewall, and that doesn't stop it either. Chrome just informs me that it can't connect to the website. And it will continue to open up new tabs regardless.</p><p>Is it possible to use Wireshark to find out WHAT exactly on my comp is trying to open this stupid website?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malware" rel="tag" title="see questions tagged &#39;malware&#39;">malware</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '11, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/154a06f1ffd8e8808740cb8732de2e83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="whaevr&#39;s gravatar image" /><p><span>whaevr</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="whaevr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Sep '11, 13:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6232" class="comments-container"><span id="6275"></span><div id="comment-6275" class="comment"><div id="post-6275-score" class="comment-score"></div><div class="comment-text"><p>That sounds like malware (or a virus). You could hunt down the offending process (with several free tools) and get rid of it. If it comes down to it, you could reformat your machine. Be sure to take <a href="http://www.pcworld.com/article/210891/how_to_avoid_malware.html">steps</a> to avoid this problem.</p></div><div id="comment-6275-info" class="comment-info"><span class="comment-age">(11 Sep '11, 13:32)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-6232" class="comment-tools"></div><div class="clear"></div><div id="comment-6232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6245"></span>

<div id="answer-container-6245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6245-score" class="post-score" title="current number of votes">1</div><span id="post-6245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it might, but it could require good timing, because Wireshark alone doesn't help with the association of program to network connection. But if you run Wireshark you can see the communication start, and with that you'll see the TCP source port your computer is using.</p><p>Now, while the browser is still trying to get the page, you need to run <code>netstat -ano</code> on the command line, which will list IPs and Ports as well as the Process IDs (PID) on the column to the right. Then, within the Windows Taskmanager, you can look up the program using this ID (you'll probably have to add the PID column first, because by default it is not shown).</p><p>Alternatively you can try <code>netstat -anb</code>, which will try to find the program name instead of the PID, but it is a lot slower (meaning that the port in question might already be closed again when it actually gets to it, giving no results).</p><p>Or you could use Microsoft NetMon, which can associate Program and Port while it captures.</p><p>Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '11, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6245" class="comments-container"></div><div id="comment-tools-6245" class="comment-tools"></div><div class="clear"></div><div id="comment-6245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

