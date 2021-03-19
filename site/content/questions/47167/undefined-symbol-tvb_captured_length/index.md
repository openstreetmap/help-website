+++
type = "question"
title = "Undefined symbol: tvb_captured_length"
description = '''Hi all, I&#x27;ve developed a wireshark plugin dissector following the README.plugins and I can compile my dissector without errors and I can also see how it works perfectly in my own wireshark. But now, I want to migrate my plugin dissector to another wireshark installation. How can I do that? So far, I...'''
date = "2015-11-02T10:50:00Z"
lastmod = "2015-11-05T08:45:00Z"
weight = 47167
keywords = [ "dissector", "plugin" ]
aliases = [ "/questions/47167" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Undefined symbol: tvb\_captured\_length](/questions/47167/undefined-symbol-tvb_captured_length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47167-score" class="post-score" title="current number of votes">0</div><span id="post-47167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I've developed a wireshark plugin dissector following the README.plugins and I can compile my dissector without errors and I can also see how it works perfectly in my own wireshark.</p><p>But now, I want to migrate my plugin dissector to another wireshark installation.</p><p>How can I do that?</p><p>So far, I been trying this by copying my two files</p><blockquote><p>mydissector.so</p><p>mydissector.la</p></blockquote><p>from <em>/usr/local/lib/wireshark/plugins/1.12.6</em> to the lib folder in the other wireshark installation, which is <em>/usr/lib/x86_64-linux-gnu/wireshark/libwireshark3/plugins</em>.</p><p>And when I start Wireshark, I have the following error:</p><p><em>Couldn't load module /usr/lib/x86_64-linux-gnu/wireshark/libwireshark3/plugins/netide.so: /usr/lib/x86_64-linux-gnu/wireshark/libwireshark3/plugins/my_dissector.so: undefined symbol: tvb_captured_length</em></p><p>Any help will be apreciated.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '15, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/0e44ec8438c9d8e618fb848677f0e91f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andres-beato&#39;s gravatar image" /><p><span>andres-beato</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andres-beato has no accepted answers">0%</span></p></div></div><div id="comments-container-47167" class="comments-container"></div><div id="comment-tools-47167" class="comment-tools"></div><div class="clear"></div><div id="comment-47167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47171"></span>

<div id="answer-container-47171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47171-score" class="post-score" title="current number of votes">2</div><span id="post-47171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>APIs are not stable between Wireshark major releases. In your case, you compiled your plugin with Wireshark 1.12.6 and copied it in an older Wireshark installation folder (1.10x and older versions do not have tvb_captured_length() function but instead use tvb_length()).</p><p>So if you want to run your plugin with Wireshark 1.10.x (for example) you must recompile it with the corresponding source code. Note that as the APIs can differ between releases, you can use the VERSION_MAJOR / VERSION_MINOR defines to be able to support multiple Wireshark source codes within a single plugin thanks to conditional compilation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '15, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-47171" class="comments-container"><span id="47213"></span><div id="comment-47213" class="comment"><div id="post-47213-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your answer. I've recompiled with a wireshark source code 1.10.x and it worked. But, I'd like to do the conditional compilation that you mentioned, where can I set the version major/minor to support multiple wireshark code?</p></div><div id="comment-47213-info" class="comment-info"><span class="comment-age">(04 Nov '15, 01:09)</span> <span class="comment-user userinfo">andres-beato</span></div></div><span id="47225"></span><div id="comment-47225" class="comment"><div id="post-47225-score" class="comment-score">2</div><div class="comment-text"><p>Note that the conditional compilation is only in the source code. You'll still need multiple copies of the plugin to distribute for the different versions of Wireshark you intend to support.</p><p>The version info can be picked up from config.h.</p></div><div id="comment-47225-info" class="comment-info"><span class="comment-age">(04 Nov '15, 03:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="47288"></span><div id="comment-47288" class="comment"><div id="post-47288-score" class="comment-score">1</div><div class="comment-text"><p><span>@andres-beato</span></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-47288-info" class="comment-info"><span class="comment-age">(05 Nov '15, 04:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="47294"></span><div id="comment-47294" class="comment"><div id="post-47294-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your answer <span></span><span>@grahamb</span>. I haven't seen it, until your last comment, that's why I didn't click the checkmark until now. So, thanks a lot for your answer, I appreciate it a lot, and sorry.</p></div><div id="comment-47294-info" class="comment-info"><span class="comment-age">(05 Nov '15, 08:45)</span> <span class="comment-user userinfo">andres-beato</span></div></div></div><div id="comment-tools-47171" class="comment-tools"></div><div class="clear"></div><div id="comment-47171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

