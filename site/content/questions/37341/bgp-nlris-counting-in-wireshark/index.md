+++
type = "question"
title = "BGP NLRIs - counting in Wireshark"
description = '''Can Wireshark count the number of BGP NLRIs in a capture?'''
date = "2014-10-24T17:18:00Z"
lastmod = "2014-10-26T15:44:00Z"
weight = 37341
keywords = [ "bgp", "nlri", "update" ]
aliases = [ "/questions/37341" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [BGP NLRIs - counting in Wireshark](/questions/37341/bgp-nlris-counting-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37341-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can Wireshark count the number of BGP NLRIs in a capture?</p></div><div id="question-tags" class="tags-container tags">bgp nlri update</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '14, 17:18</strong></p><img src="https://secure.gravatar.com/avatar/b130b603a833f954befbe2410bc7c387?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="candres&#39;s gravatar image" /><p>candres<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="candres has no accepted answers">0%</span></p></div></div><div id="comments-container-37341" class="comments-container"></div><div id="comment-tools-37341" class="comment-tools"></div><div class="clear"></div><div id="comment-37341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37363"></span>

<div id="answer-container-37363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37363-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not directly, but you can use tshark and some scripting.</p><blockquote><p>tshark -nr bgp.pcap -Y "bgp.update.nlri" -V -x &gt; out.txt</p></blockquote><p>Then parse out.txt with a script (perl, python, whatever) and look for something like this:</p><pre><code>   Network Layer Reachability Information (NLRI)
       172.16.0.0/16
           NLRI prefix length: 16
           NLRI prefix: 172.16.0.0 (172.16.0.0)</code></pre><p>As an alternative, you can write a LUA Listener, to count the NLRIs.</p><blockquote><p><a href="http://wiki.wireshark.org/Lua/Taps">http://wiki.wireshark.org/Lua/Taps</a><br />
<a href="https://www.wireshark.org/docs/wsug_html_chunked/wslua_tap_example.html">https://www.wireshark.org/docs/wsug_html_chunked/wslua_tap_example.html</a><br />
<a href="http://wiki.wireshark.org/Lua/Examples">http://wiki.wireshark.org/Lua/Examples</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '14, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '14, 15:49</p></div></div><div id="comments-container-37363" class="comments-container"></div><div id="comment-tools-37363" class="comment-tools"></div><div class="clear"></div><div id="comment-37363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

