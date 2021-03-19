+++
type = "question"
title = "Wireshark does not work on OSX"
description = '''I know this question has been asked a million times but it just is not working on my new mac, though it worked fine on my previous mac, same model and software. It just opens and closes right away. I installed X11 and Wireshark. I can launch Wireshark just fine from the X11 terminal but it fails whe...'''
date = "2015-01-13T12:35:00Z"
lastmod = "2015-01-13T12:43:00Z"
weight = 39100
keywords = [ "osx", "xquartz", "wireshark" ]
aliases = [ "/questions/39100" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark does not work on OSX](/questions/39100/wireshark-does-not-work-on-osx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39100-score" class="post-score" title="current number of votes">0</div><span id="post-39100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know this question has been asked a million times but it just is not working on my new mac, though it worked fine on my previous mac, same model and software. It just opens and closes right away.</p><p>I installed X11 and Wireshark. I can launch Wireshark just fine from the X11 terminal but it fails when I try to launch it directly from finder. So far I have done the following.</p><ol><li>Reinstalled both the softwares. Still fails.</li><li>Moved X11 to trash, launch wireshark and then move X11 back to Applications/Utilities. Still fails.</li><li>Deleted the wireshark and wireshark-etc folders from my home directory. Still fails.</li><li>Did a "ln -s /opt/X11 /usr/X11". Still fails.</li></ol><p>I know I have the right versions since wireshark works just fine via X11 terminal but its really annoying to open X11 all the time I want to use Wireshark. Is there anything I missing here?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-xquartz" rel="tag" title="see questions tagged &#39;xquartz&#39;">xquartz</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/538b07325b7a7302b8bc302894ec8043?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zee&#39;s gravatar image" /><p><span>zee</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zee has no accepted answers">0%</span></p></div></div><div id="comments-container-39100" class="comments-container"></div><div id="comment-tools-39100" class="comment-tools"></div><div class="clear"></div><div id="comment-39100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39101"></span>

<div id="answer-container-39101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39101-score" class="post-score" title="current number of votes">2</div><span id="post-39101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried 1.99.1 or one of the 1.99.2 automated builds from <a href="https://www.wireshark.org/download/automated/osx/">https://www.wireshark.org/download/automated/osx/</a> ? The new UI is missing a few features but it should be stable and doesn't rely on X11.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '15, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-39101" class="comments-container"><span id="39102"></span><div id="comment-39102" class="comment"><div id="post-39102-score" class="comment-score"></div><div class="comment-text"><p>Phew, that worked. Thanks a lot for the help.</p></div><div id="comment-39102-info" class="comment-info"><span class="comment-age">(13 Jan '15, 12:43)</span> <span class="comment-user userinfo">zee</span></div></div></div><div id="comment-tools-39101" class="comment-tools"></div><div class="clear"></div><div id="comment-39101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

