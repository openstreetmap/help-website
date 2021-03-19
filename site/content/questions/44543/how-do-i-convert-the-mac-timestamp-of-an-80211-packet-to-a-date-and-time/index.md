+++
type = "question"
title = "How do I convert the MAC timestamp of an 802.11 packet to a date and time?"
description = '''How to convert MAC timestamp to the human date ?'''
date = "2015-07-27T12:47:00Z"
lastmod = "2015-07-27T14:30:00Z"
weight = 44543
keywords = [ "timestamp", "802.11" ]
aliases = [ "/questions/44543" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I convert the MAC timestamp of an 802.11 packet to a date and time?](/questions/44543/how-do-i-convert-the-mac-timestamp-of-an-80211-packet-to-a-date-and-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44543-score" class="post-score" title="current number of votes">0</div><span id="post-44543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to convert MAC timestamp to the human date ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/123c6382006a6bdba5dd0d8a8a7b88a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Murat%20U%C3%A7an&#39;s gravatar image" /><p><span>Murat Uçan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Murat Uçan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>27 Jul '15, 14:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-44543" class="comments-container"></div><div id="comment-tools-44543" class="comment-tools"></div><div class="clear"></div><div id="comment-44543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44545"></span>

<div id="answer-container-44545" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44545-score" class="post-score" title="current number of votes">0</div><span id="post-44545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nothing in section 10.1 "Synchronization" of <a href="https://standards.ieee.org/getieee802/download/802.11-2012.pdf">IEEE 802.11-2012</a> says anything about the Time Synchronization Function timer having a particular starting point in time, so you'd need some external form of synchronization between the MAC timestamp and some date/time timestamp.</p><p>Section 10.1.3.1 "General" says:</p><blockquote><p>Each STA shall maintain a TSF timer with modulus 264 counting in increments of microseconds. STAs expect to receive Beacon frames at a nominal rate. The interval between Beacon frames is defined by the dot11BeaconPeriod parameter of the STA. A STA sending a Beacon frame shall set the value of the Beacon frame’s timestamp so that it equals the value of the STA’s TSF timer at the time that the data symbol containing the first bit of the timestamp is transmitted to the PHY plus the transmitting STA’s delays through its local PHY from the MAC-PHY interface to its interface with the WM [e.g., antenna, light- emitting diode (LED) emission surface].</p></blockquote><p>so you <em>might</em> be able to look at Beacon frames and use the frame timestamp of the Beacon frame to determine approximately what the MAC timestamp for the beacon frame corresponds to as a date and time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '15, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44545" class="comments-container"></div><div id="comment-tools-44545" class="comment-tools"></div><div class="clear"></div><div id="comment-44545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

