+++
type = "question"
title = "How can I display all IPs that are not mine with tshark"
description = '''How can I display all IPs that are not mine with `tshark.  I need to combine those 2 commands 1.Source IPs that are not mine:   `tshark -T fields -e ip.dst -Y &quot;ip.dst != 192.168.1.55&quot;`  2.Destination IPs that are not mine: `tshark -T fields -e ip.dst -Y &quot;ip.dst != 192.168.1.55&quot;`  where 192.168.1.55 ...'''
date = "2016-10-09T11:09:00Z"
lastmod = "2016-10-09T11:44:00Z"
weight = 56266
keywords = [ "filter", "filtering", "tshark" ]
aliases = [ "/questions/56266" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I display all IPs that are not mine with tshark](/questions/56266/how-can-i-display-all-ips-that-are-not-mine-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56266-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I display all IPs that are not mine with `tshark.</p><p>I need to combine those 2 commands</p><p>1.Source IPs that are not mine:</p><pre><code>  `tshark -T fields -e ip.dst -Y &quot;ip.dst != 192.168.1.55&quot;`</code></pre><p>2.Destination IPs that are not mine:</p><pre><code>`tshark -T fields -e ip.dst -Y &quot;ip.dst != 192.168.1.55&quot;`</code></pre><p>where <code>192.168.1.55</code> is my IP.</p></div><div id="question-tags" class="tags-container tags">filter filtering tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '16, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/1d0a5c898c23c1ae1a7b009804920031?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user31415&#39;s gravatar image" /><p>user31415<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user31415 has no accepted answers">0%</span></p></div></div><div id="comments-container-56266" class="comments-container"></div><div id="comment-tools-56266" class="comment-tools"></div><div class="clear"></div><div id="comment-56266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56267"></span>

<div id="answer-container-56267" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56267-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>tshark -Y usb -z endpoints,ip</code> may be what you are looking for. By <code>-Y usb</code> you prevent any individual frames from being printed, and <code>-z endpoints,ip</code> will cause tshark to print the statistics of IPs encountered in the capture - yours will be there too, but just once, like all the others.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '16, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56267" class="comments-container"></div><div id="comment-tools-56267" class="comment-tools"></div><div class="clear"></div><div id="comment-56267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56268"></span>

<div id="answer-container-56268" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56268-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try:</p><pre><code>tshark -T fields -e ip.src -e ip.dst -Y &quot;ip.src != 192.168.1.55 and ip.dst != 192.168.1.55&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '16, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56268" class="comments-container"></div><div id="comment-tools-56268" class="comment-tools"></div><div class="clear"></div><div id="comment-56268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

