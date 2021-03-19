+++
type = "question"
title = "how do I determine protocols in a network capture"
description = '''Hi there, I&#x27;m completely new to wireshark and I would like to know the correct way to determine all of the protocols the are used on the network in a specific capture, please can someone help me?'''
date = "2013-04-24T06:23:00Z"
lastmod = "2013-04-24T07:19:00Z"
weight = 20764
keywords = [ "protcols", "network" ]
aliases = [ "/questions/20764" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how do I determine protocols in a network capture](/questions/20764/how-do-i-determine-protocols-in-a-network-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20764-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I'm completely new to wireshark and I would like to know the correct way to determine all of the protocols the are used on the network in a specific capture, please can someone help me?</p></div><div id="question-tags" class="tags-container tags">protcols network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '13, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/ba098a871f62a184f74eb61b16b9abc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harry82&#39;s gravatar image" /><p>harry82<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harry82 has no accepted answers">0%</span></p></div></div><div id="comments-container-20764" class="comments-container"></div><div id="comment-tools-20764" class="comment-tools"></div><div class="clear"></div><div id="comment-20764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20765"></span>

<div id="answer-container-20765" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20765-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>the best way:</p><blockquote><p><code>Statistics -&gt; Protocol Hierarchy</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '13, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20765" class="comments-container"><span id="20767"></span><div id="comment-20767" class="comment"><div id="post-20767-score" class="comment-score"></div><div class="comment-text"><p>One should add that the Protocol Hierarchy only shows what Wireshark has been able to determine. So if there is a protocol that Wireshark doesn't know or which runs on a port it doesn't recognize, it will not appear in the statistics.</p></div><div id="comment-20767-info" class="comment-info"><span class="comment-age">(24 Apr '13, 08:37)</span> Jasper ♦♦</div></div><span id="20772"></span><div id="comment-20772" class="comment"><div id="post-20772-score" class="comment-score"></div><div class="comment-text"><p>Thank you all for your time, it is most appreciated</p><p>H</p></div><div id="comment-20772-info" class="comment-info"><span class="comment-age">(24 Apr '13, 10:16)</span> harry82</div></div></div><div id="comment-tools-20765" class="comment-tools"></div><div class="clear"></div><div id="comment-20765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20766"></span>

<div id="answer-container-20766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20766-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another way (if you're more command-line oriented) is to use "tshark -T fields -eframe.protocols -nr filename.pcap" and then do some work to sort and unique the output. There's even a simple script in the Wireshark source code distribution (tools/list_protos_in_cap.sh) that does this for you. Basically what it does (after error checking, etc.) is:</p><pre><code># Extract the protocol names.
$TSHARK -T fields -eframe.protocols -nr &quot;$CF&quot; 2&gt;/dev/null | tr &#39;:\r&#39; &#39;\n&#39; \
    | sort -u | tr &#39;\n\r&#39; &#39; &#39;</code></pre><p>(Note that this is using the *NIX utilities 'tr' and 'sort' which probably don't exist on Windows unless you have Cygwin installed.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '13, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-20766" class="comments-container"></div><div id="comment-tools-20766" class="comment-tools"></div><div class="clear"></div><div id="comment-20766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

