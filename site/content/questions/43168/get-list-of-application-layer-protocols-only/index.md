+++
type = "question"
title = "Get list of application layer protocols only"
description = '''I&#x27;m currently using this to get a list of protocols found in a pcap file.  tshark -r ~/Downloads/smallFlows.pcap -Tfields -eframe.protocols | sort | uniq  I would like to narrow this down to application layer protocols only. Can I do this without filtering the output with a script (ie: Tshark and te...'''
date = "2015-06-15T02:32:00Z"
lastmod = "2015-06-15T09:51:00Z"
weight = 43168
keywords = [ "application", "layer", "tshark" ]
aliases = [ "/questions/43168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get list of application layer protocols only](/questions/43168/get-list-of-application-layer-protocols-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm currently using this to get a list of protocols found in a <code>pcap</code> file.</p><pre><code>tshark -r ~/Downloads/smallFlows.pcap -Tfields -eframe.protocols | sort | uniq</code></pre><p>I would like to narrow this down to application layer protocols only. Can I do this without filtering the output with a script (ie: Tshark and terminal commands only?)</p><p><strong>EDIT</strong></p><p>I managed to get it doing this:</p><pre><code>tshark -r ~/Downloads/smallFlows.pcap -Tfields -eframe.protocols -R &quot;tcp &amp;&amp; ip.addr==192.168.3.131&quot; -2 | sort | uniq | cut -d &#39;:&#39; -f 5</code></pre><p>I'm curious to know if there's a better way of doing this though!</p></div><div id="question-tags" class="tags-container tags">application layer tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '15, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/22bad9a064da49d907e0ef63fdae2016?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexandre%20Kaskasoli&#39;s gravatar image" /><p>Alexandre Ka...<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexandre Kaskasoli has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jun '15, 02:47</p></div></div><div id="comments-container-43168" class="comments-container"></div><div id="comment-tools-43168" class="comment-tools"></div><div class="clear"></div><div id="comment-43168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43192"></span>

<div id="answer-container-43192" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43192-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How about this one?</p><blockquote><p>tshark -nr input.pcap -T fields -e frame.protocols | tr ":" "\n" | egrep -v "(eth|ip|tcp|udp)" | sort -u</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '15, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43192" class="comments-container"></div><div id="comment-tools-43192" class="comment-tools"></div><div class="clear"></div><div id="comment-43192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

