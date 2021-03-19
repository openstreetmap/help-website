+++
type = "question"
title = "How to show all interfaces of some remote shells on wireshark?"
description = '''Hello. I&#x27;ve launch wireshark from a remote shell like the explanation in https://ask.wireshark.org/questions/10941/how-do-you-launch-wireshark-from-a-remote-shell, but I need to launch it with interfaces of two or more shells of different virtualized nodes running over linux. Somebody that knows how...'''
date = "2015-07-17T09:25:00Z"
lastmod = "2015-07-17T22:23:00Z"
weight = 44250
keywords = [ "remoteshell", "networkinterfaces" ]
aliases = [ "/questions/44250" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to show all interfaces of some remote shells on wireshark?](/questions/44250/how-to-show-all-interfaces-of-some-remote-shells-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44250-score" class="post-score" title="current number of votes">0</div><span id="post-44250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>I've launch wireshark from a remote shell like the explanation in <a href="https://ask.wireshark.org/questions/10941/how-do-you-launch-wireshark-from-a-remote-shell,">https://ask.wireshark.org/questions/10941/how-do-you-launch-wireshark-from-a-remote-shell,</a> but I need to launch it with interfaces of two or more shells of different virtualized nodes running over linux.</p><p>Somebody that knows how to do it?</p><p>I will explain it better. I have a virtual network running over linux with mininet. I open the shells of the network nodes through mininet. When the shells appears, I run the commands like explain here: <a href="https://ask.wireshark.org/questions/10941/how-do-you-launch-wireshark-from-a-remote-shell;">https://ask.wireshark.org/questions/10941/how-do-you-launch-wireshark-from-a-remote-shell;</a> but two differents wireshark windows appear, each of one with the interfaces of the corresponding node.</p><p>So, I need that the interfaces of all my nodes appear in the same wireshark window.</p><p>Please, your help.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remoteshell" rel="tag" title="see questions tagged &#39;remoteshell&#39;">remoteshell</span> <span class="post-tag tag-link-networkinterfaces" rel="tag" title="see questions tagged &#39;networkinterfaces&#39;">networkinterfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '15, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/7dfa793da8bf7ac6a94f488e023c1ded?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mjargvell&#39;s gravatar image" /><p><span>mjargvell</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mjargvell has no accepted answers">0%</span></p></div></div><div id="comments-container-44250" class="comments-container"></div><div id="comment-tools-44250" class="comment-tools"></div><div class="clear"></div><div id="comment-44250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44253"></span>

<div id="answer-container-44253" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44253-score" class="post-score" title="current number of votes">0</div><span id="post-44253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So, I need that the interfaces of all my nodes appear in the same wireshark window.</p></blockquote><p>You can use more than one <strong>-i statements</strong> on the commandline.</p><p>Example:</p><blockquote><p>wireshark -i eth0 -i eth1 -i eth2 -n ....</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44253" class="comments-container"><span id="44257"></span><div id="comment-44257" class="comment"><div id="post-44257-score" class="comment-score"></div><div class="comment-text"><p>Well, the problem is that I have one shell for every router. For example, if I have routers R1 and R2 and if I run the command wireshark -i eth0 -i eth1 in the R1 shell and wireshark -i eth0 -i eth1 in the R2 shell, Wireshark opens two differents windows, each of one with the interfaces of only one router.</p><p>I don't know if I'm explaining well. Do you get my problem?</p><p>Thanks.</p></div><div id="comment-44257-info" class="comment-info"><span class="comment-age">(17 Jul '15, 10:54)</span> <span class="comment-user userinfo">mjargvell</span></div></div><span id="44259"></span><div id="comment-44259" class="comment"><div id="post-44259-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I don't know if I'm explaining well. Do you get my problem?</p></blockquote><p>Well, let's see: Do you have 3 virtual systems (router) with Mininet that you have to telnet/ssh into and then capture on the virtual interfaces <strong>within</strong> those virtual systems?</p></div><div id="comment-44259-info" class="comment-info"><span class="comment-age">(17 Jul '15, 10:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="44260"></span><div id="comment-44260" class="comment"><div id="post-44260-score" class="comment-score"></div><div class="comment-text"><p>Yes, this is my testing environment.</p></div><div id="comment-44260-info" class="comment-info"><span class="comment-age">(17 Jul '15, 11:15)</span> <span class="comment-user userinfo">mjargvell</span></div></div><span id="44266"></span><div id="comment-44266" class="comment"><div id="post-44266-score" class="comment-score"></div><div class="comment-text"><p>O.K. that's not easy. See my answer to a similar question.</p><blockquote><p><a href="https://ask.wireshark.org/questions/13059/capturing-from-multiple-pipes">https://ask.wireshark.org/questions/13059/capturing-from-multiple-pipes</a></p></blockquote></div><div id="comment-44266-info" class="comment-info"><span class="comment-age">(17 Jul '15, 13:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="44277"></span><div id="comment-44277" class="comment"><div id="post-44277-score" class="comment-score"></div><div class="comment-text"><p>Ehh, no, that's not what he's doing.</p><p>He's using the remote shell to run Wireshark GUI <em>at the router</em>. He just exports the DISPLAY towards his management station. These multiple Wireshark GUI processes (one on each router) give multiple windows on his management station. This he would like to aggregate into one.</p></div><div id="comment-44277-info" class="comment-info"><span class="comment-age">(17 Jul '15, 22:23)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-44253" class="comment-tools"></div><div class="clear"></div><div id="comment-44253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

