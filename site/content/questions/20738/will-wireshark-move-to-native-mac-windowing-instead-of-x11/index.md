+++
type = "question"
title = "will wireshark move to native mac windowing instead of X11?"
description = '''X11 bulky and the interface is pretty crappy all the way around. any chance wireshark will have a native mac GUI display written for it? thanks -avi'''
date = "2013-04-23T08:57:00Z"
lastmod = "2013-04-23T15:04:00Z"
weight = 20738
keywords = [ "mac", "gui" ]
aliases = [ "/questions/20738" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [will wireshark move to native mac windowing instead of X11?](/questions/20738/will-wireshark-move-to-native-mac-windowing-instead-of-x11)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20738-score" class="post-score" title="current number of votes">0</div><span id="post-20738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>X11 bulky and the interface is pretty crappy all the way around. any chance wireshark will have a native mac GUI display written for it?</p><p>thanks</p><p>-avi</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '13, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/39fadd5af3bbd895e70ecce2999c4c32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rotorboy&#39;s gravatar image" /><p><span>rotorboy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rotorboy has no accepted answers">0%</span></p></div></div><div id="comments-container-20738" class="comments-container"></div><div id="comment-tools-20738" class="comment-tools"></div><div class="clear"></div><div id="comment-20738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20739"></span>

<div id="answer-container-20739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20739-score" class="post-score" title="current number of votes">1</div><span id="post-20739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are no plans for a native OSX port, but work is progressing on a QT port. One of the features of QT is that it uses native widgets on each platform, but I don't know how that is achieved, or how successful that is on OSX.</p><p>Edit: After a quick scan of the docs I believe that QT on OSX doesn't use X11.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '13, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '13, 09:29</strong> </span></p></div></div><div id="comments-container-20739" class="comments-container"><span id="20750"></span><div id="comment-20750" class="comment"><div id="post-20750-score" class="comment-score"></div><div class="comment-text"><p>The toolkit that uses native widgets on each platform is <a href="http://www.wxwidgets.org">wXwidgets</a>. Qt uses native GUI code in some cases on some platforms, but it doesn't use them universally (Qt Wireshark's file access dialogs aren't native, for example; that's somewhat obvious on OS X).</p><p>It does not use X11 on OS X or Windows; it runs atop the low-level drawing layers of those OS's window systems, just as the native widget toolkits do. There's also a version that runs atop X11, where it <em>is</em> a native widget set (e.g., the native widget set used by KDE).</p></div><div id="comment-20750-info" class="comment-info"><span class="comment-age">(23 Apr '13, 15:04)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-20739" class="comment-tools"></div><div class="clear"></div><div id="comment-20739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

