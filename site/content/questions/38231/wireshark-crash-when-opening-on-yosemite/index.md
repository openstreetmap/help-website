+++
type = "question"
title = "Wireshark crash when opening on Yosemite"
description = '''Due to Apple not creating x11 Apple recommends QuartzX11. This is the version running on my Mac. OS is 10.10.1 and Wireshark and this new X11 package are current. Wireshark opens and closes immediately. Trying to learn how to use wireshark so this is making it difficult to play with packet captures ...'''
date = "2014-11-28T16:22:00Z"
lastmod = "2014-11-28T22:23:00Z"
weight = 38231
keywords = [ "lib", "error" ]
aliases = [ "/questions/38231" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crash when opening on Yosemite](/questions/38231/wireshark-crash-when-opening-on-yosemite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38231-score" class="post-score" title="current number of votes">0</div><span id="post-38231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Due to Apple not creating x11 Apple recommends QuartzX11. This is the version running on my Mac. OS is 10.10.1 and Wireshark and this new X11 package are current. Wireshark opens and closes immediately. Trying to learn how to use wireshark so this is making it difficult to play with packet captures from work.<br />
I get this error in Console...</p><p><em>Dyld Error Message: Library not loaded: /usr/X11/lib/libcairo.2.dylib Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Reason: image not found</em></p><p>Any idea's?</p><p>Bill</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lib" rel="tag" title="see questions tagged &#39;lib&#39;">lib</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '14, 16:22</strong></p><img src="https://secure.gravatar.com/avatar/0fb63e8bfffe6bddd3ea24968f415345?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wrcooke&#39;s gravatar image" /><p><span>wrcooke</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wrcooke has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Nov '14, 22:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-38231" class="comments-container"></div><div id="comment-tools-38231" class="comment-tools"></div><div class="clear"></div><div id="comment-38231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38232"></span>

<div id="answer-container-38232" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38232-score" class="post-score" title="current number of votes">0</div><span id="post-38232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Should have done this first... I deleted Quartz X11 -- downloaded it again and re installed. It seems to have installed many more lib files and Wireshark is now working. YAY!</p><p>Good to know anyway I guess!</p><p>Bill</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '14, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/0fb63e8bfffe6bddd3ea24968f415345?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wrcooke&#39;s gravatar image" /><p><span>wrcooke</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wrcooke has no accepted answers">0%</span></p></div></div><div id="comments-container-38232" class="comments-container"><span id="38233"></span><div id="comment-38233" class="comment"><div id="post-38233-score" class="comment-score">1</div><div class="comment-text"><p>Did you install X11 on Mountain Lion or Mavericks, and then upgrade to Yosemite?</p><p>If so, this is a known problem with Apple's Yosemite installer - it destroys a symbolic link that the current Wireshark package requires (because it's built to run on everything from Snow Leopard to Yosemite, and expects /usr/X11 to exist, whether it's a directory or a symbolic link to /opt/X11).</p></div><div id="comment-38233-info" class="comment-info"><span class="comment-age">(28 Nov '14, 22:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-38232" class="comment-tools"></div><div class="clear"></div><div id="comment-38232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

