+++
type = "question"
title = "Saving Captures with a filter?"
description = '''I captured traffic for a specific subnet, I need to be able to filter the output, and save the results so I can send the files off to the manufacturer. Wireshark ver. 1.4.1 Example: Capture filter: net 1.1.1.0/24 This captured a lot of packets, since I needed it to run until a failure in the hardwar...'''
date = "2011-08-03T09:35:00Z"
lastmod = "2015-10-29T01:39:00Z"
weight = 5450
keywords = [ "filter", "save" ]
aliases = [ "/questions/5450" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Saving Captures with a filter?](/questions/5450/saving-captures-with-a-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5450-score" class="post-score" title="current number of votes">0</div><span id="post-5450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured traffic for a specific subnet, I need to be able to filter the output, and save the results so I can send the files off to the manufacturer.</p><p>Wireshark ver. 1.4.1</p><p>Example:</p><p>Capture filter: net 1.1.1.0/24</p><p>This captured a lot of packets, since I needed it to run until a failure in the hardware occurred, and it is random when they fail.</p><p>Once I stopped the filter, I can then use a display filter to track one of the devices on that subnet</p><p>Example:</p><p>Display Filter: ip.addr == 1.1.1.1</p><p>The display changes to show just that IP, but I want to be able to save just those packets, to send to manufacturer.</p><p>Anyone have any ideas?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '11, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/dab91c0b4f767dbcb63700c52405970b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sulimo&#39;s gravatar image" /><p><span>Sulimo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sulimo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Feb '12, 20:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-5450" class="comments-container"></div><div id="comment-tools-5450" class="comment-tools"></div><div class="clear"></div><div id="comment-5450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5476"></span>

<div id="answer-container-5476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5476-score" class="post-score" title="current number of votes">1</div><span id="post-5476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're working in the GUI, simply click File &gt; Save As. Browse to the location where you'd like to save your file, and enter a file name. In the "Packet Range" box, select "All packets" on the left and "Displayed" at the top. Click "Save."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-5476" class="comments-container"><span id="47047"></span><div id="comment-47047" class="comment"><div id="post-47047-score" class="comment-score"></div><div class="comment-text"><p>In the Wireshark Gui (1.12.8) 'File &gt; Save As' would be 'File &gt; Export Specified Packets' to get to that "Packet Range" box. Otherwise that is the way to go.</p></div><div id="comment-47047-info" class="comment-info"><span class="comment-age">(29 Oct '15, 01:39)</span> <span class="comment-user userinfo">MOd24</span></div></div></div><div id="comment-tools-5476" class="comment-tools"></div><div class="clear"></div><div id="comment-5476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5451"></span>

<div id="answer-container-5451" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5451-score" class="post-score" title="current number of votes">0</div><span id="post-5451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nevermind, I got it.</p><p>Jasper had the answer.</p><p>tshark -r &lt;chunkfile##&gt; -R "ip.addr eq XX.XX.XX.XX" -w &lt;filteredfile##&gt;</p><p><a href="http://ask.wireshark.org/questions/1808/save-packets-from-a-filter-into-file/1810">here is the post</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/dab91c0b4f767dbcb63700c52405970b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sulimo&#39;s gravatar image" /><p><span>Sulimo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sulimo has no accepted answers">0%</span></p></div></div><div id="comments-container-5451" class="comments-container"></div><div id="comment-tools-5451" class="comment-tools"></div><div class="clear"></div><div id="comment-5451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

