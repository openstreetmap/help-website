+++
type = "question"
title = "Installing two separate instances of Wireshark  on the same machine"
description = '''Question: I wonder whether there is a way to have two different version (or the same version) of Wireshark on the same machine. My problem is that I need to change plugins files every time when I change version of releases of software for which ethereals are captured. '''
date = "2010-09-25T13:47:00Z"
lastmod = "2010-09-27T04:18:00Z"
weight = 321
keywords = [ "instances", "version" ]
aliases = [ "/questions/321" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Installing two separate instances of Wireshark on the same machine](/questions/321/installing-two-separate-instances-of-wireshark-on-the-same-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-321-score" class="post-score" title="current number of votes">1</div><span id="post-321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Question: I wonder whether there is a way to have two different version (or the same version) of Wireshark on the same machine.</p><p>My problem is that I need to change plugins files every time when I change version of releases of software for which ethereals are captured.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-instances" rel="tag" title="see questions tagged &#39;instances&#39;">instances</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '10, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/0c58689d728ef6ca80b00e7a9cd807d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shekhar&#39;s gravatar image" /><p><span>shekhar</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shekhar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '10, 06:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-321" class="comments-container"></div><div id="comment-tools-321" class="comment-tools"></div><div class="clear"></div><div id="comment-321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="323"></span>

<div id="answer-container-323" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-323-score" class="post-score" title="current number of votes">3</div><span id="post-323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes - you can have multiple versions installed on the same machine. When you go through the installation, choose a different directory - for example:</p><ul><li>install version 1.4.0 in a directory called wireshark140</li><li>install version 1.2.9 in a directory called wireshark129</li></ul><p>Each will have a separate plugin directory under the wireshark folder. I just checked (at least in the Windows version) to see if they pull from different plugin directories and they appear to do so which is good.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '10, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-323" class="comments-container"><span id="328"></span><div id="comment-328" class="comment"><div id="post-328-score" class="comment-score">1</div><div class="comment-text"><p>This <em>should</em> work fine with the following stipulations:</p><ul><li>You should install into separate directories, as @lchappell points out.</li><li>Only the most recently installed version will be recognized by the Wireshark uninstaller and Add/Remove Programs.</li></ul></div><div id="comment-328-info" class="comment-info"><span class="comment-age">(25 Sep '10, 16:16)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-323" class="comment-tools"></div><div class="clear"></div><div id="comment-323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="331"></span>

<div id="answer-container-331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-331-score" class="post-score" title="current number of votes">1</div><span id="post-331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I usually use the Wireshark Portable Versions to do this, they should work completely self-contained. Of course they still have to go into separate base directories. Installing multiple "normal" versions should still share the configuration settings and profiles, so if you don't want that, go portable. And kicking them off the system is easy too: just delete their installation directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '10, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-331" class="comments-container"></div><div id="comment-tools-331" class="comment-tools"></div><div class="clear"></div><div id="comment-331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="335"></span>

<div id="answer-container-335" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-335-score" class="post-score" title="current number of votes">1</div><span id="post-335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If it's about differentiating between the personal configurations of your installations (which includes your personal plugins) you can also use the command line parameter <em>-P persconf:&lt;path&gt;</em>. That save you multiple installs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '10, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-335" class="comments-container"></div><div id="comment-tools-335" class="comment-tools"></div><div class="clear"></div><div id="comment-335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

