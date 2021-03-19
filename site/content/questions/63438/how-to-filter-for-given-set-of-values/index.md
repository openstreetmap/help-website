+++
type = "question"
title = "how to filter for given set of values"
description = '''how to filter for given set of values Filter Example : bthci_evt.code == 0x03 or bthci_evt.code == 0x05 or bthci_evt.code == 0x01 or bthci_evt.code == 0x04 Which is very long when keep adding with other filter option.  Hence, is there any alternative option for simple filter like: bthci_evt.code in ...'''
date = "2017-08-08T01:49:00Z"
lastmod = "2017-08-11T02:35:00Z"
weight = 63438
keywords = [ "wireshark" ]
aliases = [ "/questions/63438" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to filter for given set of values](/questions/63438/how-to-filter-for-given-set-of-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63438-score" class="post-score" title="current number of votes">0</div><span id="post-63438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to filter for given set of values Filter Example : bthci_evt.code == 0x03 or bthci_evt.code == 0x05 or bthci_evt.code == 0x01 or bthci_evt.code == 0x04 Which is very long when keep adding with other filter option.</p><p>Hence, is there any alternative option for simple filter like: bthci_evt.code in {0x03 or 0x05 or 0x01 or 0x04}</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '17, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/ca400298b8385318d9ac844a64e8a40e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sghorai&#39;s gravatar image" /><p><span>sghorai</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sghorai has one accepted answer">100%</span></p></div></div><div id="comments-container-63438" class="comments-container"></div><div id="comment-tools-63438" class="comment-tools"></div><div class="clear"></div><div id="comment-63438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="63464"></span>

<div id="answer-container-63464" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63464-score" class="post-score" title="current number of votes">0</div><span id="post-63464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sghorai has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thx.. here is the already available solution that worked and is called Membership Operator:</p><p><code>bthci_evt.code in {0x03 0x05 0x01}</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '17, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/ca400298b8385318d9ac844a64e8a40e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sghorai&#39;s gravatar image" /><p><span>sghorai</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sghorai has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Aug '17, 02:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-63464" class="comments-container"><span id="63465"></span><div id="comment-63465" class="comment"><div id="post-63465-score" class="comment-score"></div><div class="comment-text"><p>As your post answers your question, I've convered it to an Answer. As it is the correct one, please mark it as a correct answer by clicking the checkmark icon next to it. No one else but the one who has posted the Question can do this.</p></div><div id="comment-63465-info" class="comment-info"><span class="comment-age">(11 Aug '17, 02:35)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-63464" class="comment-tools"></div><div class="clear"></div><div id="comment-63464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63439"></span>

<div id="answer-container-63439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63439-score" class="post-score" title="current number of votes">0</div><span id="post-63439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The syntax you look for is not supported in display filters. So your only chance to simplify the filter expression is to use logical operations like <code>bthci_evt.code &lt; 6 and bthci_evt.code != 0 or bthci_evt.code !=2</code>, but that doesn't save you too much typing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '17, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63439" class="comments-container"><span id="63443"></span><div id="comment-63443" class="comment"><div id="post-63443-score" class="comment-score"></div><div class="comment-text"><p>ok. thx for your information..</p></div><div id="comment-63443-info" class="comment-info"><span class="comment-age">(08 Aug '17, 03:52)</span> <span class="comment-user userinfo">sghorai</span></div></div></div><div id="comment-tools-63439" class="comment-tools"></div><div class="clear"></div><div id="comment-63439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63451"></span>

<div id="answer-container-63451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63451-score" class="post-score" title="current number of votes">0</div><span id="post-63451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Hence, is there any alternative option for simple filter like: bthci_evt.code in {0x03 or 0x05 or 0x01 or 0x04}</p></blockquote><p>No, but that might be a useful extension, so you could submit an enhancement request for that feature on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '17, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-63451" class="comments-container"></div><div id="comment-tools-63451" class="comment-tools"></div><div class="clear"></div><div id="comment-63451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

