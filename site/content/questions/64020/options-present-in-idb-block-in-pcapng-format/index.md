+++
type = "question"
title = "Options present in IDB block in Pcapng format"
description = '''I am unable to view the options added for Interface Description Block (IDB) for the below options:  - if_name  - if_speed Please let me know where this options would be displayed on wireshark. Thanks, Subhash'''
date = "2017-10-18T22:41:00Z"
lastmod = "2017-10-26T00:32:00Z"
weight = 64020
keywords = [ "pcapng" ]
aliases = [ "/questions/64020" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Options present in IDB block in Pcapng format](/questions/64020/options-present-in-idb-block-in-pcapng-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64020-score" class="post-score" title="current number of votes">0</div><span id="post-64020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to view the options added for Interface Description Block (IDB) for the below options: - if_name - if_speed Please let me know where this options would be displayed on wireshark. Thanks, Subhash</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '17, 22:41</strong></p><img src="https://secure.gravatar.com/avatar/38a15fccab6827bd3319fe93cf058e1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subhashmohan&#39;s gravatar image" /><p><span>subhashmohan</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subhashmohan has no accepted answers">0%</span></p></div></div><div id="comments-container-64020" class="comments-container"></div><div id="comment-tools-64020" class="comment-tools"></div><div class="clear"></div><div id="comment-64020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64022"></span>

<div id="answer-container-64022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64022-score" class="post-score" title="current number of votes">0</div><span id="post-64022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The interface name is expressed in the field frame.interface_name. The interface speed I'm not sure that can be shown somehow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '17, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-64022" class="comments-container"><span id="64023"></span><div id="comment-64023" class="comment"><div id="post-64023-score" class="comment-score"></div><div class="comment-text"><p>I don't think the if_speed option is written to the IDB by any capture tool so far. I checked some of my pcapng files and they don't have it.</p><p><a href="https://ask.wireshark.org/users/33585/subhashmohan">@subhashmohan</a>: you can use TraceWrangler to show the PCAPng structure by adding a pcapng file to the file list, select it and go to the "PCAPng Structure" tab at the bottom. TraceWrangler is available here: <a href="https://www.tracewrangler.com">https://www.tracewrangler.com</a></p></div><div id="comment-64023-info" class="comment-info"><span class="comment-age">(19 Oct '17, 00:29)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="64025"></span><div id="comment-64025" class="comment"><div id="post-64025-score" class="comment-score"></div><div class="comment-text"><p>Wireshark can also show the capture file structure (not sure if ALL formats are supported) using the View | Reload as File Format/Capture menu item.</p><p>This is also bound to Ctrl + Shift + F, but for me at least, that seems only to work in one direction, packets -&gt; File Format.</p></div><div id="comment-64025-info" class="comment-info"><span class="comment-age">(19 Oct '17, 02:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="64214"></span><div id="comment-64214" class="comment"><div id="post-64214-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answers</p></div><div id="comment-64214-info" class="comment-info"><span class="comment-age">(26 Oct '17, 00:32)</span> <span class="comment-user userinfo">subhashmohan</span></div></div></div><div id="comment-tools-64022" class="comment-tools"></div><div class="clear"></div><div id="comment-64022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

