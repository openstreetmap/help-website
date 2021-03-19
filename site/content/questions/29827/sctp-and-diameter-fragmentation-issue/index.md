+++
type = "question"
title = "SCTP and DIAMETER fragmentation issue"
description = '''There is an inter-dependency between SCTP- and DIAMETER-protocol analysis in case of fragmented packets.  When the preferences for SCTP protocl are set to &quot;Reassemble fragmented SCTP user messages&quot; the packet is shown as &quot;SCTP SACK DATA (Message Fragment). When the &quot;Reassemble fragmented SCTP user m...'''
date = "2014-02-13T03:19:00Z"
lastmod = "2014-02-13T13:20:00Z"
weight = 29827
keywords = [ "diameter", "sctp", "packets", "fragmented" ]
aliases = [ "/questions/29827" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SCTP and DIAMETER fragmentation issue](/questions/29827/sctp-and-diameter-fragmentation-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29827-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There is an inter-dependency between SCTP- and DIAMETER-protocol analysis in case of fragmented packets.<br />
</p><p>When the preferences for SCTP protocl are set to "Reassemble fragmented SCTP user messages" the packet is shown as "SCTP SACK DATA (Message Fragment).<br />
When the "Reassemble fragmented SCTP user messages" is deactivated in the preferences for SCTP protocl then the packet is shown as DIAMETER message, but it cannot be fully presented. It is truncated with the hint [Unreassembled Packet: DIAMETER].<br />
</p><p>Of course I would like to have the packet reassembled and correctly presented as DIAMETER packet.<br />
</p><p>Is this a bug?</p></div><div id="question-tags" class="tags-container tags">diameter sctp packets fragmented</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '14, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/f76e1057a16ab7d81c0981c956f34ae1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="efranz&#39;s gravatar image" /><p>efranz<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="efranz has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '14, 03:53</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></br></p></div></div><div id="comments-container-29827" class="comments-container"></div><div id="comment-tools-29827" class="comment-tools"></div><div class="clear"></div><div id="comment-29827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29840"></span>

<div id="answer-container-29840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29840-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're seeing <code>SCTP SACK DATA (Message Fragment)</code> then you're not looking at the final SCTP segment <strong>or</strong> if you are looking at the final fragment then Wireshark was, for some reason, not able to reassemble the fragments together (a common cause is one of the fragments is missing).</p><p>In other words, if you're looking at a series of fragments with reassembly enabled you should see:</p><ol><li>SCTP DATA (Message Fragment)</li><li>SCTP DATA (Message Fragment)</li><li>DIAMETER [...] - this frame will contain all the payload of frames 1-3 reassembled and dissected as Diameter</li></ol><p>It sounds to me like right now you're looking at frame 1 or 2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '14, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></p></div></div><div id="comments-container-29840" class="comments-container"><span id="29896"></span><div id="comment-29896" class="comment"><div id="post-29896-score" class="comment-score"></div><div class="comment-text"><p>In my case I only see one SCTP DATA (Message Fragement) packet but no following DIAMETER packet.<br />
The reason for that may be an inconsistency in handling of packet fragmentation which I detected (please confirm). The inconsistency is as follows:<br />
</p><p>The DATA chunk in the mentioned packet SCTP DATA (Message Fragement) has set the B-Bit set but not the E-Bit, which means it is the first segment of a segmented DATA chunk.<br />
On the other hand the IP header of the same packet has the Don't fragment bit set. Therefore the next DATA chunk is not received.<br />
</p><p>In Wireshark I can see the packet either as<br />
- SCTP DATA (Message Fragement) if the "Reassemble fragmented SCTP user messages" is set , or<br />
- the identified DIAMETER message if the "Reassemble fragmented SCTP user messages" is not set. In this case the Diameter message is truncated.<br />
</p><p>Isn't this the explanation of the strange behavior?</p></div><div id="comment-29896-info" class="comment-info"><span class="comment-age">(15 Feb '14, 12:52)</span> efranz</div></div><span id="29932"></span><div id="comment-29932" class="comment"><div id="post-29932-score" class="comment-score">1</div><div class="comment-text"><p>Hmm, I'm not sure I follow. Are you sure the 2nd fragment was captured? That is, if you remove all display filters can you see the last fragment?</p><p>If all the fragments were captured then Wireshark should be able to reassemble them (when the preference is turned on); if not then something weird is going on (possibly a bug). If they weren't all captured then obviously this won't be possible.</p><p>The DF bit should be set on all SCTP packets: that's what tells routers to tell the sending SCTP when they encountered an MTU smaller than the size of the message which causes SCTP to lower its path MTU. (OK so when SCTP retransmits the too-big-to-pass message it will do so without the DF bit set but that'll only happen at most a couple of times per assoc.)</p></div><div id="comment-29932-info" class="comment-info"><span class="comment-age">(17 Feb '14, 06:57)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-29840" class="comment-tools"></div><div class="clear"></div><div id="comment-29840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

