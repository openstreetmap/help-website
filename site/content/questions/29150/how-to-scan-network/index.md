+++
type = "question"
title = "How to scan network?"
description = '''Hello  I have a problem. I have to scan whole network with 30 computer in our company. I was searching for some guides, but all i could find was &quot;how to hack password&quot;. I dont want that, i just want to get infromation about :  - what sides are visited  - is there any attack on our network (hackers, ...'''
date = "2014-01-25T07:22:00Z"
lastmod = "2014-01-25T14:12:00Z"
weight = 29150
keywords = [ "problem" ]
aliases = [ "/questions/29150" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to scan network?](/questions/29150/how-to-scan-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29150-score" class="post-score" title="current number of votes">0</div><span id="post-29150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I have a problem. I have to scan whole network with 30 computer in our company. I was searching for some guides, but all i could find was "how to hack password". I dont want that, i just want to get infromation about : - what sides are visited - is there any attack on our network (hackers, malware etc.) I dont want to block our workers or something i just want to know what sites are they visiting. I have no experience. Please help me, I will be grateful</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '14, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/02bfcf9ef119a526e187ef0550113711?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beginer&#39;s gravatar image" /><p><span>Beginer</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beginer has no accepted answers">0%</span></p></div></div><div id="comments-container-29150" class="comments-container"></div><div id="comment-tools-29150" class="comment-tools"></div><div class="clear"></div><div id="comment-29150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29151"></span>

<div id="answer-container-29151" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29151-score" class="post-score" title="current number of votes">0</div><span id="post-29151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While Wireshark is certainly able to show you network packets containing details about what your co-workers are doing, it is most likely not the most efficient.</p><p>If you're interested in sites visited you should take a look at the proxy logs (I do hope you have a proxy that has to be used to surf the web, do you?).</p><p>For attacks, get something like Snort or Suricata to scan the internet uplink for signatures of attacks - it is easy to setup when using the <a href="https://code.google.com/p/security-onion/">Security Onion Live CD</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '14, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29151" class="comments-container"><span id="29152"></span><div id="comment-29152" class="comment"><div id="post-29152-score" class="comment-score"></div><div class="comment-text"><p>Thanks, but there is a little problem. I had a conversation with my mentor and he said i have to do it with wireshark. I dont know why but he insisted. If someone can help me. I just want to know what filters i have to use. I think thats all.</p></div><div id="comment-29152-info" class="comment-info"><span class="comment-age">(25 Jan '14, 11:12)</span> <span class="comment-user userinfo">Beginer</span></div></div><span id="29156"></span><div id="comment-29156" class="comment"><div id="post-29156-score" class="comment-score"></div><div class="comment-text"><p>Ok, so this is not a real life task, but homework :-)</p><p>You might want to take a look at the statistics menu, e.g. the HTTP menu items. If you need to use filters, try "http.request.method" to find all requests.</p><p>Regarding attacks - you would need to have known attack patterns to find them with a filter. Snort or Suricata have patterns like that, but translating them to display filters may not be easy.</p><p>If your mentor is one of those guys who still think that attacks can be found by looking for ancient indicators like IRC traffic you could filter for that by using the "irc" display filter.</p></div><div id="comment-29156-info" class="comment-info"><span class="comment-age">(25 Jan '14, 12:30)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="29158"></span><div id="comment-29158" class="comment"><div id="post-29158-score" class="comment-score"></div><div class="comment-text"><p>IRC??? Isn't that something for guys 50+ ;-)))</p></div><div id="comment-29158-info" class="comment-info"><span class="comment-age">(25 Jan '14, 14:00)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29151" class="comment-tools"></div><div class="clear"></div><div id="comment-29151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29159"></span>

<div id="answer-container-29159" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29159-score" class="post-score" title="current number of votes">0</div><span id="post-29159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>he said i have to do it with wireshark.<br />
I dont know why but <strong>he insisted.</strong></p></blockquote><p>hm... why don't you question that?</p><p>It does not make much sense to look for 'attacks' in your network <strong>manually</strong> as there are by far too many ways to attack a system. It's like trying to calculate 563492*67543 manually although you could use a calculator. Same set of problems in both cases:</p><ul><li>the manual approach is <strong>much</strong> slower</li><li>chances to do it wrong are rather high</li><li>you won't learn anything from it, after you've done it more than twice</li></ul><p>Maybe your mentor is just testing if you are a person that follows 'the order of the master by the word', even if it does not make any sense ;-))</p><p>So, if you don't know why, ask him/her, as that will most certainly give you some hints what to look for in Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '14, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jan '14, 14:21</strong> </span></p></div></div><div id="comments-container-29159" class="comments-container"></div><div id="comment-tools-29159" class="comment-tools"></div><div class="clear"></div><div id="comment-29159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

