+++
type = "question"
title = "Wireshark setup Linux for nonroot user"
description = '''Hello there I&#x27;ve setup Wireshark using &#x27;apt-get install wireshark&#x27; and followed the setup-configuration for non-root user (see Wireshark doesn&#x27;t see my interface). What I finally did, was following: sudo groupadd wireshark sudo usermod -a -G wireshark dionysius sudo dpkg-reconfigure wireshark-common...'''
date = "2011-12-14T10:19:00Z"
lastmod = "2016-03-21T02:45:00Z"
weight = 7976
keywords = [ "interface", "setup", "linux" ]
aliases = [ "/questions/7976" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark setup Linux for nonroot user](/questions/7976/wireshark-setup-linux-for-nonroot-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7976-score" class="post-score" title="current number of votes">2</div><span id="post-7976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there</p><p>I've setup Wireshark using 'apt-get install wireshark' and followed the setup-configuration for non-root user (see <a href="http://ask.wireshark.org/questions/5861/wireshark-doesnt-see-my-interface">Wireshark doesn't see my interface</a>).</p><p>What I finally did, was following:</p><pre><code>sudo groupadd wireshark
sudo usermod -a -G wireshark dionysius
sudo dpkg-reconfigure wireshark-common (and said there YES)</code></pre><p>But after that i still cannot see any interface. What am I missing?</p><p>edit: if it does matter i'm using linux mint 12</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '11, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/f7db33c79f4d18058f12cc4705747b55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dionysius&#39;s gravatar image" /><p><span>Dionysius</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dionysius has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Dec '11, 10:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-7976" class="comments-container"></div><div id="comment-tools-7976" class="comment-tools"></div><div class="clear"></div><div id="comment-7976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="8012"></span>

<div id="answer-container-8012" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8012-score" class="post-score" title="current number of votes">7</div><span id="post-8012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dionysius has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the answer from a duplicate <a href="http://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed">post</a>.</p><p>You don't need to manually add the "wireshark" group; <code>dpkg-reconfigure</code> does it for you. Try removing the group (and your user from the group), run <code>dpkg-reconfigure</code>, add your user back to the group, and then, re-login. I verified these steps in Mint 12:</p><pre><code>$ sudo apt-get install wireshark
$ sudo dpkg-reconfigure wireshark-common 
$ sudo usermod -a -G wireshark $USER
$ gnome-session-quit --logout --no-prompt</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '11, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-8012" class="comments-container"><span id="8311"></span><div id="comment-8311" class="comment"><div id="post-8311-score" class="comment-score"></div><div class="comment-text"><p>Perfectly, that was the trick. I suggest to follow the linked post for more details.</p></div><div id="comment-8311-info" class="comment-info"><span class="comment-age">(10 Jan '12, 17:34)</span> <span class="comment-user userinfo">Dionysius</span></div></div><span id="23694"></span><div id="comment-23694" class="comment"><div id="post-23694-score" class="comment-score"></div><div class="comment-text"><p>I have tried the suggested four lines of code above. However at the same time i have "wireshark" group manually added without the "wireshark" user and the code did not work for me. After that i tried to remove the group "wireshark" with "sudo groupdel wireshark" command. Finally the code above is worked for me thank you very much. Best Regards.</p></div><div id="comment-23694-info" class="comment-info"><span class="comment-age">(10 Aug '13, 13:37)</span> <span class="comment-user userinfo">gokhankelle</span></div></div></div><div id="comment-tools-8012" class="comment-tools"></div><div class="clear"></div><div id="comment-8012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51058"></span>

<div id="answer-container-51058" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51058-score" class="post-score" title="current number of votes">2</div><span id="post-51058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Improvement on <a href="https://ask.wireshark.org/answer_link/8012/">https://ask.wireshark.org/answer_link/8012/ helloworld's answer</a></p><p>So you dont have to restart gnome, use newgrp to switch groups</p><pre><code>$ sudo apt-get install wireshark
$ sudo dpkg-reconfigure wireshark-common 
$ sudo usermod -a -G wireshark $USER
$ newgrp wireshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '16, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/cff24874f9655be6b8a602420a4f4384?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="h4ck3rm1k3&#39;s gravatar image" /><p><span>h4ck3rm1k3</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="h4ck3rm1k3 has no accepted answers">0%</span></p></div></div><div id="comments-container-51058" class="comments-container"></div><div id="comment-tools-51058" class="comment-tools"></div><div class="clear"></div><div id="comment-51058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7977"></span>

<div id="answer-container-7977" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7977-score" class="post-score" title="current number of votes">0</div><span id="post-7977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Log out and log in again. Adding a currently logged in user to a group using <code>groupadd</code> does not take effect until the user has logged out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '11, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-7977" class="comments-container"><span id="8011"></span><div id="comment-8011" class="comment"><div id="post-8011-score" class="comment-score"></div><div class="comment-text"><p>did that already multiple times (and tested now again). I don't get interfaces without sudo :(</p><p>to be sure everything i did is correct?!</p><pre><code>[email protected] ~ $ grep &quot;wireshark&quot; /etc/group
wireshark:x:1001:dionysius</code></pre></div><div id="comment-8011-info" class="comment-info"><span class="comment-age">(16 Dec '11, 07:33)</span> <span class="comment-user userinfo">Dionysius</span></div></div><span id="44639"></span><div id="comment-44639" class="comment"><div id="post-44639-score" class="comment-score"></div><div class="comment-text"><p>That was the issue for me, thanks!</p></div><div id="comment-44639-info" class="comment-info"><span class="comment-age">(30 Jul '15, 07:48)</span> <span class="comment-user userinfo">thewade</span></div></div></div><div id="comment-tools-7977" class="comment-tools"></div><div class="clear"></div><div id="comment-7977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49005"></span>

<div id="answer-container-49005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49005-score" class="post-score" title="current number of votes">0</div><span id="post-49005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>dpkg-reconfigure wireshark-common the right answer is no</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '16, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/20faa146ca1fd0e60a582e655917f866?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michele%20Pappagallo&#39;s gravatar image" /><p><span>Michele Papp...</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michele Pappagallo has no accepted answers">0%</span></p></div></div><div id="comments-container-49005" class="comments-container"></div><div id="comment-tools-49005" class="comment-tools"></div><div class="clear"></div><div id="comment-49005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

