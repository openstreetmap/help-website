+++
type = "question"
title = "Zero window size ."
description = '''what are the cases in which a host supposed to send Zero window size ? '''
date = "2013-07-24T11:35:00Z"
lastmod = "2013-07-24T15:34:00Z"
weight = 23338
keywords = [ "tcp" ]
aliases = [ "/questions/23338" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Zero window size .](/questions/23338/zero-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23338-score" class="post-score" title="current number of votes">0</div><span id="post-23338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what are the cases in which a host supposed to send Zero window size ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '13, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/1abbbde534fa9dfe0dd459300adbe2e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ManojMaity&#39;s gravatar image" /><p><span>ManojMaity</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ManojMaity has no accepted answers">0%</span></p></div></div><div id="comments-container-23338" class="comments-container"></div><div id="comment-tools-23338" class="comment-tools"></div><div class="clear"></div><div id="comment-23338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23340"></span>

<div id="answer-container-23340" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23340-score" class="post-score" title="current number of votes">3</div><span id="post-23340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Define "supposed to" :-)</p><p>Zero Window is used in two situations:</p><ol><li>In a TCP reset packet. No problem at all</li><li>When the receiver can't take more data. This indicates a performance problem of the receiving hardware</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '13, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-23340" class="comments-container"><span id="23341"></span><div id="comment-23341" class="comment"><div id="post-23341-score" class="comment-score"></div><div class="comment-text"><p>Jasper, In what circumstances tcp reset packet will have a zero window size.My doubt is will zero window size on receiver triggers reset and causes connection termination?</p><p>Thanks</p></div><div id="comment-23341-info" class="comment-info"><span class="comment-age">(24 Jul '13, 12:10)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="23342"></span><div id="comment-23342" class="comment"><div id="post-23342-score" class="comment-score">1</div><div class="comment-text"><p>When a receiver closes a port, the TCP stack will send a Reset packet unless FIN has been used earlier. In the Reset packet, the window size is always 0.</p><p>A zero window value will not cause the Reset, it is the Reset that has a zero window value.</p><p>When a receiver sets its window to zero and does not go back to a window greater than zero (even after the sender tested it with Zero Window Probes) the sender will at some point give up and send a Reset. Just because it is never allowed to continue to send, and it will reach a time out depending on the OS/application.</p></div><div id="comment-23342-info" class="comment-info"><span class="comment-age">(24 Jul '13, 12:23)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="23343"></span><div id="comment-23343" class="comment"><div id="post-23343-score" class="comment-score"></div><div class="comment-text"><p>Thanks that cleared.</p></div><div id="comment-23343-info" class="comment-info"><span class="comment-age">(24 Jul '13, 12:40)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="23348"></span><div id="comment-23348" class="comment"><div id="post-23348-score" class="comment-score"></div><div class="comment-text"><p>@ Jasper 3. When an application is telling the stack to just accept xxx bytes of data and wait for further user input e.g. "save as" dialogs in browsers used to to that back in IE9 times</p></div><div id="comment-23348-info" class="comment-info"><span class="comment-age">(24 Jul '13, 15:28)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="23349"></span><div id="comment-23349" class="comment"><div id="post-23349-score" class="comment-score"></div><div class="comment-text"><p><span>@Landi</span>: I know. It's still sort of a performance "problem", because theoretically it could just accept the data and buffer it somewhere ;-)</p></div><div id="comment-23349-info" class="comment-info"><span class="comment-age">(24 Jul '13, 15:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-23340" class="comment-tools"></div><div class="clear"></div><div id="comment-23340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23339"></span>

<div id="answer-container-23339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23339-score" class="post-score" title="current number of votes">0</div><span id="post-23339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One cause i can think of:</p><p>If the receive buffer of host reaches it's maximum point then the host will notify the sender with zero window size so that sender won't send any data until further notification of window update from receiver.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '13, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jul '13, 11:38</strong> </span></p></div></div><div id="comments-container-23339" class="comments-container"></div><div id="comment-tools-23339" class="comment-tools"></div><div class="clear"></div><div id="comment-23339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

