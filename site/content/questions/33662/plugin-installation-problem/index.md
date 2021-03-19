+++
type = "question"
title = "Plugin Installation Problem"
description = '''I have a plugin and I need to install it to my wireshark edition. I have follower thr readme.plugins document and executed nmake -f makefile.nmake command from command prompt and it runs sucessfully but I cant see my plugin in  Help-&amp;gt;About wireshark-&amp;gt; plugins section. Where am I going wrong?'''
date = "2014-06-11T11:08:00Z"
lastmod = "2014-06-11T11:27:00Z"
weight = 33662
keywords = [ "plugin", "wireshark" ]
aliases = [ "/questions/33662" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Plugin Installation Problem](/questions/33662/plugin-installation-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33662-score" class="post-score" title="current number of votes">0</div><span id="post-33662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a plugin and I need to install it to my wireshark edition. I have follower thr readme.plugins document and executed nmake -f makefile.nmake command from command prompt and it runs sucessfully but I cant see my plugin in Help-&gt;About wireshark-&gt; plugins section. Where am I going wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '14, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/a9a254ac482208f766093c0f9c144364?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aman&#39;s gravatar image" /><p><span>aman</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aman has no accepted answers">0%</span></p></div></div><div id="comments-container-33662" class="comments-container"><span id="33663"></span><div id="comment-33663" class="comment"><div id="post-33663-score" class="comment-score"></div><div class="comment-text"><p>How are you running your new version, from the wireshark-gtk2 directory in your build tree, or via an installer you have built?</p><p>You should also state your OS and Wireshark version number.</p></div><div id="comment-33663-info" class="comment-info"><span class="comment-age">(11 Jun '14, 11:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-33662" class="comment-tools"></div><div class="clear"></div><div id="comment-33662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33665"></span>

<div id="answer-container-33665" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33665-score" class="post-score" title="current number of votes">2</div><span id="post-33665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aman has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Run it from the build directory by typing</p><p>Wireshark-GTK2\wireshark</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '14, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-33665" class="comments-container"><span id="33667"></span><div id="comment-33667" class="comment"><div id="post-33667-score" class="comment-score"></div><div class="comment-text"><p>Thanks it worked..</p></div><div id="comment-33667-info" class="comment-info"><span class="comment-age">(11 Jun '14, 11:27)</span> <span class="comment-user userinfo">aman</span></div></div></div><div id="comment-tools-33665" class="comment-tools"></div><div class="clear"></div><div id="comment-33665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33664"></span>

<div id="answer-container-33664" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33664-score" class="post-score" title="current number of votes">1</div><span id="post-33664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to copy the compiled dll in either the global or personal plugins folder. You can locate them by clicking on Help -&gt; About Wireshark -&gt; Folders tab.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '14, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-33664" class="comments-container"></div><div id="comment-tools-33664" class="comment-tools"></div><div class="clear"></div><div id="comment-33664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

