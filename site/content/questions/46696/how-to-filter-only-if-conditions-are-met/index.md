+++
type = "question"
title = "How to filter only if conditions are met?"
description = '''Hi all, need some help with Wireshark, I created the below filter,  (ip.src==10.70.40.56) || (ip.src==10.70.40.82) || (ip.dst==10.70.40.56) || (ip.dst==10.70.40.82) || (ip.dst==10.101.30.48) || (ip.src==10.101.30.48) || (eth.addr ==D0:87:E2:23:E0:0E) However it shows everything containing these IP&#x27;s...'''
date = "2015-10-19T07:52:00Z"
lastmod = "2015-10-19T16:15:00Z"
weight = 46696
keywords = [ "filtering", "condition", "if" ]
aliases = [ "/questions/46696" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter only if conditions are met?](/questions/46696/how-to-filter-only-if-conditions-are-met)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46696-score" class="post-score" title="current number of votes">0</div><span id="post-46696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, need some help with Wireshark,</p><p>I created the below filter,</p><p>(ip.src==10.70.40.56) || (ip.src==10.70.40.82) || (ip.dst==10.70.40.56) || (ip.dst==10.70.40.82) || (ip.dst==10.101.30.48) || (ip.src==10.101.30.48) || (eth.addr ==D0:87:E2:23:E0:0E)</p><p>However it shows everything containing these IP's, I want wireshark to only display output if all of the above conditions are met, so if the mac address condition is not met or another condition is not met I don't want to see it in the output. I only want it to be shown in the output if all the above conditions are met, does anyone know how to do this? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-condition" rel="tag" title="see questions tagged &#39;condition&#39;">condition</span> <span class="post-tag tag-link-if" rel="tag" title="see questions tagged &#39;if&#39;">if</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/d2bd3ee56e5ca304e5f8dc0e561043b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sheraz35&#39;s gravatar image" /><p><span>sheraz35</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sheraz35 has no accepted answers">0%</span></p></div></div><div id="comments-container-46696" class="comments-container"></div><div id="comment-tools-46696" class="comment-tools"></div><div class="clear"></div><div id="comment-46696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="46697"></span>

<div id="answer-container-46697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46697-score" class="post-score" title="current number of votes">0</div><span id="post-46697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Change the logical or's (||) to logical and's (&amp;&amp;).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-46697" class="comments-container"><span id="46698"></span><div id="comment-46698" class="comment"><div id="post-46698-score" class="comment-score"></div><div class="comment-text"><p>That will not work. The expression has multiple ip.src and ip.dst filters. If all OR's are replaced by AND's, then nothing will be displayed. For example,</p><p>(ip.src==10.70.40.56) &amp;&amp; (ip.src==10.70.40.82) ==&gt; how can a packet have 2 IP sources (assuming no tunneling)?</p><p><span>@sheraz35</span> = you will need to do a combination of AND's and OR's to get you need.</p></div><div id="comment-46698-info" class="comment-info"><span class="comment-age">(19 Oct '15, 08:33)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="46705"></span><div id="comment-46705" class="comment"><div id="post-46705-score" class="comment-score"></div><div class="comment-text"><p>Amato_C, you are, of course, right. I read (hastily) "I want Wireshark to only display output if all of the above conditions are met." mrEEDE's response is probably what is wanted.</p></div><div id="comment-46705-info" class="comment-info"><span class="comment-age">(19 Oct '15, 11:46)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-46697" class="comment-tools"></div><div class="clear"></div><div id="comment-46697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46702"></span>

<div id="answer-container-46702" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46702-score" class="post-score" title="current number of votes">0</div><span id="post-46702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This <em>may</em> be what you want to achieve ...</p><pre><code>eth.addr ==D0:87:E2:23:E0:0E &amp;&amp; (ip.addr==10.70.40.56 || ip.addr==10.70.40.82 || ip.addr==10.70.40.82)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-46702" class="comments-container"></div><div id="comment-tools-46702" class="comment-tools"></div><div class="clear"></div><div id="comment-46702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46727"></span>

<div id="answer-container-46727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46727-score" class="post-score" title="current number of votes">0</div><span id="post-46727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While thinking about your description, I can see two 'plausible' filters.</p><p><strong>Filter #1</strong>: communication between the IP addresses (src and dst) addresses and/or the MAC address</p><blockquote><p>eth.addr ==D0:87:E2:23:E0:0E or ((ip.addr == 10.70.40.56 or ip.addr == 10.70.40.82 or ip.addr == 10.101.30.48 ) and (ip.addr == 10.70.40.56 or ip.addr == 10.70.40.82 or ip.addr == 10.101.30.48))</p></blockquote><p>But that filter does not make much sense to me , so I came up with the second filter.</p><p><strong>Filter #2:</strong> communication between the addresses 10.70.40.x &lt;-&gt; 10.101.30.48 through a certain gateway D0:87:E2:23:E0:0E</p><blockquote><p>eth.addr == D0:87:E2:23:E0:0E and (ip.addr == 10.101.30.48 and (ip.addr == 10.70.40.56 or ip.addr == 10.70.40.82))</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Oct '15, 16:53</strong> </span></p></div></div><div id="comments-container-46727" class="comments-container"></div><div id="comment-tools-46727" class="comment-tools"></div><div class="clear"></div><div id="comment-46727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

