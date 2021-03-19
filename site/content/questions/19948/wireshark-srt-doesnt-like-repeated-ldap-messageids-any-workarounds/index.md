+++
type = "question"
title = "Wireshark SRT doesn&#x27;t like repeated LDAP MessageIDs - any workarounds?"
description = '''The LDAP RFC allows Message-IDs to be reused, as long as the earlier request bearing the Message-ID has been completed. This plays havoc with Wireshark&#x27;s Service Response Time analysis for LDAP. It appears that the code simply determines the elapsed time between the first &quot;use in query&quot; and last &quot;us...'''
date = "2013-03-29T22:40:00Z"
lastmod = "2013-03-30T10:11:00Z"
weight = 19948
keywords = [ "srt", "ldap" ]
aliases = [ "/questions/19948" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark SRT doesn't like repeated LDAP MessageIDs - any workarounds?](/questions/19948/wireshark-srt-doesnt-like-repeated-ldap-messageids-any-workarounds)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19948-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The LDAP RFC allows Message-IDs to be reused, as long as the earlier request bearing the Message-ID has been completed.</p><p>This plays havoc with Wireshark's Service Response Time analysis for LDAP. It appears that the code simply determines the elapsed time between the first "use in query" and last "use in response" of each Message-ID, like so (capital letters are where SRT determines its measurement):</p><p>"QUERY(1)...query(2)...response(2)...RESPONSE(1)"</p><p>If the Message-ID has been repeated, however, the measurement is completely incorrect:</p><p>"QUERY(1)......response(1).......query(1).....RESPONSE(1)"</p><p>Yeah, there's a bug report to be made, but do you folks have any ideas about splitting the capture when the Message-IDs recycle? The LDAP client in question uses a range of [1..1023] for Message-IDs, so I'd like to take a capture file of a single connection and break it into chunks at each point at which a Message-ID of 1023 appears.<br />
</p><p>Any suggestions?</p></div><div id="question-tags" class="tags-container tags">srt ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '13, 22:40</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span> </br></p></div></div><div id="comments-container-19948" class="comments-container"><span id="20191"></span><div id="comment-20191" class="comment"><div id="post-20191-score" class="comment-score"></div><div class="comment-text"><p>Bug report filed - <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8570">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8570</a></p></div><div id="comment-20191-info" class="comment-info"><span class="comment-age">(08 Apr '13, 11:31)</span> wesmorgan1</div></div></div><div id="comment-tools-19948" class="comment-tools"></div><div class="clear"></div><div id="comment-19948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19957"></span>

<div id="answer-container-19957" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19957-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can always use editcap to split up the capture files, the trick will be how to sort out where to cut. You could script processing tshark output into identifying the relevant frame numbers to cut along.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '13, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19957" class="comments-container"><span id="19962"></span><div id="comment-19962" class="comment"><div id="post-19962-score" class="comment-score"></div><div class="comment-text"><p>Yeah, this is the approach I'll probably take. I found a tool (SplitCap) that can separate a large capture file into per-conversation files; from there, a quick shell script will grab frame numbers from tshark output and feed them to editcap.</p><p>I'm just really not looking forward to running SRT analyses on 300 files instead of 3-5 files. <em>laugh</em></p></div><div id="comment-19962-info" class="comment-info"><span class="comment-age">(30 Mar '13, 11:24)</span> wesmorgan1</div></div></div><div id="comment-tools-19957" class="comment-tools"></div><div class="clear"></div><div id="comment-19957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19960"></span>

<div id="answer-container-19960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19960-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could also use a Lua plugin to do it - create a Listener tap and keep track of the message-id's inside Lua so you can detect the number being used again, and save to separate pcap files using the Dumper object. But as Jaap said, the hard part is figuring out where to "cut" safely/accurately.</p><p>For example what should you do in this case?: "query(1022)...query(1023)...query(1)...response(1023)...response(1)...response(1022)"</p><p>Have you submitted a bug yet? Some bugs get fixed very quickly. Once fixed, it might take a while for the fix to show up in a new published release, but you can get the compiled nightly builds anytime.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '13, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-19960" class="comments-container"><span id="19963"></span><div id="comment-19963" class="comment"><div id="post-19963-score" class="comment-score"></div><div class="comment-text"><p>I have not submitted a bug report; I have to get this analysis finished before I go figure out the bug reporting tool. <em>laugh</em></p></div><div id="comment-19963-info" class="comment-info"><span class="comment-age">(30 Mar '13, 11:25)</span> wesmorgan1</div></div><span id="19965"></span><div id="comment-19965" class="comment"><div id="post-19965-score" class="comment-score"></div><div class="comment-text"><p>For the immediate need (i.e. the gigabytes of capture data I have to analyze), I'm going to add a fudge factor for the overlap problem you described...</p></div><div id="comment-19965-info" class="comment-info"><span class="comment-age">(30 Mar '13, 16:11)</span> wesmorgan1</div></div></div><div id="comment-tools-19960" class="comment-tools"></div><div class="clear"></div><div id="comment-19960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

