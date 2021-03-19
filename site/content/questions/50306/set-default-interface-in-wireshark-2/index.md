+++
type = "question"
title = "Set default interface in Wireshark 2"
description = '''In Wireshark 2.0.1, OS X 10.8.5, when I open the application and hit ⌘E it doesn&#x27;t start a capture with my main interface en0, but I have to hit ⇥⇥↓↑ to select it first. I couldn&#x27;t find a default interface setting in Preferences &amp;gt; Advanced. I know I can use wireshark -k -i en0 but I wondered if t...'''
date = "2016-02-18T07:37:00Z"
lastmod = "2016-02-18T12:31:00Z"
weight = 50306
keywords = [ "interface", "wireshark-2.0", "capture-defaults" ]
aliases = [ "/questions/50306" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Set default interface in Wireshark 2](/questions/50306/set-default-interface-in-wireshark-2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50306-score" class="post-score" title="current number of votes">0</div><span id="post-50306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark 2.0.1, OS X 10.8.5, when I open the application and hit ⌘E it doesn't start a capture with my main interface <code>en0</code>, but I have to hit ⇥⇥↓↑ to select it first. I couldn't find a default interface setting in Preferences &gt; Advanced. I know I can use <code>wireshark -k -i en0</code> but I wondered if there's another way to this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-wireshark-2.0" rel="tag" title="see questions tagged &#39;wireshark-2.0&#39;">wireshark-2.0</span> <span class="post-tag tag-link-capture-defaults" rel="tag" title="see questions tagged &#39;capture-defaults&#39;">capture-defaults</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '16, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/24e4a6e495369e0c1ba6a2466a8a720b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wsk&#39;s gravatar image" /><p><span>wsk</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wsk has no accepted answers">0%</span></p></div></div><div id="comments-container-50306" class="comments-container"></div><div id="comment-tools-50306" class="comment-tools"></div><div class="clear"></div><div id="comment-50306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50312"></span>

<div id="answer-container-50312" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50312-score" class="post-score" title="current number of votes">1</div><span id="post-50312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wsk has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about Preferences -&gt; Capture. That's where you set the default interface. Restart Wireshark and go ahead.[1]</p><p>[1] That restart shouldn't be required IMHO.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '16, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-50312" class="comments-container"><span id="50313"></span><div id="comment-50313" class="comment"><div id="post-50313-score" class="comment-score"></div><div class="comment-text"><p>It should put the interfaces in the order in which libpcap returns them, so that the first interface is likely to be the main interface IMHO.</p></div><div id="comment-50313-info" class="comment-info"><span class="comment-age">(18 Feb '16, 12:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="50314"></span><div id="comment-50314" class="comment"><div id="post-50314-score" class="comment-score"></div><div class="comment-text"><p>:doublefacepalm: thanks!</p></div><div id="comment-50314-info" class="comment-info"><span class="comment-age">(18 Feb '16, 12:31)</span> <span class="comment-user userinfo">wsk</span></div></div></div><div id="comment-tools-50312" class="comment-tools"></div><div class="clear"></div><div id="comment-50312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

