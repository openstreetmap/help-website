+++
type = "question"
title = "Hw src addr (resolved) Column?"
description = '''A column with the type of &quot;Hw src addr (resolved)&quot; and Resolve MAC address name resolution on, I am getting a hostname on instead of a vendor_xx:xx:xx for certain devices. Not all but some. Is there somewhere that has cached this info and is &quot;helping me&quot; here? I wouldn&#x27;t think this would ever be the...'''
date = "2016-09-12T08:02:00Z"
lastmod = "2016-09-13T19:15:00Z"
weight = 55488
keywords = [ "mac" ]
aliases = [ "/questions/55488" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Hw src addr (resolved) Column?](/questions/55488/hw-src-addr-resolved-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55488-score" class="post-score" title="current number of votes">0</div><span id="post-55488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A column with the type of "Hw src addr (resolved)" and Resolve MAC address name resolution on, I am getting a hostname on instead of a vendor_xx:xx:xx for certain devices. Not all but some. Is there somewhere that has cached this info and is "helping me" here? I wouldn't think this would ever be the correct info in that column for that type of data.</p><p>Edit: Ver 2.2.0</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '16, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/0833f7ef8618ac6b7842265fbaa39861?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itsme0k&#39;s gravatar image" /><p><span>itsme0k</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itsme0k has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Sep '16, 08:52</strong> </span></p></div></div><div id="comments-container-55488" class="comments-container"><span id="55490"></span><div id="comment-55490" class="comment"><div id="post-55490-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark are you using? I experienced this long ago but I think it's since been fixed, although I can't say for sure when. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6534">bug 6534</a>.</p></div><div id="comment-55490-info" class="comment-info"><span class="comment-age">(12 Sep '16, 08:34)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-55488" class="comment-tools"></div><div class="clear"></div><div id="comment-55488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55489"></span>

<div id="answer-container-55489" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55489-score" class="post-score" title="current number of votes">0</div><span id="post-55489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is 'a stacked' name resolution result, as the MAC address gets resolved to IP address (for IP packets only, obviously), then get resolved to host name. A case could be made this 'stacked name resolution' shouldn't be applied for this column type. It takes some investigation to see if that's possible in current architecture. An enhancement bug could be filed for this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '16, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55489" class="comments-container"><span id="55545"></span><div id="comment-55545" class="comment"><div id="post-55545-score" class="comment-score"></div><div class="comment-text"><p>If it shouldn't apply to the column, why should it happen anywhere else - why not just remove the whole feature of using ARP packets to add entries to the MAC-address-to-name resolution table?</p></div><div id="comment-55545-info" class="comment-info"><span class="comment-age">(13 Sep '16, 19:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-55489" class="comment-tools"></div><div class="clear"></div><div id="comment-55489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

