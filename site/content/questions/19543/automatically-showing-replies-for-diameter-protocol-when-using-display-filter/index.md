+++
type = "question"
title = "Automatically showing replies for DIAMETER protocol, when using display filter"
description = '''When analyzing a large packet capture of DIAMETER traffic, I often filter based on a certain value. Is there any way to automatically show the replies to the packets matching the display filter? Currently I have to select each packet, and then add the frame number to the display filter. It&#x27;s very te...'''
date = "2013-03-15T13:17:00Z"
lastmod = "2013-03-19T13:52:00Z"
weight = 19543
keywords = [ "filter", "diameter", "display", "replies" ]
aliases = [ "/questions/19543" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Automatically showing replies for DIAMETER protocol, when using display filter](/questions/19543/automatically-showing-replies-for-diameter-protocol-when-using-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19543-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When analyzing a large packet capture of DIAMETER traffic, I often filter based on a certain value. Is there any way to automatically show the replies to the packets matching the display filter? Currently I have to select each packet, and then add the frame number to the display filter. It's very tedious.</p><p>For example, my display filter will be something like "diameter contains xxxx" where xxxx is actually the IMSI of the user I'm testing with. I then have to click on each packet, and look at the diameter details, and it will say "Reply is in &lt;n&gt;" where "&lt;n&gt;" is the frame number of the response packet. My display filter then becomes "diameter contains xxxx || frame.number == n".</p></div><div id="question-tags" class="tags-container tags">filter diameter display replies</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '13, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/6b9a44ca9bd6521b049a202a50597c2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mojo&#39;s gravatar image" /><p>Mojo<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mojo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '13, 13:21</p></div></div><div id="comments-container-19543" class="comments-container"></div><div id="comment-tools-19543" class="comment-tools"></div><div class="clear"></div><div id="comment-19543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="19646"></span>

<div id="answer-container-19646" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19646-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds like a job for <a href="http://wiki.wireshark.org/Mate">MATE</a>. Unfortunately the documentation on that can be... Somewhat painful to wade through.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '13, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-19646" class="comments-container"><span id="19647"></span><div id="comment-19647" class="comment"><div id="post-19647-score" class="comment-score"></div><div class="comment-text"><p>Very cool, I will check it out. I haven't played with plugins much, but how hard could it be? ;-)</p></div><div id="comment-19647-info" class="comment-info"><span class="comment-age">(19 Mar '13, 08:20)</span> Mojo</div></div><span id="19651"></span><div id="comment-19651" class="comment"><div id="post-19651-score" class="comment-score"></div><div class="comment-text"><p>Doesn't look like MATE is being actively maintained. Most of the Wiki pages look like they are at LEAST 5 years old or more.</p></div><div id="comment-19651-info" class="comment-info"><span class="comment-age">(19 Mar '13, 09:37)</span> Mojo</div></div><span id="19655"></span><div id="comment-19655" class="comment"><div id="post-19655-score" class="comment-score"></div><div class="comment-text"><p>Yeah, that's what I meant by the documentation being a problem. It does still work--I used it within the past year or so.</p></div><div id="comment-19655-info" class="comment-info"><span class="comment-age">(19 Mar '13, 10:18)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-19646" class="comment-tools"></div><div class="clear"></div><div id="comment-19646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19660"></span>

<div id="answer-container-19660" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19660-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does it actually say, <em>"Reply is in &lt; n &gt;"</em>? Because I could only find, <code>"Answer In &lt; n &gt;"</code>.</p><p>Well, assuming that's what you're interested in, you could add 2 custom columns, one for <code>diameter.answer_in</code>, and the other for <code>diameter.answer_to</code>. The easiest way to add those columns is to expand a diameter packet containing the field, then right-click on it, choosing, <em>"Apply as Column"</em>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '13, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-19660" class="comments-container"><span id="19662"></span><div id="comment-19662" class="comment"><div id="post-19662-score" class="comment-score"></div><div class="comment-text"><p>This is useful, but not QUITE what I was looking for. I guess what I want is to write a display filter, and have it show those packets, and ALSO include the packets referenced in each diameter.answer_in field, as sort of joined query (to mix metaphors and use a database term :) ).</p></div><div id="comment-19662-info" class="comment-info"><span class="comment-age">(19 Mar '13, 14:07)</span> Mojo</div></div></div><div id="comment-tools-19660" class="comment-tools"></div><div class="clear"></div><div id="comment-19660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19546"></span>

<div id="answer-container-19546" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19546-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>One solution I just discovered on my own is to add the diameter.Session-Id parameter to the display filter. That helps a bunch.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '13, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/6b9a44ca9bd6521b049a202a50597c2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mojo&#39;s gravatar image" /><p>Mojo<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mojo has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-19546" class="comments-container"><span id="31515"></span><div id="comment-31515" class="comment"><div id="post-31515-score" class="comment-score"></div><div class="comment-text"><p>yes thats correct, first extract message containing IMSI, i.e display filter for IMSI then extract session-id for this message.</p><p>after getting session-id, apply this as a display filter.</p><p>either write a simple code, or a unix script will solve the problem.</p></div><div id="comment-31515-info" class="comment-info"><span class="comment-age">(04 Apr '14, 08:45)</span> Sanny_D</div></div></div><div id="comment-tools-19546" class="comment-tools"></div><div class="clear"></div><div id="comment-19546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

