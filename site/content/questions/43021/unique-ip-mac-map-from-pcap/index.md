+++
type = "question"
title = "Unique IP - MAC Map from PCAP"
description = '''I&#x27;m trying to get a list of unique IP-MAC mapping from a PCAP file. There are several answers to similar questions but none of them actually meet this exactly. I&#x27;ve tried for example this: tshark -r ~/Downloads/smallFlows.pcap -T fields -e eth.src -e ip.src -e eth.dst -e ip.dst  Which will list all ...'''
date = "2015-06-09T16:23:00Z"
lastmod = "2015-06-10T02:54:00Z"
weight = 43021
keywords = [ "pcap", "tshark" ]
aliases = [ "/questions/43021" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unique IP - MAC Map from PCAP](/questions/43021/unique-ip-mac-map-from-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43021-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to get a list of unique IP-MAC mapping from a PCAP file. There are several answers to similar questions but none of them actually meet this exactly. I've tried for example this:</p><pre><code>tshark -r ~/Downloads/smallFlows.pcap -T fields -e eth.src -e ip.src -e eth.dst -e ip.dst</code></pre><p>Which will list all IP-MAC but there will be duplicates. Piping it into <code>uniq</code> as suggested elsewhere will not work (even duplicate entries will appear on unique lines).</p><p>Ideally the output I'm looking for would be two columns, IP and MAC, of every single device in the capture (regardless of whether it's <code>src</code> or <code>dst</code>). Is this possible with the command line or will it require some scripting?</p></div><div id="question-tags" class="tags-container tags">pcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '15, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/22bad9a064da49d907e0ef63fdae2016?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexandre%20Kaskasoli&#39;s gravatar image" /><p>Alexandre Ka...<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexandre Kaskasoli has no accepted answers">0%</span></p></div></div><div id="comments-container-43021" class="comments-container"></div><div id="comment-tools-43021" class="comment-tools"></div><div class="clear"></div><div id="comment-43021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43022"></span>

<div id="answer-container-43022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43022-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think this will require some scripting, because of the duplicates you'll get. IP to MAC relationships can be 1-1, 1-n, n-1, and maybe even n-n, so tshark is not enough - you need some sort of database to track what you've seen and correlate things.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '15, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-43022" class="comments-container"></div><div id="comment-tools-43022" class="comment-tools"></div><div class="clear"></div><div id="comment-43022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43029"></span>

<div id="answer-container-43029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43029-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm trying to get a list of <strong>unique IP-MAC mapping</strong></p></blockquote><p>O.K. if you want that, you are probably just interested in the MAC address that is "tied" to an IP address. You won't neccesarily see that with your approach.</p><p>Reason:</p><p>it will work, if the systems communicate directly!</p><pre><code>   MAC1:IP1 ---&gt; IP2:MAC2</code></pre><p>It won't work, if the systems communicate through a router</p><pre><code>   MAC1:IP1 ---&gt; Router:MACR ---&gt; IP2:MAC2</code></pre><p>Furthermore, if you are printing SRC and DST at the same time (some output line), you will get much more (useless) combinations, which makes using uniq harder.</p><p>My suggestion:</p><blockquote><p>tshark -nr input.pcap -T fields -e eth.src -e ip.src | uniq &gt; out1<br />
tshark -nr input.pcap -T fields -e eth.dst -e ip.dst | uniq &gt; out2<br />
cat out1 out2 | sort -u &gt; out3<br />
</p></blockquote><p>This should bring up only the unique combinations. If you are communicating through a router, you will see the MAC address of the router many times for different IP addresses.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '15, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jun '15, 02:54</p></div></div><div id="comments-container-43029" class="comments-container"></div><div id="comment-tools-43029" class="comment-tools"></div><div class="clear"></div><div id="comment-43029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

