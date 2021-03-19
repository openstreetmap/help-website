+++
type = "question"
title = "Filter help"
description = '''Hello, I&#x27;m a novice user. I suspect my computer&#x27;s been hacked. With help, I&#x27;ve captured a trace of my router traffic, and want to filter the results in Wireshark. What should I enter in the filter field? I&#x27;m trying to achieve two things:  filter out &#x27;noise&#x27; (anything that would definitely NOT be rel...'''
date = "2013-05-08T04:30:00Z"
lastmod = "2013-05-08T20:28:00Z"
weight = 21021
keywords = [ "beginner", "filters" ]
aliases = [ "/questions/21021" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter help](/questions/21021/filter-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21021-score" class="post-score" title="current number of votes">0</div><span id="post-21021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm a novice user. I suspect my computer's been hacked. With help, I've captured a trace of my router traffic, and want to filter the results in Wireshark.</p><p>What should I enter in the filter field? I'm trying to achieve two things:</p><ol><li>filter out 'noise' (anything that would definitely NOT be related to suspicious activity)</li><li>filter out traffic on my 'guest' account so I only see traffic on 'my wifi' account.</li></ol><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '13, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/c838057bd28cfa50e894a06b9136771d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="melanie&#39;s gravatar image" /><p><span>melanie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="melanie has no accepted answers">0%</span></p></div></div><div id="comments-container-21021" class="comments-container"></div><div id="comment-tools-21021" class="comment-tools"></div><div class="clear"></div><div id="comment-21021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21023"></span>

<div id="answer-container-21023" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21023-score" class="post-score" title="current number of votes">0</div><span id="post-21023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is not going to be simple. To determine what is malicious traffic and what isn't you need to know how "good" traffic looks like. And that is depending on what your PC is supposed to do on the network. For example of you're not using a web browser while you capture but you see HTTP traffic it could be hidden communication, but it may also be a background patch mechanism at work. So first you need to spot traffic that you can't explain, then find out what program it was caused by, and determine if it is a good or bad program.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '13, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21023" class="comments-container"><span id="21034"></span><div id="comment-21034" class="comment"><div id="post-21034-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper.</p><p>I did have a browser open.</p><p>I guess I'm wondering if there are some obvious things I can filter out because they are never 'bad'.</p><p>Also, any help on question 2 would be great. (filtering out traffic to and from one of two wifi accounts.)</p></div><div id="comment-21034-info" class="comment-info"><span class="comment-age">(08 May '13, 08:00)</span> <span class="comment-user userinfo">melanie</span></div></div><span id="21045"></span><div id="comment-21045" class="comment"><div id="post-21045-score" class="comment-score"></div><div class="comment-text"><p>Almost any protocol can be abused, but in most cases you could filter out any traffic that runs between IPs you trust, e.g. IPs within your own network. A typical filter could be something like "not (ip.src==192.168.1.0/24 and ip.dst==192.168.1.0/24)", which would filter out any communication of IPs both belonging to the 192.168.1.0/24 subnet. There are some cases where malware relays communication through the local subnet, but that is very rare and usually concerns enterprise/government level targets.</p><p>Filtering on accounts is kinda hard to do. How do you differentiate between "guest" accounts and your Wifi Account? Can you base it on devices/MAC addresses?</p></div><div id="comment-21045-info" class="comment-info"><span class="comment-age">(08 May '13, 20:28)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-21023" class="comment-tools"></div><div class="clear"></div><div id="comment-21023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

