+++
type = "question"
title = "type of attack related to the fields in the packets"
description = '''I want to classify the type of attack related to the fields in the packets. i,e one or more may be associated with some type of vulnerability that is responsible for the attack. please tell me how to check which fields are associated with the attacks. means how can i find if field is changed or modi...'''
date = "2011-01-14T23:25:00Z"
lastmod = "2011-01-15T08:57:00Z"
weight = 1758
keywords = [ "attacks", "packet" ]
aliases = [ "/questions/1758" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [type of attack related to the fields in the packets](/questions/1758/type-of-attack-related-to-the-fields-in-the-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1758-score" class="post-score" title="current number of votes">0</div><span id="post-1758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to classify the type of attack related to the fields in the packets. i,e one or more may be associated with some type of vulnerability that is responsible for the attack. please tell me how to check which fields are associated with the attacks. means how can i find if field is changed or modified is there any effect of such attacks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-attacks" rel="tag" title="see questions tagged &#39;attacks&#39;">attacks</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '11, 23:25</strong></p><img src="https://secure.gravatar.com/avatar/843cb22c1304ab3d9647bfe16800fae8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TINA&#39;s gravatar image" /><p><span>TINA</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TINA has no accepted answers">0%</span></p></div></div><div id="comments-container-1758" class="comments-container"></div><div id="comment-tools-1758" class="comment-tools"></div><div class="clear"></div><div id="comment-1758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1760"></span>

<div id="answer-container-1760" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1760-score" class="post-score" title="current number of votes">2</div><span id="post-1760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think what you want to do is to manually look for attack patterns in network packets. This is actually something that only makes sense in one particular scenario: you know there is an ongoing attack, and you have a pattern to look for.</p><p>Scanning for attacks that may or may not be there proactively is not going to work with Wireshark, simply because there are too many attacks and it is too much work / too slow. This is the reason why there are specialized devices like Intrusion Detection/Intrusion Prevention systems on the market. They have attack pattern databases that get updated frequently with new vulnerabilities to scan for, and inspect network traffic automatically based on filter sets. You may want to take a look at Snort if that is what you want: <a href="http://www.snort.org/" title="www.snort.org">www.snort.org</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '11, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1760" class="comments-container"></div><div id="comment-tools-1760" class="comment-tools"></div><div class="clear"></div><div id="comment-1760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1759"></span>

<div id="answer-container-1759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1759-score" class="post-score" title="current number of votes">0</div><span id="post-1759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's a tough one. There are a lot of possibilities. I would say look for things that are impossible. For example the same source and destination address on the wire. Incompatible TCP flags are also a sign.<br />
</p><p>You could get some direction by going through Fyodor's book on NMAP scannning.</p><p>http://www.amazon.com/Nmap-Network-Scanning-Official-Discovery/dp/0979958717</p><p>I just don't think you can get a conclusive answer to your question in a discussion forum, but you can absolutely bet some direction I suppose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '11, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></p></div></div><div id="comments-container-1759" class="comments-container"></div><div id="comment-tools-1759" class="comment-tools"></div><div class="clear"></div><div id="comment-1759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

