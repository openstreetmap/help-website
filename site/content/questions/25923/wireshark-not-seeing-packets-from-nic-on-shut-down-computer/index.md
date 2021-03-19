+++
type = "question"
title = "Wireshark not seeing packets from NIC on shut-down computer"
description = '''I have found a situation where WireShark seems to be ignoring packets. I have noticed that after shutting off a computer of mine, and turning off the power to the node as well! ... that the NIC is still active on the network. The communication the NIC is making with the router in this condition is b...'''
date = "2013-10-11T15:06:00Z"
lastmod = "2013-10-11T15:06:00Z"
weight = 25923
keywords = [ "capture" ]
aliases = [ "/questions/25923" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not seeing packets from NIC on shut-down computer](/questions/25923/wireshark-not-seeing-packets-from-nic-on-shut-down-computer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25923-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have found a situation where WireShark seems to be ignoring packets. I have noticed that after shutting off a computer of mine, <strong>and turning off the power to the node as well!</strong> ... that the NIC is still active on the network. <strong>The communication the NIC is making with the router in this condition is being completely ignored by WireShark.</strong> I will be using other protocol analyzers to see if this phenomenon is happening with them as well.</p><p><em>What does this mean? It is very disturbing.</em></p><p>I will get back on this as soon as I have more information.</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '13, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/e3974184a5641c70b587b0b6aac5a0f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heurist&#39;s gravatar image" /><p>Heurist<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heurist has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 12 Aug '15, 20:07</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-25923" class="comments-container"><span id="45030"></span><div id="comment-45030" class="comment"><div id="post-45030-score" class="comment-score"></div><div class="comment-text"><p>So are you saying that the machine with the NIC in question has been powered off?</p><p>What indicates that the NIC is still active on the network?</p></div><div id="comment-45030-info" class="comment-info"><span class="comment-age">(12 Aug '15, 20:08)</span> Guy Harris ♦♦</div></div><span id="45131"></span><div id="comment-45131" class="comment"><div id="post-45131-score" class="comment-score"></div><div class="comment-text"><blockquote><p>and turning off the power to the node as well! ... that the NIC is still active on the network.</p></blockquote><p>A NIC <strong>without power</strong>, being active on the network. Does that sound logical?</p><p>I guess you should add much more details, if you want any useful help ;-)</p><ul><li>is that computer a laptop (with included battery!)?</li><li>what do you mean by "NIC is still <strong>active</strong>"?</li><li>how do you know it's the NIC of the powered-down computer?</li><li>how do you know that there is <strong>activity</strong> of the NIC if Wireshark does not show the traffic?</li></ul></div><div id="comment-45131-info" class="comment-info"><span class="comment-age">(15 Aug '15, 02:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25923" class="comment-tools"></div><div class="clear"></div><div id="comment-25923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

