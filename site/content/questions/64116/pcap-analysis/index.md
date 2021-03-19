+++
type = "question"
title = "Pcap analysis"
description = '''Just another Pcap, is there anything malicious with this or is it normal traffic?  https://drive.google.com/file/d/0B1VcVVkZTYTJdGJnSXVZdm9qaWM/view?usp=sharing'''
date = "2017-10-23T09:59:00Z"
lastmod = "2017-10-23T22:14:00Z"
weight = 64116
keywords = [ "malicious", "pcap" ]
aliases = [ "/questions/64116" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Pcap analysis](/questions/64116/pcap-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64116-score" class="post-score" title="current number of votes">0</div><span id="post-64116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just another Pcap, is there anything malicious with this or is it normal traffic?</p><p><a href="https://drive.google.com/file/d/0B1VcVVkZTYTJdGJnSXVZdm9qaWM/view?usp=sharing">https://drive.google.com/file/d/0B1VcVVkZTYTJdGJnSXVZdm9qaWM/view?usp=sharing</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malicious" rel="tag" title="see questions tagged &#39;malicious&#39;">malicious</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '17, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/42a40141589fe4f48f4a73360ee6474f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subb148&#39;s gravatar image" /><p><span>subb148</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subb148 has no accepted answers">0%</span></p></div></div><div id="comments-container-64116" class="comments-container"></div><div id="comment-tools-64116" class="comment-tools"></div><div class="clear"></div><div id="comment-64116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64135"></span>

<div id="answer-container-64135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64135-score" class="post-score" title="current number of votes">0</div><span id="post-64135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Based on your other question I get a definite feeling this is a homework assignment.</p><p>Having said that, as an educational opportunity, if you right-click on the TCP stream and select "follow TCP stream" you can see that most of this trace is an ASCII terminal application where a user is issuing Linux commands. They are as follows, and can be ignored (unless a person logging into that server and issuing these commands is nefarious):</p><p><code>ls -la cd .. ls cd selinux ls ls -la</code></p><p>For the rest of it, you have a unicast DHCP request (looks non-evil), and ARP traffic (where the replies don't contradict each other at least). So, nothing "scanny" happening there, and nothing that particularly strikes me as malicious on the face of it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '17, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-64135" class="comments-container"></div><div id="comment-tools-64135" class="comment-tools"></div><div class="clear"></div><div id="comment-64135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

