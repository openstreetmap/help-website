+++
type = "question"
title = "Network storm"
description = '''Hi, we seem to be having a network storm every day at 1pm that lasts for an hour, it generates 140k of traffic to every user. Do I have to setup a filter to try and identify? I am new to this so I have no idea where to start! Steve'''
date = "2011-03-09T11:40:00Z"
lastmod = "2014-01-27T02:26:00Z"
weight = 2736
keywords = [ "packets" ]
aliases = [ "/questions/2736" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Network storm](/questions/2736/network-storm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2736-score" class="post-score" title="current number of votes">0</div><span id="post-2736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, we seem to be having a network storm every day at 1pm that lasts for an hour, it generates 140k of traffic to every user. Do I have to setup a filter to try and identify? I am new to this so I have no idea where to start!</p><p>Steve</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '11, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/11776f84d6e8d1f0bd2c24fd9c1bf602?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevewarden0&#39;s gravatar image" /><p><span>stevewarden0</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevewarden0 has no accepted answers">0%</span></p></div></div><div id="comments-container-2736" class="comments-container"></div><div id="comment-tools-2736" class="comment-tools"></div><div class="clear"></div><div id="comment-2736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2738"></span>

<div id="answer-container-2738" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2738-score" class="post-score" title="current number of votes">2</div><span id="post-2738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you have a storm, no need to filter, it will stand out in the tracefile :-)<br />
</p><p>Just look for stuff that's repeating itself. Watch for the "IP TTL" and "IP id" to see whether it is a L2 storm (IP TTL and IP id stay the same) or a L3 loop ("IP TTL" decreases and "IP id" changes).</p><p>Look at the source mac and IP address to track the source of the storm and then look at the L2 / L3 design of your network to find your loop.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '11, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div></div><div id="comments-container-2738" class="comments-container"><span id="16763"></span><div id="comment-16763" class="comment"><div id="post-16763-score" class="comment-score"></div><div class="comment-text"><p>Wouldn't L3 loop eventually die out when TTL dropping down to zero?</p></div><div id="comment-16763-info" class="comment-info"><span class="comment-age">(11 Dec '12, 00:41)</span> <span class="comment-user userinfo">xkgt</span></div></div><span id="29175"></span><div id="comment-29175" class="comment"><div id="post-29175-score" class="comment-score"></div><div class="comment-text"><p>Can share the string to capture "IP TTL" and "IP id"?</p></div><div id="comment-29175-info" class="comment-info"><span class="comment-age">(27 Jan '14, 02:26)</span> <span class="comment-user userinfo">gamermic</span></div></div></div><div id="comment-tools-2738" class="comment-tools"></div><div class="clear"></div><div id="comment-2738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16777"></span>

<div id="answer-container-16777" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16777-score" class="post-score" title="current number of votes">1</div><span id="post-16777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the symptom can be observed "every day" it sounds like a time-triggered batch job. We have observed similar behavior caused for example by</p><ul><li>Software distribution / updates</li><li>Virus pattern update</li><li>Hardware / software inventory recording</li><li>Network management systems collecting information</li></ul><p>Can you post traffic for a single workstation on cloud shark?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '12, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-16777" class="comments-container"></div><div id="comment-tools-16777" class="comment-tools"></div><div class="clear"></div><div id="comment-16777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

