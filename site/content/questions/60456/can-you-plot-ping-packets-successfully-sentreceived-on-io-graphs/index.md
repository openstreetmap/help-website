+++
type = "question"
title = "Can you plot ping packets successfully sent/received on IO graphs?"
description = '''Hi all. I&#x27;m currently doing an experiment using Mininet in which I&#x27;ve set up an OpenFlow SDN and I&#x27;m attempting to DDoS it using Hping3. I issue the Hping3 command and then kill it which overloads the network and then I send a ping between two other hosts within the network and my plan is to try and...'''
date = "2017-03-30T14:55:00Z"
lastmod = "2017-03-31T09:11:00Z"
weight = 60456
keywords = [ "openflow", "mininet", "icmp", "hping3", "iograph" ]
aliases = [ "/questions/60456" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can you plot ping packets successfully sent/received on IO graphs?](/questions/60456/can-you-plot-ping-packets-successfully-sentreceived-on-io-graphs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60456-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all.</p><p>I'm currently doing an experiment using Mininet in which I've set up an OpenFlow SDN and I'm attempting to DDoS it using Hping3. I issue the Hping3 command and then kill it which overloads the network and then I send a ping between two other hosts within the network and my plan is to try and gauge how long it takes for the network to become fully functional again by seeing how long it takes for the ping packets to be successfully sent without interruption or heavy delays.</p><p>All of the above is fine but in the IO function all I've been able to show is packets per second between the host and destination devices, whereas as I'm trying to show how network connectivity is affected I'd ideally like to show either ping packets successfully sent by the source host or received by the destination host. Can this be achieved using the IO graph function?</p><p>Hopefully the above makes sense and thanks for any advice that can be given.</p></div><div id="question-tags" class="tags-container tags">openflow mininet icmp hping3 iograph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '17, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/8dc16372ba0f25c4251e4514544d2841?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NSE17&#39;s gravatar image" /><p>NSE17<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NSE17 has no accepted answers">0%</span></p></div></div><div id="comments-container-60456" class="comments-container"></div><div id="comment-tools-60456" class="comment-tools"></div><div class="clear"></div><div id="comment-60456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60492"></span>

<div id="answer-container-60492" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60492-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're looking for <strong><em>successful</em></strong> ICMP echo replies, then you might want to plot things a bit differently. For example:</p><pre><code>Name                       Display filter       Color Style
ICMP requests              icmp.type eq 8       Blue  Dot
ICMP Successful Responses  icmp.resp_to         Green Impulse</code></pre><p>You might even want to specifically plot ICMP request packets for which no response was found, e.g.:</p><pre><code>ICMP No Response           icmp.resp_not_found  Red   Line</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '17, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-60492" class="comments-container"><span id="60494"></span><div id="comment-60494" class="comment"><div id="post-60494-score" class="comment-score"></div><div class="comment-text"><p>Oh, that's useful! I didn't know about resp_to and resp_not_found. Thanks :-)</p></div><div id="comment-60494-info" class="comment-info"><span class="comment-age">(31 Mar '17, 10:07)</span> cepheidlight</div></div></div><div id="comment-tools-60492" class="comment-tools"></div><div class="clear"></div><div id="comment-60492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60467"></span>

<div id="answer-container-60467" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60467-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would define a filter "icmp.type == 8" on the graph, something like this screen capture shows: <a href="https://notalwaysthenetwork.files.wordpress.com/2014/04/screen-shot-2014-04-08-at-10-51-25-pm.png">https://notalwaysthenetwork.files.wordpress.com/2014/04/screen-shot-2014-04-08-at-10-51-25-pm.png</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '17, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/56e5e44d5dc2d9ad0bb4e0ced530c56b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cepheidlight&#39;s gravatar image" /><p>cepheidlight<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cepheidlight has no accepted answers">0%</span></p></div></div><div id="comments-container-60467" class="comments-container"><span id="60478"></span><div id="comment-60478" class="comment"><div id="post-60478-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response, that is basically exactly what I'd like to show in my graph. However, despite getting a steady flow of pings successfully sending my IO graph looks like this - <a href="http://tinypic.com/r/3a1bb/9">http://tinypic.com/r/3a1bb/9</a></p><p>What could be going wrong?</p><p>I should say, this is the result of a normal ping test between two hosts within the network, as opposed to one that's been done while the network is overloaded.</p></div><div id="comment-60478-info" class="comment-info"><span class="comment-age">(31 Mar '17, 06:23)</span> NSE17</div></div><span id="60489"></span><div id="comment-60489" class="comment"><div id="post-60489-score" class="comment-score"></div><div class="comment-text"><p>Problem solved - I had capture set to the wrong interface. Working as expected now. Thanks for the help!</p></div><div id="comment-60489-info" class="comment-info"><span class="comment-age">(31 Mar '17, 08:46)</span> NSE17</div></div><span id="60491"></span><div id="comment-60491" class="comment"><div id="post-60491-score" class="comment-score"></div><div class="comment-text"><p>nice that it works!</p></div><div id="comment-60491-info" class="comment-info"><span class="comment-age">(31 Mar '17, 09:02)</span> cepheidlight</div></div></div><div id="comment-tools-60467" class="comment-tools"></div><div class="clear"></div><div id="comment-60467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

