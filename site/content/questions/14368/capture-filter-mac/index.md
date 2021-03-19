+++
type = "question"
title = "capture filter MAC"
description = '''when i write in the filter i get an error, this is what i write: &quot;ether host &#x27;macaddress&#x27;&quot;. I want to filter it so it only displays packets from the host Mac-address. And when i starts to write &#x27;ether&#x27; it doesn&#x27;t come up white anything i can use.  How can a make it capture the MAC address.'''
date = "2012-09-19T00:20:00Z"
lastmod = "2016-11-24T14:54:00Z"
weight = 14368
keywords = [ "capture", "mac", "mac-address" ]
aliases = [ "/questions/14368" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter MAC](/questions/14368/capture-filter-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14368-score" class="post-score" title="current number of votes">0</div><span id="post-14368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when i write in the filter i get an error, this is what i write: "ether host 'macaddress'". I want to filter it so it only displays packets from the host Mac-address. And when i starts to write 'ether' it doesn't come up white anything i can use. How can a make it capture the MAC address.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '12, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/9462598c34208d68f18c5fefeb323bf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Munken&#39;s gravatar image" /><p><span>Munken</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Munken has one accepted answer">100%</span></p></div></div><div id="comments-container-14368" class="comments-container"></div><div id="comment-tools-14368" class="comment-tools"></div><div class="clear"></div><div id="comment-14368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="14369"></span>

<div id="answer-container-14369" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14369-score" class="post-score" title="current number of votes">1</div><span id="post-14369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Munken has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>eth.src==MACaddress</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '12, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/9462598c34208d68f18c5fefeb323bf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Munken&#39;s gravatar image" /><p><span>Munken</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Munken has one accepted answer">100%</span></p></div></div><div id="comments-container-14369" class="comments-container"><span id="14371"></span><div id="comment-14371" class="comment"><div id="post-14371-score" class="comment-score">1</div><div class="comment-text"><p>This is a display filter for a MAC address. The other syntax "ether host MAC" is a capture filter.</p></div><div id="comment-14371-info" class="comment-info"><span class="comment-age">(19 Sep '12, 01:22)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-14369" class="comment-tools"></div><div class="clear"></div><div id="comment-14369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42778"></span>

<div id="answer-container-42778" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42778-score" class="post-score" title="current number of votes">0</div><span id="post-42778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This filter can not apply on my Wireshark 1.12.5 but</p><pre><code>ether src  00:08:15:00:08:15</code></pre><p>Display as green for Wireshark</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '15, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/200fc87e8b2461f56e2328bfad69a162?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sky%20Rover&#39;s gravatar image" /><p><span>Sky Rover</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sky Rover has no accepted answers">0%</span></p></div></div><div id="comments-container-42778" class="comments-container"></div><div id="comment-tools-42778" class="comment-tools"></div><div class="clear"></div><div id="comment-42778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57597"></span>

<div id="answer-container-57597" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57597-score" class="post-score" title="current number of votes">0</div><span id="post-57597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>eg.</p><pre><code>!(ether src xx:xx:xx:xx:xx:xx) &amp;&amp; !(ether dst xx:xx:xx:xx:xx:xx)</code></pre><p>works on Wireshark 2.2.2 as a display filter to see everything except for your own traffic</p><p>Regards A3an</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '16, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/52b2a546d225bc73ca5eec6b118c09b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A3an&#39;s gravatar image" /><p><span>A3an</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A3an has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Nov '16, 03:40</strong> </span></p></div></div><div id="comments-container-57597" class="comments-container"></div><div id="comment-tools-57597" class="comment-tools"></div><div class="clear"></div><div id="comment-57597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57620"></span>

<div id="answer-container-57620" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57620-score" class="post-score" title="current number of votes">0</div><span id="post-57620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To <em>capture</em> packets from MAC address XX:XX:XX:XX:XX:XX:</p><pre><code>ether src XX:XX:XX:XX:XX:XX</code></pre><p>If you've captured packets <em>without</em> a MAC source address filter, and want to filter the <em>display</em> to show only packets from MAC address XX:XX:XX:XX:XX:XX:</p><pre><code>eth.src == XX:XX:XX:XX:XX:XX</code></pre><p>if it's an Ethernet capture,</p><pre><code>wlan.src = XX:XX:XX:XX:XX:XX</code></pre><p>if it's an 802.11 capture, etc..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '16, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-57620" class="comments-container"></div><div id="comment-tools-57620" class="comment-tools"></div><div class="clear"></div><div id="comment-57620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

