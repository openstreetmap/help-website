+++
type = "question"
title = "T.38 packet loss in Graph Analysis?"
description = '''Hi, I’m having a trace of a Fax call using T.38. When I look at the packets I don’t see anything wrong. I found a match when I searched for the subject below, however there’s no answer to this issue. https://supportforums.cisco.com/discussion/12440601/spa122-t38-fails-some-lines In the Graph Analysi...'''
date = "2016-12-13T01:16:00Z"
lastmod = "2016-12-13T01:16:00Z"
weight = 58034
keywords = [ "graph", "t.38", "packetloss" ]
aliases = [ "/questions/58034" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [T.38 packet loss in Graph Analysis?](/questions/58034/t38-packet-loss-in-graph-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58034-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I’m having a trace of a Fax call using T.38. When I look at the packets I don’t see anything wrong. I found a match when I searched for the subject below, however there’s no answer to this issue. <a href="https://supportforums.cisco.com/discussion/12440601/spa122-t38-fails-some-lines">https://supportforums.cisco.com/discussion/12440601/spa122-t38-fails-some-lines</a></p><p>In the Graph Analysis there something like Duration: 46.56s Pack lost, Pack burst lost 90 When I check the timestamp, there is nothing special that can be observed in the T.38 framing.</p><p>Can somebody explain what this means. The issue in this case is that for a fax one end is sending and somewhere at the half at the page (judging the timestamps of the error in the flow graph) there is suddently a packet lost indication? The sequence numbers in the file is correct there is no packet loss at the UDP level. What does this packet loss mean that is only visable in the graph flow? As this packet loss appears in the sending direction, what does it mean, did the sender make errors on the T.38 level?</p><p>Thanks!</p><p><img src="https://osqa-ask.wireshark.org/upfiles/T38_packet_loss_48WEeTP.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">graph t.38 packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '16, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/45929f45e87892991e11f860e77af0d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcelV&#39;s gravatar image" /><p>MarcelV<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcelV has no accepted answers">0%</span></p></img></div></div><div id="comments-container-58034" class="comments-container"></div><div id="comment-tools-58034" class="comment-tools"></div><div class="clear"></div><div id="comment-58034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

