+++
type = "question"
title = "Disable &quot;Software Update&quot; Pop-up On Start of Older Version of Wireshark"
description = '''Hi I am using Wireshark Version 2.0.3  But on every system startup or fresh installation of wireshark v2.0.3 I am prompted to upgrade to release v2.2.1; Because of upgrade personal configurations are overwritten. But tried to do changes in Wireshark base code in config.nmake as shown as below Line N...'''
date = "2016-10-19T11:43:00Z"
lastmod = "2016-10-22T22:41:00Z"
weight = 56509
keywords = [ "update", "wireshark" ]
aliases = [ "/questions/56509" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Disable "Software Update" Pop-up On Start of Older Version of Wireshark](/questions/56509/disable-software-update-pop-up-on-start-of-older-version-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56509-score" class="post-score" title="current number of votes">0</div><span id="post-56509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am using Wireshark Version 2.0.3 But on every system startup or fresh installation of wireshark v2.0.3 I am prompted to upgrade to release v2.2.1; Because of upgrade personal configurations are overwritten.</p><p>But tried to do changes in Wireshark base code in config.nmake as shown as below Line No. 1737 <code>WINSPARKLE_CONFIG=^#define HAVE_SOFTWARE_UPDATE 0</code> (Changed it to 0 as it is 1 by default)</p><p>Please let me know if any other changes to be taken care</p><p>Attaching Update Ref. as below <img src="https://osqa-ask.wireshark.org/upfiles/Capture_Wireshark.JPG" alt="alt text" /></p><p>Regards Dinesh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '16, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/04334c27cb629065a13d61a61b611038?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinesh%20Babu%20Sadu&#39;s gravatar image" /><p><span>Dinesh Babu ...</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinesh Babu Sadu has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Oct '16, 03:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-56509" class="comments-container"></div><div id="comment-tools-56509" class="comment-tools"></div><div class="clear"></div><div id="comment-56509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56573"></span>

<div id="answer-container-56573" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56573-score" class="post-score" title="current number of votes">1</div><span id="post-56573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dinesh Babu Sadu has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you trying to compile a Wireshark executable that doesn't support updates at all? If so, you should be able to pass -DENABLE_WINSPARKLE=OFF to cmake. If you simply want to disable software updates, go to Edit → Preferences → Advanced and disable the <code>gui.update.enabled</code> preference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '16, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-56573" class="comments-container"><span id="56585"></span><div id="comment-56585" class="comment"><div id="post-56585-score" class="comment-score"></div><div class="comment-text"><p>Thanks Gerald Combs</p><p>DENABLE_WINSPARKLE=OFF worked for my requirement</p></div><div id="comment-56585-info" class="comment-info"><span class="comment-age">(22 Oct '16, 22:41)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div></div><div id="comment-tools-56573" class="comment-tools"></div><div class="clear"></div><div id="comment-56573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

